#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V10_N356_AUDIT_REQUIRED"
EXPECTED_CANONICAL = "6143a95a0fb380e3c30c6a464722b350666cec5f018318adefdae15800a676b3"
EXPECTED_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"

EXPECTED_SUBSET_REVIEW = 5165493296
EXPECTED_SUBSET_HEAD = "a13a39ba5ec0a281fcd65601f9f75d41405b1da1"
EXPECTED_SUBSET_REJECT = 8211103970847375998477971
EXPECTED_FULL_PREFIX_REVIEW = 5165895301
EXPECTED_FULL_PREFIX_HEAD = "3f3aadd2e5ada2a0a02a69490d6d659c02762682"
EXPECTED_FULL_PREFIX_RECEIPT_BLOB = "033294f56fb86d81b7aa43758a51a39747ccc082"
EXPECTED_FULL_PREFIX_RECEIPT_CANONICAL = "d6bda89f94eb57bf021f0acbbc5000e198f1805c09da3e5f9a531d20b70ce004"
EXPECTED_FULL_PREFIX_RESULT_BLOB = "0f30517cc5007ea435f4183201fc6cad699dd635"
EXPECTED_FULL_PREFIX_RESULT_CANONICAL = "7961cbc55993d2264879686388096fbe289a6fb84ecd4b6713b6b56c371bb775"
EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT = 30283389692998573007752221
EXPECTED_FULL_PREFIX_TOTAL_REJECT_FROM_N354 = 38494493663845949006230192
EXPECTED_REMAIN = 66462870551188628549910
EXPECTED_REMAIN_STRATA = 17128
EXPECTED_N355_SYNC_BLOB = "7574fb2497d22bad47898ed30b4789a3fa1de310"
EXPECTED_N355_SYNC_CANONICAL = "2451b411742b1316c7773db8b4e0b797fda98c0d512bede5a0c4d4be155c9a88"
EXPECTED_N355_CREDIT = "EXACT_POST_AUDITED_N355_SUBSET_FULL_KNOWN_PREFIX_BLOCK_SUM_CUT_ONLY_30283389692998573007752221_ADDITIONAL_TERMINALS_REMAINING_17128_STRATA_66462870551188628549910_TERMINALS_NO_FULL178_COMPLETION_OR_THEOREM_CREDIT"

EXPECTED_N356_MANAGEMENT_BLOB = "4af85896d3839c492773b2826f22790ad14895e1"
EXPECTED_N356_MANAGEMENT_CANONICAL = "1c2e3b6deb097587778d84ed2f29651ae7e1d77fb4cc042632c82db1bd8889ed"
EXPECTED_N356_RESULT_BLOB = "677b1ae2bab910db0805d20ee489d922522919ed"
EXPECTED_N356_RESULT_CANONICAL = "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"
EXPECTED_N356_REFERENCE_VERIFIER_BLOB = "ad0f5dcf7eb70cc24a9a54d4d31807226de1d2ad"
EXPECTED_N356_PARALLEL_VERIFIER_BLOB = "e0a1ea5e9fc4437ac39db1b332033e7274939b19"
EXPECTED_N356_WORKFLOW_BLOB = "68e105a1e2ccf65ab066e78fbb1e181368c9d5e0"
EXPECTED_N356_AFFECTED_STRATA = 4304
EXPECTED_N356_REJECT = 1065905560688394913696
EXPECTED_N356_CANDIDATE_REMAIN = 65396964990500233636214
EXPECTED_N356_STREAM = "f9a625cd546634ae208aae848657d7bc68023dd0916e35fc552cae3a188cfbe7"


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
    assert target["full178_residual_row_count"] == 178
    assert target["V6_is_current_attack_target"] is False
    assert target["O210_is_current_attack_target"] is False
    assert target["Q602_is_current_attack_target"] is False

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_MAIN
    assert auth["n355_hostile_audit_status"] == "PASS"
    assert auth["n355_hostile_audit_review_id"] == EXPECTED_SUBSET_REVIEW
    assert auth["n355_hostile_audit_exact_head"] == EXPECTED_SUBSET_HEAD
    assert auth["n355_audit_credit_consumed"] is True
    assert auth["n355_certified_subset_rejected_terminals"] == EXPECTED_SUBSET_REJECT
    assert auth["n355_full_prefix_hostile_audit_status"] == "PASS"
    assert auth["n355_full_prefix_hostile_audit_review_id"] == EXPECTED_FULL_PREFIX_REVIEW
    assert auth["n355_full_prefix_hostile_audit_exact_head"] == EXPECTED_FULL_PREFIX_HEAD
    assert auth["n355_full_prefix_audit_credit_consumed"] is True
    assert auth["n355_full_prefix_incremental_rejected_terminals"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert auth["n355_full_prefix_remaining_terminals"] == EXPECTED_REMAIN
    assert auth["n356_candidate_status"] == "AUDIT_REQUIRED"
    assert auth["n356_audit_credit_consumed"] is False
    assert auth["n356_candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert auth["n356_candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert auth["n356_candidate_remaining_terminals"] == EXPECTED_N356_CANDIDATE_REMAIN

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["full178_goal_authority_status"] == "DECLARED_GOAL"
    assert frontier["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert frontier["n354_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n355_status"] == "AUDITED_FULL_KNOWN_PREFIX_BLOCK_SUM_CUT_CONSUMED"
    assert frontier["n355_main_pruning_credit"] is True
    assert frontier["n355_subset_rejected_terminals"] == EXPECTED_SUBSET_REJECT
    assert frontier["n355_full_prefix_incremental_rejected_terminals"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert frontier["n355_rejected_terminals"] == EXPECTED_FULL_PREFIX_TOTAL_REJECT_FROM_N354
    assert frontier["n355_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["n355_remaining_terminals"] == EXPECTED_REMAIN
    assert frontier["authoritative_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_REMAIN
    assert frontier["n356_status"] == "AUDIT_REQUIRED"
    assert frontier["n356_main_pruning_credit"] is False
    assert frontier["n356_candidate_affected_strata"] == EXPECTED_N356_AFFECTED_STRATA
    assert frontier["n356_candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert frontier["n356_candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["n356_candidate_remaining_terminals"] == EXPECTED_N356_CANDIDATE_REMAIN
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "N356_EXTERNAL_HOSTILE_AUDIT_THEN_CONSUME_OPTIMISTIC_TRANSPORT_CUT"
    assert current["stacked_candidate_audit_status"] == "AUDIT_REQUIRED"
    assert current["mainbatch_stop_gate"] == "BEFORE_N356_PROMOTION"

    n355 = state["source_locks"]["n355"]
    receipt_path = ROOT / n355["full_prefix_audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_FULL_PREFIX_RECEIPT_CANONICAL)
    assert git_blob_sha(receipt_path) == EXPECTED_FULL_PREFIX_RECEIPT_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_FULL_PREFIX_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_FULL_PREFIX_HEAD
    assert receipt["credit_ceiling"] == EXPECTED_N355_CREDIT
    assert receipt["consumed_counts"]["additional_rejected_terminals"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert receipt["consumed_counts"]["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert receipt["consumed_counts"]["remaining_terminals"] == EXPECTED_REMAIN

    sync_path = ROOT / n355["management_path"]
    sync = load_canonical(sync_path, EXPECTED_N355_SYNC_CANONICAL)
    assert git_blob_sha(sync_path) == EXPECTED_N355_SYNC_BLOB
    assert sync["authority"]["n355_authority_credit"] is True
    assert sync["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN

    full_result_path = ROOT / n355["full_prefix_result_path"]
    full_result = load_canonical(full_result_path, EXPECTED_FULL_PREFIX_RESULT_CANONICAL)
    assert git_blob_sha(full_result_path) == EXPECTED_FULL_PREFIX_RESULT_BLOB

    n356 = state["source_locks"]["n356"]
    assert n356["management_blob_sha1"] == EXPECTED_N356_MANAGEMENT_BLOB
    assert n356["management_canonical_sha256"] == EXPECTED_N356_MANAGEMENT_CANONICAL
    assert n356["result_blob_sha1"] == EXPECTED_N356_RESULT_BLOB
    assert n356["result_canonical_sha256"] == EXPECTED_N356_RESULT_CANONICAL
    assert n356["reference_verifier_blob_sha1"] == EXPECTED_N356_REFERENCE_VERIFIER_BLOB
    assert n356["parallel_verifier_blob_sha1"] == EXPECTED_N356_PARALLEL_VERIFIER_BLOB
    assert n356["workflow_blob_sha1"] == EXPECTED_N356_WORKFLOW_BLOB

    n356_sync_path = ROOT / n356["management_path"]
    n356_sync = load_canonical(n356_sync_path, EXPECTED_N356_MANAGEMENT_CANONICAL)
    assert git_blob_sha(n356_sync_path) == EXPECTED_N356_MANAGEMENT_BLOB
    assert n356_sync["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN
    assert n356_sync["authority"]["n356_authority_credit"] is False
    assert n356_sync["n356"]["candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert n356_sync["n356"]["candidate_remaining_terminals"] == EXPECTED_N356_CANDIDATE_REMAIN

    n356_result_path = ROOT / n356["result_path"]
    n356_result = load_canonical(n356_result_path, EXPECTED_N356_RESULT_CANONICAL)
    assert git_blob_sha(n356_result_path) == EXPECTED_N356_RESULT_BLOB
    agg = n356_result["aggregate"]
    assert agg["affected_strata"] == EXPECTED_N356_AFFECTED_STRATA
    assert agg["candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert agg["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert agg["candidate_remaining_terminals"] == EXPECTED_N356_CANDIDATE_REMAIN
    assert agg["source_terminals_replayed"] == EXPECTED_REMAIN
    assert agg["per_stratum_stream_sha256"] == EXPECTED_N356_STREAM
    assert n356_result["semantics"]["main_pruning_credit"] is False
    assert n356_result["semantics"]["external_hostile_audit_required"] is True

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False

    fw = state["firewalls"]
    for key in [
        "historical_q602_residues_treated_as_current_survivors",
        "n353_credit_exceeds_external_audit",
        "n354_self_promoted_to_audited",
        "n354_credit_exceeds_external_audit",
        "n355_self_promoted_to_audited",
        "n355_credit_exceeds_external_audit",
        "n355_full_prefix_self_promoted_to_audited",
        "n355_full_prefix_credit_exceeds_external_audit",
        "n356_self_promoted_to_audited",
        "n356_credit_exceeds_external_audit",
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

    for rel in state["current_leaf_working_set"]:
        assert (ROOT / rel).is_file(), rel

    startup = START.read_text()
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority N356_AUDIT_REQUIRED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_REMAIN}_terminals")
    print(f"n356_candidate_reject={EXPECTED_N356_REJECT}")
    print(f"n356_candidate_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_N356_CANDIDATE_REMAIN}_terminals")
    print("n356_main_credit=false full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=N356_EXTERNAL_HOSTILE_AUDIT_THEN_CONSUME_OPTIMISTIC_TRANSPORT_CUT")


if __name__ == "__main__":
    main()
