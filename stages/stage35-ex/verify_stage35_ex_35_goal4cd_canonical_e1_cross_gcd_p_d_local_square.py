#!/usr/bin/env python3
"""Verify Goal4CD canonical p/d cross-gcd local-square sieve."""
from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4cd-canonical-e1-cross-gcd-p-d-local-square.json")
SRC = P("stages/stage35-ex/35ex-35/goal4cd-canonical-e1-cross-gcd-p-d-local-square-source-lock.md")
CC = P("stages/stage35-ex/35ex-35/goal4cc-post-source-bridge-local-completion-fresh-route-audit.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "91138db08d7e7761bdbedf1836e1e1ed59e3ab9895b938b18ee03edaed497ae5"
SRC_BLOB = "9f1d8ef3de24399382562195cf345e5e62f21052"
CC_BLOB = "c7adb599c65304f3112c34ea0887b65f60e5609f"
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


def data(tup: tuple[int, int, int, int]) -> dict:
    a, b, m, n = tup
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
    M = (V1*U2)**2 + (U1*V2)**2
    S = isqrt(M)
    assert S*S == M
    c, p, q = gcd(U1, U2), gcd(W1, V2), gcd(V1, V2)
    d = gcd(V1, W2)
    H = S // (c*q)
    e = gcd(c, H)
    D, T = U1//c, U2//c
    X, Y = q*H//e, c*D*T//e
    Be = X*X + Y*Y
    Fp = (W1*U2)**2 + (U1*V2)**2
    Fd = (U1*W2)**2 + (V1*U2)**2
    assert Fp == Fd == (c*e)**2 * Be
    return locals()


assert blob(SRC) == SRC_BLOB
assert blob(CC) == CC_BLOB
state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "e56cec5b587f21ad905008536065c9d809e56e98"
assert art["stacked_parent"]["goal4cc_run"] == 34424751268
assert art["stacked_parent"]["goal4cc_job"] == 102707479471
assert art["source_locks"]["goal4cd_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["canonical_source_gcd_local_family_complete"] is True
assert art["result"]["universal_bad_prime_in_p_d_e"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4CE_POST_CANONICAL_GCD_LOCAL_COMPLETION_FRESH_ROUTE_AUDIT"
assert all(v is False for v in art["credit_firewall"].values())

# p-balanced kill: complete local test fails on residual unit.
w = art["witnesses"]["p_kill"]
z = data(tuple(w["tuple"]))
for key in ("c", "p", "q", "H", "e"):
    assert z[key] == w[key]
assert z["Be"] == w["B_e"]
ell = w["ell"]
k = val(z["p"], ell)
assert val(z["W1"], ell) == val(z["V2"], ell) == k == 1
Rp = ((z["W1"] // ell**k) * z["U2"])**2 + (z["U1"] * (z["V2"] // ell**k))**2
assert Rp == 143377
assert z["Be"] * (z["c"]*z["e"])**2 == ell**(2*k) * Rp
v = val(z["Be"], ell)
unit = z["Be"] // ell**v
assert v == w["v_ell_B_e"] == 2
assert unit % ell == w["unit_mod_ell"] == 2 and leg(unit, ell) == -1

# d-balanced kill: odd depth.
w = art["witnesses"]["d_kill"]
z = data(tuple(w["tuple"]))
assert z["c"] == w["c"] and z["p"] == w["p"] and z["d"] == w["d"]
assert z["q"] == w["q"] and z["H"] == w["H"] and z["e"] == w["e"]
assert z["Be"] == w["B_e"]
ell = w["ell"]
k = val(z["d"], ell)
assert val(z["V1"], ell) == val(z["W2"], ell) == k == 1
Rd = (z["U1"] * (z["W2"] // ell**k))**2 + ((z["V1"] // ell**k) * z["U2"])**2
assert z["Be"] * (z["c"]*z["e"])**2 == ell**(2*k) * Rd
assert val(z["Be"], ell) == w["v_ell_B_e"] == 3

# Balanced p survivor demonstrates the balanced stratum is not automatically bad.
w = art["witnesses"]["balanced_p_survivor"]
z = data(tuple(w["tuple"]))
assert z["p"] == w["p"] == 13 and z["d"] == z["e"] == 1
ell = w["ell"]
assert val(z["W1"], ell) == val(z["V2"], ell) == 1
v = val(z["Be"], ell)
unit = z["Be"] // ell**v
assert z["Be"] == w["B_e"] and v == w["v_ell_B_e"] == 2
assert unit % ell == w["unit_mod_ell"] == 4 and leg(unit, ell) == 1

# Joint p/d/e survivor: selected local families all pass, fresh norm primes remain.
w = art["witnesses"]["joint_survivor"]
z = data(tuple(w["tuple"]))
assert z["c"] == 7 and z["p"] == 5 and z["d"] == z["e"] == 1
assert z["q"] == 8 and z["H"] == 101 and z["Be"] == w["B_e"] == 706225
ell = 5
assert val(z["W1"], ell) == 2 != 1 == val(z["V2"], ell)
assert val(z["Be"], ell) == 2
assert (z["Be"] // 25) % 5 == 4
assert z["Be"] == 5**2 * 13 * 41 * 53
assert isqrt(z["Be"])**2 != z["Be"]

src = SRC.read_text()
for marker in (
    "(CD-Fp)", "(CD-Fd)", "(CD-Be)", "(CD-p-unbalanced)", "(CD-p-balanced)",
    "(CD-Rp)", "(CD-p-local)", "(CD-d-unbalanced)", "(CD-d-balanced)", "(CD-Rd)",
    "(CD-p-witness)", "(CD-d-witness)", "(CD-p-balanced-survivor)",
    "(CD-joint-survivor)", "(CD-no-universal)"
):
    assert marker in src, marker

print("STAGE35_EX_GOAL4CD_CANONICAL_E1_CROSS_GCD_P_D_LOCAL_SQUARE=PASS")
print("p_balanced_complete_local_test=true")
print("d_balanced_complete_local_test=true")
print("universal_bad_prime_in_p_d_e=false")
print("canonical_source_gcd_local_family_complete=true")
print("next=Goal4CE_post_canonical_gcd_local_completion_fresh_route_audit")
print("canonical_sha256=" + EXPECTED)
