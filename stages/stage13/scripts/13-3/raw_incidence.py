#!/usr/bin/env python3
"""Stage13-3a raw directional incidence audit.

Enumerate canonical primitive cuboid candidates that have an integer space
diagonal and at least one integer face diagonal. The enumeration is built
from two nested Pythagorean triples:

    x^2 + y^2 = p^2,
    p^2 + t^2 = d^2.

After sorting (x, y, t) as a < b < c, the distinguished integer face is
classified as ab, ac, or bc. OR-ing the face bits for the same
(a, b, c, d) recovers raw incidence and overlap data without assuming the
exact-one condition.

The calculation is finite and observational; it does not assert an
asymptotic ratio.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path


FACE_BITS = {"ab": 1, "ac": 2, "bc": 4}
DEFAULT_CHECKPOINTS = (1000, 3000, 10000, 30000, 100000)


def pythagorean_triples(hypotenuse_max: int):
    """Yield every positive integer right triangle x<y with z<=hypotenuse_max."""
    for m in range(2, isqrt(hypotenuse_max) + 2):
        m2 = m * m
        for n in range(1, m):
            z0 = m2 + n * n
            if z0 > hypotenuse_max:
                break
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue

            x0 = m2 - n * n
            y0 = 2 * m * n
            if x0 > y0:
                x0, y0 = y0, x0

            for k in range(1, hypotenuse_max // z0 + 1):
                yield k * x0, k * y0, k * z0


def build_incidence_masks(b_max: int):
    triples = list(pythagorean_triples(b_max))
    by_hypotenuse = defaultdict(list)
    for x, y, z in triples:
        by_hypotenuse[z].append((x, y))

    masks = {}
    incidence_records = 0

    for leg1, leg2, d in triples:
        # Either outer leg can be the distinguished integer face diagonal p.
        for p, t in ((leg1, leg2), (leg2, leg1)):
            inner_representations = by_hypotenuse.get(p)
            if not inner_representations:
                continue

            for x, y in inner_representations:
                # Stage13 is primitive at the cuboid-edge level.
                if gcd(gcd(x, y), t) != 1:
                    continue

                a, b, c = sorted((x, y, t))
                if a == b or b == c:
                    continue

                face = frozenset((x, y))
                if face == frozenset((a, b)):
                    bit = FACE_BITS["ab"]
                elif face == frozenset((a, c)):
                    bit = FACE_BITS["ac"]
                elif face == frozenset((b, c)):
                    bit = FACE_BITS["bc"]
                else:
                    raise AssertionError("distinguished face did not survive sorting")

                key = (a, b, c, d)
                masks[key] = masks.get(key, 0) | bit
                incidence_records += 1

    return triples, masks, incidence_records


def snapshot(masks, b: int):
    raw = {"ab": 0, "ac": 0, "bc": 0}
    exact_one = {"ab": 0, "ac": 0, "bc": 0}
    pair = {"ab_ac": 0, "ab_bc": 0, "ac_bc": 0}
    triple = 0
    objects_with_incidence = 0

    for (_, _, _, d), mask in masks.items():
        if d > b:
            continue

        objects_with_incidence += 1

        if mask & FACE_BITS["ab"]:
            raw["ab"] += 1
        if mask & FACE_BITS["ac"]:
            raw["ac"] += 1
        if mask & FACE_BITS["bc"]:
            raw["bc"] += 1

        if mask == FACE_BITS["ab"]:
            exact_one["ab"] += 1
        elif mask == FACE_BITS["ac"]:
            exact_one["ac"] += 1
        elif mask == FACE_BITS["bc"]:
            exact_one["bc"] += 1

        if mask & FACE_BITS["ab"] and mask & FACE_BITS["ac"]:
            pair["ab_ac"] += 1
        if mask & FACE_BITS["ab"] and mask & FACE_BITS["bc"]:
            pair["ab_bc"] += 1
        if mask & FACE_BITS["ac"] and mask & FACE_BITS["bc"]:
            pair["ac_bc"] += 1
        if mask == 7:
            triple += 1

    raw_total = sum(raw.values())
    bc = raw["bc"]
    raw_bc_normalized = {
        key: (value / bc if bc else None) for key, value in raw.items()
    }
    raw_proportions = {
        key: (value / raw_total if raw_total else None) for key, value in raw.items()
    }

    exact_total = sum(exact_one.values())
    exact_bc = exact_one["bc"]
    exact_bc_normalized = {
        key: (value / exact_bc if exact_bc else None)
        for key, value in exact_one.items()
    }

    return {
        "B": b,
        "objects_with_at_least_one_integer_face": objects_with_incidence,
        "raw_incidence": raw,
        "raw_incidence_total": raw_total,
        "raw_bc_normalized": raw_bc_normalized,
        "raw_proportions": raw_proportions,
        "pair_overlaps_including_triple": pair,
        "triple_overlap": triple,
        "exact_one_diagnostic": exact_one,
        "exact_one_total_diagnostic": exact_total,
        "exact_one_bc_normalized_diagnostic": exact_bc_normalized,
    }


def parse_checkpoints(text: str):
    values = sorted({int(part) for part in text.split(",") if part.strip()})
    if not values or values[0] < 1:
        raise ValueError("checkpoints must be positive integers")
    return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--checkpoints",
        default=",".join(map(str, DEFAULT_CHECKPOINTS)),
        help="comma-separated d cutoffs",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="optional JSON output path; stdout is always printed",
    )
    args = parser.parse_args()

    checkpoints = parse_checkpoints(args.checkpoints)
    b_max = max(checkpoints)

    triples, masks, incidence_records = build_incidence_masks(b_max)
    result = {
        "task": "Stage13-3a",
        "status": "FINITE_COMPUTATION_ONLY",
        "counting_convention": {
            "canonical_order": "a<b<c",
            "primitive": "gcd(a,b,c)=1",
            "space_diagonal": "a^2+b^2+c^2=d^2",
            "cutoff": "d<=B",
            "raw_incidence": "integer face counted before exact-one sieve",
        },
        "enumeration": {
            "method": "nested Pythagorean triples",
            "B_max": b_max,
            "pythagorean_triples_with_hypotenuse_le_B_max": len(triples),
            "primitive_distinguished_incidence_records_before_face_union": incidence_records,
            "distinct_canonical_objects_with_incidence_at_B_max": len(masks),
        },
        "checkpoints": [snapshot(masks, b) for b in checkpoints],
        "validation": {
            "B": 100000 if b_max >= 100000 else None,
            "expected_exact_one_if_B_100000": {
                "ab": 84146,
                "ac": 43180,
                "bc": 40704,
            }
            if b_max >= 100000
            else None,
        },
        "interpretation_guardrail": (
            "Raw-incidence ratios at finite B are diagnostics only; "
            "no limiting 2:1:1 ratio is asserted."
        ),
    }

    if b_max >= 100000:
        observed = next(
            row["exact_one_diagnostic"]
            for row in result["checkpoints"]
            if row["B"] == 100000
        )
        expected = result["validation"]["expected_exact_one_if_B_100000"]
        result["validation"]["exact_one_B_100000_matches_stage13_1"] = (
            observed == expected
        )

    text = json.dumps(result, indent=2, sort_keys=False) + "\n"
    print(text, end="")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
