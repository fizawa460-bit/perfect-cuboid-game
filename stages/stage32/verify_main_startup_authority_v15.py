#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"
RECEIPT = HERE / "management/post-cut195-current-v14-composition-consumption-20260912.json"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED"
EXPECTED_STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
EXPECTED_STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
EXPECTED_REPOSITORY_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"
RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"
CUT195_CONSUMPTION_VERIFIER_BLOB = "fde757c2efbf0a0902a742bd72737d5b0d84e9f8"

AUDITED_V14_HEAD = "da1cdd5391ff7f298979ffacbb37e6f3823ba93f"
AUDITED_V14_REVIEW = 5185805886
AUDITED_CUT195_HEAD = "2618f4dcd546d569b212753ac7abc10e07ee5828"
AUDITED_CUT195_REVIEW = 5184909672
PRE = 47598978285064933783643
CUT195 = 26216
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

    verifier = HERE / "verify_cut195_main_consumption_v15.py"
    assert git_blob(verifier) == CUT195_CONSUMPTION_VERIFIER_BLOB

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_REPOSITORY_MAIN
    assert auth["n357_post_sync_reaudit_required"] is True
    assert auth["n357_post_sync_reaudit_status"] == "PASS"
    assert auth["n357_post_sync_reaudit_review_id"] == AUDITED_V14_REVIEW
    assert auth["n357_post_sync_reaudit_exact_head"] == AUDITED_V14_HEAD
    assert auth["n357_synchronized_head_hostile_audited"] is True
    assert auth["cut195_candidate_hostile_audit_status"] == "PASS"
    assert auth["cut195_candidate_hostile_audit_review_id"] == AUDITED_CUT195_REVIEW
    assert auth["cut195_candidate_audited_exact_head"] == AUDITED_CUT195_HEAD
    assert auth["cut195_current_v14_composition_replayed"] is True
    assert auth["cut195_current_v14_overlap_n357_terminals"] == 0
    assert auth["cut195_main_consumption_incremental_rejected_terminals"] == CUT195
    assert auth["cut195_main_consumption_remaining_strata"] == STRATA
    assert auth["cut195_main_consumption_remaining_terminals"] == POST
    assert auth["cut195_main_pruning_credit_consumed"] is True
    assert auth["cut195_post_sync_reaudit_required"] is True
    assert auth["cut195_post_sync_reaudit_status"] == "PENDING"

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == STRATA
    assert frontier["authoritative_remaining_terminals"] == POST
    assert frontier["n357_main_pruning_credit"] is True
    assert frontier["n357_synchronized_head_hostile_audited"] is True
    assert frontier["cut191_main_pruning_credit"] is True
    assert frontier["cut194_main_pruning_credit"] is True
    assert frontier["cut195_main_pruning_credit"] is True
    assert frontier["cut195_incremental_rejected_terminals"] == CUT195
    assert frontier["cut195_current_v14_overlap_n357_terminals"] == 0
    assert frontier["cut195_synchronized_head_hostile_audited"] is False
    assert frontier["cut193_main_pruning_credit"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False
    assert PRE - CUT195 == POST

    current = state["current"]
    assert current["mainbatch_stop_gate"] == "POST_CUT195_MAIN_CONSUMPTION_REPLACEMENT_HEAD_HOSTILE_REAUDIT"
    assert current["next_exact_route"] == "CUT195_MAIN_CONSUMPTION_REPLACEMENT_HEAD_HOSTILE_REAUDIT_THEN_FULL178_FRONTIER_SELECTION"

    sl = state["source_locks"]["cut195_main_consumption"]
    assert sl["receipt_blob_sha1"] == RECEIPT_BLOB
    assert sl["receipt_canonical_sha256"] == RECEIPT_CANONICAL
    assert sl["current_v14_exact_head"] == AUDITED_V14_HEAD
    assert sl["current_v14_hostile_reaudit_review_id"] == AUDITED_V14_REVIEW
    assert sl["audited_candidate_exact_head"] == AUDITED_CUT195_HEAD
    assert sl["audited_candidate_review_id"] == AUDITED_CUT195_REVIEW
    assert sl["incremental_rejected_terminals"] == CUT195
    assert sl["before_remaining_terminals"] == PRE
    assert sl["after_remaining_terminals"] == POST
    assert sl["main_pruning_credit"] is True
    assert sl["replacement_head_hostile_reaudit_required"] is True

    rr = receipt["current_v14_composition_replay"]
    assert rr["cut195_target_equals_current_prefix_offsets_511_765"] is True
    assert rr["n357_rejecting_cut195_target_blocks"] == 0
    assert rr["n357_rejecting_cut195_target_terminals"] == 0
    assert rr["double_charge"] is False
    assert receipt["claim_sync"]["claim_core_changed"] is False
    assert receipt["claim_sync"]["authority_status_changed"] is False
    assert receipt["claim_sync"]["frontier_status"] == "ACTIVE_INCOMPLETE"

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

    workflow = (ROOT / ".github/workflows/stage32-main-startup-authority.yml").read_text(encoding="utf-8")
    assert AUDITED_V14_HEAD in workflow
    assert AUDITED_CUT195_HEAD in workflow
    assert "verify_cut195_main_consumption_v15.py" in workflow
    assert "verify_main_startup_authority_v15.py" in workflow

    startup = START.read_text(encoding="utf-8")
    assert "Do not merge without explicit user authorization." in startup

    print("PASS Stage32 MAIN V15 CUT195 audited consumption boundary")
    print(f"authority={STRATA}/{POST}")
    print(f"cut195_incremental_rejected={CUT195}")
    print("cut193_main_credit=false full178_complete=false stage32_closed=false merge_authorized=false")
    print("replacement_head_hostile_reaudit=PENDING")

if __name__ == "__main__":
    main()
