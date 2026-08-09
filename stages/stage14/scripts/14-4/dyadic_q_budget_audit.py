#!/usr/bin/env python3
"""Stage14-4at: instantiate dyadic Euclid Q-budget bookkeeping."""

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
S5G = ROOT / "stages/stage14/14-s5g/result.md"
AS = ROOT / "stages/stage14/14-4as/result.md"
AQ = ROOT / "stages/stage14/data/14-4/global_sha_retainer_summary.json"
AR = ROOT / "stages/stage14/data/14-4/small_point_retainer_summary.json"
OUT = ROOT / "stages/stage14/data/14-4/dyadic_q_budget_summary.json"


def fstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def main() -> None:
    s5g = S5G.read_text()
    stage_as = AS.read_text()
    aq = json.loads(AQ.read_text())
    ar = json.loads(AR.read_text())

    assert "(RS+Q^4)" in s5g
    assert "FAMILY_LARGE_SIEVE_THEOREM_PROVED=false" in s5g
    assert "RECURSIVE_THREE_RETAINER_TRANSFER_EXACT=true" in stage_as
    assert aq["decision"]["POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED"] is False
    assert ar["decision"]["POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED"] is False

    transition = Fraction(1, 4)
    theta_grid = [Fraction(0), Fraction(1, 16), Fraction(1, 8), Fraction(3, 16), Fraction(1, 4), Fraction(5, 16)]
    rows = []
    for theta in theta_grid:
        q4_exp = 4 * theta
        rows.append({
            "theta": fstr(theta),
            "Q4_exponent": fstr(q4_exp),
            "bulk_prefactor_exponent_max_1_4theta": fstr(max(Fraction(1), q4_exp)),
            "super_volume": theta > transition,
            "at_or_below_transition": theta <= transition,
        })

    report = {
        "stage": "14-4at",
        "classification": "DYADIC_Q_BUDGET_AND_FIRST_QUANTITATIVE_GAP",
        "dyadic_geometry": {
            "box": "m~M, n~N inside m^2+n^2<=B",
            "M_N_upper_scale": "B^(1/2)",
            "box_population_bound": "A(M,N)<<MN",
            "number_of_boxes": "O((log B)^2)",
            "bulk_volume_scale": "MN~B",
            "dyadic_loss": "B^o(1)",
        },
        "s5g_candidate": {
            "second_moment_prefactor": "MN+Q^4",
            "proved": False,
            "full_local_indicator_bound": False,
            "transition_theta_for_Q_eq_Btheta_on_bulk_boxes": fstr(transition),
            "benchmark_global_Q": "B^(1/4-eta), eta>0 fixed",
            "box_adaptive_Q": "min(B^(1/4-eta),(MN)^(1/4-eta))",
            "theta_grid": rows,
            "warning": "Q^4 is a second-moment scale, not an identified additive E_loc",
        },
        "end_to_end_exponent_bookkeeping": {
            "main": "1-delta_loc-delta_glob-delta_ht",
            "propagated_E_loc": "kappa_loc-delta_glob-delta_ht",
            "propagated_E_glob": "kappa_glob-delta_ht",
            "E_ht": "kappa_ht",
        },
        "square_root_requirements": [
            "1-delta_loc-delta_glob-delta_ht <= 1/2",
            "kappa_loc-delta_glob-delta_ht <= 1/2",
            "kappa_glob-delta_ht <= 1/2",
            "kappa_ht <= 1/2",
        ],
        "first_quantitative_gap": {
            "name": "FULL_LOCAL_INDICATOR_CONVERSION",
            "missing_map": "centered prime-level second moment -> nonnegative full local 2-descent indicator -> explicit rho_loc,E_loc",
            "reciprocal_off_diagonal_control_required": True,
            "rho_loc_available": False,
            "E_loc_available": False,
            "why_first": "the ordered end-to-end chain cannot insert a numerical local retainer before this conversion",
        },
        "later_known_gaps": {
            "positive_global_saving_exponent_proved": False,
            "positive_height_saving_exponent_proved": False,
        },
        "decision": {
            "STAGE14_4AT": "DYADIC_Q_BUDGET_INSTANTIATED_AND_FIRST_QUANTITATIVE_GAP_IDENTIFIED",
            "DYADIC_EUCLID_BOX_COUNT_O_LOG2_B": True,
            "S5G_Q4_TRANSITION_THETA": "1/4",
            "BENCHMARK_Q_CHOSEN": "B^(1/4-eta)",
            "BOX_ADAPTIVE_Q_CLIPPED": True,
            "S5G_SECOND_MOMENT_IS_LOCAL_INDICATOR_BOUND": False,
            "E_LOC_IDENTIFIED_WITH_Q4": False,
            "RHO_LOC_EXPLICITLY_PROVED": False,
            "E_LOC_EXPLICITLY_PROVED": False,
            "FIRST_QUANTITATIVE_GAP": "FULL_LOCAL_INDICATOR_CONVERSION",
            "POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED": False,
            "POSITIVE_HEIGHT_SAVING_EXPONENT_PROVED": False,
            "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-4au close the first local quantitative gap by expanding the full centered local indicator on dyadic Euclid boxes and deriving explicit rho_loc/E_loc bounds, or isolate the reciprocal off-diagonal obstruction in coordination with Stage14-s5h",
        },
    }

    committed = json.loads(OUT.read_text())
    assert committed == report
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
