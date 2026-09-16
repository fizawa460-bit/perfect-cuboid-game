#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]

SOURCE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPECIAL-GRID-DELTA-CAPACITY-WALL.md": "f7ae2dac5be3b15542471e5b4b0e50515c05537b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-LOW-BIDEGREE-BEZOUT-CAPACITY.md": "60cd43c94b7d1ab2992f3cd502d1e49ac2c972e6",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-LOW-BIDEGREE-BEZOUT-CAPACITY-CERTIFICATE.json": "e06fe6ef76468e9c83c8bc8d1c1ed35a905f4b9a",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-JOINT-PAIR-BIRATIONALITY.md": "53608cb51aa49ccde1603b1cb1d136ea497b2324",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE-CERTIFICATE.json": "02c5c5b52ed18cc2850a01bab05c6dfac85a59f9",
}


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def verify_source_locks() -> None:
    for rel, expected in SOURCE_LOCKS.items():
        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"FAIL missing source lock: {rel}")
        got = git_blob_sha1(path)
        if got != expected:
            raise SystemExit(f"FAIL source lock drift: {rel} expected={expected} got={got}")


def block_square_max() -> int:
    # Scale l=1. Complementary pair totals are 16,16,16,8 and
    # the selected saturated fibre has total 28.
    caps = (16, 16, 16, 8)
    best = -1
    # A vertex of the 3D slice has at least three coordinates at bounds.
    for free in range(4):
        fixed = [i for i in range(4) if i != free]
        for bits in product((0, 1), repeat=3):
            y = [None] * 4
            for i, bit in zip(fixed, bits):
                y[i] = caps[i] if bit else 0
            y[free] = 28 - sum(y[i] for i in fixed)
            if not (0 <= y[free] <= caps[free]):
                continue
            q = sum(v * v + (cap - v) * (cap - v) for v, cap in zip(y, caps))
            best = max(best, q)
    return best


def survivor_check() -> tuple[int, int, int, int, tuple[int, ...]]:
    # Retained formal survivor from LOW-BIDEGREE-BEZOUT-CAPACITY.
    l = 10
    x = {
        0: 8, 1: 0, 2: 0, 3: 48,
        8: 42, 9: 76, 10: 2, 11: 80,
        24: 0, 25: 0, 26: 0,
        32: 0, 33: 2, 34: 78,
    }
    w = (
        x[0] + x[2], 16*l - x[0] - x[2],
        x[1] + x[3], 16*l - x[1] - x[3],
        x[24] + x[26], 16*l - x[24] - x[26],
        x[25], 8*l - x[25],
        x[8] + x[10], 16*l - x[8] - x[10],
        x[9] + x[11], 16*l - x[9] - x[11],
        x[32] + x[34], 16*l - x[32] - x[34],
        x[33], 8*l - x[33],
    )
    special_delta = sum(v * (v - 1) // 2 for v in w)
    total_delta = 784*l*l - 56*l

    b = (-16,-20,-20,4, 1,18,-19,20, -20,-20,-20, -20,-19,19)
    q = sum(v*v for v in b)
    cross = b[0]*b[2] + b[1]*b[3] + b[4]*b[6] + b[5]*b[7] + b[8]*b[10] + b[11]*b[13]
    return special_delta, total_delta, q, cross, w


def main() -> None:
    # Fail closed on all load-bearing retained inputs before doing mathematics.
    verify_source_locks()

    bmax = block_square_max()
    if bmax != 736:
        raise SystemExit(f"FAIL block square maximum: {bmax}")

    total_square_max = 2 * bmax
    if total_square_max != 1472:
        raise SystemExit("FAIL total special square maximum")

    # sum w = 112 l, hence S_special <= (1472 l^2 - 112 l)/2.
    # Compare to delta(C)=784 l^2 - 56 l: exact headroom is 48 l^2.
    # In l=2m variables this says saturation => Q+2X <= 320 m^2,
    # while the naive delta-budget contradiction threshold is 368 m^2.
    for m in (1, 2, 5, 11):
        if not (320*m*m < 368*m*m):
            raise SystemExit("FAIL strict redundancy check")

    special_delta, total_delta, q, cross, w = survivor_check()
    if w != (8,152,48,112,0,160,0,80,44,116,156,4,78,82,2,78):
        raise SystemExit(f"FAIL survivor branch masses: {w}")
    if special_delta != 63768 or total_delta != 77840:
        raise SystemExit("FAIL survivor delta arithmetic")
    if q != 4480 or cross != 601 or q + 2*cross != 5682:
        raise SystemExit("FAIL survivor thin-shell arithmetic")
    if not (q + 2*cross <= 320*25 < 368*25):
        raise SystemExit("FAIL survivor redundancy ordering")

    print("PASS stage32 MB104 000707 e2 special-grid delta-capacity wall")


if __name__ == "__main__":
    main()
