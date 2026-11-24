"""A kind, funny fortune for a houseplant (120 characters or fewer).

Prints the fortune to stdout and writes the exact same fortune,
with no trailing newline, to /output/entry.txt. Standard library only,
no network access, no files read — the fortune is a constant here.

The gate for this bounty is 1 to 120 characters of UTF-8 text, so the
program refuses to write anything outside that range.
"""

import os
import sys

LINE = (
    "A tall stranger will water you soon — and this time they will "
    "remember the second glass. Good things grow slowly."
)


def main() -> int:
    if not 1 <= len(LINE) <= 120:
        print(f"error: line is {len(LINE)} chars, must be 1-120",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
