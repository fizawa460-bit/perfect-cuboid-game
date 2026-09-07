#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
STATE=S33/'MAIN-STATE.json'
R3=HERE/'e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json'
OLD_STATE_SHA='bf00eda9927064a14562a91df106af999b292d42f6c2d5305225d8a6542a9528'
R3_SHA='e631d91eaa40a9f73b33e53ceff25745824f8ad6380d88d956424e29e9bd040e'
AUDITED_HEAD='cea554e0fc3cad4f745ed8c4a0582a34c54f1c98'
AUDIT_REVIEW_NODE='PRR_kwDOTr52Y88AAAABMZ653Q'
AUDIT_SUBMITTED_AT='2026-09-07T02:05:35Z'
MERGE_COMMIT='3dc69788084fd58960997959aedf04660c187078'
CAND='V91C1X_R3_COVER_INDEXED_A2_02_REPRESENTATIVE_BOUNDED_PREFLIGHT'
NEXT='V91C1X_R4_CONSTRUCT_NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA'
MISSING='NEW_SOURCE_BOUND_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_OR_EQUIVALENT_GLUE_BUILT_FROM_RETAINED_BOUNDARY_FUNCTION_AND_RESOLUTION_DATA_WITH_EXPLICIT_SWAP23_COMMON_REFINEMENT'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
    o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    s=load(STATE,OLD_STATE_SHA); r3=load(R3,R3_SHA)
    assert s['candidate_audit_gate']['candidate']==CAND
    assert s['candidate_audit_gate']['status']=='PENDING_GROUPED_HOSTILE_AUDIT_R1_R2_R3'
    assert s['execution_gate']['advance_allowed'] is False
    assert s['execution_gate']['next_expected_command']=='HOSTILE_AUDIT_PR_1678_GROUPED_V91C1X_R1_R2_R3_EXACT_HEAD'
    assert r3['audit_checkpoint']['mathematically_substantial_checkpoint'] is True
    assert r3['next_construction']['next_exact_leaf']==NEXT
    assert r3['next_construction']['missing_object']==MISSING

    s['schema']='STAGE33_MAIN_COMPACT_STATE_V52_V91C1X_R3_HOSTILE_AUDITED_MERGED_NONCREDIT_R4_CONSTRUCTION_ACTIVE'
    s['authority_sync']['branch_candidate_frontier']=CAND
    s['authority_sync']['status']='V91C1V_AUTHORITY_R3_GROUPED_HOSTILE_AUDITED_MERGED_NONCREDIT_R4_CONSTRUCTION_ACTIVE'
    s['candidate_audit_gate']={
      'candidate':CAND,
      'candidate_certificate':'stages/stage33/33-12/e3-v91c1x-r3-cover-indexed-a2-02-representative-bounded-preflight.json',
      'candidate_certificate_sha256':R3_SHA,
      'pr':1678,
      'status':'HOSTILE_AUDITED_MERGED_NONCREDIT_CHECKPOINT',
      'audit_pass_credit':True,
      'mathematical_authority_promoted':False,
      'hostile_audit_verdict':'PASS',
      'hostile_audit_review_node':AUDIT_REVIEW_NODE,
      'hostile_audit_submitted_at':AUDIT_SUBMITTED_AT,
      'exact_audited_head':AUDITED_HEAD,
      'merge_commit':MERGE_COMMIT,
      'merged':True,
      'merge_allowed':False,
      'retained_v91c1w_sha256':'e84dcc6692849ff065b0380e760bf725f77fff6754ab5bbdc39b7e608c76a4c7',
      'r1_sha256':'b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb',
      'r2_sha256':'912f00e0b680c39cdd0b99fb92174b5b45858dceeda4019799260869238766c1'
    }
    s['continuation_provenance']['x_r3_grouped_hostile_audit']={
      'pr':1678,'verdict':'PASS','review_node':AUDIT_REVIEW_NODE,'submitted_at':AUDIT_SUBMITTED_AT,
      'exact_audited_head':AUDITED_HEAD,'merge_commit':MERGE_COMMIT,'merged':True,
      'checkpoint_credit':'NONCREDIT_CONSTRUCTION_GATE_ONLY','authority_unchanged':True
    }
    s['continuation_provenance']['grouped_hostile_audit_policy']={
      'same_pr':1678,'r1_r2_r3_grouped_audit_complete':True,'hostile_audit_still_required_before_authority_credit_or_merge':False,
      'current_stop_reason':'AUDIT_GATE_CLEARED_R4_CONSTRUCTION_ALLOWED','stop_when':['NEW_PROMOTION','MATHEMATICALLY_SUBSTANTIAL_CHECKPOINT']
    }
    s['current']={'active_missing_interface':MISSING,'logical_internal_branch':'33-13_FINITE_V4_KUMMER_MATRIX_REPAIR','next_exact_leaf':NEXT,'substep':'E3_V91C1X_R4_NEW_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_CONSTRUCTION','unit':'33-12'}
    s['execution_gate']={'advance_allowed':True,'advance_scope':'V91C1X_R4_SOURCE_BOUND_COVER_INDEXED_A2_02_H2_REPRESENTATIVE_AND_SWAP23_COMMON_REFINEMENT_ONLY_NO_H2_FIXEDNESS_MASK20_OR_DIM5_CREDIT','next_expected_command':'STAGE33_MAIN_BATCH_V91C1X_R4_COVER_INDEXED_H2_REPRESENTATIVE','stop_semantics':'CONTINUE_ONLY_TO_NEW_SOURCE_BOUND_REPRESENTATIVE_OR_EXACT_CONSTRUCTION_BLOCKER'}
    s['work_checkpoint']={'authority':'V91C1V_HOSTILE_REAUDITED_MERGED','status':'V91C1X_R3_HOSTILE_AUDITED_MERGED_NONCREDIT_R4_CONSTRUCTION_ACTIVE'}
    s['stage33_progress']='6/11'
    for k in ['stage33_12_closed_exact','stage33_13_released','receiver_credit','theorem_credit','endpoint_credit','merge_allowed']:
        assert s['firewalls'][k] is False
    s.pop('canonical_sha256'); s['canonical_sha256']=csha(s)
    if a.write: STATE.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'success':True,'marker':'V114_R3_AUDIT_PASS_R4_CONSTRUCTION_GATE','state_sha256':s['canonical_sha256'],'authority_unchanged':True,'candidate_sha256':R3_SHA,'next_exact_leaf':NEXT,'stage33_progress':'6/11'},sort_keys=True))
if __name__=='__main__': main()
