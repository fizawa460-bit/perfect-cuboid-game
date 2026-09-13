#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'; ROOT=HERE.parents[0]
STAGE32_MAIN=ROOT/'stage32'/'MAIN-STATE.json'; CROSS=ROOT/'stage32'/'proof'/'CROSS-LANE-DEMANDS.json'; WF=ROOT.parent/'.github/workflows/stage32-ex5-main.yml'
CURRENT_MAIN='4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c'; MAIN_BLOB='73cc6ef56647a4be9119e89bf42c8ba4d96d54c9'; CROSS_BLOB='bbf4fc2460bad22c65359bc17aa89f8717e259a2'
AUDIT_HEAD='9c63ccb48dd0e5bdeedda7739dd05e2404698465'; AUDIT_REVIEW=5188625406; UNKNOWN_SHA='570b36293f136405c2beceb1be77dbad4b0c6b50e7fd2f28d9f3dfc944f590e9'
CP36_BLOB='09ac58349e388c479ac77e04724bef2fd9b49b7e'; CP36_CANON='e92cd6d07299b833a79fe20b81e9de032d61790cf1b7a6fb81ec6adccdb49fdf'; VER36_BLOB='c88d29b48249e2ec111cfbd075f7e5febfbb86f0'; RK36_BLOB='78d9c847863232b10d149b651c32c668887e4b23'
SRC37_BLOB='35a1644c197fd32aec845332452cc918f3bc75d9'; PF37_BLOB='15a008cd4557fe4e81d31591c3d80b50bc595a03'; PF37_CANON='30fa122941ee6b75e6e5004aa43ab121b216af93831cff0e9e22922f2438ddba'; RK37_BLOB='412f092eae0253432e74ab6ad470e89f19536ee5'
B32='7cfe8450cb9b9ab7f04da797d487655505598b93'; B19='b2899aa228e7a3ee97526e3787ffbefa483530b4'; D18='1e2ed93cae3c5b446c8d90c1ae2250be83289c79'; PC={'perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim'}
def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def checked(p,canon):
    o=json.loads(p.read_text()); q=dict(o); got=q.pop('canonical_sha256_without_this_field',None); req(got==canon and csha(q)==canon,'canonical drift '+p.name); return o
def main():
    s=json.loads((HERE/'MAIN-STATE.json').read_text()); req(s['schema']=='STAGE32EX5_MAIN_COMPACT_STATE_V27_BC2_36_AUDIT_CONSUMED_BC2_37_EXECUTION','schema')
    b=s['bootstrap']; req(b['active_work_pr']==1776 and b['work_branch']=='stage32ex5-bc2-25-boundary33-mainbatch' and b['current_main_sha_observed']==CURRENT_MAIN and b['merge_authorized'] is False,'bootstrap')
    req(blob(STAGE32_MAIN)==MAIN_BLOB,'MAIN blob'); ma=json.loads(STAGE32_MAIN.read_text()); mf=ma['current_exact_frontier']; req(ma['schema']=='STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED' and mf['authoritative_remaining_strata']==17128 and mf['authoritative_remaining_terminals']==47598978285064933757427 and mf['full178_numerical_census_complete'] is False,'MAIN authority')
    req(blob(CROSS)==CROSS_BLOB,'cross blob'); cl=json.loads(CROSS.read_text()); req([d for d in cl['demands'] if d.get('producer_lane')=='EX5' and d.get('status')=='OPEN']==[],'OPEN EX5 demand')
    cp36p=B2/'bc2-36-fresh-unknown52-replay-checkpoint.json'; ver36=B2/'verify_bc2_36_targeted_replay_checkpoint.py'; rk36=HERE/'runkeys/bc2-36-fresh-unknown52-replay.json'
    req(blob(cp36p)==CP36_BLOB and blob(ver36)==VER36_BLOB and blob(rk36)==RK36_BLOB,'BC2-36 retained identity'); cp36=checked(cp36p,CP36_CANON); r36=cp36['replay']; req((r36['parents_checked'],r36['unsat_count'],r36['unknown_count'],r36['sat_count'])==(52,11,41,0) and r36['unknown_parent_indices_sha256']==UNKNOWN_SHA and cp36['credit']['known_parent_unsat_count_lower_bound']==7295,'BC2-36 partition')
    pa=s['prior_audited_authority']['bc2_36_pr_1776']; req(pa=={'hostile_audit_status':'PASS','audit_checkpoint_exact_head':AUDIT_HEAD,'hostile_audit_review_id':AUDIT_REVIEW,'merged':False,'stage32_main_credit':False},'BC2-36 audit receipt')
    src=B2/'bc2_37_replay_explicit_fresh_unknown41.py'; pf=B2/'bc2-37-fresh-unknown41-replay-preflight.json'; rk=HERE/'runkeys/bc2-37-fresh-unknown41-replay.json'
    req(blob(src)==SRC37_BLOB and blob(pf)==PF37_BLOB and blob(rk)==RK37_BLOB,'BC2-37 cold identity'); p=checked(pf,PF37_CANON); k=json.loads(rk.read_text())
    audit={'bc2_36_hostile_audit_status':'PASS','bc2_36_hostile_audit_exact_head':AUDIT_HEAD,'bc2_36_hostile_audit_review_id':AUDIT_REVIEW}; req(p['audit_consumption']==audit and k['audit_consumption']==audit,'BC2-37 audit consumption')
    req(p['target']['audited_unknown_parent_count']==41 and p['target']['audited_unknown_parent_indices_sha256']==UNKNOWN_SHA and p['target']['prior_audited_unsat_count']==7295,'preflight target')
    req(k['generation'] in (0,1) and ((k['generation']==0 and k['armed'] is False) or (k['generation']==1 and k['armed'] is True)) and k['consumed_run'] is None,'runkey cold/armed semantics')
    req(k['source_git_blob_sha']==SRC37_BLOB and k['preflight_git_blob_sha']==PF37_BLOB and k['preflight_canonical']==PF37_CANON,'runkey locks'); ex=k['execution']; req(ex['per_parent_timeout_ms']==120000 and ex['effective_heavy_concurrency']==1 and ex['workflow_timeout_minutes']==110 and ex['heavy_scaleout_authorized'] is False,'execution limits')
    dep=k['dependency_locks']; req(dep['bc2_36_checkpoint_git_blob_sha']==CP36_BLOB and dep['bc2_36_checkpoint_canonical']==CP36_CANON and dep['bc2_36_producer_git_blob_sha']=='18f9c2146d5dc97400c4af1a8691560523cc03cf' and dep['bc2_32_producer_git_blob_sha']==B32 and dep['bc2_19_replay_source_git_blob_sha']==B19 and dep['bc2_18_enumerator_source_git_blob_sha']==D18,'dependency locks')
    f=s['frontier']; req(f['e8_bc2_36_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7295 and f['e8_bc2_37_executed'] is False and f['e8_bc2_37_target_unknown_count']==41 and f['e8_bc2_37_target_unknown_parent_indices_sha256']==UNKNOWN_SHA,'frontier')
    a=s['intermediate_audit_boundary']; req(a['last_hostile_audit_status']=='PASS' and a['last_hostile_audit_exact_head']==AUDIT_HEAD and a['last_hostile_audit_review_id']==AUDIT_REVIEW and a['bc2_37_execution_authorized'] is True and a['freeze_active'] is False and a['new_audit_boundary_exists'] is False,'audit boundary')
    cur=s['current']; req(cur['leaf']=='BC2_37_REFINE_REMAINING_FRESH_UNKNOWN_SET' and cur['next_route']=='BC2_37_REFINE_REMAINING_FRESH_UNKNOWN_SET','route'); ns=s['next_step']; req(ns['bc2_37_execution_authorized'] is True and ns['bc2_38_blocked_until_bc2_37_hostile_audit_pass'] is True,'next-step firewall')
    req({q for q in s['firewalls'] if 'cuboid' in q}==PC,'Perfect Cuboid keys'); [req(v is False,'firewall '+sec+'.'+q) for sec in ('historical_credit_firewall','firewalls') for q,v in s[sec].items()]; [req(v is False,'credit '+q) for q,v in s['credit'].items() if q!='level']
    wf=WF.read_text(); req('authorize-bc2-37-fresh-unknown41:' in wf and '\n  bc2-37-fresh-unknown41:' in wf,'BC2-37 workflow missing'); req('authorize-bc2-36-fresh-unknown52:' not in wf and '\n  bc2-36-fresh-unknown52:' not in wf,'BC2-36 heavy resurrected')
    for v in ('verify_bc2_34_dependency_identity_repair.py','verify_bc2_25_boundary33_partition_checkpoint.py','verify_bc2_26_boundary34_partition_checkpoint.py','verify_bc2_27_boundary35_partition_checkpoint.py','verify_bc2_28_boundary38_partition_checkpoint.py','verify_bc2_29_boundary39_partition_checkpoint.py','verify_bc2_30_boundary42_partition_checkpoint.py','verify_bc2_35_targeted_replay_checkpoint.py','verify_bc2_36_targeted_replay_checkpoint.py'): subprocess.run([sys.executable,str(B2/v)],check=True)
    print('PASS: Stage32EX5 BC2-36 audit consumed; BC2-37 exact UNKNOWN41 execution authority valid'); print('audited_lower_bound=7295 target41 timeout_ms=120000 main_credit=NO FULL178=NO merge=NO')
if __name__=='__main__': main()
