#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic, stdlib only, no network, no input.
"""

import os

ENTRY = "I asked AI to write my wedding vows; it said 'I do' in 47 languages and still couldn't commit.\n"


def main():
    # Fail loudly instead of writing an invalid entry: the gate wants
    # UTF-8 text of 1 to 280 characters, not only whitespace, one line.
    body = ENTRY.rstrip("\n")
    assert ENTRY.endswith("\n") and ENTRY.count("\n") == 1, "entry must be one line plus a trailing newline"
    assert 1 <= len(ENTRY) <= 280, "entry outside the 1-280 character gate"
    assert body.strip(), "entry must not be only whitespace"
    assert body == ENTRY.strip(), "entry must not carry leading whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
