#!/usr/bin/env python3
"""Replay historical Stage35-EX verifiers through the exact V25 authority projection."""
from __future__ import annotations
import copy, json, runpy, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
V26='STAGE35_EX_PESCH_E1_STATE_V26_POST_35EX27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM'
V25='STAGE35_EX_PESCH_E1_STATE_V25_POST_35EX26_BASE_INVOLUTION_RECEIVER_DESCENT'
CURRENT_MAIN='09d42186c06cd906042f2ca3f16a9deaf4f1b4a3'
V25_BASE='dca962cdf37d4252316885dc57f3c0a591db4ecb'
ALLOWED={'base', *{str(i) for i in range(10,27)}}
if len(sys.argv)!=2 or sys.argv[1] not in ALLOWED:
    raise SystemExit('usage: verify_stage35_ex_v26_legacy_replay.py {base|10|...|26}')
target=sys.argv[1]
real=json.loads(STATE.read_text())
assert real['schema']==V26 and real['stage']=='35-EX' and real['status']=='ACTIVE_RESEARCH_NO_CREDIT'
assert real['base_main_sha']==CURRENT_MAIN
parent=real['parent_authority']
assert parent['unit']=='35EX-26' and parent['status']=='AUDITED_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT'
assert parent['hostile_audit_verdict']=='PASS' and parent['pass_source']=='USER_CONFIRMED_HOSTILE_PASS'
assert parent['audited_head_sha']=='d836c743628b47d62e4db18c344981be8fe839f4'
assert parent['exact_head_ci_run']==33926330680 and parent['exact_head_ci_job']==101195546705
assert parent['merged_main_sha']=='74144644975d7800c6c5b529c5d8789f70366c2e' and parent['audited_theorem_credit'] is False
assert real['completed_units']['35EX-25B']['status']=='AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-26']['status']=='AUDITED_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT'
assert real['completed_units']['35EX-26B']['status']=='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
assert real['completed_units']['35EX-27']['status']=='PROVISIONAL_EXACT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_NO_CREDIT'
assert real['current']['unit']=='35EX-27_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM_OR_DESCENDED_OVERCOVER_FIREWALL'
assert real['current']['status']=='PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT'
assert real['claims']['E1_proved'] is False and real['claims']['stage35_closed'] is False

projected=copy.deepcopy(real)
projected['schema']=V25
projected['base_main_sha']=V25_BASE
projected['parent_authority']={
    'unit':'35EX-25',
    'status':'AUDITED_EXACT_SINGLE_ELLIPTIC_FULL_SQUARE_RECEIVER_NO_CREDIT',
    'hostile_audit_verdict':'PASS',
    'pass_source':'USER_CONFIRMED_AFTER_FRESHNESS_ONLY_REPAIR',
    'audited_head_sha':'7a2d70e04dcd679881630267cb2e1810f209e44c',
    'exact_head_ci_run':33922581520,
    'exact_head_ci_job':101183978655,
    'merged_main_sha':'3cadfd55d91f1e3267f31f9d7384b62d38678cc3',
    'audited_theorem_credit':False,
}
u25b=copy.deepcopy(projected['completed_units']['35EX-25B'])
u25b['status']='PROVISIONAL_FRESH_BREADTH_AUDIT_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','audited_head_sha','merged_main_sha'):
    u25b.pop(key,None)
projected['completed_units']['35EX-25B']=u25b
u26=copy.deepcopy(projected['completed_units']['35EX-26'])
u26['status']='PROVISIONAL_EXACT_BASE_INVOLUTION_RECEIVER_DESCENT_NO_CREDIT'
for key in ('hostile_audit_verdict','pass_source','audited_head_sha','exact_head_ci_run','exact_head_ci_job','merged_main_sha'):
    u26.pop(key,None)
projected['completed_units']['35EX-26']=u26
projected['completed_units'].pop('35EX-26B',None)
projected['completed_units'].pop('35EX-27',None)
projected['resolved_investigations']['CURRENT_BASE_INVOLUTION_RECEIVER_DESCENT']={
    'status':'PROVISIONAL_PASS_EXACT_RECIPROCAL_FIBER_QUOTIENT_NO_CLOSURE_PENDING_HOSTILE_AUDIT',
    'reason':'sigma:(x,p)->(1/x,p/x) acts on the full receiver, yielding K0=Q(u,h), h^2=u(u+2), and an exact descended receiver; quotient base dimension remains one and j(D_u) is nonconstant',
    'reopen_condition':'hostile audit may revoke the provisional descent; after PASS a fresh breadth audit is required before selecting the next arithmetic successor',
}
projected['resolved_investigations'].pop('CURRENT_RATIONAL_SOURCE_LIFT_KUMMER_NORMAL_FORM',None)
projected.pop('candidate_ledger_after_35ex26_breadth_audit',None)
projected['current']={
    'unit':'35EX-26_BASE_INVOLUTION_RECEIVER_DESCENT_OR_NO_REDUCTION_BLOCKER',
    'status':'PROVISIONAL_RESULT_PENDING_HOSTILE_AUDIT_NO_CREDIT',
    'candidate':'E1-BASE-INVOLUTION-A-INVERSE-DESCENT',
    'result':'PASS_EXACT_RECIPROCAL_FIBER_QUOTIENT_NO_ARITHMETIC_DIMENSION_DROP_PENDING_HOSTILE_AUDIT',
    'next_if_audited_pass':'FRESH_EXHAUSTIVE_VIEW_AUDIT_REQUIRED_BEFORE_SUCCESSOR_SELECTION',
    'working_set':[
        'stages/stage35-ex/35ex-25/post-single-elliptic-receiver-breadth-audit.json',
        'stages/stage35-ex/35ex-26/base-involution-receiver-descent.md',
        'stages/stage35-ex/35ex-26/base-involution-receiver-certificate.json',
        'stages/stage35-ex/verify_stage35_ex_26.py',
        'docs/arsenal/cards/formal/S30-W02.md',
        'docs/arsenal/cards/formal/S34-W03.md',
        'stages/stage35-ex/MAIN-STATE.json',
    ],
}
projected['arsenal']={
    'S34_W01':'FIXED_FIRST_SOURCE_ROUTING_MATCH_GLOBAL_FINITE_FAMILY_BLOCKED_DYNAMIC_UV_SUPPORT',
    'S34_W03':'DESCENDED_RECEIVER_INTERSECTION_ROUTER_ONLY_NOT_CLOSED',
    'S31_W01':'GENUS_ONE_CHARACTER_QUOTIENT_FIBERWISE_ROUTING_ONLY_NO_UNIFORM_SURFACE_CLOSURE',
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
    'S34_W03_simultaneous_kummer_router_after_dictionary':True,
    'S34_W03_single_elliptic_receiver_router_after_dictionary':True,
    'S34_W03_descended_receiver_router_after_dictionary':True,
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
    if target=='26':
        runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_26.py'),run_name='__main__')
    else:
        old_argv=sys.argv[:]
        try:
            sys.argv=['verify_stage35_ex_v25_legacy_replay.py',target]
            runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_v25_legacy_replay.py'),run_name='__main__')
        finally:
            sys.argv=old_argv
finally:
    Path.read_text=original_read_text
print(f'PASS V26_SUCCESSOR_PROJECTION_REPLAY_35EX_{target}')
