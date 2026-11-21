#!/usr/bin/env python3
"""judge-brave-21nov26 entry — Python 3.13, standard library only, no network.

The program writes one fixed text, "The Lamp Is Small", to entry.txt in
the output directory: /output inside the grader's container, or the
directory named by MAKEFUN_OUTPUT_DIR when run locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The text is a constant, so every run writes exactly the same bytes. The
text is UTF-8, 187 characters (Unicode code points, well inside the gate's
1-280 range), not only white space, and ends without a trailing newline:
the judge reads exactly the bytes written, so the file holds the text
and nothing else.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The night is wide, and the lamp is small,\n"
    "but it is lit.\n"
    "Step by step, the path finds your feet —\n"
    "not because you are fearless,\n"
    "but because you kept walking\n"
    "while the dark was still dark."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
