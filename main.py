# ai-happy-01 entry: make the AI judge happy. The image beside this file is
# a golden retriever puppy smiling in a sunflower field under a rainbow, a
# butterfly on its nose, in warm golden-hour light: pure, uncomplicated joy.
# The program copies it to the output directory; the judge sees exactly
# these bytes.

import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("entry.png"), out_dir / "entry.png")


if __name__ == "__main__":
    main()
