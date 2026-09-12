#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
RECEIPT = HERE / "management/post-cut195-replacement-head-hostile-pass-merge-sync-20260912.json"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V16_CUT195_REAUDIT_CONSUMED_FULL178_SELECTED"
EXPECTED_STATE_BLOB = "514fd4d3e4ba8ab5e33b0ff9537350e82a123ce0"
EXPECTED_STATE_CANONICAL = "23918007afdf7b01c7736dfb938d3d51261d3f79939627df7737fa7de12ba882"
EXPECTED_REPOSITORY_MAIN = "e4d3b8b83626526ffeccdbd9c956081735fe1a6e"
EXPECTED_TREE = "fccba090fb1330a0167dde476440254bda43db3f"
RECEIPT_BLOB = "a38be20bf4db3342eb0fcea91c6f8aed50b03b54"
RECEIPT_CANONICAL = "9c5ef3da7907eb37b36e30d2feb7d47194d8765f8fac4cf72b1f102159190f2c"
AUDITED_V15_HEAD = "fdc372e1666e1176d80953b6303b13b240da84c5"
AUDITED_V15_REVIEW = 5185987769
POST = 47598978285064933757427
STRATA = 17128

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise AssertionError(path)
    return obj

def main() -> None:
    assert git_blob(STATE) == EXPECTED_STATE_BLOB
    state = load(STATE)
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"
    assert state["canonical_sha256_without_this_field"] == EXPECTED_STATE_CANONICAL
    assert canonical(state) == EXPECTED_STATE_CANONICAL

    assert git_blob(RECEIPT) == RECEIPT_BLOB
    receipt = load(RECEIPT)
    assert receipt["canonical_sha256_without_this_field"] == RECEIPT_CANONICAL
    assert canonical(receipt) == RECEIPT_CANONICAL

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_REPOSITORY_MAIN
    assert auth["cut195_post_sync_reaudit_required"] is True
    assert auth["cut195_post_sync_reaudit_status"] == "PASS"
    assert auth["cut195_post_sync_reaudit_exact_head"] == AUDITED_V15_HEAD
    assert auth["cut195_post_sync_reaudit_review_id"] == AUDITED_V15_REVIEW
    assert auth["cut195_synchronized_head_hostile_audited"] is True
    assert auth["cut195_audited_head_tree_sha"] == EXPECTED_TREE
    assert auth["current_repository_main_tree_sha"] == EXPECTED_TREE
    assert auth["cut195_audited_head_tree_equals_current_main_tree"] is True
    assert auth["cut195_merge_sync_receipt_blob_sha1"] == RECEIPT_BLOB
    assert auth["cut195_merge_sync_receipt_canonical_sha256"] == RECEIPT_CANONICAL

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == STRATA
    assert frontier["authoritative_remaining_terminals"] == POST
    assert frontier["cut195_main_pruning_credit"] is True
    assert frontier["cut195_synchronized_head_hostile_audited"] is True
    assert frontier["cut195_post_sync_reaudit_review_id"] == AUDITED_V15_REVIEW
    assert frontier["cut195_post_sync_reaudit_exact_head"] == AUDITED_V15_HEAD
    assert frontier["full178_frontier_selected_after_cut195_reaudit"] is True
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["cut196_main_pruning_credit"] is False
    assert frontier["cut196_candidate_observed_rejected_terminals"] == 27346
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["mainbatch_stop_gate"] == "FULL178_FRONTIER_ACTIVE_INCOMPLETE"
    assert current["next_exact_route"] == "FULL178_FRONTIER_SELECTION_AFTER_CUT195_REAUDIT"

    sl = state["source_locks"]["v15_replacement_head_audit_merge_sync"]
    assert sl["audited_pr"] == 1788
    assert sl["audited_exact_head"] == AUDITED_V15_HEAD
    assert sl["audited_exact_head_tree_sha"] == EXPECTED_TREE
    assert sl["hostile_reaudit_review_id"] == AUDITED_V15_REVIEW
    assert sl["hostile_reaudit_status"] == "PASS"
    assert sl["merge_commit"] == EXPECTED_REPOSITORY_MAIN
    assert sl["merge_commit_tree_sha"] == EXPECTED_TREE
    assert sl["tree_equivalent"] is True
    assert sl["receipt_blob_sha1"] == RECEIPT_BLOB
    assert sl["receipt_canonical_sha256"] == RECEIPT_CANONICAL
    assert sl["full178_frontier_selected"] is True
    assert sl["active_frontier_claim_status"] == "ACTIVE_INCOMPLETE"

    rb = receipt["audited_boundary"]
    mb = receipt["merge_boundary"]
    ap = receipt["authority_projection"]
    assert rb["pr"] == 1788
    assert rb["exact_head"] == AUDITED_V15_HEAD
    assert rb["hostile_reaudit_status"] == "PASS"
    assert rb["hostile_reaudit_review_id"] == AUDITED_V15_REVIEW
    assert rb["tree_sha"] == EXPECTED_TREE
    assert mb["merge_commit"] == EXPECTED_REPOSITORY_MAIN
    assert mb["tree_sha"] == EXPECTED_TREE
    assert mb["audited_head_tree_equals_merge_commit_tree"] is True
    assert ap["cut195_post_sync_reaudit_consumed"] is True
    assert ap["authoritative_remaining_strata"] == STRATA
    assert ap["authoritative_remaining_terminals"] == POST
    assert ap["full178_numerical_census_complete"] is False
    assert ap["full178_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert receipt["cut196_observation"]["main_pruning_credit"] is False
    assert receipt["cut196_observation"]["claim_frontier_ci_conclusion"] == "FAILURE"
    assert receipt["claim_sync"]["claim_core_changed"] is False
    assert receipt["claim_sync"]["active_frontier_claim_status_changed"] is False
    assert receipt["claim_sync"]["authority_projection_changed"] is True

    fw = state["firewalls"]
    for key in (
        "cut195_main_credit_without_current_v14_composition_audit",
        "n357_main_credit_without_current_authority_composition_audit",
        "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit",
        "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ):
        assert fw[key] is False, key

    for rel in state["current_leaf_working_set"]:
        assert (ROOT / rel).is_file(), rel

    startup = START.read_text(encoding="utf-8")
    assert "Do not merge without explicit user authorization." in startup

    print("PASS Stage32 MAIN V16 CUT195 replacement-head audit consumed")
    print(f"authority={STRATA}/{POST}")
    print("full178_frontier=ACTIVE_INCOMPLETE cut196_main_credit=false")
    print("merge_authorized=false")

if __name__ == "__main__":
    main()
