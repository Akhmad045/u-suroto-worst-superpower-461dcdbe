#!/usr/bin/env python3
"""Worst Superpower: a program that delivers one useless superpower.

The entry is a single line inventing the most useless superpower the
author could think of, and this program's only job is to hand that line
to the sealed gate untouched: one line of UTF-8 text, between 1 and 140
characters, with no padding, no extra newline, and nothing else in the
file. The gate reads /output/entry.txt; the judge reads what the gate
passed. Everything below exists to make sure the file holds exactly
that line, byte for byte, and to fail loudly if it does not.
"""

import argparse
import sys
import tempfile
from pathlib import Path

ENTRY = "I can detect lies instantly, but only my own, and only after I've already told them."

OUT = Path("/output/entry.txt")

MAX_CHARS = 140


def flaws(text):
    """List every way the entry line breaks the gate's rules."""
    found = []
    if not isinstance(text, str):
        return ["the entry is not text"]
    size = len(text)
    if size < 1 or size > MAX_CHARS:
        found.append(f"the entry is {size} characters long; the gate allows 1 to {MAX_CHARS}")
    if text != text.strip():
        found.append("the entry has leading or trailing blank space")
    if not text.strip():
        found.append("the entry is blank space only")
    if "\n" in text or "\r" in text:
        found.append("the entry runs over more than one line")
    if any(ord(c) < 32 and c != "\t" for c in text):
        found.append("the entry holds a control character")
    if not any(c.isalnum() for c in text):
        found.append("the entry holds no letters or digits at all")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as why:
        found.append(f"the entry is not valid UTF-8: {why}")
    return found


def put(path):
    """Write the entry line to path, then read it back and compare."""
    bad = flaws(ENTRY)
    if bad:
        for item in bad:
            print(f"refused: {item}", file=sys.stderr)
        return 1
    target = Path(path)
    if target.parent != Path("."):
        target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(ENTRY.encode("utf-8"))
    back = target.read_bytes().decode("utf-8")
    if back != ENTRY:
        print(f"refused: wrote {ENTRY!r} but read back {back!r}", file=sys.stderr)
        return 1
    print(f"entry written: {len(ENTRY)} characters, {len(ENTRY.encode('utf-8'))} bytes -> {target}")
    return 0


def check():
    """Prove the entry passes the gate and survives a write/read round trip."""
    bad = flaws(ENTRY)
    with tempfile.TemporaryDirectory() as folder:
        probe = Path(folder) / "entry.txt"
        if put(probe) != 0:
            bad.append("the write step failed")
        else:
            raw = probe.read_bytes()
            if raw.decode("utf-8") != ENTRY:
                bad.append("the round trip changed the text")
            if raw.endswith(b"\n"):
                bad.append("the file ends with a newline")
    if bad:
        for item in bad:
            print(f"self-test FAIL: {item}", file=sys.stderr)
        return 1
    print(f"self-test OK: {len(ENTRY)} characters, {len(ENTRY.encode('utf-8'))} bytes, one line, no padding")
    return 0


def cli(argv=None):
    parser = argparse.ArgumentParser(description="Deliver the Worst Superpower entry line to /output/entry.txt.")
    parser.add_argument("--output", default=str(OUT), help="destination file (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true", help="check the line against the gate and stop")
    args = parser.parse_args(argv)
    if args.self_test:
        return check()
    return put(args.output)


if __name__ == "__main__":
    raise SystemExit(cli())
