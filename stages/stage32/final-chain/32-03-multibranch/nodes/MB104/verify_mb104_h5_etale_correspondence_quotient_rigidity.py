#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-H5-ETALE-CORRESPONDENCE-QUOTIENT-RIGIDITY-CERTIFICATE.json")

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-UNIFORM-CLOSURE-RESTART-20260917.md":"3e9fb440ea8a9c491ad58c9846d880fbd3373f66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-CLASS3-ROADMAP-20260918.md":"acb5d6b8ec03861fb2fa6e7b96d3f6d2aa612048",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-H5-ARITHMETIC-SELF-CORRESPONDENCE-SOURCE-NOTE-20260918.md":"6b96676a3ed5a72a54affab6afa735376cb19a7e",
}

def blob(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def req(ok,msg):
    if not ok:
        raise SystemExit("FAIL: "+msg)

def main():
    for rel,expected in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(),"missing "+rel)
        req(blob(p)==expected,"source drift "+rel)

    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_H5_ETALE_CORRESPONDENCE_QUOTIENT_RIGIDITY_GATE_V1","schema")
    req(c["status"]=="H5_SHALLOW_FAIL_PARKED_NO_CREDIT","status")

    f=c["current_frontier"]
    req(f["support_mask"]=="000707000f0f","frontier mask")
    req(f["support_type_counts"]==[7,7,0],"type counts")
    req(f["surviving_component_degrees_e"]==[2,4],"e frontier")

    for l in range(1,9):
        req(14*2*l==28*l,f"e2 degree l={l}")
        req(14*4*l==56*l,f"e4 degree l={l}")

    a=c["forward_adapter"]
    req(a["carrier_to_bare_etale_correspondence"]=="PASS_RETAINED","bare forward")
    req(a["packet_to_finite_equivariant_quotient_object"]=="FAIL","packet forward failure")

    amb=c["ambient_correspondence_finiteness"]
    req(amb["fixed_target_only"]=="FAIL","ambient finiteness")

    r=c["reverse_adapter"]
    req(r["status"]=="FAIL","reverse adapter")

    d=c["decision"]
    req(d["shallow_gate"]=="FAIL","H5 fail")
    req(d["roadmap_action"]=="PARK_H5","H5 parked")
    req(d["next_shallow_gate"]=="H6_FINITE_MONODROMY_NIELSEN_PASSPORT","H6 next")
    req(d["finite_degree_window_proved"] is False,"no finite window")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_H5_ETALE_CORRESPONDENCE_QUOTIENT_RIGIDITY_GATE_V1")
    print("H5=FAIL_PARKED bare_correspondence=PASS packet_finite_adapter=FAIL reverse=FAIL")
    print("next=H6_finite_monodromy_nielsen_passport no_credit")

if __name__=="__main__":
    main()
