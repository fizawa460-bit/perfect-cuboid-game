#!/usr/bin/env python3
"""Verify Goal4BZ post-bridge-quartic fresh-route audit."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4bz-post-bridge-quartic-fresh-route-audit.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bz-post-bridge-quartic-fresh-route-audit-source-lock.md")
BY = P("stages/stage35-ex/35ex-35/goal4by-bridge-quartic-integer-global-adapter.json")
EX10 = P("stages/stage35-ex/35ex-10/split-prime-obstruction.md")
EX11 = P("stages/stage35-ex/35ex-11/reciprocity-routing-and-local-route-freeze.md")
EX12 = P("stages/stage35-ex/35ex-12/sunit-thue-dynamic-support-blocker.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "aca36b4e6698f29a439c0ed1ebb4b6108e2a7892a462e583b734fbb8f5549c5b"
SRC_BLOB = "47775301f878d16bda068f73d17489e56fa8e5d9"
BY_BLOB = "e7eec251f16b562a655d5ce9669dcf6e0882af41"
EX10_BLOB = "a5761a883b3c50bbdad6a357241bba4b61e71c8a"
EX11_BLOB = "fc186e1a0b2134840135e67c29adb0e6bd9bf1a9"
EX12_BLOB = "8e982b6332c3e95af221f16a88e01e478c7d5490"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def vp(n: int, p: int) -> int:
    z = 0
    while n % p == 0:
        n //= p
        z += 1
    return z


def leg(a: int, p: int) -> int:
    z = pow(a % p, (p - 1) // 2, p)
    assert z in (1, p - 1)
    return 1 if z == 1 else -1


for path, expected in ((SRC,SRC_BLOB),(BY,BY_BLOB),(EX10,EX10_BLOB),(EX11,EX11_BLOB),(EX12,EX12_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state=json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art=json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "a55b0517af61650dc6d9c936d93af9ff18eec779"
assert art["stacked_parent"]["goal4by_run"] == 34422378913
assert art["stacked_parent"]["goal4by_run_success"] is True
assert art["cycle"]["exhaustive_view_audit"] is True
assert art["cycle"]["blind_rediscovery"] is True
assert art["cycle"]["split_triggered"] is False
assert art["ledger"]["LIVE"] == ["SOURCE_BRIDGE_NORM_ODD_VALUATION_PARITY"]
assert art["next"]["unit"] == "35EX-35_GOAL4CA_SOURCE_BRIDGE_NORM_VALUATION_PARITY_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

# Rebuild the exact nonredundancy Master-Hit from Euclid source data.
a,b,m,n=art["nonredundancy_witness"]["tuple"]
U1=a*a-b*b; V1=2*a*b; W1=a*a+b*b
U2=m*m-n*n; V2=2*m*n; W2=m*m+n*n
M=(V1*U2)**2+(U1*V2)**2
S=math.isqrt(M)
assert S*S == M
c=math.gcd(U1,U2); p=math.gcd(W1,V2); q=math.gcd(V1,V2)
H=S//(c*q); e=math.gcd(c,H); D=U1//c; T=U2//c
X=q*H//e; Y=c*D*T//e; Be=X*X+Y*Y
w=art["nonredundancy_witness"]
assert (c,p,q,H,e,D,T,X,Y,Be)==(w["c"],w["p"],w["q"],w["H"],w["e"],w["D"],w["T"],w["X"],w["Y"],w["B_e"])
assert math.gcd(X,Y)==1
ell=w["ell"]
assert leg(p*q,ell)==w["bridge_quadratic_symbol"]==1
assert vp(Be,ell)==w["v_ell_B_e"]==1
assert math.isqrt(Be)**2 != Be

src=SRC.read_text()
for marker in (
    "(BZ-Be)","(BZ-square)","(BZ-nu)","(BZ-parity)","(BZ-witness)",
    "CYCLE_EXHAUSTIVE_VIEW_AUDIT=true","CYCLE_BLIND_REDISCOVERY=true",
    "35EX-35_GOAL4CA_SOURCE_BRIDGE_NORM_VALUATION_PARITY_PREFLIGHT",
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BZ_POST_BRIDGE_QUARTIC_FRESH_ROUTE_AUDIT=PASS")
print("live=SOURCE_BRIDGE_NORM_ODD_VALUATION_PARITY")
print("nonredundant_vs_quadratic_bridge=true")
print("next=Goal4CA_source_bridge_norm_valuation_parity")
print("canonical_sha256="+EXPECTED)
