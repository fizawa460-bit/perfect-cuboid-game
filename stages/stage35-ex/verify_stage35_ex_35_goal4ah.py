#!/usr/bin/env python3
"""Permanent verifier for provisional Goal4AH degree-31 RR effectivity."""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage35-ex/MAIN-STATE.json'
ART=ROOT/'stages/stage35-ex/35ex-35/goal4ah-degree31-rr-effectivity.json'
LOCK=ROOT/'stages/stage35-ex/35ex-35/goal4ah-degree31-rr-effectivity-source-lock.md'
DIAG=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ah_degree31_rr.py'
V71='STAGE35_EX_PESCH_E1_STATE_V71_GOAL4AH_DEGREE31_RR_EFFECTIVITY_PROVED_LITERAL_F_B_PENDING_AUDIT'

def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

state=json.loads(STATE.read_text()); art=json.loads(ART.read_text())
assert state['schema']==V71
assert state['current']['unit']=='35EX-35_GOAL4AH_SECOND_CLASS_QI_CYCLIC_DEGREE31_SURVIVOR_EFFECTIVITY_AND_PRINCIPAL_FUNCTION_SYNTHESIS_PREFLIGHT'
assert state['current']['next']=='35EX-35_GOAL4AI_SECOND_CLASS_QI_CYCLIC_DEGREE31_HOMOGENEOUS_PRINCIPALIZATION_EXISTENCE_AND_LITERAL_SECTION_MATERIALIZATION_PREFLIGHT'
assert state['claims']['goal4ah_executed'] is True
assert state['claims']['open_receiver_second_class_degree31_effectivity_proved'] is True
assert state['claims']['open_receiver_second_class_explicit_F_B_computed'] is False
assert state['claims']['E1_proved'] is False and state['claims']['stage35_closed'] is False

assert art['schema']=='STAGE35_EX_35_GOAL4AH_DEGREE31_RR_EFFECTIVITY_V1'
assert art['canonical_sha256']=='958d9de580794f2bd40c1c7defd1e9d487cca4074e1389613e08a5126089d1b9'
assert art['parent']['schema']=='STAGE35_EX_PESCH_E1_STATE_V70_GOAL4AG_HOMOGENEOUS_DEGREE25_TO30_PRINCIPALIZATION_EXCLUDED_DEGREE31_SURVIVES_RETAINED_CURVE_TEST_PENDING_AUDIT'
assert art['parent']['snapshot_path']=='stages/stage35-ex/snapshots/MAIN-STATE-V70-86f1a13c0423.json'
assert art['parent']['snapshot_file_commit_sha']=='f432c76ea18cf8d5e76ced1e3eb40680b965ea48'
assert art['source_locks']['degree31_rr_diagnostic']['git_blob_sha1']=='d797ee20d7ee6f81f159249b61c492230d8eb306'
assert blob(DIAG)=='d797ee20d7ee6f81f159249b61c492230d8eb306'
assert blob(LOCK)=='096e5138a00928d9f5f1975518c4c15b59ab2a3b'
run=art['exact_runs']['degree31_rr']
assert run=={'head_sha':'86f1a13c042357a8a727dce45209294ce3c0cb5d','workflow_run':34078793811,'job':101610034252,'conclusion':'SUCCESS'}
outage=art['exact_runs']['magma_raw_outage_diagnostic']
assert outage['result']=='REMOTE_MAGMA_CALCULATOR_OFFLINE_ELECTRICAL_WORK_NO_MATHEMATICAL_NEGATIVE_CREDIT'

ns=runpy.run_path(str(DIAG)); d=ns['out']
assert d['schema']=='STAGE35_EX_GOAL4AH_DEGREE31_RR_EFFECTIVITY_DIAGNOSTIC_V1'
assert d['degree']==31 and d['strip_steps']==325
assert d['forced_support_count']==44
assert d['forced_strict_multiplicity_sum']==2
assert d['forced_exceptional_multiplicity_sum']==323
assert d['stripped_residual_H_degree']==96 and d['stripped_residual_square']==212
assert d['surface_K_square']==16 and d['surface_chi_O']==8
assert d['surface_canonical_class_equals_H'] is True and d['H_nef'] is True
assert d['chi_O_D']==66 and d['H_dot_K_minus_D']==-80
assert d['h2_D_zero'] is True and d['h0_D_lower_bound']==66
assert d['q_defined_strip_data'] is True
assert d['degree31_stripped_residual_effective_over_Q'] is True
assert d['degree31_original_residual_effective_over_Q'] is True
for name in ('formal_target_galois_invariant','positive_part_galois_invariant','negative_part_galois_invariant','forced_multiplicities_galois_invariant','stripped_residual_class_galois_invariant'):
    assert d[name]=={'cc':True,'ct':True}

packet=art['degree31_exact_packet']; rr=art['riemann_roch']
assert packet['degree']==31 and packet['strip_steps']==325 and packet['q_defined_strip_data'] is True
assert packet['stripped_residual_hyperplane_degree']==96 and packet['stripped_residual_square']==212
assert rr['canonical_class']=='H' and rr['canonical_square']==16 and rr['chi_O_S']==8
assert rr['D_square']==212 and rr['K_dot_D']==96 and rr['chi_O_D']==66
assert rr['H_dot_K_minus_D']==-80 and rr['H_nef'] is True
assert rr['K_minus_D_effective'] is False and rr['h2_D']==0 and rr['h0_D_lower_bound']==66
assert rr['stripped_residual_effective_over_Q'] is True and rr['original_degree31_residual_effective_over_Q'] is True
assert art['route_result']['degree31_q_defined_effectivity_proved'] is True
assert art['route_result']['explicit_F_B_materialized'] is False
for k,v in art['credit_firewall'].items(): assert v is False, (k,v)
print('PASS Stage35-EX Goal4AH: degree31 residual effective over Q by exact strip + surface RR; literal F_B still pending')
