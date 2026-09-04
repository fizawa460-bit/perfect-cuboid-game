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

assert state["stage"] == "35-EX"

unit14 = state["completed_units"]["35EX-14"]
assert unit14["status"] == "AUDITED_EXACT_COPRIME_E1_RECEIVER_FACTORIZATION_NO_CREDIT"
assert unit14["hostile_audit_review"] == 5108445565
assert unit14["audited_head_sha"] == "ff502d2c9455ce60b4030843947e16e5bc84057c"
assert unit14["merged_main_sha"] == "6d4354ca7e3d8162ad2f97d7aab086858c061503"
assert unit14["audited_theorem_credit"] is False

# Progression-safe: 35EX-15 may be provisional at its audit head or promoted
# after hostile re-audit/merge. Verify the recorded result, not the downstream
# current leaf or cosmetic controller wording.
unit15 = state["completed_units"]["35EX-15"]
assert unit15["status"] in {
    "PROVISIONAL_EXACT_JOINT_LOCAL_FREE_SPLIT_SUPPORT_NO_CREDIT",
    "AUDITED_EXACT_JOINT_LOCAL_FREE_SPLIT_SUPPORT_NO_CREDIT",
}
if unit15["status"].startswith("AUDITED_"):
    assert unit15["hostile_reaudit_review"] == 5108777053
    assert unit15["audited_head_sha"] == "b2fbe5f30c93259440829c3f99715d8cc3f73aa7"
    assert unit15["merged_main_sha"] == "b68af30918070f692d711e2cb377e750525e5e1e"
assert unit15["residual_squareclass_split_only"] is True
assert unit15["B35_implies_Lplus_Q2_square"] is True
assert unit15["real_place_automatic"] is True
assert unit15["S34_W03_exact_branch_receiver_adapter_matched"] is True
assert unit15["S34_W03_receiver_intersection_closed"] is False
assert unit15["current_S34_W03_joint_local_route_frozen_free_split_support"] is True
assert unit15["all_future_local_global_arguments_ruled_out"] is False
assert unit15["audited_theorem_credit"] is False

assert state["resolved_investigations"]["CURRENT_S34_W03_JOINT_LOCAL"]["status"] == "FROZEN_FREE_SPLIT_SUPPORT"
ledger = state["candidate_ledger_after_fresh_breadth_audit"]
assert (
    "E1-COPRIME-RECEIVER-JOINT-LOCAL" in ledger.get("just_frozen", [])
    or "E1-COPRIME-RECEIVER-JOINT-LOCAL" in ledger.get("blocked", [])
)
assert state["arsenal"]["S34_W03"] in {
    "EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED_CURRENT_LOCAL_ROUTE_FROZEN_INTERSECTION_NOT_CLOSED",
    "EXACT_BRANCH_RECEIVER_ADAPTER_MATCHED_CURRENT_DIRECT_LOCAL_ROUTE_FROZEN_INTERSECTION_NOT_CLOSED",
}
assert state["arsenal"]["matching_global_reciprocity_Hilbert_Jacobi_card_found"] is False

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
        pd = p*d
        Lminus = (W1*W2 - V1*V2)//pd
        Lplus = (W1*W2 + V1*V2)//pd

        if square(Lminus):
            assert Lplus % 8 == 1
            assert all(ell % 4 == 1 for ell, exp in factor(Lplus).items() if exp % 2)
            branch_survivors.append((a,b,m,n,Lminus,Lplus))

assert master_hits == 131
assert [(r[0],r[1],r[2],r[3]) for r in branch_survivors] == [
    (8,5,11,2),
    (11,2,8,5),
    (17,16,52,47),
]
assert branch_survivors[0][4] == 39**2
assert branch_survivors[0][5] == 29*101

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

print("PASS STAGE35_EX_15_JOINT_LOCAL_FREE_SPLIT_SUPPORT_V3_PROGRESSION_SAFE")
