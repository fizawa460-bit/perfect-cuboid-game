#!/usr/bin/env python3
"""Verify Goal4BT: Master hypotenuse makes the bridge reservoir source-known."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bt-master-hypotenuse-bridge-reservoir-source-reclassification.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bt-master-hypotenuse-bridge-reservoir-source-reclassification-source-lock.md")
EX02 = P("stages/stage35-ex/35ex-02/canonical-gcd-and-2adic-lemma.md")
EX08 = P("stages/stage35-ex/35ex-08/hypotenuse-bridge-triple.md")
EX10 = P("stages/stage35-ex/35ex-10/split-prime-obstruction.md")
EX11 = P("stages/stage35-ex/35ex-11/reciprocity-routing-and-local-route-freeze.md")
BS = P("stages/stage35-ex/35ex-35/goal4bs-post-boundary-derived-backup-parking-audit-source-lock.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "1eba0637995f9a3aa1e605fd7c42fb4310a51eadfe46cf459e50d81257aeb66e"
SRC_BLOB = "327133a633d6423f3979d29e91fb9d9d5b58e9a5"
EX02_BLOB = "9df24c83ed23e5d13397a2971706a5ac7def9461"
EX08_BLOB = "15c53ccd5317b6251a70a5f4bf78051a3bb4af1f"
EX10_BLOB = "a5761a883b3c50bbdad6a357241bba4b61e71c8a"
EX11_BLOB = "fc186e1a0b2134840135e67c29adb0e6bd9bf1a9"
BS_BLOB = "374a30ad8b69610120ee79ab40a8a517814a091c"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)

def v2(n: int) -> int:
    return (n & -n).bit_length() - 1

def pf(n: int) -> list[int]:
    n = abs(n); out=[]; d=2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0: n //= d
        d = 3 if d == 2 else d + 2
    if n > 1: out.append(n)
    return out

def legendre(a: int, ell: int) -> int:
    a %= ell
    assert ell > 2 and a != 0
    z = pow(a, (ell-1)//2, ell)
    assert z in (1, ell-1)
    return 1 if z == 1 else -1

for path, expected in ((SRC,SRC_BLOB),(EX02,EX02_BLOB),(EX08,EX08_BLOB),(EX10,EX10_BLOB),(EX11,EX11_BLOB),(BS,BS_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state=json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

ex10=EX10.read_text()
assert "The bridge divisor `e` is not source-known" in ex10
assert "e = gcd(c,H)" in EX08.read_text()
assert "e=gcd(c,H)" in EX11.read_text() or "e = gcd(c,H)" in EX11.read_text()

art=json.loads(ART.read_text()); checkcanon(art)
assert art["reopen_gate"]["gate"] == "B.NEW_SOURCE_FIXED_E1_INVARIANT"
assert art["reopen_gate"]["satisfied"] is True
assert art["source_computation"]["E1_assumption_needed_for_H"] is False
assert art["source_computation"]["E1_assumption_needed_for_e"] is False
assert art["result"]["new_source_fixed_E1_invariant_obtained"] is True
assert art["result"]["source_only_bridge_kill_predicate_proved"] is True
assert art["result"]["universal_E1_proof_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BU_THREE_SOURCE_RESERVOIR_RECIPROCITY_COUPLING_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

def verify_witness(a,b,m,n,expected_branch):
    assert math.gcd(a,b)==1 and (a-b)%2==1
    assert math.gcd(m,n)==1 and (m-n)%2==1
    U1,V1,W1=a*a-b*b,2*a*b,a*a+b*b
    U2,V2,W2=m*m-n*n,2*m*n,m*m+n*n
    c=math.gcd(U1,U2); p=math.gcd(W1,V2); q=math.gcd(V1,V2)
    raw1,raw2=V1*U2,U1*V2
    M=raw1*raw1+raw2*raw2; S=math.isqrt(M); assert S*S==M
    assert math.gcd(raw1,raw2)==c*q and S%(c*q)==0
    H=S//(c*q)
    A=(V1//q)*(U2//c); B=(U1//c)*(V2//q)
    assert math.gcd(A,B)==1 and A*A+B*B==H*H
    e=math.gcd(c,H)
    branch="L" if v2(V1)<v2(V2) else "R"; assert branch==expected_branch
    D,T=U1//c,U2//c; K=(W1//p)*(V1//q)
    if branch=="L":
        cross=D*V2//(2*p*q)
        old_cross_bad=any(ell%4==1 and legendre(K,ell)==-1 for ell in pf(cross) if ell>2)
        old_T_bad=any(ell%4==1 and legendre(p*q,ell)==-1 for ell in pf(T) if ell>2)
        bridge_bad=[ell for ell in pf(e) if ell>2 and legendre(p*q,ell)==-1]
    else:
        cross=D*V2//(p*q)
        old_cross_bad=any(ell%4==1 and legendre(2*K,ell)==-1 for ell in pf(cross) if ell>2)
        old_T_bad=any(ell%4==1 and legendre(2*p*q,ell)==-1 for ell in pf(T) if ell>2)
        bridge_bad=[ell for ell in pf(e) if ell>2 and legendre(2*p*q,ell)==-1]
    assert not old_cross_bad and not old_T_bad
    assert bridge_bad == [5]
    return dict(U1=U1,V1=V1,W1=W1,U2=U2,V2=V2,W2=W2,c=c,p=p,q=q,M=M,S=S,H=H,e=e,D=D,T=T,K=K,cross=cross)

L=verify_witness(13,2,32,13,"L")
assert (L["U1"],L["V1"],L["W1"])==(165,52,173)
assert (L["U2"],L["V2"],L["W2"])==(855,832,1193)
assert (L["M"],L["S"],L["c"],L["p"],L["q"],L["H"],L["e"],L["cross"])==(20822490000,144300,15,1,52,185,5,88)
R=verify_witness(33,32,22,17,"R")
assert (R["U1"],R["V1"],R["W1"])==(65,2112,2113)
assert (R["U2"],R["V2"],R["W2"])==(195,748,773)
assert (R["M"],R["S"],R["c"],R["p"],R["q"],R["H"],R["e"],R["cross"])==(171976090000,414700,65,1,44,145,5,17)

src=SRC.read_text()
for marker in ("(BT-SOURCE-H)","(BT-E)","(BT-L)","(BT-R)","(BT-WIT-L)","(BT-WIT-R)","REOPEN_GATE_B_TRIGGERED=true","NEW_SOURCE_FIXED_E1_INVARIANT=SOURCE_KNOWN_BRIDGE_RESERVOIR_RESIDUE_PROFILE","UNIVERSAL_E1_PROOF=false"):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BT_BRIDGE_RESERVOIR_SOURCE_RECLASSIFICATION=PASS")
print("H_source_computable=true")
print("e_source_computable=true")
print("reopen_gate_B_triggered=true")
print("bridge_sieve_nonredundant_branch_L=true")
print("bridge_sieve_nonredundant_branch_R=true")
print("canonical_sha256="+EXPECTED)
