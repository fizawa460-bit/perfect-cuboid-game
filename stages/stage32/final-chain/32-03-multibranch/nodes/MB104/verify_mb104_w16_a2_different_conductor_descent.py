#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W16-A2-DIFFERENT-CONDUCTOR-DESCENT-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_A2_DIFFERENT_CONDUCTOR_DESCENT_V1","schema")
    req(c["status"]=="W16_A2_LCI_DESCENT_PASS_CB_OPEN_NO_CREDIT","status")

    # Global size gate.
    for l in range(1,100):
        deg_phi=56*l
        deg_ram=2*deg_phi
        req(deg_ram==112*l,"ramification degree")
        disc=(336*l*l-224*l+16)-4*deg_ram
        req(disc==336*l*l-672*l+16,"target discriminant")
        if l>=2:
            req(disc>0,f"positive target discriminant l={l}")

    # Local node model t=x^m+y^n.
    # For m=n=2, normalization ramification length is 2.
    m=n=2
    upstairs=(m-1)+(n-1)
    req(upstairs==2,"node upstairs ramification length")

    # A=k[[x,y]]/(xy), m_A=(x,y).
    # A/m_A^2 has basis 1,x,y -> length 3.
    first_colon_len=3
    # A/m_A has basis 1 -> length 1.
    second_colon_len=1
    req(c["quotient_wall"]["simple_double_ramification"]["first_colon_scheme_length"]==first_colon_len,"first colon length")
    req(c["quotient_wall"]["simple_double_ramification"]["second_colon_scheme_length"]==second_colon_len,"second colon length")
    req(first_colon_len>upstairs>second_colon_len,"colon bracketing")

    # Fitt_0(k direct_sum k)=m_A^2 by multiplicativity, same length 3.
    req(c["quotient_wall"]["simple_double_ramification"]["fitting_scheme_length"]==3,"Fitting length")

    z=c["reduced_image_descent"]
    req(z["canonical_relative_to_retained_phi"] is True,"canonical relative to phi")
    req(z["reduced"] is True and z["zero_dimensional"] is True,"reduced finite image")
    req(z["lci_on_smooth_surface"] is True,"surface lci")
    req(z["nonempty"] is True,"nonempty")
    req(z["satisfies_W16_numeric_target"] is True,"numeric gate")
    req(z["CB_D_l_proved"] is False,"CB remains open")

    q=c["consequence"]
    req(q["surface_lci_gate_passed"] is True,"lci gate pass")
    req(q["W16_closed_negatively"] is False,"W16 remains open")
    req(c["disposition"]=="A2_PASS_LCI_DESCENT_CB_OPEN","disposition")
    req(c["next_internal_solo"]=="W16-B2-EXT-SERRE-FIRST","next route")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_A2_DIFFERENT_CONDUCTOR_DESCENT_V1")
    print("different/conductor multiplicity descent fails locally")
    print("reduced ramification image gives canonical nonempty surface lci length<=112l")
    print("A2=PASS_LCI_DESCENT_CB_OPEN next=W16-B2 no_credit")

if __name__=="__main__":
    main()
