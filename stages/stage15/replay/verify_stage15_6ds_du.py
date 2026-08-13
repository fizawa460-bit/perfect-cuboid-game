#!/usr/bin/env python3
from __future__ import annotations

from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STAGE15 = ROOT / "stages/stage15"


def require(text: str, needle: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing marker: {needle}")


def main() -> None:
    ds = (STAGE15 / "15-6ds/result.md").read_text(encoding="utf-8")
    dt = (STAGE15 / "15-6dt/result.md").read_text(encoding="utf-8")
    du = (STAGE15 / "15-6du/result.md").read_text(encoding="utf-8")

    for needle in (
        "STAGE15_6DS_CORE_SPLIT_K1_VS_KGT1=true",
        "STAGE15_6DS_K1_RECEIVER=PRIMITIVE_DIFFERENCE_OF_SQUARES_FACTOR_GAP",
        "STAGE15_6DS_K1_TWO_FACTOR_EQUATIONS_EXACT=true",
        "STAGE15_6DS_K1_FACTOR_GAP_COMPATIBILITY_EXACT=true",
        "STAGE15_6DS_K1_DOUBLE_ELIMINANT_EQUIVALENCE=true",
        "STAGE15_6DS_K1_DISTINCT_FIXED_POWER_PROVED=false",
        "STAGE15_6DS_KGT1_FIRST_NORM_UNIT_ORBITS_EXACT=true",
        "STAGE15_6DS_KGT1_SECOND_NORM_SAME_FIELD_PELL=true",
        "STAGE15_6DS_KGT1_RECEIVER=RANK_ONE_RECURRENCE_INTERSECTION",
        "STAGE15_6DS_NEW_INDEPENDENT_CODIMENSION=false",
        "STAGE15_6DS_6DA_MULTIPLICITY_RECHARGED=false",
        "STAGE15_6DS_PHYSICAL_MEASURE_PRESERVED=true",
    ):
        require(ds, needle)

    for needle in (
        "STAGE15_6DT_BRANCHWISE_TESTED=true",
        "STAGE15_6DT_K1_FACTOR_BRANCH_TESTED=true",
        "STAGE15_6DT_K1_FACTOR_BRANCH_OUTER_FIXED_POWER=false",
        "STAGE15_6DT_K1_FACTOR_BRANCH_ROLE=INPUT_TO_RESIDUAL_COMPLEMENTARY_SWITCH",
        "STAGE15_6DT_KGT1_PELL_AVERAGING_TESTED=true",
        "STAGE15_6DT_KGT1_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY",
        "STAGE15_6DT_AR016=APPLICABLE_EXPONENT_NEUTRAL",
        "STAGE15_6DT_AR023_024=FIREWALL_PASS",
        "STAGE15_6DT_AR028=NO_RECHARGE_PASS",
        "STAGE15_6DT_COMPLETION_MULTIPLICITY_CHARGED_ONCE=true",
    ):
        require(dt, needle)

    for needle in (
        "STAGE15_6DU_EXHAUSTIVE_VIEW_AUDIT=true",
        "STAGE15_6DU_BLIND_REDISCOVERY=true",
        "STAGE15_6DU_CORE_UNION_AUDITED=K1_FACTOR|KGT1_PELL",
        "STAGE15_6DU_K1_FACTOR_BRANCH=ALGEBRAICALLY_EQUIVALENT_NO_FIXED_POWER",
        "STAGE15_6DU_KGT1_PELL_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY",
        "STAGE15_6DU_COMPLETION_MULTIPLICITY_CHARGED_ONCE=true",
        "STAGE15_6DU_RESIDUAL_CELL_SWITCH=LIVE_UNTESTED_SELECTED",
        "STAGE15_6DU_SELECTED_ROUTE=RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER",
        "STAGE15_6DU_BRANCH_AWARE_POSTFILTER=K1_FACTOR_GAP|KGT1_PELL",
        "STAGE15_6DU_PARKING_ALLOWED=false",
        "STAGE15_6DU_SPLIT_TRIGGER=false",
        "CURRENT_SUBSTAGE=Stage15-6du",
    ):
        require(du, needle)

    # k=1 exact primitive factor-gap witness.
    # cells are all one and (M,N,U,V)=(5,3,7,4).
    M1, N1, U1, V1 = 5, 3, 7, 4
    C1 = M1 * U1
    L1 = N1 * V1
    C2 = N1 * U1
    L2 = M1 * V1
    P1, Q1 = 37, 29
    assert gcd(C1, L1) == 1
    assert gcd(C2, L2) == 1
    assert C1 * C1 + L1 * L1 == P1 * P1
    assert C2 * C2 + L2 * L2 == Q1 * Q1

    r1, s1 = P1 - L1, P1 + L1
    r2, s2 = Q1 - L2, Q1 + L2
    assert (r1, s1) == (25, 49)
    assert (r2, s2) == (9, 49)
    assert r1 * s1 == C1 * C1
    assert r2 * s2 == C2 * C2
    assert (s1 - r1) // (2 * N1) == V1
    assert (s2 - r2) // (2 * M1) == V1

    # Both primitive factor pairs are individual squares in this odd-leg case.
    assert isqrt(r1) ** 2 == r1 and isqrt(s1) ** 2 == s1
    assert isqrt(r2) ** 2 == r2 and isqrt(s2) ** 2 == s2

    # Recover both k=1 double eliminants.
    delta1 = M1**4 - N1**4
    assert delta1 * U1 * U1 == (M1 * P1 - N1 * Q1) * (M1 * P1 + N1 * Q1)
    assert delta1 * V1 * V1 == (M1 * Q1 - N1 * P1) * (M1 * Q1 + N1 * P1)

    # Certified k>1 (k=10) 6da witness and one exact unit step.
    k = 10
    L0, P0 = 1, 37
    unit_a, unit_b = 19, 6  # epsilon = 19 + 6 sqrt(10), norm 1
    C = 117
    assert unit_a * unit_a - k * unit_b * unit_b == 1
    assert L0 * L0 - k * P0 * P0 == -(C * C)

    Lnext = unit_a * L0 + k * unit_b * P0
    Pnext = unit_b * L0 + unit_a * P0
    assert (Lnext, Pnext) == (2239, 709)
    assert Lnext * Lnext - k * Pnext * Pnext == -(C * C)

    # j=0 survives the second norm with Q=5.
    M, N, U = 13, 1, 9
    q0_num = M * M * L0 * L0 + U * U
    assert q0_num == k * 5 * 5

    # j=1 remains on the first Pell orbit but fails the second-square postfilter.
    q1_num = M * M * Lnext * Lnext + U * U
    assert q1_num % k == 0
    q1_sq = q1_num // k
    assert q1_sq == 84721753
    assert isqrt(q1_sq) ** 2 != q1_sq

    # Recover the exact k>1 U-eliminant on the survivor j=0.
    delta = M**4 - N**4
    lhs = delta * U * U
    rhs = k * (M * M * P0 * P0 - N * N * 5 * 5)
    assert lhs == rhs

    print("Stage15-6 branch-split ds-du: PASS")


if __name__ == "__main__":
    main()
