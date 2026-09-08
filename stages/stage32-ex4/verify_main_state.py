#!/usr/bin/env python3
import json, runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=json.loads((ROOT/"stages/stage32-ex4/MAIN-STATE.json").read_text())
R4=json.loads((ROOT/"stages/stage32-ex4/ex4-r4-kuusalo-f2-branch-action-to-cecotti-b8-algebraic-binding-preflight-scratch.json").read_text())
R5=json.loads((ROOT/"stages/stage32-ex4/ex4-r5-kuusalo-figure9-10-branch-to-h1-label-recovery-scratch.json").read_text())
PRIOR=json.loads((ROOT/"stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json").read_text())
RECEIPT=json.loads((ROOT/"stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json").read_text())
START=(ROOT/"stages/stage32-ex4/MAIN-START-HERE.md").read_text()
ROADMAP=(ROOT/"stages/stage32-ex4/stage32-ex4.md").read_text()

assert STATE["schema"]=="STAGE32EX4_MAIN_COMPACT_STATE_V8_KUUSALO_R5_SCRATCH"
assert STATE["bootstrap"]["active_work_pr"]==1721
assert STATE["bootstrap"]["merge_authorized"] is False
assert STATE["authority"]["prior_bounded_terminal_claim_id"]=="S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V2"
assert STATE["authority"]["prior_bounded_terminal_authority"]=="AUDITED"
assert STATE["authority"]["prior_bounded_terminal_remains_valid_for_old_frozen_package"] is True
assert STATE["authority"]["current_reentry_leaf_authority"]=="SCRATCH"
assert STATE["authority"]["stage32_main_authority_unchanged"] is True
assert STATE["current"]["leaf"]=="EX4-R5_RECOVER_FULL_KUUSALO_FIGURE9_10_BRANCH_TO_H1_LABEL_OR_EXPLICIT_UNIFORMIZATION_MAP"
assert STATE["current"]["next_leaf"]=="EX4-R6_BREZHNEV_BURNSIDE_EXPLICIT_UNIFORMIZATION_MARKING_PREFLIGHT"

assert RECEIPT["audit_result"]=="PASS"
assert RECEIPT["audit_review_id"]==5139609916
assert PRIOR["canonical_sha256_without_this_field"]=="57b7f3e052262ff42b157b29a05bf45cf56388fe849b4202474ad63df98ae615"
assert R4["canonical_sha256_without_this_field"]=="0718f53281b215c668fbb7bb44b4b9c3e44a86cc64ba21dbcaaad4234f943679"
assert R5["canonical_sha256_without_this_field"]=="816f9c0574302ea99473384dd9dd9c047d48db3712fcd48f1630eb553f517ecc"

re=STATE["reentry"]
assert re["source_delta0inf_coordinate_mod2"]==[1,1,1,1]
assert re["period_adapter_count"]==48
assert re["period_adapter_delta_line_counts"]=={"L1":16,"L2":16,"L3":16}
assert re["transported_pair_distinct_projective_count"]==24
assert re["transported_pair_projective_delta_line_counts"]=={"L1":8,"L2":8,"L3":8}
assert re["literal_pair_conditional_line"]=="L2"
assert re["literal_pair_conditional_residue"]==97
assert re["full_branch_J2_embedding_count"]==8
assert re["f2_distinct_branch_permutation_count"]==4
assert re["f2_branch_orbit"]=="r^k*B8*r^-k, k=0..3"
assert re["kuusalo_text_fixes_octagon_branch_strata"] is True
assert re["kuusalo_text_fixes_infinity_plus1_negative_real_ray"] is True
assert re["kuusalo_text_fixes_figure9_side_number_absolute_phase"] is False
assert re["kuusalo_text_fixes_figure10_triangle_P_algebraic_label"] is False
assert re["literal_B8_source_selected"] is False

front=STATE["frontier"]
for k in ["new_marked_data_reentry_condition_met","source_side_branch_labelled_H1_marking_obtained","source_side_delta0inf_coordinate_obtained","period_adapter_torsor_exact","second_generator_pair_transport_exact","f2_branch_action_candidate_count_4","kuusalo_text_geometry_recovered"]:
    assert front[k] is True,k
for k in ["period_equivalence_prunes_W_line","simultaneous_pair_data_prunes_W_line","r5_fourfold_phase_reduced","literal_B8_source_bound","absolute_delta0inf_retained_W_line_identified","absolute_Q602_residue_identified","current_extended_package_full_target_closure","audit_ready_current_reentry"]:
    assert front[k] is False,k

credit=STATE["credit"]
assert credit["current_reentry_level"]=="SCRATCH_KUUSALO_TEXT_GEOMETRY_EXACT_FOURFOLD_PHASE_SURVIVES"
assert credit["conditional_residue97_only"] is True
for k in ["absolute_W_line_and_Q602_residue_identified","Q602_residue_contraction_credit","Q602_excluded","O210_excluded","stage32_main_credit"]:
    assert credit[k] is False,k

route=STATE["route_anti_loop"]
assert route["r4_branch_action_conjugacy_classified"] is True
assert route["r5_kuusalo_text_phase_recovery_classified_nonpruning"] is True
assert route["next_exact_route"]=="USE_BREZHNEV_EXPLICIT_BURNSIDE_UNIFORMIZATION_AS_MATERIALLY_DISTINCT_MARKED_SOURCE"

for k,v in STATE["firewalls"].items():
    assert v is False,k

assert R5["decision"]["r4_fourfold_phase_reduced"] is False
assert R5["decision"]["residual_f2_branch_action_count"]==4
assert R5["decision"]["literal_Kuusalo_f2_equals_Cecotti_B8_proved"] is False
assert R5["decision"]["conditional_residue97_only"] is True
assert R5["new_uniformization_source_candidate"]["used_for_R5_selection"] is False

for p in set(STATE["current_leaf_working_set"]): assert (ROOT/p).exists(),p
assert "stage32ex4-mainbatch" in START
assert "Scratch results are non-authoritative" in START
assert "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED" in ROADMAP
assert "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE" in ROADMAP

runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r4_kuusalo_f2_branch_action_to_cecotti_b8_algebraic_binding_preflight_scratch.py"),run_name="__main__")
runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r5_kuusalo_figure9_10_branch_to_h1_label_recovery_scratch.py"),run_name="__main__")

print("Stage32EX4 MAIN Kuusalo R5 scratch state: PASS")
print("Kuusalo text fixes branch strata and [infinity,+1] negative-real ray")
print("Figure9 side phase / Figure10 triangle P algebraic label remain unbound")
print("four B8 conjugates survive; residue97 conditional only")
