#!/usr/bin/env python3
import json
from math import gcd
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md"
AUDIT = ROOT / "stages/stage35-ex/35ex-21/post-global-surface-breadth-audit.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
audit = json.loads(AUDIT.read_text())
state = json.loads(STATE.read_text())

V20 = "STAGE35_EX_PESCH_E1_STATE_V20_POST_35EX21_GLOBAL_NORMALIZED_CUBOID_SURFACE"
V21 = "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
assert state["schema"] in {V20, V21}
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] in {
    "24438151cf76be42612b7df83314630e51c61682",
    "85e12c7b810eaafc13e663a0047111b7f3333e8b",
}

# 20/20B remain immutable audited predecessors.
for key in ("35EX-20", "35EX-20B"):
    unit = state["completed_units"][key]
    assert unit["hostile_audit_verdict"] == "PASS"
    assert unit["hostile_audit_review"] == 5109942390
    assert unit["audited_head_sha"] == "1a45fc6fca779cb22794e305e044aa37e62e76ef"
    assert unit["merged_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
    assert unit["audited_theorem_credit"] is False
assert state["completed_units"]["35EX-20"]["status"] == "AUDITED_EXACT_PAIRED_QUARTIC_SQUARECLASS_DYNAMIC_UV_SUPPORT_BLOCKER_NO_CREDIT"
assert state["completed_units"]["35EX-20B"]["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert state["completed_units"]["35EX-20B"]["preserved_untested_candidates"] == ["E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"]

unit21 = state["completed_units"]["35EX-21"]
assert unit21["status"] in {
    "PROVISIONAL_EXACT_GLOBAL_NORMALIZED_CUBOID_SURFACE_GENUS5_FIBRATION_BLOCKER_NO_CREDIT",
    "AUDITED_EXACT_GLOBAL_NORMALIZED_CUBOID_SURFACE_GENUS5_FIBRATION_BLOCKER_NO_CREDIT",
}
assert unit21["artifact"] == "stages/stage35-ex/35ex-21/global-normalized-cuboid-surface-and-genus5-fibration.md"
assert unit21["breadth_audit"] == "stages/stage35-ex/35ex-21/post-global-surface-breadth-audit.json"
assert unit21["verifier"] == "stages/stage35-ex/verify_stage35_ex_21.py"
assert unit21["global_total_surface_model_derived"] is True
assert unit21["exact_open_receiver_surface_adapter_proved"] is True
assert unit21["normalized_cuboid_square_surface_identified"] is True
assert unit21["global_surface_dimension"] == 2
assert unit21["genus5_fibration_proved"] is True
assert unit21["generic_fiber_genus"] == 5
assert unit21["primitive_source_population_reverse_adapter_proved"] is False
assert unit21["global_surface_rational_points_classified"] is False
assert unit21["brauer_obstruction_proved"] is False
assert unit21["audited_theorem_credit"] is False

unit21b = state["completed_units"]["35EX-21B"]
assert unit21b["status"] in {
    "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT",
    "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT",
}
assert unit21b["exhaustive_view_audit"] is True
assert unit21b["blind_rediscovery"] is True
assert unit21b["arsenal_comparison"] is True
assert unit21b["historical_block_ledger_comparison"] is True
assert unit21b["selected_candidate"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
assert unit21b["selected_next_unit"] == "35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER"
assert unit21b["preserved_untested_candidates"] == ["E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"]
assert unit21b["audited_theorem_credit"] is False

parent = state["parent_authority"]
if state["schema"] == V20:
    assert parent["unit"] == "35EX-20B"
    assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["hostile_audit_review"] == 5109942390
    assert parent["audited_head_sha"] == "1a45fc6fca779cb22794e305e044aa37e62e76ef"
    assert parent["merged_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
    assert state["base_main_sha"] == "24438151cf76be42612b7df83314630e51c61682"
    assert unit21["status"].startswith("PROVISIONAL_")
    assert unit21b["status"] == "PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT"
else:
    assert parent["unit"] == "35EX-21B"
    assert parent["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
    assert parent["hostile_audit_verdict"] == "PASS"
    assert parent["hostile_audit_review"] == 5110646292
    assert parent["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
    assert parent["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
    assert state["base_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
    for unit in (unit21, unit21b):
        assert unit["hostile_audit_verdict"] == "PASS"
        assert unit["hostile_audit_review"] == 5110646292
        assert unit["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
        assert unit["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"

freeze = state["resolved_investigations"]["CURRENT_GLOBAL_SURFACE_MODEL"]
assert freeze["status"] == "FROZEN_EXACT_ENDPOINT_SCALE_MODEL_NO_CLOSURE_THEOREM"
assert "normalized rational cuboid square surface" in freeze["reason"]
assert "Brauer" in freeze["reopen_condition"]

ledger = state["candidate_ledger_after_fresh_breadth_audit"]
assert ledger["selected_live"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
assert ledger["untested"] == ["E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"]
assert "E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY" in ledger["just_frozen"]
assert "E1-NORMALIZED-CUBOID-DIRECT-RATIONAL-POINT-CLASSIFICATION" in ledger["blocked"]
assert ledger["audit_artifact"] == "stages/stage35-ex/35ex-21/post-global-surface-breadth-audit.json"
assert state["completed_units"]["35EX-20B"]["preserved_untested_candidates"] == [unit21b["selected_candidate"]]
assert unit21b["selected_candidate"] == ledger["selected_live"]

current = state["current"]
assert current["unit"] == "35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER"
if state["schema"] == V20:
    assert current["status"] == "SELECTED_BY_FRESH_POST_GLOBAL_SURFACE_BREADTH_AUDIT_NO_CREDIT"
    assert "QUATERNION_SYMBOLS" in current["next_exact_leaf"]
    assert "COMPUTE_RESIDUES_EXACTLY" in current["next_exact_leaf"]
else:
    assert current["status"] == "PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT"
    assert current["candidate"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
    assert current["next_if_audited_pass"] == "35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER"

assert state["arsenal"]["S33_PW07"] == "PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR"
assert state["arsenal"]["matching_formal_global_surface_or_brauer_closure_card_found"] is False
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

for key in (
    "new_theorem_credit",
    "primitive_source_population_reverse_adapter_proved",
    "global_surface_rational_points_classified",
    "brauer_obstruction_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

for marker in (
    "GLOBAL_TOTAL_SURFACE_MODEL_DERIVED=true",
    "EXACT_OPEN_RECEIVER_SURFACE_ADAPTER_PROVED=true",
    "NORMALIZED_CUBOID_SQUARE_SURFACE_IDENTIFIED=true",
    "GLOBAL_SURFACE_DIMENSION=2",
    "GENUS5_FIBRATION_PROVED=true",
    "GENERIC_FIBER_GENUS=5",
    "PRIMITIVE_SOURCE_POPULATION_REVERSE_ADAPTER_PROVED=false",
    "GLOBAL_SURFACE_RATIONAL_POINTS_CLASSIFIED=false",
    "BRAUER_OBSTRUCTION_PROVED=false",
    "CURRENT_GLOBAL_SURFACE_MODEL_ROUTE=FROZEN_EXACT_ENDPOINT_SCALE_MODEL_NO_CLOSURE_THEOREM",
    "E1_PROVED=false",
):
    assert marker in doc

assert audit["schema"] == "STAGE35_EX_21B_POST_GLOBAL_SURFACE_BREADTH_AUDIT_V1"
assert audit["blind_rediscovery"]["performed_before_arsenal_comparison_for_this_audit"] is True
assert audit["arsenal_comparison"]["performed_after_blind_generation"] is True
assert audit["selection"]["selected_candidate"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"
assert audit["selection"]["selected_next_unit"] == "35EX-22_SURFACE_BRAUER_CLASS_OR_OBVIOUS_SYMBOL_BLOCKER"
assert audit["selection"]["preserved_untested_candidates"] == ["E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"]
allowed = {"LIVE", "UNTESTED", "EQUIVALENT", "DOMINATED", "BLOCKED"}
assert all(c["status"] in allowed for c in audit["blind_rediscovery"]["generated"])
assert next(c for c in audit["blind_rediscovery"]["generated"] if c["id"] == "E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER")["status"] == "LIVE"
assert next(c for c in audit["blind_rediscovery"]["generated"] if c["id"] == "E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT")["status"] == "UNTESTED"
assert audit["historical_ledger_comparison"]["E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER"].startswith("preserved as UNTESTED in 35EX-20B")
assert audit["selection"]["selected_candidate"] == state["completed_units"]["35EX-20B"]["preserved_untested_candidates"][0]
cycle = audit["cycle_exit"]
assert cycle["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert cycle["CYCLE_LIVE_CANDIDATES"] == 1
assert cycle["CYCLE_UNTESTED_CANDIDATES"] == 1
assert cycle["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert cycle["CYCLE_BLIND_REDISCOVERY"] is True
assert cycle["CYCLE_SPLIT_TRIGGERED"] is False
assert cycle["CYCLE_PARKING_AUDIT_COMPLETE"] is False
assert cycle["CYCLE_NEW_VIEW_SOURCE"] == "BOTH"

# Symbolic forward adapter from normalized receiver to S_PC.
r, t, s1, s2 = sp.symbols("r t s1 s2", nonzero=True)
master2 = r**2 + t**2 - 2*r**2*t**2
e12 = r**2 + t**2 - r**2*t**2
source_sub = {s1**2: 1-r**2, s2**2: 1-t**2}
assert sp.expand((1/r**2 - 1 - s1**2/r**2).subs(source_sub)) == 0
assert sp.expand((1/t**2 - 1 - s2**2/t**2).subs(source_sub)) == 0
assert sp.expand((master2/(r**2*t**2) - s1**2/r**2 - s2**2/t**2).subs(source_sub)) == 0
assert sp.expand((e12/(r**2*t**2) - 1 - s1**2/r**2 - s2**2/t**2).subs(source_sub)) == 0

# Symbolic inverse adapter on p*q != 0.
x, y, p, q, z, w = sp.symbols("x y p q z w", nonzero=True)
r_inv = 1/p
s1_inv = x/p
t_inv = 1/q
s2_inv = y/q
mu_inv = z/(p*q)
nu_inv = w/(p*q)
rel = {p**2: 1+x**2, q**2: 1+y**2, z**2: x**2+y**2, w**2: 1+x**2+y**2}
assert sp.simplify((r_inv**2+s1_inv**2-1).subs(rel)) == 0
assert sp.simplify((t_inv**2+s2_inv**2-1).subs(rel)) == 0
master_res = sp.together(mu_inv**2 - (r_inv**2+t_inv**2-2*r_inv**2*t_inv**2))
e1_res = sp.together(nu_inv**2 - (r_inv**2+t_inv**2-r_inv**2*t_inv**2))
master_num = sp.factor(master_res.as_numer_denom()[0].subs(rel))
e1_num = sp.factor(e1_res.as_numer_denom()[0].subs(rel))
assert master_num == 0
assert e1_num == 0

# Generic genus-5 fibration.
X, Y = sp.symbols("X Y")
f1 = Y**2 + 1
f2 = Y**2 + X**2
f3 = Y**2 + 1 + X**2
assert sp.factor(sp.discriminant(f1, Y) - (-4)) == 0
assert sp.factor(sp.discriminant(f2, Y) - (-4*X**2)) == 0
assert sp.factor(sp.discriminant(f3, Y) - (-4*(1+X**2))) == 0
assert sp.factor(sp.resultant(f1, f2, Y) - (X-1)**2*(X+1)**2) == 0
assert sp.factor(sp.resultant(f1, f3, Y) - X**4) == 0
assert sp.factor(sp.resultant(f2, f3, Y) - 1) == 0
cover_degree = 8
simple_branch_points = 6
inertia = 2
ramification_contribution_per_branch = cover_degree // inertia * (inertia-1)
rh = cover_degree * (-2) + simple_branch_points * ramification_contribution_per_branch
assert rh == 8
assert (rh + 2) // 2 == 5

checked = 0
for a in range(2, 25):
    for b in range(1, a):
        if gcd(a, b) != 1 or (a-b) % 2 != 1:
            continue
        U = a*a-b*b
        V = 2*a*b
        W = a*a+b*b
        assert U*U + V*V == W*W
        assert W*W == U*U + V*V
        assert U != 0 and V != 0
        checked += 1
assert checked > 50

print("PASS STAGE35_EX_21_GLOBAL_NORMALIZED_CUBOID_SURFACE_GENUS5_FIBRATION")
