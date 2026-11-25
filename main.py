#!/usr/bin/env python3
"""Write one line, a childhood memory, to /output/entry.txt.

The line is written exactly as given: 173 Unicode code points,
inside the competition gate of 1-280.
Python 3, standard library only, no network.
"""

import os

TEXT = "When the streetlights buzzed on, every kid on the block heard their mother call their name at the exact same second, and we all ran home pretending we were not the last one."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
