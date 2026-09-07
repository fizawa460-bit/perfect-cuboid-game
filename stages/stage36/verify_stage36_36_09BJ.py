#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BJ/prime2-equal-valuation-unit-branch-preflight.json'
BI=ROOT/'stages/stage36/36-09BI/prime2-full-cover-congruence-preflight.json'
BIV=ROOT/'stages/stage36/verify_stage36_36_09BI.py'
BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BI_HEAD='090276d2752d6cd4b290128e66df724f73ac1b73'
BI_CI='34104344303/101685789266'
CERT_BLOB='f9ef3dde7b756470f2fc882327a67d72db7902f1'
LOCKS={BI:'ba6a705ce61b14e640b2c400d42dded60097b406',BIV:'acc439a5a19d9886dfc7559fe29a0cd1dbf13787',BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
    assert n
    n=abs(n); k=0
    while n%2==0: n//=2; k+=1
    return k

def q2_square_int(n:int)->bool:
    if n==0: return True
    s=-1 if n<0 else 1
    if s<0: return False
    vv=v2(n)
    u=(n>>vv)%8
    return vv%2==0 and u==1

def criterion(eps:int,n:int,q:int)->bool:
    assert eps in (-1,1) and n>=2 and q%2
    if n%2==0: return False
    if n==3: return (eps*q)%8==5
    return (eps*q)%8==1

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BI_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bi=json.loads(BI.read_text()); bh=json.loads(BH.read_text()); bb=json.loads(BB.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BI_exact_head':BI_HEAD,'36_09BI_exact_head_ci':BI_CI}
    assert bi['route_result']['next_leaf']=='36-09BJ_PRIME2_EQUAL_VALUATION_UNIT_BRANCH_PREFLIGHT'
    assert bi['route_result']['equality_unit_branch_open'] is True
    assert bh['route_result']['odd_bad_support_classified_to_seven_reservoirs'] is True
    assert bb['receiver_restricted_intersection']['S34_W03_exact_joint_system_materialized'] is True

    eq=c['equality_branch_input']; crit=c['complete_Q2_unit_criterion']; cong=c['congruence_form']
    assert eq['BI_condition']=='h=0, equivalently alpha=delta+3-2*sigma'
    assert eq['minus_root_equivalence']=='the h=0 minus root exists over Q2 iff z^2-1 is a Q2-square'
    assert eq['source_variable_square']=='z^2=Qsum^2*(u^2-v^2)/(4*D0*(u^2+v^2))'
    assert crit['n_equal_3']=='epsilon*q=5 mod8'
    assert crit['n_at_least_5_odd']=='epsilon*q=1 mod8'

    # Exact factorization and square criterion. q mod 8 is the only unit datum needed;
    # for n>=5 the second unit factor is identically 1 mod 8.
    for eps in (-1,1):
        for n in range(2,16):
            for q in (1,3,5,7):
                z=eps+(1<<n)*q
                assert z%4==eps%4
                assert v2(z-eps)==n
                lhs=z*z-1
                rhs=(1<<(n+1))*eps*q*(1+eps*(1<<(n-1))*q)
                assert lhs==rhs
                actual=q2_square_int(lhs)
                expected=criterion(eps,n,q)
                assert actual==expected,(eps,n,q,z,lhs,actual,expected)
                if n%2==0: assert actual is False
                if n==3: assert actual==((eps*q)%8==5)
                if n>=5 and n%2: assert actual==((eps*q)%8==1)

    # Recorded congruence representatives really survive.
    for z in (23,-23,33,-33,129,-129):
        assert q2_square_int(z*z-1)
    assert 23%64==23 and (-23)%64==41
    assert 33%256==33 and (-33)%256==223
    assert 129%1024==129 and (-129)%1024==895
    assert cong['surviving_unit_branches_nonempty'] is True

    rr=c['route_result']
    assert rr['route_status']=='PASS_COMPLETE_Q2_EQUAL_VALUATION_UNIT_CRITERION'
    assert rr['prime2_equal_valuation_branch_classified'] is True
    assert rr['prime2_full_cover_local_gate_complete_at_valuation_and_unit_layers'] is True
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09BK_PRIME2_UNIT_GATE_PULLBACK_TO_PARAMETER_RESIDUES_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V98_36_09BJ_Q2_EQUAL_UNIT_CRITERION'
    bj=st['authority_frontier']['36-09BJ']
    assert bj['certificate_blob_sha']==CERT_BLOB
    assert bj['EQUALITY_UNIT_BRANCH_COMPLETELY_CLASSIFIED'] is True
    assert bj['UNIVERSAL_Q2_CONTRADICTION'] is False
    assert bj['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bj['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BJ'
    assert st['current']['next_exact_leaf']=='36-09BK_PRIME2_UNIT_GATE_PULLBACK_TO_PARAMETER_RESIDUES_PREFLIGHT'
    assert st['current']['36_09BK_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BJ verified: h=0 is completely classified by z^2-1 in Q2^2; surviving unit neighborhoods are nonempty, no universal Q2 contradiction and no parameter shrink. BK pullback selected next.')

if __name__=='__main__': main()
