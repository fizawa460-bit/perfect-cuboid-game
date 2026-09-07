#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
from math import gcd
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CB/general-q2-source-conic-realization-preflight.json'
CA=ROOT/'stages/stage36/36-09CA/general-tie-unit-source-pullback-preflight.json'
CAV=ROOT/'stages/stage36/verify_stage36_36_09CA.py'
BZ=ROOT/'stages/stage36/36-09BZ/fixed-p-alpha-pullback-filter-integration-preflight.json'
BY=ROOT/'stages/stage36/36-09BY/remaining-q2-alpha-tie-gate-parameter-pullback-preflight.json'
BYV=ROOT/'stages/stage36/verify_stage36_36_09BY.py'
BW=ROOT/'stages/stage36/36-09BW/general-aw-branch-prime2-taxonomy-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
AEV=ROOT/'stages/stage36/verify_stage36_36_09AE.py'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='af40c029a8721755b39dad13be452a2a74540c4e'
PARENT='b8e9ba3b091b9c0e350cafdaeefbfcfccc0dcfb0'
PCI='34149759346/101829367656'
CERT_BLOB='a55a48213f9e06346f7f500387ac812d85a7acc0'
LOCKS={
    CA:'db99f4dfe28754799af33f7354afa02cd8a85981',
    CAV:'3f97a3876d342fb1ae14acb03869b4ae5ce32569',
    BZ:'d220e1a2de3f7595e498b8987f9fa90035a1f7d9',
    BY:'35198e4124d154d1f07fdcd526899231842a1b43',
    BYV:'d0f64ae03ddc41b03924adf836e217a4f340d293',
    BW:'d7feb3e6b86c5c93bae999f8836840e64fbd5fb5',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    AEV:'4c2e672572984399a507ddddf296b3861a80edd5',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); assert s.loader; s.loader.exec_module(m); return m

def oddpart(n:int)->int:
    while n%2==0: n//=2
    return n

def bz_rows(byv,buv,a:int,b:int):
    counts,_=byv.pipeline(buv,a,b)
    rows=buv.ae_outer(a,b)
    P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    def v2(n):
        n=abs(n); c=0
        while n%2==0: c+=1; n//=2
        return c
    delta=v2(D0); sigma=v2(Q); d=delta-2*sigma
    q=[r for r in rows if r[-1]]
    same=[r for r in q if r[0]%8==r[1]%8]
    bx=[r for r in same if not(r[6]==1 and delta==2*sigma+2-r[5])]
    out=[]
    for r in bx:
        A,B,C,D,eta,e,f,mu,qok=r
        db=(D*pow(B,-1,8))%8
        if f==1 and e==1 and db==5 and d==2: continue
        if f==1 and e==1 and db==1 and d==3: continue
        out.append(r)
    assert len(out)==counts[-1]
    return out,delta,sigma,d

def row_q2_realizable(cav,a:int,b:int,r,delta:int,sigma:int,d:int)->bool:
    A,B,C,D,eta,e,f,mu,qok=r
    assert A%8==B%8
    if f==0:
        assert e==0
        normC=(eta*C*pow(A%8,-1,8))%8
        normD=(D*pow(A%8,-1,8))%8
        return (normC,normD) in {(1,1),(5,5),(7,1),(3,5)}
    db=(D*pow(B,-1,8))%8
    assert db in (1,5)
    if db==5:
        return e==1 and d>=3
    amin=4 if e==0 else 5
    Delta_max=d+3-amin
    if Delta_max>=3:
        return True
    g=(delta+e+f)%2
    if g!=0:
        return False
    mu0=oddpart(mu)%8
    if mu0 in (3,7):
        return True
    if mu0 in (1,5):
        P,M,D0,Q,delta2,sigma2,d2,tau,L,D0odd=cav.parameter_data(a,b)
        assert (delta2,sigma2,d2)==(delta,sigma,d)
        lhs=(eta*C*pow(B%4,-1,4))%4
        rhs=(tau*cav.odd_unit_mod4(L))%4
        return lhs==rhs
    return False

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PARENT,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); ca=json.loads(CA.read_text()); bw=json.loads(BW.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1696,'36_09CA_exact_green_head':PARENT,'36_09CA_exact_head_ci':PCI}
    assert ca['route_result']['next_leaf']=='36-09CB_GENERAL_Q2_SOURCE_CONIC_REALIZATION_PREFLIGHT'
    assert bt['AD_squareclass_reconstruction']['meaning']=='c,d exist exactly when the original receiver Fminus/Fplus square conditions hold on this AW branch'
    assert bw['remaining_same_AB_taxonomy']['mixed_e0_f0']=='both extra roots are Q2-automatic at the full-cover layer because A*B=1 and their square-leading gaps are at least 3'

    # Exact AE residue skeleton: in the post-AB mixed f=0 sector the source
    # conics have exactly the four constructive primitive parity families.
    aev=load(AEV,'stage36_ae')
    states=[]
    for A,B in itertools.product((1,7),repeat=2):
        for C,D in itertools.product((1,3,5,7),repeat=2):
            for e,f,h in itertools.product((0,1),repeat=3):
                if aev.reciprocity_consistent(A,B,C,D,e,f,h) and aev.uv_two_adic_allowed(A,B,e,f):
                    states.append((A,B,C,D,e,f,h))
    assert len(states)==128
    mixed=[]
    for A,B,C,D,e,f,h in states:
        if A!=B or f!=0: continue
        eta=1 if h==0 else -1
        assert e==0
        mixed.append(((eta*C*pow(A,-1,8))%8,(D*pow(A,-1,8))%8))
    assert set(mixed)=={(1,1),(5,5),(7,1),(3,5)}

    mc=c['mixed_f0_source_conic']; dp=c['deep_f1_source_conic']; fc=c['deep_f1_full_cover_completion']; pr=c['prime2_exact_local_result']
    assert [tuple(x['residues']) for x in mc['necessary_and_sufficient_families']]==[(1,1),(5,5),(7,1),(3,5)]
    assert mc['every_post_BZ_f0_row_has_source_Q2_point'] is True
    assert dp['source_Q2_point_for_each_allowed_alpha'] is True
    assert 'mu0=3 mod8' in fc['shallow_g0_mu3']
    assert 'mu0=7 mod8' in fc['shallow_g0_mu7']
    assert 'CA proves' in fc['shallow_g0_mu1_or5']
    assert pr['BZ_survivor_implies_Q2_full_cover_branch_point'] is True
    assert pr['does_not_imply_global_receiver'] is True
    assert pr['does_not_imply_simultaneous_points_at_other_places'] is True
    assert pr['prime2_branch_filter_layer_complete'] is True

    byv=load(BYV,'stage36_by'); buv=load(BUV,'stage36_bu'); cav=load(CAV,'stage36_ca')
    expected={(1,2):4,(2,11):30,(3,4):6,(1,8):5}
    got={}
    for p,n in expected.items():
        rows,delta,sigma,d=bz_rows(byv,buv,*p)
        assert len(rows)==n
        good=[r for r in rows if row_q2_realizable(cav,*p,r,delta,sigma,d)]
        assert len(good)==n
        got[p]=len(good)
    assert got==expected

    # Broader bounded sanity: whenever the exact AW/AE generator is admissible,
    # every BZ row falls into one of the proved constructive Q2 cases.
    checked=0
    for a in range(1,16):
        for b in range(1,16):
            if gcd(a,b)!=1 or a==b: continue
            P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; D0=a*b*(a-b)*(a+b)
            if not P or not M or not D0: continue
            try:
                rows,delta,sigma,d=bz_rows(byv,buv,a,b)
            except AssertionError:
                continue
            for r in rows:
                assert row_q2_realizable(cav,a,b,r,delta,sigma,d),(a,b,r,delta,sigma,d)
                checked+=1
    assert checked>100

    d=c['exact_fixed_p_diagnostics']
    assert (d['p_1_over_2']['BZ_survivors'],d['p_1_over_2']['Q2_realizable_BZ_survivors'])==(4,4)
    assert (d['p_2_over_11']['BZ_survivors'],d['p_2_over_11']['Q2_realizable_BZ_survivors'])==(30,30)
    assert (d['diagnostic_p_3_over_4']['BZ_survivors'],d['diagnostic_p_3_over_4']['Q2_realizable_BZ_survivors'])==(6,6)
    assert (d['diagnostic_p_1_over_8']['BZ_survivors'],d['diagnostic_p_1_over_8']['Q2_realizable_BZ_survivors'])==(5,5)

    rr=c['route_result']; fw=c['scope_firewalls']
    assert rr['mixed_f0_source_conic_realization_complete'] is True
    assert rr['deep_f1_source_conic_realization_complete'] is True
    assert rr['all_BZ_outer_survivors_have_Q2_full_cover_point'] is True
    assert rr['prime2_branch_filter_layer_complete'] is True
    assert rr['new_point_independent_branch_rows']==0
    assert rr['next_leaf']=='36-09CC_GENERAL_OLD_SIX_QQ_SOURCE_PULLBACK_PREFLIGHT'
    for k in ['Q2_local_point_is_global_receiver','Q2_local_point_implies_other_local_points','prime2_layer_complete_means_all_bad_places_complete','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V118_36_09CB_Q2_LOCAL_REALIZATION'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    cap=st['authority_frontier']['36-09CA']
    assert cap['status']=='PROVISIONAL_EXACT_GREEN_PARENT' and cap['exact_head']==PARENT and cap['exact_head_ci']==PCI
    cb=st['authority_frontier']['36-09CB']
    assert cb['certificate_blob_sha']==CERT_BLOB
    assert cb['ALL_BZ_OUTER_SURVIVORS_HAVE_Q2_FULL_COVER_POINT'] is True
    assert cb['PRIME2_BRANCH_FILTER_LAYER_COMPLETE'] is True
    assert cb['RECEIVER_CLOSED'] is False
    assert st['current']['next_exact_leaf']=='36-09CC_GENERAL_OLD_SIX_QQ_SOURCE_PULLBACK_PREFLIGHT'
    assert st['current']['36_09CC_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09CB verified: every BZ survivor admits a Q2 point on the exact general-AW full-cover local model. Prime-2 adds no further branch pruning after BZ; this is local Q2 credit only, not receiver/global closure. CC old-six Q_q pullback is selected.')

if __name__=='__main__': main()
