"""Weirdest Job Title entry: one job title, 60 characters at most, nothing else.

Writes the title to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

LINE = "Senior VP of Printer Whispering and Jam Prevention"

MAX_CHARS = 60


def validate(line: str) -> str:
    """Enforce the gate: a single non-blank line of 1-60 characters."""
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("line must not contain double spaces")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main() -> None:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
