#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
RECEIPT=HERE/"HPADJ11-V33-MAIN-BOUND-REPLACEMENT.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
PRED_HEAD="626359a9f981313f40bbed71129f17b664e2bd49"
PRED_STATE_BLOB="6fdcd15090d7951467675e0f732b6ce54c09d69d"
PRED_STATE_CANON="7c318668df1c9fe5f1670ed52bedffed7a21c5b2f0d0fbbffc6f1fa73b5bfa47"
RECEIPT_CANON="124e038979b8995e9a642d868865eeb34d340d3a320d2b4fe4a53273a7c5840e"
OLD=3453268626299532038131; NEW=3360778813767800658369
def req(x,msg):
    if not x: raise SystemExit("FAIL: "+msg)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--predecessor-v32-root"); ap.add_argument("--producer-root"); a=ap.parse_args()
    r=json.loads(RECEIPT.read_text()); req(r.get("canonical_sha256_without_this_field")==RECEIPT_CANON and canon(r)==RECEIPT_CANON,"receipt canonical")
    req(r["predecessor_v32"]["exact_head"]==PRED_HEAD and r["predecessor_v32"]["main_state_blob_sha1"]==PRED_STATE_BLOB,"predecessor identity")
    p=r["producer"]; req(p["audited_exact_head"]=="1c694f6650125a8fb0121925beff7f800b5d6283" and p["hostile_audit_review_id"]==5216065509,"producer audit")
    req(p["checkpoint_blob_sha1"]=="81abb4aa2c626ec2a77b5b1e751e99f4299c55ba" and p["checkpoint_canonical_sha256"]=="0eff74f8adb64b3ecd8d2a3959d55686a64b57b52bcf6baabe62ac184cc1760d","producer checkpoint lock")
    c=r["composition"]; req(c["predecessor_upper_bound"]==OLD and c["producer_upper_bound"]==NEW and c["promoted_upper_bound"]==min(OLD,NEW),"min composition")
    req(c["certified_tightening"]==OLD-NEW,"tightening")
    req(c["exact_incremental_rejected_set_claimed"] is False and c["additive_subtraction_performed"] is False and c["td01_recharged"] is False and c["hpadj10_recharged"] is False and c["double_charge"] is False,"no double charge")
    req(r["claim_sync"]["claim_core_mutated"] is False and r["claim_sync"]["full178_status"]=="ACTIVE_INCOMPLETE","claim sync")
    if a.predecessor_v32_root:
        q=Path(a.predecessor_v32_root)/"stages/stage32/MAIN-STATE.json"; req(q.is_file() and blob(q)==PRED_STATE_BLOB,"V32 state blob"); o=json.loads(q.read_text()); req(o.get("canonical_sha256_without_this_field")==PRED_STATE_CANON and canon(o)==PRED_STATE_CANON,"V32 state canonical"); req(o["current"]["mainbatch_stop_gate"]=="NONE" and o["current_exact_frontier"]["authoritative_remaining_terminals"]==OLD,"V32 authority")
    if a.producer_root:
        rr=Path(a.producer_root); cp=rr/p["checkpoint_path"]; rf=rr/p["refiner_path"]; req(cp.is_file() and blob(cp)==p["checkpoint_blob_sha1"],"producer checkpoint blob"); co=json.loads(cp.read_text()); req(co.get("canonical_sha256_without_this_field")==p["checkpoint_canonical_sha256"] and canon(co)==p["checkpoint_canonical_sha256"],"producer checkpoint canonical"); req(rf.is_file() and blob(rf)==p["refiner_blob_sha1"],"producer refiner blob")
    st=json.loads(STATE.read_text()); req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V33_HPADJ11_BOUND_CONSUMED_PENDING_REAUDIT","state schema"); req(st["current_exact_frontier"]["authoritative_remaining_terminals"]==NEW,"state authority"); req(st["current"]["mainbatch_stop_gate"]=="REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED","state stop gate")
    print("PASS: Stage32 MAIN V33 HPADJ11 same-character bound replacement")
    print(f"PASS: authority={NEW} tightening={OLD-NEW} additive_subtraction=false double_charge=false")
if __name__=="__main__": main()
