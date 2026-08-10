#!/usr/bin/env python3
"""Validate the frozen Stage14-t75 theorem boundary."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FROZEN = ROOT / "stages/stage14/data/14-t75/angular_gcd_imbalance_frozen.json"
RESULT = ROOT / "stages/stage14/14-t75/result.md"
TH20 = ROOT / "stages/stage14/14-tH20/result.md"
X11 = ROOT / "stages/stage14/14-X11/result.md"


def main() -> None:
    data = json.loads(FROZEN.read_text())
    b = data["boundary"]
    assert data["reciprocal_states"] == 560
    assert data["invisible_states"] == 419
    assert data["column_split_checks"] == 419
    assert data["primitive_short_gap_checks"] == 419
    assert data["type_i_linearization_checks"] == 419
    assert data["imbalance_checks"] == 419
    assert data["large_g_divisor_sum_checks"] == 122
    assert data["exhaustive_primitive_short_gap_regressions"] == 4085
    assert data["diagnostic_counts"] == {
        "large_g_states": 60,
        "balanced_states": 293,
        "highly_unbalanced_states": 126,
    }
    assert data["max_gap_over_gc_over_H"] == "2/1"
    assert data["max_imbalance"] == "9/1"

    assert b["STAGE14_T75"].startswith("COMPLETE_")
    assert b["MERGED_T74_IMPORTED"] is True
    assert b["MERGED_TH20_IMPORTED"] is True
    assert b["MERGED_X11_GLOBAL_19_34_LEDGER_IMPORTED"] is True
    assert b["ANGULAR_G_SPLITS_UNIQUELY_ACROSS_COVER_COLUMNS"] is True
    assert b["PRIMITIVE_SHORT_GAP_LEMMA_PROVED"] is True
    assert b["LARGE_ANGULAR_G_PARAMETER_MASS_SAVING_PROVED"] is True
    assert b["LARGE_ANGULAR_G_PAIR_ENERGY_CLOSED"] is False
    assert b["HIGH_IMBALANCE_REDUCES_TO_ONE_VARIABLE_TYPE_I"] is True
    assert b["HIGH_IMBALANCE_TYPE_I_POWER_SAVING_PROVED"] is False
    assert b["POST_T75_GENUINE_TWO_VARIABLE_BLOCK_IS_BALANCED_SMALL_G"] is True
    assert b["TH20_MERGED"] is True
    assert b["TH20_CONSUMED_BY_T75"] is True
    assert b["TH20_USED_AS_HARD_THEOREM_PREDECESSOR"] is False
    assert b["TH21_NEEDED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "19/34"
    assert b["T75_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING"] is False
    assert b["NEXT"] == "Stage14-t76"

    result = RESULT.read_text()
    th20 = TH20.read_text()
    x11 = X11.read_text()
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in result
    assert "MERGED_TH20_IMPORTED=true" in result
    assert "SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedShortCoverTypeIIDispersionEnergy" in result
    assert "TH21_NEEDED=false" in result
    assert "STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT" in th20
    assert "ANGULAR_DIVISOR_SWITCHING_POST_T74_PREFERRED=true" in th20
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34" in x11
    print("Stage14-t75 frozen boundary: OK")


if __name__ == "__main__":
    main()
