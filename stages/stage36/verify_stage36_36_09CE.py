#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CE/general-old-six-hmu0-tie-realization-preflight.json'
CD=ROOT/'stages/stage36/36-09CD/fixed-p-old-six-branch-filter-integration-preflight.json'
CDV=ROOT/'stages/stage36/verify_stage36_36_09CD.py'
CC=ROOT/'stages/stage36/36-09CC/general-old-six-qq-source-pullback-preflight.json'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
MATH_BASE='5e5c262877a21a6ef197562143657ae1ac5963c7'
CURRENT_MAIN='6431ec2a90ed9260d4362d7146a9788cbc21c8d1'
PARENT='c17277966766a6c0260504a08bdc6df783e26af2'
PCI='34165069696/101874394471'
CERT_BLOB='fcad703975f2ea39a8306846284791c05b17bd7b'
LOCKS={
    CD:'78adcb3cf8f80c58cab77cedd3e694df8e266c8e',
    CDV:'8638530c242bd979031e76aab933dd7d6ffc9ed4',
    CC:'5067d1723952edce9f4bab55cc427eb1745211cc',
    CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def vq(n:int,q:int)->int:
    n=abs(n); c=0
    while n and n%q==0: c+=1; n//=q
    return c

def primes(n:int):
    n=abs(n); out=[]
    if n%2==0:
        out.append(2)
        while n%2==0:n//=2
    d=3
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=2
    if n>1:out.append(n)
    return out

def legendre(a:int,q:int)->int:
    a%=q
    if a==0:return 0
    x=pow(a,(q-1)//2,q)
    return 1 if x==1 else -1

def is_prime(q:int)->bool:
    if q<2:return False
    if q%2==0:return q==2
    d=3
    while d*d<=q:
        if q%d==0:return False
        d+=2
    return True

def cd_rows(ccv,buv,a:int,b:int):
    rows=ccv.bz_rows(buv,a,b)
    return [r for r in rows if ccv.alpha_ok(a,b,r) and ccv.beta_ok(a,b,r)]

def ce_ok(a:int,b:int,r)->bool:
    A,B,C,D,eta,e,f,mu,qok=r
    D0=a*b*(a-b)*(a+b)
    for q in primes(D0):
        if q==2: continue
        m=vq(D0,q)
        if m%2==1 and D%q==0 and q%4!=1:
            return False
        if m==1 and q==3 and C%3==0:
            kappa0=eta*(2**e)*(C//3)
            if legendre(kappa0*A*8*(D0//3),3)!=-1:
                return False
    return True

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',MATH_BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CURRENT_MAIN,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); cd=json.loads(CD.read_text()); cc=json.loads(CC.read_text()); ae=json.loads(AE.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==MATH_BASE
    assert c['batch_parent']=={'pr':1699,'36_09CD_exact_green_head':PARENT,'36_09CD_exact_head_ci':PCI}
    assert cd['route_result']['next_leaf']=='36-09CE_GENERAL_OLD_SIX_HMU0_TIE_REALIZATION_PREFLIGHT'
    assert cc['route_result']['general_old_six_source_pullback_exact'] is True
    assert ae['squareclass_variables']['properties'][-1]=='gcd(C,D)=1'
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True

    split=c['beta_hmu0_parity_split']; cs=c['C_selected_realization']; ds=c['D_selected_realization']; nr=c['new_branch_only_filters']
    assert split['hmu0_species']==['m even and q unused in C,D','m odd and q|C','m odd and q|D']
    assert 'q>=5' in cs['consequence'] and 'q=3' in cs['consequence']
    assert 'Legendre((kappa/3)*A*8*(D0/3),3)=+1' in cs['q3_integer_criterion']
    assert ds['branch_only_condition'].endswith('q congruent 1 modulo 4')
    assert ds['necessity'] is True and ds['q_3mod4_selected_D_branch_impossible'] is True
    assert nr['selected_beta_hmu0_local_realization_complete_after_rows'] is True

    for q in range(3,100):
        if not is_prime(q) or q==2: continue
        chi_minus=legendre(-1,q)
        for a in (-1,1):
            count=sum(1 for x in range(1,q) if x!=1 and legendre(x,q)==a and legendre(x-1,q)==a)
            formula=(q-3-a*(1+chi_minus))//4
            assert count==formula,(q,a,count,formula)
            fallback=(chi_minus*a==1)
            if q>=5: assert count>0 or fallback,(q,a,count,fallback)
            else: assert (count>0 or fallback)==(a==-1)

    for q in range(5,120):
        if not is_prime(q) or q%4!=1: continue
        for a in (-1,1):
            count=(q-3-a*2)//4
            fallback=(a==1)
            assert count>0 or fallback

    ccv=load(CCV,'stage36_cc'); buv=load(BUV,'stage36_bu')
    expected={(1,2):(4,3),(2,11):(18,16),(3,4):(6,5),(1,8):(4,4)}
    for p,want in expected.items():
        rows=cd_rows(ccv,buv,*p)
        good=[r for r in rows if ce_ok(*p,r)]
        assert (len(rows),len(good))==want,(p,len(rows),len(good),want)
    assert [r for r in cd_rows(ccv,buv,1,2) if not ce_ok(1,2,r)]==[(1,1,3,1,-1,0,1,1,True)]
    removed211=[r for r in cd_rows(ccv,buv,2,11) if not ce_ok(2,11,r)]
    assert len(removed211)==2 and all(r[3]==33 for r in removed211)

    rr=c['route_result']; bd=c['remaining_hmu0_boundary']; fw=c['scope_firewalls']
    assert rr['selected_beta_hmu0_realization_complete'] is True
    assert rr['new_point_independent_branch_rows']==2
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['next_leaf']=='36-09CF_UNUSED_OLD_SIX_HMU0_LOCAL_REALIZATION_PREFLIGHT'
    assert bd['selected_beta_hmu0_realization_complete'] is True
    assert bd['alpha_unselected_hmu0_realization_complete'] is False
    assert bd['beta_even_m_unused_hmu0_realization_complete'] is False
    for k in ['CE_survivor_is_all_old_six_local_point','alpha_unselected_hmu0_realization_complete','beta_even_m_unused_hmu0_realization_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V123_36_09CE_SELECTED_BETA_HMU0_REALIZATION'
    assert st['base_main_sha']==CURRENT_MAIN and st['freshness']['current_main']==CURRENT_MAIN
    cdp=st['authority_frontier']['36-09CD']
    assert cdp['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cdp['exact_head']==PARENT and cdp['exact_head_ci']==PCI
    ce=st['authority_frontier']['36-09CE']
    assert ce['certificate_blob_sha']==CERT_BLOB
    assert ce['SELECTED_BETA_HMU0_REALIZATION_COMPLETE'] is True
    assert ce['NEW_POINT_INDEPENDENT_BRANCH_ROWS']==2
    assert ce['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CF_UNUSED_OLD_SIX_HMU0_LOCAL_REALIZATION_PREFLIGHT'
    assert st['current']['36_09CF_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CE verified: selected beta hmu=0 realization is exact. D-selected odd-m primes require q=1 mod4; simple q=3 C-selected has one exact obstruction. Counts p=1/2 4->3, p=2/11 18->16. CF selected.')

if __name__=='__main__': main()
