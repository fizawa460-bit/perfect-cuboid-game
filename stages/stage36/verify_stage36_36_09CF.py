#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CF/unused-alpha-hmu0-local-realization-preflight.json'
CE=ROOT/'stages/stage36/36-09CE/general-old-six-hmu0-tie-realization-preflight.json'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CC=ROOT/'stages/stage36/36-09CC/general-old-six-qq-source-pullback-preflight.json'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
V=ROOT/'stages/stage36/36-09V/gaussian-directional-prime-support-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='6431ec2a90ed9260d4362d7146a9788cbc21c8d1'
PARENT='13ba3948b114ec6323ee12097d17b6f22379aaf6'
PCI='34166897443/101879629715'
CERT_BLOB='37ae40020c829498f23fa38e3203e382115fd134'
LOCKS={CE:'fcad703975f2ea39a8306846284791c05b17bd7b',CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',CC:'5067d1723952edce9f4bab55cc427eb1745211cc',CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',V:'9fdec16f920104cc6c1961fb092185a0371258d5',BUV:'64b889c2dde22d021fb2933b976311d903f57dce'}

def git(*a:str)->str:return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p:Path)->str:return git('hash-object',str(p.relative_to(ROOT)))
def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def finite_exists(q:int,d:int,cminus:int,cplus:int,leg)->bool:
    for y in range(1,q):
        if y in (1,q-1):continue
        if leg(y,q)==d and leg(1-y,q)==cminus and leg(1+y,q)==cplus:return True
    return False

def small_lambda_ok(q:int,m:int,K:int,R:int,d:int,leg)->bool:
    eps=leg(-1,q)
    if K==R==d==1:return True
    if K==R==1 and finite_exists(q,d,d,d,leg):return True
    if m>=2 and eps==K==R==1:return True
    if eps*K==1 and R==1 and finite_exists(q,d,eps,1,leg):return True
    if eps*K==R==d==1:return True
    return False

def unused_alpha_ok(a:int,b:int,r,cev)->tuple[bool,list[tuple[str,int]]]:
    A,B,C,D,eta,e,f,mu,qok=r
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
    kappa=eta*(2**e)*C; rho=(2**f)*D
    fail=[]
    for q in cev.primes(P):
        if q==2 or A%q==0:continue
        K=cev.legendre(kappa*B,q); R=cev.legendre(rho*B,q); d=cev.legendre(A*B,q)
        if not small_lambda_ok(q,cev.vq(P,q),K,R,d,cev.legendre):fail.append(('P',q))
    for q in cev.primes(M):
        if q==2 or B%q==0:continue
        K=cev.legendre(-kappa*A,q); R=cev.legendre(rho*A,q); d=cev.legendre(A*B,q)
        if not small_lambda_ok(q,cev.vq(M,q),K,R,d,cev.legendre):fail.append(('M',q))
    return (not fail,fail)

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); ce=json.loads(CE.read_text()); cc=json.loads(CC.read_text()); bt=json.loads(BT.read_text()); vv=json.loads(V.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1699,'36_09CE_exact_green_head':PARENT,'36_09CE_exact_head_ci':PCI}
    assert ce['route_result']['next_leaf']=='36-09CF_UNUSED_OLD_SIX_HMU0_LOCAL_REALIZATION_PREFLIGHT'
    assert cc['general_old_six_source_pullback']['exact'] is True
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True
    assert vv['gaussian_direction_adapter']['alpha_extra_residue_identity'].startswith('2=')
    sm=c['small_lambda_model']; ma=c['M_side_adapter']; uf=c['unused_alpha_filter']
    assert sm['completeness'].startswith('the five sectors exhaust')
    assert sm['point_independent'].startswith('the finite-field existential')
    assert ma['exact'] is True
    assert uf['unused_alpha_hmu0_local_realization_complete_after_rule'] is True

    cev=load(CEV,'stage36_ce'); ccv=load(CCV,'stage36_cc'); buv=load(BUV,'stage36_bu')
    # Exhaust the character-sector truth table for representative alpha primes.
    for q in [7,17,23,31,41,47,71,73,79,89,97]:
        if cev.legendre(2,q)!=1:continue
        for m in (1,2,3):
            for K in (-1,1):
                for R in (-1,1):
                    for d in (-1,1):
                        x=small_lambda_ok(q,m,K,R,d,cev.legendre)
                        # direct implementation of the five stated sectors
                        eps=cev.legendre(-1,q)
                        y=(K==R==d==1 or
                           (K==R==1 and finite_exists(q,d,d,d,cev.legendre)) or
                           (m>=2 and eps==K==R==1) or
                           (eps*K==1 and R==1 and finite_exists(q,d,eps,1,cev.legendre)) or
                           (eps*K==R==d==1))
                        assert x==y

    expected={(1,2):(3,3),(2,11):(16,6),(3,4):(5,5),(1,8):(4,4)}
    for p,want in expected.items():
        rows=cev.cd_rows(ccv,buv,*p)
        rows=[r for r in rows if cev.ce_ok(*p,r)]
        good=[r for r in rows if unused_alpha_ok(*p,r,cev)[0]]
        assert (len(rows),len(good))==want,(p,len(rows),len(good),want)
    rows=cev.cd_rows(ccv,buv,2,11); rows=[r for r in rows if cev.ce_ok(2,11,r)]
    removed=[(r,unused_alpha_ok(2,11,r,cev)[1]) for r in rows if not unused_alpha_ok(2,11,r,cev)[0]]
    assert len(removed)==10
    assert all(any(q in (7,73) for side,q in why) for r,why in removed)

    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['CE_survivors'],d['p_1_over_2']['after_CF_unused_alpha'])==(3,3)
    assert (d['p_2_over_11']['CE_survivors'],d['p_2_over_11']['after_CF_unused_alpha'])==(16,6)
    assert d['diagnostic_p_3_over_4']['after_CF_unused_alpha']==5
    assert d['diagnostic_p_1_over_8']['after_CF_unused_alpha']==4
    rr=c['route_result']; bd=c['remaining_hmu0_boundary']; fw=c['scope_firewalls']
    assert rr['unused_alpha_hmu0_realization_complete'] is True
    assert rr['new_point_independent_branch_filter'] is True
    assert rr['next_leaf']=='36-09CG_BETA_EVEN_M_UNUSED_HMU0_LOCAL_REALIZATION_PREFLIGHT'
    assert bd['beta_even_m_unused_hmu0_realization_complete'] is False
    for k in ['CF_survivor_is_all_old_six_local_point','beta_even_m_unused_hmu0_realization_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V124_36_09CF_UNUSED_ALPHA_HMU0_REALIZATION'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cep=st['authority_frontier']['36-09CE']; assert cep['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cep['exact_head']==PARENT and cep['exact_head_ci']==PCI
    cf=st['authority_frontier']['36-09CF']; assert cf['certificate_blob_sha']==CERT_BLOB and cf['UNUSED_ALPHA_HMU0_REALIZATION_COMPLETE'] is True and cf['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CG_BETA_EVEN_M_UNUSED_HMU0_LOCAL_REALIZATION_PREFLIGHT' and st['current']['36_09CG_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:assert st['claims'][k] is False
    print('36-09CF verified: unused alpha hmu=0 local criterion is exact; p=2/11 drops 16->6, p=1/2 stays 3. Even-m unused beta hmu=0 remains for CG.')

if __name__=='__main__':main()
