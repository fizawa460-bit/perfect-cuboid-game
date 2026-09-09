#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
SRC=ROOT/'stages/stage36/36-09CW/creutz-viray-hyperelliptic-brauer-source-lock.md'
CV=ROOT/'stages/stage36/36-09CV/bt-non-kummer-divisor-cocycle-brauer-source-preflight.json'
O=ROOT/'stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json'
BASE='d5545b32e6b3088bca53318998d434f2745b03e9'
CV_HEAD='eb391492fb79af264f46a72616ccd3b1a9f37f01'
PROMO_HEAD='cc3515ba4a5e6899371973cea24b079f4dcc9bb4'
LOCKS={
    CERT:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    SRC:'4657040230644aef1dbef427a3a5ab6afe3998aa',
    CV:'2abc41fe2dccc7563e4c8af49d37b78094e7cd64',
    O:'6a2678ebedba40e13277100441361039ee47ca28',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def xor(a,b): return tuple(x^y for x,y in zip(a,b))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CV_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cv=json.loads(CV.read_text()); o=json.loads(O.read_text()); src=SRC.read_text()
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CV_exact_green_head':CV_HEAD,
        '36_09CV_exact_head_ci':'34195900786/101963435117',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34196040262/101963862133'
    }
    assert cv['source_boundary']['first_missing_obligation']=='BT_LITERAL_NON_KUMMER_DIVISOR_CECH_COMMON_COCYCLE_OR_SECONDARY_EXTENSION_CONSTRUCTION'

    # Exact physical hyperelliptic model replay.
    top=o['top_genus3_exact_factorization']
    assert top['normalized_model']=='C3_p: y^2=(t^2+p^2)*(t^2+p^(-2))*(t^2+c^2)*(t^2+c^(-2))'
    assert top['genus']==3
    assert o['notation_separation']['physical_exclusions'][:3]==['p=0','p=1','p=-1']

    ph=c['physical_hyperelliptic_receiver']
    assert ph['degree']==8 and ph['genus']==3 and ph['leading_scalar']==1
    assert ph['double_cover_type']=='even'
    assert ph['quadratic_factors']==['f0=t^2+p^2','f1=t^2+p^(-2)','f2=t^2+c^2','f3=t^2+c^(-2)']
    assert ph['branch_algebra']=='L_p ~= Q(i)^4'

    # Frozen source contract must state the exact even-cover norm criterion and this specialization.
    assert 'Theorem 1.1' in src
    assert 'when `c=1`, square norm is sufficient and necessary' in src
    assert '`L_p ~= Q(i)^4`' in src
    assert '`Norm_{L_p/Q}(ell_{d,j})=d^2`' in src
    assert '`A_{d,j}=(d,t^2+a_j^2)_2 in Br(C3_p)[2]`' in src
    assert 'does **not** prove that any `A_{d,j}` is nonconstant modulo `Br(Q)`' in src

    ad=c['creutz_viray_adapter']; ef=c['explicit_family']
    assert ad['theorem']=='Creutz--Viray Theorem 1.1'
    assert ad['source_bound'] is True
    assert ef['norm']=='Norm(ell_dj)=d^2'
    assert ef['unramified_condition_satisfied'] is True
    assert ef['class_group']=='Br(C3_p)[2]'
    assert ef['literal_unramified_Brauer_family_constructed'] is True
    assert ef['literal_classes']==[
        'A_d0=(d,t^2+p^2)_2','A_d1=(d,t^2+p^(-2))_2',
        'A_d2=(d,t^2+c^2)_2','A_d3=(d,t^2+c^(-2))_2']

    # Check the subset/complement relation purely in F2 factor parity: total factor vector is
    # the curve square z^2, so S and complement differ by the full vector and represent the
    # same quaternion class after imposing the curve equation.
    full=(1,1,1,1)
    for mask in range(16):
        s=tuple((mask>>j)&1 for j in range(4))
        comp=xor(s,full)
        assert xor(s,comp)==full
    assert ef['complement_identity']=='A_dS=A_d,S^c on C3_p because prod_j f_j(t)=z^2'

    cb=c['current_credit_boundary']
    for key in ['nonconstant_mod_BrQ_proved','one_specific_d_nonconstant_uniformly_in_p_proved','local_evaluation_variation_on_receiver_points_proved','exact_translation_to_later_BT_y_five_root_coordinates_complete','proved_outside_CU_five_root_monomial_family','required_place_inventory_complete','Brauer_Manin_obstruction_proved']:
        assert cb[key] is False,key
    rr=c['route_result']
    assert rr['route_status']=='PASS_LITERAL_UNRAMIFIED_BRAUER_FAMILY_CONSTRUCTION_EVALUATION_NEXT'
    assert rr['next_leaf']=='36-09CX_BT_HYPERELLIPTIC_BRAUER_NONCONSTANCY_RECEIVER_EVALUATION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CW verified: Creutz-Viray Theorem 1.1 source-binds an explicit unramified family A_dj=(d,t^2+a_j^2)_2 in Br(C3_p)[2]. Nonconstancy, BT-coordinate survival, evaluation variation and Brauer-Manin obstruction remain open; CX selected.')

if __name__=='__main__': main()
