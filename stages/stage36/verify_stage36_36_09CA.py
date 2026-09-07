#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CA/general-tie-unit-source-pullback-preflight.json'
BZ=ROOT/'stages/stage36/36-09BZ/fixed-p-alpha-pullback-filter-integration-preflight.json'
BZV=ROOT/'stages/stage36/verify_stage36_36_09BZ.py'
BY=ROOT/'stages/stage36/36-09BY/remaining-q2-alpha-tie-gate-parameter-pullback-preflight.json'
BYV=ROOT/'stages/stage36/verify_stage36_36_09BY.py'
BW=ROOT/'stages/stage36/36-09BW/general-aw-branch-prime2-taxonomy-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='af40c029a8721755b39dad13be452a2a74540c4e'
PARENT='dc6c23acbfc77ea5e3ce4951f136be0daa291db2'
PCI='34149039121/101827189412'
CERT_BLOB='db99f4dfe28754799af33f7354afa02cd8a85981'
LOCKS={
    BZ:'d220e1a2de3f7595e498b8987f9fa90035a1f7d9',
    BZV:'4b24aaae212d920a9eb37b5bab9c7a87fa23c862',
    BY:'35198e4124d154d1f07fdcd526899231842a1b43',
    BYV:'d0f64ae03ddc41b03924adf836e217a4f340d293',
    BW:'d7feb3e6b86c5c93bae999f8836840e64fbd5fb5',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def v2_int(n:int)->int:
    assert n
    n=abs(n); c=0
    while n%2==0:
        c+=1; n//=2
    return c

def v2_frac(x:Fraction)->int:
    return v2_int(x.numerator)-v2_int(x.denominator)

def odd_unit_mod4(x:Fraction)->int:
    x=Fraction(x)
    k=v2_frac(x)
    assert k==0
    n=x.numerator; d=x.denominator
    return (n%4)*pow(d%4,-1,4)%4

def oddpart(n:int)->int:
    while n%2==0:
        n//=2
    return n

def parameter_data(a:int,b:int):
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
    D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    assert P and M and D0 and gcd(a,b)==1
    delta=v2_int(D0); sigma=v2_int(Q); assert sigma in (0,1)
    d=delta-2*sigma; assert d>=1
    tau=1 if sigma==0 else -1
    lam=Fraction(P,M)
    L=(lam-tau)/(2**(d+2))
    assert v2_frac(lam-tau)==d+2
    assert v2_frac(L)==0
    D0odd=D0//(2**delta)
    assert (tau*odd_unit_mod4(L))%4==D0odd%4
    return P,M,D0,Q,delta,sigma,d,tau,L,D0odd

def tie_needed_rows(byv,buv,a:int,b:int):
    counts,removed=byv.pipeline(buv,a,b)
    rows=buv.ae_outer(a,b)
    P,M,D0,Q,delta,sigma,d,tau,L,D0odd=parameter_data(a,b)
    q=[r for r in rows if r[-1]]
    same=[r for r in q if r[0]%8==r[1]%8]
    bx=[r for r in same if not(r[6]==1 and delta==2*sigma+2-r[5])]
    bz=[]
    for r in bx:
        A,B,C,D,eta,e,f,mu,qok=r
        db=(D*pow(B,-1,8))%8
        bad1=(f==1 and e==1 and db==5 and d==2)
        bad2=(f==1 and e==1 and db==1 and d==3)
        if not(bad1 or bad2): bz.append(r)
    assert len(bz)==counts[-1]
    need=[]
    for r in bz:
        A,B,C,D,eta,e,f,mu,qok=r
        if f!=1 or (D*pow(B,-1,8))%8!=1: continue
        amin=4 if e==0 else 5
        Delta_max=d+3-amin
        g=(delta+e+f)%2
        mu0=oddpart(mu)
        if g==0 and Delta_max in (0,2) and mu0%8 in (1,5):
            # These are precisely the shallow rows for which the negative
            # dominance alternatives do not help and the tie must realize.
            lhs=(eta*C*pow(B%4,-1,4))%4
            rhs=(tau*odd_unit_mod4(L))%4
            assert mu0%4==1
            # odd square removal preserves mod4, and D/B=1 mod8.
            assert mu0%4==(eta*D0odd*C*D)%4
            assert (D*pow(B,-1,4))%4==1
            assert lhs==D0odd%4==rhs
            need.append(r)
    return counts,need

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bz=json.loads(BZ.read_text()); bw=json.loads(BW.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1696,'36_09BZ_exact_green_head':PARENT,'36_09BZ_exact_head_ci':PCI}
    assert bz['route_result']['next_leaf']=='36-09CA_GENERAL_TIE_UNIT_SOURCE_PULLBACK_PREFLIGHT'
    assert bt['general_BH_elimination']['identities']==['P^2-M^2=8*D0','P^2+M^2=2*Q^2']
    assert bw['remaining_same_AB_taxonomy']['deep_f1_minus_root']['Delta_0']=='g=0 tie; use the generic n-even and w0=1 mod8 criterion'
    pu=c['parameter_unit_lemma']; ts=c['tie_source_pullback']; ar=c['automatic_identity_on_tie_needed_rows']
    assert pu['valuation']=='v2(lambda-tau)=d+2'
    assert pu['mod4_identity']=='tau*L congruent D0odd modulo 4'
    assert ts['tie_alpha']=='alpha=d+3'
    assert ts['z_difference']=='z^2-mu=mu*M^2*(y^2-lambda^2)/(4*D0*(y^2+1))'
    assert ts['tie_valuation']=='N=v2(q-s*L)'
    assert ar['consequence']=='the tie-unit gate contributes no additional point-independent outer-branch exclusion beyond BZ'

    # Algebraic parameter-unit lemma sanity across a bounded primitive panel.
    for a in range(1,25):
        for b in range(1,25):
            if gcd(a,b)!=1 or a==b: continue
            P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
            if not P or not M or not D0: continue
            parameter_data(a,b)

    byv=load(BYV,'stage36_by'); buv=load(BUV,'stage36_bu')
    expected={(1,2):(4,1),(2,11):(30,10),(3,4):(6,2),(1,8):(5,1)}
    got={}
    for p,(bz_count,need_count) in expected.items():
        counts,need=tie_needed_rows(byv,buv,*p)
        assert counts[-1]==bz_count
        assert len(need)==need_count
        got[p]=(counts[-1],len(need))
    assert got==expected
    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['BZ_survivors'],d['p_1_over_2']['tie_needed_mu_1_or_5_rows'],d['p_1_over_2']['tie_realizable_rows'])==(4,1,1)
    assert (d['p_2_over_11']['BZ_survivors'],d['p_2_over_11']['tie_needed_mu_1_or_5_rows'],d['p_2_over_11']['tie_realizable_rows'])==(30,10,10)
    assert (d['diagnostic_p_3_over_4']['BZ_survivors'],d['diagnostic_p_3_over_4']['tie_needed_mu_1_or_5_rows'],d['diagnostic_p_3_over_4']['tie_realizable_rows'])==(6,2,2)
    assert (d['diagnostic_p_1_over_8']['BZ_survivors'],d['diagnostic_p_1_over_8']['tie_needed_mu_1_or_5_rows'],d['diagnostic_p_1_over_8']['tie_realizable_rows'])==(5,1,1)

    rr=c['route_result']; fw=c['scope_firewalls']; bd=c['remaining_Q2_boundary']
    assert rr['parameter_unit_lemma_exact'] is True
    assert rr['tie_source_pullback_exact'] is True
    assert rr['tie_needed_sector_locally_realizable'] is True
    assert rr['new_point_independent_branch_rows']==0
    assert bd['tie_unit_source_pullback_complete'] is True
    assert bd['tie_unit_is_independent_branch_filter'] is False
    assert bd['all_BZ_survivors_have_Q2_point_claimed'] is False
    assert rr['next_leaf']=='36-09CB_GENERAL_Q2_SOURCE_CONIC_REALIZATION_PREFLIGHT'
    for k in ['all_BZ_outer_survivors_are_Q2_points','mixed_f0_source_conic_realization_complete','outer_branch_survivor_is_receiver','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V117_36_09CA_TIE_SOURCE_PULLBACK'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    zp=st['authority_frontier']['36-09BZ']
    assert zp['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and zp['exact_head']==PARENT and zp['exact_head_ci']==PCI
    ca=st['authority_frontier']['36-09CA']
    assert ca['certificate_blob_sha']==CERT_BLOB
    assert ca['TIE_SOURCE_PULLBACK_EXACT'] is True
    assert ca['NEW_POINT_INDEPENDENT_BRANCH_ROWS']==0
    assert ca['TIE_NEEDED_SECTOR_LOCALLY_REALIZABLE'] is True
    assert st['current']['next_exact_leaf']=='36-09CB_GENERAL_Q2_SOURCE_CONIC_REALIZATION_PREFLIGHT'
    assert st['current']['36_09CB_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CA verified: the general deep tie-unit gate pulls back exactly. On tie-needed mu0=1/5 rows the realization congruence is automatic from the parameter-unit and squareclass identities, so no new branch filter is charged; CB source-conic Q2 realization is selected.')

if __name__=='__main__': main()
