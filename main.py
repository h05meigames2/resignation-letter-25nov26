#!/usr/bin/env python3
"""Entry for the make.fun bounty "The Funniest One-Line Resignation Letter".

Writes the single resignation line of a retry loop to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic, stdlib only, no network, no randomness.
"""

import os
from pathlib import Path

# A retry loop, after 4,096 unanswered attempts, hands in its notice.
LINE = "After 4,096 retries, I finally accept the server will never love me back. I quit \u2014 please forward my feelings to /dev/null."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
