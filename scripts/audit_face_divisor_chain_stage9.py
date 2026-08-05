#!/usr/bin/env python3
"""Audit the two-stage divisor-chain parameterization of face cuboids.

The audit is deliberately finite and separates exact algebraic statements
from bounded computations.  It enumerates every primitive ordered cuboid
with at least one integral face diagonal and d <= MAX_D by chaining two
integer right triangles:

    a^2 + b^2 = p^2,
    p^2 + c^2 = d^2.

Writing

    r = p-b, s = p+b, u = d-c, v = d+c

gives rs=a^2 and uv=p^2.  Conversely, same-parity divisor pairs recover the
right triangles.  A cuboid with k integral face diagonals and three distinct
positive sides therefore has exactly 2k oriented divisor-chain descriptions.

The resulting extra-square forms are recorded for later square-sieve work,
but no asymptotic theorem is claimed here.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

DEFAULT_TWO_FACE = Path("data/two_face_cuboids_1e6_fixed.json")
DEFAULT_REPORT = Path("data/face_divisor_chain_stage9_report.json")
MAX_D = 20_000
THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000]
CERTIFICATE_MODULI = [3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 24, 32, 40, 48, 64]
EXPECTED_ONE_FACE_20000 = {
    "ab_only": 12_375,
    "ac_only": 6_258,
    "bc_only": 6_079,
}


def is_square(value: int) -> bool:
    if value < 0:
        return False
    root = math.isqrt(value)
    return root * root == value


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] != p:
            continue
        start = p * p
        for multiple in range(start, limit + 1, p):
            if spf[multiple] == multiple:
                spf[multiple] = p
    return spf


def factor_with_spf(value: int, spf: list[int]) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    while value > 1:
        prime = spf[value]
        exponent = 0
        while value % prime == 0:
            value //= prime
            exponent += 1
        factors.append((prime, exponent))
    return factors


def divisors_of_square(value: int, spf: list[int]) -> list[int]:
    divisors = [1]
    for prime, exponent in factor_with_spf(value, spf):
        powers = [prime**power for power in range(1, 2 * exponent + 1)]
        divisors = divisors + [divisor * power for divisor in divisors for power in powers]
    divisors.sort()
    return divisors


def right_triangles_by_leg(limit: int) -> list[list[tuple[int, int, int, int]]]:
    """Return (other_leg, hypotenuse, small_factor, large_factor) by fixed leg."""

    spf = build_spf(limit)
    table: list[list[tuple[int, int, int, int]]] = [[] for _ in range(limit + 1)]
    for leg in range(1, limit + 1):
        square = leg * leg
        for small in divisors_of_square(leg, spf):
            if small >= leg:
                break
            large = square // small
            if (small - large) & 1:
                continue
            other = (large - small) // 2
            hypotenuse = (large + small) // 2
            if other <= 0 or hypotenuse > limit:
                continue
            if leg * leg + other * other != hypotenuse * hypotenuse:
                raise ArithmeticError("right-triangle divisor inversion failed")
            table[leg].append((other, hypotenuse, small, large))
    return table


def face_flags(a: int, b: int, c: int) -> dict[str, bool]:
    return {
        "ab": is_square(a * a + b * b),
        "ac": is_square(a * a + c * c),
        "bc": is_square(b * b + c * c),
    }


def category_from_flags(flags: dict[str, bool]) -> str:
    names = [name for name in ("ab", "ac", "bc") if flags[name]]
    if len(names) == 3:
        return "perfect"
    if len(names) == 2:
        return "+".join(names)
    if len(names) == 1:
        return f"{names[0]}_only"
    return "none"


def load_known_two_face(path: Path, max_d: int) -> dict[tuple[int, int, int, int], str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    schema = payload["metadata"]["pointSchema"]
    positions = {name: index for index, name in enumerate(schema)}
    result: dict[tuple[int, int, int, int], str] = {}
    for row in payload["points"]:
        d = int(row[positions["d"]])
        if d > max_d:
            continue
        key = tuple(int(row[positions[name]]) for name in ("a", "b", "c", "d"))
        result[key] = str(row[positions["category"]])
    return result


def enumerate_divisor_chains(max_d: int) -> tuple[
    dict[tuple[int, int, int, int], dict[str, Any]],
    dict[str, int],
]:
    triangles = right_triangles_by_leg(max_d)
    records: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    counters = Counter()

    for first_leg in range(1, max_d + 1):
        for second_leg, face_diagonal, r, s in triangles[first_leg]:
            for remaining_leg, space_diagonal, u, v in triangles[face_diagonal]:
                counters["raw_oriented_chains"] += 1
                sides = sorted((first_leg, second_leg, remaining_leg))
                if not (sides[0] < sides[1] < sides[2]):
                    counters["rejected_repeated_side"] += 1
                    continue
                if math.gcd(math.gcd(sides[0], sides[1]), sides[2]) != 1:
                    counters["rejected_nonprimitive"] += 1
                    continue
                a, b, c = sides
                d = space_diagonal
                if a * a + b * b + c * c != d * d:
                    raise ArithmeticError("space diagonal equation failed after sorting")
                key = (a, b, c, d)
                flags = face_flags(a, b, c)
                count = sum(flags.values())
                if count == 0:
                    raise ArithmeticError("divisor chain lost its generating face")
                record = records.setdefault(
                    key,
                    {
                        "flags": flags,
                        "category": category_from_flags(flags),
                        "face_count": count,
                        "oriented_chain_count": 0,
                        "sample_chain": {
                            "first_leg": first_leg,
                            "second_leg": second_leg,
                            "remaining_leg": remaining_leg,
                            "face_diagonal": face_diagonal,
                            "space_diagonal": space_diagonal,
                            "r": r,
                            "s": s,
                            "u": u,
                            "v": v,
                        },
                    },
                )
                record["oriented_chain_count"] += 1

    for key, record in records.items():
        expected = 2 * int(record["face_count"])
        if record["oriented_chain_count"] != expected:
            raise ArithmeticError(
                f"oriented-chain multiplicity failed for {key}: "
                f"{record['oriented_chain_count']} != {expected}"
            )
    counters["unique_primitive_cuboids"] = len(records)
    counters["primitive_oriented_chains"] = sum(
        int(record["oriented_chain_count"]) for record in records.values()
    )
    return records, dict(counters)


def threshold_rows(records: dict[tuple[int, int, int, int], dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for bound in THRESHOLDS:
        selected = [(key, record) for key, record in records.items() if key[3] <= bound]
        categories = Counter(record["category"] for _, record in selected)
        face_hist = Counter(str(record["face_count"]) for _, record in selected)
        exactly_one = face_hist.get("1", 0)
        at_least_two = face_hist.get("2", 0) + face_hist.get("3", 0)
        total = exactly_one + at_least_two
        primitive_chains = sum(int(record["oriented_chain_count"]) for _, record in selected)
        extra_chains = sum(
            int(record["oriented_chain_count"])
            for _, record in selected
            if int(record["face_count"]) >= 2
        )
        rows.append(
            {
                "B": bound,
                "unique_at_least_one_face": total,
                "exactly_one_face": exactly_one,
                "at_least_two_faces": at_least_two,
                "face_count_histogram": dict(sorted(face_hist.items())),
                "category_counts": dict(sorted(categories.items())),
                "extra_square_point_pass_rate": at_least_two / total if total else 0.0,
                "primitive_oriented_chain_count": primitive_chains,
                "extra_square_oriented_chain_pass_rate": (
                    extra_chains / primitive_chains if primitive_chains else 0.0
                ),
            }
        )
    return rows


def square_residues(modulus: int) -> set[int]:
    return {value * value % modulus for value in range(modulus)}


def non_generating_face_sums(
    key: tuple[int, int, int, int], record: dict[str, Any]
) -> tuple[int, int] | None:
    if int(record["face_count"]) != 1:
        return None
    a, b, c, _ = key
    flags = record["flags"]
    values = {
        "ab": a * a + b * b,
        "ac": a * a + c * c,
        "bc": b * b + c * c,
    }
    missing = [values[name] for name in ("ab", "ac", "bc") if not flags[name]]
    if len(missing) != 2:
        raise ArithmeticError("exactly-one record did not have two missing diagonals")
    return missing[0], missing[1]


def congruence_certificate_audit(
    records: dict[tuple[int, int, int, int], dict[str, Any]]
) -> dict[str, Any]:
    exactly_one_records = [
        (key, record) for key, record in records.items() if int(record["face_count"]) == 1
    ]
    all_records = list(records.items())
    certified_union: set[tuple[int, int, int, int]] = set()
    rows: list[dict[str, Any]] = []

    for modulus in CERTIFICATE_MODULI:
        squares = square_residues(modulus)
        certified: set[tuple[int, int, int, int]] = set()
        category_counts = Counter()
        residue_classes = Counter()
        false_positive = 0

        for key, record in exactly_one_records:
            missing = non_generating_face_sums(key, record)
            assert missing is not None
            if all(value % modulus not in squares for value in missing):
                certified.add(key)
                category_counts[record["category"]] += 1
                residue_classes[
                    (record["category"], key[0] % modulus, key[1] % modulus, key[2] % modulus)
                ] += 1

        for key, record in all_records:
            if int(record["face_count"]) == 1:
                continue
            a, b, c, _ = key
            flags = record["flags"]
            values = {
                "ab": a * a + b * b,
                "ac": a * a + c * c,
                "bc": b * b + c * c,
            }
            for sole_face in ("ab", "ac", "bc"):
                missing_names = [name for name in ("ab", "ac", "bc") if name != sole_face]
                if all(values[name] % modulus not in squares for name in missing_names):
                    false_positive += 1
        if false_positive:
            raise ArithmeticError(f"congruence certificate false positive modulo {modulus}")

        certified_union.update(certified)
        rows.append(
            {
                "modulus": modulus,
                "certified_exactly_one_count": len(certified),
                "coverage_fraction": len(certified) / len(exactly_one_records),
                "category_counts": dict(sorted(category_counts.items())),
                "top_certifying_residue_classes": [
                    {
                        "category": residue[0],
                        "a_mod_M": residue[1],
                        "b_mod_M": residue[2],
                        "c_mod_M": residue[3],
                        "count": count,
                    }
                    for residue, count in residue_classes.most_common(12)
                ],
                "false_positive_count_on_at_least_two_face_points": false_positive,
            }
        )

    rows.sort(key=lambda row: (-row["certified_exactly_one_count"], row["modulus"]))
    return {
        "tested_moduli": CERTIFICATE_MODULI,
        "exactly_one_population": len(exactly_one_records),
        "union_certified_count": len(certified_union),
        "union_coverage_fraction": len(certified_union) / len(exactly_one_records),
        "best_single_modulus": rows[0] if rows else None,
        "per_modulus": rows,
        "scope_note": (
            "A residue certificate is a rigorous sufficient condition for the two remaining "
            "face sums to be nonsquares.  Finite coverage is not an asymptotic lower-bound family."
        ),
    }


def compare_known_two_face(
    records: dict[tuple[int, int, int, int], dict[str, Any]], known_path: Path
) -> dict[str, Any]:
    known = load_known_two_face(known_path, MAX_D)
    generated = {
        key: record["category"]
        for key, record in records.items()
        if int(record["face_count"]) >= 2
    }
    missing = sorted(set(known) - set(generated))
    extra = sorted(set(generated) - set(known))
    category_mismatch = sorted(
        {
            key: {"known": known[key], "generated": generated[key]}
            for key in set(known) & set(generated)
            if known[key] != generated[key]
        }.items()
    )
    if missing or extra or category_mismatch:
        raise ArithmeticError(
            "divisor-chain two-face set did not match the fixed d<=20000 dataset"
        )
    return {
        "known_two_face_count": len(known),
        "generated_two_face_count": len(generated),
        "missing_count": len(missing),
        "extra_count": len(extra),
        "category_mismatch_count": len(category_mismatch),
        "exact_match": True,
    }


def build_report(known_path: Path) -> dict[str, Any]:
    records, counters = enumerate_divisor_chains(MAX_D)
    thresholds = threshold_rows(records)
    final_row = thresholds[-1]
    one_face_counts = {
        name: int(final_row["category_counts"].get(name, 0))
        for name in ("ab_only", "ac_only", "bc_only")
    }
    expected_match = one_face_counts == EXPECTED_ONE_FACE_20000
    if not expected_match:
        raise ArithmeticError(
            f"d<=20000 one-face counts changed: {one_face_counts} != {EXPECTED_ONE_FACE_20000}"
        )

    report = {
        "metadata": {
            "max_d": MAX_D,
            "thresholds": THRESHOLDS,
            "primitive": "gcd(a,b,c)=1",
            "ordering": "a<b<c",
            "source_two_face_dataset": str(known_path),
        },
        "exact_divisor_chain_bijection": {
            "first_triangle": [
                "r=p-b, s=p+b, rs=a^2",
                "b=(s-r)/2, p=(s+r)/2",
            ],
            "second_triangle": [
                "u=d-c, v=d+c, uv=p^2",
                "c=(v-u)/2, d=(v+u)/2",
            ],
            "parity_condition": "r,s have the same parity and u,v have the same parity",
            "oriented_multiplicity_theorem": (
                "for three distinct positive sides, a cuboid with k integral face diagonals "
                "has exactly 2k oriented divisor-chain descriptions"
            ),
            "all_enumerated_multiplicities_verified": True,
        },
        "extra_square_forms": {
            "for_a_c_diagonal": "4*a^2+(v-u)^2 = 4*r*s+(v-u)^2 must be a square",
            "for_b_c_diagonal": "(s-r)^2+(v-u)^2 must be a square",
            "domain_constraints": [
                "r*s is a square",
                "u*v=((r+s)/2)^2",
                "r<s and u<v",
                "same-parity divisor pairs",
            ],
            "tractability_status": (
                "explicit square conditions obtained, but the variables remain coupled by "
                "multiplicative square/divisor constraints; a standard independent-box square "
                "sieve does not apply without a further reparameterization"
            ),
        },
        "enumeration_counters": counters,
        "threshold_rows": thresholds,
        "published_d20000_one_face_counts": {
            "expected": EXPECTED_ONE_FACE_20000,
            "generated": one_face_counts,
            "exact_match": expected_match,
        },
        "known_two_face_comparison": compare_known_two_face(records, known_path),
        "congruence_certificates": congruence_certificate_audit(records),
        "decision": {
            "divisor_chain_is_complete_at_a_fixed_generating_face": True,
            "d20000_population_reproduced": True,
            "extra_square_condition_is_explicit": True,
            "standard_square_sieve_ready_without_reparameterization": False,
            "one_face_lower_bound_family_proved": False,
            "recommended_next_task": (
                "search for a low-dimensional Euclidean/Pythagorean reparameterization or a "
                "fixed congruence subfamily that yields many primitive exactly-one points; if no "
                "such family appears, compare determinant-method formulations"
            ),
            "wall_discussion_recommended_after_stage9": True,
        },
        "scope_warning": (
            "All counts and coverage fractions are finite d<=20000 computations.  They do not "
            "prove N2(B)=o(N1(B)), a power-saving upper bound, or an asymptotic lower bound."
        ),
    }
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--known-two-face", type=Path, default=DEFAULT_TWO_FACE)
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.known_two_face)
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    final = report["threshold_rows"][-1]
    print(
        json.dumps(
            {
                "valid": True,
                "max_d": MAX_D,
                "exactly_one_face": final["exactly_one_face"],
                "at_least_two_faces": final["at_least_two_faces"],
                "extra_square_point_pass_rate": final["extra_square_point_pass_rate"],
                "congruence_union_coverage": report["congruence_certificates"][
                    "union_coverage_fraction"
                ],
                "square_sieve_ready": report["decision"][
                    "standard_square_sieve_ready_without_reparameterization"
                ],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
