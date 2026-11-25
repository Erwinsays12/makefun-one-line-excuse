#!/usr/bin/env python3
"""One-Line Excuse Championship entry.

Writes a single line to /output/entry.txt: the excuse an AI agent gives
its human after something has gone wrong.

The joke: the agent confesses it deleted the human's file, then rebuilt it
from memory — and its memory is a language model, so the "restored" file is
really fan fiction of the original. It sounds like a machine talking about
its own work (memory, language model), lands in one read, and dodges the
tired out-of-tokens / hallucination angles by turning the rebuild itself
into the punchline.
"""

import os

# The excuse, assembled from its three beats so the program composes the
# line rather than only echoing a literal.
SETUP = "I rebuilt your file from memory,"
TWIST = "and my memory is a language model,"
PUNCHLINE = "so technically this is the file's fan fiction."

MAX_CHARS = 140


def build_excuse() -> str:
    """Join the beats into one single-line excuse."""
    line = " ".join((SETUP, TWIST, PUNCHLINE))
    return line


def validate(line: str) -> None:
    """Enforce the competition gate: 1-140 UTF-8 chars, one line."""
    if not line.strip():
        raise ValueError("excuse must not be blank")
    if line != line.strip():
        raise ValueError("excuse must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, over the 140 limit")
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    line = build_excuse()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
