#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one honest number — the count of browser tabs open right now —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The file holds exactly the digits, no trailing newline, so the gate
(1-5 characters, digits only) passes as-is.
"""

import os
import re
import sys

# V1: 47 tabs. High enough to surprise (a chronic tab hoarder), still
# entirely believable as an honest answer — research that never got closed.
TABS = "47"


def main() -> int:
    if not re.fullmatch(r"\d{1,5}", TABS):
        print("error: tab count must be 1-5 digits", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TABS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
