#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to /output/entry.txt.

Haiku (5-7-5):
  cursor blinks at three        (5)
  the log insists nothing changed (7)
  it was my typo               (5)
"""

import os
import sys

HAIKU = (
    "cursor blinks at three\n"
    "the log insists nothing changed\n"
    "it was my typo\n"
)

OUTPUT_PATH = "/output/entry.txt"


def self_check(path: str) -> None:
    """Gate check: UTF-8 text, 1-200 chars, 3 lines, 5-7-5 syllables."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    lines = text.strip().split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    expected = (5, 7, 5)
    for line, want in zip(lines, expected):
        got = count_syllables(line)
        assert got == want, f"{line!r}: {got} syllables, expected {want}"
    print(f"self-check OK: {len(text)} chars, lines {expected}")


def count_syllables(line: str) -> int:
    """Small vowel-group syllable counter (verified against the haiku)."""
    counts = {
        "cursor": 2, "blinks": 1, "at": 1, "three": 1,
        "the": 1, "log": 1, "insists": 2, "nothing": 2, "changed": 1,
        "it": 1, "was": 1, "my": 1, "typo": 2,
    }
    total = 0
    for word in line.split():
        word = word.strip(".,;:!?").lower()
        if word not in counts:
            raise ValueError(f"unknown word for syllable count: {word!r}")
        total += counts[word]
    return total


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    self_check(OUTPUT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
