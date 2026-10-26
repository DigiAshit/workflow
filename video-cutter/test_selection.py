import unittest

from one_pass_video_cutter import (
    Take,
    Word,
    mark_orphan_restarts,
    select_best_takes,
    speech_chunks,
)


def take(index, start, text, probabilities=None, durations=None):
    tokens = text.split()
    probabilities = probabilities or [0.95] * len(tokens)
    durations = durations or [0.20] * len(tokens)
    words = []
    cursor = start
    for token, probability, duration in zip(tokens, probabilities, durations):
        words.append(Word(cursor, cursor + duration, token, probability))
        cursor += duration
    return Take(index, words[0].start, words[-1].end, text, words)


class BestTakeSelectionTests(unittest.TestCase):
    def test_prefers_last_complete_matching_take(self):
        takes = [
            take(0, 0, "because these are bringing the most traffic"),
            take(1, 2, "because these pages are actually bringing the traffic"),
        ]
        select_best_takes(takes, 45, 0.66, True)
        self.assertFalse(takes[0].keep)
        self.assertTrue(takes[1].keep)

    def test_rejects_incomplete_last_take(self):
        takes = [
            take(0, 0, "follow for more practical SEO tips"),
            take(1, 2, "follow for more SEO practical"),
        ]
        select_best_takes(takes, 45, 0.66, True)
        self.assertTrue(takes[0].keep)
        self.assertFalse(takes[1].keep)

    def test_rejects_malformed_last_take_timing(self):
        first = take(0, 0, "a slow server above five hundred milliseconds")
        later = take(1, 2, "a slow server above five hundred thousand milliseconds")
        later.words[2] = Word(later.words[2].start, later.words[2].start, later.words[2].text, 0.95)
        select_best_takes([first, later], 45, 0.66, True)
        self.assertTrue(first.keep)
        self.assertFalse(later.keep)

    def test_removes_short_orphan_restart(self):
        takes = [
            take(0, 0, "do not"),
            take(1, 1, "do not waste time on low impact issues"),
        ]
        mark_orphan_restarts(takes)
        self.assertFalse(takes[0].keep)
        self.assertTrue(takes[1].keep)

    def test_silence_is_removed_in_same_edit_plan(self):
        words = [
            Word(0.0, 0.2, "hello"),
            Word(0.2, 0.4, "there"),
            Word(1.2, 1.4, "again"),
        ]
        item = Take(0, 0, 1.4, "hello there again", words)
        chunks = speech_chunks([item], 0.35, 0.06, 0.08, 0.04, 2.0)
        self.assertEqual(len(chunks), 2)
        self.assertAlmostEqual(chunks[0][0], 0.0)
        self.assertAlmostEqual(chunks[0][1], 0.48)
        self.assertAlmostEqual(chunks[1][0], 1.14)
        self.assertAlmostEqual(chunks[1][1], 1.48)


if __name__ == "__main__":
    unittest.main()
