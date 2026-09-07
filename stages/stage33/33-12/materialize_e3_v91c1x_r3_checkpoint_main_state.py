#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent; S33=HERE.parent
STATE=S33/'MAIN-STATE.json'
R2=HERE/'e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json'
R3=HERE/'e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json'
OLD_STATE_SHA='1a4ee3eeb74a74716d3ab0c6af2da6ee8135e50a32979797faf47cf98bd5f3b8'
R2_SHA='912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1'
R3_SHA='e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e'
CAND='V91C1X_R3_COVER_INDEXED_A2_02_REPRESENTATIVE_BOUNDED_PREFLIGHT'
NEXT='V91C1X_R4_CONSTRUCT_NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA'
MISSING='NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_OR_EQUIVALENT_GLUE_BUILT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA_WITH_EXPLICIT_SWAP23_COMMON_REFINEMENT'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(STATE,OLD_STATE_SHA); r2=load(R2,R2_SHA); r3=load(R3,R3_SHA)
 assert s['candidate_audit_gate']['candidate']=='V91C1X_R2_LITERAL_MU2_OR_UNIMODULAR_CECH_GLUE_CONSTRUCTION_CONTRACT'
 assert r2['next_exact_leaf'].startswith('V91C1X_R3_')
 assert r3['audit_checkpoint']['mathematically_substantial_checkpoint'] is True
 assert r3['exact_bounded_consequence']['repository_wide_absence_claim'] is False
 assert r3['exact_bounded_consequence']['route_mathematically_impossible'] is False
 assert r3['next_construction']['next_exact_leaf']==NEXT
 assert r3['next_construction']['missing_object']==MISSING

 s['schema']='STAGE33_MAIN_COMPACT_STATE_V51_V91C1X_R3_BOUNDED_H2_REPRESENTATIVE_PREFLIGHT_GROUPED_AUDIT_CHECKPOINT'
 s['authority_sync']['branch_candidate_frontier']=CAND
 s['authority_sync']['status']='V91C1V_HOSTILE_REAUDITED_MERGED_V91C1W_RETAINED_X_R1_NEGATIVE_X_R2_CONTRACT_X_R3_BOUNDED_PREFLIGHT_CHECKPOINT'
 s['branch_exact_frontier_candidate']='stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json'
 prior=s['candidate_audit_gate']; s['prior_x_r2_candidate_gate']=prior
 s['candidate_audit_gate']={
  'candidate':CAND,
  'candidate_certificate':'stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',
  'candidate_certificate_sha256':R3_SHA,
  'pr':1678,
  'status':'PENDING_GROUPED_HOSTILE_AUDIT_R1_R2_R3',
  'audit_pass_credit':False,
  'merge_allowed':False,
  'retained_v91c1w_sha256':'e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7',
  'r1_sha256':'b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb',
  'r2_sha256':R2_SHA,
  'hostile_audit_blocker_review':5127167940
 }
 s['continuation_provenance']['x_r3_bounded_locked_asset_preflight']={
  'pr':1678,'certificate_sha256':R3_SHA,
  'named_locked_assets_materialize_literal_mu2_2_cocycle':False,
  'named_locked_assets_materialize_equivalent_unimodular_glue':False,
  'named_locked_assets_materialize_swap23_common_refinement':False,
  'named_locked_assets_materialize_kummer_square_root_1_cochain':False,
  'triple_overlap_identity_verified':False,
  'repository_wide_absence_claim':False,
  'mathematical_nonexistence_claim':False,
  'next_missing_object':MISSING
 }
 s['continuation_provenance']['grouped_hostile_audit_policy']={
  'same_pr':1678,
  'user_authorized_same_pr_noncredit_accumulation':True,
  'current_stop_reason':'MATHEMATICALLY_SUBSTANTIAL_V91C1X_R1_R3_CHAIN_LEVEL_H2_REPRESENTATIVE_BLOCKER_CHECKPOINT',
  'hostile_audit_still_required_before_authority_credit_or_merge':True,
  'stop_when':['NEW_PROMOTION','MATHEMATICALLY_SUBSTANTIAL_CHECKPOINT']
 }
 s['current']={'active_missing_interface':MISSING,'logical_internal_branch':'33-13_FINITE_V4_KUMMER_MATRIX_REPAIR','next_exact_leaf':NEXT,'substep':'E3_V91C1X_R4_NEW_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_CONSTRUCTION','unit':'33-12'}
 f=s['current_exact_frontier']
 f['a2_02_r3_named_locked_asset_preflight_materialized']=True
 f['a2_02_current_named_locked_assets_materialize_accepted_literal_mu2_2_cocycle']=False
 f['a2_02_current_named_locked_assets_materialize_accepted_equivalent_unimodular_cech_glue']=False
 f['a2_02_current_named_locked_assets_materialize_swap23_common_refinement']=False
 f['a2_02_current_named_locked_assets_materialize_kummer_square_root_1_cochain']=False
 f['a2_02_triple_overlap_action_difference_identity_verified']=False
 f['a2_02_literal_mu2_2_cocycle_materialized']=False
 f['a2_02_equivalent_unimodular_cech_glue_materialized']=False
 f['a2_02_actual_swap23_gm_1_cochain_comparison_materialized']=False
 f['a2_02_semantic_action_difference_chain_witness_materialized']=False
 f['a2_02_swap23_seed_fixed_mod_pic2']=False
 f['a2_02_marked_brauer_image_excluded_from_mask20']=False
 f['a2_02_source_bound_stabilizer_fixed_subspace_materialized']=False
 f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_dimension_f2']=None
 f['a2_02_unknown_brauer_image_source_bound_stabilizer_fixed_subspace_cardinality']=None
 f['a2_02_minimal_source_bound_discriminator_positions_one_based']=[]
 s['current_leaf_working_set']=[
  'docs/research-os/policies/repository-asset-discovery.md','docs/arsenal/index.json',
  'docs/arsenal/cards/provisional/S33-PW04.md','docs/arsenal/cards/provisional/S33-PW07.md','docs/arsenal/cards/provisional/S33-PW08.md',
  'stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',
  'stages/stage33/33-12/e3-v91c1x-r2-literal-mu2-or-unimodular-cech-glue-contract.json',
  'stages/stage33/33-12/e3-v91c1x-r1-chain-level-action-difference-preflight.json',
  'stages/stage33/33-12/e3-v91c1d-a2-02-purity-cech-cartier-assembly.json',
  'stages/stage33/33-12/e3-v91c-type-safe-cech-adapter-interface.json',
  'stages/stage33/33-12/e3-direct-cech-seed-contract-v88.json',
  'stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json'
 ]
 s['locked_facts']['v91c1x_r3_bounded_preflight']={'sha256':R3_SHA}
 s['resolved_investigations']['e3_v91c1x_r3_cover_indexed_representative_bounded_preflight']='EXACT_NONCREDIT_NAMED_LOCKED_ASSETS_DO_NOT_MATERIALIZE_ACCEPTED_A2_02_H2_REPRESENTATIVE_OR_SWAP23_COMMON_REFINEMENT_NO_REPOSITORY_WIDE_ABSENCE_CLAIM'
 s['execution_gate']={'advance_allowed':False,'advance_scope':'GROUPED_HOSTILE_AUDIT_PR_1678_V91C1X_R1_R2_R3','next_expected_command':'HOSTILE_AUDIT_PR_1678_GROUPED_V91C1X_R1_R2_R3_EXACT_HEAD','stop_semantics':'USER_GROUPED_AUDIT_POLICY_SUBSTANTIAL_CHECKPOINT_NOT_ALGORITHM_EXHAUSTION'}
 s['work_checkpoint']={'authority':'V91C1V_HOSTILE_REAUDITED_MERGED','status':'V91C1X_R1_R3_CHAIN_LEVEL_H2_REPRESENTATIVE_BLOCKER_GROUPED_AUDIT_CHECKPOINT'}
 s['stage33_progress']='6/11'
 for k in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']: assert s['firewalls'][k] is False
 s.pop('canonical_sha256'); s['canonical_sha256']=csha(s)
 if a.write: STATE.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
 print(json.dumps({'success':True,'marker':'V113_MATERIALIZE_V91C1X_R3_GROUPED_AUDIT_CHECKPOINT','state_sha256':s['canonical_sha256'],'candidate_sha256':R3_SHA,'next_exact_leaf':NEXT,'next_expected_command':'HOSTILE_AUDIT_PR_1678_GROUPED_V91C1X_R1_R2_R3_EXACT_HEAD','stage33_progress':'6/11'},sort_keys=True))
if __name__=='__main__': main()
