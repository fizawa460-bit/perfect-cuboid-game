#!/usr/bin/env python3
"""Verify Goal4BV: early bridge primes carry a source-fixed quartic datum."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = lambda s: ROOT / s

ART = P("stages/stage35-ex/35ex-35/goal4bv-source-known-bridge-quartic-orientation.json")
SRC = P("stages/stage35-ex/35ex-35/goal4bv-source-known-bridge-quartic-orientation-source-lock.md")
BU = P("stages/stage35-ex/35ex-35/goal4bu-three-source-reservoir-reciprocity-coupling-source-lock.md")
EX08 = P("stages/stage35-ex/35ex-08/hypotenuse-bridge-triple.md")
STATE = P("stages/stage35-ex/MAIN-STATE.json")

EXPECTED = "2700556bbd4b3660d9a0d6f3f9b1a5932a1c6605edd3c4c066d194c35e283571"
SRC_BLOB = "73f853f3bba9bf00b2bd08670abf91f873d19e7f"
BU_BLOB = "d6ce919c9a8867f77008e733e4701924ae49d437"
EX08_BLOB = "15c53ccd5317b6251a70a5f4bf78051a3bb4af1f"
V74 = "STAGE35_EX_PESCH_E1_STATE_V74_GOAL4AK_EXPLICIT_F_B_AUDITED_LOCAL_EVALUATION_RELEASED"

def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()

def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256")
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def v2(n: int) -> int:
    return (n & -n).bit_length() - 1

def leg(a: int, ell: int) -> int:
    a %= ell
    assert a
    z = pow(a, (ell - 1) // 2, ell)
    assert z in (1, ell - 1)
    return 1 if z == 1 else -1

def q4_rational_value(a: int, ell: int, iota: int) -> int:
    """Return the F_ell representative in {1,-1,+iota,-iota}."""
    z = pow(a % ell, (ell - 1) // 4, ell)
    assert z in {1, ell - 1, iota % ell, (-iota) % ell}
    return z

for path, expected in ((SRC, SRC_BLOB), (BU, BU_BLOB), (EX08, EX08_BLOB)):
    assert blob(path) == expected, (path, blob(path), expected)

state = json.loads(STATE.read_text())
assert state["schema"] == V74
assert state["claims"]["E1_proved"] is False
assert state["claims"]["stage35_closed"] is False

art = json.loads(ART.read_text())
assert art["canonical_sha256"] == canonical(art) == EXPECTED
assert art["stacked_parent"]["exact_head_sha"] == "3f66b64a14d5a7f7ddc5b43759429d355279af9f"
assert art["source_locks"]["goal4bv_source"]["blob_sha1"] == SRC_BLOB
assert art["result"]["bridge_prime_source_root_of_minus_one"] is True
assert art["result"]["bridge_gaussian_prime_orientation_source_fixed"] is True
assert art["result"]["bridge_primary_generator_canonical"] is True
assert art["result"]["bridge_one_sided_gaussian_valuation"] is True
assert art["result"]["bridge_quartic_datum_source_fixed"] is True
assert art["result"]["quadratic_bridge_test_lifts_to_quartic"] is True
assert art["result"]["quartic_phase_forced_by_full_E1"] is False
assert art["result"]["universal_bad_quartic_bridge_prime"] is False
assert art["next"]["unit"] == "35EX-35_GOAL4BW_BRIDGE_QUARTIC_PHASE_FORCING_PREFLIGHT"
assert all(v is False for v in art["credit_firewall"].values())

def verify(a: int, b: int, m: int, n: int, branch: str, expected_ell: int, expected_iota: int, expected_phase: int):
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
    M = (V1*U2)**2 + (U1*V2)**2
    S = math.isqrt(M)
    assert S*S == M
    c = math.gcd(U1, U2)
    p = math.gcd(W1, V2)
    q = math.gcd(V1, V2)
    H = S // (c*q)
    assert H*c*q == S
    e = math.gcd(c, H)
    D, T = U1//c, U2//c
    A, B = (V1//q)*T, D*(V2//q)
    assert A*A+B*B == H*H
    assert math.gcd(A, B) == math.gcd(A, H) == math.gcd(B, H) == 1
    actual_branch = "L" if v2(V1) < v2(V2) else "R"
    assert actual_branch == branch
    ell = expected_ell
    assert e % ell == 0 and ell % 2 == 1
    assert A % ell and B % ell
    iota = (A * pow(B, -1, ell)) % ell
    assert iota == expected_iota and iota*iota % ell == ell-1
    numerator = p*q if branch == "L" else 2*p*q
    assert numerator % ell
    assert leg(numerator, ell) == 1
    phase = q4_rational_value(numerator, ell, iota)
    assert phase == expected_phase % ell
    assert phase in (1, ell-1)
    return A, B, H, e, numerator

assert verify(13, 4, 96, 91, "L", 17, 13, -1) == (55, 1512, 1513, 17, 104)
assert verify(88, 7, 98, 37, "R", 5, 3, 1) == (2684, 14763, 15005, 5, 56)

src = SRC.read_text()
for marker in ("(BV-iota)", "(BV-root)", "(BV-P)", "(BV-val)", "(BV-primary)", "(BV-Q4)", "(BV-square)", "(BV-real-phase)", "(BV-VERDICT)", "35EX-35_GOAL4BW_BRIDGE_QUARTIC_PHASE_FORCING_PREFLIGHT"):
    assert marker in src, marker

print("STAGE35_EX_GOAL4BV_SOURCE_KNOWN_BRIDGE_QUARTIC_ORIENTATION=PASS")
print("bridge_quartic_datum_source_fixed=true")
print("quartic_phase_forced_by_full_E1=false")
print("next=Goal4BW_bridge_quartic_phase_forcing")
print("canonical_sha256=" + EXPECTED)
