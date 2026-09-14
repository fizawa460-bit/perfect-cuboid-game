#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
CONTRACT=HERE/'bc2-40-resume-first-contract.json'; WORKER=HERE/'bc2_40_replay_parent_unit.py'; AGG=HERE/'bc2_40_resume_aggregate.py'; RUNKEY=HERE.parent/'runkeys'/'bc2-40-fresh-unknown23-replay.json'
CONTRACT_BLOB='09f01149b3a5165ec226b67cd2d9c22c6edfcc91'; CONTRACT_CANON='d016c9bf836d73979efd80cfa622aadb2390645a673c8c259e7f1ce90a3ea4e6'; WORKER_BLOB='a28061b99527c6585c3f4016992d1ef6e47b42de'; AGG_BLOB='76c1d5e9f45d113ccb17e8149b2d840e2278b301'; TARGET_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None); return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    req(blob(CONTRACT)==CONTRACT_BLOB,'contract blob'); c=json.loads(CONTRACT.read_text()); req(c.get('schema')=='STAGE32EX5_BC2_40_RESUME_FIRST_CONTRACT_V1','schema'); req(c.get('canonical_sha256_without_this_field')==CONTRACT_CANON and canon(c)==CONTRACT_CANON,'contract canonical')
    req(blob(WORKER)==WORKER_BLOB and c['partition']['unit_worker_git_blob_sha']==WORKER_BLOB,'worker lock'); req(blob(AGG)==AGG_BLOB and c['aggregation']['git_blob_sha']==AGG_BLOB,'aggregate lock')
    req(c['partition']['key']=='parent_index' and c['partition']['expected_unit_count']==23 and c['partition']['finer_exact_partition_feasible'] is True,'partition'); req(c['target']['audited_unknown_parent_indices_sha256']==TARGET_SHA,'target hash')
    req(c['recovery']['monolithic_rerun_default'] is False and c['recovery']['fresh_runkey_generation_required'] is True,'recovery'); req(c['workflow_requirements']['partial_upload_if_always_or_equivalent_required'] is True and c['workflow_requirements']['effective_heavy_concurrency']==1,'workflow requirements')
    req(c['storage_preflight']['within_budget'] is True and c['storage_preflight']['projected_peak_new_storage_bytes']<=c['storage_preflight']['repository_operating_budget_bytes'],'storage')
    req(all(v is False for v in c['authorization'].values()),'authorization cold'); req(not RUNKEY.exists(),'runkey must remain absent before workflow migration')
    subprocess.run([sys.executable,'-m','py_compile',str(WORKER),str(AGG)],check=True); print('PASS: BC2-40 resume-first contract exact parent-index partition=23 heavy=NOT_ARMED')
if __name__=='__main__': main()
