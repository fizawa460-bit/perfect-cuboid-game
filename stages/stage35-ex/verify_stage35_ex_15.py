#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-15/joint-local-free-split-support.md"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def factor(n: int):
    n = abs(n)
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


state = json.loads(STATE.read_text())
doc = DOC.read_text()

# Progression-safe: verify the recorded 35EX-15 exact boundary itself, not the
# mutable downstream schema/current candidate after a later leaf advances.
assert state["stage"] == "35-EX"
unit14 = state["completed_units"]["35EX-14"]
assert unit14["status"] == "AUDITED_EXACT_COPRIME_E1_RECEIVER_FACTORIZATION_NO_CREDIT"
assert unit14["hostile_audit_review"] == 5108445565
assert unit14["audited_head_sha"] == "ff502d2c9455ce60b4030843947e16e5bc84057c"
assert unit14["merged_main_sha"] == "6d4354ca7e3d8162ad2f97d7aab086858c061503"
assert unit14["audited_theorem_credit"] is False

unit15 = state["completed_units"]["35EX-15"]
assert unit15["status"] == "PROVISIONAL_EXACT_JOINT_LOCAL_FREE_SPLIT_SUPPORT_NO_CREDIT"
assert unit15["residual_squareclass_split_only"] is True
assert unit15["B35_implies_Lplus_Q2_square"] is True
assert unit15["real_place_automatic"] is True
assert unit15["S34_W03_exact_branch_receiver_adapter_matched"] is True
assert unit15["S34_W03_receiver_intersection_closed"] is False
assert unit15["current_S34_W03_joint_local_route_frozen_free_split_support"] is True
assert unit15["all_future_local_global_arguments_ruled_out"] is False
assert unit15["audited_theorem_credit"] is False
assert state["resolved_investigations"]["CURRENT_S34_W03_JOINT_LOCAL"]["status"] == "FROZEN_FREE_SPLIT_SUPPORT"
assert state["arsenal"]["S34_W03"] == "EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED_CURRENT_LOCAL_ROUTE_FROZEN_INTERSECTION_NOT_CLOSED"

for text in (
    "Pminus=W1*W2-V1*V2",
    "(a*m-b*n)^2+(a*n-b*m)^2",
    "Pplus =W1*W2+V1*V2",
    "(a*m+b*n)^2+(a*n+b*m)^2",
    "B35 => Lplus is a square in Q_2",
    "FREE-SPLIT-WITNESS",
    "CURRENT_S34_W03_JOINT_LOCAL_ROUTE=FROZEN_FREE_SPLIT_SUPPORT",
    "35EX-16_COPRIME_PAIR_GLOBAL_RECIPROCITY_OR_INDEPENDENT_SPLIT_ORIENTATIONS",
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
branch_survivors = []
for a, b in pairs1:
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    for m, n in pairs2:
        U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
        master = (V1*U2)**2 + (U1*V2)**2
        if not square(master):
            continue
        master_hits += 1

        p = gcd(W1, V2)
        d = gcd(V1, W2)
        pd = p * d
        assert p % 2 == d % 2 == 1 and gcd(p, d) == 1
        for ell in factor(pd):
            assert ell % 4 == 1

        Pminus = W1*W2 - V1*V2
        Pplus = W1*W2 + V1*V2
        assert Pminus == (a*m-b*n)**2 + (a*n-b*m)**2
        assert Pplus == (a*m+b*n)**2 + (a*n+b*m)**2
        assert Pminus % pd == Pplus % pd == 0

        Lminus = Pminus // pd
        Lplus = Pplus // pd
        assert Lminus > 0 and Lplus > 0
        assert Lminus % 2 == Lplus % 2 == 1
        assert gcd(Lminus, Lplus) == 1

        for ell, exponent in factor(Lminus).items():
            if ell % 4 == 3:
                assert exponent % 2 == 0
        for ell, exponent in factor(Lplus).items():
            if ell % 4 == 3:
                assert exponent % 2 == 0

        assert V1 % 4 == V2 % 4 == 0
        assert (Lplus - Lminus) % 32 == 0

        if square(Lminus):
            assert Lminus % 8 == 1
            assert Lplus % 8 == 1
            odd_squareclass_primes = [
                ell for ell, exponent in factor(Lplus).items()
                if exponent % 2 == 1
            ]
            assert all(ell % 4 == 1 for ell in odd_squareclass_primes)
            branch_survivors.append((a, b, m, n, Lminus, Lplus, odd_squareclass_primes))

assert master_hits == 131
assert branch_survivors == [
    (8, 5, 11, 2, 1521, 2929, [29, 101]),
    (11, 2, 8, 5, 1521, 2929, [29, 101]),
    (17, 16, 52, 47, 1089, 313921, [313921]),
]

# Exact fresh-support witness used by the route freeze.
a, b, m, n = (8, 5, 11, 2)
U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
assert (U1, V1, W1) == (39, 80, 89)
assert (U2, V2, W2) == (117, 44, 125)
assert square((V1*U2)**2 + (U1*V2)**2)
p = gcd(W1, V2)
d = gcd(V1, W2)
assert (p, d) == (1, 5)
Lminus = (W1*W2 - V1*V2) // (p*d)
Lplus = (W1*W2 + V1*V2) // (p*d)
assert Lminus == 39**2
assert Lplus == 29 * 101
source_odd_support = (
    set(factor(U1)) | set(factor(U2)) | set(factor(V1)) |
    set(factor(V2)) | set(factor(p)) | set(factor(d))
) - {2}
assert source_odd_support == {3, 5, 11, 13}
assert {29, 101}.isdisjoint(source_odd_support)
assert not square(Lplus)

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

print("PASS STAGE35_EX_15_JOINT_LOCAL_FREE_SPLIT_SUPPORT_V2_PROGRESSION_SAFE")
