#!/usr/bin/env python3
"""Verify Stage35-EX 35EX-32 promotion, breadth audit, historical no-recharge, and route-selection firewalls."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
AUDIT=ROOT/'stages/stage35-ex/35ex-32/post-population-equivalence-breadth-audit.json'

SCHEMA='STAGE35_EX_PESCH_E1_STATE_V31_POST_35EX32_ENDPOINT_POPULATION_BREADTH_AUDIT'
BASE_MAIN='a306fc15578bb7eac8d0fd43bbc6b7be9f9c3d33'
V30_COMMIT='8211bb0ef80de61ecf39c3b97743c58f1193187a'
FINAL_HEAD='9f1d3d73f41377bddb1296a3e6fc95b5e2fd8dd7'

def git_blob_sha(path:Path)->str:
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

state=json.loads(STATE.read_text())
audit=json.loads(AUDIT.read_text())

assert state['schema']==SCHEMA and state['stage']=='35-EX' and state['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert state['base_main_sha']==BASE_MAIN
hs=state['history_snapshot']
assert hs['commit_sha']==V30_COMMIT
assert hs['schema']=='STAGE35_EX_PESCH_E1_STATE_V30_POST_35EX31_PRIMITIVE_SOURCE_MARKING_ENDPOINT_EQUIVALENCE'
assert hs['role']=='IMMUTABLE_COMPLETE_V30_HISTORY_THROUGH_35EX31_PROVISIONAL'
assert hs['historical_replay_verifier']=='stages/stage35-ex/verify_stage35_ex_v31_legacy_replay.py'
assert hs['history_dropped'] is False

parent=state['parent_authority']
assert parent['unit']=='35EX-31'
assert parent['status']=='AUDITED_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_E1_CREDIT'
assert parent['hostile_audit_verdict']=='PASS_USER_APPROVED'
assert parent['initial_hostile_audit_review_id']==5120314137
assert parent['initial_hostile_audit_verdict']=='FAIL_FRESHNESS_ONLY_MATHEMATICS_PASS'
assert parent['final_exact_head_sha']==FINAL_HEAD
assert parent['final_exact_head_ci_run']==33953462420 and parent['final_exact_head_ci_job']==101272407623
assert parent['merged_main_sha']==V30_COMMIT
assert parent['audited_adapter_credit'] is True
assert parent['audited_population_equivalence_credit'] is True
assert parent['E1_theorem_credit'] is False

u31=state['completed_units_delta']['35EX-31']
assert u31['status']=='AUDITED_EXACT_PRIMITIVE_SOURCE_REVERSE_ADAPTER_ENDPOINT_EQUIVALENCE_NO_E1_CREDIT'
assert u31['primitive_source_reverse_adapter_audited'] is True
assert u31['E1_counterexample_rational_PC_population_equivalence_audited'] is True
assert u31['source_marking_reduces_unlabeled_endpoint_population'] is False

u32=state['completed_units_delta']['35EX-32']
assert u32['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert u32['artifact']==str(AUDIT.relative_to(ROOT))
assert u32['verifier']=='stages/stage35-ex/verify_stage35_ex_32.py'
assert u32['fresh_exhaustive_view_audit'] is True
assert u32['blind_rediscovery'] is True
assert u32['blind_generation_before_arsenal_comparison'] is True
assert u32['selected_candidate']=='E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT'
assert u32['selected_next_unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert u32['successor_selection_provisional_pending_hostile_audit'] is True

cur=state['current']
assert cur['unit']=='35EX-32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT'
assert cur['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert cur['candidate']=='E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT'
assert cur['next_if_audited_pass']=='START_35EX33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'

assert audit['schema']=='STAGE35_EX_32_POST_POPULATION_EQUIVALENCE_FRESH_BREADTH_AUDIT_V2'
assert audit['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
auth=audit['authority']
assert auth['initial_hostile_audit']['review_id']==5120314137
assert auth['initial_hostile_audit']['verdict']=='FAIL_FRESHNESS_ONLY'
assert auth['initial_hostile_audit']['mathematics_passed'] is True
assert auth['final_pass_source']=='USER_APPROVED_PASS_AFTER_FRESHNESS_REPAIR'
assert auth['final_exact_head_sha']==FINAL_HEAD
assert auth['final_exact_head_ci_run']==33953462420 and auth['final_exact_head_ci_job']==101272407623
assert auth['merged_main_sha']==V30_COMMIT

repair=audit['hostile_audit_repair']
assert repair['review_id']==5120424968
assert repair['failed_exact_head_sha']=='1729003067bd208fdcf64f7ed28d79b1e563643e'
assert repair['failure_class']=='HISTORICAL_NO_RECHARGE_COMPARISON_INCOMPLETE_NOT_FRESHNESS'
assert repair['blind_generation_repeated'] is False
assert repair['mathematics_changed'] is False

protocol=audit['protocol']
assert protocol['fresh_exhaustive_view_audit'] is True
assert protocol['blind_rediscovery'] is True
assert protocol['blind_generation_performed_before_arsenal_comparison'] is True
assert protocol['historical_comparison_performed_after_blind_generation'] is True
assert protocol['historical_block_ledger_gaussian_recheck_complete'] is True
assert protocol['split_triggered'] is False

for key,lock in audit['source_locks'].items():
    p=ROOT/lock['path']
    assert git_blob_sha(p)==lock['blob_sha'], (key,git_blob_sha(p),lock['blob_sha'])

expected_gaussian_locks={
    'stage35_ex_13_gaussian_orientation_coupling': '196d2be1bbfbcb2b416535d7bb051a9b2ec93104',
    'stage35_ex_17B_gaussian_coordinate_gcd_hook': '914c4143c41723ab30c6ad6379b7baccc39be23e',
    'stage35_ex_18_gaussian_relative_orientation_freeze': '9387364200169cacbfa5fe932df353aabe862351',
}
for key,sha in expected_gaussian_locks.items():
    assert audit['source_locks'][key]['blob_sha']==sha

receiver=audit['exact_receiver']
assert receiver['population']=='positive rational perfect cuboids modulo positive scaling and edge permutation'
assert receiver['equations']==[
    'p^2=1+x^2','q^2=1+y^2','z^2=x^2+y^2','w^2=1+x^2+y^2'
]
assert 'unique minimum-v2 edge' in receiver['canonical_2adic_fact']
assert 'may not be recharged' in receiver['forbidden_shortcut']

blind={x['id']:x for x in audit['blind_candidates']}
required={
 'E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT',
 'E1-ENDPOINT-UNIVERSAL-TORSOR-SQUARECLASS-SPLIT',
 'E1-ENDPOINT-JOINT-LOCAL-HILBERT-PROFILE',
 'E1-ENDPOINT-GENUINE-V2-INFINITE-DESCENT',
 'E1-LINKED-CONGRUENT-NUMBER-SELMER-COUPLING',
 'E1-RATIO-DISCRIMINANT-BIQUARTIC-QUOTIENT',
 'E1-UNIFORM-ENDPOINT-ELLIPTIC-SURFACE-HEIGHT',
 'E1-NONOBVIOUS-VERTICAL-BRAUER-ENDPOINT-FIBRATION',
 'E1-S3-SYMMETRIC-ENDPOINT-INVARIANTS',
 'E1-ENDPOINT-SPINOR-NORM-TERNARY-FORM',
}
assert required.issubset(blind)
assert blind['E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT']['classification_before_history']=='LIVE'
assert all(blind[k]['classification_before_history']=='UNTESTED' for k in required-{'E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT'})

hist=audit['historical_comparison']
for k in (
 'E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT',
 'E1-ENDPOINT-UNIVERSAL-TORSOR-SQUARECLASS-SPLIT',
 'E1-ENDPOINT-GENUINE-V2-INFINITE-DESCENT',
 'E1-LINKED-CONGRUENT-NUMBER-SELMER-COUPLING',
):
    assert k in hist
assert hist['E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT'].startswith('DISTINCT_PREFLIGHT_ROUTE_FROM_35EX13_17B_18')

ng=audit['historical_gaussian_no_recharge']
assert ng['overall_classification']=='DISTINCT_PREFLIGHT_ROUTE_NO_NEW_GAUSSIAN_CREDIT_YET'
assert ng['stage35_ex_13']['classification']=='DISTINCT_OBJECT_AND_TEST_SCOPE_NOT_RECHARGEABLE'
assert ng['stage35_ex_17B']['classification']=='DISTINCT_OBJECT_AND_SUPPORT_SCOPE_NOT_RECHARGEABLE'
assert ng['stage35_ex_18']['classification']=='DISTINCT_PREFLIGHT_BEYOND_FROZEN_ORIENTATION_QUESTION'
assert 'F_AB=A+iB' in ng['exact_new_test_not_previously_credited']
assert 'F_AC=A+iC' in ng['exact_new_test_not_previously_credited']
assert 'F_BC=B+iC' in ng['exact_new_test_not_previously_credited']
assert len(ng['forbidden_recharges'])==7
assert 'EQUIVALENT or BLOCKED' in ng['preflight_fail_close']

ars=audit['arsenal_comparison']
assert ars['matching_formal_gaussian_three_face_compatibility_card_found'] is False
assert ars['matching_formal_endpoint_universal_torsor_card_found'] is False
assert ars['matching_formal_linked_selmer_card_found'] is False
assert ars['matching_formal_genuine_v2_descent_card_found'] is False
assert ars['S34-W01']['classification']=='PARTIAL_ROUTER_FOR_UNIVERSAL_TORSOR_AND_GAUSSIAN_FACTOR_SUPPORT'
assert ars['S34-W03']['classification']=='DIRECT_ROUTER_FOR_JOINT_LOCAL_INTERSECTION'
assert ars['S31-W01']['classification']=='ADAPTER_ONLY_FOR_GENUS_ONE_QUARTIC_BRANCHES'
assert ars['S34-W02']['classification']=='LOCKED_UNTIL_FULL_MOVING_MW_INPUT_EXISTS'

sel=audit['selection']
assert sel['cycle_route_status']=='BLOCKED_NEW_PATTERN_ISOLATED'
assert sel['selected_candidate']=='E1-GAUSSIAN-THREE-FACE-COMPATIBILITY-DESCENT'
assert sel['selected_next_unit']=='35EX-33_GAUSSIAN_THREE_FACE_COMPATIBILITY_PREFLIGHT'
assert '35EX-13/17B/18' in sel['reason']
assert 'cannot be recharged' in sel['reason']
assert len(sel['next_unit_small_goals'])==5
assert '35EX-13/17B/18' in sel['next_unit_small_goals'][3]
assert 'EQUIVALENT/BLOCKED' in sel['next_unit_small_goals'][4]
assert sel['split_triggered'] is False
assert len(audit['preserved_untested_candidates'])==8
exit_=audit['cycle_exit']
assert exit_['CYCLE_EXHAUSTIVE_VIEW_AUDIT'] is True
assert exit_['CYCLE_BLIND_REDISCOVERY'] is True
assert exit_['CYCLE_SPLIT_TRIGGERED'] is False
assert exit_['CYCLE_LIVE_CANDIDATES']==1
assert exit_['CYCLE_UNTESTED_CANDIDATES']==8
assert exit_['CYCLE_NEW_VIEW_SOURCE']=='BLIND'

assert audit['claims']['historical_gaussian_no_recharge_comparison_complete'] is True
assert audit['claims']['old_gaussian_orientation_credit_recharged'] is False
claims=state['claims']
assert claims['audited_primitive_source_population_reverse_adapter'] is True
assert claims['audited_E1_endpoint_population_equivalence'] is True
for key in (
    'new_E1_theorem_credit','audited_35ex32_breadth_audit','gaussian_compatibility_theorem_proved',
    'E1_proved','R29_PESCH_E1_closed','R29_FIB2_closed','J12_PARAMETRIC_closed',
    'stage35_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim',
):
    assert claims[key] is False, key

print('PASS STAGE35_EX_32_POST_POPULATION_EQUIVALENCE_BREADTH_AUDIT_HISTORICAL_GAUSSIAN_REPAIRED')
