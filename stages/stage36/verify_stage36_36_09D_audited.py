#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09D/q-defined-pencil-fibration-preflight.json'
CERT_BLOB='7fb67b8bf5a37d16ef527aea6109eb0782d61201'
LEGACY_COMMIT='a306fc15578bb7eac8d0fd43bbc6b7be9f9c3d33'
LEGACY_BLOB='1e7916a25db3fd3c30927c9a57d6474c139ca18c'
AUDIT_BASE='591e513ad5d7f3f8824f14c6ce529125b0a4f193'
INTERVENING_MAIN='70c302bff5794cc30ea9cd8f4b84b75fb42c757d'
CURRENT_BASE='a306fc15578bb7eac8d0fd43bbc6b7be9f9c3d33'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V21_THIN_36_09D_AUDITED'
HEAD='f22d67dda4183c3bfd39710ebb4083f5185f3f49'
CI_RUN=33955636227
CI_JOB=101278356425
AUDIT_REVIEW=5120566848

def blob_bytes(b:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def blob_file(p:Path)->str:
    return blob_bytes(p.read_bytes())

def req(ok:bool,msg:str)->None:
    if not ok:
        raise SystemExit(msg)

def git_show(spec:str)->bytes:
    return subprocess.check_output(['git','show',spec],cwd=ROOT)

def git_lines(*args:str)->list[str]:
    out=subprocess.check_output(['git',*args],cwd=ROOT,text=True)
    return [x for x in out.splitlines() if x]

def main()->None:
    req(blob_file(CERT)==CERT_BLOB,'36-09D certificate blob drift')
    c=json.loads(CERT.read_text())
    req(c.get('schema')=='STAGE36_36_09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT_V1','36-09D certificate schema moved')
    q=c.get('q_defined_pencil',{})
    req(q.get('q_defined') is True and q.get('physical_parameter_is_positive_rational_square') is True,'36-09D Q-pencil/physical parameter moved')
    req(q.get('physical_special_parameters_not_automatically_eliminated')==['1'],'36-09D t=1 firewall moved')
    g=c.get('generic_fiber_common_geometry',{})
    req(g.get('degree')==8 and g.get('deck_group')=='(Z/2)^3','36-09D generic cover moved')
    req(g.get('finite_inertia_rank')==3 and g.get('branch_point_count_including_infinity')==5,'36-09D inertia/branch count moved')
    req(g.get('generic_fiber_genus')==3 and g.get('connected_generic_fiber') is True,'36-09D genus/connectedness moved')
    inv=c.get('character_quotient_inventory',{})
    req(inv.get('nontrivial_characters_each')==7,'36-09D character count moved')
    req(inv.get('genus1_character_quotients_each')==3 and inv.get('genus0_character_quotients_each')==4,'36-09D quotient genus inventory moved')
    req(inv.get('j_multiset_each_representative')==['J_MINUS','J_MINUS','J_PLUS'],'36-09D j multiset moved')
    req(inv.get('both_j_functions_nonconstant') is True and inv.get('fixed_elliptic_curve_reduction_obtained') is False,'36-09D moving-family firewall moved')
    req(inv.get('jacobian_product_isogeny_claimed') is False,'36-09D Jacobian-product firewall moved')
    route=c.get('route_decision',{})
    req(route.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE_GENUS3_WITH_THREE_MOVING_ELLIPTIC_CHARACTER_QUOTIENTS','36-09D B6 outcome moved')
    req(route.get('S34_W02_TRIGGERED') is False,'36-09D S34-W02 applicability moved')
    req(route.get('next_route_after_hostile_audit')=='36-09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT','36-09E route moved')
    req(all(v is False for v in c.get('claims',{}).values()),'36-09D higher claim leaked')

    legacy=git_show(f'{LEGACY_COMMIT}:stages/stage36/MAIN-STATE.json')
    req(blob_bytes(legacy)==LEGACY_BLOB,'legacy V20 state blob drift')
    old=json.loads(legacy)
    req(old.get('schema')=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V20_36_09D_PENDING_HOSTILE_AUDIT','legacy V20 schema moved')
    req(old.get('status')=='ACTIVE_PENDING_HOSTILE_AUDIT','legacy V20 hostile lifecycle moved')
    oa=old.get('authority_frontier',{}).get('36-09D',{})
    req(oa.get('promotion_status')=='PROVISIONAL_NOT_AUDITED','legacy 36-09D provisional authority moved')
    req(oa.get('certificate_blob_sha')==CERT_BLOB,'legacy 36-09D certificate lock moved')
    req(old.get('current',{}).get('36_09E_entry_allowed') is False,'legacy hostile boundary before 36-09E moved')

    changed=git_lines('diff','--name-only',AUDIT_BASE,INTERVENING_MAIN)
    req(bool(changed),'expected intervening main advance missing')
    bad=[p for p in changed if not (p.startswith('stages/stage33/') or p.startswith('.github/workflows/stage33-'))]
    req(not bad,'non-Stage33 authority changed between audit and merge: '+','.join(bad))
    parents=git_lines('show','-s','--format=%P',LEGACY_COMMIT)
    req(len(parents)==1,'merge-parent read failed')
    pp=parents[0].split()
    req(pp==[INTERVENING_MAIN,HEAD],f'36-09D merge parents moved: {pp}')

    s=json.loads(STATE.read_text())
    req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE' and s.get('base_main_sha')==CURRENT_BASE,'V21 lifecycle/base moved')
    ls=s.get('legacy_authority_snapshot',{})
    req(ls.get('commit')==LEGACY_COMMIT and ls.get('blob_sha')==LEGACY_BLOB,'V21 legacy snapshot lock moved')
    fs=s.get('freshness_sync_36_09D_promotion',{})
    req(fs.get('audit_base_main_sha')==AUDIT_BASE and fs.get('intervening_main_sha')==INTERVENING_MAIN and fs.get('merged_main_sha')==LEGACY_COMMIT,'36-09D freshness sync moved')
    a=s.get('authority_frontier',{}).get('36-09D',{})
    req(a.get('status')=='AUDITED_EXACT_GENUS3_PENCIL_WITH_THREE_MOVING_ELLIPTIC_CHARACTER_QUOTIENTS','36-09D audited status moved')
    req(a.get('pr')==1590 and a.get('hostile_audit_review')==AUDIT_REVIEW,'36-09D audit identity moved')
    req(a.get('audited_head')==HEAD and a.get('exact_head_ci')==f'{CI_RUN}/{CI_JOB}','36-09D exact head/CI moved')
    req(a.get('certificate_blob_sha')==CERT_BLOB and a.get('merged_main_sha')==LEGACY_COMMIT,'36-09D cert/merge lock moved')
    req(a.get('Q_DEFINED_PENCIL_EXACT') is True and a.get('GENERIC_FIBER_CONNECTED_DEGREE8_GENUS3') is True,'36-09D audited geometry moved')
    req(a.get('GENUS1_CHARACTER_QUOTIENTS_EACH')==3 and a.get('GENUS0_CHARACTER_QUOTIENTS_EACH')==4,'36-09D audited character inventory moved')
    req(a.get('J_MULTISET_EACH')==['J_MINUS','J_MINUS','J_PLUS'],'36-09D audited j multiset moved')
    req(a.get('MOVING_NONISOTRIVIAL_ELLIPTIC_FAMILIES') is True,'36-09D moving-family authority moved')
    req(a.get('PHYSICAL_SPECIAL_T1_RETAINED') is True and a.get('S34_W02_TRIGGERED') is False,'36-09D firewall moved')
    req(a.get('promotion_status')=='HOSTILE_AUDIT_PASS' and a.get('verdict')=='HOSTILE_AUDIT_PASS','36-09D audit promotion moved')

    cyc=s.get('cycle_ledger',{})
    req(cyc.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE_GENUS3_WITH_THREE_MOVING_ELLIPTIC_CHARACTER_QUOTIENTS','B6 audited live status moved')
    req(cyc.get('counts')=={'live':1,'untested':4,'blocked':5,'dominated':1},'cycle counts moved')
    cur=s.get('current',{})
    req(cur.get('unit')=='36-09E' and cur.get('next_exact_leaf')=='36-09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT','36-09E routing moved')
    req(cur.get('36_09E_entry_allowed') is True and cur.get('result')=='READY_UNSTARTED_AFTER_36_09D_HOSTILE_PASS','36-09E gate moved')
    gates=s.get('promotion_gates',{})
    req(gates.get('q_defined_pencil_fibration_exact') is True and gates.get('generic_fiber_genus3_exact') is True and gates.get('elliptic_character_quotients_exact') is True,'36-09D structural gates lost')
    for k in ['uniform_mordell_weil_control_proved','uniform_finite_ramification_support_proved','finite_exhaustive_H_twist_family_proved','local_solubility_filter_exhaustive','all_global_survivors_closed','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        req(gates.get(k) is False,f'promotion gate leaked: {k}')
    req(all(v is False for v in s.get('claims',{}).values()),'V21 higher claim leaked')

    print('PASS STAGE36_36_09D_AUDITED_SUCCESSOR_REPLAY')
    print(f'head={HEAD}; hostile_audit={AUDIT_REVIEW}; exact_head_ci={CI_RUN}/{CI_JOB}; authority_merge={LEGACY_COMMIT}; current_base={CURRENT_BASE}; cert={CERT_BLOB}')
    print('authority=HOSTILE_AUDIT_PASS; B6=LIVE_GENUS3_ELLIPTIC; next=36-09E ready-unstarted')

if __name__=='__main__':
    main()
