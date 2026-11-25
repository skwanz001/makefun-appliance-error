"""The Funniest Honest Appliance Error.

A washing machine reports an over-sudsing fault in its own flat voice:
too much detergent has turned the drum into foam, and the floor is next.

The program writes exactly one line (<= 200 characters) to
/output/entry.txt. Standard library only.
"""

import os
from pathlib import Path

ENTRY = "ERROR: Too much detergent. I am now 90% foam and 10% machine. The floor is next."

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Self-check the same gate the sealed scorer applies: 1 to 200
    # characters of UTF-8 text, not only white space.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("entry is only white space")
    text.encode("utf-8")

    out = Path(OUTPUT_PATH)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
