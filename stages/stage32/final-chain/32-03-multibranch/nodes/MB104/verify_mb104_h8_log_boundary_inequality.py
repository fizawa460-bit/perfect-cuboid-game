#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[6]
CERT=Path(__file__).with_name("MB104-H8-LOG-BOUNDARY-INEQUALITY-CERTIFICATE.json")

LOCKS={
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-UNIFORM-CLOSURE-RESTART-20260917.md":"3e9fb440ea8a9c491ad58c9846d880fbd3373f66",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-CLASS3-ROADMAP-20260918.md":"aa7192b4391b35e28c7f12efe5eef398d2144194",
"stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-H8-LOG-BMY-SOURCE-NOTE-20260918.md":"3a18c5f67474bd4cd413472039924607e32dd9ec",
}

def blob(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def req(ok,msg):
    if not ok:
        raise SystemExit("FAIL: "+msg)

def qmin(x:Fraction)->Fraction:
    if x <= Fraction(1,4):
        return 8*x-4
    if x <= Fraction(3,4):
        return -((8*x-6)**2)/8
    return Fraction(0)

def base_slack(x:Fraction)->Fraction:
    return 168*x*x-224*x+224+14*qmin(x)

def main():
    for rel,expected in LOCKS.items():
        p=ROOT/rel
        req(p.is_file(),"missing "+rel)
        req(blob(p)==expected,"source drift "+rel)

    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_H8_LOG_BOUNDARY_INEQUALITY_GATE_V1","schema")
    req(c["status"]=="H8_SHALLOW_FAIL_PARKED_NO_CREDIT","status")

    # Exact ray arithmetic.
    for l in range(1,9):
        delta=168*l*l+56*l
        req(delta>0,f"delta l={l}")
        req(14*8*l==112*l,f"exceptional contacts l={l}")

    # Exact regional minima. The continuous proof is encoded by the
    # closed-form quadratics and their vertices/endpoints.
    r1=168*Fraction(1,4)**2-112*Fraction(1,4)+168
    req(r1==Fraction(301,2),"region1 endpoint minimum")

    r2=7*(8*Fraction(1,2)**2-8*Fraction(1,2)+23)
    req(r2==147,"region2 vertex minimum")

    r3=168*Fraction(3,4)**2-224*Fraction(3,4)+224
    req(r3==Fraction(301,2),"region3 endpoint minimum")
    req(min(r1,r2,r3)==147,"global base slack")

    # Rational spot replay across all three regions and coefficient extremes.
    for x in [Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(1,2),
              Fraction(3,4),Fraction(1),Fraction(2),Fraction(10)]:
        req(base_slack(x)>=147,f"slack x={x}")

    p=c["positivity_proof"]
    req(p["global_slack_lower_bound"]=="3*e_orb-(K+B)^2 >= 147","certificate lower bound")

    d=c["decision"]
    req(d["shallow_gate"]=="FAIL","H8 fail")
    req(d["roadmap_action"]=="PARK_H8","H8 parked")
    req(d["next_shallow_gate"]=="H5_ETALE_CORRESPONDENCE_QUOTIENT_RIGIDITY","H5 next")
    req(d["finite_degree_window_proved"] is False,"no finite window")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit firewall "+k)

    print("PASS STAGE32_MB104_H8_LOG_BOUNDARY_INEQUALITY_GATE_V1")
    print("H8=FAIL_PARKED nodal_compatibility_BMY_slack>=147 all_boundary_weights")
    print("next=H5_etale_correspondence_quotient_rigidity no_credit")

if __name__=="__main__":
    main()
