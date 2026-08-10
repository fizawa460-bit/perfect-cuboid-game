#!/usr/bin/env python3
"""Validate Stage14-t73 frozen boundary."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t73/fixed_tag_norm_fiber_frozen.json"
RESULT = ROOT / "stages/stage14/14-t73/result.md"


def main() -> None:
    data = json.loads(DATA.read_text())
    text = RESULT.read_text()

    assert data["stage"] == "14-t73"
    assert data["reciprocal_states"] == 560
    assert data["invisible_states"] == 419
    assert data["tagged_normal_form_checks"] == 419
    assert data["canonical_filter_checks"] == 419
    assert data["private_pair_fixed_tag_orientation_checks"] == 5
    assert data["same_denominator_tag_private_pairs"] == 1
    assert data["kappa_one_exhaustive_factorization_checks"] == 1965
    assert data["fixed_norm_small_box_regression_checks"] == 3240
    assert data["max_frozen_fixed_kappa_beta_pminus_multiplicity"] == 1

    th = data["parallel_th19_audit"]
    assert th["status"] == "COMPLETE_INDEPENDENT_PELL_SMOOTH_ENERGY_AUDIT"
    assert th["pell_unit_orbit_cost"] == "Bo1_COMPATIBLE"
    assert th["moving_kappa_moving_s_uniform_quantitative_saving_available"] is False
    assert th["sharp_ell_delta_hyperbola_must_be_retained"] is True
    assert th["off_the_shelf_uniform_fixed_power_saving_proved"] is False

    b = data["boundary"]
    assert b["STAGE14_T73"].startswith("COMPLETE_")
    assert b["UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT"] == "Bo1"
    assert b["FIXED_TAG_CAYLEY_ROOTLINE_ORIENTATION_MULTIPLICITY"] == 1
    assert b["TH19_PARALLEL_AUDIT_CONSUMED"] is True
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "5/8"
    assert b["TH19_NEEDED"] is True
    assert b["NEXT"] == "Stage14-t74"

    for needle in (
        "STAGE14_T73=COMPLETE_KAPPA_ONE_LINEAR_FACTORIZATION_FIXED_TAG_CONDITIONING_AND_UNIFORM_FIXED_NORM_FIBER_REDUCTION",
        "UNIFORM_FIXED_NORM_REAL_QUADRATIC_ELEMENT_COUNT=Bo1",
        "TH19_REQUESTED_OBJECT=SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8",
        "NEXT=Stage14-t74",
    ):
        assert needle in text


if __name__ == "__main__":
    main()
