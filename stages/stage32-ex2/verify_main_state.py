#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
S=json.loads((HERE/"MAIN-STATE.json").read_text())
R=json.loads((ROOT/"stages/stage32/proof/CLAIM-REGISTRY.json").read_text())
L=json.loads((ROOT/"stages/stage32/proof/LANE-ADAPTERS.json").read_text())
CURRENT_MAIN="538913633330a8414c87931d3c52f93e4aaf5d0f"
assert S["schema"]=="STAGE32EX2_MAIN_COMPACT_STATE_V10_EX2_03F_CORRECTED_ADJOINT_BLOCKED_EX2_04_ACTIVE"
assert S["stage"]=="32EX2"
assert S["bootstrap"]["active_work_pr"]==1709 and S["bootstrap"]["merge_authorized"] is False
assert S["audit"]["status"]=="NOT_READY_INTERMEDIATE_LEAF_ONLY"
assert S["freshness"]["current_main_observed_sha"]==CURRENT_MAIN
assert S["freshness"]["last_reconciled_current_main_sha"]==CURRENT_MAIN
assert S["freshness"]["unreconciled_main_commit_count"]==0
assert S["freshness"]["stage32ex2_source_drift_in_intervening_main_commit"] is False
assert S["claim_sync"]["reconciled_current_main_sha"]==CURRENT_MAIN
A=S["authority"]
assert A["EX2_03D_candidate_claim_id"]=="S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"
assert A["EX2_03D_artifact_blob_sha1"]=="32e19797812f35ad15fc5cad7559be76140480ef"
assert A["EX2_03D_verifier_blob_sha1"]=="f7a3f88969b0599f20b0217e806f9441cfe68f01"
assert A["EX2_03E_artifact_blob_sha1"]=="3c93705c2515346853b58e337add31fa0ad83e93"
assert A["EX2_03E_claim_status"]=="TYPED_ROUTE_BLOCKER_NO_MATHEMATICAL_CLAIM_NO_CLAIM_DAG_ENTRY"
assert A["EX2_03F_artifact_blob_sha1"]=="f5e8c5dbf7d01bf9e71cde7c13924de0d66e3007"
assert A["EX2_03F_artifact_canonical_sha256"]=="d55e804b062ca30163451563ad14cbe2797d5c48a44d8ec044be149aba0007a7"
assert A["EX2_03F_diagnostic_blob_sha1"]=="636140991684704a5ba2d282094b9ab4bba386b8"
assert A["EX2_03F_verifier_blob_sha1"]=="9975ba1d418f341dbb8fe82153c473d1c5f8fc51"
assert A["EX2_03F_claim_status"]=="TYPED_ROUTE_BLOCKER_NO_MATHEMATICAL_CLAIM_NO_CLAIM_DAG_ENTRY"
F=S["frontier"]
assert F["EX2_03_zero_curve_nonfixedness_classified_count"]==2
assert F["EX2_03C_certified_nonfixed_zero_labels_1based"]==[17,98]
assert F["EX2_03C_unresolved_zero_labels_1based"]==[21,24,25,30,31]
assert F["EX2_03D_remaining_five_are_pairwise_disjoint_rational_conics"] is True
assert F["EX2_03D_remaining_five_intersection_matrix"]=="-4I5"
assert F["EX2_03D_remaining_five_restriction_bundle_abstractly_trivial"] is True
assert F["EX2_03D_RR_chi_drop_each"]==1
assert F["EX2_03D_h2_V6_minus_each_conic_zero"] is True
assert F["EX2_03D_remaining_five_H0_restriction_maps_computed"] is False
assert F["EX2_03D_remaining_five_fixedness_classified"] is False
assert F["EX2_03D_remaining_five_zero_curve_preflight_active"] is False
assert F["EX2_03E_five_conic_evaluation_preflight_active"] is False
assert F["EX2_03E_naive_adjoint_nef_route_blocked"] is True
assert F["EX2_03F_corrected_adjoint_known140_scan_complete"] is True
assert F["EX2_03F_corrected_adjoint_known140_negative_labels_1based"]==[17,26,28]
assert F["EX2_03F_corrected_adjoint_known140_negative_count_each"]==3
assert F["EX2_03F_corrected_adjoint_global_nef_proved"] is False
assert F["EX2_03F_H1_vanishing_proved"] is False
assert F["EX2_04_finite_dimensional_section_reconstruction_active"] is True
assert S["current"]["leaf"]=="EX2-04_FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION"
assert S["current"]["subroute"]=="FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION_OUTSIDE_KNOWN140_MONOID"
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
 "stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed",
 "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim",
]:
    assert S["firewalls"][k] is False, k
claims={c["claim_id"]:c for c in R["claims"]}
c=claims["S32.EX2.FIVE_CONIC_RESTRICTION_REDUCTION.V1"]
assert c["authority_status"]=="PROVISIONAL"
assert c["claim_core_sha256"]=="1a4220aae62ee856710131f5dd89173ced6ce3f40ecc741af349697677955576"
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
]:
    subprocess.check_call([sys.executable,"-B",str(HERE/rel)],cwd=ROOT)
print("PASS Stage32EX2 MAIN state V10")
print("current_leaf=EX2-04 finite-dimensional section reconstruction")
print("freshness_reconciled_main="+CURRENT_MAIN)
print("EX2-03F corrected-adjoint blockers=17,26,28 targets=21,24,25,30,31")
print("merge_authorized=false stage32_main_credit=false")
