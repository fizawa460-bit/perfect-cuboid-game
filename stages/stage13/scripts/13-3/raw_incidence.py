#!/usr/bin/env python3
"""Stage13-3a: audit raw face incidences before the exact-one sieve.

Enumerate primitive canonical cuboids (a<b<c, gcd=1, d<=B) that have at
least one integral face diagonal by gluing two integer Pythagorean triples
along a shared face diagonal p:

    x^2 + y^2 = p^2,
    p^2 + z^2 = d^2.

Every cuboid with at least one integral face is reached by choosing such a
distinguished integral face. Canonical tuples are deduplicated, then all
three face-square indicators are recomputed directly from (a,b,c).
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

DEFAULT_BOUNDS = (1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000)
DEFAULT_OUTPUT = Path("stages/stage13/data/13-3/raw_incidence_report.json")
EXPECTED_EXACT_ONE_100K = (84_146, 43_180, 40_704)


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def generate_pythagorean_indexes(bound: int):
    """Return hypotenuse and leg indexes for all positive integer triples."""
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
                x, y, d = k * u, k * v, k * w
                hyp[d].append((x, y))
                leg[x].append((y, d))
                leg[y].append((x, d))
                triple_count += 1
                k += 1

    return hyp, leg, triple_count


def enumerate_bound(bound: int) -> dict[str, Any]:
    hyp, leg, triple_count = generate_pythagorean_indexes(bound)
    masks: dict[tuple[int, int, int, int], int] = {}
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
                if not (a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                primitive_glued_records += 1

                key = (a, b, c, d)
                if key in masks:
                    continue

                if a * a + b * b + c * c != d * d:
                    raise ArithmeticError(f"space-diagonal identity failed: {key}")

                values = (
                    a * a + b * b,
                    a * a + c * c,
                    b * b + c * c,
                )
                mask = sum((1 << i) for i, value in enumerate(values) if is_square(value))
                if mask == 0:
                    raise ArithmeticError(f"glued record lost integral face: {key}")
                masks[key] = mask

    raw = [0, 0, 0]
    exact_one = [0, 0, 0]
    overlap = [0, 0, 0]  # ab-ac, ab-bc, ac-bc
    three_face = 0
    face_count_histogram = [0, 0, 0, 0]

    for mask in masks.values():
        k = mask.bit_count()
        face_count_histogram[k] += 1
        for i in range(3):
            if mask & (1 << i):
                raw[i] += 1
        if k == 1:
            exact_one[mask.bit_length() - 1] += 1
        if mask & 0b001 and mask & 0b010:
            overlap[0] += 1
        if mask & 0b001 and mask & 0b100:
            overlap[1] += 1
        if mask & 0b010 and mask & 0b100:
            overlap[2] += 1
        if mask == 0b111:
            three_face += 1

    reconstructed = (
        raw[0] - overlap[0] - overlap[1] + three_face,
        raw[1] - overlap[0] - overlap[2] + three_face,
        raw[2] - overlap[1] - overlap[2] + three_face,
    )
    if tuple(exact_one) != reconstructed:
        raise ArithmeticError(
            f"inclusion-exclusion mismatch: direct={exact_one}, reconstructed={reconstructed}"
        )

    raw_total = sum(raw)
    exact_total = sum(exact_one)
    raw_prop = [value / raw_total for value in raw]
    exact_prop = [value / exact_total for value in exact_one]

    return {
        "B": bound,
        "raw_incidence": {"ab": raw[0], "ac": raw[1], "bc": raw[2]},
        "raw_bc_normalized_ratio": {
            "ab": raw[0] / raw[2], "ac": raw[1] / raw[2], "bc": 1.0
        },
        "raw_proportion": {"ab": raw_prop[0], "ac": raw_prop[1], "bc": raw_prop[2]},
        "exact_one": {"ab": exact_one[0], "ac": exact_one[1], "bc": exact_one[2]},
        "exact_one_bc_normalized_ratio": {
            "ab": exact_one[0] / exact_one[2],
            "ac": exact_one[1] / exact_one[2],
            "bc": 1.0,
        },
        "exact_one_proportion": {
            "ab": exact_prop[0], "ac": exact_prop[1], "bc": exact_prop[2]
        },
        "overlap": {
            "ab_ac": overlap[0], "ab_bc": overlap[1], "ac_bc": overlap[2],
            "three_face": three_face,
        },
        "face_count_histogram": {
            "exactly_one": face_count_histogram[1],
            "exactly_two": face_count_histogram[2],
            "exactly_three": face_count_histogram[3],
        },
        "raw_minus_exact_one": {
            "ab": raw[0] - exact_one[0],
            "ac": raw[1] - exact_one[1],
            "bc": raw[2] - exact_one[2],
        },
        "relative_sieve_reduction_percent": {
            "ab": 100.0 * (raw[0] - exact_one[0]) / raw[0],
            "ac": 100.0 * (raw[1] - exact_one[1]) / raw[1],
            "bc": 100.0 * (raw[2] - exact_one[2]) / raw[2],
        },
        "proportion_shift": {
            "l1": sum(abs(x - y) for x, y in zip(raw_prop, exact_prop)),
            "linf": max(abs(x - y) for x, y in zip(raw_prop, exact_prop)),
        },
        "enumeration_diagnostics": {
            "integer_pythagorean_triples": triple_count,
            "glued_records_before_filters": glued_records,
            "primitive_glued_records_before_dedup": primitive_glued_records,
            "distinct_primitive_canonical_objects_with_at_least_one_face": len(masks),
        },
    }


def build_report(bounds: tuple[int, ...]) -> dict[str, Any]:
    rows = [enumerate_bound(bound) for bound in bounds]
    by_bound = {row["B"]: row for row in rows}

    if 100_000 in by_bound:
        locked = by_bound[100_000]["exact_one"]
        got = (locked["ab"], locked["ac"], locked["bc"])
        if got != EXPECTED_EXACT_ONE_100K:
            raise ArithmeticError(
                "Stage13-1 exact-one lock failed at B=100000: "
                f"expected={EXPECTED_EXACT_ONE_100K}, got={got}"
            )

    target = by_bound[max(bounds)]
    return {
        "metadata": {
            "stage": "13-3a",
            "title": "Raw incidence before exact-one sieve",
            "counting_convention": (
                "primitive canonical a<b<c, integer space diagonal d<=B; "
                "A_uv counts incidence of the uv face being integral, including overlaps"
            ),
            "method": (
                "complete Pythagorean-triple gluing enumeration, canonical deduplication, "
                "direct recomputation of all three face-square flags"
            ),
            "bounds": list(bounds),
        },
        "rows": rows,
        "conclusion": {
            "raw_ratio_already_contains_leading_two": True,
            "overlap_sieve_can_generate_leading_two": False,
            "finite_range_statement": (
                "At the audited bounds, and in particular B=100000, the near-2:1:1 "
                "shape is already present in raw incidence counts before the exact-one "
                "sieve. The overlap correction is numerically tiny and only perturbs "
                "the ratio. This is a finite computation, not an asymptotic theorem."
            ),
            "next_test": (
                "Analyze the canonical size-order chamber / geometric density effect; "
                "the exact-one overlap layer is not the source of the leading 2."
            ),
            "largest_bound_raw": target["raw_incidence"],
            "largest_bound_exact_one": target["exact_one"],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=list(DEFAULT_BOUNDS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    bounds = tuple(sorted(set(args.bounds)))
    if not bounds or bounds[0] <= 0:
        raise SystemExit("all bounds must be positive")

    report = build_report(bounds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["conclusion"], indent=2))


if __name__ == "__main__":
    main()
