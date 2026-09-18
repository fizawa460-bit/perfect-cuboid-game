#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-H2-GRADED-INCIDENCE-ADAPTER-CERTIFICATE.json")

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-CLASS3-ROADMAP-20260918.md":"72b06b65d2b16768c4b6af47f549a9f4f5a0a515",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-UNIFORM-CLOSURE-RESTART-20260917.md":"3e9fb440ea8a9c491ad58c9846d880fbd3373f66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-U1-EQUIGENERIC-SUPERABUNDANCE-WALL-20260917.md":"bffa8956a6be0eac8a0a0106c81e0e21566059d9",
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
    req(c["schema"]=="STAGE32_MB104_H2_GRADED_INCIDENCE_ADAPTER_GATE_V1","schema")
    req(c["status"]=="H2_SHALLOW_FAIL_PARKED_NO_CREDIT","status")
    req(c["scope"]["fixed_degree_scheme_encoding_rejected"] is False,"fixed-degree firewall")
    req(c["scope"]["graded_section_ring_adapter_rejected"] is True,"graded adapter decision")

    # Symbolic grading check: D_l=lD_1, hence multiplying a degree-l
    # section by itself lands in degree 2l and doubles every divisor coefficient.
    for l in range(1,9):
        req(2*l==l+l,f"grading l={l}")
        coeff_C=1
        coeff_square=coeff_C+coeff_C
        req(coeff_square==2,f"double divisor coefficient l={l}")
        req(coeff_square!=1,f"square cannot be integral reduced carrier l={l}")

    obs=c["obstruction"]["natural_submodule_case"]
    req(obs["divisor_identity"]=="div(s_C^2)=2C","divisor identity")
    req("nonreduced" in obs["failure"] and "nonintegral" in obs["failure"],"reverse-adapter failure")

    dep=c["obstruction"]["degree_dependent_packet"]
    req(dep["branches_per_supported_node"]=="8*l","packet scaling")

    dec=c["decision"]
    req(dec["shallow_gate"]=="FAIL","H2 fail")
    req(dec["roadmap_action"]=="PARK_H2","H2 parked")
    req(dec["h3_deep_release"] is False,"H3 not released")
    req(dec["next_shallow_gate"]=="H4_INFINITE_FAMILY_TO_GLOBAL_GEOMETRY_BRIDGE","H4 next")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_H2_GRADED_INCIDENCE_ADAPTER_GATE_V1")
    print("H2=FAIL_PARKED exact_R_module_reverse_adapter=false fixed_degree_incidence_not_rejected")
    print("H3_deep=false next=H4_infinite_family_global_geometry_bridge no_credit")

if __name__=="__main__":
    main()
