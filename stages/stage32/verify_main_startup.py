#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V8_N355_AUDITED_SUBSET_CONSUMED"
EXPECTED_CANONICAL = "048ee5bc0ab835878f35672ff7e97bd531b5b53e92af6fb463166758dcaa068e"
EXPECTED_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
EXPECTED_N355_REVIEW = 5165493296
EXPECTED_N355_HEAD = "a13a39ba5ec0a281fcd65601f9f75d41405b1da1"
EXPECTED_N355_AUDIT_BLOB = "2f89b467d5dab8865b4ac52b0c03333f2a903b8f"
EXPECTED_N355_AUDIT_CANONICAL = "bfb14b032932402c7b277fe301c9176fd3a80da5ef345d2c4c9961e676f6bf5e"
EXPECTED_N355_SYNC_BLOB = "e568077deb33c66d176c2d8bea9e29ce86acb24b"
EXPECTED_N355_SYNC_CANONICAL = "209a54c3c418554a1cf30ec61f0a80a2e065202e4f38dce359d674271d6a6e69"
EXPECTED_N355_RESULT_BLOB = "22141aa67a001bf0ccccc8504963ebe492c49669"
EXPECTED_N355_RESULT_CANONICAL = "241c0009f260a4136bc5abaa85caa08bfce9fea4f97c1744391e9331a21ad986"
EXPECTED_REJECT = 8211103970847375998477971
EXPECTED_REMAIN = 30349852563549761636302131
EXPECTED_CREDIT = "EXACT_POST_N354_FULL178_N355_LABEL99_DIAGONAL_CERTIFIED_SUBSET_CUT_ONLY_8211103970847375998477971_TERMINALS_NO_FULL_N355_MAXCUT_CENSUS_OR_FULL178_COMPLETION_OR_THEOREM_CREDIT"


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


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
    assert auth["n355_hostile_audit_review_id"] == EXPECTED_N355_REVIEW
    assert auth["n355_hostile_audit_exact_head"] == EXPECTED_N355_HEAD
    assert auth["n355_audit_credit_consumed"] is True
    assert auth["n355_certified_subset_rejected_terminals"] == EXPECTED_REJECT

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["full178_goal_authority_status"] == "DECLARED_GOAL"
    assert frontier["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert frontier["n354_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n355_status"] == "AUDITED_CERTIFIED_SUBSET_CUT_CONSUMED"
    assert frontier["n355_main_pruning_credit"] is True
    assert frontier["n355_rejected_terminals"] == EXPECTED_REJECT
    assert frontier["n355_remaining_strata"] == 17128
    assert frontier["n355_remaining_terminals"] == EXPECTED_REMAIN
    assert frontier["authoritative_remaining_strata"] == 17128
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_REMAIN
    assert frontier["n355_full_maxcut_census_complete"] is False
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "POST_N355_FULL_PREFIX_BLOCK_SUM_CENSUS_RESEARCH"
    assert current["stacked_candidate_audit_status"] == "NONE"

    lock = state["source_locks"]["n355"]
    audit_path = ROOT / lock["audit_receipt_path"]
    audit = load_canonical(audit_path, EXPECTED_N355_AUDIT_CANONICAL)
    assert git_blob_sha(audit_path) == EXPECTED_N355_AUDIT_BLOB
    assert audit["status"] == "PASS"
    assert audit["review_id"] == EXPECTED_N355_REVIEW
    assert audit["audited_exact_head"] == EXPECTED_N355_HEAD
    assert audit["credit_ceiling"] == EXPECTED_CREDIT
    assert audit["consumed_counts"]["rejected_terminals"] == EXPECTED_REJECT
    assert audit["consumed_counts"]["remaining_strata"] == 17128
    assert audit["consumed_counts"]["remaining_terminals"] == EXPECTED_REMAIN
    assert audit["limitations"]["full_n355_maxcut_census"] is False

    sync_path = ROOT / lock["management_path"]
    sync = load_canonical(sync_path, EXPECTED_N355_SYNC_CANONICAL)
    assert git_blob_sha(sync_path) == EXPECTED_N355_SYNC_BLOB
    assert sync["authority"]["n355_authority_credit"] is True
    assert sync["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN
    assert sync["n355"]["status"] == "AUDITED_CERTIFIED_SUBSET_CUT_CONSUMED"

    result_path = ROOT / lock["result_path"]
    result = load_canonical(result_path, EXPECTED_N355_RESULT_CANONICAL)
    assert git_blob_sha(result_path) == EXPECTED_N355_RESULT_BLOB
    assert result["exact_census"]["candidate_rejected_terminals"] == EXPECTED_REJECT
    assert result["exact_census"]["candidate_remaining_terminals"] == EXPECTED_REMAIN

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

    print("PASS Stage32 MAIN startup authority N355_AUDITED_SUBSET_CONSUMED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining=17128_strata/{EXPECTED_REMAIN}_terminals")
    print(f"n355_audited_subset_reject={EXPECTED_REJECT}")
    print("full_n355_maxcut_census=false full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=POST_N355_FULL_PREFIX_BLOCK_SUM_CENSUS_RESEARCH")


if __name__ == "__main__":
    main()
