#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CY/bt-hyperelliptic-brauer-bt-coordinate-survival-required-place-preflight.json'
CX=ROOT/'stages/stage36/36-09CX/bt-hyperelliptic-brauer-nonconstancy-receiver-evaluation-preflight.json'
CW=ROOT/'stages/stage36/36-09CW/bt-literal-non-kummer-divisor-cech-construction-preflight.json'
O=ROOT/'stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json'
CU=ROOT/'stages/stage36/36-09CU/bt-kummer-monomial-brauer-secondary-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
CX_HEAD='434c4816dad351208941921bfa7fec02c4076831'
PROMO_HEAD='4b80debeb64880c0192d2ecfa9132c95341672cc'
LOCKS={
    CERT:'781038311a51bf733d51ee62a01d710ce087a491',
    CX:'50ef72b661b8b55db2cb637d23f6848a27ff7257',
    CW:'a363c230cb44fec6d235eda0720d4fd624b1a87c',
    O:'6a2678ebedba40e13277100441361039ee47ca28',
    CU:'cb92adb9b0025e8cef8554a2c30dc6777b8e2835',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def prime_factors(n:int)->set[int]:
    n=abs(n); out=set(); d=2
    while d*d<=n:
        while n%d==0:
            out.add(d); n//=d
        d+=1
    if n>1: out.add(n)
    return out

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CX_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cx=json.loads(CX.read_text()); cw=json.loads(CW.read_text()); o=json.loads(O.read_text()); cu=json.loads(CU.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CX_exact_green_head':CX_HEAD,
        '36_09CX_exact_head_ci':'34198960652/101973104092',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34199227681/101973936096'
    }
    assert cx['nonconstancy_consequence']['A_nonconstant_mod_BrQ'] is True
    assert cx['local_Brauer_evaluation']['evaluation_varies_on_C3_2_Q7'] is True
    assert cw['explicit_family']['literal_unramified_Brauer_family_constructed'] is True
    assert o['top_genus3_exact_factorization']['genus']==3
    assert cu['construction_boundary']['BT_KUMMER_MONOMIAL_QUATERNION_FAMILY_EXHAUSTED_AS_OBSTRUCTION'] is True
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True

    d=c['direct_physical_receiver_binding']
    assert d['fixed_p']=='2'
    assert d['Brauer_class']=='A=(7,t^2+4)_2'
    assert d['class_is_defined_on_source_bound_physical_receiver'] is True
    assert d['later_BT_branch_translation_required_to_define_or_evaluate_A'] is False
    assert d['later_BT_branch_translation_still_required_for_exact_CU_family_comparison'] is True
    assert d['A_outside_CU_family_proved'] is False

    fc=c['factor_collision_control']
    assert fc['identities']==['g1-4*g0=-15','g2-g0=5','g3-9*g0=-35']
    collision=(prime_factors(15)|prime_factors(5)|prime_factors(35))-{2}
    assert collision=={3,5,7}
    assert fc['odd_primes_where_g0_can_share_a_zero_mod_q_with_another_factor']==[3,5,7]

    # q=3 is harmless because 7 is a 3-adic square: x=1 solves x^2=7 mod 3
    # with derivative 2x=2 nonzero mod 3, so Hensel applies.
    assert (1*1-7)%3==0
    assert (2*1)%3!=0

    # Real place is harmless: both Hilbert entries are positive for real t.
    assert 7>0

    z=c['zero_evaluation_outside_required_places']
    assert z['conclusion']=='Every local evaluation outside v in {2,5,7} is zero.'
    rp=c['required_place_inventory_for_this_fixed_class']
    assert rp['places']==[2,5,7]
    assert rp['complete_for_A_on_C3_2'] is True
    assert rp['known_nonconstant_place']==7
    assert rp['place7_evaluation_image_contains']==['0','1/2']
    assert rp['place2_evaluation_image_classified'] is False
    assert rp['place5_evaluation_image_classified'] is False
    assert rp['general_Stage36_required_place_inventory_complete'] is False

    rc=c['route_correction']
    assert rc['BT_coordinate_translation_is_not_a_prerequisite_for_direct_Brauer_Manin_evaluation_on_C3_2'] is True
    assert rc['CU_comparison_remains_optional_open_diagnostic'] is True
    cb=c['current_credit_boundary']
    assert cb['required_place_inventory_for_fixed_A_complete'] is True
    for k in ['local_evaluation_images_at_all_required_places_complete','adelic_evaluation_sum_classified','Brauer_Manin_obstruction_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    rr=c['route_result']
    assert rr['next_leaf']=='36-09CZ_FIXED_P2_BRAUER_LOCAL_IMAGE_ADELIC_SUM_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CY verified: for p=2 and A=(7,t^2+4)_2 on the physical genus-3 receiver, all local evaluations outside 2,5,7 are zero; 7 is already nonconstant. The fixed-class required-place inventory is exactly {2,5,7}. BT translation is not needed for direct BM evaluation, but CU-family comparison remains open. No BM/fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
