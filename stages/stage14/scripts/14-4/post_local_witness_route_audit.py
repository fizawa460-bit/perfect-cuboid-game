#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bg/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/post_local_witness_route_summary.json"
FOUR_BF = ROOT / "stages/stage14/14-4bf/result.md"
FOUR_AQ = ROOT / "stages/stage14/14-4aq/result.md"
FOUR_AR = ROOT / "stages/stage14/14-4ar/result.md"
S3 = ROOT / "stages/stage14/14-s3/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing: {needle}"


def odd_prime_factors(n: int) -> set[int]:
    n = abs(n)
    out: set[int] = set()
    p = 3
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p += 2
    if n > 1 and n % 2:
        out.add(n)
    return out


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    four_bf = FOUR_BF.read_text()
    four_aq = FOUR_AQ.read_text()
    four_ar = FOUR_AR.read_text()
    s3 = S3.read_text()

    # Merged interface locks.
    require(four_bf, "CURRENT_UNWEIGHTED_LOCAL_B_EXPONENT=81/82")
    require(four_bf, "MAIN_TRACK_PRIMARY_FOCUS=POST_LOCAL_GLOBAL_SMALL_POINT_THINNING")
    require(four_aq, "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false")
    require(four_ar, "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED=false")
    require(s3, "PHYSICAL_HIT_IMPLIES_LOGARITHMIC_CANONICAL_HEIGHT_WINDOW=true")

    # Exact exponent ledger on the currently merged 4bf theorem.
    local_exp = Fraction(81, 82)
    local_delta = Fraction(1, 1) - local_exp
    post_needed = local_exp - Fraction(1, 2)
    assert local_delta == Fraction(1, 82)
    assert post_needed == Fraction(20, 41)

    # Pending s5u ledger is recorded but intentionally not imported.
    pending_exp = Fraction(41, 42)
    assert pending_exp - Fraction(1, 2) == Fraction(10, 21)
    assert summary["pending_s5u"]["imported"] is False

    # Exact witness algebra and pairwise gcd support regression.
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

    # Summary/result boundary locks.
    direct = summary["direct_object"]
    assert direct["sandwich"] == "V(B) <= J_C(B) <= N_loc(B)"
    assert direct["post_local_saving_needed_for_sqrt"] == "20/41"
    assert summary["route_comparison"]["direct"]["selected_primary"] is True
    assert summary["route_comparison"]["separated"]["selected_primary"] is False

    flags = summary["flags"]
    assert flags["DIRECT_POST_LOCAL_CLASS_COUNT_DEFINED"] is True
    assert flags["PHYSICAL_BASE_INJECTS_TO_DIRECT_POST_LOCAL_CLASS"] is True
    assert flags["NONZERO_KUMMER_REPRESENTATIVE_WITH_NO_HEIGHT_INCREASE_PROVED"] is True
    assert flags["INTEGRAL_WITNESS_EQUATION_EXACT"] is True
    assert flags["WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH"] is True
    assert flags["DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED"] is False
    assert flags["SQRT_B_ASYMPTOTIC_PROVED"] is False

    require(result, "STAGE14_4BG=POST_LOCAL_DIRECT_GLOBAL_SMALL_POINT_WITNESS_ROUTE_SELECTED")
    require(result, "CURRENT_MERGED_LOCAL_B_EXPONENT=81/82")
    require(result, "WITNESS_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true")
    require(result, "S5U_PENDING_NOT_IMPORTED=true")
    require(result, "NEXT=Stage14-4bh")

    print("STAGE14_4BG_AUDIT=PASS")
    print("current_local_B_exponent=81/82")
    print("post_local_saving_needed_for_sqrt=20/41")
    print("route=direct_global_small_point_witness")
    print("witness_equation=Y^2=A(A-S^2D^2)(A+X^2D^2)")
    print("s5u_imported=false")


if __name__ == "__main__":
    main()
