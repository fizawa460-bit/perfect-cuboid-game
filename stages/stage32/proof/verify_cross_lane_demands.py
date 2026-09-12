#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
REPO = STAGE.parents[1]
MAIN_STATE = STAGE / "MAIN-STATE.json"
V13_SNAPSHOT = STAGE / "management/MAIN-STATE-V13-N357-PRECONSUMPTION.json"
V13_VERIFIER = HERE / "verify_cross_lane_demands_v13.py"
N357_RECEIPT = STAGE / "management/post-n357-composition-pass-consumption-20260912.json"
CUT195_RECEIPT = STAGE / "management/post-cut195-current-v14-composition-consumption-20260912.json"
CUT195_REAUDIT_RECEIPT = STAGE / "management/post-cut195-v15-hostile-reaudit-pass-consumption-20260912.json"

V13_STATE_BLOB = "0f281111572572a8068cc38bb77f5f1c869b98ad"
V13_STATE_CANONICAL = "7c39d7935c36066cf2ec4a549eadc45e821fbf818490e6bfd10126f32bdf8a6d"
V13_VERIFIER_BLOB = "4ce5d9ffe53aa25a00af054e35d5419d35b05355"
V16_STATE_BLOB = "6bba1e9cceb2de1053777805f0e5d36d357a38a0"
V16_STATE_CANONICAL = "a78056fadbc1a44ac5210a7dcd2b97b00d2f88bb7fbb26e4a664439c984366eb"
N357_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
N357_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
CUT195_RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
CUT195_RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"
CUT195_REAUDIT_RECEIPT_BLOB = "7103d4f2c44fba5db52cde910095a6cd9e21233c"
CUT195_REAUDIT_RECEIPT_CANONICAL = "663ba737e7370eb06af822f3749ba3fc4aa2c572b46a40b6f6b64dd56ef1e113"
CUT195_REAUDIT_HEAD = "fdc372e1666e1176d80953b6303b13b240da84c5"
CUT195_REAUDIT_REVIEW = 5185987769
V16_MAIN = "e4d3b8b83626526ffeccdbd9c956081735fe1a6e"
CUT196_HEAD = "b4bca5f6dee0a910626587eedc06036e86888769"
CUT196_FAILED_CI = 34684663810
CUT194_INCREMENT = 26442
N357_INCREMENT = 17797986705435299826016
CUT195_INCREMENT = 26216
POST_CUT191 = 65396964990500233636101
POST_CUT194 = 65396964990500233609659
POST_N357 = 47598978285064933783643
POST_CUT195 = 47598978285064933757427

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")

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
    return json.loads(path.read_text(encoding="utf-8"))

def replay_v13_contract() -> None:
    req(git_blob(V13_SNAPSHOT) == V13_STATE_BLOB, "V13 snapshot blob drift")
    old = load(V13_SNAPSHOT)
    req(old["canonical_sha256_without_this_field"] == V13_STATE_CANONICAL, "V13 snapshot stored canonical drift")
    req(canonical(old) == V13_STATE_CANONICAL, "V13 snapshot canonical drift")
    req(git_blob(V13_VERIFIER) == V13_VERIFIER_BLOB, "V13 cross-lane verifier blob drift")

    current = MAIN_STATE.read_bytes()
    old_bytes = V13_SNAPSHOT.read_bytes()
    try:
        MAIN_STATE.write_bytes(old_bytes)
        proc = subprocess.run([sys.executable, str(V13_VERIFIER)], cwd=REPO)
        req(proc.returncode == 0, "historical V13 cross-lane contract replay failed")
    finally:
        MAIN_STATE.write_bytes(current)
    req(git_blob(MAIN_STATE) == V16_STATE_BLOB, "V16 MAIN state was not restored after historical replay")
    restored = load(MAIN_STATE)
    req(restored["canonical_sha256_without_this_field"] == V16_STATE_CANONICAL,
        "V16 restored MAIN state stored canonical drift")
    req(canonical(restored) == V16_STATE_CANONICAL,
        "V16 restored MAIN state canonical drift")

def main() -> None:
    replay_v13_contract()

    state = load(MAIN_STATE)
    frontier = state["current_exact_frontier"]
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 lost MAIN credit")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 lost MAIN credit")
    req(frontier["n357_main_pruning_credit"] is True, "N357 not consumed into MAIN")
    req(frontier["cut195_main_pruning_credit"] is True, "CUT195 not consumed into MAIN")
    req(frontier["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized MAIN credit")
    req(frontier["cut191_remaining_terminals"] == POST_CUT191, "post-CUT191 historical count drift")
    req(frontier["cut194_remaining_terminals"] == POST_CUT194, "post-CUT194 historical count drift")
    req(frontier["n357_incremental_rejected_terminals"] == N357_INCREMENT, "N357 increment drift")
    req(frontier["n357_remaining_terminals"] == POST_N357, "post-N357 count drift")
    req(frontier["cut195_incremental_rejected_terminals"] == CUT195_INCREMENT, "CUT195 increment drift")
    req(frontier["cut195_remaining_terminals"] == POST_CUT195, "post-CUT195 count drift")
    req(frontier["authoritative_remaining_terminals"] == POST_CUT195, "live authority is not post-CUT195")
    req(frontier["authoritative_remaining_strata"] == 17128, "live strata drift")
    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_N357 - CUT195_INCREMENT == POST_CUT195, "CUT195 arithmetic drift")
    req(POST_CUT191 - POST_CUT195 == CUT194_INCREMENT + N357_INCREMENT + CUT195_INCREMENT,
        "live MAIN delta double-charge or gap")

    auth = state["authority_sync"]
    req(auth["current_repository_main"] == V16_MAIN, "current repository main lock drift")
    req(auth["n357_current_v13_composition_hostile_audit_status"] == "PASS",
        "N357 current-authority composition lacks audit PASS")
    req(auth["n357_current_v13_composition_hostile_audit_review_id"] == 5184369560,
        "N357 composition audit review drift")
    req(auth["n357_current_v13_composition_audited_exact_head"] ==
        "0bdc3b952b35ea3201d8619f21a3df7a3015ff85",
        "N357 composition audited head drift")
    req(auth["n357_main_pruning_credit_consumed"] is True, "N357 consumption flag false")
    req(auth["n357_post_sync_reaudit_status"] == "PASS", "N357 replacement-head re-audit not consumed")
    req(auth["n357_synchronized_head_hostile_audited"] is True, "N357 synchronized head not audited")
    req(auth["cut195_candidate_hostile_audit_status"] == "PASS", "CUT195 candidate lacks audit PASS")
    req(auth["cut195_current_v14_composition_replayed"] is True, "CUT195 current-V14 composition not replayed")
    req(auth["cut195_current_v14_overlap_n357_terminals"] == 0, "CUT195 overlaps N357")
    req(auth["cut195_main_pruning_credit_consumed"] is True, "CUT195 consumption flag false")
    req(auth["cut195_post_sync_reaudit_required"] is False, "CUT195 replacement-head audit was not consumed")
    req(auth["cut195_post_sync_reaudit_status"] == "PASS", "CUT195 replacement-head audit PASS missing")
    req(auth["cut195_post_sync_reaudit_exact_head"] == CUT195_REAUDIT_HEAD,
        "CUT195 replacement-head audited head drift")
    req(auth["cut195_post_sync_reaudit_review_id"] == CUT195_REAUDIT_REVIEW,
        "CUT195 replacement-head audit review drift")
    req(auth["cut195_synchronized_head_hostile_audited"] is True,
        "CUT195 replacement head not synchronized as audited")
    req(frontier["cut195_synchronized_head_hostile_audited"] is True,
        "CUT195 frontier audit synchronization lost")

    req(frontier["cut196_candidate_exact_head"] == CUT196_HEAD, "CUT196 selected head drift")
    req(frontier["cut196_candidate_rejected_terminals"] == 27346, "CUT196 candidate count drift")
    req(frontier["cut196_claim_frontier_ci_run"] == CUT196_FAILED_CI, "CUT196 failed CI identity drift")
    req(frontier["cut196_claim_frontier_ci_status"] == "FAILURE", "CUT196 failure state drift")
    req(frontier["cut196_candidate_hostile_audited"] is False, "CUT196 self-awarded hostile audit")
    req(frontier["cut196_main_pruning_credit"] is False, "CUT196 gained unauthorized MAIN credit")

    req(git_blob(N357_RECEIPT) == N357_RECEIPT_BLOB, "N357 consumption receipt blob drift")
    n357_receipt = load(N357_RECEIPT)
    req(n357_receipt["canonical_sha256_without_this_field"] == N357_RECEIPT_CANONICAL,
        "N357 consumption receipt stored canonical drift")
    req(canonical(n357_receipt) == N357_RECEIPT_CANONICAL,
        "N357 consumption receipt canonical drift")
    x = n357_receipt["overlap_and_cross_lane_replay"]
    req(x["cut191_overlap_terminals"] == 0 and x["cut194_overlap_terminals"] == 0,
        "N357 overlaps previously consumed cuts")
    req(x["double_charge"] is False, "N357 double-charge flag set")
    req(x["g1_d008_e8_current_prefix_survivor_block_count"] == 7596,
        "CUT192 source prefix block count drift")
    req(x["g1_d008_e8_current_prefix_survivor_block_stream_sha256"] ==
        "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3",
        "CUT192 source prefix stream drift")
    req(x["cut192_preferred_wave_survivor_offset_range"] == [1, 255],
        "CUT192 preferred wave identity drift")
    req(x["n357_rejecting_current_prefix_blocks"] == 0,
        "N357 invalidates e=8 current prefix")
    req(x["n357_rejecting_cut192_preferred_wave_blocks"] == 0 and
        x["n357_rejecting_cut192_preferred_wave_terminals"] == 0,
        "N357 invalidates CUT192 preferred wave")
    req(x["cut192_satisfied_handoff_remains_current_main_surviving"] is True,
        "CUT192 satisfied handoff no longer current-MAIN surviving")

    req(git_blob(CUT195_RECEIPT) == CUT195_RECEIPT_BLOB, "CUT195 consumption receipt blob drift")
    cut195_receipt = load(CUT195_RECEIPT)
    req(cut195_receipt["canonical_sha256_without_this_field"] == CUT195_RECEIPT_CANONICAL,
        "CUT195 consumption receipt stored canonical drift")
    req(canonical(cut195_receipt) == CUT195_RECEIPT_CANONICAL,
        "CUT195 consumption receipt canonical drift")
    y = cut195_receipt["current_v14_composition_replay"]
    req(y["cut195_target_equals_current_prefix_offsets_511_765"] is True,
        "CUT195 current-prefix population identity drift")
    req(y["n357_rejecting_cut195_target_blocks"] == 0 and
        y["n357_rejecting_cut195_target_terminals"] == 0,
        "CUT195 overlaps N357 in retained receipt")
    req(y["cut191_disjoint"] is True and y["cut194_disjoint"] is True,
        "CUT195 overlaps consumed CUT191/CUT194")
    req(y["double_charge"] is False, "CUT195 double-charge flag set")

    req(git_blob(CUT195_REAUDIT_RECEIPT) == CUT195_REAUDIT_RECEIPT_BLOB,
        "CUT195 re-audit consumption receipt blob drift")
    reaud = load(CUT195_REAUDIT_RECEIPT)
    req(reaud["canonical_sha256_without_this_field"] == CUT195_REAUDIT_RECEIPT_CANONICAL,
        "CUT195 re-audit receipt stored canonical drift")
    req(canonical(reaud) == CUT195_REAUDIT_RECEIPT_CANONICAL,
        "CUT195 re-audit receipt canonical drift")
    ext = reaud["external_audit"]
    req(ext["audited_exact_head"] == CUT195_REAUDIT_HEAD,
        "CUT195 re-audit receipt head drift")
    req(ext["review_id"] == CUT195_REAUDIT_REVIEW and ext["status"] == "PASS",
        "CUT195 re-audit receipt review/status drift")
    req(ext["merged_main_commit"] == V16_MAIN, "CUT195 re-audit receipt merged-main drift")
    transition = reaud["authority_transition"]
    req(transition["mathematical_authority_changed"] is False,
        "audit consumption changed mathematical authority")
    req(transition["remaining_terminals_before"] == transition["remaining_terminals_after"] == POST_CUT195,
        "audit consumption changed terminal authority")
    fs = reaud["full178_frontier_selection"]
    req(fs["selected_next_candidate"] == "CUT196", "CUT196 not selected in re-audit receipt")
    req(fs["candidate_exact_head"] == CUT196_HEAD, "CUT196 receipt head drift")
    req(fs["claim_frontier_ci_run"] == CUT196_FAILED_CI and fs["claim_frontier_ci_status"] == "FAILURE",
        "CUT196 receipt CI status drift")
    req(fs["candidate_hostile_audit_status"] == "NOT_AUDITED", "CUT196 receipt audit status drift")
    req(fs["main_pruning_credit"] is False, "CUT196 receipt grants MAIN credit")

    req(state["firewalls"]["merge_authorized"] is False, "merge authorized")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(frontier["stage32_closed"] is False, "Stage32 incorrectly closed")

    print(json.dumps({
        "verdict": "PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V16",
        "historical_v13_contract_replayed": True,
        "cut191_main_consumed": True,
        "cut194_main_consumed": True,
        "n357_main_consumed": True,
        "cut195_main_consumed": True,
        "cut195_replacement_head_reaudit_consumed": True,
        "n357_incremental_rejected_terminals": N357_INCREMENT,
        "cut195_incremental_rejected_terminals": CUT195_INCREMENT,
        "authoritative_remaining_terminals": POST_CUT195,
        "cut192_preferred_wave_n357_overlap": 0,
        "cut195_n357_overlap": 0,
        "cut193_main_credit": False,
        "cut196_candidate_terminals": 27346,
        "cut196_claim_frontier_ci": "FAILURE",
        "cut196_hostile_audited": False,
        "cut196_main_credit": False,
        "full178_complete": False,
        "replacement_head_hostile_reaudit_required": False,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
