#!/usr/bin/env python3
"""One-pass talking-head editor: silence removal + last-best-take selection.

The analysis stage transcribes the whole recording, groups nearby repeated takes,
and creates one edit decision list. FFmpeg then performs a single final encode.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Sequence


TERMINAL_RE = re.compile(r"[.!?][\"')\]]*$")
SOFT_BREAK_RE = re.compile(r"[,;:.!?][\"')\]]*$")
TOKEN_RE = re.compile(r"[a-z0-9]+(?:'[a-z0-9]+)?")
DEFAULT_RESTART_MARKERS = ("cut cut", "start again", "start over", "one more time")


@dataclass(frozen=True)
class Word:
    start: float
    end: float
    text: str
    probability: float = 1.0


@dataclass
class Take:
    index: int
    start: float
    end: float
    text: str
    words: list[Word] = field(repr=False)
    keep: bool = True
    reason: str = "unique take"
    duplicate_of: int | None = None

    @property
    def confidence(self) -> float:
        if not self.words:
            return 0.0
        return sum(word.probability for word in self.words) / len(self.words)


def fail(message: str) -> None:
    raise SystemExit(f"Error: {message}")


def run(command: Sequence[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(command), check=True, text=True,
        capture_output=capture,
    )


def normalize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def transcript_words(data: dict) -> list[Word]:
    words: list[Word] = []
    for segment in data.get("segments", []):
        segment_words = segment.get("words") or []
        if segment_words:
            for item in segment_words:
                start = item.get("start")
                end = item.get("end")
                if start is None or end is None:
                    continue
                text = str(item.get("word", item.get("text", ""))).strip()
                if text:
                    words.append(Word(float(start), float(end), text, float(item.get("probability", 1.0))))
        else:
            text = str(segment.get("text", "")).strip()
            start = segment.get("start")
            end = segment.get("end")
            if text and start is not None and end is not None:
                words.append(Word(float(start), float(end), text))
    return sorted(words, key=lambda word: (word.start, word.end))


def transcribe(input_path: Path, model_name: str, language: str | None) -> dict:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        fail("faster-whisper is not installed. Run: pip install -r requirements.txt")

    print(f"Transcribing once with faster-whisper ({model_name})…", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(input_path),
        language=language,
        beam_size=5,
        vad_filter=True,
        word_timestamps=True,
        condition_on_previous_text=False,
    )
    serialized = []
    for segment in segments:
        serialized.append({
            "start": round(segment.start, 3),
            "end": round(segment.end, 3),
            "text": segment.text.strip(),
            "words": [
                {
                    "start": round(word.start, 3),
                    "end": round(word.end, 3),
                    "word": word.word.strip(),
                    "probability": round(word.probability, 6),
                }
                for word in (segment.words or [])
            ],
        })
    return {
        "language": info.language,
        "duration": info.duration,
        "segments": serialized,
    }


def split_inline_restarts(group: list[Word]) -> list[list[Word]]:
    """Split when the opening 2-5 word phrase is repeated within the same take."""
    if len(group) < 5:
        return [group]
    tokens = [normalize(word.text)[0] if normalize(word.text) else "" for word in group]
    for width in range(min(5, len(group) // 2), 1, -1):
        prefix = tokens[:width]
        for index in range(width, min(len(group) - width + 1, 15)):
            if tokens[index:index + width] == prefix:
                return [group[:index], *split_inline_restarts(group[index:])]
    return [group]


def build_takes(words: Sequence[Word], take_gap: float, sentence_gap: float) -> list[Take]:
    if not words:
        return []
    groups: list[list[Word]] = []
    current: list[Word] = [words[0]]
    for word in words[1:]:
        gap = max(0.0, word.start - current[-1].end)
        phrase_break = bool(SOFT_BREAK_RE.search(current[-1].text))
        if gap >= take_gap or (phrase_break and gap >= sentence_gap):
            groups.append(current)
            current = [word]
        else:
            current.append(word)
    groups.append(current)
    groups = [part for group in groups for part in split_inline_restarts(group) if part]

    takes = []
    for index, group in enumerate(groups):
        text = " ".join(word.text for word in group).strip()
        takes.append(Take(index, group[0].start, group[-1].end, text, list(group)))
    return takes


def longest_common_prefix(left: Sequence[str], right: Sequence[str]) -> int:
    count = 0
    for a, b in zip(left, right):
        if a != b:
            break
        count += 1
    return count


def duplicate_score(left: Take, right: Take) -> tuple[float, dict[str, float]]:
    a = normalize(left.text)
    b = normalize(right.text)
    if min(len(a), len(b)) < 3:
        return 0.0, {}
    ratio = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    prefix = longest_common_prefix(a, b) / max(1, min(len(a), len(b)))
    common = len(set(a) & set(b)) / max(1, len(set(a) | set(b)))
    matcher = difflib.SequenceMatcher(None, a, b, autojunk=False)
    longest = matcher.find_longest_match(0, len(a), 0, len(b)).size / min(len(a), len(b))
    score = max(ratio, 0.62 * prefix + 0.38 * longest, 0.55 * longest + 0.45 * common)
    return score, {"ratio": ratio, "prefix": prefix, "jaccard": common, "coverage": longest}


def looks_repeated(left: Take, right: Take, threshold: float) -> bool:
    score, parts = duplicate_score(left, right)
    if not parts:
        return False
    a = normalize(left.text)
    b = normalize(right.text)
    prefix_words = longest_common_prefix(a, b)
    prefix_restart = prefix_words >= 3 and parts["coverage"] >= 0.58
    near_duplicate = score >= threshold and (
        parts["coverage"] >= 0.50 or parts["jaccard"] >= 0.55
    )
    contained_retry = parts["coverage"] >= 0.82 and parts["jaccard"] >= 0.46
    return prefix_restart or near_duplicate or contained_retry


def mark_restart_phrases(takes: list[Take], markers: Iterable[str]) -> None:
    normalized_markers = [normalize(marker) for marker in markers]
    for take in takes:
        tokens = normalize(take.text)
        for marker in normalized_markers:
            width = len(marker)
            if width and any(tokens[i:i + width] == marker for i in range(len(tokens) - width + 1)):
                take.keep = False
                take.reason = "restart marker"
                previous = next((item for item in reversed(takes[:take.index]) if item.keep), None)
                if previous:
                    previous.keep = False
                    previous.reason = f"superseded before restart marker at take {take.index + 1}"
                    previous.duplicate_of = take.index
                break


def mark_orphan_restarts(takes: list[Take]) -> None:
    """Drop a one/two-word opening when the next take restarts with it."""
    for index, take in enumerate(takes[:-1]):
        if not take.keep:
            continue
        tokens = normalize(take.text)
        if not 0 < len(tokens) <= 2:
            continue
        for later in takes[index + 1:index + 4]:
            later_tokens = normalize(later.text)
            if later.start - take.end <= 8 and later_tokens[:len(tokens)] == tokens:
                take.keep = False
                take.reason = f"incomplete opening; restarted in take {later.index + 1}"
                take.duplicate_of = later.index
                break


def prefer_later_take(earlier: Take, later: Take) -> bool:
    """Prefer the last take unless it is clearly incomplete or unreliable."""
    earlier_tokens = normalize(earlier.text)
    later_tokens = normalize(later.text)
    later_is_short_fragment = (
        len(later_tokens) / max(1, len(earlier_tokens)) < 0.90
        and not bool(re.search(r"[.!?]$", later.text.strip()))
    )
    later_is_uncertain = later.confidence + 0.20 < earlier.confidence
    suspicious_timing = any(
        word.end <= word.start or word.end - word.start > 3.5 for word in later.words
    )
    return not (later_is_short_fragment or later_is_uncertain or suspicious_timing)


def select_best_takes(
    takes: list[Take],
    duplicate_window: float,
    threshold: float,
    prefer_last: bool,
) -> None:
    for earlier_index, earlier in enumerate(takes):
        if not earlier.keep:
            continue
        for later in takes[earlier_index + 1:]:
            if later.start - earlier.end > duplicate_window:
                break
            if not later.keep or not looks_repeated(earlier, later, threshold):
                continue
            if prefer_last and prefer_later_take(earlier, later):
                earlier.keep = False
                earlier.reason = f"earlier repeated/false take; kept later take {later.index + 1}"
                earlier.duplicate_of = later.index
                break
            later.keep = False
            later.reason = f"lower-quality/incomplete duplicate; kept take {earlier.index + 1}"
            later.duplicate_of = earlier.index


def speech_chunks(
    takes: Sequence[Take],
    min_silence: float,
    pad_before: float,
    pad_after: float,
    merge_gap: float,
    duration: float,
) -> list[tuple[float, float]]:
    chunks: list[tuple[float, float]] = []
    for take in takes:
        if not take.keep or not take.words:
            continue
        start = take.words[0].start
        previous = take.words[0]
        for word in take.words[1:]:
            if word.start - previous.end >= min_silence:
                chunks.append((max(0.0, start - pad_before), min(duration, previous.end + pad_after)))
                start = word.start
            previous = word
        chunks.append((max(0.0, start - pad_before), min(duration, previous.end + pad_after)))

    merged: list[tuple[float, float]] = []
    for start, end in sorted(chunks):
        if end <= start:
            continue
        if merged and start - merged[-1][1] <= merge_gap:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged


def probe_duration(input_path: Path) -> float:
    result = run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(input_path),
    ], capture=True)
    return float(result.stdout.strip())


def filter_graph(chunks: Sequence[tuple[float, float]], enhance_audio: bool) -> str:
    lines: list[str] = []
    pairs: list[str] = []
    for index, (start, end) in enumerate(chunks):
        lines.append(f"[0:v]trim=start={start:.3f}:end={end:.3f},setpts=PTS-STARTPTS[v{index}]")
        lines.append(f"[0:a]atrim=start={start:.3f}:end={end:.3f},asetpts=PTS-STARTPTS[a{index}]")
        pairs.append(f"[v{index}][a{index}]")
    lines.append(f"{''.join(pairs)}concat=n={len(chunks)}:v=1:a=1[vout][joined]")
    if enhance_audio:
        lines.append("[joined]highpass=f=80,lowpass=f=12000,acompressor,loudnorm=I=-16:TP=-1.5:LRA=11[aout]")
    else:
        lines.append("[joined]anull[aout]")
    return ";\n".join(lines)


def render(input_path: Path, output_path: Path, chunks: Sequence[tuple[float, float]], enhance_audio: bool, crf: int) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".ffscript", delete=False) as handle:
        handle.write(filter_graph(chunks, enhance_audio))
        filter_path = Path(handle.name)
    try:
        command = [
            "ffmpeg", "-nostdin", "-y", "-hide_banner", "-loglevel", "warning",
            "-i", str(input_path), "-filter_complex_script", str(filter_path),
            "-map", "[vout]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf),
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart", "-metadata:s:v:0", "rotate=0", str(output_path),
        ]
        print("Encoding once from the completed edit plan…", flush=True)
        run(command)
    finally:
        filter_path.unlink(missing_ok=True)


def save_report(
    report_path: Path,
    input_path: Path,
    output_path: Path,
    duration: float,
    takes: Sequence[Take],
    chunks: Sequence[tuple[float, float]],
    args: argparse.Namespace,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "input": str(input_path.resolve()),
        "output": str(output_path.resolve()),
        "source_duration_seconds": round(duration, 3),
        "estimated_output_seconds": round(sum(end - start for start, end in chunks), 3),
        "selection_rule": "prefer latest matching take" if args.prefer_last else "prefer first matching take",
        "settings": {
            "min_silence": args.min_silence,
            "take_gap": args.take_gap,
            "sentence_gap": args.sentence_gap,
            "duplicate_window": args.duplicate_window,
            "duplicate_threshold": args.duplicate_threshold,
            "pad_before": args.pad_before,
            "pad_after": args.pad_after,
            "merge_gap": args.merge_gap,
        },
        "takes": [
            {
                **{key: value for key, value in asdict(take).items() if key != "words"},
                "confidence": round(take.confidence, 4),
            }
            for take in takes
        ],
        "kept_chunks": [
            {"start": round(start, 3), "end": round(end, 3)} for start, end in chunks
        ],
    }
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove silences and repeated false takes, preferring the last clean take, then encode once.",
    )
    parser.add_argument("input", type=Path, help="Talking-head video to edit")
    parser.add_argument("output", type=Path, nargs="?", help="Output MP4 (default: INPUT_one_pass.mp4)")
    parser.add_argument("--transcript-json", type=Path, help="Reuse a Whisper JSON transcript instead of transcribing")
    parser.add_argument("--save-transcript", type=Path, help="Where to save the generated transcript JSON")
    parser.add_argument("--model", default="small.en", help="faster-whisper model name/path (default: small.en)")
    parser.add_argument("--language", default="en", help="Language code; use 'auto' for detection")
    parser.add_argument("--min-silence", type=float, default=0.35, help="Remove pauses at least this long (seconds)")
    parser.add_argument("--take-gap", type=float, default=0.50, help="Pause that starts a new take")
    parser.add_argument("--sentence-gap", type=float, default=0.28, help="Pause after terminal punctuation that starts a new take")
    parser.add_argument("--duplicate-window", type=float, default=45.0, help="Only compare takes within this many seconds")
    parser.add_argument("--duplicate-threshold", type=float, default=0.66, help="Similarity threshold from 0 to 1")
    parser.add_argument("--pad-before", type=float, default=0.06, help="Seconds kept before speech")
    parser.add_argument("--pad-after", type=float, default=0.08, help="Seconds kept after speech")
    parser.add_argument("--merge-gap", type=float, default=0.04, help="Merge nearly touching kept chunks")
    parser.add_argument("--restart-marker", action="append", default=[], help="Spoken redo marker; repeat for several")
    parser.add_argument("--prefer-first", dest="prefer_last", action="store_false", help="Keep the first duplicate instead of the last")
    parser.set_defaults(prefer_last=True)
    parser.add_argument("--silence-only", action="store_true", help="Do not remove repeated takes")
    parser.add_argument("--enhance-audio", action="store_true", help="Apply light voice cleanup and -16 LUFS normalization")
    parser.add_argument("--crf", type=int, default=18, help="H.264 quality (lower is higher quality)")
    parser.add_argument("--report", type=Path, help="Edit decision report path")
    parser.add_argument("--dry-run", action="store_true", help="Create transcript/report without rendering")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = args.input.expanduser().resolve()
    if not input_path.is_file():
        fail(f"input does not exist: {input_path}")
    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            fail(f"{tool} is required and was not found on PATH")

    output_path = (args.output or input_path.with_name(f"{input_path.stem}_one_pass.mp4")).expanduser().resolve()
    report_path = (args.report or output_path.with_suffix(".edit-plan.json")).expanduser().resolve()
    duration = probe_duration(input_path)

    if args.transcript_json:
        transcript = json.loads(args.transcript_json.expanduser().read_text(encoding="utf-8"))
    else:
        language = None if args.language.lower() == "auto" else args.language
        transcript = transcribe(input_path, args.model, language)
    if args.save_transcript:
        save_path = args.save_transcript.expanduser().resolve()
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(json.dumps(transcript, indent=2) + "\n", encoding="utf-8")

    words = transcript_words(transcript)
    if not words:
        fail("the transcript contains no timestamped speech")
    takes = build_takes(words, args.take_gap, args.sentence_gap)
    markers = list(DEFAULT_RESTART_MARKERS) + args.restart_marker
    mark_restart_phrases(takes, markers)
    mark_orphan_restarts(takes)
    if not args.silence_only:
        select_best_takes(takes, args.duplicate_window, args.duplicate_threshold, args.prefer_last)

    chunks = speech_chunks(
        takes, args.min_silence, args.pad_before, args.pad_after, args.merge_gap, duration,
    )
    if not chunks:
        fail("no speech remained after analysis")
    save_report(report_path, input_path, output_path, duration, takes, chunks, args)

    kept = sum(take.keep for take in takes)
    removed = len(takes) - kept
    estimated = sum(end - start for start, end in chunks)
    print(f"Takes: {kept} kept, {removed} repeated/false takes removed", flush=True)
    print(f"Timeline: {duration:.2f}s → approximately {estimated:.2f}s", flush=True)
    print(f"Decision report: {report_path}", flush=True)
    if args.dry_run:
        print("Dry run complete; no video was rendered.", flush=True)
        return
    render(input_path, output_path, chunks, args.enhance_audio, args.crf)
    print(f"Finished: {output_path}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        fail(f"command failed with exit code {error.returncode}")
