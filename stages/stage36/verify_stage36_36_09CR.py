#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CR/bt-geometric-local-condition-adelic-evaluation-source-preflight.json'
CQ=ROOT/'stages/stage36/36-09CQ/bt-cartier-dual-local-condition-adapter-preflight.json'
CQV=ROOT/'stages/stage36/verify_stage36_36_09CQ.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
BT=ROOT/'stages/stage36/36-09BT/general-aw-squareclass-branch-full-cover-local-model-preflight.json'
POL=ROOT/'docs/research-os/policies/repository-asset-discovery.md'
PW33_08=ROOT/'docs/arsenal/cards/provisional/S33-PW08.md'
PW33_07=ROOT/'docs/arsenal/cards/provisional/S33-PW07.md'
PW36_04=ROOT/'docs/arsenal/cards/provisional/S36-PW04.md'
PW36_07=ROOT/'docs/arsenal/cards/provisional/S36-PW07.md'
BASE='d5545b32e6b3088bca53318998d434f2745b03e9'
CQ_HEAD='a0d8cb76e43f926342f1a57b2b6aa903d19da63d'
LOCKS={
    CERT:'d1bde3d1da2d8482ff26457aa6e437ecbabbdfea',
    CQ:'c7042cc86ff94cf94db88c8cc65ce5b69441aabe',
    CQV:'cd7716e99f2c1da83b9bfb0ea39168b43d5752ce',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    BT:'e58c417ddfa340d96b2ac1fbae9e7da7c5224d78',
    POL:'bf001d4f722da0e463352453e10d4a53b2d94bce',
    PW33_08:'c9e13a917811581578f833ea93619d85f717be6d',
    PW33_07:'7f1337858bc6f9006e101d810dd72e67aef534fd',
    PW36_04:'2f5eb6501d64393e2962aff4bb6d0b25aa104314',
    PW36_07:'9ebeb753826da005471bf677969b535f91ea8018',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def emb(x:tuple[int,int,int])->tuple[int,int,int,int,int]:
    x0,x1,x2=x
    return x0,x1,x2,x0^x1,x0^x2

def dual(a:tuple[int,int,int,int,int])->tuple[int,int,int]:
    a0,a1,a2,a3,a4=a
    return a0^a3^a4,a1^a3,a2^a4

def dot(a,b)->int:
    return sum(x*y for x,y in zip(a,b))&1

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CQ_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cq=json.loads(CQ.read_text()); cm=json.loads(CM.read_text()); bt=json.loads(BT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1712,'36_09CQ_exact_green_head':CQ_HEAD,'36_09CQ_exact_head_ci':'34188612840/101941880607'}
    assert cq['cartier_dual_module']['identified_module']=='(Z/2Z)^3'
    assert cq['geometric_adapter_gap']['first_missing_obligation']=='BT_GEOMETRIC_CONNECTING_MAP_OR_POINT_DEPENDENT_LOCAL_EVALUATION_ADAPTER'
    assert cm['global_kummer_class']['five_root_twist_vector']==['xi0','xi1','xi2','xi0*xi1=[kappa*B]','xi0*xi2=[rho*B]']
    assert cm['adapter_result']['old_S36_PW04_pointwise_36_04_class_identified_with_Xi_BT'] is False
    assert cm['exact_BT_cover_adapter']['five_equations']==[
        'w0^2=(A*B)*y','w1^2=(kappa*A)*(1-y)','w2^2=(rho*A)*(1+y)',
        'w3^2=(kappa*B)*(1-L*y)','w4^2=(rho*B)*(1+L*y)']
    assert bt['general_t_line_four_square_model']['general_AW_branch_full_cover_local_model_obtained'] is True

    # Reusable-card type boundaries are load-bearing: protocol yes, concrete map/value no.
    t33_08=PW33_08.read_text(); t33_07=PW33_07.read_text(); t36_04=PW36_04.read_text(); t36_07=PW36_07.read_text()
    assert 'GERSTEN_CONNECTING_LOCALIZATION_ADAPTER' in t33_08
    assert 'PW08 promotes the construction/audit protocol, not that value' in t33_08
    assert 'exact Gersten/residue complex' in t33_08
    assert 'TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER' in t33_07
    assert 'exact common cocycle' in t33_07
    assert 'POINTWISE_ELEMENTARY_2_TORSOR_LIFT_CLASS_CHART_ADAPTER' in t36_04
    assert 'fixed finite global twist-family credit' in t36_04
    assert 'DIRECTIONAL_PRIME_RESERVOIR_LOCAL_CHARACTER_MATRIX' in t36_07
    assert 'Selmer membership from local admissibility' in t36_07

    ares=c['asset_discovery_result']; geo=c['bt_geometry_inventory']; fp=c['formal_dual_projection_candidate']; cb=c['construction_boundary']; rr=c['route_result']
    assert ares['matching_reusable_method']=='S33-PW08 GERSTEN_CONNECTING_LOCALIZATION_ADAPTER protocol'
    assert ares['S33_PW08_concrete_zero_map_reused'] is False
    assert ares['S33_PW07_directly_applies'] is False
    assert ares['S36_PW04_directly_applies'] is False
    assert ares['S36_PW07_directly_applies'] is False
    assert ares['existing_source_bound_BT_dual_evaluation_adapter_found'] is False
    assert ares['repository_search_miss_is_mathematical_nonexistence_claim'] is False
    assert geo['five_root_cover_model_available'] is True and geo['degree']==32
    assert geo['twist_embedding_F2']=='i(x0,x1,x2)=(x0,x1,x2,x0+x1,x0+x2)'
    assert geo['source_bound_degree32_deck_torsor_action_materialized_for_CR'] is False
    assert geo['source_bound_identification_K_BT_as_degree32_deck_kernel'] is False
    assert geo['source_bound_pointwise_five_character_class_materialized'] is False
    assert geo['source_bound_local_point_to_H1_KBT_dual_map_materialized'] is False

    # Exhaustively verify the only positive mathematical construction in CR:
    # the formal F2-dual of the exact 3->5 twist embedding.
    for n in range(8):
        x=((n>>0)&1,(n>>1)&1,(n>>2)&1)
        for m in range(32):
            a=tuple((m>>j)&1 for j in range(5))
            assert dot(a,emb(x))==dot(dual(a),x),(a,x,emb(x),dual(a))
    assert fp['formula']=='i^D(a)=(a0+a3+a4,a1+a3,a2+a4) in F2^3'
    assert fp['multiplicative_squareclass_formula']==['psi0=a0*a3*a4','psi1=a1*a3','psi2=a2*a4']
    assert fp['pairing_identity_exhaustively_verifiable'] is True
    assert fp['deck_character_source_bound'] is False
    assert fp['pointwise_local_class_source_bound'] is False
    assert fp['may_be_called_BT_dual_evaluation_adapter'] is False

    assert cb['new_positive_obstruction'] is False
    assert cb['BT_geometry_bound_dual_evaluation_adapter_complete'] is False
    assert cb['BT_Poitou_Tate_local_condition_system_complete'] is False
    assert cb['LIT_WF02_applicability_PASS'] is False
    assert cb['first_missing_obligation']=='BT_FIVE_ROOT_DECK_TORSOR_ACTION_AND_POINTWISE_CHARACTER_CLASS_SOURCE_BINDING'
    assert rr['route_status']=='FAIL_CLOSED_AT_BT_FIVE_ROOT_DECK_TORSOR_SOURCE_BINDING_WITH_EXACT_DUAL_PROJECTION_SEED'
    assert rr['next_leaf']=='36-09CS_BT_FIVE_ROOT_DECK_DUAL_PROJECTION_CONSTRUCTION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CR verified: PW08 supplies protocol only; existing Stage33/Stage36 assets do not source-bind a BT dual evaluation. Exact F2 dual projection seed i^D=(a0+a3+a4,a1+a3,a2+a4) verified exhaustively; CS selected. No PT/BM/receiver/endpoint credit.')

if __name__=='__main__': main()
