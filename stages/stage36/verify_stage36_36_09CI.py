#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CI/general-q-reservoir-local-realization-preflight.json'
HNOTE=ROOT/'stages/stage36/36-09CI/hasse-bound-source-note.md'
CH=ROOT/'stages/stage36/36-09CH/selected-alpha-beta-hmu1-local-realization-preflight.json'
CHV=ROOT/'stages/stage36/verify_stage36_36_09CH.py'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CFV=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CGV=ROOT/'stages/stage36/verify_stage36_36_09CG.py'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BO=ROOT/'stages/stage36/36-09BO/q-reservoir-full-qq-cancellation-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='deaa08537f1e68e04e4189a51c6e02d28b2b7b13'
PARENT='624099676d03393a2ee0b1ef93df3b41b53e994c'
PCI='34169990479/101888318668'
CERT_BLOB='d4d5e44bdee091f5f8d8a7048013ffba552af698'
LOCKS={
    HNOTE:'7375d96c685197cf5cb0ef68c0ce1eb874d698a0',
    CH:'abedc4b33bf1c92e98efdcc43b5f0744630750a7',
    CHV:'98ae4bc76749c82b4165c7a7b37d7445f42fa6dc',
    CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',
    CFV:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',
    CGV:'7a210e55a5e2386fb02a59de00502a4e810b9410',
    CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    BO:'138749fde9766cd217fcb4622ccdebcb45730c2e',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(p:Path,n:str):
    s=importlib.util.spec_from_file_location(n,p)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def isprime(n:int)->bool:
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def generic_exists(q:int,d:int,k:int,r:int,leg)->bool:
    return any(
        y not in (0,1,q-1)
        and leg(y,q)==d
        and leg(1-y,q)==k
        and leg(1+y,q)==r
        for y in range(1,q)
    )

def cubic_sum(q:int,leg)->int:
    return sum(leg(y*(1-y*y),q) for y in range(q))

def hard_generic_count(q:int,d:int,k:int,r:int,leg)->int:
    return sum(
        1 for y in range(1,q)
        if y not in (1,q-1)
        and leg(y,q)==d
        and leg(1-y,q)==k
        and leg(1+y,q)==r
    )

def ch_rows(a:int,b:int,cev,cfv,cgv,ccv,buv,chv):
    rows=cev.cd_rows(ccv,buv,a,b)
    rows=[r for r in rows if cev.ce_ok(a,b,r) and cfv.unused_alpha_ok(a,b,r,cev)[0] and cgv.cg_ok(a,b,r,cev)]
    for r in rows:
        chv.selected_alpha_rows_consistent(a,b,r,cev)
    return [r for r in rows if chv.beta_hmu1_ok(a,b,r,cev)]

def q_prime_route(a:int,b:int,row,q:int,buv)->str:
    A,B,C,D,eta,e,f,mu,qok=row
    Q=a*a+b*b; D0=a*b*(a-b)*(a+b)
    assert Q%q==0 and q%2==1
    assert D0%q and A%q and B%q and C%q and D%q and mu%q
    assert buv.legendre(-1,q)==1
    assert buv.legendre(D0,q)==1
    kappa=eta*(2**e)*C; rho=(2**f)*D
    d=buv.legendre(A*B,q); k=buv.legendre(kappa*A,q); r=buv.legendre(rho*A,q); s=buv.legendre(2,q)
    assert buv.legendre(mu,q)==buv.legendre(kappa*rho,q)
    assert buv.legendre(mu*A*B,q)==1
    assert k*r*d==1
    if k==r==d==1:
        return 'small'
    if d==1 and k==r==s:
        return 'near_pm1'
    assert generic_exists(q,d,k,r,buv.legendre),(a,b,row,q,d,k,r,s)
    return 'generic'

def q_all_ok(a:int,b:int,row,buv)->tuple[bool,list[tuple[int,str]]]:
    out=[]
    for q in buv.primes(a*a+b*b):
        if q==2:continue
        out.append((q,q_prime_route(a,b,row,q,buv)))
    return True,out

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); ch=json.loads(CH.read_text()); bu=json.loads(BU.read_text()); bt=json.loads(BT.read_text()); bo=json.loads(BO.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1705,'promotion_head':PARENT,'promotion_ci':PCI,'consumed_pr':1699,'hostile_audit_review':5135648704}
    assert ch['old_six_completion']['all_old_six_local_realization_complete'] is True
    assert ch['old_six_completion']['does_not_cover_Q_reservoir'] is True
    assert bu['Q_reservoir_generalization']['branch_only_first_residue_row']=='Legendre(mu*A*B,q)=+1 for every odd q|Q'
    assert bu['scope_firewalls']['Q_branch_row_is_local_point_existential_sufficiency'] is False
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True
    assert bo['Q_reservoir_setup']['minus_one_square'] is True
    assert 'Hasse' in HNOTE.read_text() and '|#E(F_q) - (q+1)| <= 2*sqrt(q)' in HNOTE.read_text()

    setup=c['Q_reservoir_setup']; chars=c['character_coordinates']; sectors=c['valuation_sector_taxonomy']; ff=c['finite_field_generic_existence']; mc=c['main_consequence']
    assert 'v_q(lambda^2+1)=2h' in setup['lambda_shift']
    assert chars['Q_row_character_form']=='k*r*d=+1'
    assert sectors['exhaustive'].startswith('every q-adic y lies')
    assert ff['generic_pattern_count'].endswith('exactly (q+1+C_q)/8')
    assert ff['positivity'].endswith('> 0 for every odd q')
    assert 'all q congruent 1 modulo 4 below 300' in ff['universal_replay']
    assert mc['Q_reservoir_local_realization_complete'] is True
    assert mc['new_branch_filter_beyond_BU_Q_row'] is False

    for a in range(1,12):
        for b in range(1,12):
            if gcd(a,b)!=1 or a==b:continue
            P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; Q=a*a+b*b; D0=a*b*(a-b)*(a+b)
            if not P or not M or not D0:continue
            assert P*P+M*M==2*Q*Q
            assert P*P-M*M==8*D0

    tested=0
    for q in range(5,300):
        if not isprime(q) or q%4!=1:continue
        Cq=cubic_sum(q,lambda x,p:buv.legendre(x,p))
        assert Cq*Cq<=4*q
        s=buv.legendre(2,q)
        hard=[(-1,-1,1),(-1,1,-1)]
        if s==1: hard.append((1,-1,-1))
        for d,k,r in hard:
            assert d==k*r
            N=hard_generic_count(q,d,k,r,buv.legendre)
            assert N*8==q+1+Cq,(q,d,k,r,N,Cq)
            assert N>0,(q,d,k,r,N,Cq)
            tested+=1
    assert tested>0

    cev=load(CEV,'stage36_ce'); cfv=load(CFV,'stage36_cf'); cgv=load(CGV,'stage36_cg'); ccv=load(CCV,'stage36_cc'); buv=load(BUV,'stage36_bu'); chv=load(CHV,'stage36_ch')
    expected={(1,2):(3,3),(2,11):(5,5),(3,4):(3,3),(1,8):(3,3)}
    for p,want in expected.items():
        rows=ch_rows(*p,cev,cfv,cgv,ccv,buv,chv)
        good=[]
        for row in rows:
            ok,_=q_all_ok(*p,row,buv)
            if ok:good.append(row)
        assert (len(rows),len(good))==want,(p,len(rows),len(good),want)

    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['CH_survivors'],d['p_1_over_2']['after_CI_Q_reservoir'])==(3,3)
    assert (d['p_2_over_11']['CH_survivors'],d['p_2_over_11']['after_CI_Q_reservoir'])==(5,5)
    assert d['diagnostic_p_3_over_4']['after_CI_Q_reservoir']==3
    assert d['diagnostic_p_1_over_8']['after_CI_Q_reservoir']==3
    assert 'diagnostic_p_1_over_32' not in d

    rr=c['route_result']; fw=c['scope_firewalls']
    assert rr['general_Q_reservoir_local_realization_complete'] is True
    assert rr['BU_Q_row_necessary_and_sufficient'] is True
    assert rr['new_point_independent_branch_filter'] is False
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['next_leaf']=='36-09CJ_FIXED_P_ALL_BAD_PLACE_LOCAL_INTEGRATION_PREFLIGHT'
    for k in ['Q_reservoir_complete_means_simultaneous_all_place_point','CI_survivor_is_global_receiver','good_prime_and_real_place_integration_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V129_36_09CI_Q_RESERVOIR_LOCAL_COMPLETE'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    chp=st['authority_frontier']['36-09CH']
    assert chp['status']=='AUDITED_MERGED_INPUT'
    ci=st['authority_frontier']['36-09CI']
    assert ci['certificate_blob_sha']==CERT_BLOB
    assert ci['GENERAL_Q_RESERVOIR_LOCAL_REALIZATION_COMPLETE'] is True
    assert ci['BU_Q_ROW_NECESSARY_AND_SUFFICIENT'] is True
    assert ci['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CJ_FIXED_P_ALL_BAD_PLACE_LOCAL_INTEGRATION_PREFLIGHT'
    assert st['current']['36_09CJ_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CI verified: for every odd q|Q, the BU row Legendre(mu*A*B,q)=+1 is necessary and sufficient for the exact BT full-cover Q_q local model. Retained p=1/2 keeps 3 and p=2/11 keeps 5; CJ all-bad-place integration selected.')

if __name__=='__main__':main()
