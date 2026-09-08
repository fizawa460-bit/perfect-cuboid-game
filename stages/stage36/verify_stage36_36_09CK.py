#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CK/good-prime-and-real-place-local-integration-preflight.json'
NOTE=ROOT/'stages/stage36/36-09CK/hasse-weil-genus17-source-note.md'
CJ=ROOT/'stages/stage36/36-09CJ/fixed-p-all-bad-place-local-integration-preflight.json'
CJV=ROOT/'stages/stage36/verify_stage36_36_09CJ.py'
CI=ROOT/'stages/stage36/verify_stage36_36_09CI.py'
CHV=ROOT/'stages/stage36/verify_stage36_36_09CH.py'
CEV=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CFV=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CGV=ROOT/'stages/stage36/verify_stage36_36_09CG.py'
CCV=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='deaa08537f1e68e04e4189a51c6e02d28b2b7b13'
CJ_HEAD='6d76640e319be1af14ee7c0823311777449d3ef1'
CJ_CI='34172681275/101895889646'
CERT_BLOB='909dcb4985414fc3085818ad818f7601830dc7f6'
LOCKS={
    NOTE:'1277ee7af2b7049114ccd28a22e32831e2d0fa51',
    CJ:'bf98c1bfd468ff975755d364081d829b1f8c1233',
    CJV:'b233a9117c812022c83c5ec4d0b6857bf0af8be3',
    CI:'53655d24a59024766b6be3cba00720bed86916ad',
    CHV:'98ae4bc76749c82b4165c7a7b37d7445f42fa6dc',
    CEV:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',
    CFV:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',
    CGV:'7a210e55a5e2386fb02a59de00502a4e810b9410',
    CCV:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
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

def good_local(a:int,b:int,row,q:int,buv)->bool:
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    assert q%2==1 and (2*P*M*D0*Q)%q!=0
    A,B,C,D,eta,e,f,mu,qok=row
    assert (A*B*C*D*M)%q!=0
    L=(P*P*pow((M*M)%q,-1,q))%q
    assert L not in (0,1,q-1)
    kappa=eta*(2**e)*C; rho=(2**f)*D
    d=buv.legendre(A*B,q); k=buv.legendre(kappa*A,q); r=buv.legendre(rho*A,q)
    targets=(d,k,r,k*d,r*d)
    # Interior residues and all five finite branch residues.  At a branch
    # residue exactly one factor is zero and the other four residue
    # characters decide whether the normalization has an F_q-point above it.
    for y in range(q):
        vals=(y%q,(1-y)%q,(1+y)%q,(1-L*y)%q,(1+L*y)%q)
        if all(v==0 or buv.legendre(v,q)==targets[i] for i,v in enumerate(vals)):
            return True
    # The infinity fibre is rational exactly when the four ratios to the
    # first radicand have square leading coefficients.  Since L is a square,
    # this reduces to d=1, k=chi(-1), r=1.
    eps=buv.legendre(-1,q)
    return d==1 and k==eps and r==1

def panel(a:int,b:int,civ,cev,cfv,cgv,ccv,buv,chv):
    rows=civ.ch_rows(a,b,cev,cfv,cgv,ccv,buv,chv)
    small=[q for q in range(3,1163) if isprime(q)]
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    kept=[]; obs=[]
    for i,row in enumerate(rows):
        bad=[]
        for q in small:
            if (2*P*M*D0*Q)%q==0:continue
            if not good_local(a,b,row,q,buv):bad.append(q)
        if bad:obs.append((i,row,bad))
        else:kept.append((i,row))
    return rows,kept,obs

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items():assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CJ_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cj=json.loads(CJ.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1705,'36_09CJ_exact_green_head':CJ_HEAD,'36_09CJ_exact_head_ci':CJ_CI}
    assert cj['main_consequence']['finite_bad_place_branch_local_realization_complete'] is True
    note=NOTE.read_text()
    assert 'degree-32 (Z/2)^5-cover' in note and 'so g=17' in note
    assert 'absence of every listed F_q point is a genuine Q_q obstruction' in note
    assert 'https://stacks.math.columbia.edu/tag/0BX5' in note
    assert 'https://stacks.math.columbia.edu/tag/03QD' in note

    gm=c['good_prime_model']; lg=c['large_good_prime_route']; rp=c['real_place']
    assert gm['degree']==32 and gm['genus']==17
    assert gm['target_characters']==['d','k','r','k*d','r*d']
    assert gm['infinity_rule']=='a rational point above infinity exists iff d=+1, k=Legendre(-1,q), r=+1'
    assert gm['fq_point_equivalent_to_q_q_point'] is True
    assert lg['automatic_prime_range']=='every prime q>=1163'
    assert (1163+1)**2 > 34**2*1163
    assert (1153+1)**2 <= 34**2*1153
    assert rp['every_outer_branch_has_real_point'] is True and rp['new_real_branch_filter'] is False

    civ=load(CI,'ci'); chv=load(CHV,'ch'); cev=load(CEV,'ce'); cfv=load(CFV,'cf'); cgv=load(CGV,'cg'); ccv=load(CCV,'cc'); buv=load(BUV,'bu')
    expected={
        (1,2):(3,3,[]),
        (2,11):(5,3,[(3,[37,53,149]),(4,[37,53,149])]),
        (3,4):(3,3,[]),
        (1,8):(3,3,[]),
    }
    got={}
    for p,want in expected.items():
        rows,kept,obs=panel(*p,civ,cev,cfv,cgv,ccv,buv,chv)
        compact=[(i,bad) for i,row,bad in obs]
        got[p]=(len(rows),len(kept),compact)
        assert got[p]==want,(p,got[p],want)
    rows,kept,obs=panel(2,11,civ,cev,cfv,cgv,ccv,buv,chv)
    assert [row for i,row,bad in obs]==[(1,1,3,1,-1,0,1,429,True),(1,1,3,1,1,0,1,-429,True)]

    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['CH_survivors'],d['p_1_over_2']['after_CK_small_good_primes'])==(3,3)
    assert (d['p_2_over_11']['CH_survivors'],d['p_2_over_11']['after_CK_small_good_primes'])==(5,3)
    assert d['p_2_over_11']['good_prime_obstructed_branch_indices']==[3,4]
    assert d['p_2_over_11']['common_obstruction_primes']==[37,53,149]
    assert d['diagnostic_p_3_over_4']['after_CK_small_good_primes']==3
    assert d['diagnostic_p_1_over_8']['after_CK_small_good_primes']==3

    # Real-place sign proof is branch-uniform: A,B>0, rho>0 and sign(kappa)=eta.
    for p in expected:
        rows=civ.ch_rows(*p,cev,cfv,cgv,ccv,buv,chv)
        for A,B,C,D,eta,e,f,mu,qok in rows:
            assert A>0 and B>0 and C>0 and D>0 and (2**f)*D>0
            kappa=eta*(2**e)*C
            assert (kappa>0)==(eta==1)

    rr=c['route_result']; mc=c['main_consequence']; fw=c['scope_firewalls']
    assert rr['good_prime_and_real_place_integration_complete'] is True
    assert rr['new_point_independent_branch_filter'] is True
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['next_leaf']=='36-09CL_EVERYWHERE_LOCAL_BRANCH_GLOBAL_OBSTRUCTION_ROUTER_PREFLIGHT'
    assert mc['retained_p_2_over_11_branch_count_reduced'] is True
    for k in ['CK_survivor_is_global_receiver','CK_survivor_is_rational_point','everywhere_local_means_global','bounded_small_good_prime_scan_is_uniform_global_parameter_enumeration','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V131_36_09CK_ALL_LOCAL_PLACES_CLASSIFIED'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cjst=st['authority_frontier']['36-09CJ']
    assert cjst['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cjst['exact_head']==CJ_HEAD and cjst['exact_head_ci']==CJ_CI
    ck=st['authority_frontier']['36-09CK']
    assert ck['certificate_blob_sha']==CERT_BLOB
    assert ck['GOOD_PRIME_AND_REAL_PLACE_INTEGRATION_COMPLETE'] is True
    assert ck['NEW_GOOD_PRIME_BRANCH_FILTER'] is True
    assert ck['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09CL_EVERYWHERE_LOCAL_BRANCH_GLOBAL_OBSTRUCTION_ROUTER_PREFLIGHT'
    assert st['current']['36_09CL_entry_allowed'] is True
    assert st['current']['hostile_audit_checkpoint_reached'] is False
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CK verified: all good odd primes and the real place are classified branchwise. Small good primes prune p=2/11 CH branches 5->3 via q=37,53,149; p=1/2 remains 3. No fixed-p parameter or receiver closure; CL global-obstruction router selected.')

if __name__=='__main__':main()
