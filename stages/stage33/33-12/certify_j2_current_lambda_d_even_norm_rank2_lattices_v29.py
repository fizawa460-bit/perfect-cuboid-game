#!/usr/bin/env python3
"""V29: current-lambda_D even-norm rank-two lattice/overlap normalization."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
OUT=HERE/"j2-current-lambda-d-even-norm-rank2-lattices-v29.json"
LOCKS={
"v25":("j2-genuine-h2-mu2-kummer-adapter-v25.json","d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"),
"v28":("j2-post-v27-exceptional-overlap-inheritance-audit-v28.json","919c1fd1dfb57f0e86677e64052636918082d7ef0cf9a9f79afe51051eb96095"),
"boundary":("j2-ct-norm-actual-boundary-sheet-frames.json","5b961822dc10e7a1a424ed87ba6307d83efd3a0b31671db305a609269094937b"),
"exceptionals":("j2-ct-norm-resolution-exceptional-sheet-frames.json","bbde421a54d2b7159f8d3ff4cf641cbddf2bbbc45fe4791cb7ed18d7cfb69591"),
"handoff":("j2-post-v28-main-handoff-v29.json","043e45366c428f70090a34a4d7e1dec1e7245962cc2165f6d9dd1343ec636042")}
EXPECTED="d59ccba621bf0a41a1b53bc400cd819cd48fd19b8357c21209a5b1755fe5611b"

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load(k):
 n,h=LOCKS[k]; o=json.loads((HERE/n).read_text()); b=dict(o); got=b.pop("canonical_sha256"); assert got==h==csha(b),(n,got,csha(b)); return o

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); args=ap.parse_args()
 v25,v28,bn,ex,ho=(load(k) for k in ("v25","v28","boundary","exceptionals","handoff"))
 assert v25["genuine_h2_mu2_adapter"]["kc_lift_class"]=="lambda_D=alpha(e_D), represented generically by {f2,g22}"
 assert v25["genuine_h2_mu2_adapter"]["historical_kummer_glue_used"] is False
 assert v28["historical_overlap_promotion_audit"]["historical_candidate_inherited_as_current_authority"] is False
 assert ho["status"]=="ACTIVE_V28_FRONTIER_CHECKPOINTED_BEFORE_V29"
 assert bn["actual_nullhomotopy"]["exact_norm_identity"]=="u*sigma_u=g22"
 bf=bn["boundary_sheet_frames"]; ef=ex["actual_ct_resolution_exceptional_sheet_frames"]
 def pair(rec): return [rec["ord_u"],rec["ord_sigma_u"]]
 local={
 "C21":{"uniformizer":"eta_C21","ord_norm":bf["C21"]["ord_norm"],"sheets":{"all":pair(bf["C21"]["all_generic_components"])},"h":0,"normalized_sigma_u":"sigma(u)","basis":["sigma(u)*e1","e2"],"matrix":"diag(sigma(u),1)","parity":0},
 "Sinf":{"uniformizer":"w","ord_norm":bf["Sinf"]["ord_norm"],"sheets":{"all":pair(bf["Sinf"]["all_generic_q_sheets"])},"h":-1,"normalized_sigma_u":"w*sigma(u)","basis":["w*sigma(u)*e1","e2"],"matrix":"diag(w*sigma(u),1)","parity":0},
 "E_00":{"uniformizer":"e","ord_norm":ef["E_00"]["ord_norm"],"sheets":{"plus":pair(ef["E_00"]["sheet_plus"]),"minus":pair(ef["E_00"]["sheet_minus"])},"h":0,"normalized_sigma_u":{"plus":"sigma(u)","minus":"sigma(u)"},"basis_formula":["sigma(u)*e1","e2"],"matrix_formula":"diag(sigma(u),1)","parity":1},
 "E_0inf":{"uniformizer":"e","ord_norm":ef["E_0inf"]["ord_norm"],"sheets":{"plus":pair(ef["E_0inf"]["sheet_plus"]),"minus":pair(ef["E_0inf"]["sheet_minus"])},"h":-1,"normalized_sigma_u":{"plus":"e*sigma(u)","minus":"e*sigma(u)"},"basis_formula":["e*sigma(u)*e1","e2"],"matrix_formula":"diag(e*sigma(u),1)","parity":0},
 "E_inf0":{"uniformizer":"e","ord_norm":ef["E_inf0"]["ord_norm"],"sheets":{"plus":pair(ef["E_inf0"]["sheet_plus"]),"minus":pair(ef["E_inf0"]["sheet_minus"])},"h":0,"normalized_sigma_u":{"plus":"sigma(u)","minus":"sigma(u)"},"basis_formula":["sigma(u)*e1","e2"],"matrix_formula":"diag(sigma(u),1)","parity":1},
 "E_infinf":{"uniformizer":"e","ord_norm":ef["E_infinf"]["ord_norm"],"sheets":{"plus":pair(ef["E_infinf"]["sheet_plus"]),"minus":pair(ef["E_infinf"]["sheet_minus"])},"h":-1,"normalized_sigma_u":{"plus":"e*sigma(u)","minus":"e*sigma(u)"},"basis_formula":["e*sigma(u)*e1","e2"],"matrix_formula":"diag(e*sigma(u),1)","parity":0},
 "quotient_A1_lifts":{"count":ex["singular_partition"]["unbranched_lifts_of_quotient_A1_nodes"],"uniformizer":"e_Q","ord_norm":ex["quotient_A1_exceptional_frames"]["generic_ord_norm"],"generic_sheet_orders":[ex["quotient_A1_exceptional_frames"]["generic_ord_u_on_every_auxiliary_q_cover_component"],ex["quotient_A1_exceptional_frames"]["generic_ord_sigma_u_on_every_auxiliary_q_cover_component"]],"h":0,"normalized_sigma_u":"sigma(u)","basis":["sigma(u)*e1","e2"],"matrix":"diag(sigma(u),1)","parity":0}}
 assert local["C21"]["sheets"]["all"]==[0,0] and local["Sinf"]["sheets"]["all"]==[-1,-1]
 assert local["E_00"]["sheets"]=={"plus":[-1,1],"minus":[1,-1]}
 assert local["E_0inf"]["sheets"]=={"plus":[-1,-1],"minus":[-1,-1]}
 assert local["E_inf0"]["sheets"]=={"plus":[1,-1],"minus":[-1,1]}
 assert local["E_infinf"]["sheets"]=={"plus":[-1,-1],"minus":[-1,-1]}
 assert local["quotient_A1_lifts"]["count"]==8 and local["quotient_A1_lifts"]["generic_sheet_orders"]==[0,0]
 forced=v28["retainable_local_parity_constraints"]["forced_parities"]
 for k in ("C21","Sinf","E_00","E_0inf","E_inf0","E_infinf"): assert local[k]["parity"]==forced[k]
 assert forced["eight_unbranched_quotient_A1_exceptionals"]==0
 payload={
 "schema":"STAGE33_12_J2_CURRENT_LAMBDA_D_EVEN_NORM_RANK2_LATTICES_V29","stage":"33-12",
 "status":"PASS_EXACT_CURRENT_LAMBDA_D_EVEN_NORM_NORMALIZED_RANK2_LATTICES_ODD_BOUNDARY_QROOT_AND_RAMIFIED_C22_OVERLAPS_OPEN",
 "source_locks":{
 "v25_current_named_j2":{"path":"stages/stage33/33-12/"+LOCKS["v25"][0],"canonical_sha256":LOCKS["v25"][1]},
 "v28_frontier":{"path":"stages/stage33/33-12/"+LOCKS["v28"][0],"canonical_sha256":LOCKS["v28"][1]},
 "boundary_sheet_frames":{"path":"stages/stage33/33-12/"+LOCKS["boundary"][0],"canonical_sha256":LOCKS["boundary"][1]},
 "resolution_exceptional_sheet_frames":{"path":"stages/stage33/33-12/"+LOCKS["exceptionals"][0],"canonical_sha256":LOCKS["exceptionals"][1]},
 "v28_handoff":{"path":"stages/stage33/33-12/"+LOCKS["handoff"][0],"canonical_sha256":LOCKS["handoff"][1]}},
 "current_lambda_D_anchor":{"class":"lambda_D=alpha(e_D), represented generically by {f2,g22}","source_first":True,"historical_pre_kummer_sheet_selection_used":False,"historical_weight15_h1_used":False},
 "rank2_normalization_lemma":{"normalized_operator":"for h=k/2, u'=pi^(-h)u, sigma(u)'=pi^(-h)sigma(u), b'=pi^(-2h)Norm(u)","norm_operator":"Y'=[[0,u'],[sigma(u)',0]]","cech_square_operator":"J'=[[0,b'],[1,0]]","explicit_basis_embedding":"G=diag(sigma(u)',1)","exact_conjugacy":"G*Y'*G^-1=J'","integral_fractional_lattice":"L=O*(sigma(u)'*e1) + O*e2 is a free rank-two O-lattice in the generic two-dimensional space","overlap_regularity":"G and G^-1 have entries in O[pi^-1], so the transition is regular and invertible on the punctured overlap","determinant_parity":"ord_pi(sigma(u)') mod 2; this is independent of the common scalar normalization"},
 "materialized_even_norm_local_lattices":local,
 "replay_summary":{"C21":0,"Sinf":0,"E_00":1,"E_0inf":0,"E_inf0":1,"E_infinf":0,"eight_unbranched_quotient_A1_exceptionals":0,"all_branch_crossing_sheet_choices_same_parity":True,"matches_v28_forced_even_norm_parities":True},
 "exact_information_boundary":{"current_lambda_D_even_norm_rank2_fractional_lattice_bases_materialized":True,"current_lambda_D_even_norm_punctured_overlap_matrices_materialized":True,"all_12_resolution_exceptionals_covered":True,"T0_Tinf_integral_overlap_selection_materialized":False,"qroot_ramified_overlap_selection_materialized":False,"C22_ramified_rank2_lattice_materialized":False,"actual_full_current_overlap_2x2_matrices_materialized":False,"actual_ct_defect_marked_Pic_mod2_materialized":False,"hs_d2_2cocycle_materialized":False,"standard_kummer_columns_materialized":0},
 "next_exact_leaf":"CONSTRUCT_CURRENT_LAMBDA_D_ODD_NORM_T0_TINF_AND_RAMIFIED_QROOT_C22_LOCAL_LATTICES_WITH_EXPLICIT_REGULAR_2X2_OVERLAP_MATRICES_FROM_V25_SURFACE_ADAPTER; DO_NOT_IMPORT_PRE_KUMMER_SHEET_SELECTION",
 "promotion_firewall":{"merge_allowed":False,"stage33_12_closed_exact":False,"theorem_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
 assert csha(payload)==EXPECTED,csha(payload)
 out=dict(payload); out["canonical_sha256"]=EXPECTED
 if args.check: assert json.loads(OUT.read_text())==out
 else: OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"success":True,"canonical_sha256":EXPECTED,"status":out["status"]},sort_keys=True))
if __name__=="__main__": main()
