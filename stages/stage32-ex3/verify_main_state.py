#!/usr/bin/env python3
"""Cheap fail-closed verifier for Stage32EX3 startup/state contracts.

This verifier checks routing/credit/firewall invariants only. It is not a
mathematical proof of the O210 cover claims.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32-ex3/MAIN-STATE.json"
START_PATH = ROOT / "stages/stage32-ex3/MAIN-START-HERE.md"
ROADMAP_PATH = ROOT / "stages/stage32-ex3/stage32-ex3.md"
AUDIT_PATH = ROOT / "stages/stage32-ex3/AUDIT-CONTRACT.md"

state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
start = START_PATH.read_text(encoding="utf-8")
roadmap = ROADMAP_PATH.read_text(encoding="utf-8")
audit = AUDIT_PATH.read_text(encoding="utf-8")

assert state["stage"] == "32EX3"
assert state["execution"]["main_command"] == "stage32ex3-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex3-audit"
assert state["execution"]["startup_contract"] == "stages/stage32-ex3/MAIN-START-HERE.md"
assert state["execution"]["roadmap_contract"] == "stages/stage32-ex3/stage32-ex3.md"
assert state["execution"]["audit_contract"] == "stages/stage32-ex3/AUDIT-CONTRACT.md"

allowed = state["completion_contract"]["allowed_terminal_outcomes"]
assert allowed == [
    "O210_COVER_GEOMETRY_EXCLUDED",
    "GENUINE_O210_COVER_CONFIGURATION_ESTABLISHED",
]
assert state["completion_contract"]["full_target_closure_is_decision_state"] is True
assert state["completion_contract"]["abstract_nielsen_class_is_terminal_success"] is False
assert state["completion_contract"]["finite_monodromy_ledger_is_terminal_success"] is False
assert state["completion_contract"]["source_gap_diagnosis_is_terminal_success"] is False
assert state["completion_contract"]["blocked_route_is_stage_exhaustion"] is False

fixed = state["fixed_target"]
assert fixed["row_id"] == "g1-d186"
assert fixed["picard_class"] == "V6"
assert fixed["context_qprime"] == 4
assert fixed["context_O"] == 210
assert fixed["context_factor_degrees_N_to_X4"] == [105, 81]
assert fixed["context_projection_degrees_to_C0"] == [105, 81]
assert fixed["context_first_projection_ramification"] == 0
assert fixed["context_second_projection_ramification"] == 48
assert fixed["context_product_cover_second_ramification_remainder"] == 192
assert fixed["context_Y_genus"] == 106
assert fixed["context_contact_histogram"] == {
    "multiplicity_1_count": 210,
    "multiplicity_2_count": 28,
}
assert fixed["context_Q"] == 602
assert fixed["context_surviving_residues"] == [73, 97, 235]
assert fixed["context_values_require_EX3_00_source_lock_before_use"] is True

assert state["current"]["leaf"] == "EX3-00_SOURCE_LOCK_AND_TYPED_COVER_TOWER" or state["frontier"]["EX3_00_source_lock_complete"] is True
assert state["current_leaf_working_set"]
for rel in state["current_leaf_working_set"]:
    p = ROOT / rel
    assert p.exists(), f"missing working-set path: {rel}"

fire = state["firewalls"]
for key in [
    "first_projection_etale_promoted_to_global_normalization_bijective",
    "O210_contact_mass_identified_with_ramification_without_adapter",
    "pre_descent_192_confused_with_descended_48",
    "separate_cover_realizability_promoted_to_simultaneous_realizability",
    "common_cover_identity_promoted_to_new_obstruction_without_extra_predicate",
    "abstract_monodromy_promoted_to_algebraic_modular_cover",
    "abstract_cover_promoted_to_actual_V6_carrier_cover",
    "finite_search_miss_promoted_to_population_wide_exclusion",
    "unmarked_monodromy_promoted_to_Q602_residue_identification",
    "blocked_route_treated_as_stage_exhaustion",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "O212_plus_advance_allowed",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fire[key] is False, f"firewall unexpectedly true: {key}"

assert state["bootstrap"]["merge_authorized"] is False
assert state["audit"]["pass_auto_merges"] is False
assert state["audit"]["pass_auto_promotes_to_stage32_main"] is False
assert state["authority"]["stage32_main_authority_unchanged"] is True
assert state["authority"]["state_itself_grants_mathematical_credit"] is False

for token in [
    "stage32ex3-mainbatch",
    "stage32ex3-audit",
    "Do not merge without explicit user authorization",
]:
    assert token in start

for token in [
    "O210_COVER_GEOMETRY_EXCLUDED",
    "GENUINE_O210_COVER_CONFIGURATION_ESTABLISHED",
    "EX3-00",
    "EX3-09",
    "abstract transitive permutation representation",
]:
    assert token in roadmap

for token in [
    "O210_COVER_GEOMETRY_EXCLUDED",
    "GENUINE_O210_COVER_CONFIGURATION_ESTABLISHED",
    "Contact-to-ramification",
    "Monodromy / Nielsen exhaustiveness",
    "do not merge",
]:
    assert token in audit

# Source-seed paths must exist. Exact mathematical use still requires EX3-00.
for seed in state["source_seeds"].values():
    assert (ROOT / seed["path"]).exists(), f"missing source seed: {seed['path']}"

print("PASS Stage32EX3 MAIN startup/state contract")
print("leaf:", state["current"]["leaf"])
print("terminal outcomes:", ", ".join(allowed))
print("Q602/O210 firewalls:", fire["Q602_excluded"], fire["O210_excluded"])
