#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
S=json.loads((HERE/"MAIN-STATE.json").read_text())
R=json.loads((ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json").read_text())
L=json.loads((ROOT/"stages/stage32/proof/LANE-ADAPTERS.json").read_text())
CURRENT_MAIN="42f20e47babdfdda068a605e3fec489eeace460c"
AUDIT_HEAD="0a39b08b767681f1a475dbe12d87e29315af041d"
AUDIT_REVIEW=5142431810
assert S["schema"]=="STAGE32EX2_MAIN_COMPACT_STATE_V11_EX2_04A_TWO_DIVISOR_PENCIL_EX2_04B_ACTIVE"
assert S["stage"]=="32EX2"
assert S["bootstrap"]["active_work_pr"]==1709 and S["bootstrap"]["merge_authorized"] is False
assert S["audit"]["status"]=="NOT_READY_NEW_EX2_04A_PROVISIONAL_AFTER_AUDITED_INTERMEDIATE_CHECKPOINT"
assert S["audit"]["previous_intermediate_pass"]=={
    "credit_ceiling":"NECESSARY_CONDITION_ONLY","exact_head":AUDIT_HEAD,"review_id":AUDIT_REVIEW,"status":"PASS","through":"EX2-03F"
}
assert S["freshness"]["current_main_observed_sha"]==CURRENT_MAIN
assert S["freshness"]["last_reconciled_current_main_sha"]==CURRENT_MAIN
assert S["freshness"]["unreconciled_main_commit_count"]==0
assert S["freshness"]["stage32ex2_source_drift_in_intervening_main_commit"] is False
assert S["claim_sync"]["reconciled_current_main_sha"]==CURRENT_MAIN
assert S["claim_sync"]["audit_transition_triggered"] is True
assert S["claim_sync"]["audited_intermediate_exact_head"]==AUDIT_HEAD
assert S["claim_sync"]["audited_intermediate_review_id"]==AUDIT_REVIEW
A=S["authority"]
assert A["EX2_03D_candidate_claim_id"]=="S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"
assert A["EX2_03D_artifact_blob_sha1"]=="32e19797812f35ad15fc5cad7559be76140480ef"
assert A["EX2_03D_verifier_blob_sha1"]=="f7a3f88969b0599f20b0217e806f9441cfe68f01"
assert A["EX2_03F_artifact_blob_sha1"]=="f5e8c5dbf7d01bf9e71cde7c13924de0d66e3007"
assert A["EX2_03F_artifact_canonical_sha256"]=="d55e804b062ca30163451563ad14cbe2797d5c48a44d8ec044be149aba0007a7"
assert A["EX2_04A_artifact_blob_sha1"]=="3122bccb0afe2c72ac13b24e385aaaaa1dd67956"
assert A["EX2_04A_artifact_canonical_sha256"]=="ba5a134d3438453ece33ad05ea5ab556db5108c894864ff3c067269b38d46b34"
assert A["EX2_04A_verifier_blob_sha1"]=="e56fe9b91551c39250a1faf5de0060e697c23e73"
assert A["EX2_04A_candidate_claim_id"]=="S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"
assert A["EX2_04A_claim_status"]=="PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED"
F=S["frontier"]
assert F["EX2_03_zero_curve_nonfixedness_classified_count"]==2
assert F["EX2_03C_certified_nonfixed_zero_labels_1based"]==[17,98]
assert F["EX2_03C_unresolved_zero_labels_1based"]==[21,24,25,30,31]
assert F["EX2_03D_remaining_five_are_pairwise_disjoint_rational_conics"] is True
assert F["EX2_03D_remaining_five_intersection_matrix"]=="-4I5"
assert F["EX2_03D_remaining_five_restriction_bundle_abstractly_trivial"] is True
assert F["EX2_03D_remaining_five_fixedness_classified"] is False
assert F["EX2_03F_corrected_adjoint_known140_negative_labels_1based"]==[17,26,28]
assert F["EX2_04A_certified_two_dimensional_section_subspace"] is True
assert F["EX2_04A_projective_pencil_dimension"]==1
assert F["EX2_04A_common_divisor_labels_1based"]==[21,24,25,30,31]
assert F["EX2_04A_common_divisor_multiplicities"]==[3,3,6,2,5]
assert F["EX2_04A_outside_known140_member_certified"] is False
assert F["EX2_04A_third_explicit_section_outside_pencil"] is False
assert F["certified_section_subspace_dimension"]==2
assert F["complete_section_space_basis_obtained"] is False
assert F["EX2_04_finite_dimensional_section_reconstruction_active"] is True
assert S["current"]["leaf"]=="EX2-04_FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION"
assert S["current"]["subroute"]=="EX2-04B_SECTION_OUTSIDE_RETAINED_TWO_DIVISOR_PENCIL"
assert S["completion_contract"]["terminal_outcome"] is None
assert S["credit"]["genuine_v6_genus1_member_established"] is False
assert S["credit"]["no_integral_irreducible_v6_genus1_member_in_linear_system"] is False
assert S["credit"]["full_target_closure"] is False
assert S["credit"]["stage32_main_credit"] is False
for k in [
 "trivial_conic_restriction_promoted_to_nonfixedness",
 "trivial_conic_restriction_promoted_to_fixedness",
 "rr_chi_drop_promoted_to_h0_drop",
 "remaining_five_known140_unsat_promoted_to_fixedness",
 "corrected_adjoint_known140_scan_promoted_to_global_nef",
 "h1_vanishing_inferred_from_blocked_nef_route",
 "nef_route_blocker_promoted_to_fixedness",
 "two_dimensional_section_subspace_promoted_to_complete_H0",
 "common_pencil_divisor_promoted_to_complete_fixed_part",
 "h0_lower_bound_promoted_to_explicit_third_section",
 "known140_endpoint_pencil_promoted_to_outside_known140_member",
 "stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed",
 "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim",
]:
    assert S["firewalls"][k] is False, k
claims={c["claim_id"]:c for c in R["claims"]}
for cid in [
    "S32.EX2.SECTION_SOURCE_INVENTORY.V2",
    "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1",
    "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1",
    "S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1",
]:
    c=claims[cid]
    assert c["authority_status"]=="AUDITED", cid
    assert c["audit_receipt"]=={"exact_head":AUDIT_HEAD,"pr":1709,"review_id":AUDIT_REVIEW,"status":"PASS"}, cid
c=claims["S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"]
assert c["authority_status"]=="PROVISIONAL" and c["audit_receipt"] is None
assert c["claim_core_sha256"]=="18eb3df3292426421578f63f55c7e4552dbd2662e8b7682e970c66be3c5c0d97"
ex2=next(x for x in L["lanes"] if x["lane"]=="EX2")
assert c["claim_id"] in ex2["claim_refs"]
for rel in [
 "verify_ex2_00_source_lock.py",
 "verify_ex2_01_section_sources_v2.py",
 "verify_ex2_02_fixed_components.py",
 "verify_ex2_03_restriction_gap.py",
 "verify_ex2_03b_v6_stabilizer_orbit.py",
 "verify_ex2_03c_omission_witnesses.py",
 "verify_ex2_03d_five_conic_restriction.py",
 "verify_ex2_03e_adjoint_nef_blocker.py",
 "verify_ex2_03f_corrected_adjoint_known140.py",
 "verify_ex2_04a_two_divisor_section_pencil.py",
]:
    subprocess.check_call([sys.executable,"-B",str(HERE/rel)],cwd=ROOT)
print("PASS Stage32EX2 MAIN state V11")
print("current_leaf=EX2-04B section outside retained two-divisor pencil")
print("freshness_reconciled_main="+CURRENT_MAIN)
print("audited_intermediate_head="+AUDIT_HEAD+" review=5142431810 through=EX2-03F")
print("EX2-04A certified_subspace_dimension=2 provisional=true complete_H0=false")
print("merge_authorized=false stage32_main_credit=false")
