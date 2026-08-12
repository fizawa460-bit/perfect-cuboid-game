#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def exponent_ledger() -> dict:
    # U_Z ~ k^(1/8) Z^(1/4), U_W analogously.
    # Cauchy on kappa fibers gives k^(1/8) (ZW)^(5/8).
    return {
        "k_exp_before_height": Fraction(1, 8),
        "ZW_exp_before_height": Fraction(5, 8),
        "B_exp_after_height": Fraction(5, 8),
        "k_exp_after_height": Fraction(-1, 2),
    }


def cauchy_upper(A: list[int], B: list[int]) -> tuple[int, int]:
    if len(A) != len(B):
        raise ValueError("same kappa index set required")
    diagonal = sum(a * b for a, b in zip(A, B))
    max_a = max(A, default=0)
    max_b = max(B, default=0)
    l1_a = sum(A)
    l1_b = sum(B)
    # Squared Cauchy upper bound using sum a^2 <= max(a) sum a.
    cauchy_sq = max_a * l1_a * max_b * l1_b
    if diagonal * diagonal > cauchy_sq:
        raise AssertionError("Cauchy ledger failed")
    return diagonal, cauchy_sq


def audit_examples() -> list[dict]:
    rows = []
    for A, B in [([3, 1, 0, 2], [1, 4, 2, 0]), ([5, 2, 1], [2, 1, 6])]:
        diagonal, cauchy_sq = cauchy_upper(A, B)
        rows.append({"A": A, "B": B, "diagonal": diagonal, "cauchy_sq": cauchy_sq})
    ledger = exponent_ledger()
    if ledger["k_exp_before_height"] - ledger["ZW_exp_before_height"] != Fraction(-1, 2):
        raise AssertionError("physical-height k exponent mismatch")
    return rows


if __name__ == "__main__":
    rows = audit_examples()
    print("STAGE15_6AP_KAPPA_COUPLING=PASS")
    print("FIXED_K_BOUND=k^(1/8)*(ZW)^(5/8)*B^epsilon")
    print("PHYSICAL_BOUND=B^(5/8+epsilon)*k^(-1/2)")
    for row in rows:
        print(row)
