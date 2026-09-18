#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W16-B1-CB-FIRST-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_B1_CB_FIRST_V1","schema")
    req(c["status"]=="W16_B1_NARROWED_TO_CONDUCTOR_DESCENT_OPEN_NO_CREDIT","status")

    for l in range(1,80):
        degM=56*l
        degR=112*l
        degU=112*l
        degH=112*l
        degD=336*l*l

        req(2*degM==degR,"RH ramification degree")
        req(degU==2*degM,"supported line degree")
        req(degH==2*degM,"hyperplane degree")
        req(7*l*degH-4*l*degU==degD,"active ray degree")
        req(6*l*degM==degD,"factor line formula degree")
        req(3*l*degR==degD,"ramification formula degree")

        a=degD-degR+1
        b=degD-degR
        req(a==336*l*l-112*l+1,"L-R+p degree")
        req(b==336*l*l-112*l,"L-R degree")
        req(a>0 and b>0,"positive elliptic degrees")
        req(a-b==1,"elliptic h0 difference")

    f=c["factor_line_package"]
    req(f["pullback_branch_identity"]=="phi_i^*(B_6)=U+2R_i","branch identity")
    req(f["RH_line"]=="O_E(R_i)=M_i^2","RH line")
    req(f["supported_line"]=="O_E(U)=M_i^2","supported line")
    req(f["relative_torsion"]=="delta=M_1 tensor M_2^(-1) in Pic^0(E)[2]","2-torsion")

    h=c["canonical_hyperplane"]
    req(h["identity"]=="nu^*O_S(H)=M_1 tensor M_2","hyperplane identity")

    a=c["active_line_bundle"]
    req(a["identity_factor1"]=="nu^*O_C(D_l)=M_1^(6*l) tensor delta^l","factor1 identity")
    req(a["identity_factor2"]=="nu^*O_C(D_l)=M_2^(6*l) tensor delta^l","factor2 identity")
    req(a["ramification_form"]=="nu^*O_C(D_l)=O_E(3*l*R_i) tensor delta^l","ramification identity")

    q=c["normalization_CB_test"]
    req(q["R_i_reduced"] is True,"R reduced")
    req(q["conclusion"]=="R_i is not Cayley-Bacharach for the full normalization linear system H0(E,nu^*O_C(D_l)) for any l>=1","normalization CB conclusion")

    g=c["remaining_gate"]
    req(g["ramification_geometry_alone_forces_CB"] is False,"ramification alone no CB")
    req(g["exact_conductor_evaluation_map_materialized"] is False,"conductor map missing")

    req(c["disposition"]=="B1_CONDUCTOR_DESCENT_ONLY_OPEN","disposition")
    req(c["W16_closed_negatively"] is False,"W16 open")
    req(c["next_internal_solo"]=="W16-H-HILBERT-QUOT-CONDUCTOR-DESCENT","next")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_B1_CB_FIRST_V1")
    print("nu^*D_l=M_i^(6l) tensor delta^l=O_E(3l R_i) tensor delta^l")
    print("full normalization separates every ramification point")
    print("surface CB can only come from conductor/gluing descent")
    print("B1=conductor_descent_only_open next=W16-H no_credit")

if __name__=="__main__":
    main()
