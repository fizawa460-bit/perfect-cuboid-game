#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from fractions import Fraction
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CC/general-old-six-qq-source-pullback-preflight.json'
CB=ROOT/'stages/stage36/36-09CB/general-q2-source-conic-realization-preflight.json'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
V=ROOT/'stages/stage36/36-09V/gaussian-directional-prime-support-preflight.json'
BZ=ROOT/'stages/stage36/36-09BZ/fixed-p-alpha-pullback-filter-integration-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='5e5c262877a21a6ef197562143657ae1ac5963c7'
PARENT='3f491a8ea6d79c6c6ee2f0512814d75f200075ce'
PCI='34164299907/101872170268'
CERT_BLOB='5067d1723952edce9f4bab55cc427eb1745211cc'
LOCKS={
    CB:'a55a48213f9e06346f7f500387ac812d85a7acc0',
    BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    V:'9fdec16f920104cc6c1961fb092185a0371258d5',
    BZ:'d220e1a2de3f7595e498b8987f9fa90035a1f7d9',
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

def bz_rows(buv,a:int,b:int):
    rows=buv.ae_outer(a,b)
    D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    delta=vq(D0,2); sigma=vq(Q,2); drel=delta-2*sigma
    qrows=[r for r in rows if r[-1]]
    same=[r for r in qrows if r[0]%8==r[1]%8]
    bx=[r for r in same if not(r[6]==1 and delta==2*sigma+2-r[5])]
    out=[]
    for r in bx:
        A,B,C,D,eta,e,f,mu,qok=r
        db=(D*pow(B,-1,8))%8
        if f==1 and e==1 and db==5 and drel==2: continue
        if f==1 and e==1 and db==1 and drel==3: continue
        out.append(r)
    return out

def alpha_ok(a:int,b:int,r)->bool:
    A,B,C,D,eta,e,f,mu,qok=r
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b
    for q in primes(P):
        if q!=2 and A%q==0 and legendre(-1,q)!=1:return False
    for q in primes(M):
        if q!=2 and B%q==0 and legendre(-1,q)!=1:return False
    return True

def beta_ok(a:int,b:int,r)->bool:
    A,B,C,D,eta,e,f,mu,qok=r
    D0=a*b*(a-b)*(a+b)
    for q in primes(D0):
        if q!=2 and mu%q==0 and legendre(A*B,q)!=1:return False
    return True

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bu=json.loads(BU.read_text()); bt=json.loads(BT.read_text()); ae=json.loads(AE.read_text()); vv=json.loads(V.read_text()); bz=json.loads(BZ.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1699,'promotion_head':PARENT,'promotion_ci':PCI,'consumed_pr':1696,'hostile_audit_review':5135340667}
    assert bu['route_result']['general_old_six_odd_square_taxonomy_complete'] is True
    assert bt['general_BH_elimination']['identities']==['P^2-M^2=8*D0','P^2+M^2=2*Q^2']
    assert ae['squareclass_variables']['properties'][2]=='A|rad_odd(P)'
    assert vv['odd_prime_reservoir_partition']['pairwise_odd_disjoint'] is True
    assert bz['integrated_family']['name']=='F_{Q,2,alpha}^{branch}(p)'

    sp=c['general_old_six_source_pullback']
    assert sp['exact'] is True
    assert sp['zminus_square']=='zminus^2=mu*Q^2*Yminus/(4*D0*Yplus)'
    assert sp['zplus_square']=='zplus^2=mu*Q^2*Yplus/(4*D0*Yminus)'
    assert sp['zminus_difference']=='zminus^2-mu=mu*M^2*(A-lambda^2*B*t^2)/(4*D0*Yplus)'
    assert sp['zplus_difference']=='zplus^2-mu=mu*M^2*(A+lambda^2*B*t^2)/(4*D0*Yminus)'
    # Exact algebraic sanity for the two difference identities over a rational panel.
    for a in range(1,10):
      for b in range(1,10):
        if gcd(a,b)!=1 or a==b: continue
        P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
        if not P or not M or not D0: continue
        assert P*P-M*M==8*D0 and P*P+M*M==2*Q*Q
        lam=Fraction(P,M)
        for A,B,t in [(1,1,Fraction(2,3)),(3,5,Fraction(1,2)),(7,3,Fraction(3,5))]:
            ym=Fraction(A)-B*t*t; yp=Fraction(A)+B*t*t
            if ym==0 or yp==0: continue
            assert Q*Q*ym-4*D0*yp == M*M*(Fraction(A)-lam*lam*B*t*t)
            assert Q*Q*yp-4*D0*ym == M*M*(Fraction(A)+lam*lam*B*t*t)

    af=c['alpha_selected_branch_filter']; bf=c['beta_residual_mu_branch_filter']
    assert af['branch_only_consequence']=='every selected alpha prime q dividing A or B must satisfy Legendre(-1,q)=+1'
    assert 'q congruent 1 modulo 8' in af['combine_stage36_V']
    assert af['unused_alpha_prime_excluded_by_this_argument'] is False
    assert bf['branch_only_consequence']=='Legendre(A*B,q)=+1 is necessary for every beta reservoir prime q with q|mu'
    assert 'm+1_{q|C}+1_{q|D} is odd' in bf['assignment_interpretation']

    buv=load(BUV,'stage36_bu')
    expected={(1,2):(4,4,4),(2,11):(30,20,18),(3,4):(6,6,6),(1,8):(5,4,4)}
    got={}
    for p,want in expected.items():
        rows=bz_rows(buv,*p)
        aa=[r for r in rows if alpha_ok(*p,r)]
        both=[r for r in aa if beta_ok(*p,r)]
        got[p]=(len(rows),len(aa),len(both))
        assert got[p]==want,(p,got[p],want)
    # Nonredundancy of both families at p=2/11.
    rows=bz_rows(buv,2,11)
    assert sum(alpha_ok(2,11,r) for r in rows)==20
    assert sum(beta_ok(2,11,r) for r in rows)==20
    assert sum(alpha_ok(2,11,r) and beta_ok(2,11,r) for r in rows)==18

    d=c['integrated_preflight_diagnostics']
    assert (d['p_1_over_2']['BZ_survivors'],d['p_1_over_2']['after_alpha_selected'],d['p_1_over_2']['after_beta_residual_mu'])==(4,4,4)
    assert (d['p_2_over_11']['BZ_survivors'],d['p_2_over_11']['after_alpha_selected'],d['p_2_over_11']['after_beta_residual_mu'])==(30,20,18)
    assert d['diagnostic_p_3_over_4']['after_both_CC_rows']==6
    assert d['diagnostic_p_1_over_8']['after_both_CC_rows']==4

    rr=c['route_result']; bd=c['remaining_old_six_boundary']; fw=c['scope_firewalls']
    assert rr['general_old_six_source_pullback_exact'] is True
    assert rr['new_branch_only_filter_families']==2
    assert rr['alpha_selected_filter_exact'] is True and rr['beta_residual_mu_filter_exact'] is True
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['next_leaf']=='36-09CD_FIXED_P_OLD_SIX_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    assert bd['all_CC_survivors_have_Qq_points_at_every_old_six_prime'] is False
    for k in ['CC_survivor_is_old_six_local_point','all_old_six_local_realization_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V121_36_09CC_OLD_SIX_SOURCE_PULLBACK'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cc=st['authority_frontier']['36-09CC']
    assert cc['certificate_blob_sha']==CERT_BLOB
    assert cc['GENERAL_OLD_SIX_SOURCE_PULLBACK_EXACT'] is True
    assert cc['NEW_BRANCH_ONLY_FILTER_FAMILIES']==2
    assert cc['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CD_FIXED_P_OLD_SIX_BRANCH_FILTER_INTEGRATION_PREFLIGHT'
    assert st['current']['36_09CD_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CC verified: exact old-six source pullback yields two nonredundant branch-only filter families. BZ 30->18 at p=2/11 and diagnostic 5->4 at p=1/8; no fixed-p parameter or receiver closure. CD selected.')

if __name__=='__main__': main()
