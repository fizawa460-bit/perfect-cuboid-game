#!/usr/bin/env python3
"""Validate Stage14-t74 frozen boundary."""

from __future__ import annotations

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t74/canonical_host_short_cofactor_frozen.json"
RESULT = ROOT / "stages/stage14/14-t74/result.md"
TH20 = ROOT / "stages/stage14/14-t74/th20-target.md"


def main() -> None:
    data = json.loads(DATA.read_text())
    text = RESULT.read_text()
    th20 = TH20.read_text()

    assert data["stage"] == "14-t74"
    assert data["reciprocal_states"] == 560
    assert data["invisible_states"] == 419
    assert data["canonical_host_checks"] == 419
    assert data["ell_free_balance_checks"] == 419
    assert data["short_hyperbola_checks"] == 419
    assert data["short_factor_ellipse_checks"] == 419
    assert data["reconstruction_checks"] == 419
    assert data["max_frozen_reconstruction_candidates_per_direction_ell_c"] == 6
    assert data["max_frozen_packet_ell_c_multiplicity"] == 6
    assert data["max_frozen_tagged_packet_ell_c_multiplicity"] == 1
    assert data["max_v2_DV"] == 4

    b = data["boundary"]
    assert b["STAGE14_T74"].startswith("COMPLETE_")
    assert b["CANONICAL_ELL_CANCELS_EXACTLY_FROM_CAYLEY_BALANCE"] is True
    assert b["SHARP_ELL_G_C_HYPERBOLA_PROVED"] is True
    assert b["FIXED_PACKET_ELL_C_PHYSICAL_FIBER"] == "Bo1"
    assert b["MOVING_NORM_VALUE_PARAMETER_REDUCED_TO_ELL_C"] is True
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "47/80"
    assert b["TH20_NEEDED"] is True
    assert b["TH20_PRE_T74_TARGET_MINIMAL"] is False
    assert b["NEXT"] == "Stage14-t75"

    for needle in (
        "STAGE14_T74=COMPLETE_CANONICAL_HOST_ELL_FREE_COFACTOR_BALANCE_AND_SHORT_ANGULAR_COVER_REDUCTION",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=47/80",
        "FIXED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1",
        "TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
        "NEXT=Stage14-t75",
    ):
        assert needle in text

    for needle in (
        "SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve",
        "TH20_NEEDED=true",
        "TH20_PRE_T74_TARGET_MINIMAL=false",
    ):
        assert needle in th20


if __name__ == "__main__":
    main()
