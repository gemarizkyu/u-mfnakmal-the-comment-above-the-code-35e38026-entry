#!/usr/bin/env python3
"""The Comment Above the Code -- make.fun bounty entry.

Writes one line, a comment a developer might leave above fragile
production code, to /output/entry.txt. The line is fixed: the same
text on every run. No clock, no randomness, no network, no model
calls -- the entry is a single honest joke, written once.
"""

import os
from pathlib import Path

# The gate allows 1 to 200 characters of UTF-8 text, not only
# whitespace. Keep the cap as a named constant so the check below
# and the brief can never drift apart.
MAX_CHARS = 200

# The entry: one line, at most 200 characters, in a working
# developer's voice. A real failure (a "temporary" column that
# became load-bearing), an economical setup, and the punchline
# lands on the last few words.
LINE = "// The column is still called 'temp' because in 2016 someone was sure this was temporary. It runs payroll now."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the entry line to entry.txt."""
    text = LINE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
