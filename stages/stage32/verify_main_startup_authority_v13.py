#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V13_CUT194_AUDITED_CONSUMED"
EXPECTED_STATE_BLOB = "0f281111572572a8068cc38bb77f5f1c869b98ad"
EXPECTED_STATE_CANONICAL = "7c39d7935c36066cf2ec4a549eadc45e821fbf818490e6bfd10126f32bdf8a6d"
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

N357_REVIEW = 5183069892
N357_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"
N357_RESULT_BLOB = "50014d453266ad79101910a943d14388bd3ef6ec"
N357_RESULT_CANONICAL = "0718c1f8f92a6d18e99e82b4adcbe1efe66a0daa47347284cbc6f42e6f0dac53"
N357_ENGINE_BLOB = "479c783cb42d0952cc310708106787147b499240"
N357_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
N357_FAIL_CLOSED_VERIFIER_BLOB = "8c3bb80e6fe1c552171d3c1a4eb63cd2bb6e482a"
N357_REJECT = 17797986705435299826016
POST_N357_IF_CONSUMED = 47598978285064933783643

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
    "n357_composition": (
        "stages/stage32/management/N357-V13-CURRENT-AUTHORITY-COMPOSITION.json",
        "5abac38ee21713fd978ae59e85a0e705c2eb7b6c",
        "3a9d29b97ccc663a92cc4c0463d1e77c00a518450b65d8d9ece0054734eeebd8",
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
    n357 = assert_locked(*EXPECTED["n357_composition"])

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

    # N357 is already hostile-audited as a candidate. The current step is only
    # composition against the newer V13 authority; it must not self-promote.
    assert auth["n357_candidate_hostile_audit_status"] == "PASS"
    assert auth["n357_candidate_hostile_audit_review_id"] == N357_REVIEW
    assert auth["n357_candidate_hostile_audit_exact_head"] == N357_HEAD
    assert auth["n357_candidate_result_blob_sha1"] == N357_RESULT_BLOB
    assert auth["n357_candidate_result_canonical_sha256"] == N357_RESULT_CANONICAL
    assert auth["n357_candidate_original_incremental_rejected_terminals"] == N357_REJECT
    assert auth["n357_current_v13_composition_replayed"] is True
    assert auth["n357_current_v13_overlap_cut191_terminals"] == 0
    assert auth["n357_current_v13_overlap_cut194_terminals"] == 0
    assert auth["n357_current_v13_incremental_rejected_terminals_if_consumed"] == N357_REJECT
    assert auth["n357_current_v13_candidate_remaining_terminals_if_consumed"] == POST_N357_IF_CONSUMED
    assert auth["n357_current_v13_composition_hostile_audit_status"] == "PENDING"
    assert auth["n357_main_pruning_credit_consumed"] is False

    frontier = state["current_exact_frontier"]
    assert frontier["authoritative_remaining_strata"] == REMAIN_STRATA
    assert frontier["authoritative_remaining_terminals"] == POST_CUT194_REMAIN
    assert frontier["cut194_main_pruning_credit"] is True
    assert frontier["cut194_incremental_rejected_terminals"] == CUT194_REJECT
    assert frontier["cut194_remaining_terminals"] == POST_CUT194_REMAIN
    assert frontier["cut193_main_pruning_credit"] is False
    assert frontier["n357_audit_review_id"] == N357_REVIEW
    assert frontier["n357_audited_exact_head"] == N357_HEAD
    assert frontier["n357_result_blob_sha1"] == N357_RESULT_BLOB
    assert frontier["n357_result_canonical_sha256"] == N357_RESULT_CANONICAL
    assert frontier["n357_candidate_incremental_rejected_terminals"] == N357_REJECT
    assert frontier["n357_current_v13_composition_replayed"] is True
    assert frontier["n357_current_v13_overlap_consumed_terminals"] == 0
    assert frontier["n357_current_v13_incremental_rejected_terminals_if_later_consumed"] == N357_REJECT
    assert frontier["n357_candidate_remaining_terminals_if_later_consumed"] == POST_N357_IF_CONSUMED
    assert frontier["n357_status"] == "AUDITED_CANDIDATE_CURRENT_V13_COMPOSITION_REPLAYED_NO_MAIN_CREDIT"
    assert frontier["n357_main_pruning_credit"] is False
    assert frontier["n357_current_v13_composition_hostile_audited"] is False
    assert frontier["full178_numerical_census_complete"] is False
    assert frontier["stage32_closed"] is False
    assert PRE_CUT194_REMAIN - CUT194_REJECT == POST_CUT194_REMAIN
    assert POST_CUT194_REMAIN - N357_REJECT == POST_N357_IF_CONSUMED

    assert result["node"] == "CUT194"
    assert result["target"]["row_id"] == "g1-d008"
    assert result["target"]["d"] == 8 and result["target"]["e"] == 8
    assert result["target"]["survivor_offset_range"] == [256, 510]
    assert result["result"]["candidate_closed_block_count"] == 234
    assert result["result"]["candidate_pruned_terminals"] == CUT194_REJECT
    assert result["result"]["candidate_post_wave2_from_main_v12_terminals"] == POST_CUT194_REMAIN
    assert result["credit"]["stage32_main_pruning_credit"] is False

    assert handoff["result"]["candidate_closed_block_count"] == 234
    assert handoff["result"]["candidate_pruned_terminals"] == CUT194_REJECT
    assert handoff["audit"]["hostile_audit_passed"] is False
    assert handoff["credit"]["stage32_main_pruning_credit"] is False

    assert mgmt["status"] == "RETAINED_AUTHORITY_TRANSITION_PENDING_REPLACEMENT_HEAD_HOSTILE_AUDIT"
    assert mgmt["authority"]["cut194_main_pruning_credit"] is True
    assert mgmt["authority"]["authoritative_remaining_terminals"] == POST_CUT194_REMAIN
    assert mgmt["overlap_replay"]["n356_overlap_zero"] is True
    assert mgmt["overlap_replay"]["cut191_overlap_zero"] is True
    assert mgmt["overlap_replay"]["cut193_overlap_zero"] is True
    assert mgmt["overlap_replay"]["double_charge"] is False

    aud = n357["audited_n357_candidate"]
    assert aud["pr"] == 1782
    assert aud["hostile_audit_status"] == "PASS"
    assert aud["hostile_audit_review_id"] == N357_REVIEW
    assert aud["audited_exact_head"] == N357_HEAD
    assert aud["result_blob_sha1"] == N357_RESULT_BLOB
    assert aud["result_canonical_sha256"] == N357_RESULT_CANONICAL
    assert aud["engine_blob_sha1"] == N357_ENGINE_BLOB
    assert aud["candidate_incremental_rejected_terminals"] == N357_REJECT
    assert aud["main_pruning_credit"] is False
    comp = n357["e8_overlap_replay"]
    assert comp["n357_overlap_with_current_consumed_terminals"] == 0
    assert comp["n357_rejecting_cut191_terminal_count"] == 0
    assert comp["n357_rejecting_cut194_terminal_count"] == 0
    assert comp["composition_incremental_rejected_terminals"] == N357_REJECT
    assert comp["candidate_remaining_terminals_if_later_consumed"] == POST_N357_IF_CONSUMED
    assert n357["credit_firewall"]["n357_main_pruning_credit"] is False
    assert n357["credit_firewall"]["main_authority_mutated_by_this_replay"] is False
    assert n357["credit_firewall"]["separate_main_consumption_required"] is True

    lock = state["source_locks"]["n357_current_v13_composition"]
    assert lock["audited_candidate_pr"] == 1782
    assert lock["audited_candidate_review_id"] == N357_REVIEW
    assert lock["audited_candidate_exact_head"] == N357_HEAD
    assert lock["audited_candidate_result_blob_sha1"] == N357_RESULT_BLOB
    assert lock["audited_candidate_result_canonical_sha256"] == N357_RESULT_CANONICAL
    assert lock["audited_candidate_engine_blob_sha1"] == N357_ENGINE_BLOB
    assert lock["composition_receipt_blob_sha1"] == EXPECTED["n357_composition"][1]
    assert lock["composition_receipt_canonical_sha256"] == EXPECTED["n357_composition"][2]
    assert lock["composition_verifier_blob_sha1"] == N357_COMPOSITION_VERIFIER_BLOB
    assert git_blob_sha(HERE / "verify_n357_v13_current_authority_composition.py") == N357_COMPOSITION_VERIFIER_BLOB
    assert git_blob_sha(HERE / "verify_n357_v13_current_authority_composition_fail_closed.py") == N357_FAIL_CLOSED_VERIFIER_BLOB
    assert lock["current_v13_overlap_cut191_terminals"] == 0
    assert lock["current_v13_overlap_cut194_terminals"] == 0
    assert lock["main_pruning_credit"] is False

    workflow = (ROOT / ".github/workflows/stage32-main-startup-authority.yml").read_text(encoding="utf-8")
    assert N357_HEAD in workflow
    assert "Checkout exact hostile-audited N357 candidate boundary" in workflow
    assert "verify_n357_v13_current_authority_composition_fail_closed.py --audited-n357-root .stage32-audited-n357" in workflow

    current = state["current"]
    assert current["mainbatch_stop_gate"] == "N357_CURRENT_V13_COMPOSITION_REPLAY_EXTERNAL_AUDIT"
    assert current["next_exact_route"] == "N357_CURRENT_V13_COMPOSITION_EXTERNAL_AUDIT_THEN_MAIN_CONSUMPTION"

    fw = state["firewalls"]
    for key in [
        "cut194_self_promoted_to_audited",
        "cut194_credit_exceeds_external_audit",
        "cut193_promoted_via_cut194",
        "n357_main_credit_without_current_authority_composition_audit",
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

    runpy.run_path(
        str(HERE / "verify_n357_v13_current_authority_composition.py"),
        run_name="__main__",
    )

    startup = START.read_text(encoding="utf-8")
    assert "Do not merge without explicit user authorization." in startup

    print("PASS Stage32 MAIN startup authority V13 CUT194_CONSUMED_N357_COMPOSITION_REPLAYED")
    print(f"authoritative_remaining={REMAIN_STRATA}_strata/{POST_CUT194_REMAIN}_terminals")
    print("n357_candidate_hostile_audit=PASS review=5183069892")
    print("n357_current_v13_overlap_cut191=0 overlap_cut194=0 main_credit=false")
    print(f"n357_candidate_remaining_if_later_consumed={POST_N357_IF_CONSUMED}")
    print("n357_fail_closed_audited_object_gate=source_locked")
    print("full178_complete=false merge_authorized=false")


if __name__ == "__main__":
    main()
