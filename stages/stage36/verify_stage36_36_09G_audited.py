#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
G=ROOT/'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json'
BLIND=ROOT/'stages/stage36/36-09G/blind-rediscovery-only.json'
BASE='9309801b9caffa857adc5599ad5dd686d84d47d8'
AUDITED_HEAD='400237172efffe75232d485d0ce96e4643002a72'
AUDIT_REVIEW=5120849260
CI_RUN=33960137385
CI_JOB=101290482391
CERT_BLOB='bae34622d8ab7f94fafab4a290e770a3830e47fc'
BLIND_BLOB='3f00245edc26394d43a16a699d99634eed831909'
MERGE_PARENT='c8a876838882c91c078c85da5c88d131b151ac40'
MERGED_MAIN='605ef83aae1ba2804537eb6dc36695ca80ade412'
MERGED_V26_BLOB='d50e7ce0e67984bb8598fa1b67d1e86b245ac492'
EXACT_TRANSFER_PATHS=[
 'stages/stage36/36-09G/blind-rediscovery-only.json',
 'stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json',
 'stages/stage36/verify_stage36_36_09G.py',
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

def main()->None:
    # Squash-merge provenance: exact audited content, not false ancestor semantics.
    req(out('show','-s','--format=%P',MERGED_MAIN)==MERGE_PARENT,'36-09G merge parent moved')
    req(git('merge-base','--is-ancestor',BASE,MERGE_PARENT,check=False).returncode==0,'audit base not ancestor of merge parent')
    changed=[x for x in out('diff','--name-only',BASE,MERGE_PARENT).splitlines() if x]
    req(changed,'expected nonempty audit-to-merge freshness gap')
    allowed=lambda p: p.startswith('stages/stage35-ex/') or p.startswith('.github/workflows/stage35')
    req(all(allowed(p) for p in changed),f'36-09G freshness gap touched protected scope: {[p for p in changed if not allowed(p)]}')
    for p in EXACT_TRANSFER_PATHS:
        a=out('rev-parse',f'{AUDITED_HEAD}:{p}')
        m=out('rev-parse',f'{MERGED_MAIN}:{p}')
        req(a==m,f'squash merge did not preserve audited blob: {p}')
    req(out('rev-parse',f'{MERGED_MAIN}:stages/stage36/MAIN-STATE.json')==MERGED_V26_BLOB,'merged V26 blob moved')
    req(out('rev-parse',f'{AUDITED_HEAD}:stages/stage36/36-09G/endpoint-equivalence-breadth-refresh.json')==CERT_BLOB,'audited certificate blob moved')
    req(out('rev-parse',f'{AUDITED_HEAD}:stages/stage36/36-09G/blind-rediscovery-only.json')==BLIND_BLOB,'audited blind blob moved')

    # Re-run exact 36-09G mathematics/provenance checker on the promotion head.
    subprocess.run(['python3','stages/stage36/verify_stage36_36_09G.py'],cwd=ROOT,check=True)
    req(blob(G)==CERT_BLOB,'working 36-09G certificate drift')
    req(blob(BLIND)==BLIND_BLOB,'working blind snapshot drift')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V27_THIN_36_09G_AUDITED','V27 schema moved')
    req(s['status']=='ACTIVE','V27 status moved')
    req(s['base_main_sha']==MERGED_MAIN,'V27 base moved')
    a=s['authority_frontier']['36-09G']
    req(a['status']=='AUDITED_FRESH_BREADTH_COMMON_JMINUS_SUBRECEIVER','36-09G audited status moved')
    req(a['pr']==1602 and a['hostile_reaudit_review']==AUDIT_REVIEW,'36-09G audit identity moved')
    req(a['audited_head']==AUDITED_HEAD,'36-09G audited head moved')
    req(a['exact_head_ci']==f'{CI_RUN}/{CI_JOB}','36-09G audit CI moved')
    req(a['certificate_blob_sha']==CERT_BLOB and a['blind_snapshot_blob_sha']==BLIND_BLOB,'36-09G audited blobs moved')
    req(a['merged_main_sha']==MERGED_MAIN,'36-09G merged main moved')
    req(a['BLIND_PROVENANCE_FAIL_CLOSED'] is True,'blind provenance credit lost')
    req(a['B10_STATUS']=='LIVE_COMMON_TWO_JMINUS_SUBRECEIVER','B10 audited live status moved')
    req(a['S34_W01_STATUS']=='APPLICABILITY_CANDIDATE_PREFLIGHT_REQUIRED' and a['S34_W01_TRIGGERED'] is False,'S34-W01 audit boundary moved')
    req(a['COMMON_SUBRECEIVER_RATIONAL_STRICTNESS_PROVED'] is False,'rational strictness falsely promoted')
    req(a['promotion_status']=='HOSTILE_REAUDIT_PASS','36-09G promotion status moved')
    req(s['cycle_ledger']['counts']=={'live':1,'untested':3,'blocked':6,'dominated':1},'audited cycle counts moved')
    req(s['current']['unit']=='36-09H' and s['current']['36_09H_entry_allowed'] is True,'36-09H not unlocked')
    req(s['current']['next_exact_leaf']=='36-09H_COMMON_JMINUS_FACTOR_SQUARECLASS_DESCENT_PREFLIGHT','36-09H next leaf moved')
    req(s['promotion_gates']['common_jminus_subreceiver_rational_strictness_proved'] is False,'strictness gate leaked')
    req(s['promotion_gates']['S34_W01_finite_squareclass_branch_family_proved'] is False,'finite branch credit leaked')
    req(s['promotion_gates']['R29_CAMP2_closed'] is False,'R29-CAMP2 credit leaked')
    req(all(v is False for v in s['claims'].values()),'higher Stage36 credit leaked')
    av=s['audit_verifier']
    req(av['path']=='stages/stage36/verify_stage36_36_09G_audited.py','audit verifier path moved')
    req(av['blob_sha']==blob(ROOT/av['path']),'audit verifier self-blob mismatch')

    print('PASS STAGE36_36_09G_HOSTILE_AUDITED_PROMOTION')
    print(f'audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}; CI={CI_RUN}/{CI_JOB}')
    print('squash merge content preserved exactly; freshness gap Stage35-EX only; B10 live; 36-09H unlocked')

if __name__=='__main__': main()
