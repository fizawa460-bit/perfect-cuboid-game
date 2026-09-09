#!/usr/bin/env python3
"""Verify Goal4BU: three source-known reservoirs and quadratic reciprocity boundary."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART=P("stages/stage35-ex/35ex-35/goal4bu-three-source-reservoir-reciprocity-coupling.json")
SRC=P("stages/stage35-ex/35ex-35/goal4bu-three-source-reservoir-reciprocity-coupling-source-lock.md")
BT=P("stages/stage35-ex/35ex-35/goal4bt-master-hypotenuse-bridge-reservoir-source-reclassification.json")
EX09=P("stages/stage35-ex/35ex-09/bridge-squareclass-graph.md")
EX10=P("stages/stage35-ex/35ex-10/split-prime-obstruction.md")
EX11=P("stages/stage35-ex/35ex-11/reciprocity-routing-and-local-route-freeze.md")
STATE=P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED="1efe64e90d160d040df403589abc7b14c966ebfdfb33e4defbdb9cf620a93a7e"
SRC_BLOB="d6ce919c9a8867f77008e733e4701924ae49d437"
BT_BLOB="50970a346f7d85f2da535329fda8218e52da0adb"
EX09_BLOB="1cbd3fdf4891ffabc1911ae19632f593a87b5d14"
EX10_BLOB="a5761a883b3c50bbdad6a357241bba4b61e71c8a"
EX11_BLOB="fc186e1a0b2134840135e67c29adb0e6bd9bf1a9"
V74="STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def checkcanon(obj: dict) -> None:
    x=dict(obj); got=x.pop("canonical_sha256")
    calc=hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    assert got==calc==EXPECTED,(got,calc)

def v2(n:int)->int: return (n & -n).bit_length()-1

def pf(n:int)->list[int]:
    n=abs(n); out=[]; d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d=3 if d==2 else d+2
    if n>1:out.append(n)
    return out

def leg(a:int,p:int)->int:
    a%=p; assert p>2 and a
    z=pow(a,(p-1)//2,p); assert z in (1,p-1)
    return 1 if z==1 else -1

for path,expected in ((SRC,SRC_BLOB),(BT,BT_BLOB),(EX09,EX09_BLOB),(EX10,EX10_BLOB),(EX11,EX11_BLOB)):
    assert blob(path)==expected,(path,blob(path),expected)

state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["last_audited_authority"]["hostile_review_id"]==5142248509
assert state["claims"]["E1_proved"] is False and state["claims"]["stage35_closed"] is False

bt=json.loads(BT.read_text())
assert bt["canonical_sha256"]=="1eba0637995f9a3aa1e605fd7c42fb4310a51eadfe46cf459e50d81257aeb66e"
assert bt["result"]["bridge_reservoir_e_source_computable"] is True
assert bt["result"]["reopen_gate_B_triggered"] is True

art=json.loads(ART.read_text()); checkcanon(art)
assert art["stacked_parent"]["exact_head_sha"]=="d2a65383b141824321c6cc0bf6b594a59c03957c"
assert art["stacked_parent"]["aggregate_run"]==34400316014
assert art["stacked_parent"]["aggregate_current_job"]==102631709439
assert art["source_locks"]["goal4bu_source"]["blob_sha1"]==SRC_BLOB
assert art["source_known_triple"]["pairwise_coprime_under_E1_counterexample"] is True
assert art["quadratic_sieve"]["numerator_identity"]=="K*(p*q)=W1*V1"
assert art["quadratic_sieve"]["composite_Jacobi_compression_stronger_than_primewise"] is False
assert art["reciprocity_boundary"]["universal_bad_split_prime_in_three_source_channels"] is False
assert art["reciprocity_boundary"]["fixed_global_Jacobi_sign_forced_by_current_graph"] is False
assert art["reciprocity_boundary"]["cross_reservoir_orientation_bits_coupled_by_quadratic_reciprocity"] is False
assert art["reciprocity_boundary"]["stronger_reciprocity_impossibility_claimed"] is False
assert art["result"]["three_source_known_reservoirs_exposed"] is True
assert art["result"]["quadratic_reciprocity_universal_close_obtained"] is False
assert art["next"]["unit"]=="35EX-35_GOAL4BV_SOURCE_KNOWN_BRIDGE_QUARTIC_ORIENTATION_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

def verify(a,b,m,n,expected_branch):
    U1,V1,W1=a*a-b*b,2*a*b,a*a+b*b
    U2,V2,W2=m*m-n*n,2*m*n,m*m+n*n
    M=(V1*U2)**2+(U1*V2)**2; S=math.isqrt(M); assert S*S==M
    c=math.gcd(U1,U2); p=math.gcd(W1,V2); q=math.gcd(V1,V2)
    H=S//(c*q); assert H*c*q==S; e=math.gcd(c,H)
    D,T=U1//c,U2//c; K=(W1//p)*(V1//q)
    A=(V1//q)*T; B=D*(V2//q)
    assert math.gcd(A,B)==math.gcd(A,H)==math.gcd(B,H)==1
    branch="L" if v2(V1)<v2(V2) else "R"; assert branch==expected_branch
    if branch=="L":
        assert D*V2%(2*p*q)==0; cross=D*V2//(2*p*q); assert B==2*p*cross
        bad_cross=[ell for ell in pf(cross) if ell%4==1 and leg(K,ell)==-1]
        bad_T=[ell for ell in pf(T) if ell%4==1 and leg(p*q,ell)==-1]
        bad_e=[ell for ell in pf(e) if ell>2 and leg(p*q,ell)==-1]
    else:
        assert D*V2%(p*q)==0; cross=D*V2//(p*q); assert B==p*cross
        bad_cross=[ell for ell in pf(cross) if ell%4==1 and leg(2*K,ell)==-1]
        bad_T=[ell for ell in pf(T) if ell%4==1 and leg(2*p*q,ell)==-1]
        bad_e=[ell for ell in pf(e) if ell>2 and leg(2*p*q,ell)==-1]
    assert math.gcd(cross,T)==math.gcd(cross,e)==math.gcd(T,e)==1
    assert not bad_cross and not bad_T and not bad_e
    assert K*p*q==W1*V1
    return locals()

L=verify(13,4,96,91,"L")
assert (L["U1"],L["V1"],L["W1"])==(153,104,185)
assert (L["U2"],L["V2"],L["W2"])==(935,17472,17497)
assert (L["M"],L["S"],L["c"],L["p"],L["q"],L["H"],L["e"],L["T"],L["cross"])==(7155539400256,2674984,17,1,104,1513,17,55,756)
assert leg(L["p"]*L["q"],5)==1 and leg(L["p"]*L["q"],17)==1

R=verify(88,7,98,37,"R")
assert (R["U1"],R["V1"],R["W1"])==(7695,1232,7793)
assert (R["U2"],R["V2"],R["W2"])==(8235,7252,10973)
assert (R["M"],R["S"],R["c"],R["p"],R["q"],R["H"],R["e"],R["T"],R["cross"])==(3217033617210000,56718900,135,1,28,15005,5,61,14763)
assert leg(2*R["K"],37)==1 and leg(2*R["p"]*R["q"],61)==1 and leg(2*R["p"]*R["q"],5)==1

src=SRC.read_text()
for marker in ("(BU-COPRIME)","(BU-L)","(BU-R)","(BU-KP)","(BU-WIT-L)","(BU-WIT-R)","(BU-VERDICT)","35EX-35_GOAL4BV_SOURCE_KNOWN_BRIDGE_QUARTIC_ORIENTATION_PREFLIGHT"):
    assert marker in src,marker

print("STAGE35_EX_GOAL4BU_THREE_SOURCE_RESERVOIR_RECIPROCITY=PASS")
print("three_source_known_reservoirs=true")
print("universal_bad_split_prime_in_triple=false")
print("quadratic_reciprocity_universal_close=false")
print("next=Goal4BV_source_known_bridge_quartic_orientation")
print("canonical_sha256="+EXPECTED)
