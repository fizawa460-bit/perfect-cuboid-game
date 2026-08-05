#!/usr/bin/env python3
"""Normalize stage-seven-owned whitespace in the canonical research memo.

The stage-seven updater replaces a marked section and one conclusion bullet.
This helper makes those two regions byte-stable without touching the wording or
spacing of unrelated research sections.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


STAGE7_END = "<!-- TWO_FACE_STAGE7_END -->"
SECTION5 = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED = "### 確定\n"
PROMISING = "### 有望だが未証明"


def normalize(text: str) -> str:
    text = re.sub(
        re.escape(STAGE7_END) + r"\n+" + re.escape(SECTION5),
        STAGE7_END + "\n\n" + SECTION5,
        text,
        count=1,
    )

    if CONFIRMED not in text or PROMISING not in text:
        raise ValueError("could not locate final conclusion subsections")
    before, rest = text.split(CONFIRMED, 1)
    confirmed_block, after = rest.split(PROMISING, 1)
    bullets: list[str] = []
    seen: set[str] = set()
    for line in confirmed_block.splitlines():
        if not line.startswith("- ") or line in seen:
            continue
        seen.add(line)
        bullets.append(line)
    if not bullets:
        raise ValueError("confirmed conclusion contains no bullets")
    text = (
        before
        + CONFIRMED
        + "\n"
        + "\n".join(bullets)
        + "\n\n"
        + PROMISING
        + after
    )
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(
        normalize(args.input.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
