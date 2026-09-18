#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W16-SOLO-RAMIFICATION-CB-GATE-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_SOLO_RAMIFICATION_CB_GATE_V1","schema")
    req(c["status"]=="W16_SOLO_NARROWED_RAMIFICATION_DESCENT_OPEN_NO_CREDIT","status")

    for l in range(1,80):
        DmK2=336*l*l-224*l+16
        Delta=168*l*l+56*l

        # full conductor package
        full=DmK2-4*Delta
        req(full==-336*l*l-448*l+16,"full conductor discriminant")
        req(full<0,"full conductor wrong side")

        # retained e=2 residual conductor base locus lower bound
        norm_upper=DmK2-4*(84*l*l)
        req(norm_upper==16-224*l,"norm base-locus discriminant upper")
        req(norm_upper<0,"norm base-locus wrong side")

        # target-size ramification candidate
        ram=112*l
        target=DmK2-4*ram
        req(target==336*l*l-672*l+16,"ramification target discriminant")
        if l>=2:
            req(target>0,f"target positivity l={l}")

        # normalization conductor / singular different degrees
        conductor=336*l*l+112*l
        singular_different=conductor+ram
        req(conductor==2*Delta,"conductor degree=2delta")
        req(singular_different==336*l*l+224*l,"singular different degree")

    r=c["universal_ramification_candidate"]
    req(r["degree"]=="56*l","residual map degree")
    req(r["normalization_ramification_degree"]=="112*l","ramification degree")
    req(r["numeric_target_exact"] is True,"exact target")
    req(r["current_surface_lci_descent_available"] is False,"missing descent")

    q=c["conclusion"]
    req(q["W16_closed_negatively"] is False,"W16 remains open")
    req(q["exact_O_l_candidate_exists_on_normalization"] is True,"normalization candidate")
    req(q["exact_O_l_candidate_descended_to_surface_lci"] is False,"no surface scheme")
    req(q["currently_available_surface_canonical_conductor_clusters_are_too_large"] is True,"surface cluster wall")

    req(c["disposition"]=="SURVIVES_ONLY_AS_RAMIFICATION_TO_CB_DESCENT","disposition")
    req(c["solo_comparison"]["suggested_next_active"]=="W16","next active")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_SOLO_RAMIFICATION_CB_GATE_V1")
    print("normalization_ramification=112l exact target")
    print("canonical_singular_different=336l^2+224l quadratic")
    print("W16=ramification_to_CB_descent_open no_credit")

if __name__=="__main__":
    main()
