#!/usr/bin/env python3
"""Validate Stage14-t53 live stratification against the frozen ledger and result boundary."""

from __future__ import annotations

from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
AUDIT = ROOT / "stages/stage14/scripts/14-t/t53_kummer_principal_stratification_audit.py"
LIVE = ROOT / "stages/stage14/data/14-t53/kummer_principal_stratification.json"
FROZEN = ROOT / "stages/stage14/data/14-t53/kummer_principal_stratification_frozen.json"
RESULT = ROOT / "stages/stage14/14-t53/result.md"


def main():
    subprocess.run([sys.executable, str(AUDIT)], check=True, stdout=subprocess.DEVNULL)
    live = json.loads(LIVE.read_text())
    frozen = json.loads(FROZEN.read_text())
    result = RESULT.read_text()

    assert live["stage"] == frozen["stage"] == "14-t53"
    assert live["input"]["post_residue_principal_blocks"] == frozen["post_residue_principal_blocks"]
    assert live["input"]["distinct_ell_cross_good_ld2_blocks"] == frozen["distinct_ell_cross_good_ld2_blocks"]
    assert live["input"]["same_ell_ld2_blocks"] == frozen["same_ell_ld2_blocks"]

    strata = live["distinct_ell_strata"]
    assert strata["shared_U_blocks"] == frozen["shared_U_blocks"]
    assert strata["shared_V_blocks"] == frozen["shared_V_blocks"]
    assert strata["shared_U_or_V_union_blocks"] == frozen["shared_U_or_V_union_blocks"]
    assert strata["genuinely_UV_transverse_blocks"] == frozen["genuinely_UV_transverse_blocks"]
    assert strata["shared_U_blocks"] + strata["shared_V_blocks"] + strata["genuinely_UV_transverse_blocks"] == 12

    de = live["distinct_ell_flag_counts"]
    assert de["same_branch"] == frozen["distinct_ell_same_branch"]
    assert de["same_common_packet"] == frozen["distinct_ell_same_common_packet"]
    assert de["same_cover"] == frozen["distinct_ell_same_cover"]
    assert de["same_m"] == frozen["distinct_ell_same_m"]
    assert de["same_n"] == frozen["distinct_ell_same_n"]

    se = live["same_ell_flag_counts"]
    assert se["same_U_unit"] == frozen["same_ell_same_U"]
    assert se["same_V_unit"] == frozen["same_ell_same_V"]
    assert se["same_common_packet"] == frozen["same_ell_same_common_packet"]

    required_tokens = [
        "STAGE14_T53=COMPLETE_POST_RESIDUE_KUMMER_PRINCIPAL_STRATIFICATION",
        "FROZEN_SHARED_U_GENERIC_BLOCKS=6",
        "FROZEN_SHARED_V_GENERIC_BLOCKS=1",
        "FROZEN_UV_TRANSVERSE_GENERIC_BLOCKS=5",
        "POST_RESIDUE_COMMON_PACKET_COLLISIONS=0",
        "SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false",
        "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false",
        "T_O_SQRT_B_PROVED=false",
        "TH15_NEEDED=false",
    ]
    for token in required_tokens:
        assert token in result, token

    assert frozen["boundary"] == "COMPLETE_POST_RESIDUE_KUMMER_PRINCIPAL_STRATIFICATION"
    assert frozen["TH15_NEEDED"] is False
    assert frozen["SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED"] is False
    assert frozen["UV_TRANSVERSE_CROSS_GOOD_LD2_KUMMER_INCIDENCE_PROVED"] is False
    assert frozen["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
    assert frozen["T_O_SQRT_B_PROVED"] is False

    print("Stage14-t53 frozen ledger / boundary: OK")


if __name__ == "__main__":
    main()
