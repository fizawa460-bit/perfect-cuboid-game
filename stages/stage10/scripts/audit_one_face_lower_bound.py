#!/usr/bin/env python3
"""Audit an explicit primitive family with exactly one integral face diagonal.

For every even integer m >= 2 define the two linked Pythagorean triples

    x = 2m,
    y = m^2 - 1,
    p = m^2 + 1,

and

    c = (p^2 - 1) / 2,
    d = (p^2 + 1) / 2.

Then x^2+y^2=p^2 and p^2+c^2=d^2.  If

    m mod 14 in {2, 4, 10, 12},

the two remaining face sums are quadratic nonresidues modulo 7, so the
resulting primitive cuboid has exactly one integral face diagonal.

The script checks the symbolic identities, the complete residue table,
a finite prefix of the family, and compatibility with the Stage9 exhaustive
enumeration.  It records an unconditional lower bound

    N_1(B) >= 4 floor(floor(B^(1/4))/14),

hence N_1(B) >> B^(1/4).  No assertion about N_2(B) is made.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import sympy as sp

DEFAULT_REPORT = Path("data/one_face_lower_bound_stage10_report.json")
STAGE9_BOUND = 20_000
DEFAULT_VALIDATION_MAX_M = 10_000
SUCCESSFUL_CLASSES_MOD_14 = (2, 4, 10, 12)
REPORT_BOUNDS = (20_000, 1_000_000, 100_000_000, 1_000_000_000_000)


def is_square(value: int) -> bool:
    if value < 0:
        return False
    root = math.isqrt(value)
    return root * root == value


def face_flags(a: int, b: int, c: int) -> dict[str, bool]:
    return {
        "ab": is_square(a * a + b * b),
        "ac": is_square(a * a + c * c),
        "bc": is_square(b * b + c * c),
    }


def family_point(m: int) -> tuple[int, int, int, int, int]:
    if m < 2 or m % 2:
        raise ValueError("m must be even and at least 2")
    first_leg = 2 * m
    second_leg = m * m - 1
    p = m * m + 1
    c = (p * p - 1) // 2
    d = (p * p + 1) // 2
    a, b = sorted((first_leg, second_leg))
    return a, b, c, d, p


def is_certified_parameter(m: int) -> bool:
    return m >= 2 and m % 14 in SUCCESSFUL_CLASSES_MOD_14


def symbolic_identity_audit() -> dict[str, Any]:
    m = sp.symbols("m", integer=True, positive=True)
    x = 2 * m
    y = m**2 - 1
    p = m**2 + 1
    c = (p**2 - 1) / 2
    d = (p**2 + 1) / 2

    identities = {
        "first_pythagorean_identity": sp.expand(x**2 + y**2 - p**2),
        "second_pythagorean_identity": sp.expand(p**2 + c**2 - d**2),
        "space_diagonal_identity": sp.expand(x**2 + y**2 + c**2 - d**2),
        "c_formula": sp.expand(c - m**2 * (m**2 + 2) / 2),
        "d_formula": sp.expand(d - (m**4 + 2 * m**2 + 2) / 2),
        "c_minus_y": sp.expand(c - y - (m**4 / 2 + 1)),
        "d_height_gap": sp.expand(m**4 - d - (m**4 - 2 * m**2 - 2) / 2),
    }
    if any(value != 0 for value in identities.values()):
        raise ArithmeticError(f"symbolic identity failed: {identities}")

    derivative = sp.diff(d, m)
    if sp.expand(derivative - (2 * m**3 + 2 * m)) != 0:
        raise ArithmeticError("height derivative identity failed")

    return {
        "identities": {name: str(value) for name, value in identities.items()},
        "height_derivative": str(derivative),
        "proof_notes": [
            "gcd(2m,m^2-1)=1 for even m: any common divisor divides m and m^2-1, while m^2-1 is odd.",
            "c>m^2-1 because c-(m^2-1)=m^4/2+1>0.",
            "c>2m for m>=2 by direct factorization or monotonicity.",
            "d is strictly increasing for m>0 because d'(m)=2m^3+2m>0.",
            "d<=m^4 for m>=2 because m^4-2m^2-2>0 when m^2>=4.",
        ],
    }


def residue_audit() -> dict[str, Any]:
    modulus = 7
    squares = {value * value % modulus for value in range(modulus)}
    rows: list[dict[str, Any]] = []
    successful: list[int] = []

    for residue_mod_14 in range(0, 14, 2):
        m = residue_mod_14
        q = (m * m) % modulus
        x2 = (4 * q) % modulus
        y2 = ((q - 1) ** 2) % modulus
        inverse_two = pow(2, -1, modulus)
        c_mod = (q * (q + 2) * inverse_two) % modulus
        c2 = c_mod * c_mod % modulus
        ac_sum = (x2 + c2) % modulus
        bc_sum = (y2 + c2) % modulus
        certificate = ac_sum not in squares and bc_sum not in squares
        if certificate:
            successful.append(residue_mod_14)
        rows.append(
            {
                "m_mod_14": residue_mod_14,
                "m_squared_mod_7": q,
                "(2m)^2_mod_7": x2,
                "(m^2-1)^2_mod_7": y2,
                "c_mod_7": c_mod,
                "c^2_mod_7": c2,
                "remaining_face_sums_mod_7": [ac_sum, bc_sum],
                "both_nonresidues": certificate,
            }
        )

    if tuple(successful) != SUCCESSFUL_CLASSES_MOD_14:
        raise ArithmeticError(
            f"unexpected successful residue classes: {successful}"
        )

    return {
        "modulus": modulus,
        "square_residues": sorted(squares),
        "successful_even_classes_mod_14": successful,
        "rows": rows,
        "conclusion": (
            "For every m in the successful classes, both non-generating face sums "
            "are quadratic nonresidues modulo 7 and therefore cannot be integer squares."
        ),
    }


def validate_family_prefix(max_m: int) -> dict[str, Any]:
    eligible = [m for m in range(2, max_m + 1) if is_certified_parameter(m)]
    examples: list[dict[str, Any]] = []
    previous_d = -1

    for m in eligible:
        a, b, c, d, p = family_point(m)
        if not (a < b < c):
            raise ArithmeticError(f"ordering failed at m={m}: {(a,b,c)}")
        if math.gcd(math.gcd(a, b), c) != 1:
            raise ArithmeticError(f"primitivity failed at m={m}")
        if a * a + b * b != p * p:
            raise ArithmeticError(f"generating face failed at m={m}")
        if p * p + c * c != d * d:
            raise ArithmeticError(f"space diagonal failed at m={m}")
        flags = face_flags(a, b, c)
        if flags != {"ab": True, "ac": False, "bc": False}:
            raise ArithmeticError(f"exactly-one condition failed at m={m}: {flags}")
        if (a * a + c * c) % 7 in {0, 1, 2, 4}:
            raise ArithmeticError(f"first modulo-7 certificate failed at m={m}")
        if (b * b + c * c) % 7 in {0, 1, 2, 4}:
            raise ArithmeticError(f"second modulo-7 certificate failed at m={m}")
        if d <= previous_d:
            raise ArithmeticError("family height was not strictly increasing")
        previous_d = d
        if len(examples) < 12:
            examples.append(
                {
                    "m": m,
                    "a": a,
                    "b": b,
                    "c": c,
                    "d": d,
                    "p": p,
                    "remaining_face_residues_mod_7": [
                        (a * a + c * c) % 7,
                        (b * b + c * c) % 7,
                    ],
                }
            )

    return {
        "max_m": max_m,
        "eligible_parameter_count": len(eligible),
        "all_checks_passed": True,
        "first_examples": examples,
    }


def stage9_cross_check(bound: int) -> dict[str, Any]:
    from audit_face_divisor_chain_stage9 import enumerate_divisor_chains

    records, _ = enumerate_divisor_chains(bound)
    parameters: list[int] = []
    checked_points: list[dict[str, Any]] = []

    m = 2
    while True:
        a, b, c, d, _ = family_point(m)
        if d > bound:
            break
        if is_certified_parameter(m):
            parameters.append(m)
            key = (a, b, c, d)
            record = records.get(key)
            if record is None:
                raise ArithmeticError(f"Stage9 population missed family point {key}")
            if int(record["face_count"]) != 1 or record["category"] != "ab_only":
                raise ArithmeticError(
                    f"Stage9 classification mismatch for {key}: {record}"
                )
            checked_points.append(
                {
                    "m": m,
                    "point": [a, b, c, d],
                    "stage9_category": record["category"],
                }
            )
        m += 2

    expected_parameters = [2, 4, 10, 12] if bound == STAGE9_BOUND else parameters
    if parameters != expected_parameters:
        raise ArithmeticError(
            f"unexpected family parameters below d<={bound}: {parameters}"
        )

    return {
        "bound": bound,
        "parameters": parameters,
        "matched_count": len(checked_points),
        "all_present_and_exactly_one": True,
        "points": checked_points,
    }


def integer_fourth_root(value: int) -> int:
    if value < 0:
        raise ValueError("value must be nonnegative")
    root = math.isqrt(math.isqrt(value))
    while (root + 1) ** 4 <= value:
        root += 1
    while root**4 > value:
        root -= 1
    return root


def exact_family_count(bound: int) -> int:
    count = 0
    m = 2
    while True:
        _, _, _, d, _ = family_point(m)
        if d > bound:
            break
        if is_certified_parameter(m):
            count += 1
        m += 2
    return count


def lower_bound_audit() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for bound in REPORT_BOUNDS:
        fourth_root = integer_fourth_root(bound)
        guaranteed = sum(
            max(0, (fourth_root - residue) // 14 + 1)
            for residue in SUCCESSFUL_CLASSES_MOD_14
        )
        simple_block_bound = 4 * (fourth_root // 14)
        exact = exact_family_count(bound)
        if exact < guaranteed:
            raise ArithmeticError(
                f"exact family count {exact} below guaranteed count {guaranteed}"
            )
        rows.append(
            {
                "B": bound,
                "floor_B_fourth_root": fourth_root,
                "explicit_guaranteed_count": guaranteed,
                "simple_block_lower_bound": simple_block_bound,
                "exact_family_count": exact,
            }
        )

    return {
        "pointwise_bound": (
            "N1(B) >= sum_{r in {2,4,10,12}} "
            "max(0, floor((floor(B^(1/4))-r)/14)+1)"
        ),
        "simple_corollary": "N1(B) >= 4*floor(floor(B^(1/4))/14)",
        "asymptotic_bound": "N1(B) >= (2/7)B^(1/4)-O(1), hence N1(B) >> B^(1/4)",
        "density_of_admissible_m": "4 residue classes modulo 14, i.e. 2/7 of all positive integers",
        "height_inequality": "d(m)=(m^4+2m^2+2)/2 <= m^4 for m>=2",
        "injectivity": "d(m) is strictly increasing for m>0",
        "rows": rows,
    }


def build_report(validation_max_m: int, skip_stage9_cross_check: bool) -> dict[str, Any]:
    report: dict[str, Any] = {
        "metadata": {
            "stage": 10,
            "title": "Explicit primitive exactly-one-face family",
            "generated_by": "scripts/audit_one_face_lower_bound_stage10.py",
            "claim_status": (
                "The family and B^(1/4) lower bound are unconditional. "
                "No upper bound for N2(B) and no little-o comparison are claimed."
            ),
        },
        "family": {
            "parameter_conditions": [
                "m>=2",
                "m mod 14 in {2,4,10,12}",
            ],
            "generating_legs": ["2m", "m^2-1"],
            "face_diagonal": "p=m^2+1",
            "remaining_leg": "c=m^2(m^2+2)/2",
            "space_diagonal": "d=(m^4+2m^2+2)/2",
            "canonical_order": "sort(2m,m^2-1), followed by c",
        },
        "symbolic_identity_audit": symbolic_identity_audit(),
        "congruence_certificate": residue_audit(),
        "finite_validation": validate_family_prefix(validation_max_m),
        "stage9_cross_check": (
            {"skipped": True}
            if skip_stage9_cross_check
            else stage9_cross_check(STAGE9_BOUND)
        ),
        "lower_bound": lower_bound_audit(),
        "decision": {
            "confirmed": [
                "An explicit infinite primitive family with exactly one integral face diagonal.",
                "A fixed modulo-7 obstruction excludes both remaining face diagonals.",
                "The family is injective and satisfies N1(B) >> B^(1/4).",
            ],
            "not_claimed": [
                "This lower bound has the correct order of growth for N1(B).",
                "Any upper bound for N2(B).",
                "N2(B)=o(N1(B)).",
                "Direct applicability of the square sieve or determinant method.",
            ],
            "next_research_question": (
                "Can the shared-face-diagonal p be used to count a much larger "
                "exactly-one population through representation-function convolutions?"
            ),
        },
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-report",
        type=Path,
        default=DEFAULT_REPORT,
        help="Path to the deterministic JSON report.",
    )
    parser.add_argument(
        "--validation-max-m",
        type=int,
        default=DEFAULT_VALIDATION_MAX_M,
    )
    parser.add_argument(
        "--skip-stage9-cross-check",
        action="store_true",
        help="Skip the d<=20000 compatibility check against the Stage9 enumerator.",
    )
    args = parser.parse_args()

    if args.validation_max_m < 2:
        parser.error("--validation-max-m must be at least 2")

    report = build_report(args.validation_max_m, args.skip_stage9_cross_check)
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "report": str(args.write_report),
                "family_examples": report["finite_validation"]["first_examples"][:4],
                "lower_bound": report["lower_bound"]["pointwise_bound"],
                "stage9_cross_check": report["stage9_cross_check"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
