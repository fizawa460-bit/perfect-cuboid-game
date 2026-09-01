#!/usr/bin/env python3
"""Build/check the compact Stage33 MAIN state after the marked Picard bridge source-lock gap."""
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
 'bridge_gap':(HERE/'33-12'/'j2-indlist-magma-picard-bridge-source-lock-gap.json','85c3e0811bb9e9b5391772ae35e569f4aa0fd12940ca6c2db1b4be59b635ae2c'),
}
OUT=HERE/'MAIN-STATE.json'
def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected):
 x=json.loads(p.read_text(encoding='utf-8')); b=dict(x); h=b.pop('canonical_sha256')
 assert h==expected==csha(b),p
 return x

controller=json.loads(CONTROLLER.read_text(encoding='utf-8'))
x={k:load(*v) for k,v in FILES.items()}
stage=controller['stage33_12']; current=controller['current']
p=x['adjoint']['proper_brauer2_pullback']; h1=x['target']['retained_H1_projection']
assert controller['schema']=='STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V52_J2_KUMMER_BINDING_REPAIR'
assert controller['stage33_progress']=='6/11' and current['unit']=='33-12'
assert current['logical_internal_branch']=='33-13_FINITE_V4_KUMMER_MATRIX_REPAIR'
assert current['substep']=='REPAIR_J2_SOURCE_TARGET_KUMMER_MODULE_COMPATIBILITY'
assert current['active_missing_interface']=='MARKED_FULL_SURFACE_DISCRIMINANT_TO_PROPER_BR2_ADAPTER_NOT_SOURCE_LOCKED'
assert stage['minimal_missing_exact_datum']=='SOURCE_LOCKED_MARKED_FULL_SURFACE_DISCRIMINANT_TO_PROPER_BR2_ADAPTER_OR_EQUIVALENT_2x14_J2_PULLBACK'
assert stage['corrected_J2_named_source_target_relation_materialized'] is False
assert x['orientation']['exact_conclusion']['named_CV_J2_fixed_marked_Kc_coordinate_f2']==[1,0]
assert p['proper_Br2_14D_coordinate_f2']==[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert p['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert h1['retained_H1_dimension_f2']==75 and sum(h1['coordinates_f2'])==15
assert x['compat']['locked_named_j2']['locked_75D_target_reachable_from_locked_source'] is False
assert x['reopen']['status']=='PASS_EXACT_DIAGNOSTIC_PICARD_ADJOINT_NAMED_SOURCE_REOPENED'
assert x['gap']['status']=='PASS_EXACT_SOURCE_LOCK_GAP_MATERIALIZED'
bg=x['bridge_gap']
assert bg['status']=='PASS_EXACT_NONIDENTIFIABILITY_REQUIRES_SOURCE_AUTHORIZED_QPIC_BRIDGE'
assert bg['facts']['actual_64x64_bridge_source_locked'] is False
assert bg['facts']['retained_constraints_identify_unique_bridge'] is False
assert bg['facts']['nonunique_witness_count_materialized']==2
assert bg['facts']['induced_swap12_actions_differ'] is True
assert bg['credit']['main_progress_added'] is False
assert bg['stage33_progress']=='6/11'

out={
 'schema':'STAGE33_MAIN_COMPACT_STATE_V8_MARKED_PICARD_BRIDGE_SOURCE_GAP',
 'role':'ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE',
 'detailed_machine_authority':'stages/stage33/controller.json',
 'controller_schema':controller['schema'],
 'stage33_progress':controller['stage33_progress'],
 'current':{
  'unit':current['unit'],
  'logical_internal_branch':current['logical_internal_branch'],
  'substep':current['substep'],
  'active_missing_interface':'ACTUAL_INDLIST_TO_HISTORICAL_MAGMA_PICARD_BASIS_64x64_QPIC_BRIDGE_NOT_SOURCE_LOCKED',
  'next_exact_leaf':bg['next_exact_leaf'],
 },
 'locked_facts':{
  'named_J2_semantic_orientation':{'label':'u1','marked_Kc_coordinate_f2':[1,0],'sha256':FILES['orientation'][1]},
  'proper_Br2_domain':{'ambient_dimension_f2':14,'retained_dimension_f2':10,'sha256':FILES['proper'][1]},
  'named_J2_raw_75D_target':{'nonzero':True,'weight':15,'sha256':FILES['target'][1]},
  'historical_picard_adjoint_candidate':{'proper14_f2':p['proper_Br2_14D_coordinate_f2'],'retained10_f2':p['retained_10D_coordinate_f2'],'mask_decimal':6,'authoritative_named_J2_source':False,'sha256':FILES['adjoint'][1]},
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
 },
 'authority_changes':{
  'J2_picard_adjoint_named_source_binding':'REVOKED_EXACT_REPAIR_REQUIRED',
  'J2_picard_adjoint_source_coordinate':'REOPENED_EXACT_DO_NOT_USE_AS_NAMED_SOURCE',
  'J2_named_Kummer_source_target_relation':'REVOKED_EXACT_DO_NOT_USE',
  'named_J2_semantic_orientation':'RETAINED_EXACT_DO_NOT_REINVESTIGATE',
  'named_J2_raw_75D_target':'RETAINED_EXACT_INDEPENDENT_TARGET',
  'actual_INDLIST_to_historical_Magma_Picard_basis_bridge':'MISSING_SOURCE_LOCK_DO_NOT_INFER_FROM_RETAINED_SYMMETRIES',
 },
 'do_not_use':[
  'mask 6 as authoritative named J2 source','C2+C3=h_J2',
  'mask 742 or 736 as J2 merely from compatibility',
  'A_T[2] coefficients copied directly as proper-Br2 dual coefficients',
  'either nonunique bridge witness as the actual INDLIST-to-Magma Picard marking',
  'nonunique retained-basis swap transports as actual actions',
  '20 Kc preimsinPic rows as full-surface qPic bridge rows',
 ],
 'open_datum':{
  'named_J2_proper_Br2_source_coordinate_materialized':False,
  'marked_discriminant_proper_br2_adapter_materialized':False,
  'named_J2_source_target_relation_materialized':False,
  'named_source_target_relation_rank_f2':0,
  'matrix_standard_columns_materialized':0,
  'actual_indlist_to_magma_picard_basis_bridge_materialized':False,
 },
 'current_leaf_working_set':[
  'stages/stage33/33-12/j2-indlist-magma-picard-bridge-source-lock-gap.json',
  'stages/stage33/33-07/extract_indlist_to_magma_picard_basis.py',
  'stages/stage33/33-07/certify_marked_picard_basis_bridge.py',
  'stages/stage33/33-07/picard_base_rows_retained.py',
  'stages/stage33/33-07/picard_coordinate_sign_rows_retained.py',
  'stages/stage33/33-07/certify_actual_galois_at2_actions.py',
 ],
 'anti_loop_reopen_policy':{
  'ordinary_main_rule':'Exact non-identifiability is already materialized. Do not rerun retained-symmetry bridge searches; acquire the source-authorized qPic bridge (or an equivalent retained Smith composite) and certify it.',
  'reopen_only_if':[
   'the pinned upstream qPic/source lock changes',
   'the exact source-authorized bridge or equivalent retained Smith composite becomes available',
   'the user explicitly requests hostile audit or historical revalidation',
  ],
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
