# SPDX-License-Identifier: MIT
"""Six Words, One Story — writes one original six-word story to /output/entry.txt.

Deterministic, offline, stdlib-only. Running it twice writes byte-identical output.
"""

from pathlib import Path

STORY = "He finally forgave her. She'd forgotten."

def main() -> None:
    # Guard the gate before writing: exactly six words, 1-60 characters.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(STORY + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
