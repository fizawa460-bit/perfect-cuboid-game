#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V7_N355_AUDIT_REQUIRED"
EXPECTED_CANONICAL = "16c1cf5ad6164a7b33e32f99220cf6c37890a0ba5388639849985511fb21016a"
EXPECTED_MAIN = "5ca6acba4b591d9e2d40057241c850598c1fa1df"
EXPECTED_N354_REVIEW = 5164850548
EXPECTED_N354_HEAD = "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6"
EXPECTED_N354_AUDIT_BLOB = "0394b088349780b6cddf7bcb9d207b3889679e1e"
EXPECTED_N354_AUDIT_CANONICAL = "e329916a74eea4471e00f109964afdaa871d4f8614237efed7f0f6e5d9b9c808"
EXPECTED_N354_SYNC_BLOB = "04132f6bff0cac2f70d59a3fa195fb655585f987"
EXPECTED_N354_SYNC_CANONICAL = "aeea2acf56b281a29e8a24bd749740eb20f415b998519b5a9961c28c9070971d"
EXPECTED_N354_RESULT_BLOB = "6f6ed5646689940cc304a655711dba83333d3576"
EXPECTED_N354_RESULT_CANONICAL = "9f9976bfcf6142e44042ef393b0c5668f4d84a743dfd243ef086eb1a79cee1c4"
EXPECTED_N354_CREDIT = "EXACT_POST_N353_FULL178_TWO_SIDED_SCALAR_HURWITZ_NECESSARY_CUT_ONLY_30575_STRATA_307492486826907032120701491_TERMINALS_NO_FULL178_COMPLETION_OR_THEOREM_CREDIT"

EXPECTED_N355_RESULT_BLOB = "22141aa67a001bf0ccccc8504963ebe492c49669"
EXPECTED_N355_RESULT_CANONICAL = "241c0009f260a4136bc5abaa85caa08bfce9fea4f97c1744391e9331a21ad986"
EXPECTED_N355_SYNC_BLOB = "11066013ab5e06dce677c43eb000ea418769a06d"
EXPECTED_N355_SYNC_CANONICAL = "fe1427b8d5eaa6cc3087417d0bddbac9c47431a88f60e9fcea4d65f06147958c"
EXPECTED_N355_REJECT = 8211103970847375998477971
EXPECTED_N355_CANDIDATE_REMAIN = 30349852563549761636302131


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
    assert auth["n355_hostile_audit_status"] == "PENDING"
    assert auth["n355_hostile_audit_review_id"] is None
    assert auth["n355_audit_credit_consumed"] is False
    assert auth["n355_candidate_exact_subset_rejected_terminals"] == EXPECTED_N355_REJECT

    frontier = state["current_exact_frontier"]
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["full178_goal_authority_status"] == "DECLARED_GOAL"
    assert frontier["full178_goal_frontier_status"] == "ACTIVE_INCOMPLETE"
    assert frontier["n354_status"] == "AUDITED_NECESSARY_CUT_CONSUMED"
    assert frontier["n354_main_pruning_credit"] is True
    assert frontier["n354_remaining_strata"] == 17128
    assert frontier["n354_remaining_terminals"] == 38560956534397137634780102
    # N355 is audit-candidate only: authoritative frontier MUST remain N354.
    assert frontier["n355_status"] == "AUDIT_REQUIRED_EXACT_SUBSET_CENSUS"
    assert frontier["n355_main_pruning_credit"] is False
    assert frontier["n355_candidate_rejected_terminals"] == EXPECTED_N355_REJECT
    assert frontier["n355_candidate_remaining_strata"] == 17128
    assert frontier["n355_candidate_remaining_terminals"] == EXPECTED_N355_CANDIDATE_REMAIN
    assert frontier["authoritative_remaining_strata"] == 17128
    assert frontier["authoritative_remaining_terminals"] == 38560956534397137634780102
    assert frontier["n350_registered_producer_count"] == 0
    assert frontier["stage32_closed"] is False

    current = state["current"]
    assert current["next_exact_route"] == "N355_EXTERNAL_HOSTILE_AUDIT_EXACT_X1_DIAGONAL_SUBSET"
    assert current["mainbatch_stop_gate"] == "STOP_BEFORE_N355_AUTHORITY_DECREMENT_AND_REQUEST_EXTERNAL_STAGE32_01_178_AUDIT"
    assert current["stacked_candidate_audit_status"] == "N355_PENDING"

    # Preserve the hostile-audited N354 authority lock.
    audit_path = ROOT / state["source_locks"]["n354_audit"]["path"]
    audit = load_canonical(audit_path, EXPECTED_N354_AUDIT_CANONICAL)
    assert git_blob_sha(audit_path) == EXPECTED_N354_AUDIT_BLOB
    assert audit["status"] == "PASS"
    assert audit["review_id"] == EXPECTED_N354_REVIEW
    assert audit["audited_exact_head"] == EXPECTED_N354_HEAD
    assert audit["credit_ceiling"] == EXPECTED_N354_CREDIT
    assert audit["consumed_counts"]["remaining_strata"] == 17128
    assert audit["consumed_counts"]["remaining_terminals"] == 38560956534397137634780102

    n354_sync_path = ROOT / state["source_locks"]["management_sync"]["path"]
    n354_sync = load_canonical(n354_sync_path, EXPECTED_N354_SYNC_CANONICAL)
    assert git_blob_sha(n354_sync_path) == EXPECTED_N354_SYNC_BLOB
    assert n354_sync["n354"]["status"] == "AUDITED_NECESSARY_CUT_CONSUMED"

    n354_result_path = ROOT / state["source_locks"]["n354"]["result_path"]
    n354_result = load_canonical(n354_result_path, EXPECTED_N354_RESULT_CANONICAL)
    assert git_blob_sha(n354_result_path) == EXPECTED_N354_RESULT_BLOB
    assert n354_result["aggregate"]["n354_candidate_remaining_strata"] == 17128
    assert n354_result["aggregate"]["n354_candidate_remaining_terminals"] == 38560956534397137634780102

    # N355 candidate locks. These prove reproducibility, not audit credit.
    n355_lock = state["source_locks"]["n355"]
    n355_result_path = ROOT / n355_lock["result_path"]
    n355_result = load_canonical(n355_result_path, EXPECTED_N355_RESULT_CANONICAL)
    assert git_blob_sha(n355_result_path) == EXPECTED_N355_RESULT_BLOB
    assert n355_result["status"] == "AUDIT_CANDIDATE_EXACT_SUBSET_CENSUS_NO_AUTHORITY_DECREMENT"
    assert n355_result["exact_census"]["candidate_rejected_terminals"] == EXPECTED_N355_REJECT
    assert n355_result["exact_census"]["candidate_remaining_strata"] == 17128
    assert n355_result["exact_census"]["candidate_remaining_terminals"] == EXPECTED_N355_CANDIDATE_REMAIN
    assert n355_result["semantics"]["main_pruning_credit"] is False
    assert n355_result["semantics"]["hostile_audit_required"] is True

    n355_sync_path = ROOT / n355_lock["management_path"]
    n355_sync = load_canonical(n355_sync_path, EXPECTED_N355_SYNC_CANONICAL)
    assert git_blob_sha(n355_sync_path) == EXPECTED_N355_SYNC_BLOB
    assert n355_sync["n355"]["status"] == "AUDIT_REQUIRED"
    assert n355_sync["n355"]["candidate_rejected_terminals"] == EXPECTED_N355_REJECT
    assert n355_sync["authority"]["n355_authority_credit"] is False
    assert n355_sync["authority"]["authoritative_remaining_terminals"] == 38560956534397137634780102

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

    print("PASS Stage32 MAIN startup authority N355_AUDIT_REQUIRED")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("authoritative_remaining=17128_strata/38560956534397137634780102_terminals")
    print(f"n355_candidate_reject={EXPECTED_N355_REJECT}")
    print(f"n355_candidate_remaining=17128_strata/{EXPECTED_N355_CANDIDATE_REMAIN}_terminals")
    print("n355_main_credit=false full178_complete=false heavy_compute_authorized=false merge_authorized=false")
    print("next_route=N355_external_hostile_audit")


if __name__ == "__main__":
    main()
