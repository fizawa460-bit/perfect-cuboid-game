#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V12_N357_CONSUMED_POST_N357_SELECTION"
EXPECTED_CANONICAL = "5426fe193c2a833054858de2c9ac99e5daf7773171a6413bff40e7c742a0411e"
EXPECTED_BASE_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
EXPECTED_REMAIN_STRATA = 17128
EXPECTED_REMAIN_TERMINALS = 47598978285064933810198
EXPECTED_N357_REJECT = 17797986705435299826016
EXPECTED_N357_REVIEW = 5183069892
EXPECTED_N357_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"
EXPECTED_N357_RECEIPT_BLOB = "e9f93fb1b2bfeb68b72598632522d164fee715c6"
EXPECTED_N357_RECEIPT_CANONICAL = "74f294f87e0ae7f2f45b3f37f84f4d0636aecacf2210f9429f9ebafe5504ac31"
EXPECTED_N357_RESULT_BLOB = "50014d453266ad79101910a943d14388bd3ef6ec"
EXPECTED_N357_RESULT_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
EXPECTED_N357_STATE_BLOB = "b2c40d47b9efab836e228310a81f0fd8860ac507"
EXPECTED_N357_STATE_CANONICAL = "8cba4ce1d3b2c06740ddae4e3611015e8c4012bb6333f7f4c01db57acae62c54"
EXPECTED_N357_AUDIT_LOCK_BLOB = "9ce7477652b234e3424236bd2e61232fb38510d2"
EXPECTED_MANAGEMENT_BLOB = "1040370b6b98fc08f014aa4b104e3941e668a45a"
EXPECTED_MANAGEMENT_CANONICAL = "dd4e536e19995342cae674443173d64960b9f716869b2ce1fa43bc1a7bc55a43"
EXPECTED_HISTORICAL_V11_BLOB = "354b23978cde0bfdff45fa50ee452b3fb52503a4"
EXPECTED_HISTORICAL_V11_CANONICAL = "78d0306145f222466dfc205961e1db1ae5385ce7592a9fe451fb939bd7e0e40f"
EXPECTED_HISTORICAL_N357_STATE_BLOB = "eb4b8cfc26f789e2d0f9a1113f1894ebb730a443"
EXPECTED_HISTORICAL_N357_STATE_CANONICAL = "b2f4384ab176c0d855ee6e8d8a314e1c47c249239aca800c156938b2c944929f"
EXPECTED_CLAIM_WORKFLOW_BLOB = "8ecf0699856b83b6e37d80782d042018d205e6d0"


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
    assert obj["canonical_sha256_without_this_field"] == expected, path
    assert csha(obj) == expected, path
    return obj


def main() -> None:
    state = load_canonical(STATE, EXPECTED_CANONICAL)
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_BASE_MAIN
    assert auth["n356_audit_credit_consumed"] is True
    assert auth["n357_hostile_audit_status"] == "PASS"
    assert auth["n357_hostile_audit_review_id"] == EXPECTED_N357_REVIEW
    assert auth["n357_hostile_audit_exact_head"] == EXPECTED_N357_HEAD
    assert auth["n357_audit_credit_consumed"] is True
    assert auth["n357_status"] == "AUDITED_CONSUMED"
    assert auth["claim_dag_semantic_status_changed"] is False
    assert auth["claim_dag_full178_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE"

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["n357_main_pruning_credit"] is True
    assert frontier["n357_all178_srem_census_complete"] is True
    assert frontier["n357_incremental_rejected_terminals"] == EXPECTED_N357_REJECT
    assert frontier["n357_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["n357_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "POST_N357_FULL178_FRONTIER_SELECTION"
    assert current["stacked_candidate_audit_status"] == "N357_HOSTILE_PASS_CONSUMED"

    n357 = state["source_locks"]["n357"]
    receipt_path = ROOT / n357["audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_N357_RECEIPT_CANONICAL)
    assert git_blob_sha(receipt_path) == EXPECTED_N357_RECEIPT_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_N357_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_N357_HEAD
    counts = receipt["consumed_counts"]
    assert counts["additional_rejected_terminals"] == EXPECTED_N357_REJECT
    assert counts["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert counts["remaining_terminals"] == EXPECTED_REMAIN_TERMINALS

    result_path = ROOT / n357["result_path"]
    result = load_canonical(result_path, EXPECTED_N357_RESULT_CANONICAL)
    assert git_blob_sha(result_path) == EXPECTED_N357_RESULT_BLOB
    assert result["aggregate"]["candidate_incremental_rejected_terminals"] == EXPECTED_N357_REJECT
    assert result["aggregate"]["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert result["aggregate"]["candidate_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert result["semantics"]["main_pruning_credit"] is False
    assert result["semantics"]["external_hostile_audit_required_before_credit"] is True

    state_path = ROOT / n357["state_path"]
    n357_state = load_canonical(state_path, EXPECTED_N357_STATE_CANONICAL)
    assert git_blob_sha(state_path) == EXPECTED_N357_STATE_BLOB
    assert n357_state["status"] == "AUDITED_NECESSARY_CUT_CONSUMED_BY_MAIN"
    assert n357_state["credit"]["n357_main_pruning_credit"] is True
    assert n357_state["credit"]["full178_complete"] is False
    assert n357_state["next_exact_route"] == "POST_N357_FULL178_FRONTIER_SELECTION"

    audit_lock = ROOT / n357["audit_source_lock_verifier_path"]
    assert git_blob_sha(audit_lock) == EXPECTED_N357_AUDIT_LOCK_BLOB

    management_path = ROOT / state["source_locks"]["management_sync"]["path"]
    management = load_canonical(management_path, EXPECTED_MANAGEMENT_CANONICAL)
    assert git_blob_sha(management_path) == EXPECTED_MANAGEMENT_BLOB
    assert management["authority"]["n357_authority_credit"] is True
    assert management["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert management["claim_dag_sync"]["mathematical_claim_core_changed"] is False
    assert management["claim_dag_sync"]["full178_registered_authority_status_remains"] == "DECLARED_GOAL"

    hv11 = ROOT / state["source_locks"]["historical_v11_state"]["path"]
    load_canonical(hv11, EXPECTED_HISTORICAL_V11_CANONICAL)
    assert git_blob_sha(hv11) == EXPECTED_HISTORICAL_V11_BLOB
    hn357 = ROOT / state["source_locks"]["historical_n357_pre_audit_state"]["path"]
    load_canonical(hn357, EXPECTED_HISTORICAL_N357_STATE_CANONICAL)
    assert git_blob_sha(hn357) == EXPECTED_HISTORICAL_N357_STATE_BLOB

    claim_workflow = ROOT / state["source_locks"]["claim_frontier_workflow"]["path"]
    assert git_blob_sha(claim_workflow) == EXPECTED_CLAIM_WORKFLOW_BLOB

    lifecycle = state["workflow_lifecycle"]
    assert lifecycle["n356_workflow_classification"] == "ACTIVE_AUTO"
    assert lifecycle["post_n357_successor_auto_enabled"] is False
    assert lifecycle["retire_n356_before_or_with_successor_auto"] is True

    for key, value in state["firewalls"].items():
        if key in {
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
        }:
            assert value is False, key

    for rel in state["current_leaf_working_set"]:
        assert (ROOT / rel).is_file(), rel

    print("PASS Stage32 MAIN startup authority N357_CONSUMED_POST_N357_SELECTION")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_REMAIN_TERMINALS}_terminals")
    print(f"n357_audit_review={EXPECTED_N357_REVIEW} exact_head={EXPECTED_N357_HEAD}")
    print("n357_main_credit=true full178_complete=false merge_authorized=false")
    print("next_route=POST_N357_FULL178_FRONTIER_SELECTION")


if __name__ == "__main__":
    main()
