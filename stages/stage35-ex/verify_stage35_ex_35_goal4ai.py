#!/usr/bin/env python3
"""Permanent verifier for provisional Goal4AI degree-31 homogeneous principalization existence."""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
ART=ROOT/'stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence.json'
LOCK=ROOT/'stages/stage35-ex/35ex-35/goal4ai-degree31-homogeneous-principalization-existence-source-lock.md'
AA=ROOT/'stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json'
D25=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py'
D31=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ah_degree31_rr.py'
V72='STAGE35_EX_PESCH_E1_STATE_V72_GOAL4AI_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_PROVED_LITERAL_SECTION_COEFFICIENTS_PENDING_AUDIT'


def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

state=json.loads(STATE.read_text()); art=json.loads(ART.read_text()); aa=json.loads(AA.read_text())
assert state['schema']==V72
assert state['current']['unit']=='35EX-35_GOAL4AI_SECOND_CLASS_QI_CYCLIC_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_AND_LITERAL_SECTION_MATERIALIZATION_PREFLIGHT'
assert state['current']['next']=='35EX-35_GOAL4AJ_SECOND_CLASS_QI_CYCLIC_DEGREE31_LITERAL_SECTION_COEFFICIENT_EXTRACTION_PREFLIGHT'
assert state['claims']['goal4ai_executed'] is True
assert state['claims']['open_receiver_second_class_q_rational_principal_function_exists'] is True
assert state['claims']['open_receiver_second_class_homogeneous_principalization_existence_proved'] is True
assert state['claims']['open_receiver_second_class_achieved_homogeneous_degree']==31
assert state['claims']['open_receiver_second_class_degree31_literal_sections_materialized'] is False
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

assert art['schema']=='STAGE35_EX_35_GOAL4AI_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_V1'
assert art['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V71_GOAL4AH_DEGREE31_RR_EFFECTIVITY_PROVED_LITERAL_F_B_PENDING_AUDIT'
assert art['parent']['snapshot_path']=='stages/stage35-ex/snapshots/MAIN-STATE-V71-a8d275311cbd.json'
assert art['parent']['snapshot_file_commit_sha']=='49ed2417c3de101bf6c62dc7c483de686f69693c'
assert blob(LOCK)=='52e95382f7f05ea11479b01074574a16a22c49f9'
assert blob(AA)=='e0c3e31839b8f396e18fbafce7b021f66b8671a2'
assert blob(D25)=='a26b85c8f8be6426ecba7008ed34d6ae4d12248c'
assert blob(D31)=='d797ee20d7ee6f81f159249b61c492230d8eb306'
expected=art['canonical_sha256']
core={k:v for k,v in art.items() if k!='canonical_sha256'}
actual=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(',',':')).encode()).hexdigest()
assert expected==actual=='b6a927fcbad028c378bac73d3db6381754920e1f90316b27c275491bfdbf4d3a'

assert aa['class_B_principalization_target']['formal_target_picard_class_zero'] is True
assert aa['class_B_principalization_target']['formal_target_support_count']==69
assert aa['class_B_principalization_target']['explicit_F_B_materialized'] is False

# Recompute the common Picard residual packet exactly.
n25=runpy.run_path(str(D25))
Pc=n25['Pc']; Nc=n25['Nc']; H=n25['H']; pairing=n25['pairing']
assert Pc==Nc
assert pairing(H,H)==16
assert pairing(H,Pc)==396 and pairing(H,Nc)==396

# Recompute Goal4AH degree-31 effectivity and Q-descent invariance.
n31=runpy.run_path(str(D31)); d=n31['out']
assert d['degree']==31 and d['strip_steps']==325
assert d['stripped_residual_H_degree']==96 and d['stripped_residual_square']==212
assert d['h0_D_lower_bound']==66
assert d['q_defined_strip_data'] is True
assert d['degree31_original_residual_effective_over_Q'] is True

p=art['target_and_common_residual']
assert p['formal_target_picard_class_zero'] is True and p['target_q_defined'] is True
assert p['positive_negative_picard_classes_equal'] is True
assert p['homogeneous_degree']==31 and p['common_residual_class']=='31H-Pc=31H-Nc'
assert p['common_residual_q_effective'] is True
assert p['strip_steps']==325 and p['stripped_residual_h0_lower_bound']==66

des=art['descent']
assert des=={
 'geometric_principal_function_exists':True,
 'galois_ratio_is_constant_cocycle':True,
 'hilbert90_applied':True,
 'q_rational_principal_function_exists':True,
}
h=art['homogeneous_realization']
assert h['canonical_model_projectively_normal'] is True
assert h['resolution_global_sections_equal_canonical_model_sections'] is True
assert h['common_residual_reused_on_positive_and_negative_sides'] is True
assert h['q_degree31_numerator_section_exists'] is True
assert h['q_degree31_denominator_section_exists'] is True
assert h['degree31_homogeneous_principalization_existence_proved'] is True
assert h['achieved_homogeneous_degree']==31
assert h['literal_numerator_coefficients_materialized'] is False
assert h['literal_denominator_coefficients_materialized'] is False
assert h['explicit_F_B_materialized'] is False
assert art['route_result']['q_rational_principal_function_exists'] is True
assert art['route_result']['degree31_homogeneous_principalization_existence_proved'] is True
for k,v in art['credit_firewall'].items(): assert v is False,(k,v)
print('PASS Stage35-EX Goal4AI: degree31 Q-homogeneous principalization exists; literal section coefficients and explicit F_B remain pending')
