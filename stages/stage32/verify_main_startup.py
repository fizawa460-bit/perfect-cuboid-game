#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V9_N355_FULL_PREFIX_AUDIT_CONSUMED"
EXPECTED_CANONICAL = "19bfec17ac2e306bf290b4b4933b5fe192ee5c8752f2fa5c31adfcf6dd953699"
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

EXPECTED_SYNC_BLOB = "7574fb2497d22bad47898ed30b4789a3fa1de310"
EXPECTED_SYNC_CANONICAL = "2451b411742b1316c7773db8b4e0b797fda98c0d512bede5a0c4d4be155c9a88"
EXPECTED_CREDIT = "EXACT_POST_AUDITED_N355_SUBSET_FULL_KNOWN_PREFIX_BLOCK_SUM_CUT_ONLY_30283389692998573007752221_ADDITIONAL_TERMINALS_REMAINING_17128_STRATA_66462870551188628549910_TERMINALS_NO_FULL178_COMPLETION_OR_THEOREM_CREDIT"


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
    assert frontier["n355_full_known_prefix_census_complete"] is True
    assert frontier["n355_full_maxcut_census_complete"] is False
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "POST_N355_FULL_PREFIX_RESIDUAL_STRUCTURE_RESEARCH"
    assert current["stacked_candidate_audit_status"] == "NONE"

    lock = state["source_locks"]["n355"]

    receipt_path = ROOT / lock["full_prefix_audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_FULL_PREFIX_RECEIPT_CANONICAL)
    assert git_blob_sha(receipt_path) == EXPECTED_FULL_PREFIX_RECEIPT_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_FULL_PREFIX_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_FULL_PREFIX_HEAD
    assert receipt["credit_ceiling"] == EXPECTED_CREDIT
    assert receipt["consumed_counts"]["additional_rejected_terminals"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert receipt["consumed_counts"]["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert receipt["consumed_counts"]["remaining_terminals"] == EXPECTED_REMAIN
    assert receipt["limitations"]["full_48_exceptional_completion"] is False
    assert receipt["limitations"]["full178_complete"] is False

    sync_path = ROOT / lock["management_path"]
    sync = load_canonical(sync_path, EXPECTED_SYNC_CANONICAL)
    assert git_blob_sha(sync_path) == EXPECTED_SYNC_BLOB
    assert sync["authority"]["n355_authority_credit"] is True
    assert sync["authority"]["n355_status"] == "AUDITED_FULL_KNOWN_PREFIX_BLOCK_SUM_CUT_CONSUMED"
    assert sync["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN
    assert sync["n355"]["full_prefix_audit_review_id"] == EXPECTED_FULL_PREFIX_REVIEW
    assert sync["n355"]["full_prefix_incremental_rejected_terminals"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert sync["n355"]["full_prefix_remaining_terminals"] == EXPECTED_REMAIN

    result_path = ROOT / lock["full_prefix_result_path"]
    result = load_canonical(result_path, EXPECTED_FULL_PREFIX_RESULT_CANONICAL)
    assert git_blob_sha(result_path) == EXPECTED_FULL_PREFIX_RESULT_BLOB
    agg = result["aggregate"]
    assert agg["candidate_incremental_rejected_terminals_after_audited_x1"] == EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT
    assert agg["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert agg["candidate_remaining_terminals"] == EXPECTED_REMAIN
    assert agg["full_prefix_rejected_terminals_from_n354"] == EXPECTED_FULL_PREFIX_TOTAL_REJECT_FROM_N354

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

    print("PASS Stage32 MAIN startup authority N355_FULL_PREFIX_AUDIT_CONSUMED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_REMAIN}_terminals")
    print(f"n355_full_prefix_incremental_reject={EXPECTED_FULL_PREFIX_INCREMENTAL_REJECT}")
    print("full_48_exceptional_completion=false full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=POST_N355_FULL_PREFIX_RESIDUAL_STRUCTURE_RESEARCH")


if __name__ == "__main__":
    main()
