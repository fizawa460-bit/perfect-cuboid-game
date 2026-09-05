#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09E/character-elliptic-quotient-arithmetic-preflight.json'
CERT_BLOB='081b704fecaa3bd39e6a523ee7beaefe706683f4'
LEGACY_COMMIT='98764e37e408866386ef41cc526d830a6092462b'
LEGACY_BLOB='c15b6fe94742b9c9571c3810f3429be1d6e85a73'
AUDIT_BASE='bd402241fa69ea00d00b48695c883d1cbdbc2dbb'
INTERVENING_MAIN='3ec32ee3647d8c2a9350b1aea5aca1f8cee617a8'
CURRENT_BASE='98764e37e408866386ef41cc526d830a6092462b'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V23_THIN_36_09E_AUDITED'
HEAD='51efa8394c45bc60a4b482c4f6f94f7826eb9d20'
CI_RUN=33956972053
CI_JOB=101281945982
AUDIT_REVIEW=5120645782

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
    req(blob_file(CERT)==CERT_BLOB,'36-09E certificate blob drift')
    c=json.loads(CERT.read_text())
    req(c.get('schema')=='STAGE36_36_09E_CHARACTER_ELLIPTIC_QUOTIENT_ARITHMETIC_PREFLIGHT_V1','36-09E certificate schema moved')
    ps=c.get('physical_squareclass_restriction',{})
    req(ps.get('therefore_twist_factors_t_and_t_plus_1_are_rational_squares') is True,'36-09E physical twist collapse moved')
    req(ps.get('special_t1_status')=='ELIMINATED_FOR_ENDPOINT_IMAGE','36-09E endpoint t=1 status moved')
    par=c.get('physical_base_parameterization',{})
    req(par.get('t')=='(r^2-1)^2/(4*r^2)' and par.get('t_plus_1')=='(r^2+1)^2/(4*r^2)','36-09E physical base parameterization moved')
    collapse=c.get('four_family_collapse',{})
    req(collapse.get('occurrence_collapse_count')=={'genus1_occurrences':9,'physical_curve_point_types':4},'36-09E nine-to-four collapse moved')
    req(collapse.get('common_J_MINUS_pair_each_representative')==['E_t_PLUS','E_t_MINUS'],'36-09E common J-minus pair moved')
    req(collapse.get('J_PLUS_across_all_representatives_requires')==['E_t1_PLUS','E_t1_MINUS'],'36-09E J-plus +/- pair moved')
    pair=c.get('paired_receiver',{})
    req(pair.get('linear_compatibility')=='X_plus+X_minus=t+1','36-09E paired compatibility moved')
    req(pair.get('S34_W03_applicability_matched') is True and pair.get('S34_W03_intersection_exclusion_executed') is False,'36-09E S34-W03 firewall moved')
    route=c.get('route_decision',{})
    req(route.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE_PAIRED_LEGENDRE_PLUS_MINUS_RECEIVER_OVER_GENUS0_PHYSICAL_BASE','36-09E B6 outcome moved')
    req(route.get('next_route_after_hostile_audit')=='36-09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT','36-09F route moved')
    req(route.get('S34_W01_TRIGGERED') is False and route.get('S34_W02_TRIGGERED') is False,'36-09E Arsenal trigger firewall moved')
    req(all(v is False for v in c.get('claims',{}).values()),'36-09E higher claim leaked')

    legacy=git_show(f'{LEGACY_COMMIT}:stages/stage36/MAIN-STATE.json')
    req(blob_bytes(legacy)==LEGACY_BLOB,'legacy V22 state blob drift')
    old=json.loads(legacy)
    req(old.get('schema')=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V22_36_09E_PENDING_HOSTILE_AUDIT','legacy V22 schema moved')
    req(old.get('status')=='ACTIVE_PENDING_HOSTILE_AUDIT','legacy V22 hostile lifecycle moved')
    oa=old.get('authority_frontier',{}).get('36-09E',{})
    req(oa.get('promotion_status')=='PROVISIONAL_NOT_AUDITED','legacy 36-09E provisional authority moved')
    req(oa.get('certificate_blob_sha')==CERT_BLOB,'legacy 36-09E certificate lock moved')
    req(old.get('current',{}).get('36_09F_entry_allowed') is False,'legacy hostile boundary before 36-09F moved')

    changed=git_lines('diff','--name-only',AUDIT_BASE,INTERVENING_MAIN)
    req(bool(changed),'expected intervening main advance missing')
    allowed_prefixes=('stages/stage32/','stages/stage35-ex/','.github/workflows/stage32-','.github/workflows/stage35-')
    bad=[p for p in changed if not p.startswith(allowed_prefixes)]
    req(not bad,'authority-sensitive path changed between audit base and merge: '+','.join(bad))
    parents=git_lines('show','-s','--format=%P',LEGACY_COMMIT)
    req(len(parents)==1,'merge-parent read failed')
    pp=parents[0].split()
    req(pp==[INTERVENING_MAIN,HEAD],f'36-09E merge parents moved: {pp}')

    s=json.loads(STATE.read_text())
    req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE' and s.get('base_main_sha')==CURRENT_BASE,'V23 lifecycle/base moved')
    ls=s.get('legacy_authority_snapshot',{})
    req(ls.get('commit')==LEGACY_COMMIT and ls.get('blob_sha')==LEGACY_BLOB,'V23 legacy snapshot lock moved')
    fs=s.get('freshness_sync_36_09E_promotion',{})
    req(fs.get('audit_base_main_sha')==AUDIT_BASE and fs.get('intervening_main_sha')==INTERVENING_MAIN and fs.get('merged_main_sha')==LEGACY_COMMIT,'36-09E freshness sync moved')

    a=s.get('authority_frontier',{}).get('36-09E',{})
    req(a.get('status')=='AUDITED_EXACT_PHYSICAL_LEGENDRE_TWIST_COLLAPSE_AND_PAIRED_RECEIVER','36-09E audited status moved')
    req(a.get('pr')==1593 and a.get('hostile_audit_review')==AUDIT_REVIEW,'36-09E audit identity moved')
    req(a.get('audited_head')==HEAD and a.get('exact_head_ci')==f'{CI_RUN}/{CI_JOB}','36-09E exact head/CI moved')
    req(a.get('certificate_blob_sha')==CERT_BLOB and a.get('merged_main_sha')==LEGACY_COMMIT,'36-09E cert/merge lock moved')
    for k in ['PHYSICAL_T_AND_TPLUS1_SQUARES','PHYSICAL_T1_ELIMINATED','NINE_TO_FOUR_LEGENDRE_TWIST_COLLAPSE','PHYSICAL_BASE_GENUS0_PARAMETERIZED','PAIRED_SHARED_X_RECEIVER_EXACT','S34_W03_APPLICABILITY_MATCHED']:
        req(a.get(k) is True,f'36-09E audited claim moved: {k}')
    req(a.get('S34_W03_INTERSECTION_EXCLUSION_EXECUTED') is False,'36-09E S34-W03 execution falsely promoted')
    req(a.get('S34_W01_TRIGGERED') is False and a.get('S34_W02_TRIGGERED') is False,'36-09E Arsenal trigger falsely promoted')
    req(a.get('promotion_status')=='HOSTILE_AUDIT_PASS' and a.get('verdict')=='HOSTILE_AUDIT_PASS','36-09E audit promotion moved')

    cyc=s.get('cycle_ledger',{})
    req(cyc.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE_PAIRED_LEGENDRE_PLUS_MINUS_RECEIVER_OVER_GENUS0_PHYSICAL_BASE','B6 audited live status moved')
    req(cyc.get('counts')=={'live':1,'untested':4,'blocked':5,'dominated':1},'cycle counts moved')
    cur=s.get('current',{})
    req(cur.get('unit')=='36-09F' and cur.get('next_exact_leaf')=='36-09F_PAIRED_LEGENDRE_RECEIVER_INTERSECTION_PREFLIGHT','36-09F routing moved')
    req(cur.get('36_09F_entry_allowed') is True and cur.get('result')=='READY_UNSTARTED_AFTER_36_09E_HOSTILE_PASS','36-09F gate moved')
    gates=s.get('promotion_gates',{})
    req(gates.get('physical_legendre_twist_collapse_exact') is True and gates.get('physical_t1_eliminated') is True and gates.get('paired_legendre_receiver_exact') is True,'36-09E structural gates lost')
    for k in ['uniform_mordell_weil_control_proved','paired_legendre_receiver_intersection_empty_proved','uniform_finite_ramification_support_proved','finite_exhaustive_H_twist_family_proved','local_solubility_filter_exhaustive','all_global_survivors_closed','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        req(gates.get(k) is False,f'promotion gate leaked: {k}')
    req(all(v is False for v in s.get('claims',{}).values()),'V23 higher claim leaked')

    print('PASS STAGE36_36_09E_AUDITED_SUCCESSOR_REPLAY')
    print(f'head={HEAD}; hostile_audit={AUDIT_REVIEW}; exact_head_ci={CI_RUN}/{CI_JOB}; authority_merge={LEGACY_COMMIT}; cert={CERT_BLOB}')
    print('authority=HOSTILE_AUDIT_PASS; B6=LIVE_PAIRED_LEGENDRE; next=36-09F ready-unstarted')

if __name__=='__main__':
    main()
