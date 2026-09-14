#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent.parent
CONTRACT=HERE/'bc2-40-resume-first-contract.json'
WORKER=HERE/'bc2_40_replay_parent_unit.py'
AGG=HERE/'bc2_40_resume_aggregate.py'
HELPER=HERE/'bc2_40_resume_execute.py'
WORKFLOW=ROOT/'.github/workflows/stage32-ex5-bc2-40-resume.yml'
LEGACY_WORKFLOW=ROOT/'.github/workflows/stage32-ex5-main.yml'
RUNKEY=HERE.parent/'runkeys'/'bc2-40-fresh-unknown23-replay.json'

CONTRACT_BLOB='220edb27584ea99899e7e3f129869f1a1b7719a2'
CONTRACT_CANON='ff2106909f7d9e02c7300127f10463e7d4fc3415e300c10f1e8aad712b133ca1'
WORKER_BLOB='a28061b99527c6585c3f4016992d1ef6e47b42de'
AGG_BLOB='76c1d5e9f45d113ccb17e8149b2d840e2278b301'
HELPER_BLOB='5b262f1c05d82ae3203a689522f476d83406dbb8'
WORKFLOW_BLOB='425b0d72f1a654f53b16bf086c537e79335d6263'
TARGET_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
RUNKEY_V2='STAGE32EX5_BC2_40_RESUME_RUNKEY_V2'
LEGACY_V1='STAGE32EX5_BC2_40_FRESH_UNKNOWN23_REPLAY_RUNKEY_V1'

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    req(blob(CONTRACT)==CONTRACT_BLOB,'contract blob')
    c=json.loads(CONTRACT.read_text())
    req(c.get('schema')=='STAGE32EX5_BC2_40_RESUME_FIRST_CONTRACT_V2','schema')
    req(c.get('status')=='RESUME_FIRST_WORKFLOW_MIGRATED_NOT_ARMED','status')
    req(c.get('canonical_sha256_without_this_field')==CONTRACT_CANON and canon(c)==CONTRACT_CANON,'contract canonical')
    req(blob(WORKER)==WORKER_BLOB and c['partition']['unit_worker_git_blob_sha']==WORKER_BLOB,'worker lock')
    req(blob(AGG)==AGG_BLOB and c['aggregation']['git_blob_sha']==AGG_BLOB,'aggregate lock')
    req(blob(HELPER)==HELPER_BLOB and c['execution_helper']['git_blob_sha']==HELPER_BLOB,'helper lock')
    req(blob(WORKFLOW)==WORKFLOW_BLOB and c['workflow']['git_blob_sha']==WORKFLOW_BLOB,'workflow lock')
    req(c['partition']['key']=='parent_index' and c['partition']['expected_unit_count']==23 and c['partition']['finer_exact_partition_feasible'] is True,'partition')
    req(c['target']['audited_unknown_parent_indices_sha256']==TARGET_SHA,'target hash')
    req(c['execution_helper']['runkey_schema']==RUNKEY_V2 and c['execution_helper']['schedules_only_missing_parent_indices'] is True,'resume helper semantics')
    req(c['recovery']['monolithic_rerun_default'] is False and c['recovery']['fresh_runkey_generation_required'] is True,'recovery')
    wr=c['workflow_requirements']
    req(wr['partial_upload_if_always_or_equivalent_required'] is True and wr['effective_heavy_concurrency']==1,'workflow requirements')
    req(wr['authorization_commit_range']=='github.event.before..github.event.pull_request.head.sha','event-range authorization contract')
    req(wr['authorization_requires_runkey_path_in_event_range'] is True and wr['reopened_cold_by_default'] is True and wr['initial_opened_cold_unless_semantically_armed'] is True,'event-range cold semantics')
    req(c['storage_preflight']['within_budget'] is True and c['storage_preflight']['projected_peak_new_storage_bytes']<=c['storage_preflight']['repository_operating_budget_bytes'],'storage')
    a=c['authorization']
    req(a['workflow_migrated'] is True and a['runkey_armed'] is False and a['heavy_execution_authorized'] is False and a['main_promotion_authorized'] is False and a['merge_authorized'] is False,'contract grants no execution authorization')
    req(all(v is False for v in c['firewalls'].values()),'credit firewalls')

    if RUNKEY.exists():
        rk=json.loads(RUNKEY.read_text())
        req(rk.get('schema')==RUNKEY_V2,'only V2 runkey may coexist with migrated workflow')
        req(rk.get('canonical_sha256_without_this_field')==canon(rk),'V2 runkey canonical')

    wf=WORKFLOW.read_text()
    req('# Trigger lifecycle: ACTIVE_AUTO' in wf,'workflow lifecycle')
    req(RUNKEY_V2 in wf and 'authorize-bc2-40-resume-v2:' in wf and '\n  bc2-40-resume-heavy:' in wf,'V2 semantic gate')
    req('LIVE-MAIN-COORDINATION-SYNC-20260915.json' in wf,'V34 live-main sync path')
    req(wf.count('ref: ${{ github.event.pull_request.head.sha }}')==3,'all BC2-40 jobs must checkout exact PR head')
    req('BEFORE: ${{ github.event.before }}' in wf and 'HEAD_SHA: ${{ github.event.pull_request.head.sha }}' in wf,'event range env')
    req("['git','diff','--name-only',before,head]" in wf and "['git','show',before+':'+str(key)]" in wf,'event range diff/old-key lookup')
    req("['git','fetch','--no-tags','--depth=1','origin',before]" in wf,'event before fetch')
    req('HEAD^' not in wf,'HEAD-caret delta must not authorize heavy')
    req('bc2_40_resume_execute.py' in wf and 'bc2_40_replay_explicit_fresh_unknown23.py --output' not in wf,'resume helper replaces monolithic execution')
    req(wf.count('if: always()')>=3,'salvage/failure steps must be always')
    req(wf.count('retention-days: 2')==2,'artifact retention')
    req('matrix:' not in wf,'no heavy matrix scaleout')
    req("effective_heavy_concurrency')==1" in wf and "heavy_scaleout_authorized') is False" in wf,'semantic concurrency gate')

    legacy=LEGACY_WORKFLOW.read_text()
    req('authorize-bc2-40-fresh-unknown23:' not in legacy and '\n  bc2-40-fresh-unknown23:' not in legacy,'legacy V1 runtime jobs must remain removed')
    req(LEGACY_V1 not in legacy and RUNKEY_V2 not in legacy,'legacy workflow must not recognize BC2-40 runkey schemas')
    w=c['workflow']
    req(w['legacy_v1_monolithic_gate']=='REMOVED_FROM_STAGE32_EX5_MAIN' and w['legacy_runtime_jobs_removed'] is True and w['legacy_workflow_path']=='.github/workflows/stage32-ex5-main.yml','legacy gate removal contract')

    subprocess.run([sys.executable,'-m','py_compile',str(WORKER),str(AGG),str(HELPER)],check=True)
    print('PASS: BC2-40 resume-first V2 workflow uses exact github.event.before..PR-head runkey authorization; parent-index partition=23; contract arms no heavy execution')

if __name__=='__main__':
    main()
