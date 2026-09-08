#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CJ/fixed-p-all-bad-place-local-integration-preflight.json'
CB=ROOT/'stages/stage36/36-09CB/general-q2-source-conic-realization-preflight.json'
CBV=ROOT/'stages/stage36/verify_stage36_36_09CB.py'
CD=ROOT/'stages/stage36/36-09CD/fixed-p-old-six-branch-filter-integration-preflight.json'
CH=ROOT/'stages/stage36/36-09CH/selected-alpha-beta-hmu1-local-realization-preflight.json'
CHV=ROOT/'stages/stage36/verify_stage36_36_09CH.py'
CI=ROOT/'stages/stage36/36-09CI/general-q-reservoir-local-realization-preflight.json'
CIV=ROOT/'stages/stage36/verify_stage36_36_09CI.py'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CFV=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CGV=ROOT/'stages/stage36/verify_stage36_36_09CG.py'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='deaa08537f1e68e04e4189a51c6e02d28b2b7b13'
PARENT='7ebabfcef83571d172c65862bc4dc763ac999b9c'
PCI='34172356210/101894957109'
CERT_BLOB='bf98c1bfd468ff975755d364081d829b1f8c1233'
LOCKS={
    CB:'a55a48213f9e06346f7f500387ac812d85a7acc0',
    CBV:'4e7d21c03cd7fdcf07b082a76fb626cc6fea694d',
    CD:'78adcb3cf8f80c58cab77cedd3e694df8e266c8e',
    CH:'abedc4b33bf1c92e98efdcc43b5f0744630750a7',
    CHV:'98ae4bc76749c82b4165c7a7b37d7445f42fa6dc',
    CI:'d4d5e44bdee091f5f8d8a7048013ffba552af698',
    CIV:'53655d24a59024766b6be3cba00720bed86916ad',
    CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',
    CFV:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',
    CGV:'7a210e55a5e2386fb02a59de00502a4e810b9410',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(p:Path,n:str):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cb=json.loads(CB.read_text()); cd=json.loads(CD.read_text()); ch=json.loads(CH.read_text()); ci=json.loads(CI.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1705,'36_09CI_exact_green_head':PARENT,'36_09CI_exact_head_ci':PCI}
    assert cb['prime2_exact_local_result']['BZ_survivor_implies_Q2_full_cover_branch_point'] is True
    assert cb['prime2_exact_local_result']['prime2_branch_filter_layer_complete'] is True
    assert cd['integrated_family']['name']=='F_{Q,2,alpha,old6}^{branch}(p)'
    assert ch['old_six_completion']['all_old_six_local_realization_complete'] is True
    assert ci['route_result']['general_Q_reservoir_local_realization_complete'] is True
    assert ci['route_result']['BU_Q_row_necessary_and_sufficient'] is True

    fam=c['fixed_p_branch_family']; cover=c['finite_bad_place_cover']; mc=c['main_consequence']; rem=c['remaining_local_boundary']; rr=c['route_result']; fw=c['scope_firewalls']
    assert fam['name']=='F_bad^branch(p)'
    assert fam['same_global_branch_across_places'] is True
    assert fam['local_coordinates_may_vary_by_place'] is True
    assert fam['does_not_require_one_common_t_across_distinct_completions'] is True
    assert cover['branchwise_all_finite_bad_places_locally_realized'] is True
    assert cover['new_branch_filter'] is False
    assert mc['finite_bad_place_branch_local_realization_complete'] is True
    assert mc['new_point_independent_branch_filter'] is False
    assert rem['good_odd_primes_complete'] is False and rem['real_place_complete'] is False and rem['full_adelic_local_solubility_complete'] is False

    civ=load(CIV,'stage36_ci'); chv=load(CHV,'stage36_ch'); cev=load(CEV,'stage36_ce'); cfv=load(CFV,'stage36_cf'); cgv=load(CGV,'stage36_cg'); ccv=load(CCV,'stage36_cc'); buv=load(BUV,'stage36_bu')
    expected={(1,2):3,(2,11):5,(3,4):3,(1,8):3}
    for p,want in expected.items():
        bz=ccv.bz_rows(buv,*p)
        rows=civ.ch_rows(*p,cev,cfv,cgv,ccv,buv,chv)
        assert len(rows)==want,(p,len(rows),want)
        assert all(r in bz for r in rows),(p,'CH row escaped BZ family')
        for row in rows:
            ok,routes=civ.q_all_ok(*p,row,buv)
            assert ok
            assert all(kind in {'small','near_pm1','generic'} for _,kind in routes)

    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['CH_survivors'],d['p_1_over_2']['after_CJ_all_finite_bad_places'])==(3,3)
    assert (d['p_2_over_11']['CH_survivors'],d['p_2_over_11']['after_CJ_all_finite_bad_places'])==(5,5)
    assert d['diagnostic_p_3_over_4']['after_CJ_all_finite_bad_places']==3
    assert d['diagnostic_p_1_over_8']['after_CJ_all_finite_bad_places']==3
    assert d['p_1_over_2']['fixed_p_excluded'] is False and d['p_2_over_11']['fixed_p_excluded'] is False

    assert rr['finite_bad_place_branch_local_realization_complete'] is True
    assert rr['new_point_independent_branch_filter'] is False
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['candidate_parameter_set_shrunk'] is False
    assert rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09CK_GOOD_PRIME_AND_REAL_PLACE_LOCAL_INTEGRATION_PREFLIGHT'
    for k in ['finite_bad_place_complete_means_everywhere_local','CJ_survivor_is_global_receiver','CJ_survivor_is_rational_point','good_prime_and_real_place_integration_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V130_36_09CJ_ALL_FINITE_BAD_PLACE_LOCAL_COMPLETE'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cip=st['authority_frontier']['36-09CI']
    assert cip['status']=='PROVISIONAL_EXACT_GREEN_PARENT'
    assert cip['exact_head']==PARENT and cip['exact_head_ci']==PCI
    cj=st['authority_frontier']['36-09CJ']
    assert cj['certificate_blob_sha']==CERT_BLOB
    assert cj['FINITE_BAD_PLACE_BRANCH_LOCAL_REALIZATION_COMPLETE'] is True
    assert cj['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CK_GOOD_PRIME_AND_REAL_PLACE_LOCAL_INTEGRATION_PREFLIGHT'
    assert st['current']['36_09CK_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CJ verified: every CH survivor remains a BZ branch with a Q2 point, has old-six local points, and satisfies CI at every odd q|Q. Thus all finite bad places are locally realized branchwise; p=1/2 keeps 3 and p=2/11 keeps 5. CK selected.')

if __name__=='__main__':main()
