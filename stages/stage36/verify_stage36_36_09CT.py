#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CT/bt-pointwise-local-tate-pairing-required-place-preflight.json'
CS=ROOT/'stages/stage36/36-09CS/bt-five-root-deck-dual-projection-construction-preflight.json'
CSV=ROOT/'stages/stage36/verify_stage36_36_09CS.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
CQ=ROOT/'stages/stage36/36-09CQ/bt-cartier-dual-local-condition-adapter-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BASE='d5545b32e6b3088bca53318998d434f2745b03e9'
CS_HEAD='b1b88082b018edb4d9b22157943c7dd8b289b277'
LOCKS={
    CERT:'923ff0bfa93997bc935f280b274143377aafedde',
    CS:'4657613348e8c59630ff8bcd660e518ed491f7c9',
    CSV:'b9f5ec9caea93940c53165280ad99901e4280911',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    CQ:'c7042cc86ff94cf94db88c8cc65ce5b69441aabe',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def proj(a:tuple[int,int,int,int,int])->tuple[int,int,int]:
    a0,a1,a2,a3,a4=a
    return a0^a3^a4,a1^a3,a2^a4

def dot(a,b)->int:
    return sum(x*y for x,y in zip(a,b))&1

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CS_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cs=json.loads(CS.read_text()); cm=json.loads(CM.read_text()); cq=json.loads(CQ.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CS_exact_green_head':CS_HEAD,
        '36_09CS_exact_head_ci':'34192357445/101952828878',
        'promotion_replay_ci':'34192481550/101953195838'
    }
    assert cs['construction_boundary']['BT_geometry_bound_dual_evaluation_adapter_complete'] is True
    assert cs['construction_boundary']['new_global_obstruction_obtained'] is False
    assert cs['pointwise_five_kummer_class']['if_y_v_lifts_to_full_cover']=='all five F_i(y_v) are squares, hence Delta5_v(y_v)=0'
    assert cm['exact_BT_cover_adapter']['equivalent_to_BT_normalized_four_square_model_on_retained_open'] is True
    assert cm['exact_BT_cover_adapter']['change_of_variables']=={
        'w0':'B*t','w1':'R','w2':'S','w3':'Zminus/A','w4':'Zplus/A'
    }
    assert cm['exact_BT_cover_adapter']['five_equations']==[
        'w0^2=(A*B)*y','w1^2=(kappa*A)*(1-y)','w2^2=(rho*A)*(1+y)',
        'w3^2=(kappa*B)*(1-L*y)','w4^2=(rho*B)*(1+L*y)']
    assert cq['local_tate_pairing']['coordinate_formula_multiplicative']=='<Xi_BT,Psi>_v=(A*B,u0)_v*(kappa*A,u1)_v*(rho*A,u2)_v'
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True

    rl=c['receiver_local_lift_locus']
    assert rl['all_five_Fi_are_local_squares_on_receiver_lift_locus'] is True
    assert rl['five_equations']==[
        'w0^2=F0(y)=(A*B)*y','w1^2=F1(y)=(kappa*A)*(1-y)',
        'w2^2=F2(y)=(rho*A)*(1+y)','w3^2=F3(y)=(kappa*B)*(1-L*y)',
        'w4^2=F4(y)=(rho*B)*(1+L*y)']

    # On an actual lift, each of the five Kummer squareclass bits is zero.
    zero5=(0,0,0,0,0)
    assert proj(zero5)==(0,0,0)
    # The right dual class is neutral, so the mod-2 pairing is zero for every left class.
    for n in range(8):
        left=tuple((n>>j)&1 for j in range(3))
        assert dot(left,proj(zero5))==0

    cr=c['cs_class_restriction']
    assert cr['Delta5_v_restricts_to_zero_on_every_receiver_local_lift'] is True
    assert cr['Psi_BT_v_restricts_to_zero_on_every_receiver_local_lift'] is True
    lp=c['cq_local_tate_pairing_on_target']
    assert lp['multiplicative_value']=='<loc_v(Xi_BT),Psi_BT,v>=+1'
    assert lp['additive_invariant']=='0 in (1/2)Z/Z'
    assert lp['for_every_place_v'] is True
    assert lp['independent_of_ramification_of_Xi_BT'] is True

    rp=c['required_place_result_for_this_evaluation']
    assert rp['target_locus_nontrivial_pairing_places']==[]
    assert rp['inventory_complete_for_CS_evaluation_restricted_to_receiver_lift_locus'] is True
    assert rp['general_Stage36_required_place_inventory_complete'] is False

    ad=c['adelic_consequence']
    assert ad['sum_of_local_invariants']=='0'
    assert ad['CS_evaluation_can_produce_nonzero_adelic_obstruction_on_receiver_locus'] is False
    assert ad['CS_evaluation_can_exclude_a_fixed_p_branch'] is False
    assert ad['CS_evaluation_can_shrink_candidate_parameters'] is False
    sd=c['structural_diagnosis']
    assert sd['CS_geometry_adapter_is_mathematically_valid_on_base_open'] is True
    assert sd['CS_geometry_adapter_is_useful_as_receiver_obstruction'] is False
    assert sd['failure_mode']=='SELF_TRIVIALIZATION_ON_THE_TORSOR_IT_CLASSIFIES'
    assert sd['does_not_rule_out_other_secondary_or_Brauer_evaluations'] is True

    cb=c['construction_boundary']; rr=c['route_result']
    assert cb['BT_CS_EVALUATION_NONTRIVIAL_ON_RECEIVER_LOCAL_LOCUS'] is False
    assert cb['BT_CS_EVALUATION_SUPPLIES_OBSTRUCTION'] is False
    assert cb['BT_Poitou_Tate_local_condition_system_complete'] is False
    assert cb['general_Stage36_required_place_inventory_complete'] is False
    assert cb['LIT_WF02_applicability_PASS'] is False
    assert cb['new_global_obstruction_obtained'] is False
    assert cb['first_missing_obligation']=='BT_NONTRIVIAL_ON_RECEIVER_LOCUS_BRAUER_OR_SECONDARY_TORSOR_EVALUATION'
    assert rr['route_status']=='NO_GO_CS_PUSHOUT_EVALUATION_VANISHES_ON_TARGET_LOCAL_LIFTS_PIVOT_TO_SECONDARY_EVALUATION'
    assert rr['next_leaf']=='36-09CU_BT_NONTRIVIAL_RECEIVER_LOCUS_BRAUER_SECONDARY_TORSOR_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CT verified: on every actual receiver local five-root lift, Delta5=0, projected Psi_BT=0, and the CQ local Tate invariant is 0 at every place. CS is a valid base-open adapter but cannot obstruct the receiver lift locus. CU selected; no PT/BM/receiver/endpoint credit.')

if __name__=='__main__': main()
