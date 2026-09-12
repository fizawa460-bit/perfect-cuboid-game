#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
REPO = STAGE.parents[1]
MAIN_STATE = STAGE / "MAIN-STATE.json"
V13_SNAPSHOT = STAGE / "management/MAIN-STATE-V13-N357-PRECONSUMPTION.json"
V13_VERIFIER = HERE / "verify_cross_lane_demands_v13.py"
CONSUMPTION_RECEIPT = STAGE / "management/post-n357-composition-pass-consumption-20260912.json"

V13_STATE_BLOB = "0f281111572572a8068cc38bb77f5f1c869b98ad"
V13_STATE_CANONICAL = "7c39d7935c36066cf2ec4a549eadc45e821fbf818490e6bfd10126f32bdf8a6d"
V13_VERIFIER_BLOB = "4ce5d9ffe53aa25a00af054e35d5419d35b05355"
V14_STATE_BLOB = "7f4cdb067959b3ed561013ec195bd3b6f4993baf"
CONSUMPTION_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
CONSUMPTION_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
CUT194_INCREMENT = 26442
N357_INCREMENT = 17797986705435299826016
POST_CUT191 = 65396964990500233636101
POST_CUT194 = 65396964990500233609659
POST_N357 = 47598978285064933783643

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
    req(git_blob(MAIN_STATE) == V14_STATE_BLOB, "V14 MAIN state was not restored after historical replay")

def main() -> None:
    replay_v13_contract()

    state = load(MAIN_STATE)
    frontier = state["current_exact_frontier"]
    req(frontier["cut191_main_pruning_credit"] is True, "CUT191 lost MAIN credit")
    req(frontier["cut194_main_pruning_credit"] is True, "CUT194 lost MAIN credit")
    req(frontier["n357_main_pruning_credit"] is True, "N357 not consumed into MAIN")
    req(frontier["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized MAIN credit")
    req(frontier["cut191_remaining_terminals"] == POST_CUT191, "post-CUT191 historical count drift")
    req(frontier["cut194_remaining_terminals"] == POST_CUT194, "post-CUT194 historical count drift")
    req(frontier["n357_incremental_rejected_terminals"] == N357_INCREMENT, "N357 increment drift")
    req(frontier["n357_remaining_terminals"] == POST_N357, "post-N357 count drift")
    req(frontier["authoritative_remaining_terminals"] == POST_N357, "live authority is not post-N357")
    req(frontier["authoritative_remaining_strata"] == 17128, "live strata drift")
    req(POST_CUT191 - CUT194_INCREMENT == POST_CUT194, "CUT194 arithmetic drift")
    req(POST_CUT194 - N357_INCREMENT == POST_N357, "N357 arithmetic drift")
    req(POST_CUT191 - POST_N357 == CUT194_INCREMENT + N357_INCREMENT,
        "live MAIN delta double-charge or gap")

    auth = state["authority_sync"]
    req(auth["n357_current_v13_composition_hostile_audit_status"] == "PASS",
        "N357 current-authority composition lacks audit PASS")
    req(auth["n357_current_v13_composition_hostile_audit_review_id"] == 5184369560,
        "N357 composition audit review drift")
    req(auth["n357_current_v13_composition_audited_exact_head"] ==
        "0bdc3b952b35ea3201d8619f21a3df7a3015ff85",
        "N357 composition audited head drift")
    req(auth["n357_main_pruning_credit_consumed"] is True, "N357 consumption flag false")
    req(auth["n357_post_sync_reaudit_required"] is True, "replacement-head audit gate missing")
    req(auth["n357_synchronized_head_hostile_audited"] is False,
        "replacement head self-awarded audit")

    req(git_blob(CONSUMPTION_RECEIPT) == CONSUMPTION_RECEIPT_BLOB,
        "N357 consumption receipt blob drift")
    receipt = load(CONSUMPTION_RECEIPT)
    req(receipt["canonical_sha256_without_this_field"] == CONSUMPTION_RECEIPT_CANONICAL,
        "N357 consumption receipt stored canonical drift")
    req(canonical(receipt) == CONSUMPTION_RECEIPT_CANONICAL,
        "N357 consumption receipt canonical drift")
    x = receipt["overlap_and_cross_lane_replay"]
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

    req(state["firewalls"]["merge_authorized"] is False, "merge authorized")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 incorrectly closed")
    req(frontier["stage32_closed"] is False, "Stage32 incorrectly closed")

    print(json.dumps({
        "verdict": "PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V14",
        "historical_v13_contract_replayed": True,
        "cut191_main_consumed": True,
        "cut194_main_consumed": True,
        "n357_main_consumed": True,
        "n357_incremental_rejected_terminals": N357_INCREMENT,
        "authoritative_remaining_terminals": POST_N357,
        "cut192_preferred_wave_n357_overlap": 0,
        "cut193_main_credit": False,
        "full178_complete": False,
        "replacement_head_hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
