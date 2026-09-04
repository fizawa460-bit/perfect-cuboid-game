#!/usr/bin/env python3
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-14/coprime-e1-receiver-factorization.md"
AUDIT = ROOT / "stages/stage35-ex/35ex-14/fresh-receiver-breadth-audit.json"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def square_fraction(x: Fraction) -> bool:
    return x >= 0 and square(x.numerator) and square(x.denominator)


state = json.loads(STATE.read_text())
doc = DOC.read_text()
audit = json.loads(AUDIT.read_text())

assert state["stage"] == "35-EX"
unit13 = state["completed_units"]["35EX-13"]
assert unit13["status"] == "AUDITED_EXACT_ALTERNATE_NORM_GAUSSIAN_COUPLING_NO_CREDIT"
assert unit13["hostile_reaudit_review"] == 5108343484
assert unit13["audited_head_sha"] == "6a2193c19cce6d9022764c2daf6a2431e2348c1f"
assert unit13["merged_main_sha"] == "0dff1852f30f832e5fef104bcd143c0ee82365c0"
assert unit13["audited_theorem_credit"] is False

unit14 = state["completed_units"]["35EX-14"]
assert unit14["status"] == "PROVISIONAL_EXACT_COPRIME_E1_RECEIVER_FACTORIZATION_NO_CREDIT"
assert unit14["coprime_e1_receiver_factorization_proved_conditionally"] is True
assert unit14["gaussian_sieve_identified_with_Lminus_square"] is True
assert unit14["S34_W03_exact_branch_receiver_adapter_matched"] is True
assert unit14["S34_W03_receiver_intersection_closed"] is False
assert unit14["audited_theorem_credit"] is False

assert state["current"]["unit"] == "35EX-15_COPRIME_RECEIVER_JOINT_LOCAL_OR_FREE_SUPPORT"
assert audit["cycle_exit"]["CYCLE_ROUTE_STATUS"] == "PASS_NEW_GATE_FROM_STRONGER_VIEW"
assert audit["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert audit["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True
assert audit["selection"]["selected_candidate"] == "E1-COPRIME-RECEIVER-JOINT-LOCAL"
assert audit["arsenal_comparison_after_blind_pass"]["matches"][0]["id"] == "S34-W03"
assert audit["arsenal_comparison_after_blind_pass"]["matches"][0]["status"] == "EXACT_ADAPTER_SHAPE_MATCHED_JOINT_TEST_NOT_YET_PROVED"

for text in (
    "gcd(Lminus,Lplus)=1",
    "N = (p*d)^2 * Lminus * Lplus",
    "E1 counterexample",
    "S_plus in Q^x2",
    "<=> Lminus is an integer square",
    "S34_W03_EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED=true",
    "S34_W03_RECEIVER_INTERSECTION_CLOSED=false",
    "35EX-15_COPRIME_RECEIVER_JOINT_LOCAL_OR_FREE_SUPPORT",
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
lminus_master_survivors = []
lplus_on_survivors = []
e1_source_examples = 0

for a, b in pairs1:
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    for m, n in pairs2:
        U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n

        p = gcd(W1, V2)
        d = gcd(V1, W2)
        assert gcd(p, d) == 1
        assert p % 2 == d % 2 == 1

        A = W1 * W2
        B = V1 * V2
        assert gcd(A, B) == p * d

        Pminus = A - B
        Pplus = A + B
        assert Pminus > 0 and Pplus > 0
        assert gcd(Pminus, Pplus) == p * d
        assert Pminus % (p*d) == Pplus % (p*d) == 0

        Lminus = Pminus // (p*d)
        Lplus = Pplus // (p*d)
        assert Lminus % 2 == Lplus % 2 == 1
        assert gcd(Lminus, Lplus) == 1

        Nraw = (W1*U2)**2 + (U1*V2)**2
        assert Nraw == Pminus * Pplus
        assert Nraw == (p*d)**2 * Lminus * Lplus
        assert square(Nraw) == (square(Lminus) and square(Lplus))

        S_plus = Fraction(d * Pplus, p * Nraw)
        assert S_plus == Fraction(1, p*p*Lminus)
        assert square_fraction(S_plus) == square(Lminus)

        if square(Nraw):
            e1_source_examples += 1
            x = isqrt(Lminus)
            y = isqrt(Lplus)
            assert x % 2 == y % 2 == 1 and gcd(x, y) == 1 and y > x
            R = (y + x) // 2
            S = (y - x) // 2
            assert gcd(R, S) == 1
            assert (R-S) % 2 == 1
            assert 2*R*S == V1*V2 // (p*d)
            assert R*R + S*S == W1*W2 // (p*d)
            assert R*R - S*S == x*y

        master = (V1*U2)**2 + (U1*V2)**2
        if not square(master):
            continue
        master_hits += 1
        if square(Lminus):
            lminus_master_survivors.append((a, b, m, n))
            lplus_on_survivors.append(Lplus)

assert e1_source_examples > 0
assert master_hits == 131
assert lminus_master_survivors == [
    (8, 5, 11, 2),
    (11, 2, 8, 5),
    (17, 16, 52, 47),
]
assert lplus_on_survivors == [2929, 2929, 313921]
assert not any(square(x) for x in lplus_on_survivors)

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

print("PASS STAGE35_EX_14_COPRIME_E1_RECEIVER_FACTORIZATION_V1")
