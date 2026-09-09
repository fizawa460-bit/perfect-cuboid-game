#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CZ/fixed-p2-brauer-local-image-adelic-sum-preflight.json'
CY=ROOT/'stages/stage36/36-09CY/bt-hyperelliptic-brauer-bt-coordinate-survival-required-place-preflight.json'
CX=ROOT/'stages/stage36/36-09CX/bt-hyperelliptic-brauer-nonconstancy-receiver-evaluation-preflight.json'
BASE='f2a89e613cdf91191a0aada9e90c9fc93373a6c6'
CY_HEAD='91f29d0081ed2e82399af1578f14d5851baf87d9'
PROMO_HEAD='f59d967f00763f45b6ef92593e38614b4fff12be'
LOCKS={
    CERT:'dc0e80444707e57ce9ddb41fe76682a76e65f760',
    CY:'781038311a51bf733d51ee62a01d710ce087a491',
    CX:'50ef72b661b8b55db2cb637d23f6848a27ff7257',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def rhs(t:Fraction)->Fraction:
    return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def mod_frac(x:Fraction,p:int)->int:
    return (x.numerator%p)*pow(x.denominator%p,-1,p)%p

def hilbert_odd_units_2(a:int,b:int)->int:
    assert a%2 and b%2
    exponent=(((a-1)//2)*((b-1)//2))&1
    return -1 if exponent else 1

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CY_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cy=json.loads(CY.read_text()); cx=json.loads(CX.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CY_exact_green_head':CY_HEAD,
        '36_09CY_exact_head_ci':'34199600232/101975129036',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34199771204/101975667031'
    }
    assert cy['required_place_inventory_for_this_fixed_class']['places']==[2,5,7]
    assert cy['required_place_inventory_for_this_fixed_class']['complete_for_A_on_C3_2'] is True
    assert cx['local_Brauer_evaluation']['P2_Hilbert_symbol']==1
    assert cx['local_Brauer_evaluation']['P3_Hilbert_symbol']==-1

    # v=2 zero-evaluation witness: t=3.
    r2=rhs(Fraction(3))
    assert r2==19721
    assert r2.denominator==1 and r2.numerator%8==1  # odd 2-adic unit square criterion
    assert hilbert_odd_units_2(7,13)==1

    # v=5 zero-evaluation witness: t=2.
    r5=rhs(Fraction(2))
    assert r5==Fraction(16354,9)
    assert mod_frac(r5,5)==1
    assert (1*1-mod_frac(r5,5))%5==0
    assert 2%5!=0
    # At odd p, a pair of p-adic units has Hilbert symbol +1.
    assert 7%5!=0 and 8%5!=0

    # v=7 zero witness is the exact CX P2 witness.
    assert cx['local_receiver_points']['P2']['t']=='2'
    assert cx['local_receiver_points']['P2']['Q7_point_exists'] is True
    assert cx['local_Brauer_evaluation']['P2_Hilbert_symbol']==1

    w=c['required_place_zero_witnesses']
    assert w['v2']['rhs_exact']=='19721' and w['v2']['Hilbert_symbol']=='(7,13)_2=+1'
    assert w['v5']['rhs_exact']=='16354/9' and w['v5']['Q5_point_exists'] is True
    assert w['v7']['Q7_point_exists'] is True
    assert w['zero_evaluation_point_exists_at_every_required_place'] is True

    ad=c['adelic_consequence']
    assert ad['zero_in_selected_class_adelic_sum_image_conditional_on_adelic_solubility'] is True
    assert ad['selected_class_A_can_be_the_sole_Brauer_Manin_obstruction'] is False
    assert ad['does_not_prove_C3_2_adelic_points_exist'] is True
    assert ad['does_not_rule_out_local_obstruction_for_p2'] is True
    assert ad['does_not_rule_out_obstruction_from_additional_independent_Brauer_classes'] is True

    li=c['local_image_status']
    assert li['v7_exact_image']==['0','1/2']
    assert li['v2_image_contains']==['0'] and li['v5_image_contains']==['0']
    assert li['v2_full_image_classified'] is False and li['v5_full_image_classified'] is False
    assert li['full_images_not_needed_for_selected_class_no_go'] is True

    cb=c['current_credit_boundary']
    assert cb['selected_class_A_Brauer_Manin_obstruction_disproved_conditional_on_adelic_solubility'] is True
    for k in ['Brauer_Manin_obstruction_from_full_Br_group_proved','p2_local_solubility_all_places_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
        assert cb[k] is False,k
    rr=c['route_result']
    assert rr['next_leaf']=='36-09DA_FIXED_P2_SECOND_INDEPENDENT_BRAUER_CLASS_EVALUATION_MATRIX_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CZ verified: A=(7,t^2+4)_2 has explicit invariant-zero receiver points at every required place 2,5,7, while all other places evaluate zero. Hence whenever C3_2 has an adelic point, an A-orthogonal adelic point exists; this selected nonconstant class cannot be the sole Brauer-Manin obstruction. Additional independent classes or a local obstruction are required. No fixed-p/receiver/endpoint credit.')

if __name__=='__main__': main()
