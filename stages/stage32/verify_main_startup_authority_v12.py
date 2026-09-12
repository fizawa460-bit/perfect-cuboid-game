#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V13_N358_CONSUMED_POST_N358_SELECTION"
EXPECTED_CANONICAL = "ee451b06cfe5052cbedde107f09e13cfc232647edf88de84cf02fb81c4ed94c6"
EXPECTED_BASE_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
EXPECTED_REMAIN_STRATA = 17128
EXPECTED_REMAIN_TERMINALS = 47589703313957134966240
EXPECTED_N357_REMAIN_TERMINALS = 47598978285064933810198
EXPECTED_N358_REJECT = 9274971107798843958
EXPECTED_N358_REJECT_PREFIXES = 11344256366314850
EXPECTED_N358_REVIEW = 5184322011
EXPECTED_N358_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
EXPECTED_N358_RECEIPT_BLOB = "7b36e0159987ef65485d36fa2d672c8ee3a1ff33"
EXPECTED_N358_RECEIPT_CANONICAL = "bd27a2de6f54d5190f64917f90d64e1a07d4dac3c28947c2b44c94c6977f3482"
EXPECTED_N358_RESULT_BLOB = "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"
EXPECTED_N358_RESULT_CANONICAL = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
EXPECTED_N358_STATE_BLOB = "6091b0da0acc3fb4b3b2143327f7d57f5323668e"
EXPECTED_N358_STATE_CANONICAL = "0d96ed9bc530291e826682d2302e1b05bd985a83cb83631e38b694afbc4e09a4"
EXPECTED_N358_AUDIT_LOCK_BLOB = "78db45499a79438a4f01889012a358a39e43ea8c"
EXPECTED_MANAGEMENT_BLOB = "a0569048cfb3a7f0d048e58a438ed02110d5a7cc"
EXPECTED_MANAGEMENT_CANONICAL = "f16ead9c2773aae7089978788629a7c4a5a8442975f582cdf1139370fa5a78b9"
EXPECTED_CLAIM_WORKFLOW_BLOB = "30868ab4f29753f3e9f379701b83ddfd37cea58c"
EXPECTED_N357_RECEIPT_BLOB = "e9f93fb1b2bfeb68b72598632522d164fee715c6"
EXPECTED_N357_RECEIPT_CANONICAL = "74f294f87e0ae7f2f45b3f37f84f4d0636aecacf2210f9429f9ebafe5504ac31"
EXPECTED_N357_REVIEW = 5183069892
EXPECTED_N357_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"


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
    assert auth["n357_audit_credit_consumed"] is True
    assert auth["n357_hostile_audit_status"] == "PASS"
    assert auth["n357_hostile_audit_review_id"] == EXPECTED_N357_REVIEW
    assert auth["n357_hostile_audit_exact_head"] == EXPECTED_N357_HEAD
    assert auth["n358_hostile_audit_status"] == "PASS"
    assert auth["n358_hostile_audit_review_id"] == EXPECTED_N358_REVIEW
    assert auth["n358_hostile_audit_exact_head"] == EXPECTED_N358_HEAD
    assert auth["n358_audit_credit_consumed"] is True
    assert auth["n358_status"] == "AUDITED_CONSUMED"
    assert auth["claim_dag_semantic_status_changed"] is False
    assert auth["claim_dag_full178_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE"

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["n357_main_pruning_credit"] is True
    assert frontier["n357_remaining_terminals"] == EXPECTED_N357_REMAIN_TERMINALS
    assert frontier["n358_main_pruning_credit"] is True
    assert frontier["n358_exact_incremental_census_complete"] is True
    assert frontier["n358_incremental_rejected_exceptional_prefixes"] == EXPECTED_N358_REJECT_PREFIXES
    assert frontier["n358_incremental_rejected_terminals"] == EXPECTED_N358_REJECT
    assert frontier["n358_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["n358_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "POST_N358_FULL178_FRONTIER_SELECTION"
    assert current["stacked_candidate_audit_status"] == "N358_HOSTILE_PASS_CONSUMED"

    n358 = state["source_locks"]["n358"]
    receipt_path = ROOT / n358["audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_N358_RECEIPT_CANONICAL)
    assert git_blob_sha(receipt_path) == EXPECTED_N358_RECEIPT_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_N358_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_N358_HEAD
    counts = receipt["consumed_counts"]
    assert counts["additional_rejected_exceptional_prefixes"] == EXPECTED_N358_REJECT_PREFIXES
    assert counts["additional_rejected_terminals"] == EXPECTED_N358_REJECT
    assert counts["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert counts["remaining_terminals"] == EXPECTED_REMAIN_TERMINALS

    result_path = ROOT / n358["result_path"]
    result = load_canonical(result_path, EXPECTED_N358_RESULT_CANONICAL)
    assert git_blob_sha(result_path) == EXPECTED_N358_RESULT_BLOB
    assert result["aggregate"]["incremental_rejected_exceptional_prefixes"] == EXPECTED_N358_REJECT_PREFIXES
    assert result["aggregate"]["incremental_rejected_terminals"] == EXPECTED_N358_REJECT
    assert result["aggregate"]["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert result["aggregate"]["candidate_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert result["semantics"]["main_pruning_credit"] is False
    assert result["semantics"]["external_hostile_audit_required_before_credit"] is True

    state_path = ROOT / n358["state_path"]
    n358_state = load_canonical(state_path, EXPECTED_N358_STATE_CANONICAL)
    assert git_blob_sha(state_path) == EXPECTED_N358_STATE_BLOB
    assert n358_state["status"] == "AUDITED_NECESSARY_CUT_CONSUMED_BY_MAIN"
    assert n358_state["credit"]["n358_main_pruning_credit"] is True
    assert n358_state["credit"]["full178_complete"] is False
    assert n358_state["next_exact_route"] == "POST_N358_FULL178_FRONTIER_SELECTION"

    audit_lock = ROOT / n358["audit_source_lock_verifier_path"]
    assert git_blob_sha(audit_lock) == EXPECTED_N358_AUDIT_LOCK_BLOB

    n357 = state["source_locks"]["n357"]
    n357_receipt_path = ROOT / n357["audit_receipt_path"]
    n357_receipt = load_canonical(n357_receipt_path, EXPECTED_N357_RECEIPT_CANONICAL)
    assert git_blob_sha(n357_receipt_path) == EXPECTED_N357_RECEIPT_BLOB
    assert n357_receipt["status"] == "PASS"
    assert n357_receipt["review_id"] == EXPECTED_N357_REVIEW

    management_path = ROOT / state["source_locks"]["management_sync"]["path"]
    management = load_canonical(management_path, EXPECTED_MANAGEMENT_CANONICAL)
    assert git_blob_sha(management_path) == EXPECTED_MANAGEMENT_BLOB
    assert management["authority"]["n358_authority_credit"] is True
    assert management["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert management["claim_dag_sync"]["mathematical_claim_core_changed"] is False
    assert management["claim_dag_sync"]["full178_registered_authority_status_remains"] == "DECLARED_GOAL"

    claim_workflow = ROOT / state["source_locks"]["claim_frontier_workflow"]["path"]
    assert git_blob_sha(claim_workflow) == EXPECTED_CLAIM_WORKFLOW_BLOB

    lifecycle = state["workflow_lifecycle"]
    assert lifecycle["n356_workflow_classification"] == "ACTIVE_AUTO"
    assert lifecycle["n358_audit_replay_mode"] == "FROZEN_EXACT_HEAD_REPLAY_IN_CLAIM_FRONTIER"
    assert lifecycle["post_n358_successor_auto_enabled"] is False
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

    print("PASS Stage32 MAIN startup authority N358_CONSUMED_POST_N358_SELECTION")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_REMAIN_TERMINALS}_terminals")
    print(f"n358_audit_review={EXPECTED_N358_REVIEW} exact_head={EXPECTED_N358_HEAD}")
    print("n358_main_credit=true full178_complete=false merge_authorized=false")
    print("next_route=POST_N358_FULL178_FRONTIER_SELECTION")


if __name__ == "__main__":
    main()
