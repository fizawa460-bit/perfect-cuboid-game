#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CN/bt-kummer-immutable-localization-package-preflight.json'
DIAG=ROOT/'stages/stage36/36-09CN/derive-fixed-branch-inventory.py'
CM=ROOT/'stages/stage36/36-09CM/bt-global-kummer-class-localization-adapter-preflight.json'
CMV=ROOT/'stages/stage36/verify_stage36_36_09CM.py'
CJ=ROOT/'stages/stage36/36-09CJ/fixed-p-all-bad-place-local-integration-preflight.json'
CK=ROOT/'stages/stage36/36-09CK/good-prime-and-real-place-local-integration-preflight.json'
LIT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
LITV=ROOT/'docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py'
CI=ROOT/'stages/stage36/verify_stage36_36_09CI.py'
CH=ROOT/'stages/stage36/verify_stage36_36_09CH.py'
CE=ROOT/'stages/stage36/verify_stage36_36_09CE.py'
CF=ROOT/'stages/stage36/verify_stage36_36_09CF.py'
CG=ROOT/'stages/stage36/verify_stage36_36_09CG.py'
CC=ROOT/'stages/stage36/verify_stage36_36_09CC.py'
BU=ROOT/'stages/stage36/verify_stage36_36_09BU.py'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='8143dbaabb0cf164e65091dd315996f7eac68cf8'
CM_HEAD='f5b270da04815e6339cd8795d0ddf58ce34138ca'
CM_CI='34177867543/101910774245'
CERT_BLOB='e6b38b0bd621434a5cfa365ee1077241e1beb9bc'
LOCKS={
    DIAG:'661d7276cd92ba8f790abee0f60646a55f99c443',
    CM:'06c3e6d1fcc2453dc44b84d50896abdc6a1658d7',
    CMV:'837ef698fd808c4adf9858f4d037ef73982db2c5',
    CJ:'bf98c1bfd468ff975755d364081d829b1f8c1233',
    CK:'909dcb4985414fc3085818ad818f7601830dc7f6',
    LIT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
    LITV:'ee066a55f95184916c02dc1f1bbd9f07d1840dc8',
    CI:'53655d24a59024766b6be3cba00720bed86916ad',
    CH:'98ae4bc76749c82b4165c7a7b37d7445f42fa6dc',
    CE:'8eefd1d859b71d33693d85e5f03e4cdeb0ccf0cc',
    CF:'195741b765957a2b3c014eaab2c38ef1d6ad0a30',
    CG:'7a210e55a5e2386fb02a59de00502a4e810b9410',
    CC:'56edc0cb232290a0e369be10d6f4c972dac279e7',
    BU:'64b889c2dde22d021fb2933b976311d903f57dce',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CM_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); cm=json.loads(CM.read_text()); cj=json.loads(CJ.read_text()); ck=json.loads(CK.read_text()); lit=json.loads(LIT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={'pr':1707,'36_09CM_exact_green_head':CM_HEAD,'36_09CM_exact_head_ci':CM_CI}
    assert c['source_locks']['lit_wf02_verifier']['blob_sha']==LOCKS[LITV]
    assert cm['global_kummer_class']['global_Kummer_class_constructed_for_each_fixed_BT_branch'] is True
    assert cm['adapter_result']['BT_dynamic_localization_system_adapter_complete_at_squareclass_cover_level'] is True
    assert cm['adapter_result']['LIT_WF02_applicability_PASS'] is False
    assert cj['finite_bad_place_cover']['bad_places']=='2 together with the odd primes dividing P*M*D0*Q, where D0=a*b*(a-b)*(a+b) and Q=a^2+b^2'
    assert cj['finite_bad_place_cover']['branchwise_all_finite_bad_places_locally_realized'] is True
    assert ck['good_prime_model']['target_characters']==['d','k','r','k*d','r*d']
    assert ck['large_good_prime_route']['automatic_prime_range']=='every prime q>=1163'
    assert ck['real_place']['every_outer_branch_has_real_point'] is True

    assert lit['package_schema']=='LIT-WF02-GLOBAL-H1-LOCALIZATION-PACKAGE-V2'
    assert 'required_place_inventory' in lit['pass_package_required_fields']
    rule=lit['place_completeness_rule']
    assert 'independently verified immutable required-place inventory' in rule
    assert 'exact place set must equal the localization set' in rule
    assert 'dyadic and real/archimedean places explicitly named' in rule
    assert lit['do_not_use_for'][0]=='constructing a missing global H1/Kummer class from local compatibility'
    assert lit['pass_semantics'].startswith('PASS certifies that the repo has supplied immutable evidence')

    out=json.loads(subprocess.check_output(['python3',str(DIAG)],cwd=ROOT,text=True))
    r=c['representative_branch_diagnostic']
    assert out['panel']['a']==r['a']==1 and out['panel']['b']==r['b']==2
    assert out['panel']['P']==r['P']==1 and out['panel']['M']==r['M']==-7
    assert out['panel']['D0']==r['D0']==-6 and out['panel']['Q']==r['Q']==5
    assert out['panel']['row']==r['outer_row']==[1,1,1,1,-1,0,0,6,True]
    assert out['global_class']['kappa']==r['kappa']==-1 and out['global_class']['rho']==r['rho']==1
    assert out['global_class']['Xi_BT']==r['Xi_BT']==[1,-1,1]
    assert out['global_class']['coordinate_parity_supports']==r['Xi_BT_coordinate_parity_supports']==[[],[],[]]
    assert out['global_class']['finite_ramification_support']==r['Xi_BT_finite_ramification_support']==[2]
    assert out['BT_cover_finite_bad_places']==r['BT_cover_finite_bad_places']==[2,3,5,7]
    assert out['global_class']['real_signs']==r['real_signs']==[1,-1,1]
    assert out['LIT_WF02_required_place_inventory_identified'] is False

    lc=c['lit_wf02_contract_check']; mc=c['main_consequence']; rr=c['route_result']; fw=c['scope_firewalls']
    assert lc['LIT_WF02_PASS_package_emitted'] is False
    assert lc['first_missing_obligation']=='INDEPENDENT_REQUIRED_PLACE_SELECTION_RULE_AND_VERIFIER'
    assert mc['CM_global_class_gap_narrowed'] is True
    assert mc['CM_dynamic_localization_gap_narrowed'] is True
    assert mc['immutable_LIT_WF02_package_complete'] is False
    assert mc['LIT_WF02_applicability_PASS'] is False
    assert rr['route_status']=='FAIL_CLOSED_AT_REQUIRED_PLACE_SELECTION_RULE'
    assert rr['next_leaf']=='36-09CO_REQUIRED_PLACE_SELECTION_RULE_PREFLIGHT'
    assert rr['36_09CO_entry_allowed_after_exact_green_CN'] is True
    for key in ['class_ramification_support_equals_receiver_bad_place_set','receiver_bad_place_set_equals_LIT_WF02_required_place_set','synthetic_good_prime_family_label_is_a_mathematical_place','fixed_branch_diagnostic_is_uniform_parameter_package','LIT_WF02_applicability_PASS','Selmer_membership_obtained','Poitou_Tate_obstruction_obtained','Brauer_Manin_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert fw[key] is False

    st=json.loads(STATE.read_text())
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    assert st['freshness']['stage36_source_drift'] is False
    print('36-09CN verified: CM supplies a fixed BT global Kummer class/localizer, but LIT-WF02 remains fail-closed at the independent required-place selection rule. Representative p=1/2 branch separates Xi ramification support {2} from BT bad places {2,3,5,7}; CK good-prime family is a third layer. CO selected after exact-green CN; no obstruction or receiver credit.')

if __name__=='__main__': main()
