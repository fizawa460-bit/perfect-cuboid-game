#!/usr/bin/env python3
"""Build/check compact Stage33 MAIN state from the V9 qPic-bridge controller authority."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CONTROLLER=HERE/'controller.json'
FILES={
 'orientation':(HERE/'33-12'/'j2-cv-d2-semantic-orientation.json','0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e'),
 'proper':(HERE/'33-07'/'proper-brauer2-from-discriminant.json','c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf'),
 'target':(HERE/'33-12'/'j2-named-v4-h1-target-before-source-orientation.json','4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3'),
 'adjoint':(HERE/'33-12'/'j2-picard-adjoint-proper-br2.json','066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8'),
 'compat':(HERE/'33-12'/'j2-kummer-source-target-module-compatibility-audit.json','463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229'),
 'reopen':(HERE/'33-12'/'j2-picard-adjoint-reopen-diagnostic.json','1a20e001fd23b292881f9652818e52d5afc7f0bd43657809d5e52075ae6d1737'),
 'gap':(HERE/'33-12'/'j2-marked-discriminant-proper-br2-adapter-source-lock-gap.json','e27da962e6bd4330bd2e3ede77424bedb5ad40a684d81fadba632ac2fdef8b58'),
 'bridge_gap':(HERE/'33-12'/'j2-indlist-magma-picard-bridge-source-lock-gap.json','db9cd117556f7e63ede1256534ecd139b017089c938ab9c6d0f546f29ee82798'),
 'route':(HERE/'33-12'/'j2-marked-picard-bridge-retained-route-inventory.json','10106a86dc79aa491133cf877c21a37a546ea439c7c21b1bfa4ef5ea70b79fc9'),
}
OUT=HERE/'MAIN-STATE.json'
EXPECTED_CONTROLLER_SCHEMA='STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V53_QPIC_MARKED_BRIDGE_GAP'
EXPECTED_MISSING='SOURCE_AUTHORIZED_PINNED_UPSTREAM_QPIC_64x64_MARKED_PICARD_BRIDGE_MISSING'
EXPECTED_LEAF='ACQUIRE_SOURCE_AUTHORIZED_PINNED_UPSTREAM_QPIC_64x64_INDLIST_TO_MAGMA_PICARD_BRIDGE_THEN_CERTIFY_MARKING_DESCEND_ACTUAL_SWAPS_AND_TEST_ORDER4_AFFINE_SLICE'
EXPECTED_MINIMAL='SOURCE_AUTHORIZED_PINNED_UPSTREAM_QPIC_64x64_INDLIST_TO_MAGMA_PICARD_BRIDGE'
EXPECTED_AUDIT_SCOPE='STAGE33_12_V9_QPIC_BRIDGE_CONTROLLER_AUTHORITY_SYNC'
EXPECTED_AUDIT_REVIEW_ID=5080029385
EXPECTED_AUDIT_HEAD='8e61024cd12bcb55b3406701aea68f8bfbaa06a2'
EXPECTED_ADVANCE_SCOPE='STAGE33_12_INTERNAL_33_13_QPIC_MARKED_BRIDGE_ACQUISITION_ONLY_NO_PARENT_RECLOSURE'

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected):
 x=json.loads(p.read_text(encoding='utf-8')); b=dict(x); h=b.pop('canonical_sha256')
 assert h==expected==csha(b),p
 return x

controller=json.loads(CONTROLLER.read_text(encoding='utf-8'))
x={k:load(*v) for k,v in FILES.items()}
stage=controller['stage33_12']; current=controller['current']
p=x['adjoint']['proper_brauer2_pullback']; h1=x['target']['retained_H1_projection']
bg=x['bridge_gap']; route=x['route']

# Detailed controller is authoritative. Compact sync must reject semantic drift,
# not translate an obsolete controller into a newer compact state.
assert controller['schema']==EXPECTED_CONTROLLER_SCHEMA
assert controller['stage33_progress']=='6/11' and current['unit']=='33-12'
assert current['logical_internal_branch']=='33-13_FINITE_V4_KUMMER_MATRIX_REPAIR'
assert current['substep']=='REPAIR_J2_SOURCE_TARGET_KUMMER_MODULE_COMPATIBILITY'
assert current['active_missing_interface']==EXPECTED_MISSING
assert current['next_exact_leaf']==EXPECTED_LEAF==route['next_exact_leaf']
assert stage['minimal_missing_exact_datum']==EXPECTED_MINIMAL
assert stage['logical_internal_sequence'][0]['id']=='33-13'
assert stage['logical_internal_sequence'][0]['status']=='CURRENT_QPIC_MARKED_BRIDGE_SOURCE_GAP_RELATION_RANK_0_STANDARD_COLUMNS_0_OF_10'

# Reopened mask-6 Picard-adjoint data is historical diagnostic evidence only.
assert stage['corrected_J2_proper_Br2_14D_coordinate_materialized'] is False
assert stage['corrected_J2_retained_10D_domain_coordinate_materialized'] is False
assert stage['corrected_J2_proper_Br2_14D_coordinate_f2'] is None
assert stage['corrected_J2_retained_10D_domain_coordinate_f2'] is None
assert stage['historical_picard_adjoint_authoritative_named_J2_source'] is False
assert stage['historical_picard_adjoint_mask_decimal']==6
assert stage['historical_picard_adjoint_proper_Br2_14D_coordinate_f2']==p['proper_Br2_14D_coordinate_f2']==[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert stage['historical_picard_adjoint_retained_10D_domain_coordinate_f2']==p['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert stage['historical_picard_adjoint_proper_Br2_certificate_sha256']==FILES['adjoint'][1]
assert stage['corrected_J2_named_source_target_relation_materialized'] is False
assert stage['corrected_J2_named_standard_column_relation_valid'] is False
assert stage['finite_v4_kummer_named_relations_materialized']==0
assert stage['finite_v4_kummer_named_relation_rank_f2']==0

# qPic bridge gap and retained-route narrowing are detailed-controller facts.
assert stage['marked_picard_bridge_source_gap_certificate_sha256']==FILES['bridge_gap'][1]
assert stage['marked_picard_retained_route_inventory_sha256']==FILES['route'][1]
assert stage['actual_indlist_to_magma_picard_basis_bridge_materialized'] is False
assert stage['source_authorized_qPic_bridge_required'] is True
assert stage['retained_smith_route_authoritative_for_qPic_bridge'] is False
assert stage['new_external_magma_dispatch_authorized'] is False

# Hostile re-audit 5080029385 closes only the controller/V9 authority-sync gate.
# It authorizes MAIN to resume the qPic acquisition leaf, not merge/closure/credit
# and not a new external Magma dispatch.
assert controller['audit_required'] is False
assert controller['audit_status']=='PASS'
assert controller['audit_scope']==EXPECTED_AUDIT_SCOPE
assert controller['audit_review_id']==EXPECTED_AUDIT_REVIEW_ID
assert controller['audit_head_sha']==EXPECTED_AUDIT_HEAD
assert controller['advance_allowed'] is True
assert controller['advance_scope']==EXPECTED_ADVANCE_SCOPE
assert controller['next_item']=='Stage33-12_33-13_ACQUIRE_SOURCE_AUTHORIZED_QPIC_MARKED_BRIDGE'
assert controller['next_expected_command']=='Stage33-main-batch'
assert controller['execution']['audit_required'] is False
assert controller['execution']['audit_status']=='PASS'
assert controller['execution']['audit_scope']==EXPECTED_AUDIT_SCOPE
assert controller['execution']['audit_review_id']==EXPECTED_AUDIT_REVIEW_ID
assert controller['execution']['audit_head_sha']==EXPECTED_AUDIT_HEAD
assert controller['execution']['advance_allowed'] is True
assert controller['execution']['advance_scope']==EXPECTED_ADVANCE_SCOPE
assert controller['execution']['next_item']==controller['next_item']
assert controller['execution']['next_expected_command']==controller['next_expected_command']
assert controller['merge_allowed'] is False and controller['execution']['merge_allowed'] is False
assert controller['execution']['heavy_actions_authorized'] is False

assert x['orientation']['exact_conclusion']['named_CV_J2_fixed_marked_Kc_coordinate_f2']==[1,0]
assert h1['retained_H1_dimension_f2']==75 and sum(h1['coordinates_f2'])==15
assert x['compat']['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert x['reopen']['status']=='PASS_EXACT_DIAGNOSTIC_PICARD_ADJOINT_NAMED_SOURCE_REOPENED'
assert x['gap']['status']=='PASS_EXACT_SOURCE_LOCK_GAP_MATERIALIZED'
assert bg['status']=='PASS_EXACT_NONIDENTIFIABILITY_REQUIRES_SOURCE_AUTHORIZED_QPIC_BRIDGE'
assert bg['facts']['actual_64x64_bridge_source_locked'] is False
assert bg['facts']['retained_constraints_identify_unique_bridge'] is False
assert route['status']=='PASS_EXACT_RETAINED_SMITH_ROUTE_INSUFFICIENT_QPIC_BRIDGE_STILL_REQUIRED'
assert route['exact_findings']['retained_smith_V_exists'] is True
assert route['exact_findings']['retained_smith_V_identifies_indlist_to_historical_magma_picard_basis_64x64'] is False
assert route['conclusion']['equivalent_retained_smith_composite_found'] is False
assert route['conclusion']['source_authoritative_qPic_bridge_still_missing'] is True
assert route['conclusion']['new_external_magma_dispatch_authorized'] is False
assert route['credit']['main_progress_added'] is False

out={
 'schema':'STAGE33_MAIN_COMPACT_STATE_V9_QPIC_ONLY_MARKED_BRIDGE_ACQUISITION',
 'role':'ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE',
 'detailed_machine_authority':'stages/stage33/controller.json',
 'controller_schema':controller['schema'],
 'stage33_progress':controller['stage33_progress'],
 'current':{
  'unit':current['unit'],
  'logical_internal_branch':current['logical_internal_branch'],
  'substep':current['substep'],
  'active_missing_interface':current['active_missing_interface'],
  'next_exact_leaf':current['next_exact_leaf'],
 },
 'locked_facts':{
  'named_J2_semantic_orientation':{'label':'u1','marked_Kc_coordinate_f2':[1,0],'sha256':FILES['orientation'][1]},
  'proper_Br2_domain':{'ambient_dimension_f2':14,'retained_dimension_f2':10,'sha256':FILES['proper'][1]},
  'named_J2_raw_75D_target':{'nonzero':True,'weight':15,'sha256':FILES['target'][1]},
  'historical_picard_adjoint_candidate':{
   'proper14_f2':stage['historical_picard_adjoint_proper_Br2_14D_coordinate_f2'],
   'retained10_f2':stage['historical_picard_adjoint_retained_10D_domain_coordinate_f2'],
   'mask_decimal':stage['historical_picard_adjoint_mask_decimal'],
   'authoritative_named_J2_source':stage['historical_picard_adjoint_authoritative_named_J2_source'],
   'sha256':FILES['adjoint'][1],
  },
  'compatibility_audit':{'historical_mask6_target_reachable':False,'reachable_H1_dimension_f2':13,'relation_rank_credit':0,'sha256':FILES['compat'][1]},
  'reopen_diagnostic':{'status':x['reopen']['status'],'sha256':FILES['reopen'][1]},
  'marked_adapter_gap':{'status':x['gap']['status'],'accepted_shapes_f2':[[14,14],[2,14]],'sha256':FILES['gap'][1]},
  'marked_picard_bridge_source_gap':{
   'status':bg['status'],
   'retained_constraints_identify_unique_bridge':False,
   'nonunique_witness_count_materialized':2,
   'induced_swap12_actions_differ':True,
   'actual_64x64_bridge_source_locked':False,
   'sha256':FILES['bridge_gap'][1],
  },
  'marked_picard_retained_route_inventory':{
   'status':route['status'],
   'retained_smith_V_exists':True,
   'retained_smith_V_identifies_64x64_marking':False,
   'source_authoritative_qPic_bridge_still_missing':True,
   'sha256':FILES['route'][1],
  },
 },
 'authority_changes':{
  'J2_picard_adjoint_named_source_binding':'REVOKED_EXACT_REPAIR_REQUIRED',
  'J2_picard_adjoint_source_coordinate':'REOPENED_EXACT_DO_NOT_USE_AS_NAMED_SOURCE',
  'J2_named_Kummer_source_target_relation':'REVOKED_EXACT_DO_NOT_USE',
  'named_J2_semantic_orientation':'RETAINED_EXACT_DO_NOT_REINVESTIGATE',
  'named_J2_raw_75D_target':'RETAINED_EXACT_INDEPENDENT_TARGET',
  'actual_INDLIST_to_historical_Magma_Picard_basis_bridge':'MISSING_SOURCE_LOCK_DO_NOT_INFER_FROM_RETAINED_SYMMETRIES',
  'retained_common_Smith_route_for_literal_64x64_marking':'AUDITED_INSUFFICIENT_DO_NOT_USE_AS_QPIC_BRIDGE',
 },
 'do_not_use':[
  'mask 6 as authoritative named J2 source','C2+C3=h_J2',
  'mask 742 or 736 as J2 merely from compatibility',
  'A_T[2] coefficients copied directly as proper-Br2 dual coefficients',
  'either nonunique bridge witness as the actual INDLIST-to-Magma Picard marking',
  'nonunique retained-basis swap transports as actual actions',
  '20 Kc preimsinPic rows as full-surface qPic bridge rows',
  'retained Smith V or common-Smith transport as the literal 64x64 INDLIST-to-Magma Picard marking',
 ],
 'open_datum':{
  'named_J2_proper_Br2_source_coordinate_materialized':False,
  'marked_discriminant_proper_br2_adapter_materialized':False,
  'named_J2_source_target_relation_materialized':False,
  'named_source_target_relation_rank_f2':0,
  'matrix_standard_columns_materialized':0,
  'actual_indlist_to_magma_picard_basis_bridge_materialized':stage['actual_indlist_to_magma_picard_basis_bridge_materialized'],
 },
 'current_leaf_working_set':[
  'stages/stage33/33-12/j2-marked-picard-bridge-retained-route-inventory.json',
  'stages/stage33/33-12/j2-indlist-magma-picard-bridge-source-lock-gap.json',
  'stages/stage33/33-07/extract_indlist_to_magma_picard_basis.py',
  'stages/stage33/33-07/certify_marked_picard_basis_bridge.py',
  'stages/stage33/33-07/stoll_cuboid_source.py',
  'stages/stage33/33-12/j2-semantic-u1-full-surface-smith-source.json',
 ],
 'anti_loop_reopen_policy':{
  'ordinary_main_rule':'The retained Smith route is already audited and insufficient for the literal 64x64 marking. Do not rerun symmetry/isometry/Smith substitutes; acquire the source-authorized pinned-upstream qPic bridge and certify it.',
  'reopen_only_if':[
   'the pinned upstream qPic/source lock changes',
   'the exact source-authorized qPic bridge becomes available',
   'the user explicitly requests hostile audit or historical revalidation',
  ],
 },
 'execution_gate':{
  'audit_required':controller['audit_required'],
  'audit_status':controller['audit_status'],
  'audit_scope':controller['audit_scope'],
  'audit_review_id':controller['audit_review_id'],
  'audit_head_sha':controller['audit_head_sha'],
  'advance_allowed':controller['advance_allowed'],
  'advance_scope':controller['advance_scope'],
  'next_expected_command':controller['next_expected_command'],
 },
 'firewalls':{
  'stage33_12_closed_exact':stage['closed_exact'],
  'stage33_07_reclosed':controller['release_gates']['stage33_07_reclosed'],
  'stage33_08_released':controller['release_gates']['stage33_08_released'],
  'theorem_credit':controller['theorem_credit'],
  'receiver_credit':controller['receiver_credit'],
  'endpoint_credit':controller['endpoint_credit'],
  'perfect_cuboid_existence_claim':controller['perfect_cuboid_existence_claim'],
  'perfect_cuboid_nonexistence_claim':controller['perfect_cuboid_nonexistence_claim'],
  'merge_allowed':controller['merge_allowed'],
 },
}
out['canonical_sha256']=csha(out)
rendered=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n'
parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
if args.check:
 assert OUT.exists() and OUT.read_text(encoding='utf-8')==rendered,'MAIN-STATE.json is stale; run sync_main_state.py'
 print(json.dumps({'success':True,'mode':'check','canonical_sha256':out['canonical_sha256']},sort_keys=True))
else:
 OUT.write_text(rendered,encoding='utf-8')
 print(json.dumps({'success':True,'mode':'write','canonical_sha256':out['canonical_sha256']},sort_keys=True))
