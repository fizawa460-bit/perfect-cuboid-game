#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers through the exact V26 authority projection."""
from __future__ import annotations
import copy, json, runpy, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V27='STAGE35_EX_PESCH_E1_STATE_V27_POST_35EX28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION'
V26='STAGE35_EX_PESCH_E1_STATE_V26_POST_35EX27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM'
CURRENT_MAIN='dc5898281a7ccea25d8ee0c1ae9953a18941ec08'
V26_BASE='09d42186c06cd906042f2ca3f16a9deaf4f1b4a3'
ALLOWED={'base', *{str(i) for i in range(10,28)}}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v27_legacy_replay.py {base|10|...|27}')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V27 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==CURRENT_MAIN
parent=real['parent_authority']
assert parent['unit']=='35EX-27' and parent['status']=='AUDITED_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS' and parent['pass_source']=='USER_CONFIRMED_HOSTILE_PASS'
assert parent['audited_head_sha']=='dc1930632304d2c47e5583e4d8cb324cbbd73e15'
assert parent['exact_head_ci_run']==33929237884 and parent['exact_head_ci_job']==101204270892
assert parent['merged_main_sha']=='ee3e7aafd1742c5d96e2871f117412ef0823d57e' and parent['audited_theorem_credit'] is False
assert real['completed_units']['35EX-26B']['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-27']['status']=='AUDITED_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT'
assert real['completed_units']['35EX-27B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-28']['status']=='PROVISIONAL_EXACT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_NO_CREDIT'
assert real['current']['unit']=='35EX-28_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION_OR_JOINT_LOCAL_FIREWALL'
assert real['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

projected=copy.deepcopy(real)
projected['schema']=V26
projected['base_main_sha']=V26_BASE
projected['parent_authority']={
    'unit':'35EX-26',
    'status':'AUDITED_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT',
    'hostile_audit_verdict':'PASS',
    'pass_source':'USER_CONFIRMED_HOSTILE_PASS',
    'audited_head_sha':'d836c743628b47d62e4db18c344981be8fe839f4',
    'exact_head_ci_run':33926330680,
    'exact_head_ci_job':101195546705,
    'merged_main_sha':'74144644975d7800c6c5b529c5d8789f70366c2e',
    'audited_theorem_credit':False,
}
u26b=copy.deepcopy(projected['completed_units']['35EX-26B'])
u26b['status']='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','audited_head_sha','merged_main_sha'):
    u26b.pop(key,None)
projected['completed_units']['35EX-26B']=u26b
u27=copy.deepcopy(projected['completed_units']['35EX-27'])
u27['status']='PROVISIONAL_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','audited_head_sha','exact_head_ci_run','exact_head_ci_job','merged_main_sha'):
    u27.pop(key,None)
projected['completed_units']['35EX-27']=u27
projected['completed_units'].pop('35EX-27B',None)
projected['completed_units'].pop('35EX-28',None)
projected['resolved_investigations']['CURRENT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM']={
    'status':'PROVISIONAL_PASS_EXACT_RATIONAL_LIFT_AND_KUMMER_NORMAL_FORM_PENDING_HOSTILE_AUDIT',
    'reason':'rational source use of the fixed-field quotient requires k^2=u^2-4; with Q1--Q4 this becomes exact K1--K3 Kummer equations and a moving fixed-alpha genus-one quartic',
    'reopen_condition':'hostile audit may revoke this provisional gate; after PASS run a fresh breadth audit before selecting another successor',
}
projected['resolved_investigations'].pop('CURRENT_FULL_RATIONAL_SOURCE_KUMMER_COMPLETION',None)
projected.pop('candidate_ledger_after_35ex27_breadth_audit',None)
projected['current']={
    'unit':'35EX-27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_OR_DESCENDED_OVERCOVER_FIREWALL',
    'status':'PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT',
    'candidate':'E1-RATIONAL-SOURCE-LIFT-KUMMER-NORMAL-FORM',
    'result':'PASS_EXACT_RATIONAL_SOURCE_LIFT_AND_KUMMER_NORMAL_FORM_MOVING_GENUSONE_NO_CLOSURE_PENDING_HOSTILE_AUDIT',
    'next_if_audited_pass':'FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION',
    'working_set':[
        'stages/stage35-ex/35ex-26/post-base-involution-breadth-audit.json',
        'stages/stage35-ex/35ex-27/rational-source-lift-kummer-normal-form.md',
        'stages/stage35-ex/35ex-27/rational-source-lift-kummer-certificate.json',
        'stages/stage35-ex/verify_stage35_ex_27.py',
        'docs/arsenal/cards/formal/S31-W01.md',
        'docs/arsenal/cards/formal/S34-W03.md',
        'stages/stage35-ex/MAIN-STATE.json',
    ],
}
projected['arsenal']={
    'S34_W01':'FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT',
    'S34_W03':'RATIONAL_SOURCE_LIFT_KUMMER_RECEIVER_ROUTER_ONLY_INTERSECTION_NOT_CLOSED',
    'S31_W01':'FIXED_ALPHA_GENUS_ONE_BIRATIONAL_ROUTER_ONLY_MOVING_PARAMETER_NO_UNIFORM_CLOSURE',
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
    'S34_W03_simultaneous_kummer_router_after_dictionary':True,
    'S34_W03_single_elliptic_receiver_router_after_dictionary':True,
    'S34_W03_descended_receiver_router_after_dictionary':True,
    'S34_W03_rational_source_lift_router_after_dictionary':True,
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
    if target=='27':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_27.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v26_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v26_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V27_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}')
