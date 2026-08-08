#!/usr/bin/env python3
"""Stage14-2a: primitive canonical two-face census.

This is a standalone Stage14 implementation. It does not import Stage13 code.
It enumerates primitive canonical cuboids

    0 < a < b < c,
    gcd(a,b,c)=1,
    a^2+b^2+c^2=d^2,
    d<=B,

that have at least one integral face diagonal. The complete family with at
least one integral face is reached by gluing two integer Pythagorean triples
along a shared integer length p:

    x^2 + y^2 = p^2,
    p^2 + z^2 = d^2.

Canonical tuples are deduplicated by (a,b,c,d), then all three face-square
flags are recomputed using exact integer arithmetic. Stage14 retains only the
pair/triple and exactly-two ledgers in its primary output.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

HISTORICAL_BOUNDS = (1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000)
DEFAULT_OUTPUT = Path("stages/stage14/data/14-2/historical_reproduction_report.json")

# Locked Stage14-1b checksum targets inherited from Stage13 finite data.
EXPECTED_HISTORICAL = {
    1_000: ((2, 0, 0), 0),
    2_000: ((2, 2, 1), 0),
    5_000: ((6, 6, 3), 0),
    10_000: ((9, 11, 5), 0),
    20_000: ((16, 16, 10), 0),
    50_000: ((24, 24, 14), 0),
    100_000: ((33, 33, 23), 0),
}


def is_square(n: int) -> bool:
    """Exact integer-square predicate."""
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def generate_pythagorean_indexes(bound: int):
    """Generate all positive integer Pythagorean triples with hypotenuse<=bound.

    Returns two indexes:
      hyp[w] -> (u,v) with u^2+v^2=w^2,
      leg[u] -> (v,w) and leg[v] -> (u,w).
    """
    hyp: dict[int, list[tuple[int, int]]] = defaultdict(list)
    leg: dict[int, list[tuple[int, int]]] = defaultdict(list)
    triple_count = 0

    for m in range(2, math.isqrt(bound) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue

            u = m * m - n * n
            v = 2 * m * n
            w = m * m + n * n
            if w > bound:
                continue
            if u > v:
                u, v = v, u

            k = 1
            while k * w <= bound:
                x, y, h = k * u, k * v, k * w
                hyp[h].append((x, y))
                leg[x].append((y, h))
                leg[y].append((x, h))
                triple_count += 1
                k += 1

    return hyp, leg, triple_count


def face_mask(a: int, b: int, c: int) -> tuple[int, tuple[int | None, int | None, int | None]]:
    """Return the three face-square mask and exact diagonal witnesses."""
    values = (a * a + b * b, a * a + c * c, b * b + c * c)
    roots: list[int | None] = []
    mask = 0
    for i, value in enumerate(values):
        r = math.isqrt(value)
        if r * r == value:
            mask |= 1 << i
            roots.append(r)
        else:
            roots.append(None)
    return mask, (roots[0], roots[1], roots[2])


def enumerate_bound(bound: int) -> dict[str, Any]:
    hyp, leg, triple_count = generate_pythagorean_indexes(bound)

    masks: dict[tuple[int, int, int, int], tuple[int, tuple[int | None, int | None, int | None]]] = {}
    glued_records = 0
    primitive_glued_records = 0

    for p, face_pairs in hyp.items():
        extensions = leg.get(p)
        if not extensions:
            continue

        for x, y in face_pairs:
            for z, d in extensions:
                glued_records += 1
                a, b, c = sorted((x, y, z))

                if not (0 < a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                primitive_glued_records += 1

                key = (a, b, c, d)
                if key in masks:
                    continue
                if a * a + b * b + c * c != d * d:
                    raise ArithmeticError(f"space-diagonal identity failed: {key}")

                mask, diagonals = face_mask(a, b, c)
                if mask == 0:
                    raise ArithmeticError(f"glued record lost its integral face: {key}")
                masks[key] = (mask, diagonals)

    pair = [0, 0, 0]  # ab-ac, ab-bc, ac-bc
    exactly_two = [0, 0, 0]  # shared a, shared b, shared c
    triple = 0
    triple_witnesses: list[dict[str, int]] = []
    histogram = [0, 0, 0, 0]

    for (a, b, c, d), (mask, diagonals) in masks.items():
        k = mask.bit_count()
        histogram[k] += 1

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
            d_ab, d_ac, d_bc = diagonals
            if d_ab is None or d_ac is None or d_bc is None:
                raise ArithmeticError("triple mask without all face diagonals")
            triple_witnesses.append(
                {
                    "a": a,
                    "b": b,
                    "c": c,
                    "d": d,
                    "d_ab": d_ab,
                    "d_ac": d_ac,
                    "d_bc": d_bc,
                }
            )

    expected_exact = [pair[i] - triple for i in range(3)]
    if exactly_two != expected_exact:
        raise ArithmeticError(
            f"exactly-two identity failed: direct={exactly_two}, pair-minus-T={expected_exact}"
        )

    n2 = sum(exactly_two)
    pair_sum = sum(pair)
    if n2 != pair_sum - 3 * triple:
        raise ArithmeticError("total exactly-two identity failed")

    proportions = {
        "a": exactly_two[0] / n2 if n2 else None,
        "b": exactly_two[1] / n2 if n2 else None,
        "c": exactly_two[2] / n2 if n2 else None,
    }
    c_ratio = None
    if exactly_two[2] > 0:
        c_ratio = {
            "a": exactly_two[0] / exactly_two[2],
            "b": exactly_two[1] / exactly_two[2],
            "c": 1.0,
        }

    return {
        "B": bound,
        "raw_pair": {
            "ab_ac": pair[0],
            "ab_bc": pair[1],
            "ac_bc": pair[2],
        },
        "triple": triple,
        "exactly_two": {
            "a": exactly_two[0],
            "b": exactly_two[1],
            "c": exactly_two[2],
            "total": n2,
        },
        "exactly_two_proportion": proportions,
        "c_normalized_ratio": c_ratio,
        "face_count_histogram": {
            "exactly_one": histogram[1],
            "exactly_two": histogram[2],
            "exactly_three": histogram[3],
        },
        "triple_witnesses": triple_witnesses,
        "enumeration_diagnostics": {
            "integer_pythagorean_triples": triple_count,
            "glued_records_before_filters": glued_records,
            "primitive_glued_records_before_dedup": primitive_glued_records,
            "distinct_primitive_canonical_objects_with_at_least_one_face": len(masks),
        },
        "validation": {
            "pair_minus_triple_matches_exactly_two": True,
            "total_identity_matches": True,
            "space_diagonal_rechecked_after_dedup": True,
            "face_flags_recomputed_after_dedup": True,
            "exact_integer_square_tests_only": True,
        },
    }


def verify_historical(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_bound = {row["B"]: row for row in rows}
    checked: list[dict[str, Any]] = []

    for bound, (expected_pair, expected_triple) in EXPECTED_HISTORICAL.items():
        row = by_bound.get(bound)
        if row is None:
            continue
        got_pair = (
            row["raw_pair"]["ab_ac"],
            row["raw_pair"]["ab_bc"],
            row["raw_pair"]["ac_bc"],
        )
        got_triple = row["triple"]
        passed = got_pair == expected_pair and got_triple == expected_triple
        checked.append(
            {
                "B": bound,
                "expected_pair": list(expected_pair),
                "got_pair": list(got_pair),
                "expected_triple": expected_triple,
                "got_triple": got_triple,
                "pass": passed,
            }
        )
        if not passed:
            raise ArithmeticError(
                f"historical checksum failed at B={bound}: "
                f"expected pair/T={expected_pair}/{expected_triple}, "
                f"got={got_pair}/{got_triple}"
            )

    all_historical_present = all(bound in by_bound for bound in HISTORICAL_BOUNDS)
    return {
        "all_historical_bounds_present": all_historical_present,
        "checked_rows": checked,
        "all_checked_rows_pass": all(item["pass"] for item in checked),
        "full_historical_gate_pass": all_historical_present and len(checked) == len(HISTORICAL_BOUNDS),
    }


def build_report(bounds: tuple[int, ...]) -> dict[str, Any]:
    rows = [enumerate_bound(bound) for bound in bounds]
    historical = verify_historical(rows)
    return {
        "metadata": {
            "stage": "14-2a",
            "title": "Standalone historical two-face census reproduction",
            "counting_convention": "primitive canonical 0<a<b<c, integer space diagonal d<=B",
            "implementation": "standalone Stage14 Pythagorean-triple gluing census; no Stage13 code import",
            "bounds": list(bounds),
        },
        "rows": rows,
        "historical_reproduction": historical,
        "decision": {
            "STAGE14_2A": "COMPLETE" if historical["full_historical_gate_pass"] else "PARTIAL",
            "HISTORICAL_REPRODUCTION_PASS": historical["full_historical_gate_pass"],
            "MAX_VERIFIED_B": max(bounds),
            "EXTENSION_ABOVE_B100000_COMPLETED": max(bounds) > 100_000,
            "PERFECT_CUBOID_WITNESS_FOUND": any(row["triple"] > 0 for row in rows),
            "NEXT": "Stage14-2b extend verified census above B=100000",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=list(HISTORICAL_BOUNDS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    bounds = tuple(sorted(set(args.bounds)))
    if not bounds or bounds[0] <= 0:
        raise SystemExit("all bounds must be positive")

    report = build_report(bounds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
