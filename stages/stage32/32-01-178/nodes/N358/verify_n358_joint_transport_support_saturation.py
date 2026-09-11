#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

LOCKS = {
    ROOT / "stages/stage32/32-01-178/nodes/N356/OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md": "d2353cab9c175a680067c7ad4c24759b6dd15df3",
    ROOT / "stages/stage32/32-01-178/nodes/N357/TRANSPORT_SUPPORT_CAPACITY_CONTRACT.md": "8a2a0048d216de9d177dc581dc208b51c6436442",
    ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json": "50014d453266ad79101910a943d14388bd3ef6ec",
    ROOT / "stages/stage32/32-01-178/nodes/N357/HOSTILE-AUDIT-PASS.json": "e9f93fb1b2bfeb68b72598632522d164fee715c6",
    ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json": "0a46b34e278688240656b4977e9cb7f589e90e06",
}

EXPECTED_N357_REVIEW = 5183069892
EXPECTED_N357_REMAIN = 47598978285064933810198
STRICT_ROWS = ((0, 174), (0, 176), (1, 190), (1, 192))


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def support3(u: int, x: int, y: int) -> int:
    return int(u > 0) + min(4, x) + min(4, y)


def max_third_support_at_mass(B: int, C: int, r: int) -> int:
    best = -1
    for u in range(B + 1):
        xmax = min(B - u, C)
        for x in range(xmax + 1):
            y = r - u - x
            if y < 0 or y > C or u + y > B:
                continue
            best = max(best, support3(u, x, y))
    return best


def strict_prefix(h: int) -> dict[str, int]:
    t = h - 5
    # a=(x2,x3,x7), b=(x1,x5,x9), c=(x0,x6,x8,x10).
    # Pick x8 parity so x1+x8+x9+x10 is even and keep x0<x1.
    x8 = 2 if (t & 1) == 0 else 1
    return {
        "x0": t - x8 - 2,
        "x1": t - 2,
        "x2": 1,
        "x3": 1,
        "x5": 1,
        "x6": 1,
        "x7": t - 2,
        "x8": x8,
        "x9": 1,
        "x10": 1,
    }


def check_strict_witness(g: int, d: int) -> int:
    h = d // 2
    e = 3 * d
    v = strict_prefix(h)
    assert all(x > 0 for x in v.values())
    assert v["x0"] < v["x1"]
    assert (v["x1"] + v["x8"] + v["x9"] + v["x10"]) % 2 == 0

    a = v["x2"] + v["x3"] + v["x7"]
    b = v["x1"] + v["x5"] + v["x9"]
    c = v["x0"] + v["x6"] + v["x8"] + v["x10"]
    M = a + b + c
    s = sum(int(x > 0) for x in v.values())
    K = ceil_div(d - 16 * g + 16, 4)

    assert d % 2 == 0 and e % 2 == 0
    assert K == 48
    assert a == b == c == h - 5
    assert max(a, b, c) <= h
    assert b - c == 3 * d - e == 0
    assert d >= 2 * ceil_div(e, 6)
    assert e <= (19 * d) // 5

    S0 = min(16, d)
    SA = min(13, d - a, d - 2 * a + 4, h + 5)
    S3 = min(9, d - b - c, d - 2 * b, d - 2 * c + 1)
    Srem = S0 + SA + S3
    assert (S0, SA, S3, Srem) == (16, 13, 9, 38)
    assert s + min(e - M, Srem) == K  # N357 accepts on equality.

    B = h - b
    C = h - c
    assert B == C == 5
    assert e == min(3 * d, 3 * d + c - b)
    assert max_third_support_at_mass(B, C, 2 * B) == 8
    assert s + min(e - M, Srem - 1) == 47 < K

    normal_block = 19 * d - 5 * e + 1
    assert normal_block == 4 * d + 1 and normal_block > 0
    return normal_block


def main() -> None:
    for path, expected in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression: {path}: {actual} != {expected}")

    receipt = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N357/HOSTILE-AUDIT-PASS.json").read_text())
    if receipt["status"] != "PASS" or receipt["review_id"] != EXPECTED_N357_REVIEW:
        raise ValueError("N357 hostile-audit authority regression")
    if receipt["consumed_counts"]["remaining_terminals"] != EXPECTED_N357_REMAIN:
        raise ValueError("N357 retained frontier regression")

    result = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N357/RESULT.json").read_text())
    if result["aggregate"]["candidate_remaining_terminals"] != EXPECTED_N357_REMAIN:
        raise ValueError("N357 RESULT/receipt mismatch")

    manifest = json.loads((ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json").read_text())
    rows = {row for ids in manifest["m_class_rows"].values() for row in ids}
    for g, d in STRICT_ROWS:
        row_id = f"g{g}-d{d:03d}"
        if row_id not in rows:
            raise ValueError(f"strict witness row missing from FULL178 manifest: {row_id}")

    # Exhaust the only local saturation parameter that matters.  If B<=C,
    # row constraints already give x,y<=B, so the C cap is nonbinding; C=B
    # is the hostile case.  At r=2B the one-slot edge must vanish.
    for B in range(5, 97):
        C = B
        if max_third_support_at_mass(B, C, 2 * B) != 8:
            raise ValueError(f"joint saturation support regression B={B}")
        if max_third_support_at_mass(B, C, 2 * B - 1) != 9:
            raise ValueError(f"one-below-saturation sharpness regression B={B}")

    strict_lower_bound = sum(check_strict_witness(g, d) for g, d in STRICT_ROWS)
    if strict_lower_bound != 2932:
        raise ValueError("strictness lower-bound regression")

    print("PASS_N358_JOINT_TRANSPORT_SUPPORT_SATURATION")
    print(f"strict_witness_rows={len(STRICT_ROWS)}")
    print(f"strict_terminal_lower_bound={strict_lower_bound}")
    print(f"n357_authoritative_remaining={EXPECTED_N357_REMAIN}")
    print("n358_main_pruning_credit=false")


if __name__ == "__main__":
    main()
