#!/usr/bin/env python3
"""Validate the frozen Stage14-t76 theorem boundary."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FROZEN = ROOT / "stages/stage14/data/14-t76/clean_kappa_cover_rootline_frozen.json"
RESULT = ROOT / "stages/stage14/14-t76/result.md"
T75 = ROOT / "stages/stage14/14-t75/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
X11 = ROOT / "stages/stage14/14-X11/result.md"


def main() -> None:
    data = json.loads(FROZEN.read_text())
    b = data["boundary"]

    assert data["reciprocal_states"] == 560
    assert data["invisible_states"] == 419
    assert data["bad_support_checks"] == 419
    assert data["clean_unit_checks"] == 419
    assert data["signed_factor_checks"] == 419
    assert data["rootline_checks"] == 419
    assert data["balance_checks"] == 419
    assert data["diagnostic_balanced_states"] == 293
    assert data["diagnostic_balanced_nontrivial_clean_states"] == 293
    assert data["diagnostic_balanced_spacing_closed_states"] == 291
    assert data["diagnostic_clean_kappa_one_states"] == 0
    assert data["max_orientation_bound"] == 32
    assert data["max_K_bad"] == 15
    assert data["max_g"] == 21
    assert data["max_fixed_rootline_packet_multiplicity"] == 1
    assert data["determinant_regressions"] == 263904
    assert data["max_zero_determinant_slope_multiplicity"] == 2

    assert b["STAGE14_T76"].startswith("COMPLETE_")
    assert b["MERGED_T75_IMPORTED"] is True
    assert b["MERGED_TH20_IMPORTED"] is True
    assert b["MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED"] is True
    assert b["KAPPA_NONUNIT_SUPPORT_EQUALS_KAPPA_INTERSECTION_ANGULAR_GCD"] is True
    assert b["CLEAN_KAPPA_COPRIME_TO_DIRECTION_AND_COVER_COORDINATES"] is True
    assert b["CLEAN_KAPPA_LOWER_BOUND"] == "K/g"
    assert b["FIXED_BETA_DETERMINES_CLEAN_KAPPA_ROOT_SIGN"] is True
    assert b["CLEAN_KAPPA_RECIPROCAL_DIRECTION_CHOICES_PER_PRIME_AT_MOST"] == 2
    assert b["CLEAN_KAPPA_CRT_PROJECTIVE_ROOT_LINE_PROVED"] is True
    assert b["LARGE_CLEAN_KAPPA_COVER_BRANCH_CLOSED_BY_ELEMENTARY_ROOTLINE_SPACING"] is True
    assert b["TH21_NEEDED"] is True
    assert b["TH21_REQUESTED_OBJECT"] == "SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion"
    assert b["T_ROUTE_BLOCKED_WAITING_FOR_TH21"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "19/34"
    assert b["T76_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING"] is False
    assert b["NEXT"] == "Stage14-t77"

    result = RESULT.read_text()
    assert "K_bad = gcd(K,g)" in result
    assert "t == rho*r (mod K_clean)" in result
    assert "TH21_NEEDED=true" in result
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in result

    assert "STAGE14_T75=COMPLETE_ANGULAR_GCD_COLUMN_SPLIT_PRIMITIVE_SHORT_GAP_AND_TYPE_I_TYPE_II_COVER_REDUCTION" in T75.read_text()
    assert "STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT" in TH20.read_text()
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in X11.read_text()

    print("Stage14-t76 frozen boundary: OK")


if __name__ == "__main__":
    main()
