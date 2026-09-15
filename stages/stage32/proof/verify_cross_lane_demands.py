#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
REGISTRY=HERE/"CROSS-LANE-DEMANDS.json"; MONITOR=HERE/"ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"; STATE=ROOT/"stages/stage32/MAIN-STATE.json"
REGISTRY_BLOB="68a02f31431ad658b42ad695f9553c67fd6cff01"; REGISTRY_CANON="aec14c8c2a843e39478a287eb48d10696b1465124b2d089e0085630c66d346f5"
MONITOR_BLOB="2d245205d2c4e597284fcefc6b5f6b43f8df7a2a"; MONITOR_CANON="f5b2403a76546db1c7aea61bfb3eb5b62b3141063969e819758e6911f3a54e6e"
STATE_BLOB="ec0243cb998c5c58340100d8151559516c474193"; STATE_CANON="25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb"
BOUND=3360778813767800658369
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(p,b,c):
    req(blob(p)==b,f"blob drift {p}"); o=json.loads(p.read_text()); req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,f"canonical drift {p}"); return o
def main():
    reg=lock(REGISTRY,REGISTRY_BLOB,REGISTRY_CANON); mon=lock(MONITOR,MONITOR_BLOB,MONITOR_CANON); st=lock(STATE,STATE_BLOB,STATE_CANON)
    req([d["demand_id"] for d in reg["demands"] if d["status"]=="OPEN"]==[],"unexpected OPEN demand")
    req(mon["schema"]=="STAGE32_ACTIVE_SPECIALIST_MONITOR_CONTRACT_V9_V33_AUDIT_SYNCED_FULL178_REENTRY","monitor schema")
    ls=mon["last_live_sweep"]
    req(ls["lane_178"]["semantic_leaf"]=="TD02_GRF04_BOUNDED_PROBE" and ls["lane_178"]["main_handoff"]=="NONE","178 live sweep")
    req(ls["ex5"]["semantic_leaf"]=="HPADJ11_POSTAUDIT_MAIN_HANDOFF_PACKAGE" and ls["ex5"]["additional_main_credit"]==0,"EX5 live sweep")
    req(ls["mb"]["semantic_leaf"]=="MB104_ACTIVE_INCOMPLETE" and ls["mb"]["main_handoff"]=="NONE","MB live sweep")
    c=mon["latest_main_consumption"]; req(c["replacement_upper_bound"]==BOUND and c["main_consumed"] is True and c["double_charge"] is False,"historical V33 consumption")
    req(c["replacement_head_hostile_audited"] is True and c["replacement_head_hostile_audit_review_id"]==5216402010 and c["replacement_head_audit_synced_by_v34"] is True,"V33 audit sync")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V34_HPADJ11_AUDIT_SYNCED_FULL178_REENTRY","state schema")
    req(st["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"authority")
    req(st["current"]["mainbatch_stop_gate"]=="NONE" and st["firewalls"]["replacement_head_hostile_reaudit_required"] is False,"sync gate")
    req(st["current_exact_frontier"]["v34_additional_pruning"]==0,"sync added pruning")
    req(st["firewalls"]["full178_complete"] is False and st["firewalls"]["merge_authorized"] is False,"firewalls")
    print("PASS: Stage32 V34 synchronizes hostile-audited V33 with zero new pruning and resumes FULL178")
    print("PASS: 178 TD02 has no MAIN handoff; EX5 post-audit handoff gets zero duplicate credit; MB104 incomplete")
if __name__=="__main__": main()
