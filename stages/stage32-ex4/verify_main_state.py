#!/usr/bin/env python3
import json, runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=json.loads((ROOT/"stages/stage32-ex4/MAIN-STATE.json").read_text())
R2=json.loads((ROOT/"stages/stage32-ex4/ex4-r2-kuusalo-period-to-retained-b5-lattice-adapter-preflight-scratch.json").read_text())
R3=json.loads((ROOT/"stages/stage32-ex4/ex4-r3-kuusalo-second-generator-pair-preflight-scratch.json").read_text())
PRIOR=json.loads((ROOT/"stages/stage32-ex4/ex4-10s-retained-bounded-terminal-candidate.json").read_text())
RECEIPT=json.loads((ROOT/"stages/stage32-ex4/ex4-11-hostile-audit-pass-receipt.json").read_text())
START=(ROOT/"stages/stage32-ex4/MAIN-START-HERE.md").read_text()
ROADMAP=(ROOT/"stages/stage32-ex4/stage32-ex4.md").read_text()

assert STATE["schema"]=="STAGE32EX4_MAIN_COMPACT_STATE_V6_KUUSALO_R3_SCRATCH"
assert STATE["bootstrap"]["active_work_pr"]==1721
assert STATE["bootstrap"]["merge_authorized"] is False
assert STATE["authority"]["prior_bounded_terminal_claim_id"]=="S32.EX4.FIXED_SOURCE_PACKAGE_AMBIGUITY_TERMINAL.V2"
assert STATE["authority"]["prior_bounded_terminal_authority"]=="AUDITED"
assert STATE["authority"]["prior_bounded_terminal_remains_valid_for_old_frozen_package"] is True
assert STATE["authority"]["current_reentry_leaf_authority"]=="SCRATCH"
assert STATE["authority"]["stage32_main_authority_unchanged"] is True
assert STATE["current"]["leaf"]=="EX4-R3_KUUSALO_SECOND_GENERATOR_PAIR_PREFLIGHT"
assert STATE["current"]["next_leaf"]=="EX4-R4_KUUSALO_F2_BRANCH_ACTION_TO_CECOTTI_B8_ALGEBRAIC_BINDING_PREFLIGHT"

assert RECEIPT["audit_result"]=="PASS"
assert RECEIPT["audit_review_id"]==5139609916
assert PRIOR["canonical_sha256_without_this_field"]=="57b7f3e052262ff42b157b29a05bf45cf56388fe849b4202474ad63df98ae615"
assert R2["canonical_sha256_without_this_field"]=="fdcaa13fe6708406387eb46fd7832b25fb891be183748f840777d7c5a8a9212a"
assert R3["canonical_sha256_without_this_field"]=="d5443619f6b781d13725fea69adf5f53ed24d412ffabf7c82b78e20a950310d4"

re=STATE["reentry"]
assert re["source_delta0inf_coordinate_mod2"]==[1,1,1,1]
assert re["period_adapter_count"]==48
assert re["period_adapter_delta_line_counts"]=={"L1":16,"L2":16,"L3":16}
assert re["transported_pair_distinct_projective_count"]==24
assert re["transported_pair_projective_delta_line_counts"]=={"L1":8,"L2":8,"L3":8}
assert re["literal_pair_compatible_adapter_count"]==2
assert re["literal_pair_delta_line"]=="L2"
assert re["literal_pair_conditional_residue"]==97
assert re["literal_pair_result_is_conditional_only"] is True

front=STATE["frontier"]
for k in [
 "new_marked_data_reentry_condition_met","source_side_branch_labelled_H1_marking_obtained",
 "source_side_delta0inf_coordinate_obtained","period_adapter_torsor_exact",
 "second_generator_source_matrix_obtained","second_generator_pair_transport_exact",
 "transported_projective_pair_count_24","literal_pair_would_select_L2"
]: assert front[k] is True,k
for k in [
 "period_equivalence_prunes_W_line","simultaneous_pair_data_prunes_W_line",
 "absolute_delta0inf_retained_W_line_identified","absolute_Q602_residue_identified",
 "current_extended_package_full_target_closure","audit_ready_current_reentry"
]: assert front[k] is False,k

credit=STATE["credit"]
assert credit["current_reentry_level"]=="SCRATCH_SECOND_GENERATOR_PAIR_ORBIT_EXACT_NONPRUNING"
assert credit["conditional_residue97_only"] is True
for k in ["absolute_W_line_and_Q602_residue_identified","Q602_residue_contraction_credit","Q602_excluded","O210_excluded","stage32_main_credit"]:
    assert credit[k] is False,k

fw=STATE["firewalls"]
for k in [
 "prior_audited_terminal_revoked","period_isomorphism_promoted_to_marked_isomorphism",
 "source_pair_orbit_promoted_to_literal_target_pair","literal_target_pair_promoted_without_source_binding",
 "conditional_residue97_promoted_to_absolute_residue","post1648j_candidate_self_promoted_to_audited_authority",
 "stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed",
 "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"
]: assert fw[k] is False,k

for p in set(STATE["current_leaf_working_set"]): assert (ROOT/p).exists(),p
assert "stage32ex4-mainbatch" in START
assert "Scratch results are non-authoritative" in START
assert "ABSOLUTE_W_LINE_AND_Q602_RESIDUE_IDENTIFIED" in ROADMAP
assert "FIXED_SOURCE_PACKAGE_CANNOT_SELECT_ABSOLUTE_W_LINE" in ROADMAP

runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r2_kuusalo_period_to_retained_b5_lattice_adapter_preflight_scratch.py"),run_name="__main__")
runpy.run_path(str(ROOT/"stages/stage32-ex4/verify_ex4_r3_kuusalo_second_generator_pair_preflight_scratch.py"),run_name="__main__")

print("Stage32EX4 MAIN Kuusalo R3 scratch state: PASS")
print("R2 adapters=48 line=16/16/16; R3 projective pairs=24 line=8/8/8")
print("literal_pair=(S*T^-1,-T) -> L2/residue97 conditional only; absolute=false")
