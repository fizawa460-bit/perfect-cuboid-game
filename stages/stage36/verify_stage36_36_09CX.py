#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CX/bt-hyperelliptic-brauer-nonconstancy-receiver-evaluation-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
SRC=ROOT/'stages/stage36/36-09CW/creutz-viray-hyperelliptic-brauer-source-lock.md'
O=ROOT/'stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
CW_HEAD='8211470f1739b1ca936cf75079e452510cdf89f7'
PROMO_HEAD='9233473d850ab16feb491be5b3d68fb85566a78a'
LOCKS={
    CERT:'50ef72b661b8b55db2cb637d23f6848a27ff7257',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    SRC:'4657040230644aef1dbef427a3a5ab6afe3998aa',
    O:'6a2678ebedba40e13277100441361039ee47ca28',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def mod_frac(x:Fraction,p:int)->int:
    return (x.numerator % p)*pow(x.denominator % p,-1,p)%p

def legendre(a:int,p:int)->int:
    a%=p
    if a==0: return 0
    v=pow(a,(p-1)//2,p)
    return 1 if v==1 else -1

def rhs(t:Fraction)->Fraction:
    return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def factor_residues(t:Fraction)->list[int]:
    return [mod_frac(t*t+4,7),mod_frac(t*t+Fraction(1,4),7),mod_frac(t*t+9,7),mod_frac(t*t+Fraction(1,9),7)]

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CW_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cw=json.loads(CW.read_text()); o=json.loads(O.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CW_exact_green_head':CW_HEAD,
        '36_09CW_exact_head_ci':'34196500765/101965293728',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34198678285/101972205853'
    }
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert 'A_d0=(d,t^2+p^2)_2' in cw['explicit_family']['literal_classes']
    assert o['top_genus3_exact_factorization']['normalized_model']=='C3_p: y^2=(t^2+p^2)*(t^2+p^(-2))*(t^2+c^2)*(t^2+c^(-2))'

    fc=c['fixed_candidate']
    assert fc['base_parameter_p']=='2' and fc['c_p']=='3'
    assert fc['Brauer_class']=='A=(7,t^2+4)_2'
    assert fc['unramified_on_C3_2'] is True

    expected={
        2:{'rhs':Fraction(16354,9),'factors':[1,6,6,1],'rhsmod':1,'z':1,'deriv':2,'hilbert':1},
        3:{'rhs':Fraction(19721,1),'factors':[6,4,4,6],'rhsmod':2,'z':3,'deriv':6,'hilbert':-1},
    }
    for t,e in expected.items():
        T=Fraction(t)
        r=rhs(T)
        assert r==e['rhs']
        assert factor_residues(T)==e['factors']
        assert mod_frac(r,7)==e['rhsmod']
        assert (e['z']*e['z']-e['rhsmod'])%7==0
        assert (2*e['z'])%7==e['deriv'] and e['deriv']!=0
        assert all(v!=0 for v in e['factors'])
        b=mod_frac(T*T+4,7)
        assert legendre(b,7)==e['hilbert']

    lp=c['local_receiver_points']
    assert lp['P2']['rhs_exact']=='16354/9' and lp['P2']['Q7_point_exists'] is True
    assert lp['P3']['rhs_exact']=='19721' and lp['P3']['Q7_point_exists'] is True
    assert lp['P2']['nonboundary'] is True and lp['P3']['nonboundary'] is True

    ev=c['local_Brauer_evaluation']
    assert ev['P2_Hilbert_symbol']==1
    assert ev['P3_Hilbert_symbol']==-1
    assert ev['evaluation_varies_on_C3_2_Q7'] is True
    nc=c['nonconstancy_consequence']
    assert nc['constant_BrQ_class_has_constant_evaluation_on_fixed_local_curve'] is True
    assert nc['A_nonconstant_mod_BrQ'] is True
    assert nc['BT_BRAUER_CLASS_NONCONSTANT_MOD_CONSTANTS_PROVED_FOR_FIXED_BRANCH_P2'] is True
    assert nc['BT_BRAUER_CLASS_WITH_POINT_DEPENDENT_RECEIVER_EVALUATION_FOUND_FOR_FIXED_BRANCH_P2'] is True

    cb=c['current_credit_boundary']
    for k in ['uniform_in_p_nonconstancy_proved','exact_translation_to_later_BT_y_five_root_coordinates_complete','proved_outside_CU_five_root_monomial_family','required_place_inventory_for_A_complete','adelic_evaluation_image_classified','Brauer_Manin_obstruction_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    rr=c['route_result']
    assert rr['next_leaf']=='36-09CY_BT_HYPERELLIPTIC_BRAUER_BT_COORDINATE_SURVIVAL_REQUIRED_PLACE_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CX verified: on C3_2(Q_7), A=(7,t^2+4)_2 evaluates +1 at a Hensel lift with t=2 and -1 at one with t=3. Hence A is nonconstant modulo Br(Q) and has point-dependent receiver-local evaluation for fixed p=2. No Brauer-Manin/fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
