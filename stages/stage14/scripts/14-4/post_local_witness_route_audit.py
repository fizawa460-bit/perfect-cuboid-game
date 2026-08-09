#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bg/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/post_local_witness_route_summary.json"
S6 = ROOT / "stages/stage14/14-s6-00/result.md"
S5U = ROOT / "stages/stage14/14-s5u/result.md"
S3 = ROOT / "stages/stage14/14-s3/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing: {needle}"


def odd_prime_factors(n: int) -> set[int]:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    out: set[int] = set()
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        out.add(n)
    return out


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    s6 = S6.read_text()
    s5u = S5U.read_text()
    s3 = S3.read_text()

    require(s6, "DIRECT_POST_LOCAL_GLOBAL_SMALL_POINT_INCIDENCE_PRIMARY=true")
    require(s6, "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42")
    require(s6, "POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21")
    require(s5u, "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/21")
    require(s5u, "S5_METHOD_CLOSED=true")
    require(s3, "PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW=true")

    local_exp = Fraction(41, 42)
    assert Fraction(1) - local_exp == Fraction(1, 42)
    assert local_exp - Fraction(1, 2) == Fraction(10, 21)
    assert Fraction(2) - Fraction(1, 21) == Fraction(41, 21)

    triples = [(3, 4, 5), (5, 12, 13), (7, 24, 25), (20, 21, 29)]
    for S, X, H in triples:
        assert S * S + X * X == H * H
        for D in range(1, 8):
            for A in range(-50, 51):
                if A == 0 or math.gcd(A, D) != 1:
                    continue
                g0 = A
                g1 = A - S * S * D * D
                g2 = A + X * X * D * D
                assert g0 - g1 == S * S * D * D
                assert g2 - g0 == X * X * D * D
                assert g2 - g1 == H * H * D * D
                assert odd_prime_factors(math.gcd(abs(g0), abs(g1))) <= odd_prime_factors(S)
                assert odd_prime_factors(math.gcd(abs(g0), abs(g2))) <= odd_prime_factors(X)
                assert odd_prime_factors(math.gcd(abs(g1), abs(g2))) <= odd_prime_factors(H)

    direct = summary["direct_object"]
    assert direct["sandwich"] == "V(B) <= J_C(B) <= N_loc(B)"
    assert direct["current_bound"] == "J_C(B) << B^(41/42+epsilon)"
    assert direct["post_local_saving_needed_for_sqrt"] == "10/21"

    flags = summary["flags"]
    expected = {
        "S6_00_PRIMARY_ROUTE_IMPORTED": True,
        "S5U_LOCAL_METHOD_CLOSURE_IMPORTED": True,
        "CURRENT_LOCAL_CLASS_B_EXPONENT": "41/42",
        "CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA": "10/21",
        "DIRECT_POST_LOCAL_CLASS_COUNT_DEFINED": True,
        "PHYSICAL_BASE_INJECTS_TO_DIRECT_POST_LOCAL_CLASS": True,
        "NONZERO_KUMMER_REPRESENTATIVE_WITH_NO_HEIGHT_INCREASE_PROVED": True,
        "LOW_CANONICAL_HEIGHT_TO_POLYNOMIAL_RATIONAL_COORDINATE_BOX": True,
        "INTEGRAL_WITNESS_EQUATION_EXACT": True,
        "WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH": True,
        "FIXED_STATE_TWO_QUADRIC_DIFFERENCE_SYSTEM_EXACT": True,
        "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED": False,
        "SQRT_B_UPPER_BOUND_PROVED": False,
        "SQRT_B_ASYMPTOTIC_PROVED": False,
    }
    for key, value in expected.items():
        assert flags[key] == value, (key, flags[key], value)

    require(result, "STAGE14_4BG=S6_PRIMARY_ROUTE_IMPORTED_AND_EXACT_INTEGRAL_WITNESS_MODEL_FROZEN")
    require(result, "WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true")
    require(result, "FIXED_STATE_TWO_QUADRIC_DIFFERENCE_SYSTEM_EXACT=true")
    require(result, "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false")
    require(result, "NEXT=Stage14-4bh")

    print("STAGE14_4BG_AUDIT=PASS")
    print("s6_primary_route_imported=true")
    print("local_B_exponent=41/42")
    print("post_local_saving_needed_for_sqrt=10/21")
    print("witness_equation=Y^2=A(A-S^2D^2)(A+X^2D^2)")


if __name__ == "__main__":
    main()
