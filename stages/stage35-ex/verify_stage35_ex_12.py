#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-12/sunit-thue-dynamic-support-blocker.md"


def v2(n: int) -> int:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def prime_support(n: int):
    n = abs(n)
    out = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.add(n)
    return out


state = json.loads(STATE.read_text())
doc = DOC.read_text()

# Authority-stable: verify the immutable recorded 35EX-12 audit/boundary only.
# Do not pin parent_authority or the mutable latest candidate ledger, both of
# which legitimately advance after later audited leaves.
assert state["stage"] == "35-EX"
assert state["target"]["id"] == "PESCH-CONJ-E1-BASIS-NONSQUARE"
unit = state["completed_units"]["35EX-12"]
assert unit["status"] == "AUDITED_EXACT_DYNAMIC_SUPPORT_BLOCKER_NO_CREDIT"
assert unit["hostile_audit_review"] == 5108290559
assert unit["audited_head_sha"] == "d652f912d660ef9e5ec0b0dfa29e8a4eac35766f"
assert unit["merged_main_sha"] == "5436d56fd897426a3a0889874ada2aa6a42df9fd"
assert unit["per_master_hit_finite_sunit_support_proved"] is True
assert unit["uniform_fixed_finite_S_proved"] is False
assert unit["fixed_finite_Thue_family_proved"] is False
assert unit["sunit_thue_finite_enumeration_authorized"] is False
assert unit["route_frozen_dynamic_support"] is True
assert unit["audited_theorem_credit"] is False

block = state["resolved_investigations"]["CURRENT_SUNIT_THUE_DYNAMIC_SUPPORT"]
assert block["status"] == "FROZEN_NO_UNIFORM_FIXED_SUPPORT_ADAPTER_FROM_CURRENT_IDENTITIES"

for text in (
    "PER_MASTER_HIT_FINITE_SUNIT_SUPPORT_PROVED=true",
    "UNIFORM_FIXED_FINITE_S_PROVED=false",
    "FIXED_FINITE_THUE_FAMILY_PROVED=false",
    "SUNIT_THUE_FINITE_ENUMERATION_AUTHORIZED=false",
    "CURRENT_SUNIT_THUE_ADAPTER_ROUTE=FROZEN_DYNAMIC_SUPPORT",
):
    assert text in doc

panel = [
    (4, 3, 16, 5),
    (5, 2, 8, 3),
    (6, 5, 8, 5),
    (9, 8, 6, 5),
    (11, 2, 8, 5),
    (13, 2, 17, 8),
]
supports = []
branches = set()
for a, b, m, n in panel:
    assert gcd(a, b) == gcd(m, n) == 1
    assert (a - b) % 2 == 1 and (m - n) % 2 == 1
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
    master = (V1*U2)**2 + (U1*V2)**2
    assert isqrt(master)**2 == master

    c = gcd(U1, U2)
    p = gcd(W1, V2)
    q = gcd(V1, V2)
    D = U1 // c
    T = U2 // c
    assert gcd(D, T) == 1

    if v2(V1) < v2(V2):
        branches.add("L")
        num = D * V2
        den = 2 * p * q
        assert num % den == 0
        cross = num // den
        assert cross * T * c == D * V2 * U2 // (2 * p * q)
    else:
        branches.add("R")
        num = D * V2
        den = p * q
        assert num % den == 0
        cross = num // den
        assert cross * T * c == D * V2 * U2 // (p * q)

    S_hit = prime_support(2 * c * cross * T)
    assert len(S_hit) < 100
    supports.append(tuple(sorted(S_hit)))

assert branches == {"L", "R"}
assert len(set(supports)) > 1

for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

print("PASS STAGE35_EX_12_AUDITED_SUNIT_THUE_DYNAMIC_SUPPORT_BLOCKER_V3_AUTHORITY_STABLE")
