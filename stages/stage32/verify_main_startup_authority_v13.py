#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V13_CUT194_AUDITED_CONSUMED"
EXPECTED_STATE_BLOB = "16d23a965d42a38f6a22d1cbb6545ef294b8ba16"
EXPECTED_STATE_CANONICAL = "a5d4889843bf4ad66c945823812a2f3f2edd5729a709124c97c7f7f4156a140e"
EXPECTED_REPOSITORY_MAIN = "c31684fb5f63d8a025eb298c91861d4c979b0e28"

PRE_CUT194_REMAIN = 65396964990500233636101
CUT194_REJECT = 26442
POST_CUT194_REMAIN = 65396964990500233609659
REMAIN_STRATA = 17128

MAIN_PRE_CUT194_REVIEW = 5184015342
MAIN_PRE_CUT194_HEAD = "eb43085946a019323879b708aeb5246f88640c01"
MAIN_PRE_CUT194_STARTUP_CI = 34644848505
CUT194_REVIEW = 5183299107
CUT194_HEAD = "847f3bff0c5e0d0530bfb8db406e955b2d231d9a"
CUT194_CI = 34643840690
CUT194_HEAVY = 34614132290

EXPECTED = {
    "result": (
        "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-result.json",
        "dab1a28f55918b617112799f11ac9614eb8a481c",
        "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4",
    ),
    "handoff": (
        "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-audit-handoff.json",
        "7585f93df035b928ebfbad733ccf501125d57e08",
        "273ceb4cf9fba64023f9dcb5f0ab11342f4e6f1d71b5dd8574e75e886c3be4f9",
    ),
    "management": (
        "stages/stage32/management/post-cut194-hostile-pass-consumption-20260912.json",
        "775c7853de989ee92167269bf3be774bd1e984f3",
        "6e9711716358ff955fe3aac1fda9661a800f3f1e3d10286fa5127a4638efb568",
    ),
}


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json(rel: str) -> dict:
    obj = json.loads((ROOT / rel).read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise AssertionError(rel)
    return obj


def assert_locked(rel: str, blob: str, canon: str) -> dict:
    path = ROOT / rel
    assert path.is_file(), rel
    assert git_blob_sha(path) == blob, rel
    obj = load_json(rel)
    assert obj.get("canonical_sha256_without_this_field") == canon, rel
    assert canonical(obj) == canon, rel
    return obj


def main() -> None:
    assert git_blob_sha(STATE) == EXPECTED_STATE_BLOB
    state = json.loads(STATE.read_text(encoding="utf-8"))
    assert state["schema"] == EXPECTED_SCHEMA
    assert state["role"] == "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE"
    assert state["canonical_sha256_without_this_field"] == EXPECTED_STATE_CANONICAL
    assert canonical(state) == EXPECTED_STATE_CANONICAL

    result = assert_locked(*EXPECTED["result"])
    handoff = assert_locked(*EXPECTED["handoff"])
    mgmt = assert_locked(*EXPECTED["management"])

    auth = state["authority_sync"]
    assert auth["current_repository_main"] == EXPECTED_REPOSITORY_MAIN
    assert auth["main_pre_cut194_hostile_reaudit_status"] == "PASS"
    assert auth["main_pre_cut194_hostile_reaudit_review_id"] == MAIN_PRE_CUT194_REVIEW
    assert auth["main_pre_cut194_audited_exact_head"] == MAIN_PRE_CUT194_HEAD
    assert auth["main_pre_cut194_startup_ci_run"] == MAIN_PRE_CUT194_STARTUP_CI
    assert auth["cut194_external_hostile_audit_status"] == "PASS"
    assert auth["cut194_external_hostile_audit_review_id"] == CUT194_REVIEW
    assert auth["cut194_external_hostile_audit_exact_head"] == CUT194_HEAD
    assert auth["cut194_external_exact_head_ci_run"] == CUT194_CI
    assert auth["cut194_heavy_run"] == CUT194_HEAVY
    assert auth["cut194_main_pruning_credit_consumed"] is True
    assert auth["cut194_incremental_rejected_terminals"] == CUT194_REJECT
    assert auth["cut194_remaining_strata"] == REMAIN_STRATA
    assert auth["cut194_remaining_terminals"] == POST_CUT194_REMAIN
    assert auth["cut194_post_sync_reaudit_required"] is True
    assert auth["cut194_post_sync_reaudit_status"] == "PENDING"
    assert auth["cut194_synchronized_head_hostile_audited"] is False

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == POST_CUT194_REMAIN
    assert frontier["cut194_main_pruning_credit"] is True
    assert frontier["cut194_incremental_rejected_terminals"] == CUT194_REJECT
    assert frontier["cut194_remaining_terminals"] == POST_CUT194_REMAIN
    assert frontier["cut193_main_pruning_credit"] is False
    assert frontier["n357_main_pruning_credit"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False
    assert PRE_CUT194_REMAIN - CUT194_REJECT == POST_CUT194_REMAIN

    assert result["node"] == "CUT194"
    assert result["target"]["row_id"] == "g1-d008"
    assert result["target"]["d"] == 8 and result["target"]["e"] == 8
    assert result["target"]["survivor_offset_range"] == [256, 510]
    assert result["target"]["block_count"] == 255
    assert result["target"]["terminal_count"] == 28815
    assert result["target"]["cut191_block0_disjoint"] is True
    assert result["target"]["cut193_wave1_disjoint"] is True
    assert result["target"]["n356_preserved_all_wave_blocks"] is True
    assert result["result"]["candidate_closed_block_count"] == 234
    assert result["result"]["candidate_pruned_terminals"] == CUT194_REJECT
    assert result["result"]["remaining_nonclosed_block_count"] == 21
    assert result["result"]["candidate_post_wave2_from_main_v12_terminals"] == POST_CUT194_REMAIN
    assert result["credit"]["stage32_main_pruning_credit"] is False
    assert result["credit"]["cut194_pruning_credit"] is False

    assert handoff["result"]["candidate_closed_block_count"] == 234
    assert handoff["result"]["candidate_pruned_terminals"] == CUT194_REJECT
    assert handoff["audit"]["hostile_audit_passed"] is False
    assert handoff["credit"]["stage32_main_pruning_credit"] is False

    assert mgmt["status"] == "RETAINED_AUTHORITY_TRANSITION_PENDING_REPLACEMENT_HEAD_HOSTILE_AUDIT"
    assert mgmt["upstream_authority"]["main_parent_exact_head"] == MAIN_PRE_CUT194_HEAD
    assert mgmt["upstream_authority"]["main_parent_hostile_reaudit_review_id"] == MAIN_PRE_CUT194_REVIEW
    assert mgmt["authority"]["cut194_main_pruning_credit"] is True
    assert mgmt["authority"]["cut194_incremental_rejected_terminals"] == CUT194_REJECT
    assert mgmt["authority"]["authoritative_remaining_terminals"] == POST_CUT194_REMAIN
    assert mgmt["overlap_replay"]["n356_overlap_zero"] is True
    assert mgmt["overlap_replay"]["cut191_overlap_zero"] is True
    assert mgmt["overlap_replay"]["cut193_overlap_zero"] is True
    assert mgmt["overlap_replay"]["cut193_main_credit_remains_false"] is True
    assert mgmt["overlap_replay"]["unknown_checks_promoted"] is False
    assert mgmt["overlap_replay"]["double_charge"] is False
    assert mgmt["claim_sync"]["claim_core_changed"] is False
    assert mgmt["claim_sync"]["authority_status"] == "DECLARED_GOAL"
    assert mgmt["claim_sync"]["frontier_status"] == "ACTIVE_INCOMPLETE"

    lock = state["source_locks"]["cut194"]
    for key, expected in [
        ("result_blob_sha1", EXPECTED["result"][1]),
        ("result_canonical_sha256", EXPECTED["result"][2]),
        ("audit_handoff_blob_sha1", EXPECTED["handoff"][1]),
        ("audit_handoff_canonical_sha256", EXPECTED["handoff"][2]),
        ("management_blob_sha1", EXPECTED["management"][1]),
        ("management_canonical_sha256", EXPECTED["management"][2]),
    ]:
        assert lock[key] == expected, key
    assert lock["external_audit_review_id"] == CUT194_REVIEW
    assert lock["external_audited_exact_head"] == CUT194_HEAD
    assert lock["external_exact_head_ci_run"] == CUT194_CI
    assert lock["heavy_run"] == CUT194_HEAVY

    current = state["current"]
    assert current["mainbatch_stop_gate"] == "POST_CUT194_REPLACEMENT_HEAD_HOSTILE_REAUDIT"
    assert current["next_exact_route"] == "N357_ALL178_TRANSPORT_SUPPORT_CAPACITY_CENSUS_THEN_EXTERNAL_AUDIT"

    fw = state["firewalls"]
    for key in [
        "cut194_self_promoted_to_audited",
        "cut194_credit_exceeds_external_audit",
        "cut193_promoted_via_cut194",
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

    startup = START.read_text(encoding="utf-8")
    assert "Do not merge without explicit user authorization." in startup

    print("PASS Stage32 MAIN startup authority V13 CUT194_AUDITED_CONSUMED")
    print(f"authoritative_remaining={REMAIN_STRATA}_strata/{POST_CUT194_REMAIN}_terminals")
    print("cut194_incremental_reject=26442 cut193_main_credit=false")
    print("replacement_head_reaudit_required=true synchronized_head_hostile_audited=false")
    print("full178_complete=false n357_main_credit=false merge_authorized=false")


if __name__ == "__main__":
    main()
