#!/usr/bin/env python3
"""One Line of Earned Pride - a make.fun entry.

The program writes one line to entry.txt in the output directory:
a quiet, earned moment of pride, shown inside a concrete scene
rather than explained.
"""

import os

# The line: eleven years of night shifts behind it, and the
# pride lands in the last gesture, never announced.
LINE = "After eleven years of night shifts, Marta pinned her daughter's nurse badge on with hands that finally stopped shaking."


def out_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main() -> None:
    with open(out_path(), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
