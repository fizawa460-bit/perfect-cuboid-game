#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32-ex4/MAIN-STATE.json"
ROADMAP_PATH = ROOT / "stages/stage32-ex4/stage32-ex4.md"
START_PATH = ROOT / "stages/stage32-ex4/MAIN-START-HERE.md"
AUDIT_PATH = ROOT / "stages/stage32-ex4/AUDIT-CONTRACT.md"
RETAINED_PATH = ROOT / "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json"
RECEIPT_PATH = ROOT / "stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json"
REGISTRY_PATH = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
ADAPTER_PATH = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

state = json.loads(STATE_PATH.read_text())
roadmap = ROADMAP_PATH.read_text()
startup = START_PATH.read_text()
audit_contract = AUDIT_PATH.read_text()
retained = json.loads(RETAINED_PATH.read_text())
receipt = json.loads(RECEIPT_PATH.read_text())
registry = json.loads(REGISTRY_PATH.read_text())
adapters = json.loads(ADAPTER_PATH.read_text())

assert state["schema"] == "STAGE32EX4_MAIN_COMPACT_STATE_V3_AUDITED_TERMINAL"
assert state["stage"] == "32EX4"
assert state["execution"]["main_command"] == "stage32ex4-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex4-audit"
assert state["bootstrap"]["active_work_pr"] == 1719
assert state["bootstrap"]["audited_candidate_pr"] == 1713
assert state["bootstrap"]["audited_candidate_merge_commit"] == "1eea6800e479729c41ed8767a38298384a2dbc0f"
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

assert state["authority"]["retained_terminal_candidate_authority"] == "AUDITED"
assert state["authority"]["hostile_audit_pass_recorded"] is True
assert state["authority"]["stage32_main_authority_unchanged"] is True
assert state["current"]["status"] == "FULL_TARGET_CLOSURE_AUDITED"
assert state["current"]["leaf"] == "EX4-11_AUDITED_BOUNDED_TERMINAL_HOLD"
assert state["current"]["stop_semantics"] == "EX4_FULL_TARGET_CLOSURE_REACHED_NO_FURTHER_MAINBATCH_RESEARCH_WITHOUT_REENTRY"

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
    "frozen_source_package_exhaustiveness_proved_audited",
    "residual_ambiguity_W_line_orbit_computed",
    "minimal_new_datum_reentry_interface_identified",
    "audit_ready_full_target_closure",
    "hostile_audit_pass",
    "full_target_closure",
]:
    assert frontier[key] is True, key
assert frontier["all_admissible_conjugators_same_W_line"] is False
assert frontier["absolute_delta0inf_retained_W_line_identified"] is False
assert frontier["absolute_Q602_residue_identified"] is False
assert frontier["terminal_outcome"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"

candidate = state["retained_terminal_candidate"]
assert candidate["claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V1"
assert candidate["authority_status"] == "AUDITED"
assert candidate["canonical_sha256"] == retained["canonical_sha256_without_this_field"]
assert candidate["projective_pair_classes"] == 24
assert candidate["delta0inf_line_counts"] == {"L1": 8, "L2": 8, "L3": 8}
expected_audit = {
    "status": "PASS",
    "pr": 1713,
    "review_id": 5139609916,
    "exact_head": "e1b65ef259182502a397a5a570827c43be1ebe6c",
    "merge_commit": "1eea6800e479729c41ed8767a38298384a2dbc0f",
}
assert candidate["audit_receipt"] == expected_audit

credit = state["credit"]
assert credit["level"] == "FULL_TARGET_CLOSURE_AUDITED_FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
assert credit["provisional_bounded_terminal_candidate"] is False
assert credit["fixed_source_package_cannot_select_absolute_W_line_audited_credit"] is True
assert credit["full_target_closure"] is True
assert credit["stage32_main_credit"] is False
assert credit["Q602_residue_contraction_credit"] is False
assert credit["Q602_excluded"] is False
assert credit["O210_excluded"] is False

state_audit = state["audit"]
assert state_audit["status"] == "PASS_CONSUMED_BY_AUTHORITY_TRANSITION_SYNC"
assert state_audit["candidate_pr"] == 1713
assert state_audit["exact_head"] == expected_audit["exact_head"]
assert state_audit["review_id"] == expected_audit["review_id"]
assert state_audit["result"] == "PASS"
assert state_audit["candidate_merge_commit"] == expected_audit["merge_commit"]
assert state_audit["authority_transition_pr"] == 1719
assert state_audit["pass_auto_merges"] is False
assert state_audit["pass_auto_promotes_to_stage32_main"] is False

assert receipt["candidate_pr"] == 1713
assert receipt["candidate_exact_head"] == expected_audit["exact_head"]
assert receipt["candidate_merge_commit"] == expected_audit["merge_commit"]
assert receipt["audit_review_id"] == expected_audit["review_id"]
assert receipt["audit_result"] == "PASS"
assert receipt["claim_id"] == candidate["claim_id"]
assert receipt["audited_credit"] == "FULL_TARGET_CLOSURE / FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
assert receipt["terminal_scope"] == "EX4_STRONG_FROZEN_PACKAGE_THROUGH_05D_ONLY"
assert receipt["promotion_ceiling"]["EX4_full_target_closure"] is True
assert receipt["promotion_ceiling"]["stage32_main_promotion"] is False
assert receipt["promotion_ceiling"]["Q602_excluded"] is False
assert receipt["promotion_ceiling"]["O210_excluded"] is False

claims = {c["claim_id"]: c for c in registry["claims"]}
claim = claims[candidate["claim_id"]]
assert claim["authority_status"] == "AUDITED"
assert claim["audit_receipt"] == expected_audit
assert claim["claim_core_sha256"] == "2d5ffc68edd76653e0c776f51f0a32ab99d327baa4353d6f4636abed0b046ca9"
assert claim["scope"]["candidate_pr"] == 1713
assert claim["scope"]["frozen_package"] == "EX4_STRONG_FROZEN_PACKAGE_THROUGH_05D_ONLY"
assert "Stage32 MAIN credit or Stage32 closure." in claim["does_not_prove"]

lane = next(x for x in adapters["lanes"] if x["lane"] == "EX4")
assert candidate["claim_id"] in lane["claim_refs"]
assert "AUDITED" in lane["notes"]
assert "5139609916" in lane["notes"]
assert "Stage32 MAIN" in lane["notes"]

route = state["route_anti_loop"]
assert route["audited_fact_available"] is True
assert route["do_not_repeat_frozen_package_without_new_marked_data"] is True
assert route["stage32_main_mathematical_frontier_changed"] is False
assert route["explicit_main_promotion_adapter_present"] is False
assert route["reentry_requires_one_of"] == candidate["minimal_reentry_interface"]

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
    assert token in audit_contract, token

expected_working = {
    "stages/stage32-ex4/AUDIT-CONTRACT.md",
    "stages/stage32-ex4/stage32-ex4.md",
    "stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json",
    "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json",
    "stages/stage32-ex4/verify_ex4_10s_retained_bounded_terminal_candidate.py",
    "stages/stage32-ex4/verify_main_state.py",
    "stages/stage32/proof/CLAIM-REGISTRY.json",
    "stages/stage32/proof/LANE-ADAPTERS.json",
}
assert set(state["current_leaf_working_set"]) == expected_working

print("Stage32EX4 MAIN audited-terminal state: PASS")
print("terminal=FULL_TARGET_CLOSURE / FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE")
print("authority=AUDITED review=5139609916 exact_head=e1b65ef259182502a397a5a570827c43be1ebe6c")
print("route_anti_loop=true stage32_main_credit=false Q602_excluded=false O210_excluded=false")
