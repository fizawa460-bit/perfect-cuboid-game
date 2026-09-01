#!/usr/bin/env python3
"""Build/check the compact Stage33 MAIN startup projection.

V6 keeps the independently exact corrected J2 proper-Br2 source and raw/75D
J2 target, but revokes their former Kummer source-target binding after the exact
all-V4-module-extension compatibility audit. Ordinary MAIN now starts directly
at that binding repair instead of accumulating relations from a false rank-one
anchor.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CONTROLLER=HERE/'controller.json'
ORIENTATION=HERE/'33-12'/'j2-cv-d2-semantic-orientation.json'
PROPER=HERE/'33-07'/'proper-brauer2-from-discriminant.json'
DOMAIN=HERE/'33-12'/'full-surface-pic2-kummer-target.json'
TARGET=HERE/'33-12'/'j2-named-v4-h1-target-before-source-orientation.json'
U1=HERE/'33-12'/'j2-semantic-u1-full-surface-smith-source.json'
U2=HERE/'33-12'/'j2-semantic-u2-full-surface-at2.json'
ADJOINT=HERE/'33-12'/'j2-picard-adjoint-proper-br2.json'
OLD_RELATION=HERE/'33-12'/'j2-named-kummer-source-target-relation.json'
COMPAT=HERE/'33-12'/'j2-kummer-source-target-module-compatibility-audit.json'
OUT=HERE/'MAIN-STATE.json'
LOCKS={
 ORIENTATION:'0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e',
 PROPER:'c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf',
 DOMAIN:'384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890',
 TARGET:'4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3',
 U1:'ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec',
 U2:'60b6d058459f7745f6fa3f9b6d3b44f1610e12ff46c42e3133ec574f71613039',
 ADJOINT:'066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',
 OLD_RELATION:'0563af417d41765e39ecb1b73fdabf33c1bc831e78f74d2227d286227c3aa082',
 COMPAT:'463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229',
}
def csha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected=None):
 x=json.loads(p.read_text(encoding='utf-8')); b=dict(x); h=b.pop('canonical_sha256'); assert h==csha(b),p
 if expected is not None: assert h==expected,p
 return x,h

controller=json.loads(CONTROLLER.read_text(encoding='utf-8'))
orientation,_=load(ORIENTATION,LOCKS[ORIENTATION]); proper,_=load(PROPER,LOCKS[PROPER]); domain,_=load(DOMAIN,LOCKS[DOMAIN]); target,_=load(TARGET,LOCKS[TARGET]); u1,_=load(U1,LOCKS[U1]); u2,_=load(U2,LOCKS[U2]); adj,_=load(ADJOINT,LOCKS[ADJOINT]); old_relation,_=load(OLD_RELATION,LOCKS[OLD_RELATION]); compat,_=load(COMPAT,LOCKS[COMPAT])
stage=controller['stage33_12']; current=controller['current']; p=adj['proper_brauer2_pullback']; h1=target['retained_H1_projection']; db=domain['proper_invariant_domain']
assert controller['schema']=='STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V52_J2_KUMMER_BINDING_REPAIR'
assert p['proper_Br2_14D_coordinate_f2']==[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert p['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert old_relation['source']['retained_10D_coordinate_f2']==p['retained_10D_coordinate_f2']
assert old_relation['target']['coordinates_f2']==h1['coordinates_f2']
assert compat['status']=='FAIL_EXACT_LOCKED_J2_SOURCE_TARGET_MODULE_COMPATIBILITY'
assert compat['locked_named_j2']['proper_Br2_14D_coordinate_f2']==p['proper_Br2_14D_coordinate_f2']
assert compat['locked_named_j2']['retained_10D_support_1based']==[2,3]
assert compat['locked_named_j2']['locked_75D_target_weight']==15
assert compat['locked_named_j2']['reachable_H1_subspace_dimension_f2']==13
assert compat['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert compat['consequence']['old_relation_may_be_used_as_kummer_matrix_relation'] is False
assert compat['consequence']['named_source_target_relation_rank_credit_after_this_audit']==0
assert stage['corrected_J2_proper_Br2_14D_coordinate_materialized'] is True
assert stage['corrected_J2_proper_Br2_14D_coordinate_f2']==p['proper_Br2_14D_coordinate_f2']
assert stage['corrected_J2_retained_10D_domain_coordinate_materialized'] is True
assert stage['corrected_J2_retained_10D_domain_coordinate_f2']==p['retained_10D_coordinate_f2']
assert stage['corrected_J2_named_V4_H1_target_materialized'] is True
assert stage['corrected_J2_named_source_target_relation_materialized'] is False
assert stage['corrected_J2_named_source_target_relation_status']=='REVOKED_BY_EXACT_V4_MODULE_COMPATIBILITY_AUDIT'
assert stage['corrected_J2_kummer_source_target_module_compatibility'] is False
assert stage['corrected_J2_kummer_source_target_module_compatibility_audit_sha256']==LOCKS[COMPAT]
assert stage['finite_v4_kummer_named_relations_materialized']==0
assert stage['finite_v4_kummer_named_relation_rank_f2']==0
assert stage['finite_v4_kummer_columns_materialized']==0 and stage['first_exact_kummer_column_materialized'] is False
assert db['dimension_f2']==10 and h1['retained_H1_dimension_f2']==75

out={
 'schema':'STAGE33_MAIN_COMPACT_STATE_V6',
 'role':'ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE',
 'detailed_machine_authority':'stages/stage33/controller.json',
 'controller_schema':controller['schema'],
 'stage33_progress':controller['stage33_progress'],
 'current':{k:current[k] for k in ['unit','logical_internal_branch','substep','active_missing_interface','next_exact_leaf']},
 'exact_reusable_inputs':{
  'named_J2_semantic_orientation':{'label':'u1','fixed_marked_Kc_coordinate_f2':[1,0],'certificate':'stages/stage33/33-12/j2-cv-d2-semantic-orientation.json','canonical_sha256':LOCKS[ORIENTATION]},
  'proper_Br2_domain':{'ambient_dimension_f2':14,'retained_invariant_dimension_f2':10,'retained_10D_basis_rows_in_proper14_coordinates_f2':db['basis_rows_original_proper_br2_coordinates_f2'],'retained_basis_sha256':db['basis_sha256'],'proper14_canonical_sha256':LOCKS[PROPER],'target_basis_canonical_sha256':LOCKS[DOMAIN]},
  'corrected_J2_picard_adjoint_source':{'proper_Br2_14D_coordinate_f2':p['proper_Br2_14D_coordinate_f2'],'retained_10D_coordinate_f2':p['retained_10D_coordinate_f2'],'proper14_weight':p['proper_Br2_14D_weight'],'retained10_weight':p['retained_10D_weight'],'certificate':'stages/stage33/33-12/j2-picard-adjoint-proper-br2.json','canonical_sha256':LOCKS[ADJOINT]},
  'named_J2_locked_target':{'ambient_dimension_f2':75,'coordinates_f2':h1['coordinates_f2'],'coordinate_weight':15,'nonzero':True,'certificate':'stages/stage33/33-12/j2-named-v4-h1-target-before-source-orientation.json','canonical_sha256':LOCKS[TARGET]},
  'J2_source_target_module_compatibility_audit':{'compatible':False,'locked_source_reachable_H1_dimension_f2':13,'old_relation_rank_credit_after_audit':0,'old_standard_column_equation_valid':False,'certificate':'stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json','canonical_sha256':LOCKS[COMPAT]},
  'semantic_discriminant_pullbacks':{'u1_full_surface_A_T_2_f2':u1['exact_normalization']['full_surface_A_T_2_coordinates_f2'],'u2_full_surface_A_T_2_f2':u2['semantic_u2_pullback']['full_surface_A_T_2_coordinates_f2'],'u1_u2_cross_bilinear_numerator_mod8':u2['semantic_u2_pullback']['cross_bilinear_with_u1_numerator_mod8_for_b_equals_num_over_8']},
 },
 'revoked_claims':{
  'J2_named_Kummer_source_target_relation':{'status':'REVOKED_EXACT_DO_NOT_USE','historical_certificate':'stages/stage33/33-12/j2-named-kummer-source-target-relation.json','historical_canonical_sha256':LOCKS[OLD_RELATION],'historical_equation':'C2 + C3 = h_J2','reason':'locked source and locked target are not realizable as one Kummer boundary pair under any V4-module extension compatible with the locked Pic/2 and proper-Br2 actions','revoking_certificate':'stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json','revoking_canonical_sha256':LOCKS[COMPAT]},
 },
 'resolved_investigations':{
  'named_J2_semantic_orientation':{'status':'RESOLVED_DO_NOT_REINVESTIGATE_IN_ORDINARY_MAIN','fact':'named J2 is semantic u1 with marked Kc coordinate [1,0]','source_canonical_sha256':LOCKS[ORIENTATION]},
  'A_T_2_coefficients_are_not_proper_dual_coefficients':{'status':'REJECTED_EXACT_DO_NOT_RETRY','fact':'do not copy the u1 A_T[2] vector into the proper-Br2 dual basis'},
  'order4_direct_picard_pullback_route':{'status':'SUPERSEDED_DO_NOT_REOPEN','fact':'the lift-sensitive direct order4 route is unnecessary for J2 proper-Br2 after the exact Picard-adjoint map'},
  'J2_picard_adjoint_source_coordinate':{'status':'RESOLVED_EXACT_DO_NOT_REINVESTIGATE','fact':{'proper14':p['proper_Br2_14D_coordinate_f2'],'retained10':p['retained_10D_coordinate_f2']},'source_certificate':'stages/stage33/33-12/j2-picard-adjoint-proper-br2.json','source_canonical_sha256':LOCKS[ADJOINT]},
  'J2_raw_75D_target_projection':{'status':'RESOLVED_EXACT_INDEPENDENT_TARGET','fact':'the raw J2 V4 Pic/2 cocycle projects exactly to the locked nonzero weight-15 75D H1 target; this does not by itself identify its proper-Br2 source coordinate','source_certificate':'stages/stage33/33-12/j2-named-v4-h1-target-before-source-orientation.json','source_canonical_sha256':LOCKS[TARGET]},
  'J2_source_target_Kummer_binding':{'status':'REVOKED_EXACT_REPAIR_REQUIRED','fact':'the locked proper-Br2 source retained10=e2+e3 has a 13D reachable H1 subspace across all compatible V4-module extensions, and the locked J2 75D target is outside it; do not use C2+C3=h_J2','source_certificate':'stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json','source_canonical_sha256':LOCKS[COMPAT]},
 },
 'anti_loop_reopen_policy':{'ordinary_main_rule':'Do not reinvestigate resolved_investigations while all listed source locks still match. Repair only the explicitly open source-target binding adapter.','reopen_only_if':['a listed source canonical_sha256 changes','an authoritative current certificate contradicts the recorded fact','the user explicitly requests hostile audit or historical revalidation']},
 'open_datum':{
  'corrected_J2_current_proper_Br2_14D_coordinate_materialized':True,
  'corrected_J2_retained_10D_coordinate_materialized':True,
  'named_J2_raw_75D_target_materialized':True,
  'named_J2_source_target_relation_materialized':False,
  'named_source_target_relation_rank_f2':0,
  'matrix_standard_columns_materialized':stage['finite_v4_kummer_columns_materialized'],
  'first_exact_standard_75D_column_materialized':stage['first_exact_kummer_column_materialized'],
  'active_missing_interface':current['active_missing_interface'],
 },
 'current_leaf_working_set':[
  'stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json',
  'stages/stage33/33-12/verify_j2_kummer_source_target_module_compatibility.py',
  'stages/stage33/33-12/audit_v4_kummer_extension_space_after_j2_anchor.py',
  'stages/stage33/33-12/j2-picard-adjoint-proper-br2.json',
  'stages/stage33/33-12/j2-named-v4-h1-target-before-source-orientation.json',
  'stages/stage33/33-12/full-surface-pic2-kummer-target.json',
 ],
 'targeted_expansion_hints':{'human_checkpoint_only_if_needed':'stages/stage33/33-12/result.md','detailed_state_only_if_state_write_needed':'stages/stage33/controller.json','raw_J2_cocycle_only_if_binding_repair_needs_it':['stages/stage33/33-12/j2-cc-actual-cech-global-square-overlap.json','stages/stage33/33-12/j2-ct-six-kc-support-fullpic64-pullbacks.json']},
 'default_startup_exclusions':['stages/stage33/controller-post-r5-hs-d2-override.json','stages/stage33/33-05/j2-post-r5-hs-d2-state.json','stages/stage33/33-05/j2-representative-repair-state.json','stages/stage33/HISTORY.md','stages/stage33/ROADMAP.md','stages/stage33/ROADMAP-33-07-REPAIR-BAND.md'],
 'firewalls':{'merge_allowed':controller['merge_allowed'],'stage33_12_closed_exact':stage['closed_exact'],'stage33_07_reclosed':controller['release_gates']['stage33_07_reclosed'],'stage33_08_released':controller['release_gates']['stage33_08_released'],'theorem_credit':controller['theorem_credit'],'receiver_credit':controller['receiver_credit'],'endpoint_credit':controller['endpoint_credit'],'perfect_cuboid_existence_claim':controller['perfect_cuboid_existence_claim'],'perfect_cuboid_nonexistence_claim':controller['perfect_cuboid_nonexistence_claim']},
}
out['canonical_sha256']=csha(out)
parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
rendered=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
if args.check:
 assert OUT.exists() and OUT.read_text(encoding='utf-8')==rendered, 'MAIN-STATE.json is stale; run sync_main_state.py'
 print(json.dumps({'success':True,'mode':'check','canonical_sha256':out['canonical_sha256']},sort_keys=True))
else:
 OUT.write_text(rendered,encoding='utf-8')
 print(json.dumps({'success':True,'mode':'write','canonical_sha256':out['canonical_sha256']},sort_keys=True))
