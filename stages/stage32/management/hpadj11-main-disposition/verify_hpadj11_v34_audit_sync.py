#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
RECEIPT=HERE/"HPADJ11-V34-HOSTILE-AUDIT-PASS-SYNC.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
PREDECESSOR_HEAD="3c0c3b7b288853a2b5d4ebae47cc192d6089cbc6"
PREDECESSOR_STATE_BLOB="d67244969defc7da77dfc431346e0d045da0978d"
PREDECESSOR_STATE_CANON="3ab94343566377b4a5a7646f1334b13968ba15f363c9f63fcb48a66e3b5b9398"
AUDIT_REVIEW_ID=5216402010
CURRENT_MAIN="c6284abbb29930255892d56f800da0ea1e34734b"
RECEIPT_CANON="11dfd2437ee464c80d74984fb3428201020c103ca19b3a435d887b7bcf98e123"
BOUND=3360778813767800658369
def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--audited-v33-root"); a=ap.parse_args()
    r=json.loads(RECEIPT.read_text())
    req(r["schema"]=="STAGE32_MAIN_HPADJ11_V34_HOSTILE_AUDIT_PASS_SYNC_V1","receipt schema")
    req(r.get("canonical_sha256_without_this_field")==RECEIPT_CANON and canon(r)==RECEIPT_CANON,"receipt canonical")
    req(r["predecessor_v33"]["exact_head"]==PREDECESSOR_HEAD,"predecessor head")
    req(r["predecessor_v33"]["main_state_blob_sha1"]==PREDECESSOR_STATE_BLOB,"predecessor state blob")
    req(r["predecessor_v33"]["main_state_canonical_sha256"]==PREDECESSOR_STATE_CANON,"predecessor state canonical")
    au=r["hostile_audit"]
    req(au["audited_exact_head"]==PREDECESSOR_HEAD and au["review_id"]==AUDIT_REVIEW_ID and au["status"]=="PASS","audit identity")
    req(au["merge_ready_freshness"]=="CLEAR" and au["current_repository_main_at_audit"]==CURRENT_MAIN,"audit freshness")
    p=r["promoted_authority"]
    req(p["remaining_strata"]==17128 and p["remaining_terminals_upper_bound"]==BOUND,"authority changed")
    req(p["additional_pruning_added_by_sync"]==0 and p["replacement_head_hostile_reaudit_required"] is False,"sync semantics")
    live=r["live_specialist_refresh"]
    req(live["lane_178"]["semantic_leaf"]=="TD02_GRF04_BOUNDED_PROBE" and live["lane_178"]["audited_main_handoff_ready"] is False and live["lane_178"]["main_credit"]==0,"178 live disposition")
    req(live["ex5"]["same_mathematical_bound_as_v33"] is True and live["ex5"]["additional_main_credit"]==0,"EX5 duplicate credit")
    req(r["claim_sync"]["claim_core_mutated"] is False and r["claim_sync"]["full178_status"]=="ACTIVE_INCOMPLETE","claim sync")
    if a.audited_v33_root:
        pth=Path(a.audited_v33_root)/"stages/stage32/MAIN-STATE.json"
        req(pth.is_file() and blob(pth)==PREDECESSOR_STATE_BLOB,"audited V33 state blob")
        old=json.loads(pth.read_text()); req(old.get("canonical_sha256_without_this_field")==PREDECESSOR_STATE_CANON and canon(old)==PREDECESSOR_STATE_CANON,"audited V33 canonical")
        req(old["current"]["mainbatch_stop_gate"]=="REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED","audited V33 gate")
        req(old["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"audited V33 bound")
    cur=json.loads(STATE.read_text())
    req(cur["schema"]=="STAGE32_MAIN_COMPACT_STATE_V34_HPADJ11_AUDIT_SYNCED_FULL178_REENTRY","current schema")
    req(cur["current"]["mainbatch_stop_gate"]=="NONE","current stop gate")
    req(cur["firewalls"]["replacement_head_hostile_reaudit_required"] is False,"current audit firewall")
    req(cur["current_exact_frontier"]["authoritative_remaining_terminals"]==BOUND,"current bound")
    req(cur["authority_sync"]["v33_hpadj11_replacement_hostile_audit_review_id"]==AUDIT_REVIEW_ID,"current audit review")
    req(cur["current_exact_frontier"]["v34_additional_pruning"]==0,"current sync pruning")
    print("PASS: Stage32 MAIN V34 HPADJ11 V33 hostile-audit PASS synchronization")
    print("PASS: additional_pruning=0 stop_gate=NONE FULL178=ACTIVE_INCOMPLETE TD02=unconsumed merge_authorized=false")
if __name__=="__main__": main()
