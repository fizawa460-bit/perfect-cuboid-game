#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-17/product-hypotenuse-successor-or-no-self-map.md"
AUDIT = ROOT / "stages/stage35-ex/35ex-17/post-descent-fresh-breadth-audit.json"
HOOK = ROOT / "stages/stage35-ex/35ex-17/post-descent-gaussian-coordinate-gcd-hook.md"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def odd_prime_factors(n: int):
    n = abs(n)
    out = []
    q = 3
    while q*q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        out.append(n)
    return out


state = json.loads(STATE.read_text())
doc = DOC.read_text()
audit = json.loads(AUDIT.read_text())
hook = HOOK.read_text()

assert state["stage"] == "35-EX"
for unit_name in ("35EX-15", "35EX-16"):
    u = state["completed_units"][unit_name]
    assert u["status"].startswith("AUDITED_EXACT_")
    assert u["hostile_reaudit_review"] == 5108777053
    assert u["audited_head_sha"] == "b2fbe5f30c93259440829c3f99715d8cc3f73aa7"
    assert u["merged_main_sha"] == "b68af30918070f692d711e2cb377e750525e5e1e"
    assert u["audited_theorem_credit"] is False

unit17 = state["completed_units"]["35EX-17"]
assert unit17["status"] in {
    "PROVISIONAL_EXACT_PRODUCT_HYPOTENUSE_NO_SELF_MAP_FREEZE_NO_CREDIT",
    "AUDITED_EXACT_PRODUCT_HYPOTENUSE_NO_SELF_MAP_FREEZE_NO_CREDIT",
}
assert unit17["product_hypotenuse_primitive_triple_inherited"] is True
assert unit17["canonical_two_triple_reconstruction_proved"] is False
assert unit17["natural_successor_P_T2_requires_new_square_obligations"] is True
assert unit17["natural_successor_T1_P_requires_new_square_obligations"] is True
assert unit17["strict_well_founded_same_type_height_decrease_proved"] is False
assert unit17["all_product_hypotenuse_descents_ruled_out_in_principle"] is False
assert unit17["infinite_descent_proved"] is False
assert unit17["audited_theorem_credit"] is False

unit17b = state["completed_units"]["35EX-17B"]
assert unit17b["status"] in {
    "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT",
    "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT",
}
assert unit17b["exhaustive_view_audit"] is True
assert unit17b["blind_rediscovery"] is True
assert unit17b["arsenal_comparison"] is True
assert unit17b["historical_block_ledger_comparison"] is True
assert unit17b["selected_next_unit"] == "35EX-18_GAUSSIAN_COORDINATE_GCD_SPLIT_OR_MOVING_ORIENTATION"
assert unit17b["audited_theorem_credit"] is False

assert audit["schema"] == "STAGE35_EX_17B_POST_DESCENT_FRESH_BREADTH_AUDIT_V2"
assert audit["cycle_exit"]["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert audit["cycle_exit"]["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert audit["cycle_exit"]["CYCLE_BLIND_REDISCOVERY"] is True
assert audit["cycle_exit"]["CYCLE_LIVE_CANDIDATES"] == 1
assert audit["cycle_exit"]["CYCLE_UNTESTED_CANDIDATES"] == 1
assert audit["selection"]["selected_candidate"] == "E1-GAUSSIAN-COORDINATE-GCD-SPLIT"
assert audit["selection"]["selected_next_unit"] == "35EX-18_GAUSSIAN_COORDINATE_GCD_SPLIT_OR_MOVING_ORIENTATION"
new_hook = audit["new_exact_hook_for_selected_candidate"]
assert new_hook["gminus_gplus_equals_c"] is True
assert new_hook["gminus_gplus_coprime"] is True
assert new_hook["full_receiver_primitive_pd_twisted_norms_proved"] is True
assert new_hook["pd_odd_prime_support_split_only"] is True

# Successor-safe routing assertions: the audited 35EX-17B selection remains
# exact even after 35EX-18 records its provisional result and queues 35EX-19.
assert state["current"]["unit"] in {
    "35EX-18_GAUSSIAN_COORDINATE_GCD_SPLIT_OR_MOVING_ORIENTATION",
    "35EX-19_RECEIVER_SPECIFIC_GENUSONE_ADAPTER_OR_BLOCKER",
}
assert state["candidate_ledger_after_fresh_breadth_audit"]["selected_live"] in {
    "E1-GAUSSIAN-COORDINATE-GCD-SPLIT",
    "E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION",
}
assert state["candidate_ledger_after_fresh_breadth_audit"]["untested"] in {
    ("E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION",),
    (),
}

for text in (
    "PRODUCT_HYPOTENUSE_CANONICAL_TWO_TRIPLE_RECONSTRUCTION=false",
    "CURRENT_PRODUCT_HYPOTENUSE_SELF_MAP_ROUTE=FROZEN_NO_CANONICAL_SAME_TYPE_SUCCESSOR",
    "NATURAL_SUCCESSOR_P_T2_REQUIRES_NEW_SQUARE_OBLIGATIONS=true",
    "NATURAL_SUCCESSOR_T1_P_REQUIRES_NEW_SQUARE_OBLIGATIONS=true",
    "STRICT_WELL_FOUNDED_SAME_TYPE_HEIGHT_DECREASE_PROVED=false",
    "ALL_PRODUCT_HYPOTENUSE_DESCENTS_RULED_OUT_IN_PRINCIPLE=false",
    "INFINITE_DESCENT_PROVED=false",
):
    assert text in doc

for text in (
    "gminus*gplus=c",
    "gcd(gminus,gplus)=1",
    "Norm(zminus0)=p*d*X^2",
    "Norm(zplus0) =p*d*Y^2",
    "GAUSSIAN_COORDINATE_GCD_SPLIT_PROVED=true",
    "MASTER_GAUSSIAN_FORCES_ORIENTATION_CONTRADICTION=false",
):
    assert text in hook

# Deterministic exact regression for both the 35EX-17 identities and the fresh
# 35EX-17B coordinate-gcd theorem. The algebraic proof is in the source note;
# this panel protects signs, normalizations, and prime-support implementation.
checked = 0
product_triples = 0
for a in range(2, 31):
    for b in range(1, a):
        if gcd(a, b) != 1 or (a - b) % 2 != 1:
            continue
        U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
        for m in range(2, 61):
            for n in range(1, m):
                if gcd(m, n) != 1 or (m - n) % 2 != 1:
                    continue
                U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
                c = gcd(U1, U2)
                p = gcd(W1, V2)
                d = gcd(V1, W2)
                pd = p*d
                assert gcd(c, pd) == 1
                for ell in odd_prime_factors(pd):
                    assert ell % 4 == 1

                E2 = W1*W1*W2*W2 - V1*V1*V2*V2
                assert E2 == (W1*U2)**2 + (U1*V2)**2

                # Candidate A=(P,T2): after removing a rational square factor.
                assert (V1*U2)**2 + E2 == (U1*W2)**2 + 2*(V1*U2)**2
                assert (W1*W2*U2)**2 + E2*V2*V2 == (W1*W2*W2)**2 - (V1*V2*V2)**2

                # Candidate B=(T1,P): likewise after removing a rational square.
                assert E2 + (U1*V2)**2 == (W1*U2)**2 + 2*(U1*V2)**2
                assert W1*W1*E2 + (U1*V1*V2)**2 == (W1*W1*W2)**2 - (V1*V1*V2)**2

                zm_r, zm_i = a*m-b*n, a*n-b*m
                zp_r, zp_i = a*m+b*n, a*n+b*m
                gminus = gcd(abs(zm_r), abs(zm_i))
                gplus = gcd(abs(zp_r), abs(zp_i))
                assert gcd(gminus, gplus) == 1
                assert gminus*gplus == c

                Pminus = W1*W2 - V1*V2
                Pplus = W1*W2 + V1*V2
                assert zm_r*zm_r + zm_i*zm_i == Pminus
                assert zp_r*zp_r + zp_i*zp_i == Pplus
                assert Pminus % pd == Pplus % pd == 0
                Lminus = Pminus // pd
                Lplus = Pplus // pd

                # Whenever the raw E1 norm is a square, reconstruct both the
                # product triple and the exact primitive p*d-twisted norms.
                if square(E2):
                    assert square(Lminus) and square(Lplus)
                    x, y = isqrt(Lminus), isqrt(Lplus)
                    assert x % gminus == 0
                    assert y % gplus == 0
                    X, Y = x//gminus, y//gplus
                    zm0_r, zm0_i = zm_r//gminus, zm_i//gminus
                    zp0_r, zp0_i = zp_r//gplus, zp_i//gplus
                    assert gcd(abs(zm0_r), abs(zm0_i)) == 1
                    assert gcd(abs(zp0_r), abs(zp0_i)) == 1
                    assert zm0_r*zm0_r + zm0_i*zm0_i == pd*X*X
                    assert zp0_r*zp0_r + zp0_i*zp0_i == pd*Y*Y

                    R, S = (y+x)//2, (y-x)//2
                    U3 = isqrt(E2) // pd
                    V3 = V1*V2 // pd
                    W3 = W1*W2 // pd
                    assert U3 == R*R-S*S
                    assert V3 == 2*R*S
                    assert W3 == R*R+S*S
                    assert U3*U3 + V3*V3 == W3*W3
                    assert gcd(U3, V3) == gcd(U3, W3) == gcd(V3, W3) == 1
                    product_triples += 1
                checked += 1

assert checked > 100000
assert product_triples > 0

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

print("PASS STAGE35_EX_17_FREEZE_AND_FRESH_GAUSSIAN_GCD_HOOK")
