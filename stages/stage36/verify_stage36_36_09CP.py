#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CP/fixed-dual-pairing-local-condition-system-preflight.json'
CO=ROOT/'stages/stage36/36-09CO/required-place-selection-rule-preflight.json'
COV=ROOT/'stages/stage36/verify_stage36_36_09CO.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
X=ROOT/'stages/stage36/36-09X/kummer-class-coupled-hilbert-local-solvability-preflight.json'
Y=ROOT/'stages/stage36/36-09Y/kummer-complement-prime-2adic-hilbert-preflight.json'
Z=ROOT/'stages/stage36/36-09Z/explicit-mw-rankjump-witness-preflight.json'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
BASE='8143dbaabb0cf164e65091dd315996f7eac68cf8'
CO_HEAD='b19439a701579d1563a77746cb1e6d57da04460e'
CO_CI='34180908069/101919663411'
LOCKS={
    CERT:'3ea852b149986c1ac0b3916005b605b138b21feb',
    CO:'e41bfad47046ff47074285f2c6f719d9125b12a1',
    COV:'7102c81b0af5530ee0462fb23ddce66f2b5c7f2e',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    X:'3eb6e42b563ee2b5042917467a62e7606f27a869',
    Y:'20c6d782e59bff820392731ec81653d15b2d1921',
    Z:'6a3b05e70fb146eff576df17142547b11679cf65',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def main()->None:
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CO_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); co=json.loads(CO.read_text()); cm=json.loads(CM.read_text())
    x=json.loads(X.read_text()); y=json.loads(Y.read_text()); z=json.loads(Z.read_text()); lit=json.loads(LIT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1707,'36_09CO_exact_green_head':CO_HEAD,'36_09CO_exact_head_ci':CO_CI}
    assert co['route_result']['next_leaf']=='36-09CP_FIXED_DUAL_PAIRING_OR_LOCAL_CONDITION_SYSTEM_PREFLIGHT'
    assert cm['global_kummer_class']['module']=='K_BT=mu_2^3 over Q'
    assert cm['global_kummer_class']['class_name']=='Xi_BT'

    assert x['homogeneous_model']['alpha_class_scope']=='d is a squarefree signed representative supported on primes dividing C0'
    assert x['homogeneous_model']['beta_class_scope']=='e is a squarefree signed representative supported on primes dividing 2*D0'
    assert '2-isogeny Kummer class' in x['source_locks']['standard_2isogeny_descent']['uses'][0]
    assert x['scope_firewalls']['Kummer_class_coupled_global_Hilbert_obstruction_proved'] is False
    assert x['receiver_sensitive_reciprocity_status']['multiplace_reciprocity_obstruction_proved'] is False

    rb=y['reciprocity_route_boundary']
    assert rb['full_global_arithmetic_route']=='LIVE_REQUIRES_SELMER_TO_MW_OR_SHA_DISTINCTION_NOT_JUST_LOCAL_HILBERT_SOLVABILITY'
    assert rb['multiplace_reciprocity_obstruction_proved'] is False
    assert y['scope_firewalls']['global_Selmer_class_proved_for_witnesses'] is False
    assert y['scope_firewalls']['Cassels_pairing_computed'] is False

    aw=z['alpha_actual_kummer_growth_witness']; bw=z['beta_actual_kummer_growth_witness']
    assert aw['parameter']['p']=='14/13' and aw['class_d']==337
    assert aw['kummer_class']=='alpha(P)=[337]'
    assert aw['nontrivial_against_generic_alpha_baseline'] is True
    assert bw['parameter']['p']=='5/2' and bw['class_e']==5
    assert bw['kummer_class']=="beta(P')=[5]"
    assert bw['nonbaseline'] is True
    assert z['cassels_route_boundary']['uniform_rankjump_locus_emptiness_via_Cassels_impossible'] is True

    td=c['bt_dual_target']; pa=c['existing_pw07_lineage_audit']; ar=c['adapter_result']; rr=c['route_result']; fw=c['scope_firewalls']
    assert td['left_module']=='K_BT=mu_2^3 over Q'
    assert td['abstract_dual_identification_alone_is_adapter'] is False
    assert pa['Y_multiplace_reciprocity_obstruction_proved'] is False
    assert pa['map_from_alpha_beta_classes_to_H1_of_KBT_dual_source_bound'] is False
    assert pa['pairing_alpha_beta_with_Xi_BT_source_bound'] is False
    assert pa['BT_local_condition_subgroups_for_poitou_tate_source_bound'] is False
    assert ar['existing_PW07_supplies_BT_dual_pairing_adapter'] is False
    assert ar['existing_PW07_supplies_BT_poitou_tate_local_condition_system'] is False
    assert ar['conditional_CO_place_rule_instantiated_for_Stage36'] is False
    assert ar['LIT_WF02_applicability_PASS'] is False
    assert ar['first_missing_obligation']=='BT_CARTIER_DUAL_CLASS_AND_LOCAL_CONDITION_ADAPTER'
    assert rr['route_status']=='FAIL_CLOSED_EXISTING_LOCAL_CHARACTER_LINEAGE_TYPE_MISMATCH'
    assert rr['next_leaf']=='36-09CQ_BT_CARTIER_DUAL_LOCAL_CONDITION_ADAPTER_PREFLIGHT'
    assert rr['36_09CQ_entry_allowed_after_exact_green_CP'] is True
    assert 'fixed finite global Galois module' in [p for p in lit['literature'] if p['authors']=='J. S. Milne'][0]['exact_hypotheses_summary']
    for key,val in fw.items(): assert val is False,(key,val)
    print('36-09CP verified: S36-PW07 alpha/beta 2-isogeny Kummer lineage is not a source-bound Cartier-dual/local-condition adapter for Xi_BT; Z contains actual MW Kummer-image witnesses, so uniform obstruction relabelling is forbidden. CQ selected; no obstruction or receiver credit.')

if __name__=='__main__': main()
