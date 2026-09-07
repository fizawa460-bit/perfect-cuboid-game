#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BN/old-six-tie-normalized-unit-residue-preflight.json'
BM=ROOT/'stages/stage36/36-09BM/old-six-full-cover-degenerate-cancellation-residue-preflight.json'
BMV=ROOT/'stages/stage36/verify_stage36_36_09BM.py'
BL=ROOT/'stages/stage36/36-09BL/old-six-higher-qadic-hensel-reduction-preflight.json'
BK=ROOT/'stages/stage36/36-09BK/prime2-unit-gate-pullback-parameter-separation-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BM_HEAD='b8c1c6ed972ff48149a0ed417c7c027f29d69c37'
BM_CI='34107704490/101696432668'
CERT_BLOB='c64ad051bb1466aa05dfb0cf638b9e7759766ed9'
LOCKS={BM:'4fae43a7ebc9022acb4283a40f6eb95cb88d2aa5',BMV:'c1fc8f05d87f1afbbe17a493e00bba9d917e0beb',BL:'4d858793827216b2109b81c6a7fb9eaa83b7eaa7',BK:'0f264dfa584d41e2cf39578a1b61c80ecfc0aec1'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def vq_int(n:int,q:int)->int:
    assert n
    n=abs(n); k=0
    while n%q==0: n//=q; k+=1
    return k
def vq(x:Fraction,q:int)->int:
    return vq_int(x.numerator,q)-vq_int(x.denominator,q)
def legendre_unit(x:Fraction,q:int)->int:
    vn=vq_int(x.numerator,q); vd=vq_int(x.denominator,q)
    a=(x.numerator//(q**vn))%q; b=(x.denominator//(q**vd))%q
    u=a*pow(b,-1,q)%q
    return 1 if pow(u,(q-1)//2,q)==1 else -1
def q_square(x:Fraction,q:int)->bool:
    if x==0: return True
    vv=vq(x,q)
    return vv%2==0 and legendre_unit(x,q)==1

def tie_criterion_integer(z:int,q:int)->bool:
    assert math.gcd(z,q)==1
    zm=z%q
    if zm not in (1,q-1):
        return legendre_unit(Fraction(z*z-1),q)==1
    eps=1 if zm==1 else -1
    n=vq_int(z-eps,q)
    c=(z-eps)//(q**n)
    return n%2==0 and (1 if pow((2*eps*c)%q,(q-1)//2,q)==1 else -1)==1

def point_data(u:int,v:int):
    a,b=1,2; D0=-6; P=1; M=-7; Q=5; kappa=-3
    aym=Fraction(u*u-v*v,kappa); ayp=Fraction(u*u+v*v,2)
    gm=Fraction(M*M*u*u-P*P*v*v,kappa)
    gp=Fraction(M*M*u*u+P*P*v*v,2)
    T2=Fraction(2*D0,kappa)
    zm2=Fraction(Q*Q)*aym/(4*T2*ayp)
    zp2=Fraction(Q*Q)*ayp/(kappa*kappa*T2*aym)
    return aym,ayp,gm,gp,zm2-1,zp2-1

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BM_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bm=json.loads(BM.read_text()); bl=json.loads(BL.read_text()); bk=json.loads(BK.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BM_exact_head':BM_HEAD,'36_09BM_exact_head_ci':BM_CI}
    assert bm['route_result']['next_leaf']=='36-09BN_OLD_SIX_TIE_BRANCH_NORMALIZED_UNIT_RESIDUE_PREFLIGHT'
    assert bm['exact_progress']['tie_branches_isolated'] is True
    assert bl['odd_Qq_square_criterion']['higher_digit_square_root_obstruction'] is False
    assert bk['exact_conclusion']['prime2_gate_is_parameter_only_predicate'] is False

    t=c['universal_tie_reduction']; crit=c['complete_odd_q_unit_criterion']
    assert t['x_y_z_are_q_units'] is True
    assert 'z^2-1' in t['Gminus_tie'] and 'z^2-1' in t['Gplus_tie']
    assert crit['odd_n']=='impossible because the valuation of z^2-1 is odd'
    # Exhaust the exact odd-q criterion on many integral unit representatives.
    for q in (3,5,7,11,13):
        for z in range(-200,201):
            if math.gcd(z,q)!=1 or z in (-1,1): continue
            actual=q_square(Fraction(z*z-1),q)
            expected=tie_criterion_integer(z,q)
            assert actual==expected,(q,z,actual,expected)

    inst=c['old_six_tie_instantiation']
    assert inst['all_old_six_tie_species_covered'] is True
    assert 'double tie' in inst['alpha_P_or_M']
    assert 'Gminus uses the criterion' in inst['beta_m_odd']
    assert 'Gminus uses the criterion' in inst['beta_m_even_R_branch']
    assert 'Gplus uses the criterion' in inst['beta_m_even_S_branch']

    # Exact same-parameter p=1/2 separation witnesses.
    lam=Fraction(-1,7)
    for q,u,v,should_pass in [(7,1,49,True),(7,1,14,False),(3,1,20,True),(3,1,2,False)]:
        tval=Fraction(v,u)
        assert tval not in (0,1,-1) and lam*tval not in (1,-1)
        aym,ayp,gm,gp,zm1,zp1=point_data(u,v)
        assert q_square(aym,q) and q_square(ayp,q)
        actual=q_square(gm,q) and q_square(gp,q)
        assert actual is should_pass
        if q==7 and v==49:
            assert (aym,ayp,gm,gp,zm1,zp1)==(Fraction(800),Fraction(1201),Fraction(784),Fraction(1225),Fraction(49,1201),Fraction(49,1152))
        if q==7 and v==14:
            assert (aym,ayp,gm,gp,zm1,zp1)==(Fraction(65),Fraction(197,2),Fraction(49),Fraction(245,2),Fraction(49,1576),Fraction(49,936))
            assert vq(zp1,7)==2 and legendre_unit(zp1,7)==-1
        if q==3 and v==20:
            assert (aym,ayp,gm,gp,zm1)==(Fraction(133),Fraction(401,2),Fraction(117),Fraction(449,2),Fraction(117,3208))
            assert vq(zm1,3)==2 and legendre_unit(zm1,3)==1
        if q==3 and v==2:
            assert (aym,ayp,gm,gp,zm1)==(Fraction(1),Fraction(5,2),Fraction(-15),Fraction(53,2),Fraction(-3,8))
            assert vq(zm1,3)==1

    interp=c['interpretation']; rr=c['route_result']
    assert interp['all_old_six_tie_residues_classified'] is True
    assert interp['old_six_odd_local_square_criteria_complete'] is True
    assert interp['old_six_parameter_only_filter_from_local_square_tests'] is False
    assert interp['receiver_point_local_gates_retained'] is True
    assert interp['candidate_parameter_set_shrunk'] is False and interp['receiver_closed'] is False
    assert rr['route_status']=='PASS_COMPLETE_OLD_SIX_TIE_CRITERION_PARAMETER_ONLY_LOCAL_FILTER_BLOCKED'
    assert rr['old_six_bad_place_local_layer_complete'] is True
    assert rr['next_leaf']=='36-09BO_Q_RESERVOIR_FULL_QQ_CANCELLATION_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V102_36_09BN_OLD_SIX_TIE_COMPLETE'
    bn=st['authority_frontier']['36-09BN']
    assert bn['certificate_blob_sha']==CERT_BLOB
    assert bn['ALL_OLD_SIX_TIE_RESIDUES_CLASSIFIED'] is True
    assert bn['OLD_SIX_PARAMETER_ONLY_LOCAL_FILTER'] is False
    assert bn['RECEIVER_POINT_LOCAL_GATES_RETAINED'] is True
    assert bn['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bn['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BN'
    assert st['current']['next_exact_leaf']=='36-09BO_Q_RESERVOIR_FULL_QQ_CANCELLATION_PREFLIGHT'
    assert st['current']['36_09BO_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BN verified: every old-six odd tie branch reduces to an exact z^2-1 Q_q-square criterion; fixed p=1/2 has pass/fail tie branches in alpha and beta sectors. Old-six parameter-only local filter is blocked; Q-reservoir selected next.')

if __name__=='__main__': main()
