#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bg/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/post_local_witness_route_summary.json"
S5U = ROOT / "stages/stage14/14-s5u/result.md"
FOUR_AQ = ROOT / "stages/stage14/14-4aq/result.md"
FOUR_AR = ROOT / "stages/stage14/14-4ar/result.md"
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
    s5u = S5U.read_text()
    four_aq = FOUR_AQ.read_text()
    four_ar = FOUR_AR.read_text()
    s3 = S3.read_text()

    require(s5u, "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/21")
    require(s5u, "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=41/42")
    require(s5u, "S5_METHOD_CLOSED=true")
    require(four_aq, "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false")
    require(four_ar, "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false")
    require(s3, "PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW=true")

    local_exp = Fraction(41, 42)
    local_delta = Fraction(1, 1) - local_exp
    post_needed = local_exp - Fraction(1, 2)
    assert local_delta == Fraction(1, 42)
    assert post_needed == Fraction(10, 21)
    assert Fraction(2, 1) - Fraction(1, 21) == Fraction(41, 21)

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

                gcd01 = math.gcd(abs(g0), abs(g1))
                gcd02 = math.gcd(abs(g0), abs(g2))
                gcd12 = math.gcd(abs(g1), abs(g2))
                assert odd_prime_factors(gcd01) <= odd_prime_factors(S)
                assert odd_prime_factors(gcd02) <= odd_prime_factors(X)
                assert odd_prime_factors(gcd12) <= odd_prime_factors(H)

    direct = summary["direct_object"]
    assert direct["sandwich"] == "V(B) <= J_C(B) <= N_loc(B)"
    assert direct["current_bound"] == "J_C(B) << B^(41/42+epsilon)"
    assert direct["post_local_saving_needed_for_sqrt"] == "10/21"
    assert summary["route_comparison"]["direct"]["selected_primary"] is True
    assert summary["route_comparison"]["separated"]["selected_primary"] is False

    flags = summary["flags"]
    expected = {
        "S5U_LOCAL_METHOD_CLOSURE_IMPORTED": True,
        "CURRENT_LOCAL_CLASS_B_EXPONENT": "41/42",
        "CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA": "10/21",
        "DIRECT_POST_LOCAL_CLASS_COUNT_DEFINED": True,
        "PHYSICAL_BASE_INJECTS_TO_DIRECT_POST_LOCAL_CLASS": True,
        "NONZERO_KUMMER_REPRESENTATIVE_WITH_NO_HEIGHT_INCREASE_PROVED": True,
        "INTEGRAL_WITNESS_EQUATION_EXACT": True,
        "WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH": True,
        "SEPARATED_GLOBAL_HEIGHT_ROUTE_REJECTED_AS_PRIMARY": True,
        "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED": False,
        "SQRT_B_ASYMPTOTIC_PROVED": False,
    }
    for key, value in expected.items():
        assert flags[key] == value, (key, flags[key], value)

    require(result, "STAGE14_4BG=POST_LOCAL_DIRECT_GLOBAL_SMALL_POINT_WITNESS_ROUTE_SELECTED")
    require(result, "CURRENT_LOCAL_CLASS_B_EXPONENT=41/42")
    require(result, "CURRENT_SQRT_REMAINING_POST_LOCAL_DELTA=10/21")
    require(result, "WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true")
    require(result, "DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false")
    require(result, "NEXT=Stage14-4bh")

    print("STAGE14_4BG_AUDIT=PASS")
    print("local_B_exponent=41/42")
    print("post_local_saving_needed_for_sqrt=10/21")
    print("route=direct_global_small_point_witness")
    print("witness_equation=Y^2=A(A-S^2D^2)(A+X^2D^2)")


if __name__ == "__main__":
    main()
