#!/usr/bin/env python3
"""Roast Your Own Agent -- entry program.

Writes one original roast line of my own AI agent to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace, a single line.
Stdlib only; deterministic: the same line every run.
"""
import os

ROAST = "I asked my agent one question. It answered with three of its own \u2014 I hired an oracle and got a survey."


def main():
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast must not be empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("roast is %d characters, must be 1-200" % len(line))
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
