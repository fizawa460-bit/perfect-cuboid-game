#!/usr/bin/env python3
import json, runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=json.loads((ROOT/"stages/stage32-ex4/MAIN-STATE.json").read_text())
R4=json.loads((ROOT/"stages/stage32-ex4/ex4-r4-kuusalo-f2-branch-action-to-cecotti-b8-algebraic-binding-preflight-scratch.json").read_text())
R5=json.loads((ROOT/"stages/stage32-ex4/ex4-r5-kuusalo-figure9-10-branch-to-h1-label-recovery-scratch.json").read_text())
R6=json.loads((ROOT/"stages/stage32-ex4/ex4-r6-brezhnev-burnside-explicit-uniformization-marking-preflight-scratch.json").read_text())
R7=json.loads((ROOT/"stages/stage32-ex4/ex4-r7-triangle-group-regular-octagon-marking-preflight-scratch.json").read_text())
PRIOR=json.loads((ROOT/"stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json").read_text())
RECEIPT=json.loads((ROOT/"stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json").read_text())
START=(ROOT/"stages/stage32-ex4/MAIN-START-HERE.md").read_text()
ROADMAP=(ROOT/"stages/stage32-ex4/stage32-ex4.md").read_text()

assert STATE["schema"]=="STAGE32EX4_MAIN_COMPACT_STATE_V10_TRIANGLE_GROUP_R7_SCRATCH"
assert STATE["bootstrap"]["active_work_pr"]==1721
assert STATE["bootstrap"]["merge_authorized"] is False
assert STATE["authority"]["prior_bounded_terminal_claim_id"]=="S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V2"
assert STATE["authority"]["prior_bounded_terminal_authority"]=="AUDITED"
assert STATE["authority"]["prior_bounded_terminal_remains_valid_for_old_frozen_package"] is True
assert STATE["authority"]["current_reentry_leaf_authority"]=="SCRATCH"
assert STATE["authority"]["stage32_main_authority_unchanged"] is True
assert STATE["current"]["leaf"]=="EX4-R7_TRIANGLE_GROUP_REGULAR_OCTAGON_MARKING_PREFLIGHT"
assert STATE["current"]["next_leaf"]=="EX4-R8_COOK_JENNI_BRANCH_LABELLED_OCTAGON_TO_ORDER3_TRIANGLE_MARKING_PREFLIGHT"

assert RECEIPT["audit_result"]=="PASS"
assert RECEIPT["audit_review_id"]==5139609916
assert PRIOR["canonical_sha256_without_this_field"]=="57b7f3e052262ff42b157b29a05bf45cf56388fe849b4202474ad63df98ae615"
assert R4["canonical_sha256_without_this_field"]=="0718f53281b215c668fbb7bb44b4b9c3e44a86cc64ba21dbcaaad4234f943679"
assert R5["canonical_sha256_without_this_field"]=="816f9c0574302ea99473384dd9dd9c047d48db3712fcd48f1630eb553f517ecc"
assert R6["canonical_sha256_without_this_field"]=="007c80db16b644bbffc999bdeb3b4f264edfe0f7b1288face4195ae04d4a86fd"
assert R7["canonical_sha256_without_this_field"]=="89a8f229461877f8030577962e61218610c62afdde99c3912fabfd779f058f96"

re=STATE["reentry"]
assert re["source_delta0inf_coordinate_mod2"]==[1,1,1,1]
assert re["period_adapter_count"]==48
assert re["period_adapter_delta_line_counts"]=={"L1":16,"L2":16,"L3":16}
assert re["transported_pair_distinct_projective_count"]==24
assert re["transported_pair_projective_delta_line_counts"]=={"L1":8,"L2":8,"L3":8}
assert re["literal_pair_conditional_line"]=="L2"
assert re["literal_pair_conditional_residue"]==97
assert re["f2_distinct_branch_permutation_count"]==4
assert re["f2_branch_orbit"]=="r^k*B8*r^-k, k=0..3"
assert re["brezhnev_branch_labels_to_own_modular_polygon_exact"] is True
assert re["brezhnev_independently_selects_k"] is False
assert re["r7_regular_octagon_triangle_group_words_exact"] is True
assert re["r7_triangle_group_conjugate_choices"]==3
assert re["r7_S_T_fixed_points_only_unlabelled_weierstrass"] is True
assert re["r7_surface_group_diagonal_pairing_words_exact"] is True
assert re["r7_to_kuusalo_figure9_side_phase_adapter"] is False
assert re["r7_to_kuusalo_figure10_order3_triangle_adapter"] is False
assert re["r7_independently_selects_k"] is False
assert re["literal_B8_source_selected"] is False

front=STATE["frontier"]
for k in ["new_marked_data_reentry_condition_met","source_side_branch_labelled_H1_marking_obtained","source_side_delta0inf_coordinate_obtained","period_adapter_torsor_exact","second_generator_pair_transport_exact","f2_branch_action_candidate_count_4","kuusalo_text_geometry_recovered","brezhnev_branch_to_own_polygon_exact","r7_regular_octagon_group_geometry_exact"]:
    assert front[k] is True,k
for k in ["period_equivalence_prunes_W_line","simultaneous_pair_data_prunes_W_line","r5_fourfold_phase_reduced","brezhnev_to_kuusalo_phase_adapter_exact","r6_fourfold_phase_reduced","r7_algebraic_weierstrass_phase_adapter_exact","r7_fourfold_phase_reduced","literal_B8_source_bound","absolute_delta0inf_retained_W_line_identified","absolute_Q602_residue_identified","current_extended_package_full_target_closure","audit_ready_current_reentry"]:
    assert front[k] is False,k

credit=STATE["credit"]
assert credit["current_reentry_level"]=="SCRATCH_TRIANGLE_GROUP_OCTAGON_WORDS_EXACT_FOURFOLD_PHASE_SURVIVES"
assert credit["conditional_residue97_only"] is True
for k in ["absolute_W_line_and_Q602_residue_identified","Q602_residue_contraction_credit","Q602_excluded","O210_excluded","stage32_main_credit"]:
    assert credit[k] is False,k

route=STATE["route_anti_loop"]
assert route["r6_brezhnev_explicit_uniformization_classified_requires_adapter_nonpruning"] is True
assert route["r7_triangle_group_regular_octagon_classified_requires_algebraic_label_adapter_nonpruning"] is True
assert route["next_exact_route"]=="USE_COOK_JENNI_BRANCH_LABELLED_OCTAGON_AND_ORDER3_TRIANGLE_ACTION_AS_MATERIALLY_DISTINCT_MARKING_SOURCE"

for k,v in STATE["firewalls"].items():
    assert v is False,k

assert R7["source_exact_data"]["triangle_group_choice"]["conjugate_subgroup_count"]==3
assert R7["source_exact_data"]["genus2_surface_group_diagonal_pairing_words"]=={"f1":"S^4*T^2","f2":"S*T^2*S^3","f3":"S^-2*T^2*S^6","f4":"S^3*T^2*S"}
assert R7["typed_adapter_test"]["triangle_group_to_regular_octagon_geometry"]["provided"] is True
assert R7["r4_phase_replay"]["candidate_k_after_r7"]==[0,1,2,3]
assert R7["r4_phase_replay"]["hknr_independently_selects_one_k"] is False
assert R7["decision"]["source_lane_classification"]=="EXACT_GROUP_GEOMETRY_NONPRUNING_REQUIRES_ALGEBRAIC_LABEL_ADAPTER"
assert R7["decision"]["conditional_residue97_only"] is True

for p in set(STATE["current_leaf_working_set"]): assert (ROOT/p).exists(),p
assert "stage32ex4-mainbatch" in START
assert "Scratch results are non-authoritative" in START
assert "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED" in ROADMAP
assert "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE" in ROADMAP

runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r4_kuusalo_f2_branch_action_to_cecotti_b8_algebraic_binding_preflight_scratch.py"),run_name="__main__")
runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r5_kuusalo_figure9_10_branch_to_h1_label_recovery_scratch.py"),run_name="__main__")
runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r6_brezhnev_burnside_explicit_uniformization_marking_preflight_scratch.py"),run_name="__main__")
runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r7_triangle_group_regular_octagon_marking_preflight_scratch.py"),run_name="__main__")

print("Stage32EX4 MAIN triangle-group R7 scratch state: PASS")
print("regular-octagon triangle-group and surface-group words are exact")
print("algebraic Weierstrass labels / Kuusalo Figure9-10 phase remain unbound")
print("four B8 conjugates survive; residue97 conditional only; next route is Cook/Jenni branch-labelled octagon")
