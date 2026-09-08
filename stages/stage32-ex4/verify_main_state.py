#!/usr/bin/env python3
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage32-ex4/MAIN-STATE.json"
ROADMAP_PATH = ROOT / "stages/stage32-ex4/stage32-ex4.md"
START_PATH = ROOT / "stages/stage32-ex4/MAIN-START-HERE.md"
ART_PATH = ROOT / "stages/stage32-ex4/ex4-r1-kuusalo-branch-labelled-h1-reentry-scratch.json"
LEAF_VERIFY = ROOT / "stages/stage32-ex4/verify_ex4_r1_kuusalo_branch_labelled_h1_reentry_scratch.py"
PRIOR_PATH = ROOT / "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json"
RECEIPT_PATH = ROOT / "stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json"

state = json.loads(STATE_PATH.read_text())
roadmap = ROADMAP_PATH.read_text()
startup = START_PATH.read_text()
art = json.loads(ART_PATH.read_text())
prior = json.loads(PRIOR_PATH.read_text())
receipt = json.loads(RECEIPT_PATH.read_text())

assert state["schema"] == "STAGE32EX4_MAIN_COMPACT_STATE_V4_KUUSALO_REENTRY_SCRATCH"
assert state["stage"] == "32EX4"
assert state["execution"]["main_command"] == "stage32ex4-mainbatch"
assert state["execution"]["audit_command"] == "stage32ex4-audit"
assert state["bootstrap"]["work_branch"] == "stage32ex4-r1-kuusalo-h1-reentry"
assert state["bootstrap"]["active_work_pr"] == 1721
assert state["bootstrap"]["merge_authorized"] is False
assert state["bootstrap"]["scratch_freshness_sync_deferred_to_consolidation"] is True

auth = state["authority"]
assert auth["prior_bounded_terminal_claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V2"
assert auth["prior_bounded_terminal_authority"] == "AUDITED"
assert auth["prior_bounded_terminal_remains_valid_for_old_frozen_package"] is True
assert auth["current_reentry_leaf_authority"] == "SCRATCH"
assert auth["stage32_main_authority_unchanged"] is True
assert auth["hostile_audit_credit_self_assigned"] is False

old = state["prior_audited_terminal"]
assert old["outcome"] == "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE"
assert old["scope"] == "EX4_STRONG_FROZEN_PACKAGE_THROUGH_05D_ONLY"
assert old["claim_id"] == "S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V2"
assert old["audit_review_id"] == 5139609916
assert old["projective_pair_classes"] == 24
assert old["delta0inf_line_counts"] == {"L1": 8, "L2": 8, "L3": 8}
assert old["reentry_requires_one_of"] == receipt["reentry_requires_one_of"]
assert prior["canonical_sha256_without_this_field"] == "57b7f3e052262ff42b157b29a05bf45cf56388fe849b4202474ad63df98ae615"
assert receipt["audit_result"] == "PASS"
assert receipt["audit_review_id"] == 5139609916
assert receipt["claim_id"] == old["claim_id"]

cur = state["current"]
assert cur["status"] == "REENTRY_ACTIVE_SCRATCH_NEW_MARKED_DATA"
assert cur["leaf"] == "EX4-R1_KUUSALO_BRANCH_LABELLED_H1_REENTRY"
assert cur["next_leaf"] == "EX4-R2_KUUSALO_PERIOD_TO_RETAINED_B5_LATTICE_ADAPTER_PREFLIGHT"
assert cur["stop_semantics"] == "SCRATCH_REENTRY_ACTIVE_ONE_NEW_MARKED_DATA_CLASS_ACCEPTED"

re = state["reentry"]
assert re["interface_class"] == "BRANCH_LABELLED_SYMPLECTIC_HOMOLOGY_OR_LEVEL_MARKING"
assert re["interface_satisfied"] is True
assert re["source_delta0inf_coordinate_mod2"] == [1, 1, 1, 1]
assert re["source_fixed_vector_unique_nonzero"] is True
assert re["literal_retained_test_word"] == "S*T^-1"
assert re["literal_retained_intertwiner_count"] == 8
assert re["literal_retained_all_delta_images"] == [[0, 0, 0, 1]]
assert re["literal_conditional_line"] == "L2"
assert re["literal_conditional_residue"] == 97
assert re["literal_result_is_conditional_only"] is True

front = state["frontier"]
for k in [
    "new_marked_data_reentry_condition_met",
    "source_side_branch_labelled_H1_marking_obtained",
    "source_side_delta0inf_coordinate_obtained",
    "literal_target_order8_intertwiner_preflight_complete",
    "all_literal_target_intertwiners_same_W_line",
]:
    assert front[k] is True, k
for k in [
    "absolute_delta0inf_retained_W_line_identified",
    "absolute_Q602_residue_identified",
    "current_extended_package_full_target_closure",
    "audit_ready_current_reentry",
]:
    assert front[k] is False, k

credit = state["credit"]
assert credit["prior_frozen_package_bounded_terminal_audited"] is True
assert credit["current_reentry_level"] == "SCRATCH_SOURCE_H1_MARKING_ONLY"
assert credit["conditional_residue97_only"] is True
assert credit["absolute_W_line_and_Q602_residue_identified"] is False
assert credit["Q602_residue_contraction_credit"] is False
assert credit["Q602_excluded"] is False
assert credit["O210_excluded"] is False
assert credit["stage32_main_credit"] is False

route = state["route_anti_loop"]
assert route["old_frozen_package_search_remains_closed_without_new_data"] is True
assert route["reentry_is_legal_because_named_new_data_class_is_supplied"] is True
assert route["old_audited_terminal_revoked"] is False
assert route["do_not_repeat_trace_order_only_or_unmarked_ppav_matching"] is True

fw = state["firewalls"]
for k in [
    "prior_audited_terminal_revoked",
    "literal_target_word_promoted_without_source_binding",
    "conditional_residue97_promoted_to_absolute_residue",
    "post1648j_candidate_self_promoted_to_audited_authority",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "stage32_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[k] is False, k

assert art["decision"]["reentry_condition_met"] is True
assert art["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert art["finite_literal_intertwiner_test"]["conditional_residue"] == 97
runpy.run_path(str(LEAF_VERIFY), run_name="__main__")

expected_working = {
    "stages/stage32-ex4/stage32-ex4.md",
    "stages/stage32-ex4/ex4-r1-kuusalo-branch-labelled-h1-reentry-scratch.json",
    "stages/stage32-ex4/verify_ex4_r1_kuusalo_branch_labelled_h1_reentry_scratch.py",
    "stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json",
    "stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json",
    "stages/stage32/residual-32-01-production/post1648j-cecotti-trace-orientation-correction.json",
    "stages/stage32/residual-32-01-production/post1648b-cecotti-generator-pair-absolute-marking-preflight.json",
    "stages/stage32-ex4/verify_main_state.py",
}
assert set(state["current_leaf_working_set"]) == expected_working

for token in [
    "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED",
    "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE",
]:
    assert token in roadmap
assert "stage32ex4-mainbatch" in startup
assert "Scratch results are non-authoritative" in startup

print("Stage32EX4 MAIN Kuusalo reentry scratch state: PASS")
print("prior_terminal=AUDITED_V2_still_valid_for_old_frozen_package")
print("reentry=BRANCH_LABELLED_SYMPLECTIC_HOMOLOGY_OR_LEVEL_MARKING")
print("source_delta0inf=[1,1,1,1] conditional_literal_residue=97 absolute=false")
