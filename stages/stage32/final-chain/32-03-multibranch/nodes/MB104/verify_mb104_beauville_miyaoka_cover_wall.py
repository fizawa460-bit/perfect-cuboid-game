#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"


def main() -> None:
    cert = json.loads((NODE / "BEAUVILLE-MIYAOKA-COVER-WALL.json").read_text())
    assert cert["schema"] == "STAGE32_MB104_BEAUVILLE_MIYAOKA_COVER_WALL_V1"

    # Product/quotient Chern arithmetic.
    assert 8 * 4 * 4 == 128
    assert 4 * 4 * 4 == 64
    assert 128 // 4 == 32
    assert 64 // 4 == 16

    K2, c2 = 32, 16
    sqrt_term_sq = 2 * K2 * (3 * c2 - K2)
    assert sqrt_term_sq == 1024
    sqrt_term = 32
    a_num = 2 * K2 + sqrt_term
    a_den = K2 - c2
    assert a_num // a_den == 6 and a_num % a_den == 0
    b_num = K2 * (3 * c2 - K2) + c2 * sqrt_term
    b_den = 2 * (K2 - c2)
    assert b_num // b_den == 32 and b_num % b_den == 0

    for g in (0, 1):
        for d in range(2, 5001):
            r0 = d - 4 * g + 4
            assert r0 > 0
            # Existing minimal-branch ramification lower bound makes the
            # Miyaoka cover inequality automatically compatible.
            assert 2 * d <= 3 * r0 + 12 * g + 20

    fw = cert["firewalls"]
    assert fw["finite_degree_window_proved"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 Beauville-Miyaoka cover wall verifier PASS")
    print("X invariants: K^2=32, c2=16; Miyaoka constants a=6, b=32")
    print("derived: 2d<=3r+12g+20")
    print("dominated by retained r>=d-4g+4; finite degree window remains OPEN")


if __name__ == "__main__":
    main()
