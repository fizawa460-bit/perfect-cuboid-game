#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage32/management/post-cut196-current-v16-composition-consumption-20260912.json"
PREDECESSOR = ROOT / "stages/stage32/management/MAIN-STATE-V16-CUT196-PRECONSUMPTION.json"
CUT196_RESULT = ROOT / "stages/stage32/management/CUT196-AUDITED-RESULT.json"
COMPOSITION_VERIFIER = ROOT / "stages/stage32/verify_cut196_v16_current_authority_composition.py"

STATE_BLOB = "157acdb438bfbde40a71a5974effbd097bff05df"
STATE_CANONICAL = "a21faa5b3c3f5be259d8c5bc7ffa6f7aac827b911256e7a916e0bf9ea8e85de9"
RECEIPT_BLOB = "a45f27611d6d274e7e7e3ff65e8a75089e996596"
RECEIPT_CANONICAL = "2c55ddd13f90068fc8383c755dcada07f265c40c6ff468709b0add12a390c0e2"
PREDECESSOR_BLOB = "1b46f01070f5bbf1b81ba5c84684dcaa1a459119"
PREDECESSOR_CANONICAL = "cd1865abe9918e1b5a64d2b9148f378a54cc24b203f16295ce256685164d3fd8"
CUT196_RESULT_BLOB = "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde"
CUT196_RESULT_CANONICAL = "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92"
COMPOSITION_VERIFIER_BLOB = "ce2d82da5b37af53e55212c0c60ebc03d2ab5836"
PRE = 47598978285064933757427
INC = 27346
POST = 47598978285064933730081
STRATA = 17128

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob mismatch: {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical mismatch: {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical mismatch: {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    prev = load_locked(PREDECESSOR, PREDECESSOR_BLOB, PREDECESSOR_CANONICAL)
    req(prev["schema"] == "STAGE32_MAIN_COMPACT_STATE_V16_CUT195_REAUDIT_CONSUMED", "unexpected predecessor schema")
    pf = prev["current_exact_frontier"]
    req(pf["authoritative_remaining_strata"] == STRATA, "predecessor strata drift")
    req(pf["authoritative_remaining_terminals"] == PRE, "predecessor terminals drift")
    req(pf["cut196_candidate_exact_head"] == "85f4e988acf6446fa0d472208e21990621a650b4", "predecessor CUT196 head drift")
    req(pf["cut196_claim_frontier_ci_status"] == "SUCCESS", "predecessor CUT196 CI drift")
    req(pf["cut196_main_pruning_credit"] is False, "predecessor self-awarded CUT196 credit")
    cut = load_locked(CUT196_RESULT, CUT196_RESULT_BLOB, CUT196_RESULT_CANONICAL)
    req(cut["result"]["candidate_closed_block_count"] == 242, "CUT196 closed count drift")
    req(cut["result"]["candidate_pruned_terminals"] == INC, "CUT196 increment drift")
    req(cut["target"]["survivor_offset_range"] == [766, 1020], "CUT196 offset drift")
    req(cut["target"]["cut191_block0_disjoint"] is True, "CUT196/CUT191 overlap")
    req(cut["target"]["cut193_wave1_disjoint"] is True, "CUT196/CUT193 overlap")
    req(cut["target"]["cut194_wave2_disjoint"] is True, "CUT196/CUT194 overlap")
    req(cut["target"]["cut195_wave3_disjoint"] is True, "CUT196/CUT195 overlap")
    req(git_blob(COMPOSITION_VERIFIER) == COMPOSITION_VERIFIER_BLOB, "CUT196 current-V16 composition verifier drift")
    receipt = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANONICAL)
    req(receipt["schema"] == "STAGE32_MAIN_POST_CUT196_CURRENT_V16_COMPOSITION_CONSUMPTION_V1", "receipt schema drift")
    req(receipt["prior_main_boundary"]["exact_head"] == "bc4463794055b8442814b892fd33204416c2b531", "predecessor exact head drift")
    req(receipt["prior_main_boundary"]["hostile_reaudit_review_id"] == 5186235938, "predecessor hostile re-audit review drift")
    cc = receipt["cut196_candidate"]
    req(cc["audited_exact_head"] == "85f4e988acf6446fa0d472208e21990621a650b4", "CUT196 audited head drift")
    req(cc["hostile_audit_review_id"] == 5186302071 and cc["hostile_audit_status"] == "PASS", "CUT196 hostile audit identity/status drift")
    req(cc["exact_head_claim_frontier_ci_run"] == 34687223279, "CUT196 CI identity drift")
    rr = receipt["current_v16_composition_replay"]
    req(rr["cut196_target_equals_current_prefix_offsets_766_1020"] is True, "CUT196 current-prefix identity drift")
    req(rr["n357_rejecting_cut196_target_blocks"] == 0, "CUT196/N357 block overlap")
    req(rr["n357_rejecting_cut196_target_terminals"] == 0, "CUT196/N357 terminal overlap")
    req(rr["double_charge"] is False, "CUT196 double-charge flag set")
    ra = receipt["authority"]
    req(ra["before_remaining_terminals"] == PRE, "receipt pre authority drift")
    req(ra["incremental_rejected_terminals"] == INC, "receipt increment drift")
    req(ra["after_remaining_terminals"] == POST, "receipt post authority drift")
    req(receipt["next_gate"]["replacement_head_hostile_reaudit_required"] is True, "replacement re-audit gate missing")
    req(receipt["next_gate"]["replacement_head_hostile_reaudit_status"] == "PENDING", "replacement re-audit self-awarded")
    state = load_locked(STATE, STATE_BLOB, STATE_CANONICAL)
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V17_CUT196_AUDITED_CONSUMED", "unexpected V17 schema")
    auth = state["authority_sync"]
    req(auth["cut196_candidate_hostile_audit_status"] == "PASS", "CUT196 audit PASS missing")
    req(auth["cut196_candidate_hostile_audit_review_id"] == 5186302071, "CUT196 review drift")
    req(auth["cut196_current_v16_composition_replayed"] is True, "CUT196 composition replay missing")
    req(auth["cut196_current_v16_overlap_n357_terminals"] == 0, "CUT196/N357 overlap not zero")
    req(auth["cut196_main_pruning_credit_consumed"] is True, "CUT196 MAIN credit not consumed")
    req(auth["cut196_post_sync_reaudit_status"] == "PENDING", "V17 replacement audit self-awarded")
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == STRATA, "V17 strata drift")
    req(frontier["authoritative_remaining_terminals"] == POST, "V17 terminal authority drift")
    req(frontier["cut196_incremental_rejected_terminals"] == INC, "V17 increment drift")
    req(frontier["cut196_main_pruning_credit"] is True, "V17 CUT196 credit missing")
    req(frontier["cut196_synchronized_head_hostile_audited"] is False, "V17 replacement head self-awarded hostile audit")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 falsely closed")
    req(frontier["stage32_closed"] is False, "Stage32 falsely closed")
    req(PRE - INC == POST, "V17 authority arithmetic drift")
    fw = state["firewalls"]
    for key in ("receiver_credit","theorem_credit","endpoint_credit","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized","stage32_closed"):
        req(fw[key] is False, f"firewall opened: {key}")
    print(json.dumps({"verdict":"PASS_STAGE32_MAIN_V17_CUT196_AUDITED_CONSUMED","cut196_main_pruning_credit":True,"cut196_incremental_rejected_terminals":INC,"authoritative_remaining_strata":STRATA,"authoritative_remaining_terminals":POST,"full178_complete":False,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
