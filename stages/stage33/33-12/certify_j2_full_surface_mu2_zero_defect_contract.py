#!/usr/bin/env python3
"""Freeze revocation of the historical full-surface J2 mu2 zero-defect credit."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ADJUST=HERE/"full-surface-hs-adjustment-contract.json"
REOPEN=HERE/"j2-cv-lclass-zero-regression.json"
OUT=HERE/"j2-full-surface-mu2-zero-defect-contract.json"
EXPECTED_ADJUST="5d872ca51f4b3d7192dfc91764abe1d7e63ae62b0302cc08ea2b1abdb4062b7e"

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(path): return json.loads(path.read_text())
adjust=load(ADJUST); b=dict(adjust); claimed=b.pop("canonical_sha256",None)
if claimed!=EXPECTED_ADJUST or csha(b)!=EXPECTED_ADJUST: raise SystemExit("full-surface HS adjustment source lock moved")
reopen=load(REOPEN)
if reopen["status"]!="PASS_EXACT_UPSTREAM_REPRESENTATIVE_CONTRADICTION": raise SystemExit("hostile reopen certificate regression")
if adjust["full_surface_proper_adjustment_module"]["kernel_contains_q_defined_J2"]: raise SystemExit("stale J2 kernel credit reappeared")
certificate={
"schema":"STAGE33_12_J2_FULL_SURFACE_MU2_ZERO_DEFECT_CONTRACT_V2_REVOKED",
"status":"REVOKED_PENDING_NAMED_J2_REPRESENTATIVE_REPAIR",
"source_locks":{"full_surface_hs_adjustment_contract_sha256":EXPECTED_ADJUST,"hostile_reopen_certificate":"stages/stage33/33-12/j2-cv-lclass-zero-regression.json"},
"exact_input":{"class":"abstract J2","full_surface_q_defined_pullback_certified":False,"j2_certified_inside_P_equals_BrSbar2_GQ":False},
"kummer_exact_sequence":{"sequence":"Pic(S)/2 -> H^2_et(S,mu_2) -> Br(S)[2] -> 0","arithmetic_mu2_lift_exists_for_current_named_representative":False,"reason":"The previously charged Q-defined ell_J2 representative was revoked: it is zero in the geometric CV quotient. No nonzero named full-surface J2 representative is currently certified."},
"finite_v4_consequence":{"delta_Kum_V4_of_J2":"NOT_CREDITED_AFTER_HOSTILE_REOPEN","geometric_mu2_lift_is_v4_invariant":False,"integral_bockstein_of_this_zero_defect":"NOT_CREDITED","known_zero_defect_direction_dimension_lower_bound_f2":0},
"coordinate_firewall":{"j2_vector_in_original_proper_br2_coordinates_materialized":False,"j2_coordinates_in_retained_10_vector_P_basis_materialized":False,"existing_75x10_matrix_column_index_identified":False,"columns_materialized":0,"matrix_entries_materialized":0,"reason":"No coordinate or zero-defect credit may be assigned until a corrected nonzero named J2 representative is certified."},
"absolute_firewall":{"finite_V4_zero_implies_absolute_zero":False,"absolute_H1_identified_with_finite_V4_H1":False},
"next_exact_leaf":"REPAIR_OR_REPLACE_STAGE33_05_NAMED_J2_CV_REPRESENTATIVE_THEN_RECOMPUTE_EXPLICIT_CV_E2_COCYCLE",
"promotion_firewall":{"proper_d2_map_computed":False,"finite_obstruction_cosets_materialized":0,"arithmetic_hs_d2_computed":False,"global_q_residue_lifts_complete":False,"stage33_12_closed":False,"stage33_07_closed":False,"stage33_progress":"5/11","theorem_credit":False,"endpoint_credit":False,"class3_promoted":False}}
certificate["canonical_sha256"]=csha(certificate)
OUT.write_text(json.dumps(certificate,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"status":certificate["status"],"certificate_sha256":certificate["canonical_sha256"]},indent=2,sort_keys=True))
