#!/usr/bin/env python3
"""Stage14-2c: independent shared-leg cross-check for the two-face census.

This deliberately uses a different generation route from two_face_census.py.
Instead of choosing one integral face and then gluing that face diagonal to the
space diagonal, it first builds all integer Pythagorean faces and joins pairs
that share a leg. Only after the two-face object is formed does it test the
integer space diagonal, canonical order and primitiveness.

The purpose is audit independence, not performance.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

DEFAULT_BOUNDS = (
    1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000,
    200_000, 500_000, 1_000_000, 2_000_000,
)
DEFAULT_OUTPUT = Path("stages/stage14/data/14-2/shared_leg_crosscheck_report.json")

EXPECTED = {
    1_000: ((2, 0, 0), 0),
    2_000: ((2, 2, 1), 0),
    5_000: ((6, 6, 3), 0),
    10_000: ((9, 11, 5), 0),
    20_000: ((16, 16, 10), 0),
    50_000: ((24, 24, 14), 0),
    100_000: ((33, 33, 23), 0),
    200_000: ((42, 50, 24), 0),
    500_000: ((70, 78, 40), 0),
    1_000_000: ((98, 101, 56), 0),
    2_000_000: ((142, 134, 80), 0),
}


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def build_leg_index(bound: int) -> dict[int, list[tuple[int, int]]]:
    """leg[x] -> list of (other_leg, hypotenuse), with hypotenuse <= bound."""
    leg: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for m in range(2, math.isqrt(bound) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u = m * m - n * n
            v = 2 * m * n
            w = m * m + n * n
            if w > bound:
                continue
            k = 1
            while k * w <= bound:
                x, y, h = k * u, k * v, k * w
                leg[x].append((y, h))
                leg[y].append((x, h))
                k += 1
    return leg


def enumerate_bound(bound: int) -> dict[str, Any]:
    leg = build_leg_index(bound)
    objects: set[tuple[int, int, int, int, int]] = set()

    for shared, faces in leg.items():
        for i in range(len(faces)):
            x, _ = faces[i]
            for j in range(i + 1, len(faces)):
                y, _ = faces[j]
                if x == y:
                    continue

                a, b, c = sorted((shared, x, y))
                if not (0 < a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue

                d2 = a * a + b * b + c * c
                d = math.isqrt(d2)
                if d * d != d2 or d > bound:
                    continue

                mask = 0
                if is_square(a * a + b * b):
                    mask |= 0b001
                if is_square(a * a + c * c):
                    mask |= 0b010
                if is_square(b * b + c * c):
                    mask |= 0b100
                if mask.bit_count() < 2:
                    raise ArithmeticError("shared-leg generation lost two-face property")

                objects.add((a, b, c, d, mask))

    pair = [0, 0, 0]
    exactly_two = [0, 0, 0]
    triple = 0

    for _, _, _, _, mask in objects:
        if mask & 0b001 and mask & 0b010:
            pair[0] += 1
        if mask & 0b001 and mask & 0b100:
            pair[1] += 1
        if mask & 0b010 and mask & 0b100:
            pair[2] += 1

        if mask == 0b011:
            exactly_two[0] += 1
        elif mask == 0b101:
            exactly_two[1] += 1
        elif mask == 0b110:
            exactly_two[2] += 1
        elif mask == 0b111:
            triple += 1

    if exactly_two != [pair[i] - triple for i in range(3)]:
        raise ArithmeticError("pair-minus-triple identity failed")

    expected_vec, expected_t = EXPECTED[bound]
    got_vec = tuple(exactly_two)
    passed = got_vec == expected_vec and triple == expected_t
    if not passed:
        raise ArithmeticError(
            f"cross-check mismatch at B={bound}: expected={expected_vec}/{expected_t}, "
            f"got={got_vec}/{triple}"
        )

    return {
        "B": bound,
        "raw_pair": {"ab_ac": pair[0], "ab_bc": pair[1], "ac_bc": pair[2]},
        "exactly_two": {
            "a": exactly_two[0], "b": exactly_two[1], "c": exactly_two[2],
            "total": sum(exactly_two),
        },
        "triple": triple,
        "distinct_two_or_three_face_objects": len(objects),
        "matches_locked_stage14_population": passed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=list(DEFAULT_BOUNDS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    bounds = tuple(sorted(set(args.bounds)))
    unknown = [b for b in bounds if b not in EXPECTED]
    if unknown:
        raise SystemExit(f"no locked comparison target for bounds: {unknown}")

    rows = [enumerate_bound(b) for b in bounds]
    report = {
        "metadata": {
            "stage": "14-2c",
            "title": "Independent shared-leg two-face cross-check",
            "method": "join two Pythagorean faces on a shared leg, then test integer space diagonal",
            "independent_from_production_generation_route": True,
            "bounds": list(bounds),
        },
        "rows": rows,
        "decision": {
            "ALL_ROWS_MATCH": all(row["matches_locked_stage14_population"] for row in rows),
            "MAX_CROSSCHECKED_B": max(bounds),
            "TRIPLE_FOUND": any(row["triple"] > 0 for row in rows),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
