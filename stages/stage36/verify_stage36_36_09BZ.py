#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BZ/fixed-p-alpha-pullback-filter-integration-preflight.json'
BY=ROOT/'stages/stage36/36-09BY/remaining-q2-alpha-tie-gate-parameter-pullback-preflight.json'
BYV=ROOT/'stages/stage36/verify_stage36_36_09BY.py'
BX=ROOT/'stages/stage36/36-09BX/fixed-p-q2-branch-filter-integration-preflight.json'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='af40c029a8721755b39dad13be452a2a74540c4e'
PARENT='98f247ffa5b37e637097cdedd034674f727bfc54'
PCI='34132943006/101777172748'
CERT_BLOB='d220e1a2de3f7595e498b8987f9fa90035a1f7d9'
LOCKS={BY:'35198e4124d154d1f07fdcd526899231842a1b43',BYV:'d0f64ae03ddc41b03924adf836e217a4f340d293',BX:'9edd1343c38005d2d47954e2652b43b02079c160',BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',BUV:'64b889c2dde22d021fb2933b976311d903f57dce'}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); by=json.loads(BY.read_text()); bx=json.loads(BX.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1696,'36_09BY_exact_green_head':PARENT,'36_09BY_exact_head_ci':PCI}
    assert by['route_result']['next_leaf']=='36-09BZ_FIXED_P_ALPHA_PULLBACK_FILTER_INTEGRATION_PREFLIGHT'
    assert by['route_result']['new_point_independent_branch_rows']==2
    assert bx['sound_exclusion_rule']['parameter_exclusion_requires_zero_survivors'] is True
    fam=c['integrated_family']; rule=c['sound_fixed_p_exclusion_rule']; rr=c['route_result']; fw=c['scope_firewalls']
    assert fam['name']=='F_{Q,2,alpha}^{branch}(p)'
    assert len(fam['filters_in_order'])==5
    assert fam['all_rows_are_receiver_necessary'] is True
    assert fam['tie_unit_realization_filter_included'] is False
    assert rule['unconditional'] is True and rule['converse'] is False
    assert rule['surviving_branch_is_Q2_point'] is False and rule['surviving_branch_is_receiver_point'] is False

    byv=load(BYV,'stage36_by')
    bu=load(BUV,'stage36_bu')
    expected={(1,2):(14,8,6,4,4),(2,11):(158,77,52,30,30),(3,4):(44,21,16,8,6),(1,8):(47,14,8,8,5)}
    got={p:byv.pipeline(bu,*p)[0] for p in expected}
    assert got==expected,got
    d=c['exact_fixed_p_diagnostics']
    assert tuple(d['p_1_over_2'][k] for k in ['AW_AE_outer','after_Q','after_AB','after_BX_critical','after_BY_alpha'])==expected[(1,2)]
    assert tuple(d['p_2_over_11'][k] for k in ['AW_AE_outer','after_Q','after_AB','after_BX_critical','after_BY_alpha'])==expected[(2,11)]
    assert tuple(d['diagnostic_p_3_over_4'][k] for k in ['AW_AE_outer','after_Q','after_AB','after_BX_critical','after_BY_alpha'])==expected[(3,4)]
    assert tuple(d['diagnostic_p_1_over_8'][k] for k in ['AW_AE_outer','after_Q','after_AB','after_BX_critical','after_BY_alpha'])==expected[(1,8)]
    assert d['p_1_over_2']['fixed_p_excluded'] is False and d['p_2_over_11']['fixed_p_excluded'] is False
    assert 'not a retained-candidate membership assertion' in d['diagnostic_p_3_over_4']['scope']
    assert 'not a retained-candidate membership assertion' in d['diagnostic_p_1_over_8']['scope']
    assert rr['fixed_p_alpha_filter_integration_complete'] is True
    assert rr['sound_zero_survivor_exclusion_rule'] is True
    assert rr['new_rows_integrated']==2
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['candidate_parameter_set_shrunk'] is False
    assert rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09CA_GENERAL_TIE_UNIT_SOURCE_PULLBACK_PREFLIGHT'
    for k in ['surviving_branch_implies_Q2_point','surviving_branch_implies_receiver_point','tie_unit_gate_integrated_as_row_filter','full_Q2_local_solubility_classified_for_general_AW_branch','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V116_36_09BZ_ALPHA_FILTER_INTEGRATION'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    yp=st['authority_frontier']['36-09BY']
    assert yp['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and yp['exact_head']==PARENT and yp['exact_head_ci']==PCI
    z=st['authority_frontier']['36-09BZ']
    assert z['certificate_blob_sha']==CERT_BLOB
    assert z['FIXED_P_ALPHA_FILTER_INTEGRATION_COMPLETE'] is True
    assert z['SOUND_ZERO_SURVIVOR_EXCLUSION_RULE'] is True
    assert z['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CA_GENERAL_TIE_UNIT_SOURCE_PULLBACK_PREFLIGHT'
    assert st['current']['36_09CA_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09BZ verified: F_{Q,2,alpha}^{branch}(p) integrates the two exact BY alpha rows; p=1/2 and 2/11 retain 4 and 30 branches, diagnostics 3/4 and 1/8 retain 6 and 5. Zero survivors would exclude a fixed p, but no parameter or receiver closure is obtained. CA selected.')

if __name__=='__main__': main()
