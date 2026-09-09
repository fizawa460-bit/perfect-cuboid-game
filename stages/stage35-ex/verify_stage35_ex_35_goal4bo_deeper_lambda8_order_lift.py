#!/usr/bin/env python3
"""Verify Goal4BO: lambda8 orientation detection and unbounded deeper ray tower boundary."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bo-deeper-lambda8-order-lift.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bo-deeper-lambda8-order-lift-source-lock.md")
BN = P("stages/stage35-ex/35ex-35/goal4bn-common-w-primary-space-root-ray-product.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "20439e1eda541da3bb8f8b8d5bbac1cc7e4f476ad9b7dc69ed5632a7cbfd8c9b"
SRC_BLOB = "bbb9adee04d6b68937d7393974778a06b119befb"
BN_BLOB = "7da460f1e2d7f3a68a5b093f0bc004155d775523"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def checkcanon(obj: dict) -> None:
    x = dict(obj)
    got = x.pop("canonical_sha256")
    calc = hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == calc == EXPECTED, (got, calc)

def gmul_raw(z, w):
    a, b = z; c, d = w
    return (a*c-b*d, a*d+b*c)

def gpow_raw(z, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = gmul_raw(out, z)
        z = gmul_raw(z, z)
        n //= 2
    return out

def vlambda(z):
    a, b = z
    v = 0
    while (a, b) != (0, 0) and (a-b) % 2 == 0:
        a, b = (a+b)//2, (b-a)//2
        v += 1
    return v

def gm(z, w, m=16):
    a, b = z; c, d = w
    return ((a*c-b*d) % m, (a*d+b*c) % m)

def gpow(z, n, m=16):
    out = (1, 0)
    while n:
        if n & 1:
            out = gm(out, z, m)
        z = gm(z, z, m)
        n //= 2
    return out

def primary(z):
    a, b = z
    return a % 2 == 1 and b % 2 == 0 and (a+b-1) % 4 == 0

assert blob(SRC) == SRC_BLOB
assert blob(BN) == BN_BLOB
state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["last_audited_authority"]["hostile_review_id"] == 5142248509
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

bn = json.loads(BN.read_text())
assert bn["canonical_sha256"] == "cb5d180ad3a42762426f9e8a7792600b5a2e43a03f1bb77e07ed20938f277e3a"
assert bn["result"]["both_sigma_signs_same_selected_pi_locally_compatible"] is True

src = SRC.read_text()
for marker in ("(BO-pi)","(BO-valuation)","(BO-order)","(BO-structure)","(BO-pi-coords)","(BO-detect)","(BO-BN-flex)","(BO-no-obstruction)","(BO-order-table)","35EX-35_GOAL4BP_POST_GAUSSIAN_RAY_TOWER_FRESH_ROUTE_AUDIT"):
    assert marker in src, marker

art = json.loads(ART.read_text())
checkcanon(art)
parent = art["stacked_parent"]
assert parent["exact_head_sha"] == "2ef61ba9d0919e9bdef33f1971c48650b5f8915a"
assert parent["aggregate_run"] == 34317632854
assert parent["aggregate_job"] == 102358457114
assert parent["hostile_audited"] is False

assert gpow_raw((1, 1), 5) == (-4, -4)
assert (1-(-4), -(-4)) == (5, 4)
pi = (5, 4)
for k in range(7):
    z = gpow_raw(pi, 2**k)
    assert vlambda((z[0]-1, z[1])) == 5 + 2*k

G = {(a, b) for a in range(16) for b in range(16) if primary((a, b))}
assert len(G) == 32
g = (3, 2); h = (1, 4)
assert gpow(g, 8) == (1, 0) and gpow(g, 4) != (1, 0)
assert gpow(h, 4) == (1, 0) and gpow(h, 2) != (1, 0)
seen = {}
for u in range(8):
    for v in range(4):
        z = gm(gpow(g, u), gpow(h, v))
        assert z in G and z not in seen
        seen[z] = (u, v)
assert len(seen) == 32
assert seen[(5, 4)] == (2, 2)
assert seen[(13, 12)] == (6, 2)
assert gm((5, 4), (13, 12)) == (1, 0)

assert art["ray_order"]["table"] == {"7": 2, "8": 4, "9": 4, "10": 8, "11": 8}
assert art["lambda8_group"]["structure"] == "C8 x C4"
assert art["lambda8_group"]["pi_order"] == 4
assert art["orientation_character"]["chi_8_pi"] == "i"
assert art["orientation_character"]["chi_8_pi_inverse"] == "-i"
res = art["result"]
assert res["pi_1_minus_lambda5_exact"] is True
assert res["valuation_tower_exact"] is True
assert res["lambda8_orientation_detection_obtained"] is True
assert res["deeper_ray_order_unbounded"] is True
assert res["source_fixed_deeper_character_value_obtained"] is False
assert res["mechanical_deeper_conductor_route_fail_closed"] is True
assert res["global_reciprocity_contradiction_obtained"] is False
assert res["new_branch_pruning_obtained"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BP_POST_GAUSSIAN_RAY_TOWER_FRESH_ROUTE_AUDIT"
for key, val in art["credit_firewall"].items():
    assert val is False, (key, val)

print("STAGE35_EX_GOAL4BO_DEEPER_LAMBDA8_ORDER_LIFT=PASS")
print("lambda8_orientation_detected=true")
print("deeper_ray_order_unbounded=true")
print("source_fixed_deeper_character_value=false")
print("mechanical_deeper_conductor_route_fail_closed=true")
print("canonical_sha256=" + EXPECTED)
