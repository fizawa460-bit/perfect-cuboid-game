#!/usr/bin/env python3
"""Verify Goal4CA source bridge-norm odd-valuation sieve."""
from __future__ import annotations

import hashlib
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s
ART = P("stages/stage35-ex/35ex-35/goal4ca-source-bridge-norm-valuation-parity.json")
SRC = P("stages/stage35-ex/35ex-35/goal4ca-source-bridge-norm-valuation-parity-source-lock.md")
BZ = P("stages/stage35-ex/35ex-35/goal4bz-post-bridge-quartic-fresh-route-audit.json")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "33daeadddc24a10393550f5cacbb360b321442916954f79b9c0345f675572c27"
SRC_BLOB = "a40ebfd0a20fda3e911e31fafa591cd8ee5d01a9"
BZ_BLOB = "96ef615398c9499c386b0424d4bec82134012f0f"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def val(n: int, ell: int) -> int:
    k = 0
    while n % ell == 0:
        n //= ell
        k += 1
    return k


def v2(n: int) -> int:
    return val(n, 2)


def leg(a: int, ell: int) -> int:
    z = pow(a % ell, (ell - 1) // 2, ell)
    assert z in (1, ell - 1)
    return 1 if z == 1 else -1


def prime_factors(n: int) -> list[int]:
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def master_data(tup: tuple[int, int, int, int]) -> dict:
    a, b, m, n = tup
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2 = m*m-n*n, 2*m*n
    M = (V1*U2)**2 + (U1*V2)**2
    S = isqrt(M)
    assert S*S == M
    c, p, q = gcd(U1, U2), gcd(W1, V2), gcd(V1, V2)
    H = S // (c*q)
    e = gcd(c, H)
    D, T = U1//c, U2//c
    X, Y = q*H//e, c*D*T//e
    Be = X*X + Y*Y
    branch = "L" if v2(V1) < v2(V2) else "R"
    K = (W1//p)*(V1//q)
    cross = D*V2//((2 if branch == "L" else 1)*p*q)
    return locals()


def goal4bu_pass(d: dict) -> bool:
    branch, cross, T, e, K, p, q = (d[k] for k in ("branch","cross","T","e","K","p","q"))
    if branch == "L":
        if any(ell % 4 == 1 and leg(K, ell) != 1 for ell in prime_factors(cross)):
            return False
        if any(ell % 4 == 1 and leg(p*q, ell) != 1 for ell in prime_factors(T)):
            return False
        return all(ell % 4 == 1 and leg(p*q, ell) == 1 for ell in prime_factors(e))
    if any(ell % 4 == 1 and leg(2*K, ell) != 1 for ell in prime_factors(cross)):
        return False
    if any(ell % 4 == 1 and leg(2*p*q, ell) != 1 for ell in prime_factors(T)):
        return False
    return all(ell % 4 == 1 and leg(2*p*q, ell) == 1 for ell in prime_factors(e))


assert blob(SRC) == SRC_BLOB
assert blob(BZ) == BZ_BLOB
state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "aef846dcacb25ab22927b339fd990a68fa5203a6"
assert art["stacked_parent"]["goal4bz_run"] == 34422872919
assert art["source_locks"]["goal4ca_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["source_only_odd_valuation_kill"] is True
assert art["result"]["universal_odd_valuation_at_e"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4CB_SOURCE_BRIDGE_NORM_LOCAL_UNIT_SQUARECLASS_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

# Branch-L and Branch-R nonredundancy witnesses: Goal4BU passes, Goal4CA kills.
for key in ("branch_L", "branch_R"):
    w = art["witnesses"][key]
    d = master_data(tuple(w["tuple"]))
    for field in ("c","p","q","H","e","D","T","X","Y","Be"):
        json_field = "B_e" if field == "Be" else field
        assert d[field] == w[json_field]
    assert goal4bu_pass(d)
    assert val(d["Be"], w["ell"]) == w["v_ell_B_e"]
    assert w["v_ell_B_e"] % 2 == 1

# Even-valuation survivor proves parity is not universal and exposes the next layer.
w = art["witnesses"]["even_survivor"]
d = master_data(tuple(w["tuple"]))
assert d["Be"] == w["B_e"]
assert val(d["Be"], w["ell"]) == 2
unit = d["Be"] // (w["ell"] ** 2)
assert unit % w["ell"] == w["unit_mod_ell"] == 2
assert leg(unit, w["ell"]) == -1

# Exact scale identity and coprimality on every retained witness.
for w in art["witnesses"].values():
    d = master_data(tuple(w["tuple"]))
    F = (d["W1"]*d["U2"])**2 + (d["U1"]*d["V2"])**2
    assert F == (d["c"]*d["e"])**2 * d["Be"]
    assert gcd(d["X"], d["Y"]) == 1

src = SRC.read_text()
for marker in ("(CA-Be)","(CA-scale)","(CA-equiv)","(CA-unbalanced)","(CA-depth)","(CA-kill)","(CA-WIT-L)","(CA-WIT-R)","(CA-even-survivor)"):
    assert marker in src, marker

print("STAGE35_EX_GOAL4CA_SOURCE_BRIDGE_NORM_VALUATION_PARITY=PASS")
print("source_only_odd_valuation_kill=true")
print("branch_L_nonredundant_vs_goal4bu=true")
print("branch_R_nonredundant_vs_goal4bu=true")
print("universal_odd_valuation_at_e=false")
print("next=Goal4CB_source_bridge_norm_local_unit_squareclass")
print("canonical_sha256=" + EXPECTED)
