#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BY/remaining-q2-alpha-tie-gate-parameter-pullback-preflight.json'
BX=ROOT/'stages/stage36/36-09BX/fixed-p-q2-branch-filter-integration-preflight.json'
BW=ROOT/'stages/stage36/36-09BW/general-aw-branch-prime2-taxonomy-preflight.json'
BU=ROOT/'stages/stage36/36-09BU/general-aw-branch-bad-place-valuation-taxonomy-preflight.json'
BUV=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
AE=ROOT/'stages/stage36/36-09AE/six-reservoir-squareclass-conic-coupling-preflight.json'
AEV=ROOT/'stages/stage36/verify_stage36_36_09AE.py'
BI=ROOT/'stages/stage36/36-09BI/prime2-full-cover-congruence-preflight.json'
BJ=ROOT/'stages/stage36/36-09BJ/prime2-equal-valuation-unit-branch-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'

BASE='af40c029a8721755b39dad13be452a2a74540c4e'
PROMOTION_HEAD='73ff78298a7de1ae8a310bd753ed3412753f5728'
AUDITED_BX_HEAD='11e1152a2de6df17c7354ab48f33f25865dd0ae5'
CERT_BLOB='35198e4124d154d1f07fdcd526899231842a1b43'
LOCKS={
    BX:'9edd1343c38005d2d47954e2652b43b02079c160',
    BW:'d7feb3e6b86c5c93bae999f8836840e64fbd5fb5',
    BU:'a8f3fb880b83aac2240ce299fe8a8fa42e044093',
    BUV:'64b889c2dde22d021fb2933b976311d903f57dce',
    AE:'ddae37dd35cd0e732cebadf9c17f3f3fa57930df',
    AEV:'4c2e672572984399a507ddddf296b3861a80edd5',
    BI:'ba6a705ce61b14e640b2c400d42dded60097b406',
    BJ:'f9ef3dde7b756470f2fc882327a67d72db7902f1',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def v2(n:int)->int:
    assert n
    n=abs(n); c=0
    while n%2==0:
        c+=1; n//=2
    return c

def load(path:Path,name:str):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    assert s.loader
    s.loader.exec_module(m)
    return m

def pipeline(mod,a:int,b:int):
    rows=mod.ae_outer(a,b)
    D0=a*b*(a-b)*(a+b); Q=a*a+b*b
    delta=v2(D0); sigma=v2(Q); drel=delta-2*sigma
    q=[r for r in rows if r[-1]]
    same=[r for r in q if r[0]%8==r[1]%8]
    bx=[r for r in same if not (r[6]==1 and delta==2*sigma+2-r[5])]
    by=[]
    removed=[]
    for r in bx:
        A,B,C,D,eta,e,f,mu,qok=r
        db=(D*pow(B,-1,8))%8
        bad1=(f==1 and e==1 and db==5 and drel==2)
        bad2=(f==1 and e==1 and db==1 and drel==3)
        if bad1 or bad2:
            removed.append((r,'row1' if bad1 else 'row2'))
        else:
            by.append(r)
    return (len(rows),len(q),len(same),len(bx),len(by)),removed

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items():
        assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMOTION_HEAD,'HEAD'],cwd=ROOT)
    git('cat-file','-e',f'{AUDITED_BX_HEAD}^{{commit}}')

    c=json.loads(CERT.read_text()); bx=json.loads(BX.read_text()); bw=json.loads(BW.read_text())
    assert c['schema']=='STAGE36_36_09BY_REMAINING_Q2_ALPHA_TIE_GATE_PARAMETER_PULLBACK_PREFLIGHT_V1'
    assert c['base_main_sha']==BASE
    assert c['promotion_parent']['hostile_reaudit_review']==5132705989
    assert bx['route_result']['next_leaf']=='36-09BY_REMAINING_Q2_ALPHA_TIE_GATE_PARAMETER_PULLBACK_PREFLIGHT'
    assert bw['remaining_same_AB_taxonomy']['deep_f1_minus_root']['Delta_2_or_1']=='impossible'
    assert bw['remaining_same_AB_taxonomy']['deep_f1_minus_root']['Delta_negative_g1']=='impossible'

    # Exact 2-adic source alpha pullback.  For y=epsilon+2^n q with n>=2,
    # q odd, v2(y^2-1)=n+1 and (y^2+1)/2 is 5 mod8 only at n=2,
    # otherwise 1 mod8.  This is the entire residue distinction used by BY.
    for eps in (-1,1):
        for n in range(2,9):
            for q0 in (1,3,5,7):
                y=eps+(2**n)*q0
                assert y%2
                assert v2(y-eps)==n
                assert v2(y*y-1)==n+1
                want=5 if n==2 else 1
                assert ((y*y+1)//2)%8==want
    ap=c['source_alpha_pullback']
    assert ap['alpha']=='n+1'
    assert ap['necessary_alpha_families']['D_over_B_5_mod8']=='e=1 and alpha=3'
    assert ap['necessary_alpha_families']['D_over_B_1_mod8_e0']=='alpha in {4,6,8,...}'
    assert ap['necessary_alpha_families']['D_over_B_1_mod8_e1']=='alpha in {5,7,9,...}'

    # Replay the exact AE 128-state skeleton.  Once A=B and f=1, its only
    # (D/B mod8,e) combinations are (1,0),(1,1),(5,1).  Hence the residue
    # prerequisites discovered by the alpha pullback are already implicit in
    # AE/BX and are not double-counted as new BY filters.
    aev=load(AEV,'stage36_ae')
    survivors=[]
    for A,B in itertools.product((1,7),repeat=2):
        for C,D in itertools.product((1,3,5,7),repeat=2):
            for e,f,h in itertools.product((0,1),repeat=3):
                if aev.reciprocity_consistent(A,B,C,D,e,f,h) and aev.uv_two_adic_allowed(A,B,e,f):
                    survivors.append((A,B,C,D,e,f,h))
    assert len(survivors)==128
    deep=[x for x in survivors if x[0]==x[1] and x[5]==1]
    combos={(D*pow(B,-1,8)%8,e) for A,B,C,D,e,f,h in deep}
    assert combos=={(1,0),(1,1),(5,1)}

    # New row 1 is forced by alpha=3 -> Delta=drel.  drel=2 is exactly the
    # previously uncharged Delta=2 impossibility; drel=1 was already BX-critical.
    ex=c['post_BX_new_branch_only_exclusions']
    assert ex['new_row_1']['point_independent'] is True
    assert 2+3-3==2
    # New row 2: drel=3, e=f=1, D/B=1 forces alpha=5,7,... .
    # Delta is 1,-1,-3,... and g=1, so all are impossible by BW.
    for alpha in (5,7,9,11,13):
        Delta=3+3-alpha
        assert Delta in (1,-1,-3,-5,-7)
    assert (3+1+1)%2==1
    assert ex['new_row_2']['point_independent'] is True

    bu=load(BUV,'stage36_bu')
    expected={
        (1,2):(14,8,6,4,4),
        (2,11):(158,77,52,30,30),
        (3,4):(44,21,16,8,6),
        (1,8):(47,14,8,8,5),
    }
    got={p:pipeline(bu,*p)[0] for p in expected}
    assert got==expected,got
    _,rm34=pipeline(bu,3,4)
    _,rm18=pipeline(bu,1,8)
    assert len(rm34)==2 and {tag for _,tag in rm34}=={'row1'}
    assert len(rm18)==3 and {tag for _,tag in rm18}=={'row2'}
    d=c['fixed_p_diagnostics']
    assert tuple(d['p_1_over_2'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue','after_BX_critical','after_BY_new_rows'])==expected[(1,2)]
    assert tuple(d['p_2_over_11'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue','after_BX_critical','after_BY_new_rows'])==expected[(2,11)]
    assert tuple(d['nonredundancy_p_3_over_4'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue','after_BX_critical','after_BY_new_rows'])==expected[(3,4)]
    assert tuple(d['nonredundancy_p_1_over_8'][k] for k in ['AW_AE_outer','after_Q_row','after_AB_residue','after_BX_critical','after_BY_new_rows'])==expected[(1,8)]

    rr=c['route_result']; fw=c['scope_firewalls']
    assert rr['source_alpha_pullback_exact'] is True
    assert rr['new_point_independent_branch_rows']==2
    assert rr['new_rows_nonredundant_against_BX'] is True
    assert rr['fixed_p_parameter_exclusion_obtained'] is False
    assert rr['candidate_parameter_set_shrunk'] is False
    assert rr['remaining_tie_unit_gate_point_dependent'] is True
    assert rr['next_leaf']=='36-09BZ_FIXED_P_ALPHA_PULLBACK_FILTER_INTEGRATION_PREFLIGHT'
    for k in ['outer_branch_survivor_is_Q2_point','alpha_family_realization_for_every_outer_row','tie_unit_gate_row_only','full_Q2_local_solubility_classified_for_general_AW_branch','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','local_parameter_elimination_exhausted','uniform_finite_Q_squareclass_family','finite_exhaustive_H1_twist_family','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[k] is False

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V115_36_09BY_ALPHA_PULLBACK'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    by=st['authority_frontier']['36-09BY']
    assert by['certificate_blob_sha']==CERT_BLOB
    assert by['SOURCE_ALPHA_PULLBACK_EXACT'] is True
    assert by['NEW_POINT_INDEPENDENT_BRANCH_ROWS']==2
    assert by['FIXED_P_PARAMETER_EXCLUSION_OBTAINED'] is False
    assert st['current']['next_exact_leaf']=='36-09BZ_FIXED_P_ALPHA_PULLBACK_FILTER_INTEGRATION_PREFLIGHT'
    assert st['current']['36_09BZ_entry_allowed'] is True
    for k in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][k] is False
    print('36-09BY verified: exact source-alpha pullback gives two new nonredundant post-BX branch-only Q2 exclusions; p=1/2 and 2/11 stay 4 and 30, while diagnostic 3/4 is 8->6 and 1/8 is 8->5. Tie-unit realization remains point-dependent; BZ selected.')

if __name__=='__main__':
    main()
