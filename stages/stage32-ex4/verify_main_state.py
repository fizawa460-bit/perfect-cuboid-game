#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32-ex4/MAIN-STATE.json"
ROADMAP_PATH = ROOT / "stages/stage32-ex4/stage32-ex4.md"
START_PATH = ROOT / "stages/stage32-ex4/MAIN-START-HERE.md"
AUDIT_PATH = ROOT / "stages/stage32-ex4/AUDIT-CONTRACT.md"
RETAINED_PATH = ROOT / "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json"

state = json.loads(STATE_PATH.read_text())
roadmap = ROADMAP_PATH.read_text()
startup = START_PATH.read_text()
audit = AUDIT_PATH.read_text()
retained = json.loads(RETAINED_PATH.read_text())

assert state["schema"] == "STAGE32EX4_MAIN_COMPACT_STATE_V2_AUDIT_HANDOFF"
assert state["stage"] == "32EX4"
assert state["execution"]["main_command"] == "stage32ex4-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex4-audit"
assert state["bootstrap"]["active_work_pr"] == 1713
assert state["bootstrap"]["merge_authorized"] is False

allowed = state["completion_contract"]["allowed_terminal_outcomes"]
assert allowed == [
    "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED",
    "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE",
]
assert state["completion_contract"]["terminal_outcome"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
assert state["completion_contract"]["terminal_scope"] == "EX4_STRONG_FROZEN_PACKAGE_THROUGH_05D_ONLY"
assert state["completion_contract"]["negative_terminal_is_bounded_to_explicit_frozen_source_package"] is True
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

assert state["current"]["status"] == "AUDIT_READY_FULL_TARGET_CLOSURE_PROVISIONAL_PENDING_HOSTILE_AUDIT"
assert state["current"]["leaf"] == "EX4-11_HOSTILE_AUDIT_HANDOFF"
assert state["current"]["stop_semantics"] == "MAINBATCH_STOPS_AT_AUDIT_BOUNDARY"

frontier = state["frontier"]
for key in [
    "EX4_00_source_lock_complete",
    "typed_object_arrow_graph_complete",
    "absolute_marking_input_contract_complete",
    "current_ambiguity_group_computed",
    "marked_source_inventory_complete",
    "curve_weierstrass_action_anchor_complete",
    "retained_ppav_J2_basis_anchor_complete",
    "admissible_conjugator_set_enumerated",
    "coordinate_model_invariance_crosscheck_complete",
    "frozen_source_package_exhaustiveness_proved_candidate",
    "residual_ambiguity_W_line_orbit_computed",
    "minimal_new_datum_reentry_interface_identified",
    "audit_ready_full_target_closure",
]:
    assert frontier[key] is True, key
assert frontier["all_admissible_conjugators_same_W_line"] is False
assert frontier["absolute_delta0inf_retained_W_line_identified"] is False
assert frontier["absolute_Q602_residue_identified"] is False
assert frontier["terminal_outcome"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
assert frontier["full_target_closure"] is False

candidate = state["retained_terminal_candidate"]
assert candidate["claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V1"
assert candidate["authority_status"] == "PROVISIONAL"
assert candidate["canonical_sha256"] == retained["canonical_sha256_without_this_field"]
assert candidate["projective_pair_classes"] == 24
assert candidate["delta0inf_line_counts"] == {"L1": 8, "L2": 8, "L3": 8}

credit = state["credit"]
assert credit["level"] == "AUDIT_READY_FULL_TARGET_CLOSURE_PROVISIONAL_NO_AUDITED_CREDIT"
assert credit["provisional_bounded_terminal_candidate"] is True
assert credit["fixed_source_package_cannot_select_absolute_W_line_audited_credit"] is False
assert credit["full_target_closure"] is False
assert credit["stage32_main_credit"] is False
assert credit["Q602_excluded"] is False
assert credit["O210_excluded"] is False

assert state["audit"]["status"] == "READY_FOR_HOSTILE_AUDIT_PROVISIONAL_TERMINAL_CANDIDATE"
assert state["audit"]["candidate_pr"] == 1713
assert state["audit"]["review_id"] is None
assert state["audit"]["result"] is None

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
    "hostile_audit_credit_self_assigned",
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
    "stages/stage32-ex4/AUDIT-CONTRACT.md",
    "stages/stage32-ex4/stage32-ex4.md",
    "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json",
    "stages/stage32-ex4/verify_ex4_10s_retained_bounded_terminal_candidate.py",
    "stages/stage32-ex4/ex4-10-bounded-terminal-decision-certificate-assembly-scratch.json",
    "stages/stage32-ex4/verify_ex4_10_bounded_terminal_decision_certificate_assembly_scratch.py",
    "stages/stage32-ex4/verify_main_state.py",
    "stages/stage32/proof/CLAIM-REGISTRY.json",
    "stages/stage32/proof/LANE-ADAPTERS.json",
}
assert set(state["current_leaf_working_set"]) == expected_working

print("Stage32EX4 MAIN audit-handoff state: PASS")
print("terminal_candidate=FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE")
print("authority=PROVISIONAL pending hostile audit")
print("stage32_main_credit=false Q602_excluded=false O210_excluded=false")
