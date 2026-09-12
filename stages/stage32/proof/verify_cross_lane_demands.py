#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = STAGE.parents[1]
STATE = STAGE / "MAIN-STATE.json"
RECEIPT = STAGE / "management/post-cut196-current-v16-composition-consumption-20260912.json"
PREDECESSOR = STAGE / "management/MAIN-STATE-V16-CUT196-PRECONSUMPTION.json"
CUT196_RESULT = STAGE / "management/CUT196-AUDITED-RESULT.json"
N357_RECEIPT = STAGE / "management/post-n357-composition-pass-consumption-20260912.json"
CUT195_RECEIPT = STAGE / "management/post-cut195-current-v14-composition-consumption-20260912.json"
STATE_BLOB = "157acdb438bfbde40a71a5974effbd097bff05df"
STATE_CANONICAL = "a21faa5b3c3f5be259d8c5bc7ffa6f7aac827b911256e7a916e0bf9ea8e85de9"
RECEIPT_BLOB = "a45f27611d6d274e7e7e3ff65e8a75089e996596"
RECEIPT_CANONICAL = "2c55ddd13f90068fc8383c755dcada07f265c40c6ff468709b0add12a390c0e2"
PREDECESSOR_BLOB = "1b46f01070f5bbf1b81ba5c84684dcaa1a459119"
PREDECESSOR_CANONICAL = "cd1865abe9918e1b5a64d2b9148f378a54cc24b203f16295ce256685164d3fd8"
CUT196_RESULT_BLOB = "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde"
CUT196_RESULT_CANONICAL = "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92"
N357_RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
N357_RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"
CUT195_RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
CUT195_RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"
POST_CUT191=65396964990500233636101
CUT194_INCREMENT=26442
POST_CUT194=65396964990500233609659
N357_INCREMENT=17797986705435299826016
POST_N357=47598978285064933783643
CUT195_INCREMENT=26216
POST_CUT195=47598978285064933757427
CUT196_INCREMENT=27346
POST_CUT196=47598978285064933730081

def req(v: bool, msg: str) -> None:
    if not v: raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canonical(obj: dict) -> str:
    cp=dict(obj); cp.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(cp,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path)==blob, f"blob drift {path.relative_to(ROOT)}")
    obj=json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field")==can, f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj)==can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    state=load_locked(STATE,STATE_BLOB,STATE_CANONICAL)
    prev=load_locked(PREDECESSOR,PREDECESSOR_BLOB,PREDECESSOR_CANONICAL)
    result=load_locked(CUT196_RESULT,CUT196_RESULT_BLOB,CUT196_RESULT_CANONICAL)
    receipt=load_locked(RECEIPT,RECEIPT_BLOB,RECEIPT_CANONICAL)
    load_locked(N357_RECEIPT,N357_RECEIPT_BLOB,N357_RECEIPT_CANONICAL)
    load_locked(CUT195_RECEIPT,CUT195_RECEIPT_BLOB,CUT195_RECEIPT_CANONICAL)
    pf=prev["current_exact_frontier"]
    req(pf["authoritative_remaining_terminals"]==POST_CUT195,"predecessor authority drift")
    req(pf["cut196_main_pruning_credit"] is False,"predecessor CUT196 credit drift")
    f=state["current_exact_frontier"]
    req(f["cut191_main_pruning_credit"] is True,"CUT191 lost MAIN credit")
    req(f["cut194_main_pruning_credit"] is True,"CUT194 lost MAIN credit")
    req(f["n357_main_pruning_credit"] is True,"N357 lost MAIN credit")
    req(f["cut195_main_pruning_credit"] is True,"CUT195 lost MAIN credit")
    req(f["cut193_main_pruning_credit"] is False,"CUT193 gained unauthorized MAIN credit")
    req(f["cut196_main_pruning_credit"] is True,"CUT196 MAIN credit missing")
    req(f["cut196_candidate_hostile_audited"] is True,"CUT196 audit PASS not synchronized")
    req(f["cut196_current_v16_composition_replayed"] is True,"CUT196 composition replay missing")
    req(f["cut196_current_v16_overlap_n357_terminals"]==0,"CUT196/N357 overlap nonzero")
    req(f["cut196_synchronized_head_hostile_audited"] is False,"replacement head self-awarded audit")
    req(f["authoritative_remaining_strata"]==17128,"strata drift")
    req(f["authoritative_remaining_terminals"]==POST_CUT196,"terminal authority drift")
    req(f["full178_numerical_census_complete"] is False,"FULL178 incorrectly closed")
    req(f["stage32_closed"] is False,"Stage32 incorrectly closed")
    req(POST_CUT191-CUT194_INCREMENT==POST_CUT194,"CUT194 arithmetic drift")
    req(POST_CUT194-N357_INCREMENT==POST_N357,"N357 arithmetic drift")
    req(POST_N357-CUT195_INCREMENT==POST_CUT195,"CUT195 arithmetic drift")
    req(POST_CUT195-CUT196_INCREMENT==POST_CUT196,"CUT196 arithmetic drift")
    rr=receipt["current_v16_composition_replay"]
    req(rr["cut191_disjoint"] and rr["cut193_disjoint"] and rr["cut194_disjoint"] and rr["cut195_disjoint"],"CUT196 prior-cut disjointness missing")
    req(rr["n357_rejecting_cut196_target_blocks"]==0,"CUT196/N357 block overlap")
    req(rr["n357_rejecting_cut196_target_terminals"]==0,"CUT196/N357 terminal overlap")
    req(rr["double_charge"] is False,"CUT196 double-charge flag set")
    req(result["result"]["candidate_pruned_terminals"]==CUT196_INCREMENT,"CUT196 result increment drift")
    req(result["target"]["survivor_offset_range"]==[766,1020],"CUT196 result offsets drift")
    auth=state["authority_sync"]
    req(auth["cut196_candidate_hostile_audit_status"]=="PASS","CUT196 audit status drift")
    req(auth["cut196_candidate_hostile_audit_review_id"]==5186302071,"CUT196 review drift")
    req(auth["cut196_main_pruning_credit_consumed"] is True,"CUT196 consumption flag false")
    req(auth["cut196_post_sync_reaudit_required"] is True,"replacement re-audit gate lost")
    req(auth["cut196_post_sync_reaudit_status"]=="PENDING","replacement audit self-awarded")
    fw=state["firewalls"]
    req(fw["merge_authorized"] is False,"merge authorized")
    req(fw["receiver_credit"] is False and fw["theorem_credit"] is False and fw["endpoint_credit"] is False,"final-chain credit firewall opened")
    print(json.dumps({"verdict":"PASS_STAGE32_CROSS_LANE_DEMAND_COORDINATION_V17","cut191_main_consumed":True,"cut194_main_consumed":True,"n357_main_consumed":True,"cut195_main_consumed":True,"cut196_main_consumed":True,"cut193_main_credit":False,"cut196_incremental_rejected_terminals":CUT196_INCREMENT,"authoritative_remaining_terminals":POST_CUT196,"cut196_n357_overlap":0,"full178_complete":False,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False},sort_keys=True))

if __name__=="__main__": main()
