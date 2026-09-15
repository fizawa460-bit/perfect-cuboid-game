#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
STATE=HERE/"MAIN-STATE.json"; CROSS=HERE/"proof/verify_cross_lane_demands.py"; RECEIPT=HERE/"management/hpadj11-main-disposition/HPADJ11-V33-MAIN-BOUND-REPLACEMENT.json"; CLAIMS=HERE/"proof/CLAIM-REGISTRY.json"; FRONTIER=HERE/"proof/ACTIVE-FRONTIER.json"; ADAPTERS=HERE/"proof/LANE-ADAPTERS.json"
STATE_BLOB="d67244969defc7da77dfc431346e0d045da0978d"; STATE_CANON="3ab94343566377b4a5a7646f1334b13968ba15f363c9f63fcb48a66e3b5b9398"; CROSS_BLOB="a07386860a0e7576511f7c87954b25660659e02c"; RECEIPT_BLOB="6e2328f40bea32daf9ccee4c921700432dc6e369"; RECEIPT_CANON="124e038979b8995e9a642d868865eeb34d340d3a320d2b4fe4a53273a7c5840e"
def req(x,m):
    if not x: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
    req(blob(STATE)==STATE_BLOB,"state blob"); s=json.loads(STATE.read_text()); req(s.get("canonical_sha256_without_this_field")==STATE_CANON and canon(s)==STATE_CANON,"state canonical")
    req(blob(CROSS)==CROSS_BLOB,"cross blob"); req(blob(RECEIPT)==RECEIPT_BLOB,"receipt blob"); r=json.loads(RECEIPT.read_text()); req(r.get("canonical_sha256_without_this_field")==RECEIPT_CANON and canon(r)==RECEIPT_CANON,"receipt canonical")
    req(blob(CLAIMS)=="f3a884adc1c82aace81cb73d049ff14720ace862","claims changed"); req(blob(FRONTIER)=="4c251be4aa5c355481fe3bcfc71c292fb6389ba4","frontier changed"); req(blob(ADAPTERS)=="c0ef34e5838e27046a20fed77063593009c56f40","adapters changed")
    runpy.run_path(str(CROSS),run_name="__main__")
    req(s["current_exact_frontier"]["authoritative_remaining_terminals"]==3360778813767800658369,"authority"); req(s["firewalls"]["replacement_head_hostile_reaudit_required"] is True,"reaudit"); req(s["firewalls"]["full178_complete"] is False and s["firewalls"]["merge_authorized"] is False,"firewalls")
    print("PASS: Stage32 MAIN V33 HPADJ11 bound retained pending hostile re-audit")
if __name__=="__main__": main()
