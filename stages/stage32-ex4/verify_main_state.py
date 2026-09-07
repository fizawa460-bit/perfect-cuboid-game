#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32-ex4/MAIN-STATE.json"
ROADMAP_PATH = ROOT / "stages/stage32-ex4/stage32-ex4.md"
START_PATH = ROOT / "stages/stage32-ex4/MAIN-START-HERE.md"
AUDIT_PATH = ROOT / "stages/stage32-ex4/AUDIT-CONTRACT.md"

state = json.loads(STATE_PATH.read_text())
roadmap = ROADMAP_PATH.read_text()
startup = START_PATH.read_text()
audit = AUDIT_PATH.read_text()

assert state["stage"] == "32EX4"
assert state["execution"]["main_command"] == "stage32ex4-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex4-audit"
assert state["bootstrap"]["merge_authorized"] is False

allowed = state["completion_contract"]["allowed_terminal_outcomes"]
assert allowed == [
    "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED",
    "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE",
]
assert state["completion_contract"]["terminal_outcome"] is None
assert state["completion_contract"]["gauge_representative_is_terminal_success"] is False
assert state["completion_contract"]["inner_conjugacy_orbit_is_terminal_success"] is False
assert state["completion_contract"]["conditional_residue_is_terminal_success"] is False

fixed = state["fixed_target"]
assert fixed["context_O"] == 210
assert fixed["context_Q"] == 602
assert fixed["context_surviving_residues"] == [73, 97, 235]
assert fixed["context_abstract_character"] == "chi_u"
assert fixed["context_abstract_J2_direction"] == "delta_0inf=[P_0-P_infinity]"
assert fixed["context_retained_W_nonzero_line_count"] == 3
assert fixed["context_absolute_delta0inf_retained_W_line_identified"] is False

assert state["current"]["leaf"] == "EX4-00_SOURCE_LOCK_AND_TYPED_MARKING_TARGET"
assert state["frontier"]["EX4_00_source_lock_complete"] is False
assert state["frontier"]["absolute_delta0inf_retained_W_line_identified"] is False
assert state["frontier"]["absolute_Q602_residue_identified"] is False
assert state["frontier"]["full_target_closure"] is False

fw = state["firewalls"]
for key in [
    "gauge_choice_promoted_to_absolute_marking",
    "delta0inf_membership_in_W_promoted_to_specific_W_line",
    "inner_conjugacy_orbit_promoted_to_explicit_conjugator",
    "group_order_or_trace_match_promoted_to_semantic_adapter",
    "literal_plus_r_representative_promoted_without_source_binding",
    "post1648j_candidate_self_promoted_to_audited_authority",
    "other_stage_marking_imported_without_population_adapter",
    "conditional_residue_promoted_to_absolute_residue",
    "three_to_one_selection_promoted_to_Q602_exclusion",
    "bounded_source_package_obstruction_promoted_to_global_impossibility",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "O212_plus_advance_allowed",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False, key

for token in [
    "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED",
    "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE",
    "Gauge choice is not absolute marking",
    "3 -> 1",
    "No automatic merge",
]:
    assert token in roadmap, token

for token in ["stage32ex4-mainbatch", "stage32ex4-audit", "Do not merge without explicit user authorization"]:
    assert token in startup, token

for token in [
    "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED",
    "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE",
    "3 -> 1",
    "does not exclude Q602/O210",
]:
    assert token in audit, token

expected_working = {
    "stages/stage32-ex4/stage32-ex4.md",
    "stages/stage32-ex4/verify_main_state.py",
    "stages/stage32/MAIN-STATE.json",
    "stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement.json",
    "stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json",
    "stages/stage32/residual-32-01-production/post1505-o210-q602-marked-w-line-gauge-orbit.json",
    "stages/stage32/residual-32-01-production/post1648j-cecotti-trace-orientation-correction.json",
}
assert set(state["current_leaf_working_set"]) == expected_working

print("Stage32EX4 MAIN bootstrap state: PASS")
print("target: delta_0inf -> retained W-line -> one of [73,97,235]")
print("credit: BOOTSTRAP_NO_MATHEMATICAL_CREDIT")
