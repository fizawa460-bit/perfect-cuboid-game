#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-19/receiver-specific-genusone-family-blocker.md"
AUDIT = ROOT / "stages/stage35-ex/35ex-19/post-genusone-breadth-audit.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
audit = json.loads(AUDIT.read_text())
state = json.loads(STATE.read_text())

V18 = "STAGE35_EX_PESCH_E1_STATE_V18_POST_35EX19_NONISOTRIVIAL_GENUSONE_BLOCKER"
V19 = "STAGE35_EX_PESCH_E1_STATE_V19_POST_35EX20_PAIRED_SQUARECLASS_DYNAMIC_SUPPORT_BLOCKER"
V20 = "STAGE35_EX_PESCH_E1_STATE_V20_POST_35EX21_GLOBAL_NORMALIZED_CUBOID_SURFACE"
V21 = "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
V22 = "STAGE35_EX_PESCH_E1_STATE_V22_POST_35EX23_GENUS5_CHARACTER_QUOTIENT_UNIFORMITY_BLOCKER"
assert state["schema"] in {V18, V19, V20, V21, V22}
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] in {
    "751ac2ed47843223340b2d9b09db3d5cca8c3464",
    "fd0986693a8806fb77083c862d0f939d23a05abb",
    "24438151cf76be42612b7df83314630e51c61682",
    "85e12c7b810eaafc13e663a0047111b7f3333e8b",
    "ea51d06f3fe46b134e98a065332e9c70fcec57f0",
    "378096fa313b582b63553b395ec85a5c86de2685",
    "2e07dde92fdf270fff1233635a7cb4cea1427080",
    "7a5d01b438c68c228ad73955f906f3128780d6ef",
}

unit18 = state["completed_units"]["35EX-18"]
assert unit18["status"] == "AUDITED_EXACT_GAUSSIAN_RELATIVE_ORIENTATION_MASTER_UNIT_FREEZE_NO_CREDIT"
assert unit18["hostile_audit_verdict"] == "PASS"
assert unit18["audited_head_sha"] == "4f271921e745e90ff9764c727d0d4234d2ae0b4a"
assert unit18["merged_main_sha"] == "cb3e36183f291ec5d96b440ff2287e3d009d9691"
assert unit18["audited_theorem_credit"] is False

unit19 = state["completed_units"]["35EX-19"]
assert unit19["status"] in {
    "PROVISIONAL_EXACT_NONISOTRIVIAL_GENUSONE_FAMILY_BLOCKER_NEW_PAIRED_QUARTIC_HOOK_NO_CREDIT",
    "AUDITED_EXACT_NONISOTRIVIAL_GENUSONE_FAMILY_BLOCKER_NEW_PAIRED_QUARTIC_HOOK_NO_CREDIT",
}
assert unit19["artifact"] == "stages/stage35-ex/35ex-19/receiver-specific-genusone-family-blocker.md"
assert unit19["breadth_audit"] == "stages/stage35-ex/35ex-19/post-genusone-breadth-audit.json"
assert unit19["verifier"] == "stages/stage35-ex/verify_stage35_ex_19.py"
assert unit19["fixed_r_genus_one_quartic_derived"] is True
assert unit19["fixed_r_fiber_adapter_proved"] is True
assert unit19["all_admissible_fibers_smooth_genus_one"] is True
assert unit19["genus_one_j_invariant_nonconstant"] is True
assert unit19["global_fixed_genus_one_model_derived"] is False
assert unit19["S31_W01_global_use_unlocked"] is False
assert unit19["paired_source_filter_quartics_derived"] is True
assert unit19["paired_quartic_contradiction_proved"] is False
assert unit19["audited_theorem_credit"] is False

unit19b = state["completed_units"]["35EX-19B"]
assert unit19b["status"] in {
    "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT",
    "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT",
}
assert unit19b["exhaustive_view_audit"] is True
assert unit19b["blind_rediscovery"] is True
assert unit19b["arsenal_comparison"] is True
assert unit19b["selected_next_unit"] == "35EX-20_PAIRED_SOURCE_FILTER_QUARTIC_SQUARECLASS_OR_FREE_FAMILY"
assert unit19b["selected_candidate"] == "E1-PAIRED-SOURCE-FILTER-QUARTIC-INTERSECTION"
assert unit19b["preserved_untested_candidates"] == ["E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY"]
assert unit19b["audited_theorem_credit"] is False

if state["schema"] == V18:
    parent = state["parent_authority"]
    assert parent["unit"] == "35EX-18"
    assert parent["status"] == "AUDITED_EXACT_GAUSSIAN_RELATIVE_ORIENTATION_MASTER_UNIT_FREEZE_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["audited_head_sha"] == "4f271921e745e90ff9764c727d0d4234d2ae0b4a"
    assert parent["merged_main_sha"] == "cb3e36183f291ec5d96b440ff2287e3d009d9691"
    assert state["base_main_sha"] == "751ac2ed47843223340b2d9b09db3d5cca8c3464"
    assert unit19["status"].startswith("PROVISIONAL_")
    assert unit19b["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
elif state["schema"] == V19:
    parent = state["parent_authority"]
    assert parent["unit"] == "35EX-19B"
    assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["audited_head_sha"] == "b63fcf4f7888f86f6881d15f5e5bd9d3873dc1b5"
    assert parent["merged_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
    assert parent["audited_theorem_credit"] is False
    assert state["base_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"
elif state["schema"] == V20:
    assert state["base_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
elif state["schema"] == V21:
    assert state["base_main_sha"] == "378096fa313b582b63553b395ec85a5c86de2685"
else:
    assert state["base_main_sha"] == "7a5d01b438c68c228ad73955f906f3128780d6ef"

for old in (unit19, unit19b):
    if state["schema"] in {V19, V20, V21, V22}:
        assert old["hostile_audit_verdict"] == "PASS"
        assert old["audited_head_sha"] == "b63fcf4f7888f86f6881d15f5e5bd9d3873dc1b5"
        assert old["merged_main_sha"] == "fd0986693a8806fb77083c862d0f939d23a05abb"

freeze = state["resolved_investigations"]["CURRENT_RECEIVER_SPECIFIC_FIXED_GENUSONE"]
assert freeze["status"] == "FROZEN_NONISOTRIVIAL_MOVING_SOURCE_PARAMETER"
assert "fixed source parameter" in freeze["reopen_condition"]
assert "uniform" in freeze["reopen_condition"]

ledger = state["candidate_ledger_after_fresh_breadth_audit"]
assert ledger["selected_live"] in {
    "E1-PAIRED-SOURCE-FILTER-QUARTIC-INTERSECTION",
    "E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY",
    "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER",
}
assert "E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION" in ledger["just_frozen"]
assert "E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION" in ledger["blocked"]
assert ledger["audit_artifact"] in {
    "stages/stage35-ex/35ex-19/post-genusone-breadth-audit.json",
    "stages/stage35-ex/35ex-20/post-paired-squareclass-breadth-audit.json",
    "stages/stage35-ex/35ex-21/post-global-surface-breadth-audit.json",
}

current = state["current"]
assert current["unit"] in {
    "35EX-20_PAIRED_SOURCE_FILTER_QUARTIC_SQUARECLASS_OR_FREE_FAMILY",
    "35EX-21_GLOBAL_BIQUADRATIC_SURFACE_MODEL_OR_GEOMETRY_BLOCKER",
    "35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER",
    "35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER",
}
assert state["arsenal"]["S31_W01"] in {
    "FIBERWISE_ROUTING_ONLY_GLOBAL_FIXED_CURVE_USE_BLOCKED_BY_NONISOTRIVIAL_K",
    "GENUS_ONE_CHARACTER_QUOTIENT_FIBERWISE_ROUTING_ONLY_NO_UNIFORM_SURFACE_CLOSURE",
}
assert state["arsenal"]["S34_W01"] in {
    "SELECTED_ROUTING_PATTERN_FOR_35EX20_PAIRED_QUARTIC_NOT_YET_UNLOCKED",
    "FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT",
}
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

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

for marker in (
    "FIXED_R_GENUS_ONE_QUARTIC_DERIVED=true",
    "FIXED_R_QUARTIC_SMOOTH_GENUS_ONE=true",
    "GENUS_ONE_J_INVARIANT_NONCONSTANT=true",
    "GLOBAL_FIXED_GENUS_ONE_MODEL_DERIVED=false",
    "CURRENT_RECEIVER_SPECIFIC_FIXED_GENUSONE_ROUTE=FROZEN_NONISOTRIVIAL_MOVING_SOURCE_PARAMETER",
    "S31_W01_GLOBAL_35EX19_USE_BLOCKED=true",
    "PAIRED_SOURCE_FILTER_QUARTICS_DERIVED=true",
    "PAIRED_QUARTIC_CONTRADICTION_PROVED=false",
    "E1_PROVED=false",
):
    assert marker in doc

assert audit["schema"] == "STAGE35_EX_19B_POST_GENUSONE_BLOCKER_BREADTH_AUDIT_V1"
assert audit["blind_rediscovery"]["performed_before_arsenal_comparison_for_new_candidates"] is True
assert audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-PAIRED-SOURCE-FILTER-QUARTIC-INTERSECTION"
assert audit["selection"]["selected_next_unit"] == "35EX-20_PAIRED_SOURCE_FILTER_QUARTIC_SQUARECLASS_OR_FREE_FAMILY"
assert audit["selection"]["preserved_untested_candidates"] == ["E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY"]
cycle = audit["cycle_exit"]
assert cycle["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert cycle["CYCLE_LIVE_CANDIDATES"] == 1
assert cycle["CYCLE_UNTESTED_CANDIDATES"] == 1
assert cycle["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert cycle["CYCLE_BLIND_REDISCOVERY"] is True
assert cycle["CYCLE_SPLIT_TRIGGERED"] is False
assert cycle["CYCLE_PARKING_AUDIT_COMPLETE"] is False

r, u = sp.symbols("r u", nonzero=True)
k = 1 - 2*r**2
den = k - u**2
t = 2*r*u/den
mu = r*(k + u**2)/den
assert sp.factor(mu**2 - (r**2 + k*t**2)) == 0
quartic_plus = sp.expand(den**2 + 4*(1-r**2)*u**2)
assert sp.factor(quartic_plus - (u**4 + 2*u**2 + k**2)) == 0
quartic_minus = sp.expand(den**2 - 4*r**2*u**2)
assert sp.factor(quartic_minus - (u**4 - 2*u**2 + k**2)) == 0
assert sp.expand((u**4 + 2*u**2 + k**2) - (u**4 - 2*u**2 + k**2)) == 4*u**2
sigma2 = 4*r**2*(1-r**2)
assert sp.factor(k**2 + sigma2 - 1) == 0
assert sp.expand((u**2+1)**2 - sigma2 - (u**4+2*u**2+k**2)) == 0
assert sp.expand((u**2-1)**2 - sigma2 - (u**4-2*u**2+k**2)) == 0
K = sp.symbols("K")
f = u**4 + 2*u**2 + K**2
disc = sp.factor(sp.discriminant(f, u))
assert disc == 256*K**2*(K-1)**2*(K+1)**2
I = 4*(1+3*K**2)
J = 16*(9*K**2-1)
Delta = sp.factor((4*I**3-J**2)/27)
assert sp.factor(Delta - 256*K**2*(1-K**2)**2) == 0
j = sp.factor(2**8 * I**3 / Delta)
assert sp.factor(j - 64*(1+3*K**2)**3/(K**2*(1-K**2)**2)) == 0
assert sp.diff(j, K) != 0

def j_fraction(kv: Fraction) -> Fraction:
    return Fraction(64) * (1 + 3*kv*kv)**3 / (kv*kv * (1-kv*kv)**2)

k43 = Fraction(527, 625)
k85 = Fraction(4879, 7921)
assert k43 != k85
assert j_fraction(k43) != j_fraction(k85)
for a, b in ((2,1), (4,3), (8,5), (9,8), (11,2)):
    rr = Fraction(a*a-b*b, a*a+b*b)
    assert 0 < rr < 1
    kk = 1 - 2*rr*rr
    assert kk not in (0, 1, -1)

print("PASS STAGE35_EX_19_NONISOTRIVIAL_GENUSONE_FAMILY_BLOCKER_AND_PAIRED_QUARTIC_HOOK")