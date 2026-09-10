#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V5_N353_AUDITED_N354_REAUDIT_REQUIRED"
EXPECTED_CANONICAL = "55dc2129276bb85ac0cd1a4f7a2ed79c0a9d2c351beaf90b74c93fb6f47049af"
EXPECTED_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
EXPECTED_N353_REVIEW = 5163144778
EXPECTED_N353_HEAD = "0f8cee995e5c982cdb7ceceae14d69f91e65588d"
EXPECTED_N353_AUDIT_BLOB = "7f1e2a7d930e6ddc25b83e00321c40e68742d656"
EXPECTED_N353_AUDIT_CANONICAL = "fd3b372743e404570881bd5e25699dada273006bd006da8d5ac45d037a745d03"
EXPECTED_N354_RESULT_BLOB = "6f6ed5646689940cc304a655711dba83333d3576"
EXPECTED_N354_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
EXPECTED_SYNC_CANONICAL = "eaf5bbd1300921b6e9910e678c2f6ea92aed0de7f9716c6029707e0b6c5c7ef2"
EXPECTED_N354_VERIFIER_BLOB = "9e67a10127e192ad8922685adbcea1c77c4846f4"
EXPECTED_N354_PRIOR_AUDIT_REVIEW = 5163432572
EXPECTED_N354_PRIOR_AUDIT_HEAD = "ab0ce28876dbba306985343c104b02b69cec89fb"
EXPECTED_N354_REPAIR_COMMIT = "7c0125a56bead253f7c0799632e38a3882776bc8"
EXPECTED_WORKING_SET = [
    "stages/stage32/management/post-n353-hostile-pass-n354-checkpoint-20260910.json",
    "stages/stage32/32-01-178/nodes/N354/RESULT.json",
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


def load_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text())
    assert obj["canonical_sha256_without_this_field"] == expected
    assert csha(obj) == expected
    return obj


def main() -> None:
    state = load_canonical(STATE, EXPECTED_CANONICAL)
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"

    target = state["current_target"]
    assert target["control_mode"] == "FULL178_AND_FINAL_MILESTONE_CHAIN"
    assert target["primary_incomplete_id"] == "32-01"
    assert target["primary_incomplete_name"] == "FULL178"
    assert target["full178_residual_row_count"] == 178
    assert target["full178_coarse_strata_count"] == 64111
    assert target["V6_is_current_attack_target"] is False
    assert target["O210_is_current_attack_target"] is False
    assert target["Q602_is_current_attack_target"] is False

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_MAIN
    assert auth["stage32_main_integration_pr"] == 1753
    assert auth["n353_hostile_audit_status"] == "PASS"
    assert auth["n353_hostile_audit_review_id"] == EXPECTED_N353_REVIEW
    assert auth["n353_hostile_audit_exact_head"] == EXPECTED_N353_HEAD
    assert auth["n353_audit_credit_consumed"] is True
    assert auth["freshness_checkpoint"] == EXPECTED_N353_HEAD
    assert auth["claim_dag_semantic_status_changed"] is False
    assert auth["n354_prior_hostile_audit_status"] == "FAIL"
    assert auth["n354_prior_hostile_audit_review_id"] == EXPECTED_N354_PRIOR_AUDIT_REVIEW
    assert auth["n354_prior_audit_exact_head"] == EXPECTED_N354_PRIOR_AUDIT_HEAD
    assert auth["n354_ordering_repair_commit"] == EXPECTED_N354_REPAIR_COMMIT
    assert auth["n354_reaudit_required"] is True

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["primary_incomplete_remains_32_01"] is True
    assert frontier["full178_goal_claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1"
    assert frontier["full178_goal_authority_status"] == "DECLARED_GOAL"
    assert frontier["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert frontier["post_n220_strata"] == 60491
    assert frontier["post_n220_terminals"] == 346053707902916587089896969
    assert frontier["n353_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n353_rejected_strata"] == 12788
    assert frontier["n353_rejected_terminals"] == 264541612417334415376
    assert frontier["n353_remaining_strata"] == 47703
    assert frontier["n353_remaining_terminals"] == 346053443361304169755481593
    assert frontier["n354_status"] == "REAUDIT_REQUIRED_AFTER_ORDERING_REPAIR"
    assert frontier["n354_candidate_rejected_strata"] == 30575
    assert frontier["n354_candidate_rejected_terminals"] == 307492486826907032120701491
    assert frontier["n354_candidate_remaining_strata"] == 17128
    assert frontier["n354_candidate_remaining_terminals"] == 38560956534397137634780102
    assert frontier["n354_main_pruning_credit"] is False
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "N354_EXTERNAL_REAUDIT_AFTER_ORDERING_CANONICALIZATION"
    assert current["mainbatch_stop_gate"] == "STOP_BEFORE_N354_AUTHORITY_PROMOTION_AND_REQUEST_EXTERNAL_STAGE32_01_178_REAUDIT"
    assert state["current_leaf_working_set"] == EXPECTED_WORKING_SET
    for rel in EXPECTED_WORKING_SET:
        assert (ROOT / rel).is_file(), rel

    audit_path = ROOT / state["source_locks"]["n353_audit"]["path"]
    audit = load_canonical(audit_path, EXPECTED_N353_AUDIT_CANONICAL)
    assert git_blob_sha(audit_path) == EXPECTED_N353_AUDIT_BLOB
    assert audit["status"] == "PASS"
    assert audit["review_id"] == EXPECTED_N353_REVIEW
    assert audit["audited_exact_head"] == EXPECTED_N353_HEAD
    assert audit["consumed_counts"]["remaining_strata"] == 47703
    assert audit["consumed_counts"]["remaining_terminals"] == 346053443361304169755481593

    sync_path = ROOT / EXPECTED_WORKING_SET[0]
    sync = load_canonical(sync_path, EXPECTED_SYNC_CANONICAL)
    assert sync["authority_transition"]["n353_hostile_audit_status"] == "PASS"
    assert sync["authority_transition"]["n353_hostile_audit_review_id"] == EXPECTED_N353_REVIEW
    assert sync["claim_sync"]["goal_claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1"
    assert sync["claim_sync"]["goal_authority_status"] == "DECLARED_GOAL"
    assert sync["claim_sync"]["goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert sync["claim_sync"]["goal_core_semantic_change"] is False
    assert sync["claim_sync"]["full178_completion_claim_registered"] is False
    assert sync["n354_candidate"]["status"] == "REAUDIT_REQUIRED_AFTER_ORDERING_REPAIR"
    assert sync["n354_candidate"]["audit_repair"]["failure_class"] == "ORDERING_ONLY_MANIFEST_TRAVERSAL_HASH_INSTABILITY"
    assert sync["n354_candidate"]["audit_repair"]["canonical_order"] == "stable_sort_(g,d,e)"
    assert sync["n354_candidate"]["audit_repair"]["canonical_stream_changed"] is False
    assert sync["n354_candidate"]["audit_repair"]["unique_stratum_keys"] == 60491
    assert sync["n354_candidate"]["audit_repair"]["aggregate_changed"] is False
    assert sync["n354_candidate"]["main_credit"] is False

    n354_path = ROOT / EXPECTED_WORKING_SET[1]
    n354 = load_canonical(n354_path, EXPECTED_N354_RESULT_CANONICAL)
    assert git_blob_sha(n354_path) == EXPECTED_N354_RESULT_BLOB
    assert n354["status"] == "AUDIT_CANDIDATE_DIAGNOSTIC_NO_MAIN_CREDIT"
    assert n354["aggregate"]["n354_candidate_rejected_strata"] == 30575
    assert n354["aggregate"]["n354_candidate_rejected_terminals"] == 307492486826907032120701491
    assert n354["aggregate"]["n354_candidate_remaining_strata"] == 17128
    assert n354["aggregate"]["n354_candidate_remaining_terminals"] == 38560956534397137634780102
    assert n354["semantics"]["main_pruning_credit"] is False
    assert n354["semantics"]["full178_complete"] is False
    assert state["source_locks"]["n354"]["verifier_blob_sha1"] == EXPECTED_N354_VERIFIER_BLOB
    assert state["source_locks"]["management_sync"]["canonical_sha256"] == EXPECTED_SYNC_CANONICAL

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False

    fw = state["firewalls"]
    for key in [
        "historical_q602_residues_treated_as_current_survivors",
        "n353_credit_exceeds_external_audit",
        "n354_self_promoted_to_audited",
        "n354_candidate_counts_treated_as_main_pruning_credit",
        "n350_producer_registered_without_audit",
        "production_complete_released_without_audited_leaf_contract",
        "n104_completeness_release_granted",
        "heavy_compute_authorized_by_startup_state",
        "receiver_credit",
        "route_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        assert fw[key] is False, key

    startup = START.read_text()
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority N353_AUDITED_N354_REAUDIT_REQUIRED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("primary_incomplete=32-01_FULL178")
    print("n353=hostile_audit_PASS_consumed_bounded_cut")
    print("n354=REAUDIT_REQUIRED_after_ordering_repair_candidate_remaining_strata_17128")
    print("full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_gate=N354_external_reaudit_after_ordering_canonicalization")


if __name__ == "__main__":
    main()
