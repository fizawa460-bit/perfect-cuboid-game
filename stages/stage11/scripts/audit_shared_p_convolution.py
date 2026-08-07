#!/usr/bin/env python3
"""Audit the shared-face-diagonal convolution and a two-parameter one-face family.

Stage 11 studies cuboids obtained from two right triangles sharing the
intermediate diagonal p:

    x^2 + y^2 = p^2,
    p^2 + c^2 = d^2.

The first part proves and finitely checks an exact convolution for oriented
divisor chains. The second part uses a fixed Euclid congruence class

    m ≡ 2 (mod 14), n ≡ 1 (mod 14)

to construct a two-parameter primitive family with exactly one integral face
diagonal and derive N1(B) >> B^(1/2).

No upper bound for N2(B) and no little-o comparison are claimed.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

MAX_D = 20_000
THRESHOLDS = [1_000, 2_000, 5_000, 10_000, 20_000]
RECTANGLE_T_VALUES = [100, 250, 500, 1_000, 2_000]
DEFAULT_REPORT = Path("data/shared_p_convolution_stage11_report.json")


def is_square(value: int) -> bool:
    if value < 0:
        return False
    root = math.isqrt(value)
    return root * root == value


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for prime in range(2, math.isqrt(limit) + 1):
        if spf[prime] != prime:
            continue
        for multiple in range(prime * prime, limit + 1, prime):
            if spf[multiple] == multiple:
                spf[multiple] = prime
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
    return sorted(divisors)


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


def hypotenuse_count_formula(p: int, spf: list[int]) -> int:
    product = 1
    for prime, exponent in factor_with_spf(p, spf):
        if prime % 4 == 1:
            product *= 2 * exponent + 1
    return (product - 1) // 2


def leg_count_from_divisors(p: int, bound: int, spf: list[int]) -> int:
    count = 0
    square = p * p
    for small in divisors_of_square(p, spf):
        if small >= p:
            break
        large = square // small
        if (small - large) & 1:
            continue
        if small + large <= 2 * bound:
            count += 1
    return count


def face_flags(a: int, b: int, c: int) -> dict[str, bool]:
    return {
        "ab": is_square(a * a + b * b),
        "ac": is_square(a * a + c * c),
        "bc": is_square(b * b + c * c),
    }


def enumerate_shared_p(limit: int) -> tuple[
    list[list[tuple[int, int, int, int]]],
    Counter[int],
    dict[tuple[int, int, int, int], dict[str, Any]],
    dict[str, int],
]:
    triangles = right_triangles_by_leg(limit)
    hypotenuse_counts: Counter[int] = Counter()
    for leg in range(1, limit + 1):
        for other, hypotenuse, _, _ in triangles[leg]:
            if leg < other:
                hypotenuse_counts[hypotenuse] += 1

    records: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    counters = Counter()
    for first_leg in range(1, limit + 1):
        for second_leg, p, _, _ in triangles[first_leg]:
            for remaining_leg, d, _, _ in triangles[p]:
                counters["raw_oriented_chains"] += 1
                sides = sorted((first_leg, second_leg, remaining_leg))
                if not (sides[0] < sides[1] < sides[2]):
                    counters["rejected_repeated_side"] += 1
                    continue
                if math.gcd(math.gcd(sides[0], sides[1]), sides[2]) != 1:
                    counters["rejected_nonprimitive"] += 1
                    continue
                a, b, c = sides
                key = (a, b, c, d)
                flags = face_flags(a, b, c)
                face_count = sum(flags.values())
                if face_count == 0:
                    raise ArithmeticError("generating face was lost")
                record = records.setdefault(
                    key,
                    {
                        "face_count": face_count,
                        "flags": flags,
                        "oriented_chain_count": 0,
                    },
                )
                record["oriented_chain_count"] += 1

    for key, record in records.items():
        expected = 2 * int(record["face_count"])
        if record["oriented_chain_count"] != expected:
            raise ArithmeticError(
                f"oriented multiplicity mismatch at {key}: "
                f"{record['oriented_chain_count']} != {expected}"
            )
    counters["primitive_oriented_chains"] = sum(
        int(record["oriented_chain_count"]) for record in records.values()
    )
    counters["unique_primitive_cuboids"] = len(records)
    return triangles, hypotenuse_counts, records, dict(counters)


def convolution_rows(
    triangles: list[list[tuple[int, int, int, int]]],
    hypotenuse_counts: Counter[int],
    records: dict[tuple[int, int, int, int], dict[str, Any]],
    spf: list[int],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    formula_mismatch = []
    for p in range(1, MAX_D + 1):
        enumerated = hypotenuse_counts.get(p, 0)
        formula = hypotenuse_count_formula(p, spf)
        if enumerated != formula:
            formula_mismatch.append((p, enumerated, formula))
    if formula_mismatch:
        raise ArithmeticError(f"hypotenuse formula mismatch: {formula_mismatch[:5]}")

    for bound in THRESHOLDS:
        leg_counts = {
            p: sum(1 for _, d, _, _ in triangles[p] if d <= bound)
            for p in range(1, bound + 1)
        }
        divisor_mismatches = [
            (p, leg_counts[p], leg_count_from_divisors(p, bound, spf))
            for p in range(1, bound + 1)
            if leg_counts[p] != leg_count_from_divisors(p, bound, spf)
        ]
        if divisor_mismatches:
            raise ArithmeticError(f"leg divisor formula mismatch: {divisor_mismatches[:5]}")

        raw_convolution = 2 * sum(
            hypotenuse_counts.get(p, 0) * leg_counts[p] for p in range(1, bound + 1)
        )
        direct_raw = 0
        for first_leg in range(1, bound + 1):
            for _, p, _, _ in triangles[first_leg]:
                if p > bound:
                    continue
                direct_raw += sum(1 for _, d, _, _ in triangles[p] if d <= bound)
        if raw_convolution != direct_raw:
            raise ArithmeticError("raw shared-p convolution did not match direct chain count")

        selected = [(key, record) for key, record in records.items() if key[3] <= bound]
        face_hist = Counter(int(record["face_count"]) for _, record in selected)
        primitive_weighted = sum(
            int(record["oriented_chain_count"]) for _, record in selected
        )
        weighted_identity = sum(2 * faces * count for faces, count in face_hist.items())
        if primitive_weighted != weighted_identity:
            raise ArithmeticError("primitive weighted identity failed")

        rows.append(
            {
                "B": bound,
                "raw_oriented_chains_convolution": raw_convolution,
                "raw_oriented_chains_direct": direct_raw,
                "primitive_oriented_chains": primitive_weighted,
                "unique_primitive_cuboids": len(selected),
                "face_count_histogram": {
                    str(key): value for key, value in sorted(face_hist.items())
                },
                "identity": "C_prim(B)=2*N1(B)+4*N_exact2(B)+6*N3(B)",
            }
        )
    return rows


def family_point(m: int, n: int) -> tuple[int, int, int, int, int]:
    if not (m > n >= 1):
        raise ValueError("require m>n>=1")
    x = m * m - n * n
    y = 2 * m * n
    p = m * m + n * n
    c = (p * p - 1) // 2
    d = (p * p + 1) // 2
    a, b = sorted((x, y))
    return a, b, c, d, p


def validate_two_parameter_family(max_m: int = 2_000) -> dict[str, Any]:
    examples: list[dict[str, Any]] = []
    count = 0
    for m in range(2, max_m + 1):
        if m % 14 != 2:
            continue
        for n in range(1, m):
            if n % 14 != 1 or math.gcd(m, n) != 1:
                continue
            a, b, c, d, p = family_point(m, n)
            count += 1
            if (m - n) % 2 != 1:
                raise ArithmeticError("fixed residue classes did not force opposite parity")
            if a * a + b * b != p * p:
                raise ArithmeticError("first Pythagorean identity failed")
            if p * p + c * c != d * d:
                raise ArithmeticError("second Pythagorean identity failed")
            if a * a + b * b + c * c != d * d:
                raise ArithmeticError("space diagonal identity failed")
            if math.gcd(math.gcd(a, b), c) != 1:
                raise ArithmeticError("two-parameter family was not primitive")
            if not (a < b < c):
                raise ArithmeticError("two-parameter family ordering failed")
            flags = face_flags(a, b, c)
            if sum(flags.values()) != 1 or not flags["ab"]:
                raise ArithmeticError("two-parameter family was not exactly-one-face")
            residues = ((a * a + c * c) % 7, (b * b + c * c) % 7)
            if residues != (6, 6):
                raise ArithmeticError(f"unexpected modulo-7 certificate: {residues}")
            if len(examples) < 12:
                examples.append(
                    {
                        "m": m,
                        "n": n,
                        "a": a,
                        "b": b,
                        "c": c,
                        "d": d,
                        "p": p,
                        "remaining_face_residues_mod_7": list(residues),
                    }
                )
    return {
        "max_m": max_m,
        "validated_parameter_count": count,
        "all_checks_passed": True,
        "first_examples": examples,
    }


def rectangle_count(T: int) -> int:
    total = 0
    for m in range(T + 1, 2 * T + 1):
        if m % 14 != 2:
            continue
        for n in range(1, T + 1):
            if n % 14 == 1 and math.gcd(m, n) == 1:
                total += 1
    return total


def rectangle_rows() -> list[dict[str, Any]]:
    rows = []
    main_constant = 1.0 / (24.0 * math.pi * math.pi)
    for T in RECTANGLE_T_VALUES:
        count = rectangle_count(T)
        main = main_constant * T * T
        rows.append(
            {
                "T": T,
                "coprime_parameter_pairs": count,
                "main_term_T2_over_24pi2": main,
                "ratio_to_T2": count / (T * T),
                "ratio_to_predicted_main": count / main,
                "height_bound": f"d <= (25*{T}^4+1)/2",
            }
        )
    return rows


def stage9_cross_check(
    records: dict[tuple[int, int, int, int], dict[str, Any]]
) -> dict[str, Any]:
    point = family_point(2, 1)
    key = point[:4]
    record = records.get(key)
    if record is None or int(record["face_count"]) != 1:
        raise ArithmeticError("smallest Stage11 family point missing from d<=20000 population")
    return {
        "bound": MAX_D,
        "parameter": {"m": 2, "n": 1},
        "point": list(key),
        "face_count": int(record["face_count"]),
        "flags": record["flags"],
        "exact_match": True,
    }


def build_report() -> dict[str, Any]:
    triangles, hypotenuse_counts, records, counters = enumerate_shared_p(MAX_D)
    spf = build_spf(MAX_D)
    rows = convolution_rows(triangles, hypotenuse_counts, records, spf)
    family_validation = validate_two_parameter_family()
    rectangle = rectangle_rows()
    cross_check = stage9_cross_check(records)

    return {
        "metadata": {
            "stage": 11,
            "title": "Shared-face-diagonal convolution and two-parameter lower bound",
            "generated_by": "scripts/audit_shared_p_convolution_stage11.py",
            "claim_status": (
                "The convolution identities and the N1(B) >> B^(1/2) family are "
                "unconditional. No upper bound for N2(B) and no little-o comparison are claimed."
            ),
        },
        "shared_p_convolution": {
            "hypotenuse_representation_formula": (
                "H(p)=(prod_{q|p, q=1 mod 4}(2*v_q(p)+1)-1)/2"
            ),
            "leg_representation_formula": (
                "L_B(p)=#{u|p^2: u<p, u and p^2/u have the same parity, "
                "u+p^2/u<=2B}"
            ),
            "raw_identity": "C_raw(B)=2*sum_{p<=B} H(p)*L_B(p)",
            "primitive_weighted_identity": (
                "C_prim(B)=2*N1(B)+4*N_exact2(B)+6*N3(B)"
            ),
            "structural_warning": (
                "The raw product H(p)L_B(p) does not impose gcd, distinct-side, "
                "or unique-point conditions. Primitive counting retains coupled corrections."
            ),
            "rows": rows,
            "max_bound_counters": counters,
        },
        "two_parameter_family": {
            "conditions": [
                "m>n>=1",
                "m mod 14 = 2",
                "n mod 14 = 1",
                "gcd(m,n)=1",
            ],
            "formulas": {
                "x": "m^2-n^2",
                "y": "2mn",
                "p": "m^2+n^2",
                "c": "(p^2-1)/2",
                "d": "(p^2+1)/2",
                "canonical_sides": "a=min(x,y), b=max(x,y), c",
            },
            "modulo_7_certificate": {
                "x_squared": 2,
                "y_squared": 2,
                "p_squared": 4,
                "c_squared": 4,
                "remaining_face_sums": [6, 6],
                "quadratic_residues": [0, 1, 2, 4],
            },
            "finite_validation": family_validation,
            "stage9_cross_check": cross_check,
        },
        "coprime_rectangle_count": {
            "rectangle": "T<m<=2T, 1<=n<=T, m=2 mod14, n=1 mod14",
            "mobius_formula": "C(T)=sum_{(e,14)=1} mu(e) A_e(T)B_e(T)",
            "asymptotic": "C(T)=T^2/(24*pi^2)+O(T log T)",
            "height_choice": "T=floor(((2B-1)/25)^(1/4))",
            "height_implication": "p<=5T^2 and d=(p^2+1)/2<=B",
            "lower_bound": (
                "N1(B)>=sqrt(2)/(120*pi^2)*B^(1/2)-O(B^(1/4)log B)"
            ),
            "corollary": "N1(B)>>B^(1/2)",
            "rows": rectangle,
        },
        "decision": {
            "confirmed": [
                "The raw oriented divisor-chain population has an exact shared-p convolution.",
                "Primitive unique points require coupled gcd, ordering, and multiplicity corrections.",
                "A fixed two-parameter Euclid congruence family is primitive and exactly-one-face.",
                "The two-parameter family gives the unconditional lower bound N1(B)>>B^(1/2).",
            ],
            "not_claimed": [
                "An asymptotic formula for the full N1(B) population.",
                "Any new upper bound for N2(B).",
                "N2(B)=o(N1(B)).",
                "That the finite convolution profile is an asymptotic density.",
            ],
            "next_research_question": (
                "Can the primitive correction and the extra-face correction in the shared-p "
                "convolution be bounded on average strongly enough to compare N2(B) with N1(B)?"
            ),
            "wall_bounce_recommended": True,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "raw_d20000": report["shared_p_convolution"]["rows"][-1][
                    "raw_oriented_chains_convolution"
                ],
                "primitive_d20000": report["shared_p_convolution"]["rows"][-1][
                    "primitive_oriented_chains"
                ],
                "family_validation_count": report["two_parameter_family"][
                    "finite_validation"
                ]["validated_parameter_count"],
                "lower_bound": report["coprime_rectangle_count"]["corollary"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
