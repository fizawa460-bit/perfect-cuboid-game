#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
AUDIT_BASE='2f708b8f0b36483eb7ce19fbb4f7dcc6b9d9d0bc'
AUDIT_HEAD='476829b39679f4c380fe0458e37c28745e5f5621'
AUDIT_REVIEW=5121286430
FAIL_REVIEW=5121228524
CI_RUN=33965406417
CI_JOB=101304528893
CERT_BLOB='f9bf252f3be47f606a3b270961df3b5943fa1909'
VERIFIER_BLOB='8b6265849150519022e96a1f0c39e91eccfb32f0'
MERGE_PARENT='d6d49a7a5b7678442d5c26080926f3f80032c4d4'
MERGED_MAIN='dbd9ab95f1cf248a8a4704b205f62b8b96b1aefa'
MERGED_V30_BLOB='475c4c92a519b645a680527c043781f91f0ca5f9'
CURRENT_BASE='af2bcbe67f8ea71238829877c04a054d49ba2f11'
EXACT_TRANSFER_PATHS=[
 'stages/stage36/36-09I/blind-rediscovery-only.json',
 'stages/stage36/36-09I/post-w01-breadth-refresh.json',
 'stages/stage36/verify_stage36_36_09I.py',
 'stages/stage36/MAIN-STATE.json',
 '.github/workflows/stage36-bootstrap-audit.yml',
]
AUDIT_RACE_PATHS={
 '.github/workflows/stage33-v41-e3-source.yml',
 'stages/stage33/33-12/e3-v91c1a-a2-02-literal-boundary-seed-localization.json',
 'stages/stage33/33-12/verify_e3_v91c1a_a2_02_literal_boundary_seed_localization.py',
}
POSTMERGE_PATHS={
 '.github/workflows/stage32-post1588-hperp-nonexceptional-mod2-preflight.yml',
 '.github/workflows/stage33-v41-e3-source.yml',
 '.github/workflows/stage35-35-01-to-09-audit.yml',
 'AGENTS.md',
 'docs/research-os/README.md',
 'docs/research-os/policies/context-safe-file-inspection.md',
 'stages/stage32/residual-32-01-production/diagnose_stage32_post1588_hperp_nonexceptional_mod2.py',
 'stages/stage32/residual-32-01-production/post1588-hperp-nonexceptional-mod2-witness-source-note.md',
 'stages/stage32/residual-32-01-production/post1588-hperp-nonexceptional-mod2-witness.json',
 'stages/stage32/residual-32-01-production/verify_stage32_post1588_hperp_nonexceptional_mod2_witness.py',
 'stages/stage33/33-12/verify_stage33_v91c1a_current_startup_v94.py',
 'stages/stage33/MAIN-STATE.json',
 'stages/stage33/sync_main_state.py',
 'stages/stage35-ex/35ex-35/goal4a-two-adic-automatic-square.json',
 'stages/stage35-ex/MAIN-STATE.json',
 'stages/stage35-ex/verify_stage35_ex_35_goal4a.py',
 'stages/stage35-ex/verify_stage35_ex_v35_legacy_replay.py',
 'stages/stage35-ex/verify_stage35_ex_v36_legacy_replay.py',
}

def req(ok:bool,msg:str)->None:
    if not ok: raise SystemExit(msg)
def git(*args:str,check=True)->subprocess.CompletedProcess:
    return subprocess.run(['git',*args],cwd=ROOT,check=check,capture_output=True,text=True)
def out(*args:str)->str:
    return git(*args).stdout.strip()
def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def changed(a:str,b:str)->set[str]:
    return {p for p in out('diff','--name-only',a,b).splitlines() if p}

def main()->None:
    req(out('show','-s','--format=%P',MERGED_MAIN)==MERGE_PARENT,'36-09I squash merge parent moved')
    req(git('merge-base','--is-ancestor',AUDIT_BASE,MERGE_PARENT,check=False).returncode==0,'audit base not ancestor of merge parent')
    race=changed(AUDIT_BASE,MERGE_PARENT)
    req(race==AUDIT_RACE_PATHS,f'audit race path set moved: {sorted(race)}')
    post=changed(MERGED_MAIN,CURRENT_BASE)
    req(post==POSTMERGE_PATHS,f'postmerge freshness path set moved: {sorted(post)}')
    for p in EXACT_TRANSFER_PATHS:
        req(out('rev-parse',f'{AUDIT_HEAD}:{p}')==out('rev-parse',f'{MERGED_MAIN}:{p}'),f'audited blob not preserved by squash merge: {p}')
    req(out('rev-parse',f'{MERGED_MAIN}:stages/stage36/MAIN-STATE.json')==MERGED_V30_BLOB,'merged V30 blob moved')
    req(out('rev-parse',f'{AUDIT_HEAD}:stages/stage36/36-09I/post-w01-breadth-refresh.json')==CERT_BLOB,'audited certificate blob moved')
    req(out('rev-parse',f'{AUDIT_HEAD}:stages/stage36/verify_stage36_36_09I.py')==VERIFIER_BLOB,'audited verifier blob moved')

    s=json.loads(STATE.read_text())
    req(s['schema']=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V31_THIN_36_09I_AUDITED','V31 schema moved')
    req(s['status']=='ACTIVE' and s['base_main_sha']==CURRENT_BASE,'V31 base/status moved')
    a=s['authority_frontier']['36-09I']
    req(a['status']=='AUDITED_FRESH_BREADTH_RECIPROCAL_INVOLUTION_TWO_LINEAR_COVER','36-09I audited status moved')
    req(a['pr']==1611 and a['hostile_reaudit_review']==AUDIT_REVIEW and a['hostile_audit_fail_review']==FAIL_REVIEW,'36-09I audit identity moved')
    req(a['audited_head']==AUDIT_HEAD and a['exact_head_ci']==f'{CI_RUN}/{CI_JOB}','36-09I audit head/CI moved')
    req(a['certificate_blob_sha']==CERT_BLOB and a['verifier_blob_sha']==VERIFIER_BLOB,'36-09I audited blobs moved')
    req(a['merged_main_sha']==MERGED_MAIN,'36-09I merge identity moved')
    req(a['BLIND_PROVENANCE_FAIL_CLOSED'] is True and a['FRESH_EXHAUSTIVE_VIEW_AUDIT'] is True and a['FRESH_BLIND_REDISCOVERY'] is True,'breadth provenance lost')
    req(a['RECIPROCAL_TWO_LINEAR_REDUCTION_EXACT'] is True and a['PHYSICAL_RECONSTRUCTION_XZ_PLUS_MINUS_2_EXACT'] is True,'reciprocal reduction credit moved')
    req(a['CHARACTER_LINEAR_INTERMEDIATE_REFINEMENT_EXISTS'] is False,'character-linear firewall moved')
    req(a['B3_STATUS']=='LIVE_RECIPROCAL_INVOLUTION_COVER_PREFLIGHT','B3 status moved')
    req(a['B7_STATUS']=='UNTESTED_STANDARD_CAMPEDELLI_MODEL_ARITHMETIC_TRANSFER','B7 status moved')
    req(a['C2_GAUSSIAN_NORM_COMPRESSION_STATUS']=='UNTESTED_DISTINCT_FROM_B7_NO_EXACT_EQUIVALENCE','C2 status moved')
    req(a['B7_C2_EXACT_EQUIVALENCE_PROVED'] is False and a['B7_C2_EXACT_IMPLICATION_EITHER_DIRECTION_PROVED'] is False,'B7/C2 unsupported transfer leaked')
    req(a['B11_STATUS']=='UNTESTED_VARIABLE_PRIME_RECIPROCITY','B11 status moved')
    req(a['S31_W01_TRIGGERED'] is False and a['S34_W01_TRIGGERED'] is False and a['S34_W03_TRIGGERED'] is False,'Arsenal credit leaked')
    req(a['promotion_status']=='HOSTILE_REAUDIT_PASS','promotion status moved')
    req(s['cycle_ledger']['counts']=={'live':1,'untested':3,'blocked':6,'dominated':2},'cycle counts moved')
    req(s['cycle_ledger']['distinct_unmapped_candidates']==['C2_GAUSSIAN_NORM_COMPRESSION'],'distinct candidate preservation moved')
    req(s['current']['unit']=='36-09J' and s['current']['36_09J_entry_allowed'] is True,'36-09J not unlocked')
    req(s['current']['next_exact_leaf']=='36-09J_RECIPROCAL_INVOLUTION_TWO_LINEAR_COVER_PREFLIGHT','36-09J leaf moved')
    req(s['promotion_gates']['generic_cover_genera_classified'] is False,'generic cover genus credit leaked')
    req(s['promotion_gates']['receiver_emptiness_proved'] is False and s['promotion_gates']['R29_CAMP2_closed'] is False,'receiver/theorem credit leaked')
    req(all(v is False for v in s['claims'].values()),'higher credit leaked')
    print('PASS STAGE36_36_09I_HOSTILE_REAUDITED_PROMOTION')
    print(f'audit_review={AUDIT_REVIEW}; audited_head={AUDIT_HEAD}; CI={CI_RUN}/{CI_JOB}')
    print('squash content preserved; freshness non-Stage36 only; B3 live; B7/C2/B11 separately untested; 36-09J unlocked')

if __name__=='__main__': main()
