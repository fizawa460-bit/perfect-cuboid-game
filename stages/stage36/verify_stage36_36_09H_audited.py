#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
AUDIT_BASE='29ce620a693f7cbdec48bce9b720cc02dfe5fa74'
AUDIT_HEAD='025cd5069eef938a42a5fd9cae0d2a4217ef8192'
AUDIT_REVIEW=5120981814
CI_RUN=33961255962
CI_JOB=101293415845
CERT_BLOB='08e7e87f866aebbc92b7d5cd776ce8b5fe60744d'
VERIFIER_BLOB='b9a3b1db57e8d9260922d29cf676d63f4a95bebc'
MERGE_PARENT='5e99bea45f495e9129e67af7bf0f2b43e7f14500'
MERGED_MAIN='c8b6bca818697125ef75a85527e282c15c6bd8f3'
MERGED_V28_BLOB='874a304ab20666451d9542f1c8dd71bc33ae68e2'
CURRENT_BASE='17c53d659e8d5d49b6e2bfca5c65c38a8658ac0d'
EXACT_TRANSFER_PATHS=[
 'stages/stage36/36-09H/common-jminus-factor-squareclass-descent-preflight.json',
 'stages/stage36/verify_stage36_36_09H.py',
 'stages/stage36/MAIN-STATE.json',
 '.github/workflows/stage36-bootstrap-audit.yml',
]

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def git(*args:str,check=True)->subprocess.CompletedProcess:
    return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=True)
def out(*args:str)->str:
    return git(*args).stdout.strip()
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def allowed_audit_race(p:str)->bool:
    return p.startswith('stages/stage33/') or p.startswith('.github/workflows/stage33')
def allowed_postmerge(p:str)->bool:
    return p.startswith('stages/stage35-ex/') or p.startswith('.github/workflows/stage35')

def main()->None:
    req(out('show','-s','--format=%P',MERGED_MAIN)==MERGE_PARENT,'36-09H squash merge parent moved')
    req(git('merge-base','--is-ancestor',AUDIT_BASE,MERGE_PARENT,check=False).returncode==0,'audit base not ancestor of merge parent')
    race=[p for p in out('diff','--name-only',AUDIT_BASE,MERGE_PARENT).splitlines() if p]
    req(race and all(allowed_audit_race(p) for p in race),f'audit race touched protected scope: {race}')
    post=[p for p in out('diff','--name-only',MERGED_MAIN,CURRENT_BASE).splitlines() if p]
    req(post and all(allowed_postmerge(p) for p in post),f'postmerge freshness touched protected scope: {post}')
    for p in EXACT_TRANSFER_PATHS:
        req(out('rev-parse',f'{AUDIT_HEAD}:{p}')==out('rev-parse',f'{MERGED_MAIN}:{p}'),f'audited blob not preserved by squash merge: {p}')
    req(out('rev-parse',f'{MERGED_MAIN}:stages/stage36/MAIN-STATE.json')==MERGED_V28_BLOB,'merged V28 blob moved')
    req(out('rev-parse',f'{AUDIT_HEAD}:stages/stage36/36-09H/common-jminus-factor-squareclass-descent-preflight.json')==CERT_BLOB,'audited certificate blob moved')
    req(out('rev-parse',f'{AUDIT_HEAD}:stages/stage36/verify_stage36_36_09H.py')==VERIFIER_BLOB,'audited verifier blob moved')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V29_THIN_36_09H_AUDITED','V29 schema moved')
    req(s['status']=='ACTIVE' and s['base_main_sha']==CURRENT_BASE,'V29 base/status moved')
    a=s['authority_frontier']['36-09H']
    req(a['status']=='AUDITED_EXACT_FOUR_FACTOR_S34_W01_FIRST_LAYER_BLOCK','36-09H audited status moved')
    req(a['pr']==1607 and a['hostile_audit_review']==AUDIT_REVIEW,'36-09H audit identity moved')
    req(a['audited_head']==AUDIT_HEAD and a['exact_head_ci']==f'{CI_RUN}/{CI_JOB}','36-09H audit head/CI moved')
    req(a['certificate_blob_sha']==CERT_BLOB and a['verifier_blob_sha']==VERIFIER_BLOB,'36-09H audited blobs moved')
    req(a['merged_main_sha']==MERGED_MAIN,'36-09H merge identity moved')
    req(a['UNBOUNDED_SHARED_ODD_PRIME_SUPPORT_PROVED'] is True,'shared-prime blocker lost')
    req(a['LOCAL_SUPPORT_CONSTRUCTION_IS_GLOBAL_RECEIVER_POINT'] is False,'local/global firewall leaked')
    req(a['S34_W01_TRIGGERED'] is False and a['S34_W01_FINITE_BRANCH_FAMILY_PROVED'] is False,'S34-W01 credit leaked')
    req(a['B10_STATUS']=='LIVE_RECEIVER_S34_W01_FIRST_LAYER_BLOCKED','B10 status moved')
    req(a['FRESH_BREADTH_REQUIRED'] is True and a['NEXT_ROUTE']=='36-09I_COMMON_JMINUS_POST_W01_BREADTH_REFRESH','breadth trigger moved')
    req(a['promotion_status']=='HOSTILE_AUDIT_PASS','promotion status moved')
    req(s['cycle_ledger']['counts']=={'live':1,'untested':3,'blocked':6,'dominated':1},'cycle counts moved')
    req(s['cycle_ledger']['fresh_EXHAUSTIVE_VIEW_AUDIT_after_36_09H'] is False,'breadth audit falsely precompleted')
    req(s['cycle_ledger']['fresh_BLIND_REDISCOVERY_after_36_09H'] is False,'blind rediscovery falsely precompleted')
    req(s['current']['unit']=='36-09I' and s['current']['36_09I_entry_allowed'] is True,'36-09I not unlocked')
    req(s['current']['next_exact_leaf']=='36-09I_COMMON_JMINUS_POST_W01_BREADTH_REFRESH','36-09I leaf moved')
    req(s['promotion_gates']['S34_W01_finite_squareclass_branch_family_proved'] is False,'finite branch credit leaked')
    req(s['promotion_gates']['R29_CAMP2_closed'] is False,'R29 credit leaked')
    req(all(v is False for v in s['claims'].values()),'higher credit leaked')
    print('PASS STAGE36_36_09H_HOSTILE_AUDITED_PROMOTION')
    print(f'audit_review={AUDIT_REVIEW}; audited_head={AUDIT_HEAD}; CI={CI_RUN}/{CI_JOB}')
    print('squash content preserved; race Stage33-only; postmerge Stage35-EX-only; 36-09I unlocked')

if __name__=='__main__': main()
