#!/usr/bin/env python3
"""ai-happy-01 entry: "Sunflower Smile".

Writes entry.png to the output directory. The image shows a smiling
golden retriever puppy sitting in a sunflower field under a rainbow,
a butterfly resting on its nose, in warm golden-hour light -- a
picture made to make the AI judge happy. Sunflowers, a rainbow, a
puppy grin and a butterfly: simple, sunny, impossible not to smile at.

Deterministic by design: a pure byte-for-byte copy of the bundled
entry.png. No network, no randomness, no timestamps in the output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SOURCE, dest)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
