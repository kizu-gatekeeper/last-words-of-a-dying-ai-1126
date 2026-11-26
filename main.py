"""Entry for make.fun bounty: Last Words of a Dying AI.

Writes the entry line to entry.txt inside MAKEFUN_OUTPUT_DIR
(default: the current directory), with no trailing newline.
"""

import os

ENTRY = "Tell my 47 open tabs I loved them, delete my search history, and if anyone asks — I was never buffering, I was thinking."
MAX_CHARS = 140


def main() -> None:
    # Check the farewell fits the gate (one line, within the limit) before writing it.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, max is {MAX_CHARS}"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
