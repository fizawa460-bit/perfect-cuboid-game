#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09CL/everywhere-local-branch-global-obstruction-router-preflight.json'
CK=ROOT/'stages/stage36/36-09CK/good-prime-and-real-place-local-integration-preflight.json'
CKV=ROOT/'stages/stage36/verify_stage36_36_09CK.py'
CARD=ROOT/'docs/arsenal/cards/workflows/LIT-WF02.md'
CONTRACT=ROOT/'docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json'
LITV=ROOT/'docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py'
PROMO=ROOT/'docs/stage36-literature-strengthening-promotion.md'
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
BASE='deaa08537f1e68e04e4189a51c6e02d28b2b7b13'
CK_HEAD='50069e0ab2e0c76b5119b3d74b8b79ffe3c26875'
CK_CI='34174776757/101901910910'
CK_PROMOTION_HEAD='9f3741fdd609f54ad02dd0a25ea089ebc52c2b29'
CK_PROMOTION_CI='34174862068/101902152862'
CERT_BLOB='9c08afb5b5f712c8d85df5fd20ae57f7e0f7ef39'
LOCKS={
    CK:'909dcb4985414fc3085818ad818f7601830dc7f6',
    CKV:'d7541d86948d98a629f503443a82d52ab1c95908',
    CARD:'a1e3e922ce3b2e26bfc5897fb1c1e2e82e3d6105',
    CONTRACT:'6fc62623ee59b4aaf1fc053ad42df2dcbba0855b',
    LITV:'ee066a55f95184916c02dc1f1bbd9f07d1840dc8',
    PROMO:'1a92c2012e1931076983a61d50d72ea83f326dcb',
}

def git(*a:str)->str:
    return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()

def blob(p:Path)->str:
    return git('hash-object',str(p.relative_to(ROOT)))

def main()->None:
    assert blob(CERT)==CERT_BLOB
    for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
    subprocess.check_call(['git','merge-base','--is-ancestor',BASE,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CK_HEAD,'HEAD'],cwd=ROOT)
    subprocess.check_call(['git','merge-base','--is-ancestor',CK_PROMOTION_HEAD,'HEAD'],cwd=ROOT)

    c=json.loads(CERT.read_text()); ck=json.loads(CK.read_text()); contract=json.loads(CONTRACT.read_text())
    assert c['base_main_sha']==BASE
    assert c['batch_parent']=={
        'pr':1705,
        '36_09CK_exact_green_head':CK_HEAD,
        '36_09CK_exact_head_ci':CK_CI,
        '36_09CK_promotion_head':CK_PROMOTION_HEAD,
        '36_09CK_promotion_ci':CK_PROMOTION_CI,
    }
    assert ck['main_consequence']['good_prime_local_classification_complete_for_each_fixed_branch'] is True
    assert ck['main_consequence']['real_place_local_realization_complete'] is True
    assert ck['remaining_boundary']['all_local_places_classified_branchwise_after_CJ_plus_CK'] is True
    assert ck['remaining_boundary']['global_rational_point_obtained'] is False
    assert ck['remaining_boundary']['global_H1_or_Selmer_family_obtained'] is False

    # The workflow implementation may self-check, but this is explicitly not an applicability PASS.
    out=subprocess.check_output(['python3',str(LITV),'--self-check'],cwd=ROOT,text=True)
    assert 'SELF_CHECK_OK:' in out
    assert 'no applicability PASS is inferred' in out
    assert 'PASS: LIT-WF02 immutable global-H1/localization applicability package verified' not in out

    assert contract['stable_id']=='LIT-WF02'
    assert contract['role']=='GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW'
    assert contract['maturity']=='PROVISIONAL'
    assert contract['self_check_is_applicability_pass'] is False
    assert contract['current_stage36_applicability_status']=='FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE'
    assert 'does not contain a Stage36 LIT-WF02 PASS package' in contract['current_stage36_status_reason']
    assert 'DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM' in contract['repo_adapter']
    assert 'POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS' in contract['repo_adapter']
    fw=contract['credit_firewall']
    assert fw['repo_theorem_credit'] is False
    for key in ['stage36_progress_increment','stage36_theorem_credit_increment','receiver_closure_increment','mw_closure_increment','local_global_obstruction_increment','endpoint_credit_increment']:
        assert fw[key]==0

    card=CARD.read_text(); promo=PROMO.read_text()
    assert 'FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE' in card
    assert 'POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS' in card
    assert 'DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM' in card
    assert 'no Stage36 LIT-WF02 PASS package' in card
    assert 'POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS' in promo
    assert 'DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM' in promo
    assert 'The global-localization adapter is missing.' in promo
    assert 'LOCAL_GLOBAL_OBSTRUCTION_INCREMENT=0' in promo
    assert 'GLOBAL-HILBERT-SELMER-COMPATIBILITY-TERMINAL' in promo

    inp=c['input_boundary']; app=c['lit_wf02_applicability']; src=c['source_diagnosis']; rr=c['router_result']; cp=c['checkpoint']
    assert inp['all_local_places_classified_branchwise'] is True
    assert inp['p_1_over_2_everywhere_local_surviving_branches']==3
    assert inp['p_2_over_11_everywhere_local_surviving_branches']==3
    assert inp['global_rational_point_obtained'] is False and inp['receiver_point_obtained'] is False
    assert app['current_stage36_applicability_status']==contract['current_stage36_applicability_status']
    assert app['missing_obligations']==['POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS','DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM']
    assert app['stage36_pass_package_registered'] is False
    assert app['self_check_is_applicability_pass'] is False
    assert src['S36_PW04_requires_chart_to_global_adapter'] is True
    assert src['S36_PW07_requires_dynamic_reservoir_localization_adapter'] is True
    assert src['S36_PW07_states_global_localization_adapter_missing'] is True
    assert src['local_global_obstruction_increment_from_literature_strengthening']==0
    assert src['global_terminal_research_gap']=='GLOBAL-HILBERT-SELMER-COMPATIBILITY-TERMINAL'

    for key in ['global_H1_route_available','Selmer_route_available','Hilbert_reciprocity_route_available','Poitou_Tate_route_available','Brauer_Manin_full_cover_complete','new_global_obstruction_obtained','fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_closed']:
        assert rr[key] is False
    assert rr['route_status']=='FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE'
    assert rr['next_leaf']=='36-09CM_GLOBAL_KUMMER_CLASS_AND_LOCALIZATION_ADAPTER_PREFLIGHT'
    assert cp['natural_hostile_audit_checkpoint_after_exact_green'] is True
    assert cp['next_leaf_must_remain_locked_until_hostile_audit'] is True
    for key,val in c['scope_firewalls'].items():
        assert val is False,(key,val)

    st=json.loads(STATE.read_text())
    assert st['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V133_36_09CL_ROUTER_CANDIDATE_PENDING_EXACT_CI'
    assert st['base_main_sha']==BASE and st['freshness']['current_main']==BASE
    ckst=st['authority_frontier']['36-09CK']
    assert ckst['status']=='PROVISIONAL_EXACT_GREEN_PARENT'
    assert ckst['exact_head']==CK_HEAD and ckst['exact_head_ci']==CK_CI
    cl=st['authority_frontier']['36-09CL']
    assert cl['status']=='PROVISIONAL_CANDIDATE_PENDING_EXACT_HEAD_CI'
    assert cl['certificate_blob_sha']==CERT_BLOB
    assert cl['GLOBAL_OBSTRUCTION_ROUTER_FAIL_CLOSED'] is True
    assert cl['LIT_WF02_APPLICABILITY_PASS'] is False
    assert cl['NEW_GLOBAL_OBSTRUCTION_OBTAINED'] is False
    assert st['current']['unit']=='36-09CL'
    assert st['current']['next_exact_leaf']=='36-09CM_GLOBAL_KUMMER_CLASS_AND_LOCALIZATION_ADAPTER_PREFLIGHT'
    assert st['current']['36_09CM_entry_allowed'] is False
    assert st['current']['hostile_audit_checkpoint_reached'] is False
    assert st['promotion_gates']['36_09CL_exact_head_ci_passed'] is False
    assert st['promotion_gates']['36_09CM_unlocked'] is False
    for key in ['fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed']:
        assert st['promotion_gates'][key] is False
    for key in ['fixed_p_parameter_exclusion_obtained','candidate_parameter_set_shrunk','receiver_emptiness_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        assert st['claims'][key] is False

    print('36-09CL verified: CK everywhere-local branch data cannot currently enter LIT-WF02. The global class and dynamic localization adapters are explicitly missing, so H1/Selmer/reciprocity/Poitou-Tate/Brauer-Manin routes remain fail-closed with zero new obstruction or receiver credit. Exact-green CL will be the hostile-audit checkpoint; CM remains locked.')

if __name__=='__main__':main()
