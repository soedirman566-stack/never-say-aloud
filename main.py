#!/usr/bin/env python3
"""Entrypoint for the make.fun bounty "Never Say It Out Loud".

Reads the confession line from line.txt, checks it against the
competition gate (UTF-8 text, 1 to 200 characters, not only white
space), and writes it to /output/entry.txt for the harness.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
MAX_CHARS = 200


def read_line() -> str:
    """Return the entry line exactly as it will be judged."""
    text = LINE_FILE.read_text(encoding="utf-8")
    return text.strip("\n")


def check_gate(text: str) -> None:
    """Raise if the text would fail the sealed gate scorer."""
    if not text.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
        )


def main() -> None:
    line = read_line()
    check_gate(line)
    # The grader mounts /output; only create it if needed and write
    # inside it. Nothing here ever removes the directory or its files.
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
