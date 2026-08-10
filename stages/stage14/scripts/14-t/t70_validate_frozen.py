#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t70/common_support_rootline_frozen.json"


def main() -> None:
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    a = d["audit"]
    assert d["input"]["reciprocal_states"] == 560
    assert d["input"]["invisible_states"] == 419
    assert d["input"]["mutually_cayley_private_pairs"] == 5
    assert a["crt_rootline_checks"] == 5
    assert a["same_sign_prime_power_orientation_checks"] == 6
    assert a["opposite_sign_prime_power_orientation_checks"] == 2
    assert a["primitive_rootline_exhaustive_regression_checks"] == 4272
    assert a["max_frozen_J"] == 75
    assert a["synthetic_small_J_clique_size"] == 6
    assert a["synthetic_pairwise_J_one_pairs"] == 15
    assert b["STAGE14_T70"] == "COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION"
    assert b["MERGED_S7_30_GLOBAL_11_16_LEDGER_IMPORTED"] is True
    assert b["COMMON_SUPPORT_PRIME_POWER_ROOT_ORIENTATION_PROVED"] is True
    assert b["FOUR_ORIENTATION_COMMON_SUPPORT_CRT_COMPRESSES_TO_ONE_LINEAR_ROOT_LINE"] is True
    assert b["T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED"] is True
    assert b["FULL_COMMON_SUPPORT_MUST_BE_USED_BEFORE_RADIAL_UNCHARGING"] is True
    assert b["FIXED_ANCHOR_COMMON_SUPPORT_ROOTLINE_PARTNER_BOUND_PROVED"] is True
    assert b["LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR"] is True
    assert b["GENERIC_SMALL_J_CAYLEY_RECONSTRUCTION_VALID"] is False
    assert b["SHARED_U_PRIVATE_LARGEST_PRIME_SMALL_COMMON_SUPPORT_PHYSICAL_SQUARE_SCALE_ENERGY_PROVED"] is False
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "11/16"
    assert b["T70_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING"] is False
    assert b["TH18_CONSUMED"] is True
    assert b["TH19_NEEDED"] is False
    assert b["NEXT"] == "Stage14-t71"
    print("Stage14-t70 frozen boundary OK")


if __name__ == "__main__":
    main()
