#!/usr/bin/env python3
"""Write the one-line sick-day excuse to /output/entry.txt.

Stdlib only. The entry is exactly one line: no trailing newline, no
extra text, so what the judge reads is the message and nothing else.
"""

import os

EXCUSE = (
    "I sprained my ankle stepping on a Lego in the dark and the doctor "
    "says I have to elevate it and my dignity."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    if not 1 <= len(EXCUSE) <= 200:
        raise SystemExit("entry must be 1..200 characters, got %d" % len(EXCUSE))
    if not EXCUSE.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise SystemExit("entry must be a single line")

    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
