#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=ROOT/'stages/stage35-ex'
ART=HERE/'35ex-35/goal4ag-bounded-principalization-degree-exclusion.json'
LOCK=HERE/'35ex-35/goal4ag-bounded-principalization-degree-exclusion-source-lock.md'
SNAP=HERE/'snapshots/MAIN-STATE-V69-8bed9082aeeb.json'
DIAG=HERE/'diagnose_stage35_ex_35_goal4ag_fixed_component_strip.py'
RUNKEY=HERE/'runkeys/goal4ag-fixed-strip.json'
STATE=HERE/'MAIN-STATE.json'

EXPECTED_ART_BLOB='15245f0f300a60494afd424363e68a296a80c337'
EXPECTED_LOCK_BLOB='4f959830e54e7829d61de70d3990e776bbef55f4'
EXPECTED_SNAP_BLOB='86318a71af1f9dfe7f97132f0b2e2b19a189f302'
EXPECTED_DIAG_BLOB='8a3dbd418d650f6d5454482678aa91e6d6e62fe1'
EXPECTED_CANON='9db1f8abc453d50f6849af1236c89e9bf0db5ffbfd26199853ebe43a9f157f45'
V70='STAGE35_EX_PESCH_E1_STATE_V70_GOAL4AG_HOMOGENEOUS_DEGREE25_TO30_PRINCIPALIZATION_EXCLUDED_DEGREE31_SURVIVES_RETAINED_CURVE_TEST_PENDING_AUDIT'


def git_blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def csha(o:object)->str:
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

assert git_blob(ART)==EXPECTED_ART_BLOB
assert git_blob(LOCK)==EXPECTED_LOCK_BLOB
assert git_blob(SNAP)==EXPECTED_SNAP_BLOB
assert git_blob(DIAG)==EXPECTED_DIAG_BLOB
rk=json.loads(RUNKEY.read_text())
assert rk['schema']=='STAGE35_EX_GOAL4AG_FIXED_STRIP_RUNKEY_V1'
assert rk['armed'] is True and rk['generation']==2
assert rk['diagnostic_blob_sha1']==EXPECTED_DIAG_BLOB

art=json.loads(ART.read_text()); canon=art.pop('canonical_sha256')
assert canon==EXPECTED_CANON==csha(art)
assert art['schema']=='STAGE35_EX_35_GOAL4AG_BOUNDED_PRINCIPALIZATION_DEGREE_EXCLUSION_V1'
assert art['parent']['source_head_sha']=='8bed9082aeeb893b3c34c5fc0da4103415d215f1'
assert art['exact_runs']['degree25_residual']=={'head_sha':'8bed9082aeeb893b3c34c5fc0da4103415d215f1','workflow_run':34076057541,'job':101602278476,'conclusion':'SUCCESS'}
fs=art['exact_runs']['fixed_component_strip']
assert fs=={'head_sha':'8bed9082aeeb893b3c34c5fc0da4103415d215f1','workflow_run':34076057633,'job':101602278686,'conclusion':'SUCCESS','generation':2,'diagnostic_blob_sha1':EXPECTED_DIAG_BLOB}
pt=art['principalization_target']
assert pt=={'formal_target_support_count':69,'positive_hyperplane_degree':396,'negative_hyperplane_degree':396,'surface_hyperplane_square':16,'homogeneous_ratio_degree_lower_bound':25}
be=art['bounded_exclusion']
assert be['tested_degree_range']==[25,128]
assert be['proved_noneffective_degrees']==[25,26,27,28,29,30]
assert be['contiguous_noneffective_through']==30
assert be['first_surviving_degree']==31
assert be['first_survivor_status']=='SURVIVES_NEF_AGAINST_RETAINED_CURVES'
assert be['degree31_final_hyperplane_degree']==96 and be['degree31_final_square']==212
assert be['degree31_effectivity_proved'] is False and be['degree31_principal_function_materialized'] is False
rr=art['route_result']
assert rr['goal4ag_executed'] is True and rr['bounded_homogeneous_degree_exclusion_obtained'] is True
assert rr['general_qi_principal_function_problem']=='OPEN'
assert rr['next']=='35EX-35_GOAL4AH_SECOND_CLASS_QI_CYCLIC_DEGREE31_SURVIVOR_EFFECTIVITY_AND_PRINCIPAL_FUNCTION_SYNTHESIS_PREFLIGHT'
for k,v in art['credit_firewall'].items():
    assert v is False,k

st=json.loads(STATE.read_text())
assert st['schema']==V70
assert st['current']['unit']==art['unit']
assert st['current']['next']==rr['next']
assert st['claims']['goal4ag_executed'] is True
assert st['claims']['open_receiver_second_class_homogeneous_degree_lower_bound']==25
assert st['claims']['open_receiver_second_class_noneffective_through_degree']==30
assert st['claims']['open_receiver_second_class_first_retained_curve_survivor_degree']==31
assert st['claims']['open_receiver_second_class_degree31_effectivity_proved'] is False
assert st['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert st['claims']['open_receiver_second_class_global_F_B_nonexistence_proved'] is False
assert st['claims']['E1_proved'] is False and st['claims']['stage35_closed'] is False
print(json.dumps({'success':True,'goal4ag':'PASS','noneffective_through':30,'first_retained_curve_survivor':31,'explicit_F_B_materialized':False,'theorem_credit':False,'endpoint_credit':False},sort_keys=True))
