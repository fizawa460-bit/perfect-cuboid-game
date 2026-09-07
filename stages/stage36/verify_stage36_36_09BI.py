#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09BI/prime2-full-cover-congruence-preflight.json'
BH=ROOT/'stages/stage36/36-09BH/bad-place-full-cover-valuation-preflight.json'
BHV=ROOT/'stages/stage36/verify_stage36_36_09BH.py'
AD=ROOT/'stages/stage36/36-09AD/coupled-six-reservoir-factor-squareclass-parity-preflight.json'
BA=ROOT/'stages/stage36/36-09BA/ay-auxiliary-genusone-open-points-preflight.json'
BB=ROOT/'stages/stage36/36-09BB/ay-receiver-scaled-self-intersection-preflight.json'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='e758e05953df2cf8cd4ab26ac1e9d72374e99760'
BH_HEAD='9f6e7da25e70aaf86c3051e8823a4ce380fe518f'
BH_CI='34101682021/101677315243'
CERT_BLOB='ba6a705ce61b14e640b2c400d42dded60097b406'
LOCKS={BH:'76487371ed363868af18a9fa0f6f7e1367d28f27',BHV:'c6f8d064f3d2829459d74d39095671bab152580e',AD:'9d0388845955efee71d1a761ae4ee943d8b565d5',BA:'2f31c89b2760f2270fa0ea21106ef97a3ec0840b',BB:'e4b63fd500d05ff5dc704e0c08409edee5895053'}

def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p): return git('hash-object',str(p.relative_to(ROOT)))
def v2(n):
    assert n
    n=abs(n); k=0
    while n%2==0: n//=2; k+=1
    return k

def main():
    assert blob(CERT)==CERT_BLOB,(blob(CERT),CERT_BLOB)
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',BH_HEAD,'HEAD'],cwd=ROOT)
    c=json.loads(CERT.read_text()); bh=json.loads(BH.read_text()); ad=json.loads(AD.read_text()); ba=json.loads(BA.read_text()); bb=json.loads(BB.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1691,'36_09BH_exact_head':BH_HEAD,'36_09BH_exact_head_ci':BH_CI}
    assert bh['route_result']['next_leaf']=='36-09BI_PRIME2_FULL_COVER_CONGRUENCE_PREFLIGHT'
    assert ad['two_adic_parity_reduction']['complete_2adic_congruence_branch_enumeration'] is False
    assert 'e=(1+v2(D0)) mod2' in ba['AY_branch']['squareclasses']
    assert bb['AY_genusone_ratio_model']['from_coupled_conics']==['u^2-v^2=kappa*r^2','u^2+v^2=2*s^2']

    # Primitive retained p-open sanity: a,b,a-b,a+b,P,M are all nonzero.
    # The previous verifier accidentally sampled a=+/-b, where D0=0 is outside the retained open.
    for a in range(-15,16):
        for b in range(-15,16):
            if not a or not b or math.gcd(abs(a),abs(b))!=1 or a==b or a==-b: continue
            P=a*a+2*a*b-b*b; M=a*a-2*a*b-b*b; Q=a*a+b*b
            if P==0 or M==0: continue
            D0=a*b*(a-b)*(a+b)
            assert D0!=0
            sigma=1 if a%2 and b%2 else 0
            assert v2(P)==sigma and v2(M)==sigma and v2(Q)==sigma
            assert v2(D0)>=(3 if sigma else 1)

    gate=c['minus_root_valuation_gate']
    plus=c['plus_root_Q2_automatic']
    # Exhaust symbolic valuation cases over a wide delta window; formulas are affine and parity-periodic.
    for sigma,delta0 in [(0,1),(1,3)]:
        for delta in range(delta0,33):
            e=(1+delta)%2
            m=(1+delta-e)//2
            for alpha in range(3,delta+12):
                if alpha%2!=e: continue
                rho=(alpha-e)//2
                X=sigma+rho; Y=1+m; h=Y-X
                assert 2*h==delta+3-2*sigma-alpha
                survivor_by_h=(h>=2 or h==0)
                survivor_recorded=(alpha<=delta-1-2*sigma or alpha==delta+3-2*sigma)
                assert survivor_by_h==survivor_recorded
                if h==1: assert alpha==delta+1-2*sigma
                if h<0: assert alpha>delta+3-2*sigma
                g=e+m+rho-sigma
                assert 2*g==1+delta+alpha-2*sigma
                assert g>=3

    # Q2 square-unit criterion: an odd unit is a square iff it is 1 mod 8.
    for u0 in [1,3,5,7]:
        u2=(u0*u0)%8
        assert u2==1
        assert (1-4*u2)%8==5          # h=1, x-dominant: impossible
        assert (4*u2-1)%8==3          # h=-1, y-dominant: impossible
        assert (1-16*u2)%8==1         # h>=2: automatic
        assert (16*u2-1)%8==7         # h<=-2: impossible
        assert (1-64*u2)%8==1         # plus branch, g>=3: automatic

    assert gate['equivalent_survivor_valuation_condition']=='alpha <= delta-1-2*sigma OR alpha = delta+3-2*sigma'
    assert gate['excluded_near_equality']=='alpha = delta+1-2*sigma'
    assert gate['receiver_2adic_branch_shrunk'] is True
    assert plus['uniform_lower_bound']==3 and plus['new_plus_root_2adic_filter'] is False
    rr=c['route_result']
    assert rr['route_status']=='PASS_NEW_Q2_RECEIVER_VALUATION_GATE'
    assert rr['prime2_full_cover_first_valuation_layer_classified'] is True
    assert rr['equality_unit_branch_open'] is True
    assert rr['candidate_parameter_set_shrunk'] is False and rr['receiver_closed'] is False
    assert rr['next_leaf']=='36-09BJ_PRIME2_EQUAL_VALUATION_UNIT_BRANCH_PREFLIGHT'

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V97_36_09BI_PRIME2_VALUATION_GATE'
    bi=st['authority_frontier']['36-09BI']
    assert bi['certificate_blob_sha']==CERT_BLOB
    assert bi['MINUS_ROOT_Q2_VALUATION_GATE'] is True
    assert bi['PLUS_ROOT_Q2_FILTER_NEW'] is False
    assert bi['EQUALITY_UNIT_BRANCH_OPEN'] is True
    assert bi['CANDIDATE_PARAMETER_SET_SHRUNK'] is False and bi['RECEIVER_CLOSED'] is False
    assert st['current']['unit']=='36-09BI'
    assert st['current']['next_exact_leaf']=='36-09BJ_PRIME2_EQUAL_VALUATION_UNIT_BRANCH_PREFLIGHT'
    assert st['current']['36_09BJ_entry_allowed'] is True
    for key in ['candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False
    print('36-09BI verified: Q2 plus root is automatic on AY; minus root gives the exact valuation gate h>=2 or h=0, with h=1 and h<0 impossible. Equality unit branch remains open; no parameter shrink.')

if __name__=='__main__': main()
