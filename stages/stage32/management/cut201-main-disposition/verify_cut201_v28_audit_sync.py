#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
SYNC=HERE/"CUT201-V28-HOSTILE-AUDIT-PASS-SYNC.json"
V27R=HERE/"CUT201-V27-MAIN-CONSUMPTION.json"
CLAIM=ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER=ROOT/"stages/stage32/proof/ACTIVE-FRONTIER.json"
LANES=ROOT/"stages/stage32/proof/LANE-ADAPTERS.json"
AUDITED="3cf5df3dab8968bf20188ee94d8e4a0a834dc2bb"
REVIEW=5207093455
OLD_BLOB="399221dc91733b3a9a2d79ae3473ea2365e409a3"
OLD_CANON="e25d3c2d3381193462af28577c6ddd0c6c5fc597192a640d7534034213b86d1b"
STATE_BLOB="69dd727697ab3f8d464f8a48e7bc708739d6973a"
STATE_CANON="29859578ce1c4e2372379cd508595e767393d676c0b6429e7de3bc8691998fc9"
SYNC_BLOB="1af25126b74dc887208f785b27e2fc5e02eff99c"
SYNC_CANON="411df68063eab37a5d81053f01c436c803edb79df18752466777525a0dcac33d"
V27R_BLOB="cdd766cae064430bb1aa901f1d023fcb48b39877"
V27R_CANON="aa9a40c0514412444a15db8a59d54de4866de39345ff4a0dbd531c14eaced9f6"
AUTH=26876434389242951065128; STRATA=17128

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def locked(p,b,c=None):
    req(p.is_file() and blob(p)==b,f"blob drift {p}")
    o=json.loads(p.read_text())
    if c: req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}")
    return o
def head(p): return subprocess.check_output(["git","-C",str(p),"rev-parse","HEAD"],text=True).strip()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--audited-v27-root",type=Path); a=ap.parse_args()
    if a.audited_v27_root:
        r=a.audited_v27_root.resolve(); req(head(r)==AUDITED,"audited V27 head")
        o=locked(r/"stages/stage32/MAIN-STATE.json",OLD_BLOB,OLD_CANON)
        req(o["schema"]=="STAGE32_MAIN_COMPACT_STATE_V27_CUT201_CONSUMED_PENDING_REAUDIT","old schema")
        req(o["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"old audit gate")
        req(o["current_exact_frontier"]["authoritative_remaining_terminals"]==AUTH,"old authority")
    y=locked(SYNC,SYNC_BLOB,SYNC_CANON); b=y["audited_boundary"]; ac=y["authority_accounting"]
    req(b["status"]=="PASS" and b["exact_head"]==AUDITED and b["review_id"]==REVIEW,"audit identity")
    req(b["merge_ready_freshness"]=="CLEAR" and b["main_state_blob_sha1"]==OLD_BLOB,"audit source lock")
    req(ac["pre_sync_remaining_terminals_upper_bound"]==AUTH==ac["post_sync_remaining_terminals_upper_bound"],"sync authority")
    req(ac["cut201_consumed_terminals"]==18758 and ac["cut201_certlift03_overlap_terminals"]==6780,"CUT201 accounting")
    req(ac["cut201_other_consumed_route_overlap_terminals"]==0 and ac["additional_pruning_credit_consumed"]==0,"new credit")
    req(ac["double_charge"] is False and ac["producer_lane_subtraction_performed"] is False and ac["main_consumer_subtraction_performed"] is True,"double charge")
    v=locked(V27R,V27R_BLOB,V27R_CANON)
    req(v["accounting"]["credited_incremental_rejected_terminals"]==18758 and v["accounting"]["post_consumption_certified_remaining_terminals_upper_bound"]==AUTH,"V27 receipt")
    req(blob(CLAIM)=="f3a884adc1c82aace81cb73d049ff14720ace862" and blob(FRONTIER)=="4c251be4aa5c355481fe3bcfc71c292fb6389ba4" and blob(LANES)=="c0ef34e5838e27046a20fed77063593009c56f40","claim surface drift")
    s=locked(STATE,STATE_BLOB,STATE_CANON); f=s["current_exact_frontier"]
    req(s["schema"]=="STAGE32_MAIN_COMPACT_STATE_V28_CUT201_AUDIT_SYNCED","schema")
    req(f["authoritative_remaining_strata"]==STRATA and f["authoritative_remaining_terminals"]==AUTH,"authority")
    req(f["cut201_v27_replacement_hostile_audited"] is True and f["cut201_v27_replacement_hostile_audit_review_id"]==REVIEW,"audit sync")
    req(s["current"]["mainbatch_stop_gate"]=="NONE" and s["firewalls"]["replacement_head_hostile_reaudit_required"] is False,"route release")
    req(s["current"]["next_exact_route"]=="FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS","route")
    for k in ("effectivity_released","endpoint_credit","full178_complete","merge_authorized","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","receiver_credit","route_credit","stage32_closed","theorem_credit"): req(s["firewalls"][k] is False,k)
    print(json.dumps({"verdict":"PASS_V28_CUT201_HOSTILE_AUDIT_SYNC","audited_exact_head":AUDITED,"review_id":REVIEW,"remaining_strata":STRATA,"remaining_terminals_upper_bound":AUTH,"additional_pruning_credit":0,"full178_status":"ACTIVE_INCOMPLETE","merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
