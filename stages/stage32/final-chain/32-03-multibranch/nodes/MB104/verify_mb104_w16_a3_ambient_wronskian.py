#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W16-A3-AMBIENT-WRONSKIAN-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_A3_AMBIENT_WRONSKIAN_V1","schema")
    req(c["status"]=="W16_A3_CLOSED_NEGATIVE_AS_INDEPENDENT_DIFFERENTIAL_ROUTE_NO_CREDIT","status")

    for l in range(1,100):
        degL=112*l
        degphi=56*l
        degB=degL-degphi
        degR=2*degphi
        degW=2*degL
        req(degB==56*l,"base divisor degree")
        req(degR==112*l,"ramification degree")
        req(2*degB+degR==degW==224*l,"normalization Wronskian split")

        Delta=168*l*l+56*l
        conductor=2*Delta
        total=336*l*l+336*l
        req(conductor==336*l*l+112*l,"conductor")
        req(conductor+2*degB+degR==total,"singular Wronskian degree")

    a=c["favorable_literal_pencil_test"]
    req(a["wronskian_degree"]=="224*l","wronskian degree")
    req(a["factorization"]=="div(W)=2*B+R_phi","factorization")

    q=c["route_wall"]
    req(q["full_ambient_differential_scheme_linear_size"] is False,"full scheme not linear")
    req(q["full_ambient_differential_scheme_has_quadratic_conductor_excess"] is True,"quadratic excess")
    req(q["subtracting_conductor_and_base_recovers_ramification"] is True,"subtraction recovers R")
    req(q["subtraction_preserves_automatic_determinantal_CB"] is False,"CB not preserved")
    req(q["reduced_image_after_subtraction"]=="exactly returns to A2-type Z_red and its unresolved CB(|D_l|) gate","A2 return")

    req(c["disposition"]=="A3_CLOSED_NEGATIVE_ABSORBED_BY_A2_PLUS_B1","disposition")
    req(c["W16_closed_negatively"] is False,"W16 remains open")
    req(c["next_internal_solo"]=="W16-A1-DIRECT-DESCENT","next")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_A3_AMBIENT_WRONSKIAN_V1")
    print("normalization: div(W)=2B+R_phi with degrees 112l+112l")
    print("singular carrier: conductor adds 336l^2+112l")
    print("A3=closed_negative_as_independent_route next=W16-A1 no_credit")

if __name__=="__main__":
    main()
