#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers through the exact V27 authority projection."""
from __future__ import annotations
import copy, json, runpy, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V28='STAGE35_EX_PESCH_E1_STATE_V28_POST_35EX29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION'
V27='STAGE35_EX_PESCH_E1_STATE_V27_POST_35EX28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION'
CURRENT_MAIN='5fa33e600b81fc34f4be9b22761c8079b31d7806'
V27_BASE='dc5898281a7ccea25d8ee0c1ae9953a18941ec08'
ALLOWED={'base', *{str(i) for i in range(10,29)}}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v28_legacy_replay.py {base|10|...|28}')
target=sys.argv[1]

real=json.loads(STATE.read_text())
assert real['schema']==V28 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==CURRENT_MAIN
parent=real['parent_authority']
assert parent['unit']=='35EX-28'
assert parent['status']=='AUDITED_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS'
assert parent['pass_source']=='HOSTILE_AUDIT_REVIEW_ON_PR1576'
assert parent['hostile_audit_review_node_id']=='PRR_kwDOTr52Y88AAAABMR185Q'
assert parent['audited_head_sha']=='908047d41b3f856cb5e6083793fb4815666b64b3'
assert parent['exact_head_ci_run']==33932898366 and parent['exact_head_ci_job']==101215004429
assert parent['merged_main_sha']=='0ebf2cfec83a39b016f61b996a0dd533d242de87'
assert parent['audited_theorem_credit'] is False
assert real['completed_units']['35EX-27B']['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-28']['status']=='AUDITED_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
assert real['completed_units']['35EX-28B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-29']['status']=='PROVISIONAL_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT'
assert real['current']['unit']=='35EX-29_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_OR_JOINT_LOCAL_FIREWALL'
assert real['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

projected=copy.deepcopy(real)
projected['schema']=V27
projected['base_main_sha']=V27_BASE
projected['parent_authority']={
    'unit':'35EX-27',
    'status':'AUDITED_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT',
    'hostile_audit_verdict':'PASS',
    'pass_source':'USER_CONFIRMED_HOSTILE_PASS',
    'audited_head_sha':'dc1930632304d2c47e5583e4d8cb324cbbd73e15',
    'exact_head_ci_run':33929237884,
    'exact_head_ci_job':101204270892,
    'merged_main_sha':'ee3e7aafd1742c5d96e2871f117412ef0823d57e',
    'audited_theorem_credit':False,
}

u27b=copy.deepcopy(projected['completed_units']['35EX-27B'])
u27b['status']='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','hostile_audit_review_node_id','audited_head_sha','exact_head_ci_run','exact_head_ci_job','merged_main_sha'):
    u27b.pop(key,None)
projected['completed_units']['35EX-27B']=u27b

u28=copy.deepcopy(projected['completed_units']['35EX-28'])
u28['status']='PROVISIONAL_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','hostile_audit_review_node_id','audited_head_sha','exact_head_ci_run','exact_head_ci_job','merged_main_sha'):
    u28.pop(key,None)
projected['completed_units']['35EX-28']=u28
projected['completed_units'].pop('35EX-28B',None)
projected['completed_units'].pop('35EX-29',None)

projected['resolved_investigations']['CURRENT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION']={
    'status':'PROVISIONAL_PASS_EXACT_K1_K4_COMPLETION_PENDING_HOSTILE_AUDIT',
    'reason':'the remaining quotient-base h-square is exactly K4, so K1--K4 are the complete rational-source Kummer receiver on the retained chamber; no joint-local exclusion is yet proved',
    'reopen_condition':'hostile audit may revoke this provisional gate; after PASS run a fresh breadth audit before selecting another successor',
}
projected['resolved_investigations'].pop('CURRENT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION',None)
projected.pop('candidate_ledger_after_35ex28_breadth_audit',None)

projected['current']={
    'unit':'35EX-28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_OR_JOINT_LOCAL_FIREWALL',
    'status':'PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT',
    'candidate':'E1-FULL-RATIONAL-SOURCE-KUMMER-COMPLETION',
    'result':'PASS_EXACT_K1_K4_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CLOSURE_PENDING_HOSTILE_AUDIT',
    'next_if_audited_pass':'FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION',
    'working_set':[
        'stages/stage35-ex/35ex-27/post-rational-source-kummer-breadth-audit.json',
        'stages/stage35-ex/35ex-28/full-rational-source-kummer-completion.md',
        'stages/stage35-ex/35ex-28/full-rational-source-kummer-certificate.json',
        'stages/stage35-ex/verify_stage35_ex_28.py',
        'docs/arsenal/cards/formal/S31-W01.md',
        'docs/arsenal/cards/formal/S34-W03.md',
        'stages/stage35-ex/MAIN-STATE.json',
    ],
}
projected['arsenal']={
    'S34_W01':'FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT',
    'S34_W03':'FULL_K1_K4_RATIONAL_SOURCE_RECEIVER_ROUTER_ONLY_INTERSECTION_NOT_CLOSED',
    'S31_W01':'PAIRED_FIXED_A_GENUS_ONE_BIRATIONAL_ROUTER_ONLY_MOVING_PARAMETER_NO_UNIFORM_CLOSURE',
    'S34_W02':'LOCKED_NO_GLOBAL_FINITE_REDUCTION_OR_UNIFORM_FULL_MW',
    'S30_W02':'ADJACENT_SEMILINEAR_DESCENT_PATTERN_ONLY_FINITE_ACTION_OBJECT_MISMATCH_NO_MATHEMATICAL_CREDIT',
    'S33_PW07':'PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR',
    'matching_global_reciprocity_Hilbert_Jacobi_card_found':False,
    'matching_formal_gaussian_coordinate_gcd_split_card_found':False,
    'matching_formal_nonisotrivial_surface_closure_card_found':False,
    'matching_formal_global_surface_classification_card_found':False,
    'matching_formal_global_surface_or_brauer_closure_card_found':False,
    'matching_formal_isogeny_twist_compression_card_found':False,
    'matching_formal_uniform_elliptic_surface_specialization_card_found':False,
    'matching_formal_uniform_moving_family_kummer_closure_card_found':False,
    'matching_formal_base_involution_receiver_descent_card_found':False,
    'matching_formal_rational_source_lift_kummer_card_found':False,
    'matching_formal_full_rational_source_kummer_completion_card_found':False,
    'S34_W03_simultaneous_kummer_router_after_dictionary':True,
    'S34_W03_single_elliptic_receiver_router_after_dictionary':True,
    'S34_W03_descended_receiver_router_after_dictionary':True,
    'S34_W03_rational_source_lift_router_after_dictionary':True,
    'S34_W03_full_K1_K4_router_after_dictionary':True,
    'stage34_concrete_coefficients_branches_and_local_primes_transfer':False,
}

original_read_text=Path.read_text
state_resolved=STATE.resolve()
def projected_read_text(self:Path,*args,**kwargs):
    if self.resolve()==state_resolved:
        return json.dumps(projected)
    return original_read_text(self,*args,**kwargs)
Path.read_text=projected_read_text
try:
    if target=='28':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_28.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v27_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v27_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V28_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}')
