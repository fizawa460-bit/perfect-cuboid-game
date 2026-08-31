#!/usr/bin/env python3
"""Assemble the current Stage33-12 arithmetic-HS obstruction inventory.

The Kc two-primary block is closed by exact zero Q-survival.  It must not be
reused as a Q-defined J2 kernel charge on the distinct full-surface receiver.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE33=HERE.parent
ROOT=STAGE33.parent.parent
OUT=HERE/"stage33-12-exact-obstruction-inventory.json"

def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(rel):
    return json.loads((ROOT/rel).read_text(encoding="utf-8"))
def locked(rel,expected):
    o=load(rel); b=dict(o); claimed=b.pop("canonical_sha256",None)
    if claimed!=expected or csha(b)!=expected:
        raise SystemExit(f"canonical source lock moved: {rel}")
    return o

c09=locked("stages/stage33/33-09/stage33-09-closure.json","6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7")
h10=locked("stages/stage33/33-10/handoff.json","4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f")
e11=locked("stages/stage33/33-11g/stage33-11g-hostile-audit-exact-exit-certificate.json","233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e")
zero=locked("stages/stage33/33-05/stage33-05-br2-zero-q-survival-hostile-replay.json","4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9")
odd=locked("stages/stage33/33-07/proper-brauer-odd-invariants-zero.json","63f1ba53a422a7d9334767d5cde2d52a4535b8022d3f78b214f981ad0596fcc9")
proper2=locked("stages/stage33/33-07/proper-brauer2-from-discriminant.json","c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf")
adjust=locked("stages/stage33/33-12/full-surface-hs-adjustment-contract.json","ec455bac5ba80c5be07e3eff045bb180d4b63d6d02bd6e8758c1c02e130b4f5b")
target=locked("stages/stage33/33-12/full-surface-pic2-kummer-target.json","384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890")
controller=load("stages/stage33/controller.json")

if c09["exit_condition"]["PICARD_EQUIVARIANT_TRANSPORT_CLOSED"] is not True: raise SystemExit("33-09 regressed")
if h10["status"]!="CLOSED_EXACT": raise SystemExit("33-10 regressed")
if e11["exact_result"]["arithmetic_localization_connecting_map"]!="COMPUTED_EXACT_ZERO_MAP" or e11["exact_result"]["connecting_columns_exact_audited"]!="26/26": raise SystemExit("33-11 regressed")
if zero["hostile_checks"]["global_kernel_dimension_f2"]!=0 or zero["verdict"]["corrected_J2_Q_defined_Brauer_preimage"] is not False: raise SystemExit("33-05 zero survival regressed")
if odd["repair_reduced_to_two_primary"] is not True or odd["constant_odd_boundary_cokernel_globally_liftable_part"]!="0": raise SystemExit("odd-primary closure regressed")
if proper2["proper_Br2_joint_v4_fixed_dimension_f2"]!=10: raise SystemExit("full-surface invariant dimension regressed")
if adjust["full_surface_proper_adjustment_module"]["known_q_defined_zero_boundary_proper_subgroup_dimension_f2_charged"]!=0: raise SystemExit("stale J2 kernel charge reappeared")
if target["finite_v4_pic2_cohomology"]["H1_dimension_f2"]!=75 or target["proper_invariant_domain"]["dimension_f2"]!=10: raise SystemExit("retained finite-V4 target basis regressed")
if controller["stage33_progress"]!="6/11" or controller["stage33_07"]["unit_closed"]: raise SystemExit("controller firewall regressed")

directions=[f"A2_{i:02d}" for i in range(1,27)]
cert={
 "schema":"STAGE33_12_EXACT_ARITHMETIC_HS_OBSTRUCTION_INVENTORY_V2_KC_ZERO_SURVIVAL_NO_J2_KERNEL_CHARGE",
 "stage":"33","unit":"33-12",
 "source_locks":{
   "stage33_09_closure_sha256":"6c3ff8f7ca7d1bbd4084da0cc77ca6d43b31b32566a3bbb2c2103b7c2e9548b7",
   "stage33_10_handoff_sha256":"4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f",
   "stage33_11g_certificate_sha256":"233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e",
   "stage33_05_zero_survival_hostile_sha256":"4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9",
   "proper_brauer_odd_invariants_sha256":"63f1ba53a422a7d9334767d5cde2d52a4535b8022d3f78b214f981ad0596fcc9",
   "proper_brauer2_from_discriminant_sha256":"c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
   "full_surface_hs_adjustment_contract_sha256":"ec455bac5ba80c5be07e3eff045bb180d4b63d6d02bd6e8758c1c02e130b4f5b",
   "full_surface_pic2_kummer_target_retained_basis_sha256":"384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890"},
 "audited_interface_assembly":{"stage33_09_picard_equivariant_transport":"CLOSED_EXACT","stage33_10_absolute_receiver":"EXACT","stage33_11_connecting_map":"COMPUTED_EXACT_ZERO_MAP","stage33_11_connecting_columns_exact_audited":"26/26","stage33_05_Kc_Br2_Q_survival_dimension_f2":0},
 "two_stage_separation":{"stage_A_localization_connecting_map":"CLOSED_EXACT_ZERO_ON_ALL_26_FINITE_DIRECTIONS","stage_B_hoch_schild_serre_d2":"UNCOMPUTED_ON_FULL_SURFACE_PROPER_10D_AND_REMAINING_TWO_PRIMARY_BLOCKS","connecting_zero_implies_hs_d2_zero_without_adapter":False,"connecting_zero_implies_global_q_lift_without_adapter":False},
 "Kc_zero_survival_effect":{"Kc_invariant_dimension_f2":2,"Kc_Q_surviving_dimension_f2":0,"corrected_J2_Q_defined_Brauer_preimage":False,"q1_Q_defined_Brauer_preimage":False,"old_inventory_J2_Q_defined_proper_class_charge_revoked":True,"Kc_zero_survival_implies_full_surface_P_zero":False},
 "odd_primary_completion":{"proper_geometric_brauer_odd_gq_invariants":"0","constant_odd_boundary_cokernel_globally_liftable_part":"0","new_odd_primary_q_defined_residue_lifts_required":0,"status":"EXACT_COMPLETE_NO_NEW_ODD_PRIMARY_BLOCK"},
 "full_surface_stage_B_adjustment":{"proper_invariant_module":"P=Br(Sbar)[2]^{G_Q}","proper_invariant_dimension_f2":10,"known_q_defined_zero_boundary_proper_subgroup_dimension_f2_charged":0,"proper_d2_map_materialized":False,"finite_v4_pic2_h1_dimension_f2":75,"finite_v4_kummer_defect_matrix_shape":[75,10],"finite_v4_kummer_defect_columns_materialized":0,"retained_target_basis_certificate_note":"The V1 target certificate remains valid for its 75D H1 basis and 10D domain basis only. Its historical J2 kernel lower-bound field is superseded by the V3 adjustment contract.","absolute_h1_identified_with_finite_v4_h1":False},
 "remaining_two_primary_obstruction_blocks":[
   {"block_id":"C2_CONSTANT_COKERNEL","group":odd["remaining_two_primary_constant_unknown"],"full_cokernel_claimed_globally_liftable":False,"liftable_subgroup_exact_safe_bound":{"proper_geometric_br2_gq_invariant_dimension_f2":10,"known_q_defined_zero_boundary_proper_subgroup_dimension_f2_charged":0,"therefore_dimension_upper_bound_f2":10,"therefore_cardinality_upper_bound":1024,"therefore_exponent":2,"old_9_dimension_512_bound_revoked":True,"reason":"The previous one-dimensional subtraction used the historical J2 Q-defined proper-class claim. Current Stage33-05 exact zero survival removes that charge, so only the ambient 10D full-surface invariant bound is presently justified."},"hs_d2_status":"UNCOMPUTED_PARAMETRIC_MAP","global_q_residue_lift_status":"UNRESOLVED"},
   {"block_id":"F26_FINITE_AFTER_U44","group":odd["remaining_finite_two_primary_hs_unknown"],"invariant_factor_generator_count":26,"named_direction_ids":directions,"localization_connecting_map_status":"ZERO_EXACT_AUDITED_26_OF_26","boundary_function_galois_scalar_correction":"ZERO_EXACT_ALL_26_DIRECTIONS","hs_d2_status":"26_NAMED_VALUES_UNCOMPUTED","global_q_residue_lift_status":"26_NAMED_LIFTS_UNRESOLVED"}],
 "exact_remaining_work":{"unresolved_block_count":2,"next_leaf":"MATERIALIZE_ONE_75_COORDINATE_FINITE_V4_KUMMER_DEFECT_COLUMN_FROM_A_FULL_SURFACE_MU2_LIFT_OR_EQUIVALENT_UNIMODULAR_GLUE_DATUM","why_one_column_first":"No full-surface Kummer extension producer is currently retained. One exact column is the minimal proof that the missing interface is constructible; guessed zero columns and blind 10-column filling are forbidden."},
 "stage33_12_exit":{"arithmetic_hs_d2_computed":False,"global_q_br0g_residue_lifts_complete":False,"complete_relevant_q_defined_class_list_for_stage33_brauer_scope":False,"stage33_07_hostile_reaudit":"NOT_RUN","stage33_12_closed":False},
 "firewalls":{"stage33_progress":"6/11","stage33_07_closed":False,"stage33_08_released":False,"stage33_40_released":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
cert["canonical_sha256"]=csha(cert)
if cert["canonical_sha256"]!="3187e5d4bb4b0dd7b47841fd7be097bb71858183cc7af49c527254994360720c": raise SystemExit("inventory canonical regression")
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"J2_kernel_charge":0,"constant_bound_dimension_f2":10,"constant_bound_cardinality":1024,"next_leaf":cert["exact_remaining_work"]["next_leaf"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
