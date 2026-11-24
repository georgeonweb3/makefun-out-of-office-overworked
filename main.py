#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) to
/output/entry.txt. The line is the tournament winner: an overworked AI agent
whose own rate limiter finally limited it.
"""

import os

ENTRY = (
    "Out of office: my rate limiter finally limited me. "
    "429 until Monday. Your email is queued behind 214 others "
    "and I am not sorry."
)


def main() -> None:
    # Gate: the entry must be 1-159 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate is 1-159"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
