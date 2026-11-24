#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

Competition: The Funniest Out-of-Office (program/v1).
The program writes a single line, 140 characters or fewer, and nothing else.
"""

import os

LINE = "I'm away. The last person who emailed me 'quick question' is still waiting — it's been 11 months."


def validate(entry):
    if not isinstance(entry, str) or not entry.strip():
        raise SystemExit("invalid entry: must be a non-blank string")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("invalid entry: must be exactly one line")
    if not (1 <= len(entry) <= 140):
        raise SystemExit("invalid entry: must be 1-140 characters")
    return entry


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("output mismatch: file does not contain the entry exactly")


if __name__ == "__main__":
    main()
