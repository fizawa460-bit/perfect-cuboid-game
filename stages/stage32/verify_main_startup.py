#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V3_FULL178_FINAL_CHAIN_N350_CONTRACT_AUDIT_REQUIRED"
EXPECTED_CANONICAL = "c598c91acc2cb3fb61761168e6023eb5ca686efcc0e612652115efdc368c63fa"
EXPECTED_N240_SYNC_CANONICAL = "b1a84efcc6352122a3595628fdfea0658d5e38714f139ebaaad8bdc058d6bab3"
EXPECTED_N350_CANONICAL = "7292601f1ba187b5c607fa174e9edffd4ba96762ff9a40921e1ec14aadeaa42d"
EXPECTED_N350_CONTRACT_CANONICAL = "7d64040945f258048f9d61b0f888ca8d3720bedee6eab8902c7233ffc059d25a"
EXPECTED_N240_BLOB = "869c8b1dc3937a7e78e907e74b0ed08994a5199c"
EXPECTED_N350_BLOB = "af55b1b59d173d3ef4492a69e3a6e7c9aa24ce42"
EXPECTED_WORKING_SET = [
    "stages/stage32/management/post-n240-v2-hostile-reaudit-pass-sync-20260910.json",
    "stages/stage32/32-01-178/nodes/N350/STATE.json",
]


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


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
    assert target["full178_manifest_blob_sha1"] == "0a46b34e278688240656b4977e9cb7f589e90e06"
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
    assert auth["n240_hostile_reaudit_status"] == "PASS"
    assert auth["n240_hostile_reaudit_review_id"] == 5161254728
    assert auth["n240_hostile_reaudit_exact_head"] == "b56a832e6c194321916fe4ef63eef0d673b8ff9a"
    assert auth["n240_reaudit_consumed_at_structural_ceiling"] is True

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["primary_incomplete_remains_32_01"] is True
    assert frontier["n240_status"] == "AUDITED_STRUCTURAL_ADAPTER_ONLY"
    assert frontier["n240_validation"] == "HOSTILE_REAUDIT_PASS_CONSUMED"
    assert frontier["n240_hostile_reaudit_review_id"] == 5161254728
    assert frontier["n240_hostile_reaudit_exact_head"] == "b56a832e6c194321916fe4ef63eef0d673b8ff9a"
    assert frontier["n240_production_complete_available"] is False
    assert frontier["n240_n104_old_domain_release_available"] is False
    assert frontier["production_leaf_certificate_verifier_contract_registered"] is True
    assert frontier["production_leaf_certificate_verifier_contract_audited"] is False
    assert frontier["n350_status"] == "AUDIT_REQUIRED"
    assert frontier["n350_contract_canonical_sha256"] == EXPECTED_N350_CONTRACT_CANONICAL
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["ex5_retained_evidence_merged_to_main"] is True
    assert frontier["ex5_local_g1_d008_e4_exact_unsat_prefix"] == [0, 398]
    assert frontier["ex5_whole_g1_d008_e4_stratum_closed"] is False
    assert frontier["ex5_population_wide_full178_result_complete"] is False
    assert frontier["ex5_auto_promoted_to_n150"] is False
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["active_missing_interface"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert current["next_exact_route"] == "N350_HOSTILE_AUDIT_THEN_REGISTER_EXACT_PRODUCER_ADAPTER"
    assert current["mainbatch_stop_gate"] == "STOP_BEFORE_N350_AUTHORITY_PROMOTION_AND_REQUEST_EXTERNAL_STAGE32_01_178_AUDIT"
    assert current["stop_semantics"] == "N350_FAIL_CLOSED_META_CONTRACT_REGISTERED_AUDIT_REQUIRED_NO_PRODUCER_COVERAGE_FULL178_INCOMPLETE"

    assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
    for rel in EXPECTED_WORKING_SET:
        assert (ROOT / rel).is_file(), rel

    sync_path = ROOT / EXPECTED_WORKING_SET[0]
    sync = json.loads(sync_path.read_text())
    assert sync["schema"] == "STAGE32_MAIN_POST_N240_V2_HOSTILE_REAUDIT_PASS_SYNC_V1"
    assert sync["canonical_sha256_without_this_field"] == EXPECTED_N240_SYNC_CANONICAL
    assert csha(sync) == EXPECTED_N240_SYNC_CANONICAL
    assert sync["authority"]["n240_state_blob_sha1"] == EXPECTED_N240_BLOB
    assert sync["authority"]["n240_hostile_reaudit_status"] == "PASS"
    assert sync["authority"]["n240_hostile_reaudit_review_id"] == 5161254728
    assert sync["authority"]["n240_hostile_reaudit_exact_head"] == "b56a832e6c194321916fe4ef63eef0d673b8ff9a"
    assert sync["consumed_credit"]["structural_filtered_interval_adapter_mechanics"] is True
    assert sync["consumed_credit"]["old_canonical_rank_preserved_as_completeness_authority"] is True
    assert all(v is False for v in sync["not_consumed"].values())
    assert sync["claim_sync"]["full178_claim_core_changed"] is False
    assert sync["claim_sync"]["active_full178_claim_remains_incomplete"] is True
    assert sync["next_gate"]["heavy_compute_authorized"] is False

    n240_path = ROOT / "stages/stage32/32-01-178/nodes/N240/STATE.json"
    n240 = json.loads(n240_path.read_text())
    assert git_blob_sha(n240_path) == EXPECTED_N240_BLOB
    assert state["source_locks"]["n240_state"]["blob_sha1"] == EXPECTED_N240_BLOB
    assert n240["validation"]["status"] == "HOSTILE_REAUDIT_PASS_CONSUMED"
    assert n240["validation"]["hostile_reaudit_status"] == "PASS"
    assert n240["validation"]["hostile_reaudit_review_id"] == 5161254728
    assert n240["validation"]["hostile_reaudit_exact_head"] == "b56a832e6c194321916fe4ef63eef0d673b8ff9a"
    assert n240["retained_result"]["status"] == "AUDITED_STRUCTURAL_ADAPTER_ONLY"
    assert n240["retained_result"]["production_complete_available"] is False
    assert n240["retained_result"]["n104_old_domain_release_available"] is False
    assert n240["retained_result"]["full178_complete"] is False

    n350_path = ROOT / EXPECTED_WORKING_SET[1]
    n350 = json.loads(n350_path.read_text())
    assert git_blob_sha(n350_path) == EXPECTED_N350_BLOB
    assert n350["canonical_sha256_without_this_field"] == EXPECTED_N350_CANONICAL
    assert csha(n350) == EXPECTED_N350_CANONICAL
    assert n350["node_id"] == "N350"
    assert n350["validation"]["status"] == "AUDIT_REQUIRED"
    assert n350["validation"]["heavy_compute"] is False
    assert n350["retained_result"]["status"] == "AUDIT_REQUIRED"
    assert n350["retained_result"]["registered_producer_count"] == 0
    assert n350["retained_result"]["production_complete_available"] is False
    assert n350["retained_result"]["n104_old_domain_release_available"] is False
    assert n350["retained_result"]["full178_complete"] is False
    assert n350["implementation"]["contract_canonical_sha256"] == EXPECTED_N350_CONTRACT_CANONICAL
    n350_lock = state["source_locks"]["n350_contract"]
    assert n350_lock["state_blob_sha1"] == EXPECTED_N350_BLOB
    assert n350_lock["contract_blob_sha1"] == "31ab6791dfe48259b60d4917ecab2b4590b4eb63"
    assert n350_lock["contract_canonical_sha256"] == EXPECTED_N350_CONTRACT_CANONICAL
    assert n350_lock["verifier_blob_sha1"] == "3f1fcef571f09ade24977c771b0d438cf8c76723"
    assert n350_lock["workflow_blob_sha1"] == "e2cc191e6e5cba9f1d1361974a189e198156f33b"

    org = state["organizational_integration"]
    assert all(v is False for v in org["ordinary_separate_lane_startup"].values())
    assert org["EX5_separate_pr_active"] is False
    assert org["EX5_retained_evidence_merged_to_main"] is True
    assert org["integration_changes_mathematical_credit"] is False

    fw = state["firewalls"]
    assert fw["historical_q602_residues_treated_as_current_survivors"] is False
    assert fw["ex5_merge_auto_promotes_n150"] is False
    assert fw["ex5_merge_auto_promotes_full178"] is False
    assert fw["n240_reaudit_self_promoted"] is False
    assert fw["n240_structural_credit_exceeds_external_audit"] is False
    assert fw["production_complete_released_without_audited_leaf_contract"] is False
    assert fw["n104_completeness_release_granted"] is False
    assert fw["heavy_compute_authorized_by_startup_state"] is False
    assert fw["n350_contract_self_promoted_to_audited"] is False
    assert fw["n350_empty_registry_grants_production_credit"] is False
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

    print("PASS Stage32 MAIN startup authority FULL178_FINAL_CHAIN_N350_AUDIT_REQUIRED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("primary_incomplete=32-01_FULL178")
    print("n240=hostile_reaudit_PASS_consumed_structural_only")
    print("n350=fail_closed_meta_contract_AUDIT_REQUIRED_registered_producers_0")
    print("full178_complete=false heavy_compute_authorized=false")
    print("next_gate=N350_external_hostile_audit")


if __name__ == "__main__":
    main()
