#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V3_FULL178_FINAL_CHAIN_POST_EX5_MERGE"
EXPECTED_CANONICAL = "8f44f0473be26d183e3b9710e074f1b6d727ca825b543da8af3d31047284ca88"
EXPECTED_CHECKPOINT_CANONICAL = "6730cc294f6a2f5800a1ba6697639e5c25c4f6ce43361acffc9e130025858a0e"
EXPECTED_WORKING_SET = [
    "stages/stage32/management/post-ex5-merge-final-chain-sync-20260910.json",
    "stages/stage32/32-01-178/nodes/N240/STATE.json",
]


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    state = json.loads(STATE.read_text())
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert csha(state) == EXPECTED_CANONICAL

    target = state["current_target"]
    assert target["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert target["primary_incomplete_id"] == "32-01"
    assert target["primary_incomplete_name"] == "FULL178"
    assert target["full178_residual_row_count"] == 178
    assert target["full178_coarse_strata_count"] == 64111
    assert target["full178_manifest_canonical_sha256"] == "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
    assert target["V6_is_current_attack_target"] is False
    assert target["O210_is_current_attack_target"] is False
    assert target["Q602_is_current_attack_target"] is False

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False
    assert prov["narrow_chain_semantics"] == "AUDITED_CONSUMED_HISTORICAL_PREREQUISITE_PROVENANCE_NOT_CURRENT_ATTACK_TARGET"

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == "bf2890ec0b8168f70db803de876024aa6b6d1f6d"
    assert auth["ex5_merged_pr"] == 1742
    assert auth["ex5_hostile_audit_status"] == "PASS"
    assert auth["ex5_audited_exact_head"] == "a5e59bab3f7fe5a31e356c5a78edcbd741b093a6"
    assert auth["ex5_merge_commit"] == "bf2890ec0b8168f70db803de876024aa6b6d1f6d"
    assert auth["ex5_merge_auto_promotes_main_credit"] is False

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["primary_incomplete_remains_32_01"] is True
    assert frontier["n240_status"] == "AUDIT_REQUIRED"
    assert frontier["n240_validation"] == "HOSTILE_FAIL_REPAIRED_REAUDIT_REQUIRED"
    assert frontier["n240_production_complete_available"] is False
    assert frontier["n240_n104_old_domain_release_available"] is False
    assert frontier["ex5_retained_evidence_merged_to_main"] is True
    assert frontier["ex5_local_g1_d008_e4_exact_unsat_prefix"] == [0, 398]
    assert frontier["ex5_whole_g1_d008_e4_stratum_closed"] is False
    assert frontier["ex5_population_wide_full178_result_complete"] is False
    assert frontier["ex5_auto_promoted_to_n150"] is False
    assert frontier["stage32_closed"] is False

    assert state["current"]["active_missing_interface"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert state["current"]["next_exact_route"] == "N240_HOSTILE_REAUDIT_THEN_SOURCE_LOCKED_PRODUCTION_LEAF_CERTIFICATION"
    assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
    for rel in EXPECTED_WORKING_SET:
        assert (ROOT / rel).is_file(), rel

    checkpoint = json.loads((ROOT / EXPECTED_WORKING_SET[0]).read_text())
    assert checkpoint["canonical_sha256_without_this_field"] == EXPECTED_CHECKPOINT_CANONICAL
    assert csha(checkpoint) == EXPECTED_CHECKPOINT_CANONICAL
    assert checkpoint["status"] == "RETAINED_MANAGEMENT_SYNC_NO_NEW_MATHEMATICAL_CREDIT"
    assert checkpoint["ex5"]["auto_promoted_to_n150"] is False
    assert checkpoint["ex5"]["auto_promoted_to_full178"] is False
    assert checkpoint["n240"]["status"] == "AUDIT_REQUIRED"
    assert checkpoint["claim_sync"]["ex_to_main_promotion_performed"] is False

    n240 = json.loads((ROOT / EXPECTED_WORKING_SET[1]).read_text())
    assert git_blob_sha(ROOT / EXPECTED_WORKING_SET[1]) == state["source_locks"]["n240_state"]["blob_sha1"]
    assert n240["validation"]["status"] == "HOSTILE_FAIL_REPAIRED_REAUDIT_REQUIRED"
    assert n240["retained_result"]["status"] == "AUDIT_REQUIRED"
    assert n240["retained_result"]["production_complete_available"] is False
    assert n240["retained_result"]["n104_old_domain_release_available"] is False

    org = state["organizational_integration"]
    assert all(v is False for v in org["ordinary_separate_lane_startup"].values())
    assert org["EX5_separate_pr_active"] is False
    assert org["EX5_retained_evidence_merged_to_main"] is True
    assert org["integration_changes_mathematical_credit"] is False

    fw = state["firewalls"]
    assert fw["historical_q602_residues_treated_as_current_survivors"] is False
    assert fw["ex5_merge_auto_promotes_n150"] is False
    assert fw["ex5_merge_auto_promotes_full178"] is False
    assert fw["n240_repair_self_promoted_to_audited"] is False
    assert fw["n104_completeness_release_granted"] is False
    assert fw["heavy_compute_authorized_by_startup_state"] is False
    assert fw["stage32_closed"] is False

    cleanup = state["cleanup_gate"]
    assert cleanup["proof_or_source_locked_assets_may_be_deleted_without_reference_audit"] is False
    assert cleanup["root_cleanup_phase"] == "PHASE_C_USER_FACING_EX1_EX4_INTEGRATION_AND_LOOSE_ROOT_RELOCATION"
    assert cleanup["legacy_numbered_directories_physically_relocated"] is False

    startup = START.read_text()
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority FULL178_FINAL_CHAIN_POST_EX5_MERGE")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("primary_incomplete=32-01_FULL178")
    print("v6_o210_q602=current_targets:false")
    print("q602_residues_73_97_235=historical_provenance_only")
    print("ex5_pr1742=merged_retained_evidence_no_auto_n150_credit")
    print("next_gate=N240_fresh_hostile_reaudit")


if __name__ == "__main__":
    main()
