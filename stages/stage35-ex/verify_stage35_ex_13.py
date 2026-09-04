#!/usr/bin/env python3
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-13/alternate-norm-gaussian-coupling.md"


def is_square_int(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def is_square_fraction(x: Fraction) -> bool:
    return x >= 0 and is_square_int(x.numerator) and is_square_int(x.denominator)


def v2(n: int) -> int:
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


state = json.loads(STATE.read_text())
doc = DOC.read_text()

# Progression-safe: verify the recorded audited 35EX-13 authority and its
# mathematics, not the mutable downstream schema/current leaf.
assert state["stage"] == "35-EX"
assert state["target"]["id"] == "PESCH-CONJ-E1-BASIS-NONSQUARE"
unit = state["completed_units"]["35EX-13"]
assert unit["status"] == "AUDITED_EXACT_ALTERNATE_NORM_GAUSSIAN_COUPLING_NO_CREDIT"
assert unit["failed_hostile_audit_review"] == 5108306912
assert unit["hostile_reaudit_review"] == 5108343484
assert unit["audited_head_sha"] == "6a2193c19cce6d9022764c2daf6a2431e2348c1f"
assert unit["merged_main_sha"] == "0dff1852f30f832e5fef104bcd143c0ee82365c0"
assert unit["alternate_gcd_factorization_proved"] is True
assert unit["second_primitive_e1_triple_proved_conditionally"] is True
assert unit["index_swap_dominates_mirrored_receiver"] is True
assert unit["mirrored_four_factor_receiver_new_independent_theorem"] is False
assert unit["gaussian_orientation_coupling_proved_conditionally"] is True
assert unit["source_only_gaussian_square_sieve_proved_conditionally"] is True
assert unit["bounded_panel_master_hits"] == 131
assert unit["bounded_panel_gaussian_survivors"] == 3
assert unit["bounded_panel_e1_counterexamples"] == 0
assert unit["audited_theorem_credit"] is False

for text in (
    "g1 = c*d",
    "p*w = d*z",
    "INDEX_SWAP_DOMINATES_MIRRORED_RECEIVER=true",
    "GAUSSIAN_ORIENTATION_COUPLING_PROVED_CONDITIONALLY=true",
    "SOURCE_ONLY_GAUSSIAN_SQUARE_SIEVE_PROVED_CONDITIONALLY=true",
    "GAUSSIAN_SOURCE_SIEVE_KILLS_128_OF_131=true",
    "GAUSSIAN_SOURCE_SIEVE_PROVES_E1=false",
):
    assert text in doc

pairs1 = [
    (a, b)
    for a in range(2, 51)
    for b in range(1, a)
    if gcd(a, b) == 1 and (a - b) % 2 == 1
]
pairs2 = [
    (m, n)
    for m in range(2, 101)
    for n in range(1, m)
    if gcd(m, n) == 1 and (m - n) % 2 == 1
]

master_hits = 0
gaussian_survivors = []
e1_counterexamples = []
branches = set()

for a, b in pairs1:
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    for m, n in pairs2:
        U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n

        N1 = (W1*U2)**2 + (U1*V2)**2
        N2 = (U1*W2)**2 + (V1*U2)**2
        assert N1 == N2

        c = gcd(U1, U2)
        p = gcd(W1, V2)
        q = gcd(V1, V2)
        d = gcd(V1, W2)
        assert gcd(U1*W2, V1*U2) == c*d
        assert gcd(c, d) == gcd(p, d) == gcd(q, d) == 1
        assert d % 2 == 1

        master = (V1*U2)**2 + (U1*V2)**2
        if not is_square_int(master):
            continue

        master_hits += 1
        branches.add("L" if v2(V1) < v2(V2) else "R")

        S_plus = Fraction(d * (W1*W2 + V1*V2), p * N1)
        if is_square_fraction(S_plus):
            gaussian_survivors.append((a, b, m, n))

        if is_square_int(N1):
            e1_counterexamples.append((a, b, m, n))
            assert is_square_fraction(S_plus)

assert branches == {"L", "R"}
assert master_hits == 131
assert gaussian_survivors == [
    (8, 5, 11, 2),
    (11, 2, 8, 5),
    (17, 16, 52, 47),
]
assert e1_counterexamples == []

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

print("PASS STAGE35_EX_13_ALTERNATE_NORM_GAUSSIAN_COUPLING_AUDITED_V2")
