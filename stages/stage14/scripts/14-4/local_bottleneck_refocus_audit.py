#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4bf/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/local_bottleneck_refocus_summary.json"
S5T = ROOT / "stages/stage14/14-s5t/result.md"
FOUR_BE = ROOT / "stages/stage14/14-4be/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing: {needle}"


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    s5t = S5T.read_text()
    four_be = FOUR_BE.read_text()

    # Imported theorem locks.
    require(s5t, "GRAPH_ESCAPE_OPTIMAL_SAVING=1/41")
    require(s5t, "ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/41")
    require(s5t, "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=81/82")
    require(s5t, "ALL_SHORT_ABSOLUTE_TUPLE_SUM_IS_CURRENT_BOTTLENECK=true")
    require(s5t, "OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL=false")
    require(four_be, "UNWEIGHTED_RHO_LOC_B_EXPONENT=1/400")
    require(four_be, "UNWEIGHTED_E_LOC=0")

    # Exact B-scale conversion.
    delta_m = Fraction(1, 41)
    delta_b = delta_m / 2
    assert delta_b == Fraction(1, 82)
    local_count_exp = Fraction(1, 1) - delta_b
    assert local_count_exp == Fraction(81, 82)

    # The 4be exponent is strictly superseded.
    assert Fraction(1, 82) > Fraction(1, 400)

    # Remaining exponent needed to reach a B^(1/2) main term.
    remaining = Fraction(1, 2) - delta_b
    assert remaining == Fraction(20, 41)

    # Conditional ceiling if Case C were removed but current A/B estimates
    # and lambda<=1 were left unchanged.
    # A and B can both save delta only if lambda >= 5 sigma / 2.
    # lambda<=1 => sigma<=2/5 => delta<=sigma/2<=1/5 on M scale.
    sigma_ceiling = Fraction(2, 5)
    delta_m_ceiling = sigma_ceiling / 2
    delta_b_ceiling = delta_m_ceiling / 2
    post_local_still_needed = Fraction(1, 2) - delta_b_ceiling
    assert delta_m_ceiling == Fraction(1, 5)
    assert delta_b_ceiling == Fraction(1, 10)
    assert post_local_still_needed == Fraction(2, 5)

    lr = summary["updated_local_retainer"]
    assert lr["delta_loc_B_scale"] == "1/82"
    assert lr["E_loc"] == 0
    assert lr["direct_physical_upper_bound"] == "B^(81/82+epsilon)"

    sqrt_ledger = summary["sqrt_ledger"]
    assert sqrt_ledger["remaining_delta_after_current_local"] == "20/41"
    assert sqrt_ledger["sqrt_requirement_if_separated"] == "delta_glob+delta_ht>=20/41"

    ceiling = summary["current_AB_architecture_ceiling_if_case_C_removed"]
    assert ceiling["delta_M_max"] == "1/5"
    assert ceiling["delta_B_max"] == "1/10"
    assert ceiling["post_local_delta_still_needed_for_sqrt"] == "2/5"
    assert ceiling["absolute_future_local_barrier_claim"] is False

    decision = summary["roadmap_decision"]
    assert decision["one_targeted_s5u_optimization_justified"] is True
    assert decision["main_track_waits_for_s5u"] is False
    assert decision["main_track_primary_focus"] == "post-local global-small-point thinning"
    assert decision["next_main_stage"] == "14-4bg"

    flags = summary["flags"]
    expected = {
        "S5T_SAVING_OPTIMIZATION_IMPORTED": True,
        "OLD_LOCAL_B_EXPONENT_1_OVER_400_SUPERSEDED": True,
        "LOCAL_M_SCALE_SAVING_EXPONENT": "1/41",
        "UNWEIGHTED_LOCAL_B_SCALE_SAVING_EXPONENT": "1/82",
        "UNWEIGHTED_E_LOC": 0,
        "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": True,
        "EXPLICIT_COMPLETE_E_LOC_PROVED": True,
        "ACTIVE_PHYSICAL_BASE_UPPER_BOUND": "B^(81/82+epsilon)",
        "OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL": False,
        "ALL_SHORT_ABSOLUTE_TUPLE_SUM_IS_CURRENT_BOTTLENECK": True,
        "NEW_ARITHMETIC_RESONANCE_FOUND": False,
        "ONE_TARGETED_S5U_OPTIMIZATION_JUSTIFIED": True,
        "MAIN_TRACK_WAITS_FOR_S5U": False,
        "MAIN_TRACK_PRIMARY_FOCUS": "POST_LOCAL_GLOBAL_SMALL_POINT_THINNING",
        "CURRENT_SQRT_REMAINING_DELTA": "20/41",
        "CASE_C_REMOVED_CURRENT_AB_ARCHITECTURE_LOCAL_B_CEILING": "1/10",
        "CASE_C_REMOVED_CURRENT_AB_ARCHITECTURE_STILL_REQUIRES_POST_LOCAL_DELTA_GE_2/5": True,
        "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
    }
    for key, value in expected.items():
        assert flags[key] == value, (key, flags[key], value)

    # Boundary wording locks.
    require(result, "UNWEIGHTED_LOCAL_B_SCALE_SAVING_EXPONENT=1/82")
    require(result, "MAIN_TRACK_WAITS_FOR_S5U=false")
    require(result, "MAIN_TRACK_PRIMARY_FOCUS=POST_LOCAL_GLOBAL_SMALL_POINT_THINNING")
    require(result, "CURRENT_SQRT_REMAINING_DELTA=20/41")
    require(result, "CASE_C_REMOVED_CURRENT_AB_ARCHITECTURE_LOCAL_B_CEILING=1/10")
    require(result, "NEXT=Stage14-4bg")

    print("STAGE14_4BF_AUDIT=PASS")
    print("delta_M=1/41")
    print("delta_B=1/82")
    print("physical_upper_bound_exponent=81/82")
    print("remaining_delta_for_sqrt=20/41")
    print("case_C_removed_current_AB_ceiling_delta_B=1/10")
    print("main_track_waits_for_s5u=false")


if __name__ == "__main__":
    main()
