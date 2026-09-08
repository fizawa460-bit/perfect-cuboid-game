#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CV/bt-non-kummer-divisor-cocycle-brauer-source-preflight.json'
CU=ROOT/'stages/stage36/36-09CU/bt-kummer-monomial-brauer-secondary-preflight.json'
H04=ROOT/'stages/stage36/36-04/h-torsor-lift-class.json'
PW04=ROOT/'docs/arsenal/cards/provisional/S36-PW04.md'
B=ROOT/'stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json'
A=ROOT/'stages/stage36/36-09A/camp4-brauer-compatibility-preflight.json'
O=ROOT/'stages/stage36/36-09O/physical-square-lift-v4-quotient-preflight.json'
AA=ROOT/'stages/stage36/36-09AA/receiver-coupled-same-x-twist-intersection-preflight.json'
AC=ROOT/'stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json'
PW07=ROOT/'docs/arsenal/cards/provisional/S33-PW07.md'
BASE='d5545b32e6b3088bca53318998d434f2745b03e9'
CU_HEAD='b741a0459eee46cb3f0404c0d13befb819c793d0'
PROMO_HEAD='7c37a117cc69239ea6e06cb36aa8f19badb44d05'
LOCKS={
    CERT:'2abc41fe2dccc7563e4c8af49d37b78094e7cd64',
    CU:'cb92adb9b0025e8cef8554a2c30dc6777b8e2835',
    H04:'a06e201a9b554da71c5e75d8f8541e7284f8d020',
    PW04:'2f5eb6501d64393e2962aff4bb6d0b25aa104314',
    B:'da9143e587506522ed966d380d9980ff1875db0d',
    A:'66f31c03e5a978783a60b036322538f173a2f411',
    O:'6a2678ebedba40e13277100441361039ee47ca28',
    AA:'be447726a97158849c67ed6d57d6d3c35d6ba20f',
    AC:'3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021',
    PW07:'7f1337858bc6f9006e101d810dd72e67aef534fd',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CU_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',PROMO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cu=json.loads(CU.read_text()); h=json.loads(H04.read_text()); b=json.loads(B.read_text()); a=json.loads(A.read_text()); o=json.loads(O.read_text()); aa=json.loads(AA.read_text()); ac=json.loads(AC.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1712,
        '36_09CU_exact_green_head':CU_HEAD,
        '36_09CU_exact_head_ci':'34195137169/101961098375',
        'promotion_replay_head':PROMO_HEAD,
        'promotion_replay_ci':'34195275892/101961512776'
    }
    assert cu['construction_boundary']['BT_KUMMER_MONOMIAL_QUATERNION_FAMILY_EXHAUSTED_AS_OBSTRUCTION'] is True
    assert cu['construction_boundary']['BT_NONTRIVIAL_RECEIVER_LOCUS_SECONDARY_EVALUATION_FOUND'] is False

    # The retained H-torsor class is exact, but it classifies lifting and is not a Brauer/H2 adapter.
    p=h['pointwise_class']
    assert p['rational_lift_iff']=='q_H^{-1}(P)(Q) nonempty iff delta_H(P)=1 iff all three G_ci(q) are rational squares'
    assert h['pass_condition']['POINTWISE_H_TORSOR_CLASS_EXPLICIT'] is True
    t4=PW04.read_text()
    assert 'POINTWISE_ELEMENTARY_2_TORSOR_LIFT_CLASS_CHART_ADAPTER' in t4
    assert 'marked Brauer/H2(mu2) binding' in t4

    rb=b['exact_receiver_condition_K']
    assert rb['available'] is True
    assert rb['equivalence']=='P lies in q_H(U(Q)) iff K(P) holds'
    assert 'three square equations' in b['why_pointwise_torsor_equations_do_not_complete_B4']['reason']

    # Later route is still the physical receiver, not an enlarged auxiliary locus.
    assert o['receiver_restricted_intersection_adapter']['S34_W03_applicability']=='EXACT_ADAPTER_READY'
    assert aa['receiver_square_on_E_minus']['exact_same_x_equivalence'].startswith('receiver K')
    assert aa['scope_firewalls']['same_x_receiver_equivalence_proved'] is True
    assert ac['receiver_birational_reconstruction']['conclusion']=='on the retained open this genus-three V4 cover is birational to the audited physical top receiver; it is an arithmetic-normalized receiver model, not a larger rankjump locus'

    rc=c['retained_candidate_S36_PW04']
    assert rc['is_Brauer_or_H2_class'] is False
    assert rc['card_explicitly_forbids_marked_Brauer_H2_binding'] is True
    assert rc['consequence_on_rational_physical_receiver']=='delta_H(P)=1 for every P in q_H(U(Q))'
    assert rc['can_be_nontrivial_receiver_locus_secondary_evaluation'] is False

    # CAMP4 sibling payload was already blocked upstream before any transport existed.
    assert a['retained_camp4_dependency_chain']['relationship_to_stage36']=='SIBLING_ASSET_PROVIDER_ONLY'
    assert a['upstream_payload_audit']['BR2A_EXPLICIT_TWO_PRIMARY_CLASS_PACKET_CLOSED'] is False
    assert a['upstream_payload_audit']['BR2B_LOCAL_EVALUATION_MAPS_CLOSED'] is False
    assert a['compatibility_checks']['CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED'] is False
    assert a['compatibility_checks']['CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED'] is False
    camp=c['retained_candidate_CAMP4']
    assert camp['explicit_endpoint_2primary_Brauer_class_available'] is False
    assert camp['explicit_local_evaluation_table_available'] is False
    assert camp['can_supply_current_BT_Brauer_evaluation'] is False

    t7=PW07.read_text()
    assert 'exact common cocycle' in t7
    assert 'actual transition function/divisor/Cartier data' in t7
    r7=c['retained_candidate_S33_PW07']
    assert r7['protocol_reusable'] is True
    assert r7['concrete_Stage33_representative_reusable_on_BT'] is False
    assert r7['those_BT_specific_inputs_materialized'] is False

    sb=c['source_boundary']; rr=c['route_result']
    assert sb['CU_five_root_Kummer_monomial_family_already_no_go'] is True
    assert sb['older_H_torsor_lift_class_is_self_trivial_on_physical_receiver'] is True
    assert sb['CAMP4_explicit_Brauer_packet_available_for_transport'] is False
    assert sb['existing_source_bound_BT_nontrivial_Brauer_or_secondary_class_found'] is False
    assert sb['repository_search_miss_is_mathematical_nonexistence_claim'] is False
    assert sb['first_missing_obligation']=='BT_LITERAL_NON_KUMMER_DIVISOR_CECH_COMMON_COCYCLE_OR_SECONDARY_EXTENSION_CONSTRUCTION'
    assert rr['route_status']=='FAIL_CLOSED_RETAINED_NON_KUMMER_ASSETS_DO_NOT_SUPPLY_RECEIVER_EVALUATION_NEW_LITERAL_BRAUER_SOURCE_REQUIRED'
    assert rr['next_leaf']=='36-09CW_BT_LITERAL_NON_KUMMER_DIVISOR_CECH_CONSTRUCTION_PREFLIGHT'
    for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
    print('36-09CV verified: retained non-Kummer candidates do not supply a receiver obstruction. The old H-torsor class self-trivializes on the physical lifted receiver and is not Brauer/H2; CAMP4 lacks the upstream class/evaluation packet and compatibility; PW07 supplies protocol only. Literal new divisor/Cech/common-cocycle or secondary-extension construction is required. No BM/PT/receiver/endpoint credit.')

if __name__=='__main__': main()
