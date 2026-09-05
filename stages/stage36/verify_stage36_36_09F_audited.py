#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09F/paired-legendre-receiver-intersection-preflight.json'
CERT_BLOB='0615844de212eb3644f15cd3f5577b37ccc3855a'
LEGACY_COMMIT='7b3a5f54b63f52a8707d85003024f6dfafb580fd'
LEGACY_BLOB='b9ebbe0e5d813af5ff22d4c47fc94fb84fd6e78c'
AUDIT_BASE='3b4b5969330ae89a41899598fbdf17e76be76f72'
INTERVENING_MAIN='e21378e59f7f1076a7ad71d34cee1fd0ac3a5cb3'
CURRENT_BASE='7b3a5f54b63f52a8707d85003024f6dfafb580fd'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V25_THIN_36_09F_AUDITED'
HEAD='a3f6380a89e627a9fa36915466a901361e0cb175'
CI_RUN=33958206747
CI_JOB=101285265805
AUDIT_REVIEW=5120699559

def blob_bytes(b:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def blob_file(p:Path)->str:
    return blob_bytes(p.read_bytes())
def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def git_show(spec:str)->bytes:
    return subprocess.check_output(['git','show',spec],cwd=ROOT)
def git_lines(*args:str)->list[str]:
    out=subprocess.check_output(['git',*args],cwd=ROOT,text=True)
    return [x for x in out.splitlines() if x]

def main()->None:
    req(blob_file(CERT)==CERT_BLOB,'36-09F certificate blob drift')
    c=json.loads(CERT.read_text())
    req(c.get('schema')=='STAGE36_36_09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT_V1','36-09F certificate schema moved')
    sc=c.get('squareclass_linear_system',{})
    req(sc.get('rank_F2')==4 and sc.get('kernel_dimension')==0,'36-09F rank/kernel moved')
    req(sc.get('only_squareclass_solution')==['0','0','0','0'],'36-09F squareclass solution moved')
    seven=c.get('seven_line_reconstruction',{})
    req(seven.get('paired_four_equations_force_all_moving_line_values_square') is True,'36-09F moving-line implication moved')
    req(seven.get('therefore_all_seven_line_values_square') is True and seven.get('converse_checked') is True,'36-09F endpoint equivalence moved')
    route=c.get('route_decision',{})
    req(route.get('B6_FIBRATION_TO_CURVE_BASE')=='BLOCKED_BY_EXACT_ENDPOINT_EQUIVALENCE_NO_PROPER_RECEIVER_GAIN','36-09F B6 block moved')
    req(route.get('cycle_route_status')=='BLOCKED_NEW_PATTERN_ISOLATED','36-09F cycle status moved')
    req(route.get('S34_W03_INTERSECTION_EXCLUSION_EXECUTED') is False,'36-09F S34-W03 falsely executed')
    req(route.get('S34_W01_TRIGGERED') is False and route.get('S34_W02_TRIGGERED') is False,'36-09F Arsenal trigger moved')
    req(route.get('next_route_after_hostile_audit')=='36-09G_ENDPOINT_EQUIVALENCE_BREADTH_REFRESH','36-09G route moved')
    cu=c.get('cycle_update',{})
    req(cu.get('new_material_block') is True and cu.get('fresh_breadth_audit_required_now') is True,'36-09F breadth trigger moved')
    req(cu.get('live_candidates_after_block')==0 and len(cu.get('untested_candidates_preserved',[]))==4,'36-09F post-block ledger moved')
    req(cu.get('fresh_EXHAUSTIVE_VIEW_AUDIT_after_36_09F') is False and cu.get('fresh_BLIND_REDISCOVERY_after_36_09F') is False,'36-09F falsely completed breadth')
    req(all(v is False for v in c.get('claims',{}).values()),'36-09F higher claim leaked')

    legacy=git_show(f'{LEGACY_COMMIT}:stages/stage36/MAIN-STATE.json')
    req(blob_bytes(legacy)==LEGACY_BLOB,'legacy V24 state blob drift')
    old=json.loads(legacy)
    req(old.get('schema')=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V24_36_09F_PENDING_HOSTILE_AUDIT','legacy V24 schema moved')
    req(old.get('status')=='ACTIVE_PENDING_HOSTILE_AUDIT','legacy V24 hostile lifecycle moved')
    oa=old.get('authority_frontier',{}).get('36-09F',{})
    req(oa.get('promotion_status')=='PROVISIONAL_NOT_AUDITED','legacy 36-09F provisional authority moved')
    req(oa.get('certificate_blob_sha')==CERT_BLOB,'legacy 36-09F certificate lock moved')
    req(old.get('current',{}).get('36_09G_entry_allowed') is False,'legacy hostile boundary before 36-09G moved')

    changed=git_lines('diff','--name-only',AUDIT_BASE,INTERVENING_MAIN)
    req(bool(changed),'expected intervening main advance missing')
    allowed_prefixes=('stages/stage35-ex/','.github/workflows/stage35-')
    bad=[p for p in changed if not p.startswith(allowed_prefixes)]
    req(not bad,'authority-sensitive path changed between audit base and merge: '+','.join(bad))
    pp=git_lines('show','-s','--format=%P',LEGACY_COMMIT)[0].split()
    req(pp==[INTERVENING_MAIN,HEAD],f'36-09F merge parents moved: {pp}')

    s=json.loads(STATE.read_text())
    req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE' and s.get('base_main_sha')==CURRENT_BASE,'V25 lifecycle/base moved')
    ls=s.get('legacy_authority_snapshot',{})
    req(ls.get('commit')==LEGACY_COMMIT and ls.get('blob_sha')==LEGACY_BLOB,'V25 legacy snapshot lock moved')
    fs=s.get('freshness_sync_36_09F_promotion',{})
    req(fs.get('audit_base_main_sha')==AUDIT_BASE and fs.get('intervening_main_sha')==INTERVENING_MAIN and fs.get('merged_main_sha')==LEGACY_COMMIT,'36-09F freshness sync moved')
    a=s.get('authority_frontier',{}).get('36-09F',{})
    req(a.get('status')=='AUDITED_EXACT_PAIRED_RECEIVER_EQUALS_FULL_ENDPOINT_KUMMER_CONDITION_BLOCK','36-09F audited status moved')
    req(a.get('pr')==1597 and a.get('hostile_audit_review')==AUDIT_REVIEW,'36-09F audit identity moved')
    req(a.get('audited_head')==HEAD and a.get('exact_head_ci')==f'{CI_RUN}/{CI_JOB}','36-09F exact head/CI moved')
    req(a.get('certificate_blob_sha')==CERT_BLOB and a.get('merged_main_sha')==LEGACY_COMMIT,'36-09F cert/merge lock moved')
    for k in ['FOUR_PAIRED_LEGENDRE_RHS_EXACT','SQUARECLASS_MATRIX_RANK4','FOUR_PRODUCTS_IFF_FOUR_MOVING_LINES_SQUARE','PHYSICAL_BASE_PLUS_PAIRED_RECEIVER_IFF_FULL_SEVEN_LINE_LIFT','FRESH_BREADTH_AUDIT_REQUIRED']:
        req(a.get(k) is True,f'36-09F audited claim moved: {k}')
    req(a.get('B6_STATUS')=='BLOCKED_BY_EXACT_ENDPOINT_EQUIVALENCE_NO_PROPER_RECEIVER_GAIN','36-09F audited B6 moved')
    req(a.get('promotion_status')=='HOSTILE_AUDIT_PASS' and a.get('verdict')=='HOSTILE_AUDIT_PASS','36-09F audit promotion moved')

    cyc=s.get('cycle_ledger',{})
    req(cyc.get('B6_FIBRATION_TO_CURVE_BASE')=='BLOCKED_BY_EXACT_ENDPOINT_EQUIVALENCE_NO_PROPER_RECEIVER_GAIN','B6 audited block moved')
    req(cyc.get('counts')=={'live':0,'untested':4,'blocked':6,'dominated':1},'cycle counts moved')
    req(cyc.get('fresh_breadth_audit_required_now') is True,'breadth refresh requirement lost')
    cur=s.get('current',{})
    req(cur.get('unit')=='36-09G' and cur.get('next_exact_leaf')=='36-09G_ENDPOINT_EQUIVALENCE_BREADTH_REFRESH','36-09G routing moved')
    req(cur.get('36_09G_entry_allowed') is True and cur.get('result')=='READY_UNSTARTED_AFTER_36_09F_HOSTILE_PASS','36-09G gate moved')
    gates=s.get('promotion_gates',{})
    req(gates.get('paired_receiver_endpoint_kummer_equivalence_exact') is True,'36-09F structural gate lost')
    for k in ['paired_legendre_receiver_intersection_empty_proved','uniform_mordell_weil_control_proved','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        req(gates.get(k) is False,f'promotion gate leaked: {k}')
    req(all(v is False for v in s.get('claims',{}).values()),'V25 higher claim leaked')

    print('PASS STAGE36_36_09F_AUDITED_SUCCESSOR_REPLAY')
    print(f'head={HEAD}; hostile_audit={AUDIT_REVIEW}; exact_head_ci={CI_RUN}/{CI_JOB}; authority_merge={LEGACY_COMMIT}; cert={CERT_BLOB}')
    print('authority=HOSTILE_AUDIT_PASS; B6=BLOCKED_ENDPOINT_EQUIVALENCE; next=36-09G ready-unstarted')

if __name__=='__main__': main()
