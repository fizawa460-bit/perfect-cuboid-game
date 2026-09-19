#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[3]
STATE=ROOT/"stages/stage32/MAIN-STATE.json"; RECEIPT=HERE/"HPADJ22-V44-MAIN-BOUND-REPLACEMENT.json"; SOURCE=HERE/"HPADJ22-DIRECT-FULL178-RETAINED.json"
REGISTRY=ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json"; FRONTIER=ROOT/"stages/stage32/proof/ACTIVE-FRONTIER.json"; ADAPTERS=ROOT/"stages/stage32/proof/LANE-ADAPTERS.json"
AUDITED_HEAD="e24488f1394abae25d9b0f9d099c8efd84e03a2a"; AUDIT_REVIEW=5254762142; CURRENT_MAIN="83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49"
OLD=157570677819451133507; NEW=138652739800650593494; TIGHTENING=18917938018800540013
RECEIPT_BLOB="a2be82fe69bf1d2fdefc0a7ba566601246a0bec4"; RECEIPT_CANON="cef45672a180124ce46972fed6ead43bb94b16e552496c6101a8e5dfa1b8a7b9"
SOURCE_BLOB="60ca65208b774cc79c646c46c6780e7028a29845"; SOURCE_CANON="285def36fd8d05557a73ab324ed56178116d5d51fbf6323a33a5f6ecaf6c8805"
AUDITED_STATE_BLOB="bb37bee4d433921e4bbdb2a9fdd5b74042b3282f"; AUDITED_STATE_CANON="fd80eea92a14827186edc71767880f4c7f7bc9a8ea206ca2a19e0ee756224abf"
AUDITED_STARTUP_BLOB="3af851faed82912e4fb138bce8779435b6e76f80"; AUDITED_AUTHORITY_BLOB="0af26aa6436019a05f2151125e2374d0527be136"
REGISTRY_BLOB="f3a884adc1c82aace81cb73d049ff14720ace862"; FRONTIER_BLOB="4c251be4aa5c355481fe3bcfc71c292fb6389ba4"; ADAPTERS_BLOB="c0ef34e5838e27046a20fed77063593009c56f40"
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock_json(p,b,c,label):
    req(blob(p)==b,label+" blob drift"); o=json.loads(p.read_text(encoding="utf-8")); req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,label+" canonical drift"); return o
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--audited-root",type=Path); args=ap.parse_args()
    receipt=lock_json(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON,"V44 replacement receipt"); source=lock_json(SOURCE,SOURCE_BLOB,SOURCE_CANON,"HPADJ22 source")
    state=json.loads(STATE.read_text(encoding="utf-8")); req(canon(state)==state.get("canonical_sha256_without_this_field"),"MAIN state canonical drift")
    req(blob(REGISTRY)==REGISTRY_BLOB and blob(FRONTIER)==FRONTIER_BLOB and blob(ADAPTERS)==ADAPTERS_BLOB,"claim DAG lock drift")
    if args.audited_root is not None:
        root=args.audited_root; old=lock_json(root/"stages/stage32/MAIN-STATE.json",AUDITED_STATE_BLOB,AUDITED_STATE_CANON,"audited candidate state")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"]==OLD,"audited predecessor authority")
        req(blob(root/"stages/stage32/verify_main_startup.py")==AUDITED_STARTUP_BLOB,"audited startup drift")
        req(blob(root/"stages/stage32/verify_main_startup_authority_v44_btva_static7_normalmass.py")==AUDITED_AUTHORITY_BLOB,"audited authority verifier drift")
    cand=receipt["audited_candidate"]; req(cand["audited_exact_head"]==AUDITED_HEAD and cand["hostile_audit_review_id"]==AUDIT_REVIEW and cand["hostile_audit_status"]=="PASS","candidate audit")
    req(cand["candidate_upper_bound"]==str(NEW) and cand["exact_tightening_vs_hpadj21"]==str(TIGHTENING) and cand["full178_cells"]==1424 and cand["gaps"]==0 and cand["overlaps"]==0,"candidate evidence")
    req(source["result"]["current_authority"]==str(OLD) and source["result"]["candidate_global_upper_bound_if_promoted"]==str(NEW) and source["result"]["exact_tightening_if_promoted"]==str(TIGHTENING),"source arithmetic")
    req(source["composition"]["all_1424_cells_covered_exactly_once"] is True and source["composition"]["additive_subtraction"] is False and source["composition"]["statistical_independence"] is False,"source composition")
    repl=receipt["replacement"]; req(repl["authoritative_remaining_terminals"]==str(NEW) and repl["additive_subtraction_performed"] is False and repl["double_charge"] is False and repl["full178_numerical_census_complete"] is False,"replacement")
    req(state["schema"]=="STAGE32_MAIN_COMPACT_STATE_V44_HPADJ22_FULL178_BOUND_CONSUMED_REAUDIT_PENDING","state schema")
    f=state["current_exact_frontier"]; req(f["authoritative_remaining_strata"]==17128 and f["authoritative_remaining_terminals"]==NEW,"state authority"); req(f["predecessor_v43_authoritative_remaining_terminals"]==OLD,"V43 predecessor"); req(f["v44_hpadj22_main_numeric_bound_replacement_consumed"] is True and f["v44_hpadj22_candidate_main_credit"] is True,"V44 credit"); req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,"closure")
    req(state["current"]["mainbatch_stop_gate"]=="NONE","legacy stop gate"); req(state["current"]["next_exact_route"]=="HOSTILE_AUDIT_V44_HPADJ22_FULL178_BOUND_REPLACEMENT","next route"); req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"reaudit gate")
    for key in ("full178_complete","effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"): req(state["firewalls"][key] is False,"firewall "+key)
    req(OLD-NEW==TIGHTENING,"arithmetic")
    print("PASS: Stage32 V44 consumes hostile-audited HPADJ22 FULL178 candidate by same-population MIN replacement")
    print("PASS: authoritative upper bound = 138652739800650593494; replacement head requires hostile re-audit")
if __name__=="__main__": main()
