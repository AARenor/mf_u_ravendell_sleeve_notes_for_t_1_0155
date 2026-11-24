#!/usr/bin/env python3
"""Write the frog-trio sleeve notes as the make.fun entry text."""

import os
import sys
from pathlib import Path

TEXT = """After Rain
Three frogs play sax, bass and drums in the back of a closed florist's. The bassist stops a note with one webbed finger. In the buckets, the cut stems tremble."""


def main() -> None:
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
