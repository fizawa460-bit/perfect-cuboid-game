#!/usr/bin/env python3
"""Verify Goal4CB complete odd bridge-prime local square test."""
from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4cb-source-bridge-norm-local-unit-squareclass.json")
SRC = P("stages/stage35-ex/35ex-35/goal4cb-source-bridge-norm-local-unit-squareclass-source-lock.md")
CA = P("stages/stage35-ex/35ex-35/goal4ca-source-bridge-norm-valuation-parity.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "b5c08a39ffa192e26f51c716ef1964ef296572d19e56bf7ef266ce4fe383cdb7"
SRC_BLOB = "b4fd218eef21b8be4199fe31917ef52c7b473019"
CA_BLOB = "2944de70b569b879b32e75956a9e2f1182bc18fa"
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
    a,b,m,n = tup
    U1,V1,W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2,V2 = m*m-n*n, 2*m*n
    M = (V1*U2)**2 + (U1*V2)**2
    S = isqrt(M)
    assert S*S == M
    c,p,q = gcd(U1,U2), gcd(W1,V2), gcd(V1,V2)
    H = S // (c*q)
    e = gcd(c,H)
    D,T = U1//c, U2//c
    X,Y = q*H//e, c*D*T//e
    Be = X*X + Y*Y
    return locals()


assert blob(SRC) == SRC_BLOB
assert blob(CA) == CA_BLOB
state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "766f3d432ee9099eb15d2cebe2c481ea7a293532"
assert art["stacked_parent"]["goal4ca_run"] == 34423996853
assert art["source_locks"]["goal4cb_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["odd_bridge_Qell_square_criterion_complete"] is True
assert art["result"]["bridge_local_square_route_complete"] is True
assert art["result"]["universal_bad_local_square_prime_in_e"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4CC_POST_SOURCE_BRIDGE_LOCAL_COMPLETION_FRESH_ROUTE_AUDIT"
assert all(v is False for v in art["credit_firewall"].values())

# New local-unit kills after CA parity passes.
for key in ("branch_L_depth0", "branch_R_positive_even"):
    w = art["witnesses"][key]
    d = data(tuple(w["tuple"]))
    for field in ("c","p","q","H","e","D","T","X","Y","Be"):
        jf = "B_e" if field == "Be" else field
        assert d[field] == w[jf]
    ell = w["ell"]
    depth = val(d["Be"], ell)
    assert depth == w["v_ell_B_e"] and depth % 2 == 0
    unit = d["Be"] // ell**depth
    assert unit % ell == w["unit_mod_ell"]
    assert leg(unit, ell) == -1

# Complete bridge-local survivor: all e-prime tests pass, but B_e is not globally square.
w = art["witnesses"]["complete_bridge_local_survivor"]
d = data(tuple(w["tuple"]))
assert d["Be"] == w["B_e"] == 2955121
ell = w["ell"]
depth = val(d["Be"], ell)
assert depth == 0
assert d["Be"] % ell == 1 and leg(d["Be"], ell) == 1
assert isqrt(d["Be"])**2 != d["Be"]
assert d["Be"] == 13*53*4289
assert val(d["c"], ell) != val(d["H"], ell)  # unbalanced, hence automatic local square

src = SRC.read_text()
for marker in (
    "(CB-unit)","(CB-local)","(CB-kill)","(CB-unbalanced)","(CB-balanced)",
    "(CB-unit-factor)","(CB-WIT-L)","(CB-WIT-R)","(CB-survivor)","(CB-no-universal)"
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4CB_SOURCE_BRIDGE_NORM_LOCAL_UNIT_SQUARECLASS=PASS")
print("odd_bridge_Qell_square_criterion_complete=true")
print("source_only_even_valuation_unit_kill=true")
print("universal_bad_local_square_prime_in_e=false")
print("bridge_local_square_route_complete=true")
print("next=Goal4CC_post_source_bridge_local_completion_fresh_route_audit")
print("canonical_sha256=" + EXPECTED)
