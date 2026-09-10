#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V6_N354_AUDITED_CONSUMED"
EXPECTED_CANONICAL = "e4ed93d73e9a139c91cca7dac627ad44f1f051dc3394fe35bccb3a4ad8cded6e"
EXPECTED_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
EXPECTED_N354_REVIEW = 5164850548
EXPECTED_N354_HEAD = "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6"
EXPECTED_N354_AUDIT_BLOB = "0394b088349780b6cddf7bcb9d207b3889679e1e"
EXPECTED_N354_AUDIT_CANONICAL = "e329916a74eea4471e00f109964afdaa871d4f8614237efed7f0f6e5d9b9c808"
EXPECTED_SYNC_BLOB = "04132f6bff0cac2f70d59a3fa195fb655585f987"
EXPECTED_SYNC_CANONICAL = "aeea2acf56b281a29e8a24bd749740eb20f415b998519b5a9961c28c9070971d"
EXPECTED_RESULT_BLOB = "6f6ed5646689940cc304a655711dba83333d3576"
EXPECTED_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
EXPECTED_CREDIT = "EXACT_POST_N353_FULL178_TWO_SIDED_SCALAR_HURWITZ_NECESSARY_CUT_ONLY_30575_STRATA_307492486826907032120701491_TERMINALS_NO_FULL178_COMPLETION_OR_THEOREM_CREDIT"


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
    assert target["full178_coarse_strata_count"] == 64111
    assert target["V6_is_current_attack_target"] is False
    assert target["O210_is_current_attack_target"] is False
    assert target["Q602_is_current_attack_target"] is False

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_MAIN
    assert auth["n354_hostile_audit_status"] == "PASS"
    assert auth["n354_hostile_audit_review_id"] == EXPECTED_N354_REVIEW
    assert auth["n354_hostile_audit_exact_head"] == EXPECTED_N354_HEAD
    assert auth["n354_audit_credit_consumed"] is True
    assert auth["n354_reaudit_required"] is False
    assert auth["n354_merge_ready_freshness"] == "BLOCKED_PENDING"

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["full178_goal_authority_status"] == "DECLARED_GOAL"
    assert frontier["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert frontier["n354_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n354_main_pruning_credit"] is True
    assert frontier["n354_rejected_strata"] == 30575
    assert frontier["n354_rejected_terminals"] == 307492486826907032120701491
    assert frontier["n354_remaining_strata"] == 17128
    assert frontier["n354_remaining_terminals"] == 38560956534397137634780102
    assert frontier["authoritative_remaining_strata"] == 17128
    assert frontier["authoritative_remaining_terminals"] == 38560956534397137634780102
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "POST_N354_SURVIVOR_FRONTIER_REMAP_AND_NEXT_EXACT_NECESSARY_CUT"
    assert current["mainbatch_stop_gate"] == "NO_AUDIT_GATE_ACTIVE_CONTINUE_POST_N354_RESEARCH"

    audit_path = ROOT / state["source_locks"]["n354_audit"]["path"]
    audit = load_canonical(audit_path, EXPECTED_N354_AUDIT_CANONICAL)
    assert git_blob_sha(audit_path) == EXPECTED_N354_AUDIT_BLOB
    assert audit["status"] == "PASS"
    assert audit["review_id"] == EXPECTED_N354_REVIEW
    assert audit["audited_exact_head"] == EXPECTED_N354_HEAD
    assert audit["credit_ceiling"] == EXPECTED_CREDIT
    assert audit["freshness"]["merge_ready_status"] == "BLOCKED_PENDING"
    assert audit["consumed_counts"]["remaining_strata"] == 17128
    assert audit["consumed_counts"]["remaining_terminals"] == 38560956534397137634780102

    sync_path = ROOT / state["source_locks"]["management_sync"]["path"]
    sync = load_canonical(sync_path, EXPECTED_SYNC_CANONICAL)
    assert git_blob_sha(sync_path) == EXPECTED_SYNC_BLOB
    assert sync["authority_transition"]["n354_hostile_audit_status"] == "PASS"
    assert sync["authority_transition"]["n354_hostile_audit_review_id"] == EXPECTED_N354_REVIEW
    assert sync["n354"]["status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert sync["n354"]["main_pruning_credit"] is True
    assert sync["consumed_credit"]["remaining_strata"] == 17128
    assert sync["consumed_credit"]["remaining_terminals"] == 38560956534397137634780102

    result_path = ROOT / state["source_locks"]["n354"]["result_path"]
    result = load_canonical(result_path, EXPECTED_RESULT_CANONICAL)
    assert git_blob_sha(result_path) == EXPECTED_RESULT_BLOB
    assert result["status"] == "AUDIT_CANDIDATE_DIAGNOSTIC_NO_MAIN_CREDIT"
    assert result["aggregate"]["n354_candidate_remaining_strata"] == 17128
    assert result["aggregate"]["n354_candidate_remaining_terminals"] == 38560956534397137634780102

    prov = state["historical_formal_provenance"]
    assert prov["formal_q602_residues"] == [73, 97, 235]
    assert prov["formal_q602_residues_are_current_survivors"] is False

    fw = state["firewalls"]
    for key in [
        "historical_q602_residues_treated_as_current_survivors",
        "n353_credit_exceeds_external_audit",
        "n354_self_promoted_to_audited",
        "n354_credit_exceeds_external_audit",
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

    print("PASS Stage32 MAIN startup authority N354_AUDITED_CONSUMED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("authoritative_remaining=17128_strata/38560956534397137634780102_terminals")
    print("full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=post_N354_survivor_frontier")


if __name__ == "__main__":
    main()
