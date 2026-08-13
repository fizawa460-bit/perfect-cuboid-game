#!/usr/bin/env python3
from __future__ import annotations

from math import isqrt
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
        "STAGE15_6DS_FIRST_NORM_UNIT_ORBITS_EXACT=true",
        "STAGE15_6DS_SECOND_NORM_SAME_FIELD_PELL=true",
        "STAGE15_6DS_RECEIVER=RANK_ONE_RECURRENCE_INTERSECTION",
        "STAGE15_6DS_DOUBLE_ELIMINANT_RECOVERED=true",
        "STAGE15_6DS_NEW_INDEPENDENT_CODIMENSION=false",
        "STAGE15_6DS_PHYSICAL_MEASURE_PRESERVED=true",
    ):
        require(ds, needle)

    for needle in (
        "STAGE15_6DT_PELL_AVERAGING_TESTED=true",
        "STAGE15_6DT_AR016=APPLICABLE_EXPONENT_NEUTRAL",
        "STAGE15_6DT_AR023_024=FIREWALL_PASS",
        "STAGE15_6DT_AR028=NO_RECHARGE_PASS",
        "STAGE15_6DT_FIXED_POWER_FROM_CURRENT_PELL_INPUTS=false",
        "STAGE15_6DT_NEGATIVE_CERTIFICATE=CURRENT_INPUTS_ONLY",
    ):
        require(dt, needle)

    for needle in (
        "STAGE15_6DU_EXHAUSTIVE_VIEW_AUDIT=true",
        "STAGE15_6DU_BLIND_REDISCOVERY=true",
        "STAGE15_6DU_RESIDUAL_CELL_SWITCH=LIVE_UNTESTED_SELECTED",
        "STAGE15_6DU_SELECTED_ROUTE=RESIDUAL_CELL_COMPLEMENTARY_SWITCH_WITH_PELL_POSTFILTER",
        "STAGE15_6DU_PARKING_ALLOWED=false",
        "STAGE15_6DU_SPLIT_TRIGGER=false",
        "CURRENT_SUBSTAGE=Stage15-6du",
    ):
        require(du, needle)

    # Certified 6da witness and one exact unit step in Q(sqrt(10)).
    k = 10
    L0, P0 = 1, 37
    unit_a, unit_b = 19, 6  # epsilon = 19 + 6 sqrt(10), norm 1
    C1 = 117
    assert unit_a * unit_a - k * unit_b * unit_b == 1
    assert L0 * L0 - k * P0 * P0 == -(C1 * C1)

    L1 = unit_a * L0 + k * unit_b * P0
    P1 = unit_b * L0 + unit_a * P0
    assert (L1, P1) == (2239, 709)
    assert L1 * L1 - k * P1 * P1 == -(C1 * C1)

    # j=0 survives the second norm with Q=5.
    M, N, U = 13, 1, 9
    q0_num = M * M * L0 * L0 + U * U
    assert q0_num == k * 5 * 5

    # j=1 remains on the first Pell orbit but fails the second-square postfilter.
    q1_num = M * M * L1 * L1 + U * U
    assert q1_num % k == 0
    q1_sq = q1_num // k
    assert q1_sq == 84721753
    assert isqrt(q1_sq) ** 2 != q1_sq

    # Recover the exact U-eliminant on the survivor j=0.
    delta = M**4 - N**4
    lhs = delta * U * U
    rhs = k * (M * M * P0 * P0 - N * N * 5 * 5)
    assert lhs == rhs

    print("Stage15-6 Pell/unit-orbit ds-du: PASS")


if __name__ == "__main__":
    main()
