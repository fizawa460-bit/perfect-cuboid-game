#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CS/bt-five-root-deck-dual-projection-construction-preflight.json'
CR=ROOT/'stages/stage36/36-09CR/bt-geometric-local-condition-adelic-evaluation-source-preflight.json'
CRV=ROOT/'stages/stage36/verify_stage36_36_09CR.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
CQ=ROOT/'stages/stage36/36-09CQ/bt-cartier-dual-local-condition-adapter-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
BASE='d5545b32e6b3088bca53318998d434f2745b03e9'
CR_HEAD='1e9cf94bc7ffc6ac78fabf51adac3cdf31d2bd12'
LOCKS={
    CERT:'4657613348e8c59630ff8bcd660e518ed491f7c9',
    CR:'f31123ca0ed74db2fab03d033e63e4a9ced2bfeb',
    CRV:'f5403cf85053ec15d69df18d174d2ca711764bc3',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    CQ:'c7042cc86ff94cf94db88c8cc65ce5b69441aabe',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def emb(x:tuple[int,int,int])->tuple[int,int,int,int,int]:
    x0,x1,x2=x
    return x0,x1,x2,x0^x1,x0^x2

def proj(a:tuple[int,int,int,int,int])->tuple[int,int,int]:
    a0,a1,a2,a3,a4=a
    return a0^a3^a4,a1^a3,a2^a4

def dot(a,b)->int:
    return sum(x*y for x,y in zip(a,b))&1

def add(u,v):
    return tuple(a^b for a,b in zip(u,v))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CR_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cr=json.loads(CR.read_text()); cm=json.loads(CM.read_text()); cq=json.loads(CQ.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']['36_09CR_corrected_exact_green_head']==CR_HEAD
    assert c['batch_parent']['36_09CR_corrected_exact_head_ci']=='34191981610/101951737243'
    assert c['batch_parent']['promotion_replay_ci']=='34192082062/101952032086'
    assert cr['construction_boundary']['first_missing_obligation']=='BT_FIVE_ROOT_DECK_TORSOR_ACTION_AND_POINTWISE_CHARACTER_CLASS_SOURCE_BINDING'
    assert cq['cartier_dual_module']['identified_module']=='(Z/2Z)^3'
    assert cm['exact_BT_cover_adapter']['five_equations']==[
        'w0^2=(A*B)*y','w1^2=(kappa*A)*(1-y)','w2^2=(rho*A)*(1+y)',
        'w3^2=(kappa*B)*(1-L*y)','w4^2=(rho*B)*(1+L*y)']
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True
    assert 'P^2-M^2=8*D0' in bt['general_BH_elimination']['identities']

    cover=c['five_root_cover']
    assert cover['degree']==32 and cover['deck_group']=='G5=mu_2^5'
    assert cover['G5_torsor_on_retained_open'] is True
    assert cover['K_BT_is_identified_with_full_degree32_deck_group'] is False

    # The geometric fiber can be labelled by the five independent sign bits.
    G=[tuple((n>>j)&1 for j in range(5)) for n in range(32)]
    assert len(set(G))==32
    for g in G:
        images={add(g,x) for x in G}
        assert len(images)==32
        fixed=[x for x in G if add(g,x)==x]
        assert (len(fixed)==32 if g==(0,0,0,0,0) else len(fixed)==0)

    tq=c['transpose_quotient']
    assert tq['cartier_dual_transpose']=='i^D:F2^5 -> F2^3, i^D(a0,a1,a2,a3,a4)=(a0+a3+a4,a1+a3,a2+a4)'
    image={proj(a) for a in G}; kernel=[a for a in G if proj(a)==(0,0,0)]
    assert len(image)==8 and len(kernel)==4
    for a in G:
        for n in range(8):
            x=tuple((n>>j)&1 for j in range(3))
            assert dot(a,emb(x))==dot(proj(a),x),(a,x)

    # Coefficient squareclasses of F0..F4 on generators (A,B,kappa,rho).
    coeff=[
        (1,1,0,0), # AB
        (1,0,1,0), # kappa A
        (1,0,0,1), # rho A
        (0,1,1,0), # kappa B
        (0,1,0,1), # rho B
    ]
    def sumv(ids):
        z=(0,0,0,0)
        for i in ids: z=add(z,coeff[i])
        return z
    assert sumv([0,3,4])==(1,1,1,1)  # kappa rho A B mod squares
    assert sumv([1,3])==(1,1,0,0)    # A B mod squares
    assert sumv([2,4])==(1,1,0,0)    # A B mod squares

    ev=c['geometry_bound_dual_evaluation']
    assert ev['raw_squareclass_coordinates']==['[F0*F3*F4]','[F1*F3]','[F2*F4]']
    assert ev['generic_function_squareclass_supports']==[
        ['y','1-L*y','1+L*y'],['1-y','1-L*y'],['1+y','1+L*y']]
    assert all(ev['generic_function_squareclass_supports'])
    assert ev['nonconstant_at_function_squareclass_level'] is True
    assert ev['geometry_bound_local_dual_evaluation_adapter_complete'] is True
    assert ev['brauer_class_or_brauer_evaluation_constructed'] is False
    assert ev['poitou_tate_local_condition_system_constructed'] is False

    pk=c['pointwise_five_kummer_class']
    assert pk['point_dependent'] is True
    assert pk['global_class_for_arbitrary_adelic_tuple'] is False
    pi=c['cq_pairing_interface']
    assert pi['local_tate_pairing_is_now_well_typed'] is True
    assert pi['pairing_total_is_automatically_global_reciprocity_trivial_for_arbitrary_adelic_yv'] is False
    assert pi['nonzero_global_obstruction_already_proved'] is False
    assert pi['required_place_inventory_for_this_pointwise_pairing_complete'] is False

    cb=c['construction_boundary']; rr=c['route_result']
    assert cb['BT_five_root_deck_torsor_action_source_bound'] is True
    assert cb['BT_pointwise_five_character_or_kummer_class_source_bound'] is True
    assert cb['BT_geometry_bound_dual_evaluation_adapter_complete'] is True
    assert cb['BT_Poitou_Tate_local_condition_system_complete'] is False
    assert cb['LIT_WF02_applicability_PASS'] is False
    assert cb['new_global_obstruction_obtained'] is False
    assert cb['first_missing_obligation']=='BT_POINTWISE_LOCAL_TATE_PAIRING_REQUIRED_PLACE_AND_ADELIC_ORTHOGONALITY_INTEGRATION'
    assert rr['next_leaf']=='36-09CT_BT_POINTWISE_LOCAL_TATE_PAIRING_REQUIRED_PLACE_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CS verified: degree-32 five-root G5=mu2^5 deck torsor, transpose quotient to K_BT^D, and point-dependent local dual Kummer pushout are exact. No PT/BM/receiver/endpoint credit; CT selected.')

if __name__=='__main__': main()
