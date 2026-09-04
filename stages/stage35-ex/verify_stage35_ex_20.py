#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-20/paired-quartic-squareclass-moving-support-blocker.md"
AUDIT = ROOT / "stages/stage35-ex/35ex-20/post-paired-squareclass-breadth-audit.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def v2(n: int) -> int:
    n = abs(n)
    assert n != 0
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def prime_factors(n: int):
    n = abs(n)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e % 2:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


doc = DOC.read_text()
audit = json.loads(AUDIT.read_text())
state = json.loads(STATE.read_text())

V19 = "STAGE35_EX_PESCH_E1_STATE_V19_POST_35EX20_PAIRED_SQUARECLASS_DYNAMIC_SUPPORT_BLOCKER"
V20 = "STAGE35_EX_PESCH_E1_STATE_V20_POST_35EX21_GLOBAL_NORMALIZED_CUBOID_SURFACE"
V21 = "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
V22 = "STAGE35_EX_PESCH_E1_STATE_V22_POST_35EX23_GENUS5_CHARACTER_QUOTIENT_UNIFORMITY_BLOCKER"
assert state["schema"] in {V19, V20, V21, V22}
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] in {
    "fd0986693a8806fb77083c862d0f939d23a05abb",
    "24438151cf76be42612b7df83314630e51c61682",
    "85e12c7b810eaafc13e663a0047111b7f3333e8b",
    "ea51d06f3fe46b134e98a065332e9c70fcec57f0",
    "378096fa313b582b63553b395ec85a5c86de2685",
    "2e07dde92fdf270fff1233635a7cb4cea1427080",
}

unit19 = state["completed_units"]["35EX-19"]
assert unit19["status"] == "AUDITED_EXACT_NONISOTRIVIAL_GENUSONE_FAMILY_BLOCKER_NEW_PAIRED_QUARTIC_HOOK_NO_CREDIT"
assert unit19["hostile_audit_verdict"] == "PASS"
assert unit19["audited_head_sha"] == "b63fcf4f7888f86f6881d15f5e5bd9d3873dc1b5"
assert unit19["merged_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
assert unit19["audited_theorem_credit"] is False
unit19b = state["completed_units"]["35EX-19B"]
assert unit19b["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert unit19b["hostile_audit_verdict"] == "PASS"
assert unit19b["audited_head_sha"] == "b63fcf4f7888f86f6881d15f5e5bd9d3873dc1b5"
assert unit19b["merged_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
assert unit19b["selected_next_unit"] == "35EX-20_PAIRED_SOURCE_FILTER_QUARTIC_SQUARECLASS_OR_FREE_FAMILY"
assert unit19b["audited_theorem_credit"] is False

unit20 = state["completed_units"]["35EX-20"]
assert unit20["status"] in {"PROVISIONAL_EXACT_PAIRED_QUARTIC_SQUARECLASS_DYNAMIC_UV_SUPPORT_BLOCKER_NO_CREDIT","AUDITED_EXACT_PAIRED_QUARTIC_SQUARECLASS_DYNAMIC_UV_SUPPORT_BLOCKER_NO_CREDIT"}
assert unit20["artifact"] == "stages/stage35-ex/35ex-20/paired-quartic-squareclass-moving-support-blocker.md"
assert unit20["breadth_audit"] == "stages/stage35-ex/35ex-20/post-paired-squareclass-breadth-audit.json"
assert unit20["verifier"] == "stages/stage35-ex/verify_stage35_ex_20.py"
for key in ("pair_source_square_identity_proved","primitive_integer_four_factor_model_proved","pairwise_gcd_resultant_support_proved","fixed_first_source_squareclass_overcover_proved","y_branch_odd_support_split_only","pair_2adic_branch_bookkeeping_proved"):
    assert unit20[key] is True
assert unit20["uniform_fixed_squareclass_support_proved"] is False
assert unit20["S34_W01_global_finite_exhaustive_family_unlocked"] is False
assert unit20["all_paired_quartic_descents_ruled_out_in_principle"] is False
assert unit20["audited_theorem_credit"] is False
unit20b = state["completed_units"]["35EX-20B"]
assert unit20b["status"] in {"PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT","AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"}
assert unit20b["exhaustive_view_audit"] is True
assert unit20b["blind_rediscovery"] is True
assert unit20b["arsenal_comparison"] is True
assert unit20b["selected_candidate"] == "E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY"
assert unit20b["selected_next_unit"] == "35EX-21_GLOBAL_BIQUADRATIC_SURFACE_MODEL_OR_GEOMETRY_BLOCKER"
assert unit20b["preserved_untested_candidates"] == ["E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"]
assert unit20b["audited_theorem_credit"] is False

parent = state["parent_authority"]
if state["schema"] == V19:
    assert parent["unit"] == "35EX-19B"
    assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["audited_head_sha"] == "b63fcf4f7888f86f6881d15f5e5bd9d3873dc1b5"
    assert parent["merged_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
    assert parent["audited_theorem_credit"] is False
    assert state["base_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
    assert unit20["status"].startswith("PROVISIONAL_")
    assert unit20b["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
elif state["schema"] == V20:
    assert parent["unit"] == "35EX-20B"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["hostile_audit_review"] == 5109942390
    assert parent["audited_head_sha"] == "1a45fc6fca779cb22794e305e044aa37e62e76ef"
    assert parent["merged_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
    assert state["base_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
elif state["schema"] == V21:
    assert parent["unit"] == "35EX-21B"
    assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["hostile_audit_review"] == 5110646292
    assert parent["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
    assert parent["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
    assert state["base_main_sha"] == "378096fa313b582b63553b395ec85a5c86de2685"
else:
    assert parent["unit"] == "35EX-22"
    assert parent["status"] == "AUDITED_EXACT_OBVIOUS_BRAUER_SYMBOL_LAYER_BLOCKER_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["hostile_audit_review"] == 5111539148
    assert parent["audited_head_sha"] == "f4276680239bb2b84687f8ba8ac8964de0613552"
    assert parent["merged_main_sha"] == "2e07dde92fdf270fff1233635a7cb4cea1427080"
    assert parent["audited_theorem_credit"] is False
    assert state["base_main_sha"] == "2e07dde92fdf270fff1233635a7cb4cea1427080"

for old in (unit20, unit20b):
    if state["schema"] in {V20, V21, V22}:
        assert old["hostile_audit_verdict"] == "PASS"
        assert old["hostile_audit_review"] == 5109942390
        assert old["audited_head_sha"] == "1a45fc6fca779cb22794e305e044aa37e62e76ef"
        assert old["merged_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"

freeze = state["resolved_investigations"]["CURRENT_PAIRED_QUARTIC_SQUARECLASS"]
assert freeze["status"] == "FROZEN_DYNAMIC_UV_SUPPORT_NO_GLOBAL_FINITE_FAMILY"
assert "U1*V1" in freeze["reason"]
assert "uniform" in freeze["reopen_condition"]
ledger = state["candidate_ledger_after_fresh_breadth_audit"]
assert ledger["selected_live"] in {"E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY","E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"}
assert "E1-PAIRED-SOURCE-FILTER-QUARTIC-INTERSECTION" in ledger["just_frozen"]
assert "E1-PAIRED-SOURCE-FILTER-QUARTIC-INTERSECTION" in ledger["blocked"]
assert ledger["audit_artifact"] in {"stages/stage35-ex/35ex-20/post-paired-squareclass-breadth-audit.json","stages/stage35-ex/35ex-21/post-global-surface-breadth-audit.json"}
assert unit20b["preserved_untested_candidates"] == [ledger["selected_live"]]
current = state["current"]
assert current["unit"] in {"35EX-21_GLOBAL_BIQUADRATIC_SURFACE_MODEL_OR_GEOMETRY_BLOCKER","35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER","35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER"}
assert state["arsenal"]["S34_W01"] == "FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT"
assert state["arsenal"]["S31_W01"] in {"FIBERWISE_ROUTING_ONLY_GLOBAL_FIXED_CURVE_USE_BLOCKED_BY_NONISOTRIVIAL_K","GENUS_ONE_CHARACTER_QUOTIENT_FIBERWISE_ROUTING_ONLY_NO_UNIFORM_SURFACE_CLOSURE"}
assert state["arsenal"]["matching_formal_global_surface_classification_card_found"] is False
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False
for key in ("new_theorem_credit","R29_PESCH_E1_closed","R29_FIB2_closed","J12_PARAMETRIC_closed","stage35_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"):
    assert state["claims"][key] is False
for marker in ("PAIR_SOURCE_SQUARE_IDENTITY_PROVED=true","PRIMITIVE_INTEGER_FOUR_FACTOR_MODEL_PROVED=true","PAIRWISE_GCD_RESULTANT_SUPPORT_PROVED=true","FIXED_FIRST_SOURCE_SQUARECLASS_OVERCOVER_PROVED=true","Y_BRANCH_ODD_SUPPORT_SPLIT_ONLY=true","PAIR_2ADIC_BRANCH_BOOKKEEPING_PROVED=true","UNIFORM_FIXED_SQUARECLASS_SUPPORT_PROVED=false","S34_W01_GLOBAL_FINITE_EXHAUSTIVE_FAMILY_UNLOCKED=false","CURRENT_PAIRED_QUARTIC_SQUARECLASS_ROUTE=FROZEN_DYNAMIC_UV_SUPPORT_NO_GLOBAL_FINITE_FAMILY","ALL_PAIRED_QUARTIC_DESCENTS_RULED_OUT_IN_PRINCIPLE=false","E1_PROVED=false"):
    assert marker in doc
assert audit["schema"] == "STAGE35_EX_20B_POST_PAIRED_SQUARECLASS_BREADTH_AUDIT_V1"
assert audit["blind_rediscovery"]["performed_before_arsenal_comparison_for_this_audit"] is True
assert audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY"
assert audit["selection"]["selected_next_unit"] == "35EX-21_GLOBAL_BIQUADRATIC_SURFACE_MODEL_OR_GEOMETRY_BLOCKER"
assert audit["selection"]["preserved_untested_candidates"] == ["E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"]
generated = audit["blind_rediscovery"]["generated"]
allowed_candidate_statuses = {"LIVE", "UNTESTED", "EQUIVALENT", "DOMINATED", "BLOCKED"}
assert all(candidate["status"] in allowed_candidate_statuses for candidate in generated)
dependent = next(candidate for candidate in generated if candidate["id"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER")
assert dependent["status"] == "UNTESTED"
assert "requires the LIVE global-surface model" in dependent["dependency"]
cycle = audit["cycle_exit"]
assert cycle["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert cycle["CYCLE_LIVE_CANDIDATES"] == 1
assert cycle["CYCLE_UNTESTED_CANDIDATES"] == 1
assert cycle["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert cycle["CYCLE_BLIND_REDISCOVERY"] is True
assert cycle["CYCLE_SPLIT_TRIGGERED"] is False
assert cycle["CYCLE_PARKING_AUDIT_COMPLETE"] is False
assert cycle["CYCLE_NEW_VIEW_SOURCE"] == "BLIND"

checked = 0
split_checks = 0
z_orientation_checks = 0
square_product_checks = 0
for aa in range(2, 22):
    for bb in range(1, aa):
        if gcd(aa, bb) != 1 or (aa - bb) % 2 != 1:
            continue
        U = aa * aa - bb * bb
        V = 2 * aa * bb
        W = aa * aa + bb * bb
        e = U - V
        f = U + V
        assert U % 2 == W % 2 == 1
        assert V % 4 == 0
        assert gcd(U, V) == gcd(U, W) == gcd(V, W) == 1
        assert gcd(e, f) == gcd(abs(e), W) == gcd(f, W) == 1
        assert W * W - 2 * U * V == e * e
        assert W * W + 2 * U * V == f * f
        assert f * f - e * e == 4 * U * V
        assert e * e + f * f == 2 * W * W
        for P in range(1, 24):
            for Q in range(1, 18):
                if gcd(P, Q) != 1:
                    continue
                A = P * P + Q * Q * e * e
                B = P * P + Q * Q * f * f
                C = P * P - Q * Q * f * f
                D = P * P - Q * Q * e * e
                if C == 0 or D == 0:
                    continue
                assert gcd(A, Q) == gcd(B, Q) == gcd(abs(C), Q) == gcd(abs(D), Q) == 1
                assert (B - A) == 4 * Q * Q * U * V
                assert (D - C) == 4 * Q * Q * U * V
                assert (A - C) == 2 * Q * Q * W * W
                assert (B - D) == 2 * Q * Q * W * W
                assert (A - D) == 2 * Q * Q * e * e
                assert (B - C) == 2 * Q * Q * f * f
                assert (4 * U * V) % gcd(A, B) == 0
                assert (4 * U * V) % gcd(abs(C), abs(D)) == 0
                assert (2 * W * W) % gcd(A, abs(C)) == 0
                assert (2 * W * W) % gcd(B, abs(D)) == 0
                assert oddpart(gcd(A, abs(D))) == gcd(P, abs(e)) ** 2
                assert oddpart(gcd(B, abs(C))) == gcd(P, f) ** 2
                if (P + Q) % 2 == 1:
                    assert A % 2 == B % 2 == C % 2 == D % 2 == 1
                else:
                    assert P % 2 == Q % 2 == 1
                    assert v2(A) == v2(B) == 1
                    assert v2(C) >= 3 and v2(D) >= 3
                if square(A * B):
                    dA = squarefree_kernel(A)
                    dB = squarefree_kernel(B)
                    assert dA == dB
                    assert oddpart(U * V) % oddpart(dA) == 0
                    for ell in prime_factors(oddpart(dA)):
                        assert ell % 4 == 1
                        split_checks += 1
                    square_product_checks += 1
                if C * D > 0 and square(C * D):
                    dC = squarefree_kernel(abs(C))
                    dD = squarefree_kernel(abs(D))
                    assert dC == dD
                    assert oddpart(U * V) % oddpart(dC) == 0
                    if P % 2 == Q % 2 == 1:
                        assert v2(C) % 2 == v2(D) % 2
                        assert (dC % 2 == 0) == (v2(C) % 2 == 1)
                    for ell in prime_factors(oddpart(dC)):
                        if U % ell == 0:
                            assert (P - Q * V) % ell == 0 or (P + Q * V) % ell == 0
                        elif V % ell == 0:
                            assert (P - Q * U) % ell == 0 or (P + Q * U) % ell == 0
                        else:
                            raise AssertionError((aa, bb, P, Q, ell))
                        z_orientation_checks += 1
                    square_product_checks += 1
                if square(A * B) and C * D > 0 and square(C * D):
                    dY = squarefree_kernel(A)
                    dZ = squarefree_kernel(abs(C))
                    assert gcd(oddpart(dY), oddpart(dZ)) == 1
                checked += 1
assert checked > 20000
assert square_product_checks > 0
assert split_checks > 0
assert z_orientation_checks > 0
prod = 1
for prime in (3, 5, 7, 11, 13):
    prod *= prime
    aa = 2 * prod
    bb = 1
    assert gcd(aa, bb) == 1 and (aa - bb) % 2 == 1
    U = aa * aa - 1
    V = 2 * aa
    W = aa * aa + 1
    assert gcd(U, V) == gcd(U, W) == gcd(V, W) == 1
    for divisor in prime_factors(prod):
        assert V % divisor == 0
print("PASS STAGE35_EX_20_PAIRED_QUARTIC_SQUARECLASS_DYNAMIC_UV_SUPPORT_BLOCKER")