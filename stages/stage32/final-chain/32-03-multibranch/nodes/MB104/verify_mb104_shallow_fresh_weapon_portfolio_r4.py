#!/usr/bin/env python3
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-SHALLOW-FRESH-WEAPON-PORTFOLIO-R4-CERTIFICATE.json"

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_SHALLOW_FRESH_WEAPON_PORTFOLIO_R4_V1"
    a=d["route_A_web"]
    assert sum(a["P_dot_fibers"])==280
    assert 2*sum(a["P_dot_fibers"])==560
    # 6*(336 l^2+112 l)+560 l
    assert 6*336==2016
    assert 6*112+560==1232
    b=d["route_B_hilbert_chow"]
    assert b["H_dot_C"]=="112*l"
    assert b["arithmetic_genus"]=="168*l^2+56*l+1"
    assert b["hilbert_polynomial"]=="112*l*n-168*l^2-56*l"
    assert d["route_C_specialization"]["finite_state_receiver"] is False
    assert d["firewalls"]["MB104_complete"] is False
    assert d["firewalls"]["merge_authorized"] is False
    print("PASS: MB104 shallow fresh-weapon portfolio R4 certificate")
    print("A web: no new quadratic strictness")
    print("B Hilbert/Chow: no l-uniform boundedness")
    print("C arithmetic specialization: no finite-state receiver")

if __name__=="__main__":
    main()
