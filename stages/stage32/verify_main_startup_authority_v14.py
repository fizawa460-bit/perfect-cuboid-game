#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V14_N357_AUDITED_CONSUMED"
EXPECTED_STATE_BLOB = "7f4cdb067959b3ed561013ec195bd3b6f4993baf"
EXPECTED_STATE_CANONICAL = "81e430b60e184488f3cf07ad7b5b11c083aa4af909a3b87073d03ea95937ce41"
EXPECTED_REPOSITORY_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"

PRE_N357 = 65396964990500233609659
N357_REJECT = 17797986705435299826016
POST_N357 = 47598978285064933783643
REMAIN_STRATA = 17128

N357_CANDIDATE_REVIEW = 5183069892
N357_CANDIDATE_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"
N357_RESULT_BLOB = "50014d453266ad79101910a943d14388bd3ef6ec"
N357_RESULT_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
N357_ENGINE_BLOB = "479c783cb42d0952cc310708106787147b499240"

COMPOSITION_AUDIT_REVIEW = 5184369560
COMPOSITION_AUDITED_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
COMPOSITION_CI = 34659920867
PRE_V14_STATE_BLOB = "0f281111572572a8068cc38bb77f5f1c869b98ad"
PRE_V14_STATE_CANONICAL = "7c39d7935c36066cf2ec4a549eadc45e821fbf818490e6bfd10126f32bdf8a6d"
COMPOSITION_RECEIPT_BLOB = "5abac38ee21713fd978ae59e85a0e705c2eb7b6c"
COMPOSITION_RECEIPT_CANONICAL = "3a9d29b97ccc663a92cc4c0463d1e77c00a518450b65d8d9ece0054734eeebd8"
INNER_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
FAIL_CLOSED_COMPOSITION_VERIFIER_BLOB = "8c3bb80e6fe1c552171d3c1a4eb63cd2bb6e482a"
V13_STARTUP_VERIFIER_BLOB = "9a083e2f2e165edc26dd025558b8a459739968b4"

CONSUMPTION_RECEIPT = HERE / "management/post-n357-composition-pass-consumption-20260912.json"
CONSUMPTION_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
CONSUMPTION_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
V13_SNAPSHOT = HERE / "management/MAIN-STATE-V13-N357-PRECONSUMPTION.json"

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

    assert git_blob(V13_SNAPSHOT) == PRE_V14_STATE_BLOB
    old = load(V13_SNAPSHOT)
    assert old["canonical_sha256_without_this_field"] == PRE_V14_STATE_CANONICAL
    assert canonical(old) == PRE_V14_STATE_CANONICAL

    assert git_blob(CONSUMPTION_RECEIPT) == CONSUMPTION_RECEIPT_BLOB
    receipt = load(CONSUMPTION_RECEIPT)
    assert receipt["canonical_sha256_without_this_field"] == CONSUMPTION_RECEIPT_CANONICAL
    assert canonical(receipt) == CONSUMPTION_RECEIPT_CANONICAL

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_REPOSITORY_MAIN
    assert auth["n357_candidate_hostile_audit_status"] == "PASS"
    assert auth["n357_candidate_hostile_audit_review_id"] == N357_CANDIDATE_REVIEW
    assert auth["n357_candidate_hostile_audit_exact_head"] == N357_CANDIDATE_HEAD
    assert auth["n357_candidate_result_blob_sha1"] == N357_RESULT_BLOB
    assert auth["n357_candidate_result_canonical_sha256"] == N357_RESULT_CANONICAL
    assert auth["n357_current_v13_composition_replayed"] is True
    assert auth["n357_current_v13_overlap_cut191_terminals"] == 0
    assert auth["n357_current_v13_overlap_cut194_terminals"] == 0
    assert auth["n357_current_v13_composition_hostile_audit_status"] == "PASS"
    assert auth["n357_current_v13_composition_hostile_audit_review_id"] == COMPOSITION_AUDIT_REVIEW
    assert auth["n357_current_v13_composition_audited_exact_head"] == COMPOSITION_AUDITED_HEAD
    assert auth["n357_current_v13_composition_exact_head_ci_run"] == COMPOSITION_CI
    assert auth["n357_main_pruning_credit_consumed"] is True
    assert auth["n357_main_consumption_incremental_rejected_terminals"] == N357_REJECT
    assert auth["n357_main_consumption_remaining_strata"] == REMAIN_STRATA
    assert auth["n357_main_consumption_remaining_terminals"] == POST_N357
    assert auth["n357_post_sync_reaudit_required"] is True
    assert auth["n357_post_sync_reaudit_status"] == "PENDING"
    assert auth["n357_synchronized_head_hostile_audited"] is False

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == POST_N357
    assert frontier["n357_current_v13_composition_hostile_audited"] is True
    assert frontier["n357_current_v13_composition_audit_review_id"] == COMPOSITION_AUDIT_REVIEW
    assert frontier["n357_main_pruning_credit"] is True
    assert frontier["n357_incremental_rejected_terminals"] == N357_REJECT
    assert frontier["n357_remaining_terminals"] == POST_N357
    assert frontier["n357_post_sync_reaudit_required"] is True
    assert frontier["n357_synchronized_head_hostile_audited"] is False
    assert frontier["cut193_main_pruning_credit"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False
    assert PRE_N357 - N357_REJECT == POST_N357

    ra = receipt["authority"]
    assert ra["before_remaining_strata"] == REMAIN_STRATA
    assert ra["before_remaining_terminals"] == PRE_N357
    assert ra["incremental_rejected_terminals"] == N357_REJECT
    assert ra["after_remaining_strata"] == REMAIN_STRATA
    assert ra["after_remaining_terminals"] == POST_N357
    assert ra["n357_main_pruning_credit"] is True
    assert ra["cut193_main_pruning_credit"] is False

    ca = receipt["current_v13_composition_audit"]
    assert ca["hostile_audit_status"] == "PASS"
    assert ca["hostile_audit_review_id"] == COMPOSITION_AUDIT_REVIEW
    assert ca["audited_exact_head"] == COMPOSITION_AUDITED_HEAD
    assert ca["exact_head_main_startup_ci_run"] == COMPOSITION_CI
    assert ca["composition_receipt_blob_sha1"] == COMPOSITION_RECEIPT_BLOB
    assert ca["composition_receipt_canonical_sha256"] == COMPOSITION_RECEIPT_CANONICAL
    assert ca["composition_verifier_blob_sha1"] == INNER_COMPOSITION_VERIFIER_BLOB
    assert ca["fail_closed_verifier_blob_sha1"] == FAIL_CLOSED_COMPOSITION_VERIFIER_BLOB

    xa = receipt["overlap_and_cross_lane_replay"]
    assert xa["cut191_overlap_terminals"] == 0
    assert xa["cut194_overlap_terminals"] == 0
    assert xa["double_charge"] is False
    assert xa["g1_d008_e8_current_prefix_survivor_block_count"] == 7596
    assert xa["g1_d008_e8_current_prefix_survivor_block_stream_sha256"] == "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
    assert xa["n357_rejecting_current_prefix_blocks"] == 0
    assert xa["n357_rejecting_cut192_preferred_wave_blocks"] == 0
    assert xa["n357_rejecting_cut192_preferred_wave_terminals"] == 0
    assert xa["cut192_preferred_wave_survivor_offset_range"] == [1, 255]
    assert xa["cut192_satisfied_handoff_remains_current_main_surviving"] is True

    sl = state["source_locks"]["n357_main_consumption"]
    assert sl["receipt_blob_sha1"] == CONSUMPTION_RECEIPT_BLOB
    assert sl["receipt_canonical_sha256"] == CONSUMPTION_RECEIPT_CANONICAL
    assert sl["prior_main_state_exact_head"] == COMPOSITION_AUDITED_HEAD
    assert sl["prior_main_state_blob_sha1"] == PRE_V14_STATE_BLOB
    assert sl["prior_main_state_canonical_sha256"] == PRE_V14_STATE_CANONICAL
    assert sl["composition_hostile_audit_review_id"] == COMPOSITION_AUDIT_REVIEW
    assert sl["composition_exact_head_ci_run"] == COMPOSITION_CI
    assert sl["incremental_rejected_terminals"] == N357_REJECT
    assert sl["before_remaining_terminals"] == PRE_N357
    assert sl["after_remaining_terminals"] == POST_N357
    assert sl["main_pruning_credit"] is True
    assert sl["replacement_head_hostile_reaudit_required"] is True

    nlock = state["source_locks"]["n357_current_v13_composition"]
    assert nlock["audited_candidate_engine_blob_sha1"] == N357_ENGINE_BLOB
    assert nlock["composition_receipt_blob_sha1"] == COMPOSITION_RECEIPT_BLOB
    assert nlock["composition_receipt_canonical_sha256"] == COMPOSITION_RECEIPT_CANONICAL
    assert nlock["composition_verifier_blob_sha1"] == INNER_COMPOSITION_VERIFIER_BLOB
    assert nlock["fail_closed_verifier_blob_sha1"] == FAIL_CLOSED_COMPOSITION_VERIFIER_BLOB
    assert nlock["composition_hostile_audit_review_id"] == COMPOSITION_AUDIT_REVIEW
    assert nlock["main_pruning_credit"] is False

    current = state["current"]
    assert current["mainbatch_stop_gate"] == "POST_N357_MAIN_CONSUMPTION_REPLACEMENT_HEAD_HOSTILE_REAUDIT"
    assert current["next_exact_route"] == "N357_MAIN_CONSUMPTION_REPLACEMENT_HEAD_HOSTILE_REAUDIT_THEN_FULL178_FRONTIER_SELECTION"

    fw = state["firewalls"]
    for key in (
        "n357_main_credit_without_current_authority_composition_audit",
        "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit",
        "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ):
        assert fw[key] is False, key

    cfw = receipt["credit_firewall"]
    assert cfw["numerical_pruning_credit_only"] is True
    for key in ("full178_complete", "receiver_credit", "theorem_credit",
                "effectivity_credit", "endpoint_credit", "stage32_closed",
                "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "merge_authorized"):
        assert cfw[key] is False, key

    for rel in state["current_leaf_working_set"]:
        assert (ROOT / rel).is_file(), rel

    workflow = (ROOT / ".github/workflows/stage32-main-startup-authority.yml").read_text(encoding="utf-8")
    assert COMPOSITION_AUDITED_HEAD in workflow
    assert "Checkout exact hostile-audited N357 composition boundary" in workflow
    assert "verify_n357_main_consumption_v14.py" in workflow

    startup = START.read_text(encoding="utf-8")
    assert "Do not merge without explicit user authorization." in startup

    print("PASS Stage32 MAIN V14 N357 audited consumption boundary")
    print(f"authority={REMAIN_STRATA}/{POST_N357}")
    print(f"n357_incremental_rejected={N357_REJECT}")
    print("cut193_main_credit=false full178_complete=false stage32_closed=false merge_authorized=false")
    print("replacement_head_hostile_reaudit=PENDING")

if __name__ == "__main__":
    main()
