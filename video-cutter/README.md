# One-Pass Video Cutter

A local, reusable talking-head editor that:

1. transcribes the recording once;
2. removes silences;
3. detects nearby repeated or false-start takes;
4. keeps the **last matching take** by default, after checking that it is complete and usable;
5. builds one edit-decision plan; and
6. performs a single final video encode.

No API key is required. Your video stays on your computer.

## Best recording pattern

When you make a mistake, pause, repeat the whole line, and continue. The later
matching line is treated as the preferred take. For maximum reliability, say
`cut cut`, pause, and repeat the line. The marker and the preceding failed take
are removed automatically.

“Prefer last” is not blind. A later take is rejected when it is clearly
truncated, has substantially worse transcription confidence, or contains
malformed word timing. In that case, the earlier complete take is preserved.

## Install

Install [FFmpeg](https://ffmpeg.org/) and Python 3.10 or newer. Then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On macOS, FFmpeg can be installed with:

```bash
brew install ffmpeg
```

## Use

```bash
python one_pass_video_cutter.py input.mov output.mp4
```

The defaults are designed for short talking-head videos:

- pauses of 0.35 seconds or longer are removed;
- a 0.50-second pause is treated as a likely new take boundary;
- repeated takes within 45 seconds are compared;
- the last matching take is kept;
- 60 ms before and 80 ms after speech are retained so cuts do not clip words;
- the video is encoded only once after all decisions are made.

The run also creates `output.edit-plan.json`. It records every detected take,
why it was kept or removed, and the exact timeline segments used in the export.

## Recommended commands

Standard one-pass edit:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4
```

Preview decisions without rendering:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4 --dry-run
```

Add light voice cleanup and loudness normalization:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4 --enhance-audio
```

Only remove silence; keep every spoken take:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4 --silence-only
```

Use a custom spoken redo marker:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4 \
  --restart-marker "redo that"
```

Keep more natural breathing room:

```bash
python one_pass_video_cutter.py recording.mov recording_clean.mp4 \
  --min-silence 0.55 --pad-before 0.10 --pad-after 0.12
```

## Accuracy notes

Repeated-take selection is transcript-based. Clear pauses and repeating the
complete sentence make the automatic choice much more reliable. The JSON edit
plan is intentionally saved because two genuinely different sentences can
occasionally sound similar, and creative intent cannot always be inferred from
audio alone.

The repository includes automated tests for last-take preference, incomplete
last takes, malformed retries, restart fragments, and silence removal. Run:

```bash
python -m unittest -v
```

If a line must never be guessed, use the spoken marker `cut cut` before its
replacement. This is deterministic and is the safest recording habit.

## Upload to GitHub

Create an empty GitHub repository, then run inside this folder:

```bash
git init
git add .
git commit -m "Add one-pass talking-head video cutter"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/one-pass-video-cutter.git
git push -u origin main
```

## Main options

Run `python one_pass_video_cutter.py --help` for every setting.

| Option | Default | Purpose |
|---|---:|---|
| `--min-silence` | `0.35` | Minimum pause removed |
| `--duplicate-window` | `45` | Seconds in which retries are compared |
| `--duplicate-threshold` | `0.66` | Similarity required for duplicate removal |
| `--prefer-first` | off | Keep the first matching take instead |
| `--silence-only` | off | Disable repeated-take removal |
| `--dry-run` | off | Save the plan without rendering |
| `--enhance-audio` | off | Clean and normalize voice audio |
| `--model` | `small.en` | Local faster-whisper model |

## License

MIT
