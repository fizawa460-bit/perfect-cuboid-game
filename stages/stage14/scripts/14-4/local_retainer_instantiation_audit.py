#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4be/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/local_retainer_instantiation_summary.json"
S5S = ROOT / "stages/stage14/14-s5s/result.md"
FOUR_AL = ROOT / "stages/stage14/archive/stage14-4al-collective-first-hit.md"
FOUR_BD = ROOT / "stages/stage14/14-4bd/result.md"
FOUR_AS = ROOT / "stages/stage14/14-4as/result.md"


def require(text: str, needle: str) -> None:
    assert needle in text, f"missing: {needle}"


def main() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    s5s = S5S.read_text()
    four_al = FOUR_AL.read_text()
    four_bd = FOUR_BD.read_text()
    four_as = FOUR_AS.read_text()

    # Imported theorem locks.
    require(s5s, "LOCALLY_SOLUBLE_CLASS_BOUND_B_EXPONENT=399/400")
    require(s5s, "ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED=true")
    require(four_al, "A(B)=\\frac{B}{\\pi}+O(\\sqrt B\\log B)")
    require(four_bd, "COMPLETE_POSITIVE_RECIPROCAL_EXPONENT_PROVED=true")
    require(four_as, "S_Q\\le \\rho_{\\rm loc}A_Q+E_{\\rm loc}")

    # Exact exponent conversion: local class exponent 399/400 against A~B.
    class_exp = Fraction(399, 400)
    delta_loc = Fraction(1, 1) - class_exp
    assert delta_loc == Fraction(1, 400)

    # Euclid M saving 1/200 halves when B~M^2.
    assert Fraction(1, 200) / 2 == Fraction(1, 400)

    # 4as square-root main-term requirement after delta_loc is installed.
    remaining = Fraction(1, 2) - delta_loc
    assert remaining == Fraction(199, 400)

    # The unweighted direct retainer can put the entire proved local bound
    # in rho_loc*A because A(B)>>B. Thus outer E_loc is exactly zero.
    lr = summary["local_retainer"]
    assert lr["scope"] == "unweighted cumulative family H<=B"
    assert lr["delta_loc_B_scale"] == "1/400"
    assert lr["E_loc"] == 0

    transfer = summary["four_as_transfer"]
    assert transfer["propagated_local_error"] == 0
    assert transfer["sqrt_main_term_requirement"] == "delta_glob+delta_ht>=199/400"

    flags = summary["flags"]
    expected = {
        "UNWEIGHTED_CUMULATIVE_LOCAL_RETAINER_PROVED": True,
        "UNWEIGHTED_RHO_LOC_B_EXPONENT": "1/400",
        "UNWEIGHTED_E_LOC": 0,
        "EXPLICIT_NONTRIVIAL_RHO_LOC_PROVED": True,
        "EXPLICIT_COMPLETE_E_LOC_PROVED": True,
        "LOCAL_ERROR_ZERO_IN_UNWEIGHTED_SPECIALIZATION": True,
        "D_LOC_SEPARATE_POWER_SAVING_PROVED": False,
        "D_LOC_SPLIT_REQUIRED_FOR_CURRENT_UNWEIGHTED_UPPER_BOUND": False,
        "ARBITRARY_WEIGHT_LOCAL_RETAINER_PROVED": False,
        "ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_PROVED": True,
        "ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED": False,
    }
    for key, value in expected.items():
        assert flags[key] == value, (key, flags[key], value)

    # Boundary wording must keep D_loc and arbitrary-weight claims honest.
    require(result, "D_LOC_SEPARATE_POWER_SAVING_PROVED=false")
    require(result, "ARBITRARY_WEIGHT_LOCAL_RETAINER_PROVED=false")
    require(result, "UNWEIGHTED_RHO_LOC_B_EXPONENT=1/400")
    require(result, "UNWEIGHTED_E_LOC=0")
    require(result, "SQRT_MAIN_TERM_REQUIRES_DELTA_GLOB_PLUS_DELTA_HT_GE_199/400=true")
    require(result, "NEXT=Stage14-4bf")

    print("STAGE14_4BE_AUDIT=PASS")
    print("delta_loc_B=1/400")
    print("E_loc_unweighted=0")
    print("remaining_delta_for_sqrt=199/400")
    print("D_loc_separate_claim=false")
    print("arbitrary_weight_claim=false")


if __name__ == "__main__":
    main()
