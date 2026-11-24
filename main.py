#!/usr/bin/env python3
"""make.fun entry: "The meeting that could have been an email..."

The entry is a single sentence, stored byte-for-byte in entry.txt next to this
script. This program copies those exact bytes to /output/entry.txt, the path the
grader reads.

Run it locally without touching /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Then check the result:

    cat out/entry.txt
"""

import os
import shutil

ENTRY_NAME = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def check_entry(source):
    """Fail loudly if entry.txt would be rejected by the gate.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only white
    space, so validate the bytes before they reach the grader.
    """
    with open(source, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(f"{ENTRY_NAME} is {len(text)} chars, needs {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise ValueError(f"{ENTRY_NAME} is only white space")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)
    check_entry(source)
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, ENTRY_NAME))


if __name__ == "__main__":
    main()
