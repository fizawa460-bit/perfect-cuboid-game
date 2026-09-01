#!/usr/bin/env python3
"""Build/check compact Stage33 MAIN V10 after certified qPic bridge + actual S3 descent."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

H=Path(__file__).resolve().parent; OUT=H/'MAIN-STATE.json'
LOCKS={
 'orientation':(H/'33-12/j2-cv-d2-semantic-orientation.json','0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e'),
 'proper':(H/'33-07/proper-brauer2-from-discriminant.json','c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'),
 'target':(H/'33-12/j2-named-v4-h1-target-before-source-orientation.json','4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3'),
 'adjoint':(H/'33-12/j2-picard-adjoint-proper-br2.json','066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8'),
 'compat':(H/'33-12/j2-kummer-source-target-module-compatibility-audit.json','463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229'),
 'bridge_gap':(H/'33-12/j2-indlist-magma-picard-bridge-source-lock-gap.json','db9cd117556f7e63ede1256534ecd139b017089c938ab9c6d0f546f29ee82798'),
 'route':(H/'33-12/j2-marked-picard-bridge-retained-route-inventory.json','10106a86dc79aa491133cf877c21a37a546ea439c7c21b1bfa4ef5ea70b79fc9'),
 'receipt':(H/'33-12/qpic-bridge-local-recertification-receipt.json','c6e9466c509699b1ef2c037ad248915673d391f00115032782970667f44e7dd0'),
 'swap':(H/'33-12/j2-actual-swap-mixed-discriminant-descent.json','93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3'),
}
def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(k):
 p,h=LOCKS[k]; x=json.loads(p.read_text()); b=dict(x); got=b.pop('canonical_sha256'); assert got==h==csha(b),k; return x
c=json.loads((H/'controller.json').read_text()); x={k:load(k) for k in LOCKS}; s=c['stage33_12']; q=c['current']; receipt=x['receipt']; swap=x['swap']
assert c['schema']=='STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V54_QPIC_CERTIFIED_ACTUAL_SWAP_DESCENT'
assert c['stage33_progress']=='6/11' and q['unit']=='33-12' and q['logical_internal_branch']=='33-13_FINITE_V4_KUMMER_MATRIX_REPAIR'
assert q['substep']=='IDENTIFY_NAMED_J2_ORDER4_LIFT_WITH_ACTUAL_S3_ACTION'
assert q['active_missing_interface']=='NAMED_J2_ORDER4_LIFT_ACTUAL_S3_BEHAVIOR_OR_EQUIVALENT_SOURCE_LABEL_MISSING'
assert q['next_exact_leaf']==swap['next_exact_leaf']
assert s['actual_indlist_to_magma_picard_basis_bridge_materialized'] is True
assert s['source_authorized_qPic_bridge_requirement_satisfied'] is True
assert s['actual_indlist_to_magma_picard_basis_bridge_raw_sha256']==receipt['raw_bridge']['canonical_sha256']
assert s['actual_indlist_to_magma_picard_basis_bridge_certified_sha256']==receipt['certified_bridge']['canonical_sha256']
assert s['qpic_bridge_local_recertification_receipt_sha256']==LOCKS['receipt'][1]
assert s['actual_swap_mixed_discriminant_descent_certificate_sha256']==LOCKS['swap'][1]
assert s['actual_swap_mixed_discriminant_actions_materialized'] is True
assert s['corrected_J2_order4_affine_candidate_s3_action_materialized'] is True
assert s['corrected_J2_order4_unique_joint_s3_fixed_retained10_mask_decimal']==6
assert s['corrected_J2_order4_unique_joint_s3_fixed_proper14_mask_decimal']==25
assert s['historical_picard_adjoint_mask6_independently_rederived_as_unique_joint_s3_fixed_candidate'] is True
assert s['historical_picard_adjoint_authoritative_named_J2_source'] is False
assert s['historical_picard_adjoint_mask6_reused_as_named_J2_source'] is False
assert s['corrected_J2_order4_lift_actual_s3_behavior_source_locked'] is False
assert s['corrected_J2_proper_Br2_14D_coordinate_materialized'] is False
assert s['corrected_J2_retained_10D_domain_coordinate_materialized'] is False
assert s['corrected_J2_named_source_target_relation_materialized'] is False
assert s['finite_v4_kummer_columns_materialized']==0 and s['finite_v4_kummer_named_relation_rank_f2']==0
assert c['advance_scope']=='STAGE33_12_INTERNAL_33_13_NAMED_J2_ORDER4_LIFT_ACTUAL_S3_LABEL_ONLY_NO_PARENT_RECLOSURE'
assert c['next_item']=='Stage33-12_33-13_SOURCE_LOCK_NAMED_J2_ORDER4_LIFT_ACTUAL_S3_BEHAVIOR'
assert c['merge_allowed'] is False and c['theorem_credit'] is False and c['receiver_credit'] is False and c['endpoint_credit'] is False
assert x['orientation']['exact_conclusion']['named_CV_J2_fixed_marked_Kc_coordinate_f2']==[1,0]
assert x['target']['retained_H1_projection']['retained_H1_dimension_f2']==75
assert x['compat']['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert x['bridge_gap']['facts']['actual_64x64_bridge_source_locked'] is False
assert x['route']['conclusion']['source_authoritative_qPic_bridge_still_missing'] is True
assert swap['residual_order4_affine_candidate_S3_action']['unique_joint_fixed_retained10_mask_decimal']==6
assert swap['exact_consequence']['historical_mask6_reused_as_named_J2_source'] is False
out={
 'schema':'STAGE33_MAIN_COMPACT_STATE_V10_QPIC_CERTIFIED_ACTUAL_SWAP_DESCENT',
 'role':'ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE',
 'detailed_machine_authority':'stages/stage33/controller.json',
 'controller_schema':c['schema'],'stage33_progress':'6/11',
 'current':{k:q[k] for k in ['unit','logical_internal_branch','substep','active_missing_interface','next_exact_leaf']},
 'locked_facts':{
  'named_J2_semantic_orientation':{'label':'u1','marked_Kc_coordinate_f2':[1,0],'sha256':LOCKS['orientation'][1]},
  'proper_Br2_domain':{'ambient_dimension_f2':14,'retained_dimension_f2':10,'sha256':LOCKS['proper'][1]},
  'named_J2_raw_75D_target':{'nonzero':True,'weight':15,'sha256':LOCKS['target'][1]},
  'qpic_marked_picard_bridge':{'status':receipt['status'],'raw_bridge_sha256':receipt['raw_bridge']['canonical_sha256'],'certified_bridge_sha256':receipt['certified_bridge']['canonical_sha256'],'bridge_determinant':receipt['certified_bridge']['bridge_determinant'],'receipt_sha256':LOCKS['receipt'][1]},
  'actual_swap_mixed_discriminant_descent':{'status':swap['status'],'moduli':[2]*4+[4]*6+[8]*4,'s3_braid_exact':True,'semantic_u1_fixed_by_both_swaps':True,'candidate_count':4,'unique_joint_fixed_retained10_mask_decimal':6,'unique_joint_fixed_proper14_mask_decimal':25,'named_J2_source_selected':False,'sha256':LOCKS['swap'][1]},
  'historical_picard_adjoint_candidate':{'mask_decimal':6,'proper14_f2':s['historical_picard_adjoint_proper_Br2_14D_coordinate_f2'],'retained10_f2':s['historical_picard_adjoint_retained_10D_domain_coordinate_f2'],'authoritative_named_J2_source':False,'independently_rederived_as_unique_joint_s3_fixed_candidate':True,'sha256':LOCKS['adjoint'][1]},
  'compatibility_audit':{'historical_mask6_target_reachable':False,'reachable_H1_dimension_f2':13,'relation_rank_credit':0,'sha256':LOCKS['compat'][1]},
  'historical_qpic_gap':{'superseded_by_source_authorized_bridge':True,'sha256':LOCKS['bridge_gap'][1]},
  'historical_retained_smith_route':{'still_not_literal_qpic_marking':True,'superseded_as_current_blocker':True,'sha256':LOCKS['route'][1]},
 },
 'authority_changes':{
  'actual_INDLIST_to_historical_Magma_Picard_basis_bridge':'SOURCE_LOCKED_CERTIFIED_EXACT',
  'actual_swap12_swap13_on_mixed_discriminant_basis':'MATERIALIZED_EXACT',
  'historical_mask6':'INDEPENDENTLY_REDERIVED_UNIQUE_JOINT_S3_FIXED_CANDIDATE_NOT_NAMED_SOURCE',
  'J2_picard_adjoint_named_source_binding':'REVOKED_EXACT_DO_NOT_REVIVE_FROM_HISTORY',
  'J2_named_Kummer_source_target_relation':'REVOKED_EXACT_DO_NOT_USE',
  'named_J2_semantic_orientation':'RETAINED_EXACT_DO_NOT_REINVESTIGATE',
  'named_J2_raw_75D_target':'RETAINED_EXACT_INDEPENDENT_TARGET',
 },
 'do_not_use':['historical mask 6 as authoritative named J2 source without a new source-locked lift label','unique S3-fixed candidate implies named J2 unless named order-4 lift S3 behavior is proved','C2+C3=h_J2','mask 742 or 736 as J2 merely from compatibility','A_T[2] coefficients copied directly as proper-Br2 dual coefficients','nonunique retained-basis bridge witnesses instead of the certified literal qPic bridge','retained Smith V as the literal 64x64 qPic marking'],
 'open_datum':{'named_J2_order4_lift_actual_s3_behavior_source_locked':False,'named_J2_proper_Br2_source_coordinate_materialized':False,'retained10_named_J2_source_coordinate_materialized':False,'named_J2_source_target_relation_materialized':False,'named_source_target_relation_rank_f2':0,'matrix_standard_columns_materialized':0,'actual_indlist_to_magma_picard_basis_bridge_materialized':True,'actual_swap_mixed_discriminant_actions_materialized':True},
 'current_leaf_working_set':['stages/stage33/33-12/j2-actual-swap-mixed-discriminant-descent.json','stages/stage33/33-12/verify_j2_actual_swap_mixed_discriminant_descent.py','stages/stage33/33-12/qpic-bridge-local-recertification-receipt.json','stages/stage33/33-07/marked-picard-basis-bridge-certified.json','stages/stage33/33-12/j2-semantic-u1-full-surface-smith-source.json','stages/stage33/33-12/j2-marked-order4-lift-label-gap.json','stages/stage33/33-12/j2-marked-order4-geometric-sign-indistinguishability.json','stages/stage33/33-12/j2-cv-d2-semantic-orientation.json','stages/stage33/33-12/j2-order4-brauer-lift-reduction.json'],
 'anti_loop_reopen_policy':{'ordinary_main_rule':'The literal qPic bridge and actual mixed-discriminant S3 action are now exact. Do not reacquire the bridge, rerun Smith/symmetry substitutes, or select mask 6 merely because it is the unique S3-fixed candidate. Resolve the named J2 order-4 lift behavior under actual swaps or an equivalent source-locked label.','reopen_only_if':['the pinned upstream qPic/source lock changes','the certified bridge or mixed-discriminant swap certificate fails replay','a source-locked named J2 order-4 lift label or swap behavior becomes available','the user explicitly requests hostile audit or historical revalidation']},
 'execution_gate':{'audit_required':c['audit_required'],'audit_status':c['audit_status'],'last_completed_audit_scope':c['audit_scope'],'last_completed_audit_review_id':c['audit_review_id'],'last_completed_audit_head_sha':c['audit_head_sha'],'advance_allowed':c['advance_allowed'],'advance_scope':c['advance_scope'],'next_expected_command':c['next_expected_command']},
 'firewalls':{'stage33_12_closed_exact':False,'stage33_07_reclosed':False,'stage33_08_released':False,'theorem_credit':False,'receiver_credit':False,'endpoint_credit':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,'merge_allowed':False},
}
out['canonical_sha256']=csha(out); rendered=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args()
if a.check:
 assert OUT.exists() and OUT.read_text()==rendered,'MAIN-STATE.json is stale; run sync_main_state.py'
 print(json.dumps({'success':True,'mode':'check','canonical_sha256':out['canonical_sha256']},sort_keys=True))
else:
 OUT.write_text(rendered); print(json.dumps({'success':True,'mode':'write','canonical_sha256':out['canonical_sha256']},sort_keys=True))
