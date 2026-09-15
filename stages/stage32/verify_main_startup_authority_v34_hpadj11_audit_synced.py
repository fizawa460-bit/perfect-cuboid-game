#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
STATE=HERE/"MAIN-STATE.json"; CROSS=HERE/"proof/verify_cross_lane_demands.py"; MONITOR=HERE/"proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json"
RECEIPT=HERE/"management/hpadj11-main-disposition/HPADJ11-V34-HOSTILE-AUDIT-PASS-SYNC.json"; SYNC=HERE/"management/hpadj11-main-disposition/verify_hpadj11_v34_audit_sync.py"
CLAIMS=HERE/"proof/CLAIM-REGISTRY.json"; FRONTIER=HERE/"proof/ACTIVE-FRONTIER.json"; ADAPTERS=HERE/"proof/LANE-ADAPTERS.json"
STATE_BLOB="ec0243cb998c5c58340100d8151559516c474193"; STATE_CANON="25e68a40148ce1ca4bb893ef47d23a0e213898aca8be3a76f497252cb2adc2eb"; CROSS_BLOB="9d7c3ee0e74f8d32d54904faf817f1b387c1f01b"; MONITOR_BLOB="2d245205d2c4e597284fcefc6b5f6b43f8df7a2a"; MONITOR_CANON="f5b2403a76546db1c7aea61bfb3eb5b62b3141063969e819758e6911f3a54e6e"
RECEIPT_BLOB="0cb8f764cda214548869f24d27427acb1d611462"; RECEIPT_CANON="11dfd2437ee464c80d74984fb3428201020c103ca19b3a435d887b7bcf98e123"; SYNC_BLOB="9ae1968c82710efaec29906d8fab8337dc3f75f3"
CLAIMS_BLOB="f3a884adc1c82aace81cb73d049ff14720ace862"; FRONTIER_BLOB="4c251be4aa5c355481fe3bcfc71c292fb6389ba4"; ADAPTERS_BLOB="c0ef34e5838e27046a20fed77063593009c56f40"
BOUND=3360778813767800658369
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    req(blob(STATE)==STATE_BLOB,"V34 state blob"); st=json.loads(STATE.read_text()); req(st.get("canonical_sha256_without_this_field")==STATE_CANON and canon(st)==STATE_CANON,"V34 state canon")
    req(blob(CROSS)==CROSS_BLOB,"V34 cross verifier")
    req(blob(MONITOR)==MONITOR_BLOB,"V34 monitor blob"); m=json.loads(MONITOR.read_text()); req(m.get("canonical_sha256_without_this_field")==MONITOR_CANON and canon(m)==MONITOR_CANON,"V34 monitor canon")
    req(blob(RECEIPT)==RECEIPT_BLOB,"V34 receipt blob"); r=json.loads(RECEIPT.read_text()); req(r.get("canonical_sha256_without_this_field")==RECEIPT_CANON and canon(r)==RECEIPT_CANON,"V34 receipt canon")
    req(blob(SYNC)==SYNC_BLOB,"V34 sync verifier")
    req(blob(CLAIMS)==CLAIMS_BLOB and blob(FRONTIER)==FRONTIER_BLOB and blob(ADAPTERS)==ADAPTERS_BLOB,"claim core drift")
    runpy.run_path(str(CROSS),run_name="__main__")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V34_HPADJ11_AUDIT_SYNCED_FULL178_REENTRY","schema")
    req(st["current_exact_frontier"]["authoritative_remaining_strata"]==17128 and st["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"authority")
    req(st["current"]["mainbatch_stop_gate"]=="NONE" and st["current"]["next_exact_route"]=="FULL178_VIA_ACTIVE_178_TD02_AND_SPECIALIST_MONITOR","route")
    req(st["current_exact_frontier"]["v33_hpadj11_replacement_hostile_audited"] is True and st["current_exact_frontier"]["v33_hpadj11_replacement_hostile_audit_review_id"]==5216402010,"V33 audit")
    req(st["current_exact_frontier"]["v34_additional_pruning"]==0,"V34 pruning")
    req(st["firewalls"]["replacement_head_hostile_reaudit_required"] is False and st["firewalls"]["full178_complete"] is False and st["firewalls"]["merge_authorized"] is False,"firewalls")
    print("PASS: Stage32 MAIN V34 V33-audit synchronization retained with zero new pruning")
    print("FULL178=ACTIVE_INCOMPLETE authority=3360778813767800658369 stop_gate=NONE next=178_TD02_specialist")
if __name__=="__main__": main()
