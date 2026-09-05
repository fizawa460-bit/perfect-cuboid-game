#!/usr/bin/env python3
"""Verify the user-approved merged 35EX-32 route-selection promotion without inventing hostile PASS credit."""
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
SCHEMA='STAGE35_EX_PESCH_E1_STATE_V32_POST_35EX32_USER_APPROVED_MERGE_ROUTE_SELECTION'
BASE_MAIN='3b4b5969330ae89a41899598fbdf17e76be76f72'
MERGE='3fbcecfb17c8eadde6479ee4c6f55c80be32cf42'
MERGE_BASE='bd402241fa69ea00d00b48695c883d1cbdbc2dbb'
FINAL_HEAD='eeae79b8678ab23d92b01d7f749025e164eeaf45'
V31='STAGE35_EX_PESCH_E1_STATE_V31_POST_35EX32_ENDPOINT_POPULATION_BREADTH_AUDIT'

state=json.loads(STATE.read_text())
assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==BASE_MAIN
hs=state['history_snapshot']
assert hs['commit_sha']==MERGE and hs['schema']==V31
assert hs['role']=='IMMUTABLE_COMPLETE_V31_HISTORY_THROUGH_35EX32_MERGED_PROVISIONAL'
assert hs['history_dropped'] is False

parent=state['parent_authority']
assert parent['unit']=='35EX-32'
assert parent['status']=='USER_APPROVED_MERGED_ROUTE_SELECTION_NO_THEOREM_CREDIT'
assert parent['merge_authorization']=='USER_DIRECT_MERGE_AFTER_REPEATED_FRESHNESS_ONLY_HOSTILE_FAILS'
assert parent['historical_repair_review_id']==5120424968
assert parent['freshness_only_review_ids']==[5120542777,5120615203]
assert parent['latest_hostile_review_id']==5120615203
assert parent['latest_hostile_verdict']=='FAIL_FRESHNESS_ONLY_MATHEMATICS_PASS'
assert parent['hostile_audit_pass'] is False
assert parent['final_exact_head_sha']==FINAL_HEAD
assert parent['final_exact_head_ci_run']==33956976310 and parent['final_exact_head_ci_job']==101281958689
assert parent['merged_main_sha']==MERGE
assert parent['mathematics_passed_by_latest_hostile_review'] is True
assert parent['historical_gaussian_no_recharge_passed'] is True
assert parent['selected_candidate_historical_classification']=='DISTINCT_PREFLIGHT_ROUTE_NO_NEW_GAUSSIAN_CREDIT_YET'
assert parent['route_selection_authorized_by_user_merge'] is True
assert parent['theorem_credit'] is False

u32=state['completed_units_delta']['35EX-32']
assert u32['status']=='USER_APPROVED_MERGED_ROUTE_SELECTION_NO_THEOREM_CREDIT'
assert u32['merge_sha']==MERGE
assert u32['latest_hostile_verdict']=='FAIL_FRESHNESS_ONLY_MATHEMATICS_PASS'
assert u32['user_approved_merge'] is True
assert u32['historical_gaussian_no_recharge_comparison_complete'] is True
assert u32['old_gaussian_orientation_credit_recharged'] is False
assert u32['selected_candidate_historical_classification']=='DISTINCT_PREFLIGHT_ROUTE_NO_NEW_GAUSSIAN_CREDIT_YET'
assert u32['selected_next_unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert u32['theorem_credit'] is False

cur=state['current']
assert cur['unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert len(cur['small_goals'])==5 if 'small_goals' in cur else cur['completed_small_goals']==[1,2,3,4,5]

snapshot_text=subprocess.check_output(
    ['git','show',f'{MERGE}:stages/stage35-ex/MAIN-STATE.json'],
    cwd=ROOT,text=True,stderr=subprocess.STDOUT,
)
snapshot=json.loads(snapshot_text)
assert snapshot['schema']==V31
assert snapshot['base_main_sha']==MERGE_BASE
assert snapshot['current']['unit']=='35EX-32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT'
assert snapshot['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert snapshot['claims']['audited_35ex32_breadth_audit'] is False

parents=subprocess.check_output(['git','rev-list','--parents','-n','1',MERGE],cwd=ROOT,text=True).strip().split()
assert parents[0]==MERGE and MERGE_BASE in parents[1:] and FINAL_HEAD in parents[1:]

claims=state['claims']
assert claims['35ex32_hostile_audit_pass'] is False
assert claims['35ex32_user_approved_merge'] is True
assert claims['35ex32_route_selection_authorized'] is True
assert claims['35ex32_theorem_credit'] is False
for key in ('gaussian_compatibility_theorem_proved','E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed','stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'):
    assert claims[key] is False, key

print('PASS STAGE35_EX_32_USER_APPROVED_MERGED_ROUTE_SELECTION_NO_HOSTILE_PASS_INVENTED')
