#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CD/fixed-p-old-six-branch-filter-integration-preflight.json'
CC=ROOT/'stages/stage36/36-09CC/general-old-six-qq-source-pullback-preflight.json'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BZ=ROOT/'stages/stage36/36-09BZ/fixed-p-alpha-pullback-filter-integration-preflight.json'
AW=ROOT/'stages/stage36/36-09AW/fixed-p-finite-squareclass-tunnell-branch-sieve-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='5e5c262877a21a6ef197562143657ae1ac5963c7'
PARENT='99a4f5235b0d2c9a8aaabc1ad2e36eadf518e7e7'
PCI='34164929391/101873986407'
CERT_BLOB='78adcb3cf8f80c58cab77cedd3e694df8e266c8e'
LOCKS={
    CC:'5067d1723952edce9f4bab55cc427eb1745211cc',
    CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    BZ:'d220e1a2de3f7595e498b8987f9fa90035a1f7d9',
    AW:'c1970a020803275ba87b249229e319367fa8f811',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
}

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
    c=json.loads(CERT.read_text()); cc=json.loads(CC.read_text()); bz=json.loads(BZ.read_text()); aw=json.loads(AW.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1699,'36_09CC_exact_green_head':PARENT,'36_09CC_exact_head_ci':PCI}
    assert cc['route_result']['next_leaf']=='36-09CD_FIXED_P_OLD_SIX_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    fam=c['integrated_family']; rule=c['sound_fixed_p_exclusion_rule']; rr=c['route_result']; fw=c['scope_firewalls']
    assert fam['name']=='F_{Q,2,alpha,old6}^{branch}(p)'
    assert len(fam['filters_in_order'])==6
    assert fam['all_rows_are_receiver_necessary'] is True
    assert fam['all_rows_are_point_independent'] is True
    assert fam['old_six_hmu0_tie_realization_included'] is False
    assert rule['unconditional_given_CC_exactness'] is True
    assert rule['converse'] is False
    assert rule['surviving_branch_is_Qq_point_at_old_six'] is False
    assert rule['surviving_branch_is_receiver_point'] is False
    assert aw['fixed_p_outer_enumerator']['outer_superset'] is True
    assert bz['sound_fixed_p_exclusion_rule']['unconditional'] is True

    ccv=load(CCV,'stage36_cc'); buv=load(BUV,'stage36_bu')
    expected={(1,2):(4,4),(2,11):(30,18),(3,4):(6,6),(1,8):(5,4)}
    got={}
    for p,want in expected.items():
        rows=ccv.bz_rows(buv,*p)
        good=[r for r in rows if ccv.alpha_ok(*p,r) and ccv.beta_ok(*p,r)]
        got[p]=(len(rows),len(good))
        assert got[p]==want,(p,got[p],want)
    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['BZ_survivors'],d['p_1_over_2']['after_CC_old_six'])==(4,4)
    assert (d['p_2_over_11']['BZ_survivors'],d['p_2_over_11']['after_CC_old_six'])==(30,18)
    assert d['p_2_over_11']['after_CC_selected_alpha']==20
    assert d['diagnostic_p_3_over_4']['after_CC_old_six']==6
    assert d['diagnostic_p_1_over_8']['after_CC_old_six']==4
    assert d['p_1_over_2']['fixed_p_excluded'] is False
    assert d['p_2_over_11']['fixed_p_excluded'] is False

    assert rr['fixed_p_old_six_filter_integration_complete'] is True
    assert rr['sound_zero_survivor_exclusion_rule'] is True
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['candidate_parameter_set_shrunk'] is False
    assert rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09CE_GENERAL_OLD_SIX_HMU0_TIE_REALIZATION_PREFLIGHT'
    for k in ['surviving_branch_implies_old_six_local_points','surviving_branch_implies_receiver_point','old_six_hmu0_tie_realization_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V122_36_09CD_OLD_SIX_FILTER_INTEGRATION'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    ccp=st['authority_frontier']['36-09CC']
    assert ccp['status']=='PROVISIONAL_EXACT_GREEN_PARENT'
    assert ccp['exact_head']==PARENT and ccp['exact_head_ci']==PCI
    cd=st['authority_frontier']['36-09CD']
    assert cd['certificate_blob_sha']==CERT_BLOB
    assert cd['FIXED_P_OLD_SIX_FILTER_INTEGRATION_COMPLETE'] is True
    assert cd['SOUND_ZERO_SURVIVOR_EXCLUSION_RULE'] is True
    assert cd['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CE_GENERAL_OLD_SIX_HMU0_TIE_REALIZATION_PREFLIGHT'
    assert st['current']['36_09CE_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CD verified: F_{Q,2,alpha,old6}^{branch}(p) integrates the two exact CC filter families; p=1/2 retains 4 and p=2/11 retains 18. Zero survivors would exclude fixed p, but no parameter/receiver closure is obtained. CE selected.')

if __name__=='__main__': main()
