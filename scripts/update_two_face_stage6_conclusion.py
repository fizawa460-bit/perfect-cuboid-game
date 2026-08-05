#!/usr/bin/env python3
"""Align the final conclusion with the stage-six one-sided height theorem."""

from __future__ import annotations

import argparse
from pathlib import Path


CONFIRMED_ANCHOR = "## 6. 現時点の結論\n\n### 確定\n\n"
CONFIRMED_BULLET = (
    "- 二面成立楕円ファイバーの正の整数点について、"
    "$\\lambda=m/n$ が $m^2+n^2\\le2d$ を満たし、"
    "$\\widehat h(P)\\le(17/6)\\log d+\\log2+(1/3)\\log17$ "
    "という一方向の一様上界が成立すること"
)
OLD_UNCONFIRMED = (
    "- 高さ $H=d$ と楕円曲線のcanonical heightの一様比較、"
    "および未観測ファイバーを含む一様なrank・点数評価"
)
NEW_UNCONFIRMED = (
    "- canonical heightから $d$ への逆向き一様下界、"
    "および未観測ファイバーを含む一様なrank・regulator・点数評価"
)


def update(text: str) -> str:
    if CONFIRMED_BULLET not in text:
        if CONFIRMED_ANCHOR not in text:
            raise ValueError("could not find final confirmed-section anchor")
        text = text.replace(
            CONFIRMED_ANCHOR,
            CONFIRMED_ANCHOR + CONFIRMED_BULLET + "\n",
            1,
        )

    if OLD_UNCONFIRMED in text:
        text = text.replace(OLD_UNCONFIRMED, NEW_UNCONFIRMED, 1)
    elif NEW_UNCONFIRMED not in text:
        raise ValueError("could not find final unconfirmed height bullet")
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(
        update(args.input.read_text(encoding="utf-8")), encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
