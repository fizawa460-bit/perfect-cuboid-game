#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V11_N356_AUDITED_CONSUMED"
EXPECTED_CANONICAL = "9167620fab303b3bf8ffa6fcae2e2201bcd4d8e3b0c7ad2b41f6263a4dfd0106"
EXPECTED_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"

EXPECTED_N355_REVIEW = 5165895301
EXPECTED_N355_HEAD = "3f3aadd2e5ada2a0a02a69490d6d659c02762682"
EXPECTED_N355_REMAIN = 66462870551188628549910

EXPECTED_N356_REVIEW = 5176607630
EXPECTED_N356_HEAD = "0cd222d4824e65ea122bc90ac0d48686ddae38f2"
EXPECTED_N356_CI = 34578552640
EXPECTED_N356_REJECT = 1065905560688394913696
EXPECTED_N356_REMAIN = 65396964990500233636214
EXPECTED_REMAIN_STRATA = 17128

EXPECTED_RECEIPT_BLOB = "b6dd078c258c51b88c7fccb791893af6dc7a81f1"
EXPECTED_RECEIPT_CANONICAL = "b710cb0fdaf9f5308655e3c5491ec4017e5f19a6a82f3fd5477a8e2396881505"
EXPECTED_MANAGEMENT_BLOB = "715aa701208b576b78503dabf294a7b5c71c971e"
EXPECTED_MANAGEMENT_CANONICAL = "ef33829623f399fd5de2d46ce529c6a4b8eb8f14ba490057b65246f6f4919933"
EXPECTED_RESULT_BLOB = "677b1ae2bab910db0805d20ee489d922522919ed"
EXPECTED_RESULT_CANONICAL = "d1aecec8b78c78f03fa7b82b3dc136668f435d9cfb98636a1a23b704431abe31"
EXPECTED_RESULT_STREAM = "f9a625cd546634ae208aae848657d7bc68023dd0916e35fc552cae3a188cfbe7"

EXPECTED_DEP_LOCK = "45c0c793f8b2edfec29728412f2951ce9639e352"
EXPECTED_PUBLIC_SERIAL = "a7fdee753ba3cb46766ad465f1d4db50a493d6b1"
EXPECTED_PUBLIC_PARALLEL = "d7d2e93ea125ee1002d2d39ebf64c7deb0fe9e12"
EXPECTED_PUBLIC_FAST = "cf508c75d847c6e9df0119f805987fa4ac98cfc6"
EXPECTED_ENGINE_SERIAL = "ad0f5dcf7eb70cc24a9a54d4d31807226de1d2ad"
EXPECTED_ENGINE_PARALLEL = "e0a1ea5e9fc4437ac39db1b332033e7274939b19"
EXPECTED_ENGINE_FAST = "ec2bba109f4a42816f366dbf605afeea7c16f0a2"


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


def assert_blob(path: Path, expected: str) -> None:
    actual = git_blob_sha(path)
    assert actual == expected, f"{path}: {actual}!={expected}"


def main() -> None:
    state = load_canonical(STATE, EXPECTED_CANONICAL)
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_MAIN
    assert auth["n355_full_prefix_hostile_audit_status"] == "PASS"
    assert auth["n355_full_prefix_hostile_audit_review_id"] == EXPECTED_N355_REVIEW
    assert auth["n355_full_prefix_hostile_audit_exact_head"] == EXPECTED_N355_HEAD
    assert auth["n355_full_prefix_audit_credit_consumed"] is True
    assert auth["n355_full_prefix_remaining_terminals"] == EXPECTED_N355_REMAIN
    assert auth["n356_hostile_audit_status"] == "PASS"
    assert auth["n356_hostile_audit_review_id"] == EXPECTED_N356_REVIEW
    assert auth["n356_hostile_audit_exact_head"] == EXPECTED_N356_HEAD
    assert auth["n356_exact_head_ci_run"] == EXPECTED_N356_CI
    assert auth["n356_audit_credit_consumed"] is True
    assert auth["n356_candidate_status"] == "AUDITED_OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CUT_CONSUMED"

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == EXPECTED_N356_REMAIN
    assert frontier["n356_main_pruning_credit"] is True
    assert frontier["n356_status"] == "AUDITED_OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CUT_CONSUMED"
    assert frontier["n356_rejected_terminals"] == EXPECTED_N356_REJECT
    assert frontier["n356_audit_credit_consumed"] is True
    assert frontier["n357_status"] == "RESEARCH_CHECKPOINT_NO_MAIN_CREDIT"
    assert frontier["n357_main_pruning_credit"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "N357_ALL178_TRANSPORT_SUPPORT_CAPACITY_CENSUS_THEN_EXTERNAL_AUDIT"
    assert current["mainbatch_stop_gate"] == "NONE_UNTIL_N357_AUDITABLE_CANDIDATE_OR_TRUE_AUTHORITY_GATE"
    assert current["stop_semantics"] == "N357_OWNED_BY_STAGE32_01_178_MAINBATCH_MAIN_MUST_NOT_DUPLICATE"

    n356 = state["source_locks"]["n356"]
    assert n356["audit_review_id"] == EXPECTED_N356_REVIEW
    assert n356["audited_exact_head"] == EXPECTED_N356_HEAD
    assert n356["audit_receipt_blob_sha1"] == EXPECTED_RECEIPT_BLOB
    assert n356["audit_receipt_canonical_sha256"] == EXPECTED_RECEIPT_CANONICAL
    assert n356["management_blob_sha1"] == EXPECTED_MANAGEMENT_BLOB
    assert n356["management_canonical_sha256"] == EXPECTED_MANAGEMENT_CANONICAL
    assert n356["result_blob_sha1"] == EXPECTED_RESULT_BLOB
    assert n356["result_canonical_sha256"] == EXPECTED_RESULT_CANONICAL
    assert n356["dependency_lock_verifier_blob_sha1"] == EXPECTED_DEP_LOCK
    assert n356["serial_entrypoint_blob_sha1"] == EXPECTED_PUBLIC_SERIAL
    assert n356["parallel_entrypoint_blob_sha1"] == EXPECTED_PUBLIC_PARALLEL
    assert n356["fast_entrypoint_blob_sha1"] == EXPECTED_PUBLIC_FAST
    assert n356["serial_engine_blob_sha1"] == EXPECTED_ENGINE_SERIAL
    assert n356["parallel_engine_blob_sha1"] == EXPECTED_ENGINE_PARALLEL
    assert n356["fast_engine_blob_sha1"] == EXPECTED_ENGINE_FAST

    receipt_path = ROOT / n356["audit_receipt_path"]
    receipt = load_canonical(receipt_path, EXPECTED_RECEIPT_CANONICAL)
    assert_blob(receipt_path, EXPECTED_RECEIPT_BLOB)
    assert receipt["status"] == "PASS"
    assert receipt["review_id"] == EXPECTED_N356_REVIEW
    assert receipt["audited_exact_head"] == EXPECTED_N356_HEAD
    assert receipt["validation"]["exact_head_workflow_run"] == EXPECTED_N356_CI
    assert receipt["consumed_counts"]["incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert receipt["consumed_counts"]["remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert receipt["consumed_counts"]["remaining_terminals"] == EXPECTED_N356_REMAIN

    management_path = ROOT / n356["management_path"]
    management = load_canonical(management_path, EXPECTED_MANAGEMENT_CANONICAL)
    assert_blob(management_path, EXPECTED_MANAGEMENT_BLOB)
    assert management["authority"]["n356_authority_credit"] is True
    assert management["authority"]["authoritative_remaining_terminals"] == EXPECTED_N356_REMAIN
    assert management["claim_sync"]["full178_claim_authority_status"] == "DECLARED_GOAL"
    assert management["claim_sync"]["full178_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert management["route"]["owner"] == "stage32-01-178-mainbatch"
    assert management["firewalls"]["n357_main_pruning_credit"] is False

    result_path = ROOT / n356["result_path"]
    result = load_canonical(result_path, EXPECTED_RESULT_CANONICAL)
    assert_blob(result_path, EXPECTED_RESULT_BLOB)
    agg = result["aggregate"]
    assert agg["affected_strata"] == 4304
    assert agg["candidate_incremental_rejected_terminals"] == EXPECTED_N356_REJECT
    assert agg["candidate_remaining_strata"] == EXPECTED_REMAIN_STRATA
    assert agg["candidate_remaining_terminals"] == EXPECTED_N356_REMAIN
    assert agg["per_stratum_stream_sha256"] == EXPECTED_RESULT_STREAM

    for rel, blob in [
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_dependency_source_locks.py", EXPECTED_DEP_LOCK),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport.py", EXPECTED_PUBLIC_SERIAL),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport_parallel.py", EXPECTED_PUBLIC_PARALLEL),
        ("stages/stage32/32-01-178/nodes/N356/verify_n356_optimistic_exceptional_transport_fast.py", EXPECTED_PUBLIC_FAST),
        ("stages/stage32/32-01-178/nodes/N356-engine/verify_n356_optimistic_exceptional_transport.py", EXPECTED_ENGINE_SERIAL),
        ("stages/stage32/32-01-178/nodes/N356-engine/verify_n356_optimistic_exceptional_transport_parallel.py", EXPECTED_ENGINE_PARALLEL),
        ("stages/stage32/32-01-178/nodes/N356-engine/verify_n356_optimistic_exceptional_transport_fast.py", EXPECTED_ENGINE_FAST),
    ]:
        assert_blob(ROOT / rel, blob)

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False

    fw = state["firewalls"]
    for key in [
        "historical_q602_residues_treated_as_current_survivors",
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
        "Ordinary `stage32mainbatch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        assert fragment in startup

    print("PASS Stage32 MAIN startup authority N356_AUDITED_CONSUMED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print(f"authoritative_remaining={EXPECTED_REMAIN_STRATA}_strata/{EXPECTED_N356_REMAIN}_terminals")
    print(f"n356_reject={EXPECTED_N356_REJECT}")
    print("n357_main_credit=false full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=N357_ALL178_TRANSPORT_SUPPORT_CAPACITY_CENSUS_THEN_EXTERNAL_AUDIT")


if __name__ == "__main__":
    main()
