#!/usr/bin/env python3
"""Verify Goal4BY integer bridge-quartic adapter redundancy."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4by-bridge-quartic-integer-global-adapter.json")
SRC = P("stages/stage35-ex/35ex-35/goal4by-bridge-quartic-integer-global-adapter-source-lock.md")
BX = P("stages/stage35-ex/35ex-35/goal4bx-bridge-quartic-global-product.json")
EX09 = P("stages/stage35-ex/35ex-09/bridge-squareclass-graph.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "537787d916edd8903a70acb5346b6f572ff267bd58f481a82dec4ab51bb885fa"
SRC_BLOB = "2cf893790272fafe6d7302d700ebfab3e7aa2b95"
BX_BLOB = "019d022bdd9a0934d7ba1be5b89c2a5e24b6bfed"
EX09_BLOB = "1cbd3fdf4891ffabc1911ae19632f593a87b5d14"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def leg(a: int, ell: int) -> int:
    z = pow(a % ell, (ell - 1) // 2, ell)
    assert z in (1, ell - 1), (a, ell, z)
    return 1 if z == 1 else -1


def eps4_square(a: int, ell: int) -> int:
    assert leg(a, ell) == 1, (a, ell)
    z = pow(a % ell, (ell - 1) // 4, ell)
    assert z in (1, ell - 1), (a, ell, z)
    return 1 if z == 1 else -1


def inv(a: int, ell: int) -> int:
    return pow(a % ell, -1, ell)


for path, expected in ((SRC, SRC_BLOB), (BX, BX_BLOB), (EX09, EX09_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "1033a99c16237f1d6ae0cf943d1b35e84a391967"
assert art["stacked_parent"]["goal4bx_run"] == 34420555860
assert art["stacked_parent"]["aggregate_run"] == 34420555856
assert art["source_locks"]["goal4by_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["bridge_e_allocation_source_fixed_by_omega"] is True
assert art["result"]["integer_factor_graph_gives_vertex_unit_quartic_adapter"] is True
assert art["result"]["apparent_integer_adapter_reduces_to_source_Qe"] is True
assert art["result"]["branch_L_chi_qT_automatic"] is True
assert art["result"]["branch_R_chi_qT_over_2_automatic"] is True
assert art["result"]["goal4by_adds_new_bridge_quartic_pruning"] is False
assert art["result"]["mechanical_bridge_quartic_route_fail_closed"] is True
assert art["next"]["unit"] == "35EX-35_GOAL4BZ_POST_BRIDGE_QUARTIC_FRESH_ROUTE_AUDIT"
assert all(v is False for v in art["credit_firewall"].values())


def check_L(d: dict, ell: int, expected_omega: int, expected_leg: int) -> None:
    r,s,u,v,p,q,w,H,e,t,T,a,b = (d[k] for k in ("r","s","u","v","p","q","w","H","e","t","T","a","b"))
    assert math.gcd(r,s) == math.gcd(u,v) == 1
    assert (r-s) % 2 == (u-v) % 2 == 1
    assert w == r*r+s*s and H == u*u+v*v and e == ell
    assert p*r*s == q*u*v
    W1=a*a+b*b; V1=2*a*b
    assert p*(r*r-s*s) == W1*T
    assert q*(u*u-v*v) == V1*T
    assert t == r*s//q == u*v//p
    A0_num=p*w-q*H; B0_num=p*w+q*H
    assert A0_num % e == B0_num % e == 0
    assert math.isqrt(A0_num//e)**2 == A0_num//e
    assert math.isqrt(B0_num//e)**2 == B0_num//e
    iota=u*inv(v,ell)%ell
    rho=r*inv(s,ell)%ell
    omega=rho*inv(iota,ell)%ell
    assert omega == expected_omega % ell
    assert iota*iota % ell == ell-1
    assert W1*inv(V1,ell)%ell == omega
    L1=r*u+s*v; L2=r*v-s*u; L3=r*u-s*v; L4=r*v+s*u
    if expected_omega == 1:
        assert L1 % ell == L2 % ell == 0 and L3 % ell and L4 % ell
        K=L3
    else:
        assert L3 % ell == L4 % ell == 0 and L1 % ell and L2 % ell
        K=L1
    F=a+expected_omega*b
    assert K*K % ell == iota*t*T*F*F % ell
    z=q*v*inv(s,ell)%ell
    assert z == d["z_mod_ell"] and leg(z,ell) == expected_leg == d["legendre_z"]
    pred=leg(q*F*inv(2,ell),ell)*eps4_square(iota*t*T,ell)
    assert pred == expected_leg
    assert leg(q*T,ell) == 1
    assert iota*t*T % ell == V1*T*T*inv(2*p*q,ell)%ell
    assert F*F % ell == 2*omega*V1 % ell


def check_R(d: dict, ell: int, expected_omega: int, expected_leg: int) -> None:
    r,s,u,v,p,q,w,H,e,j,T,a,b = (d[k] for k in ("r","s","u","v","p","q","w","H","e","j","T","a","b"))
    assert math.gcd(r,s) == math.gcd(u,v) == 1
    assert (r-s) % 2 == (u-v) % 2 == 1
    assert w == r*r+s*s and H == u*u+v*v and e == ell
    assert 2*p*r*s == q*(u*u-v*v)
    W1=a*a+b*b; V1=2*a*b
    assert p*(r*r-s*s) == W1*T
    assert 2*q*u*v == V1*T
    assert j == (u*u-v*v)//p
    A0_num=p*w-q*H; B0_num=p*w+q*H
    assert A0_num % e == B0_num % e == 0
    assert math.isqrt(A0_num//e)**2 == A0_num//e
    assert math.isqrt(B0_num//e)**2 == B0_num//e
    iota=(2*u*v)*inv(u*u-v*v,ell)%ell
    rho=r*inv(s,ell)%ell
    omega=rho*inv(iota,ell)%ell
    assert omega == expected_omega % ell
    assert iota*iota % ell == ell-1
    assert W1*inv(V1,ell)%ell == omega
    R1=r*(u-v)-s*(u+v)
    R2=r*(u+v)+s*(u-v)
    R3=r*(u-v)+s*(u+v)
    R4=r*(u+v)-s*(u-v)
    if expected_omega == 1:
        assert R1 % ell == R2 % ell == 0 and R3 % ell and R4 % ell
        K=R4
    else:
        assert R3 % ell == R4 % ell == 0 and R1 % ell and R2 % ell
        K=R2
    F=a+expected_omega*b
    assert K*K % ell == iota*j*T*F*F % ell
    z=(1+iota)*q*v*inv(s,ell)%ell
    assert z == d["z_mod_ell"] and leg(z,ell) == expected_leg == d["legendre_z"]
    pred=leg(q*F*inv(2,ell),ell)*eps4_square(iota*j*T,ell)
    assert pred == expected_leg
    assert leg(q*T*inv(2,ell),ell) == 1
    assert iota*j*T % ell == V1*T*T*inv(p*q,ell)%ell
    assert F*F % ell == 2*omega*V1 % ell


L=art["integer_diagnostics"]["branch_L"]
check_L(L["negative"],17,-1,-1)
check_L(L["positive"],17,-1,1)
R=art["integer_diagnostics"]["branch_R"]
check_R(R["negative"],41,1,-1)
check_R(R["positive"],41,1,1)

src=SRC.read_text()
for marker in (
    "(BY-L-vertices)",
    "(BY-R-vertices)",
    "(BY-e-allocation)",
    "(BY-K2)",
    "(BY-apparent-adapter)",
    "(BY-C-collapse)",
    "(BY-F2)",
    "(BY-square-collapse)",
    "(BY-L-auto)",
    "(BY-R-auto)",
    "35EX-35_GOAL4BZ_POST_BRIDGE_QUARTIC_FRESH_ROUTE_AUDIT",
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BY_BRIDGE_QUARTIC_INTEGER_GLOBAL_ADAPTER=PASS")
print("bridge_e_allocation_source_fixed=true")
print("integer_quartic_adapter_reduces_to_source_Qe=true")
print("new_bridge_quartic_pruning=false")
print("next=Goal4BZ_post_bridge_quartic_fresh_route_audit")
print("canonical_sha256=" + EXPECTED)
