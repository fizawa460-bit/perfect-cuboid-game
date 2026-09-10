#!/usr/bin/env python3
"""Verify Goal4CC fresh-route audit and p/d balanced cancellation witnesses."""
from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4cc-post-source-bridge-local-completion-fresh-route-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4cc-post-source-bridge-local-completion-fresh-route-audit-source-lock.md")
CB = P("stages/stage35-ex/35ex-35/goal4cb-source-bridge-norm-local-unit-squareclass.json")
EX04 = P("stages/stage35-ex/35ex-04/product-rectangle-reduction.md")
EX13 = P("stages/stage35-ex/35ex-13/alternate-norm-gaussian-coupling.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "6828976117b9a5b2d374d53dbcf9f7dd89296c79583f1cbcc2df1940823d0829"
BLOBS = {
    SRC: "cd0e553f6fb22de5b42c438ee265b9c82deb2a7c",
    CB: "fa898141770bf93fa2490af18f0667f38a478a1c",
    EX04: "186226223798e89e97d504ead7931b8209d63282",
    EX13: "196d2be1bbfbcb2b416535d7bb051a9b2ec93104",
}
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def val(n: int, p: int) -> int:
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def leg(a: int, p: int) -> int:
    z = pow(a % p, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


def data(tup: tuple[int,int,int,int]) -> dict:
    a,b,m,n=tup
    U1,V1,W1=a*a-b*b,2*a*b,a*a+b*b
    U2,V2,W2=m*m-n*n,2*m*n,m*m+n*n
    M=(V1*U2)**2+(U1*V2)**2
    S=isqrt(M); assert S*S==M
    c,p,q=gcd(U1,U2),gcd(W1,V2),gcd(V1,V2)
    H=S//(c*q); e=gcd(c,H); D,T=U1//c,U2//c
    X,Y=q*H//e,c*D*T//e; Be=X*X+Y*Y
    dd=gcd(V1,W2)
    return locals()


for path, expected in BLOBS.items():
    assert blob(path) == expected, (path, blob(path), expected)
state=json.loads(STATE.read_text())
assert state["schema"]==V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art=json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "f10685d8404160cf945d80a327e489711b85e1a0"
assert art["stacked_parent"]["goal4cb_run"] == 34424246899
assert art["ledger"]["LIVE"] == ["CANONICAL_E1_CROSS_GCD_P_D_BALANCED_LOCAL_SQUARE"]
assert art["cycle"]["exhaustive_view_audit"] is True
assert art["cycle"]["blind_rediscovery"] is True
assert art["next"]["unit"] == "35EX-35_GOAL4CD_CANONICAL_E1_CROSS_GCD_P_D_LOCAL_SQUARE_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

# p-balanced witness
w=art["witnesses"]["p"]
d=data(tuple(w["tuple"]))
assert d["p"]==w["p"]==5 and d["e"]==1 and d["Be"]==w["B_e"]
ell=w["ell"]
assert val(d["W1"],ell)==val(d["V2"],ell)==val(d["p"],ell)==1
vp=val(d["Be"],ell); assert vp==w["v_ell_B_e"]==2
u=d["Be"]//ell**vp; assert u%ell==w["unit_mod_ell"]==2 and leg(u,ell)==-1

# d-balanced witness
w=art["witnesses"]["d"]
d=data(tuple(w["tuple"]))
assert d["p"]==1 and d["dd"]==w["d"]==17 and d["e"]==1 and d["Be"]==w["B_e"]
ell=w["ell"]
assert val(d["V1"],ell)==val(d["W2"],ell)==val(d["dd"],ell)==1
assert val(d["Be"],ell)==w["v_ell_B_e"]==3

src=SRC.read_text()
for marker in ("(CC-p-balanced)","(CC-p-witness)","(CC-alt)","(CC-d-balanced)","(CC-d-witness)"):
    assert marker in src, marker

print("STAGE35_EX_GOAL4CC_POST_SOURCE_BRIDGE_LOCAL_COMPLETION_FRESH_ROUTE_AUDIT=PASS")
print("live=CANONICAL_E1_CROSS_GCD_P_D_BALANCED_LOCAL_SQUARE")
print("next=Goal4CD_canonical_E1_cross_gcd_p_d_local_square")
print("canonical_sha256=" + EXPECTED)
