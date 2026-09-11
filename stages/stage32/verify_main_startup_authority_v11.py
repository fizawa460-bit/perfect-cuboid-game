#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
V10 = HERE / "verify_main_startup_authority_v10.py"
HISTORICAL_V10_STATE = HERE / "proof/historical-routing-blobs/9981889309c833a1834eaadddce73e52c0aa0176.json"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V11_N356_CONSUMED_N357_RESEARCH"
EXPECTED_CANONICAL = "78d0306145f222466dfc205961e1db1ae5385ce7592a9fe451fb939bd7e0e40f"
EXPECTED_BASE_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
EXPECTED_REMAIN_STRATA = 17128
EXPECTED_REMAIN_TERMINALS = 65396964990500233636214
EXPECTED_N356_REJECT = 1065905560688394913696
EXPECTED_N356_REVIEW = 5176607630
EXPECTED_N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
EXPECTED_N356_RECEIPT_BLOB = "4966d57f61624c1cfd313ae5d1fe5e33bb25e569"
EXPECTED_N356_RECEIPT_CANONICAL = "fdeedf56ba9dca97dc06175f892efeae09fd7ef0d3bb8670bfea438106227b74"
EXPECTED_MANAGEMENT_BLOB = "3a82ffc1d41655d17adb83ca7a4551d80ecfe8ed"
EXPECTED_MANAGEMENT_CANONICAL = "ff90000cb353d8f3f5994588541cc39c5448973f9796950c7317969c472b5269"
EXPECTED_N357_STATE_BLOB = "eb4b8cfc26f789e2d0f9a1113f1894ebb730a443"
EXPECTED_N357_STATE_CANONICAL = "b2f4384ab176c0d855ee6e8d8a314e1c47c249239aca800c156938b2c944929f"
EXPECTED_N357_CONTRACT_BLOB = "8a2a0048d216de9d177dc581dc208b51c6436442"
EXPECTED_N357_VERIFIER_BLOB = "b164bc85e0e58ca36b72504b8f32874484d56bf6"
EXPECTED_N357_ENGINE_BLOB = "479c783cb42d0952cc310708106787147b499240"

EXPECTED_N356_RESULT_BLOB = "677b1ae2bab910db0805d20ee489d922522919ed"
EXPECTED_N356_RESULT_CANONICAL = "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"
EXPECTED_N356_DEP_LOCK_BLOB = "45c0c793f8b2edfec29728412f2951ce9639e352"
EXPECTED_N356_SERIAL_ENTRY_BLOB = "a7fdee753ba3cb46766ad465f1d4db50a493d6b1"
EXPECTED_N356_PARALLEL_ENTRY_BLOB = "d7d2e93ea125ee1002d2d39ebf64c7deb0fe9e12"
EXPECTED_N356_FAST_ENTRY_BLOB = "cf508c75d847c6e9df0119f805987fa4ac98cfc6"


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


def replay_v10_historical_authority() -> None:
    spec = importlib.util.spec_from_file_location("stage32_main_authority_v10_frozen", V10)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert git_blob_sha(HISTORICAL_V10_STATE) == "9981889309c833a1834eaadddce73e52c0aa0176"
    mod.STATE = HISTORICAL_V10_STATE
    startup = START.read_text()
    class StartupCompatProxy:
        def read_text(self, *args, **kwargs):
            return startup + "\nOrdinary `Stage32-main-batch` reads, in this order:\n"
    mod.START = StartupCompatProxy()
    mod.main()


def main() -> None:
    replay_v10_historical_authority()

    state = load_canonical(STATE, EXPECTED_CANONICAL)
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_BASE_MAIN
    assert auth["n356_hostile_audit_status"] == "PASS"
    assert auth["n356_hostile_audit_review_id"] == EXPECTED_N356_REVIEW
    assert auth["n356_hostile_audit_exact_head"] == EXPECTED_N356_HEAD
    assert auth["n356_audit_credit_consumed"] is True
    assert auth["n356_candidate_status"] == "AUDITED_CONSUMED"
    assert auth["claim_dag_semantic_status_changed"] is False
    assert auth["claim_dag_full178_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE"
    assert auth["n357_status"] == "RETAINED_RESEARCH_CHECKPOINT_NO_MAIN_CREDIT"

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["n356_main_pruning_credit"] is True
    assert frontier["n356_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n356_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert frontier["n356_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["n356_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert frontier["n357_status"] == "RETAINED_RESEARCH_CHECKPOINT_NO_MAIN_CREDIT"
    assert frontier["n357_main_pruning_credit"] is False
    assert frontier["n357_all178_srem_census_complete"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "N357_ALL178_SREM_SYMBOLIC_CENSUS"
    assert current["mainbatch_stop_gate"] == "N357_RESEARCH_FRONTIER_NO_MAIN_CREDIT"
    assert current["stacked_candidate_audit_status"] == "N356_HOSTILE_PASS_CONSUMED"

    n356 = state["source_locks"]["n356"]
    receipt_path = ROOT / n356["audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_N356_RECEIPT_CANONICAL)
    assert git_blob_sha(receipt_path) == EXPECTED_N356_RECEIPT_BLOB
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_N356_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_N356_HEAD
    assert receipt["consumed_counts"]["additional_rejected_terminals"] == EXPECTED_N356_REJECT
    assert receipt["consumed_counts"]["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert receipt["consumed_counts"]["remaining_terminals"] == EXPECTED_REMAIN_TERMINALS

    n356_result_path = ROOT / n356["result_path"]
    n356_result = load_canonical(n356_result_path, EXPECTED_N356_RESULT_CANONICAL)
    assert git_blob_sha(n356_result_path) == EXPECTED_N356_RESULT_BLOB
    assert n356_result["aggregate"]["candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert n356_result["aggregate"]["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert n356_result["aggregate"]["candidate_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert n356_result["semantics"]["main_pruning_credit"] is False
    assert n356_result["semantics"]["external_hostile_audit_required"] is True

    for rel, expected in [
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_dependency_source_locks.py", EXPECTED_N356_DEP_LOCK_BLOB),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport.py", EXPECTED_N356_SERIAL_ENTRY_BLOB),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport_parallel.py", EXPECTED_N356_PARALLEL_ENTRY_BLOB),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport_fast.py", EXPECTED_N356_FAST_ENTRY_BLOB),
    ]:
        assert git_blob_sha(ROOT / rel) == expected

    management_path = ROOT / "stages/stage32/management/post-n356-hostile-pass-n357-checkpoint-20260911.json"
    management = load_canonical(management_path, EXPECTED_MANAGEMENT_CANONICAL)
    assert git_blob_sha(management_path) == EXPECTED_MANAGEMENT_BLOB
    assert management["authority"]["n356_authority_credit"] is True
    assert management["authority"]["n357_authority_credit"] is False
    assert management["authority"]["authoritative_remaining_terminals"] == EXPECTED_REMAIN_TERMINALS
    assert management["claim_dag_sync"]["mathematical_claim_core_changed"] is False
    assert management["claim_dag_sync"]["full178_registered_authority_status_remains"] == "DECLARED_GOAL"

    n357 = state["source_locks"]["n357"]
    assert git_blob_sha(ROOT / n357["contract_path"]) == EXPECTED_N357_CONTRACT_BLOB
    assert git_blob_sha(ROOT / n357["verifier_path"]) == EXPECTED_N357_VERIFIER_BLOB
    assert git_blob_sha(ROOT / n357["frozen_engine_path"]) == EXPECTED_N357_ENGINE_BLOB
    n357_state = load_canonical(ROOT / n357["state_path"], EXPECTED_N357_STATE_CANONICAL)
    assert git_blob_sha(ROOT / n357["state_path"]) == EXPECTED_N357_STATE_BLOB
    assert n357_state["status"] == "RETAINED_RESEARCH_CHECKPOINT_AFTER_N356_HOSTILE_AUDIT_NO_MAIN_CREDIT"
    assert n357_state["credit"]["n356_main_pruning_credit_after_authority_sync"] is True
    assert n357_state["credit"]["n357_main_pruning_credit"] is False
    assert n357_state["next_exact_route"] == "BUILD_ALL178_SREM_SYMBOLIC_CENSUS"

    lifecycle = state["workflow_lifecycle"]
    assert lifecycle["n356_workflow_classification"] == "ACTIVE_AUTO"
    assert lifecycle["n356_role"] == "AUDITED_CONSUMED_AUTHORITY_REPLAY_GUARD"
    assert lifecycle["n357_successor_auto_enabled"] is False
    assert lifecycle["retire_n356_before_or_with_n357_successor_auto"] is True

    fw = state["firewalls"]
    for key in [
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

    print("PASS Stage32 MAIN startup authority N356_CONSUMED_N357_RESEARCH")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_REMAIN_TERMINALS}_terminals")
    print(f"n356_audit_review={EXPECTED_N356_REVIEW} exact_head={EXPECTED_N356_HEAD}")
    print("n356_main_credit=true n357_main_credit=false full178_complete=false merge_authorized=false")
    print("next_route=N357_ALL178_SREM_SYMBOLIC_CENSUS")


if __name__ == "__main__":
    main()
