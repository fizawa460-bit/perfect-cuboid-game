#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09C/single-place-direct-receiver-obstruction-preflight.json'
CERT_BLOB='67fd5cd61ef35582dce32811aac4bebdb9356138'
LEGACY_COMMIT='676700d2fe1dc179053a79bb99536827d82ecfb1'
LEGACY_BLOB='73120d12b771a8f3a9b141bb8536c3b2ed292dc0'
CURRENT_BASE='5ab9318d9d8845b8dd48ffb08ac460691cc9ddb4'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V19_THIN_36_09C_AUDITED'
HEAD='ac5a7c81d3f268bebbc2a9de8e658b23c97d5649'
CI_RUN=33954373555
CI_JOB=101274880776
AUDIT_REVIEW=5120420108
LEGAL='BLOCKED_SINGLE_PLACE_ROUTE_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS'


def blob_bytes(b:bytes)->str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def blob_file(p:Path)->str:
    return blob_bytes(p.read_bytes())

def req(ok:bool,msg:str)->None:
    if not ok:
        raise SystemExit(msg)

def git_show(spec:str)->bytes:
    return subprocess.check_output(['git','show',spec],cwd=ROOT)


def main()->None:
    req(blob_file(CERT)==CERT_BLOB,'36-09C certificate blob drift')
    c=json.loads(CERT.read_text())
    req(c.get('schema')=='STAGE36_36_09C_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_PREFLIGHT_V1','36-09C certificate schema moved')
    req(c.get('single_place_route_decision',{}).get('legal_outcome')==LEGAL,'36-09C legal outcome moved')
    lemma=c.get('all_place_local_point_lemma',{})
    req(lemma.get('ALL_PLACES_ENDPOINT_OPEN_LOCALLY_SOLUBLE') is True,'36-09C all-place endpoint local solubility moved')
    req(lemma.get('ALL_PLACES_EACH_AUDITED_RECEIVER_IMAGE_LOCALLY_NONEMPTY') is True,'36-09C quotient local image nonemptiness moved')
    req(c.get('single_place_route_decision',{}).get('SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_POSSIBLE') is False,'36-09C B2 block moved')
    fire=c.get('local_global_firewall',{})
    for k in ['ONE_GLOBAL_Q_POINT_CONSTRUCTED','SAME_RATIONAL_POINT_USED_AT_ALL_PLACES','BRAUER_MANIN_NONOBSTRUCTION_PROVED','ETALE_BRAUER_NONOBSTRUCTION_PROVED','QUOTIENT_Q_POINT_EXISTENCE_PROVED','ENDPOINT_Q_POINT_EXISTENCE_PROVED']:
        req(fire.get(k) is False,f'36-09C local/global firewall leaked: {k}')
    cyc=c.get('post_block_cycle_audit',{})
    req(cyc.get('EXHAUSTIVE_VIEW_AUDIT') is True and cyc.get('BLIND_REDISCOVERY') is True,'36-09C breadth refresh moved')
    req(cyc.get('selected_next_candidate')=='B6_FIBRATION_TO_CURVE_BASE','36-09D/B6 selection moved')
    req(cyc.get('next_route_after_hostile_audit')=='36-09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT','36-09D route moved')
    req(all(v is False for v in c.get('claims',{}).values()),'36-09C higher claim leaked')

    legacy=git_show(f'{LEGACY_COMMIT}:stages/stage36/MAIN-STATE.json')
    req(blob_bytes(legacy)==LEGACY_BLOB,'legacy V18 state blob drift')
    old=json.loads(legacy)
    req(old.get('schema')=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V18_36_09C_PENDING_HOSTILE_AUDIT','legacy V18 schema moved')
    req(old.get('status')=='ACTIVE_PENDING_HOSTILE_AUDIT','legacy V18 hostile lifecycle moved')
    ou=old.get('authority_frontier',{}).get('36-09C',{})
    req(ou.get('promotion_status')=='PROVISIONAL_NOT_AUDITED','legacy 36-09C provisional authority moved')
    req(ou.get('certificate_blob_sha')==CERT_BLOB and ou.get('legal_outcome')==LEGAL,'legacy 36-09C result moved')
    req(ou.get('ALL_PLACES_ENDPOINT_OPEN_LOCALLY_SOLUBLE') is True,'legacy local-solubility theorem moved')
    req(ou.get('SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_POSSIBLE') is False,'legacy B2 decision moved')
    oc=old.get('current',{})
    req(oc.get('unit')=='36-09C' and oc.get('36_09D_entry_allowed') is False,'legacy hostile boundary before 36-09D moved')

    s=json.loads(STATE.read_text())
    req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE' and s.get('base_main_sha')==CURRENT_BASE,'V19 lifecycle/base moved')
    ls=s.get('legacy_authority_snapshot',{})
    req(ls.get('commit')==LEGACY_COMMIT and ls.get('blob_sha')==LEGACY_BLOB,'V19 legacy snapshot lock moved')
    fs=s.get('freshness_sync_36_09C_promotion',{})
    req(fs.get('main_sha')==CURRENT_BASE and fs.get('advanced_from')==LEGACY_COMMIT,'36-09C promotion freshness moved')
    a=s.get('authority_frontier',{}).get('36-09C',{})
    expected={
        'status':'AUDITED_BLOCKED_SINGLE_PLACE_ROUTE_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS',
        'pr':1587,
        'hostile_audit_review':AUDIT_REVIEW,
        'audited_head':HEAD,
        'exact_head_ci':f'{CI_RUN}/{CI_JOB}',
        'certificate_blob_sha':CERT_BLOB,
        'merged_main_sha':LEGACY_COMMIT,
        'legal_outcome':LEGAL,
        'ALL_PLACES_ENDPOINT_OPEN_LOCALLY_SOLUBLE':True,
        'ALL_PLACES_EACH_AUDITED_RECEIVER_IMAGE_LOCALLY_NONEMPTY':True,
        'SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_POSSIBLE':False,
        'EXHAUSTIVE_VIEW_AUDIT':True,
        'BLIND_REDISCOVERY':True,
        'verdict':'HOSTILE_AUDIT_PASS'
    }
    req(a==expected,'36-09C audited authority block moved')
    cyc=s.get('cycle_ledger',{})
    req(cyc.get('B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION')=='BLOCKED_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS','B2 audited block moved')
    req(cyc.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE','B6 not live after 36-09C promotion')
    req(cyc.get('counts')=={'live':1,'untested':4,'blocked':5,'dominated':1},'cycle counts moved')
    req(cyc.get('EXHAUSTIVE_VIEW_AUDIT') is True and cyc.get('BLIND_REDISCOVERY') is True,'V19 breadth locks moved')
    cur=s.get('current',{})
    req(cur.get('unit')=='36-09D' and cur.get('next_exact_leaf')=='36-09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT','36-09D routing moved')
    req(cur.get('36_09D_entry_allowed') is True and cur.get('36_06_entry_allowed') is False,'36-09D/36-06 gate moved')
    g=s.get('promotion_gates',{})
    for k in ['uniform_finite_ramification_support_proved','finite_exhaustive_H_twist_family_proved','local_solubility_filter_exhaustive','all_global_survivors_closed','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
        req(g.get(k) is False,f'promotion gate leaked: {k}')
    req(all(v is False for v in s.get('claims',{}).values()),'V19 higher claim leaked')
    print('PASS STAGE36_36_09C_AUDITED_SUCCESSOR_REPLAY')
    print(f'head={HEAD}; hostile_audit={AUDIT_REVIEW}; exact_head_ci={CI_RUN}/{CI_JOB}; authority_merge={LEGACY_COMMIT}; current_base={CURRENT_BASE}; cert={CERT_BLOB}')
    print('authority=HOSTILE_AUDIT_PASS; B2=BLOCKED; next=36-09D ready-unstarted')


if __name__=='__main__':
    main()
