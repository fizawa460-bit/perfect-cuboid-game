#!/usr/bin/env python3
"""Verify 35EX-34 post-Gaussian blind breadth audit and route selection."""
from __future__ import annotations
import hashlib, json, subprocess
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
BLIND=ROOT/'stages/stage35-ex/35ex-34/blind-post-gaussian-block-candidate-generation.json'
AUDIT=ROOT/'stages/stage35-ex/35ex-34/post-gaussian-block-exhaustive-view-audit.json'
SCHEMA='STAGE35_EX_PESCH_E1_STATE_V33_POST_35EX33_HOSTILE_AUDITED_ROUTE_BLOCKER'
BASE_MAIN='9309801b9caffa857adc5599ad5dd686d84d47d8'
PARENT_MERGE='e21378e59f7f1076a7ad71d34cee1fd0ac3a5cb3'
PARENT_HOSTILE_REVIEW=5120722298
BLIND_COMMIT='f80d0321549d120a6f4d8a0713ec1100fc4ca6e5'
AUDIT_COMMIT='e073c322d52122de10791bb8174c62bd696bf037'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
blind=json.loads(BLIND.read_text())
audit=json.loads(AUDIT.read_text())
assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==BASE_MAIN
assert state['history_snapshot']['commit_sha']==PARENT_MERGE
assert blind['schema']=='STAGE35_EX_34_BLIND_POST_GAUSSIAN_BLOCK_CANDIDATES_V1'
assert blind['phase']=='BLIND_REDISCOVERY_BEFORE_ARSENAL_OR_HISTORY_COMPARISON'
assert blind['credit_firewall']['blind_pass_completed'] is True
assert blind['credit_firewall']['arsenal_consulted_for_generation'] is False
assert blind['credit_firewall']['history_consulted_for_generation'] is False
assert len(blind['blind_candidates'])==10
assert blind['blind_selection']['candidate']=='B34-01_PRIVATE_EDGE_GCD_TORSOR_DECOMPOSITION'
assert blind['blind_selection']['selection_is_final_before_history_comparison'] is False

assert audit['schema']=='STAGE35_EX_34_POST_GAUSSIAN_BLOCK_EXHAUSTIVE_VIEW_AUDIT_V1'
assert audit['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_SELECT_PRIVATE_GCD_PREFLIGHT_NO_E1_CREDIT'
parent=audit['parent_35ex33']
assert parent['pr']==1598 and parent['pass_source']=='HOSTILE_AUDIT_PASS'
assert parent['hostile_review_id']==PARENT_HOSTILE_REVIEW
assert parent['exact_head_sha']=='2fa20cabe38bd4003187757921389f9623e6e260'
assert parent['exact_head_ci_run']==33958273867 and parent['exact_head_ci_job']==101285448666
assert parent['merge_sha']==PARENT_MERGE
assert parent['audited_route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
assert parent['E1_credit'] is False

for key,lock in audit['source_locks'].items():
    p=ROOT/lock['path']
    actual=git_blob_sha(p)
    assert actual==lock['blob_sha'], (key,actual,lock['blob_sha'])

subprocess.run(['git','merge-base','--is-ancestor',BLIND_COMMIT,AUDIT_COMMIT],cwd=ROOT,check=True)
assert audit['protocol_order']['blind_generation_committed_before_history_and_arsenal_comparison'] is True
assert audit['protocol_order']['blind_generation_commit']==BLIND_COMMIT
assert audit['protocol_order']['blind_pass_completed'] is True
assert audit['protocol_order']['history_comparison_completed_after_blind_pass'] is True
assert audit['protocol_order']['arsenal_comparison_completed_after_blind_pass'] is True

classes={row['blind_id']:row for row in audit['candidate_classification']}
assert set(classes)=={f'B34-{i:02d}' for i in range(1,11)}
expected_hist={
'B34-01':'E1-ENDPOINT-UNIVERSAL-TORSOR-SQUARECLASS-SPLIT',
'B34-02':'E1-ENDPOINT-JOINT-LOCAL-HILBERT-PROFILE',
'B34-03':'E1-ENDPOINT-GENUINE-V2-INFINITE-DESCENT',
'B34-04':'E1-LINKED-CONGRUENT-NUMBER-SELMER-COUPLING',
'B34-05':'E1-RATIO-DISCRIMINANT-BIQUARTIC-QUOTIENT',
'B34-06':'E1-UNIFORM-ENDPOINT-ELLIPTIC-SURFACE-HEIGHT',
'B34-07':'E1-NONOBVIOUS-VERTICAL-BRAUER-ENDPOINT-FIBRATION',
'B34-08':'E1-ENDPOINT-SPINOR-NORM-TERNARY-FORM',
'B34-09':'E1-S3-SYMMETRIC-ENDPOINT-INVARIANTS_WITHOUT_STRICT_ARITHMETIC_REDUCTION',
'B34-10':None,
}
for k,v in expected_hist.items(): assert classes[k]['historical_match']==v
assert classes['B34-01']['classification']=='LIVE'
for k in [f'B34-{i:02d}' for i in range(2,9)]+['B34-10']:
    assert classes[k]['classification']=='UNTESTED', k
assert classes['B34-09']['classification']=='BLOCKED'
assert 'already quotiented by edge permutation' in classes['B34-09']['exact_blocker']
assert 'strictly decreasing invariant' in classes['B34-10']['relation_to_35EX31']

sel=audit['selected_route']
assert sel['blind_id']=='B34-01'
assert sel['historical_route']=='E1-ENDPOINT-UNIVERSAL-TORSOR-SQUARECLASS-SPLIT'
assert sel['operational_name']=='PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_PREFLIGHT'
assert sel['universal_torsor_claimed'] is False
assert sel['new_squareclass_theorem_claimed'] is False
assert len(audit['selected_next_small_goals'])==5
assert len(audit['mandatory_lens_completion'])==2
assert audit['mandatory_lens_completion'][0]['classification']=='BLOCKED_FOR_CURRENT_EXACT_THEOREM_TARGET'
assert audit['mandatory_lens_completion'][1]['classification']=='BLOCKED'

exit_=audit['cycle_exit']
assert exit_['CYCLE_ROUTE_STATUS']=='PASS_NEW_GATE_FROM_STRONGER_VIEW'
assert exit_['CYCLE_LIVE_CANDIDATES']==1
assert exit_['CYCLE_UNTESTED_CANDIDATES']==8
assert exit_['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is True
assert exit_['CYCLE_BLIND_REDISCOVERY'] is True
assert exit_['CYCLE_SPLIT_TRIGGERED'] is False
assert exit_['CYCLE_NEW_VIEW_SOURCE']=='BLIND'

pa=state['parent_authority']
assert pa['unit']=='35EX-33' and pa['audit_verdict']=='HOSTILE_AUDIT_PASS'
assert pa['pass_source']=='HOSTILE_AUDIT_REVIEW'
assert pa['hostile_review_id']==PARENT_HOSTILE_REVIEW
assert pa['exact_head_sha']==parent['exact_head_sha'] and pa['merged_main_sha']==PARENT_MERGE
assert pa['route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
u33=state['completed_units_delta']['35EX-33']
assert u33['audit_verdict']=='HOSTILE_AUDIT_PASS' and u33['hostile_review_id']==PARENT_HOSTILE_REVIEW
u34=state['completed_units_delta']['35EX-34']
assert u34['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert u34['blind_rediscovery'] is True and u34['exhaustive_view_audit'] is True
assert u34['blind_before_history_and_arsenal'] is True
assert u34['selected_blind_candidate']=='B34-01'
assert u34['universal_torsor_constructed'] is False
assert u34['live_candidates']==1 and u34['untested_candidates']==8
cur=state['current']
assert cur['unit']=='35EX-34_POST_GAUSSIAN_BLOCK_FRESH_BREADTH_AUDIT'
assert cur['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT'
assert cur['next_if_hostile_audit_pass']=='START_35EX35_PRIVATE_EDGE_GCD_SIX_VARIABLE_DECOMPOSITION_PREFLIGHT'
assert state['candidate_ledger']['live']==['E1-ENDPOINT-UNIVERSAL-TORSOR-SQUARECLASS-SPLIT']
assert state['candidate_ledger']['untested_count']==8
assert state['candidate_ledger']['split_triggered'] is False

for A in range(1,18):
  for B in range(1,18):
    for C in range(1,18):
      if gcd(gcd(A,B),C)!=1: continue
      x,y,z=gcd(A,B),gcd(A,C),gcd(B,C)
      assert gcd(x,y)==gcd(x,z)==gcd(y,z)==1
      assert A%(x*y)==0 and B%(x*z)==0 and C%(y*z)==0
      a,b,c=A//(x*y),B//(x*z),C//(y*z)
      assert (A,B,C)==(x*y*a,x*z*b,y*z*c)
      assert gcd(y*a,z*b)==1
      assert gcd(x*a,z*c)==1
      assert gcd(x*b,y*c)==1

cf=audit['credit_firewall']
assert cf['audited_35ex33_route_blocker_recorded'] is True
for key in ('selected_private_gcd_route_theorem_credit','universal_torsor_constructed','finite_squareclass_receiver_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert cf[key] is False, key
claims=state['claims']
assert claims['35ex33_hostile_audit_pass'] is True
assert claims['35ex33_hostile_review_id']==PARENT_HOSTILE_REVIEW
for key in ('universal_torsor_constructed','finite_squareclass_receiver_obtained','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert claims[key] is False, key

print('PASS STAGE35_EX_34_POST_GAUSSIAN_BLOCK_FRESH_BREADTH_AUDIT')
