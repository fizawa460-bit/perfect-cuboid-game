#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'; ROOT=HERE.parents[0]
STAGE32_MAIN=ROOT/'stage32'/'MAIN-STATE.json'; CROSS=ROOT/'stage32'/'proof'/'CROSS-LANE-DEMANDS.json'; WF=ROOT.parent/'.github/workflows/stage32-ex5-main.yml'
CURRENT_MAIN='4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c'; MAIN_BLOB='73cc6ef56647a4be9119e89bf42c8ba4d96d54c9'; CROSS_BLOB='bbf4fc2460bad22c65359bc17aa89f8717e259a2'
AUDIT37_HEAD='9852fcec959962607da3290100291a60185e7104'; AUDIT37_REVIEW=5189412496
CP37_BLOB='6ac4592eded6be2bf80e88c33d0ac5944f13afaf'; RK37_BLOB='f23a9062f5211dbf0cd17dd6d9d14299551a8e51'; VER37_BLOB='9f4b6dbfbecc386ece02b5839a3b795c7206f82b'; UNKNOWN34_SHA='b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891'
SRC38_BLOB='6fb0af6c77e44edfa5d2b8a13fbde73bfbd468aa'; PF38_BLOB='aa959e57cfe9f9ffc136c9722c96ed0ec9770f7e'; PF38_CANON='22b74170a7ebb556fc97315f147c1fe90bb80d225fbd611f60b4ff8bed6fe964'; RK38_BLOB='4c7ac5bf049b71b1a968fc56d016f1a18298f84a'
def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None); return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    s=json.loads((HERE/'MAIN-STATE.json').read_text()); req(s['schema']=='STAGE32EX5_MAIN_COMPACT_STATE_V29_BC2_37_AUDIT_CONSUMED_BC2_38_EXECUTION','schema')
    b=s['bootstrap']; req(b['active_work_pr']==1776 and b['work_branch']=='stage32ex5-bc2-25-boundary33-mainbatch' and b['current_main_sha_observed']==CURRENT_MAIN and b['merge_authorized'] is False,'bootstrap')
    req(blob(STAGE32_MAIN)==MAIN_BLOB,'MAIN blob'); ma=json.loads(STAGE32_MAIN.read_text()); mf=ma['current_exact_frontier']; req(ma['schema']=='STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED' and mf['authoritative_remaining_strata']==17128 and mf['authoritative_remaining_terminals']==47598978285064933757427 and mf['full178_numerical_census_complete'] is False,'MAIN authority')
    req(blob(CROSS)==CROSS_BLOB,'cross blob'); cl=json.loads(CROSS.read_text()); req([d for d in cl['demands'] if d.get('producer_lane')=='EX5' and d.get('status')=='OPEN']==[],'OPEN EX5 demand')
    cp37=B2/'bc2-37-fresh-unknown41-replay-checkpoint.json'; rk37=HERE/'runkeys/bc2-37-fresh-unknown41-replay.json'; ver37=B2/'verify_bc2_37_targeted_replay_checkpoint.py'; req(blob(cp37)==CP37_BLOB and blob(rk37)==RK37_BLOB and blob(ver37)==VER37_BLOB,'BC2-37 retained identity')
    cp=json.loads(cp37.read_text()); r=cp['replay']; req((r['parents_checked'],r['unsat_count'],r['unknown_count'],r['sat_count'])==(41,7,34,0) and r['unknown_parent_indices_sha256']==UNKNOWN34_SHA,'BC2-37 partition'); req(cp['credit']['known_parent_unsat_count_lower_bound']==7302 and cp['credit']['stage32_main_credit'] is False and cp['credit']['full178_complete'] is False,'BC2-37 audited credit')
    pa=s['prior_audited_authority']['bc2_37_pr_1776']; req(pa['hostile_audit_status']=='PASS' and pa['audit_checkpoint_exact_head']==AUDIT37_HEAD and pa['hostile_audit_review_id']==AUDIT37_REVIEW and pa['stage32_main_credit'] is False,'BC2-37 external audit receipt')
    src38=B2/'bc2_38_replay_explicit_fresh_unknown34.py'; pf38=B2/'bc2-38-fresh-unknown34-replay-preflight.json'; rk38=HERE/'runkeys/bc2-38-fresh-unknown34-replay.json'; req(blob(src38)==SRC38_BLOB and blob(pf38)==PF38_BLOB and blob(rk38)==RK38_BLOB,'BC2-38 source/preflight/runkey identity')
    pf=json.loads(pf38.read_text()); req(pf['canonical_sha256_without_this_field']==PF38_CANON and canon(pf)==PF38_CANON,'BC2-38 preflight canonical'); rk=json.loads(rk38.read_text()); req(rk['schema']=='STAGE32EX5_BC2_38_FRESH_UNKNOWN34_REPLAY_RUNKEY_V1' and rk['generation']==1 and rk['armed'] is True and rk['source_git_blob_sha']==SRC38_BLOB and rk['preflight_git_blob_sha']==PF38_BLOB and rk['preflight_canonical']==PF38_CANON,'BC2-38 armed runkey')
    req(rk['audit_consumption']=={'bc2_37_hostile_audit_exact_head':AUDIT37_HEAD,'bc2_37_hostile_audit_review_id':AUDIT37_REVIEW,'bc2_37_hostile_audit_status':'PASS'},'BC2-38 audit consumption'); req(rk['target']['fresh_unknown_parent_count']==34 and rk['target']['fresh_unknown_parent_indices_sha256']==UNKNOWN34_SHA and rk['target']['prior_audited_unsat_count']==7302 and rk['execution']['per_parent_timeout_ms']==140000 and rk['execution']['effective_heavy_concurrency']==1 and rk['execution']['heavy_scaleout_authorized'] is False,'BC2-38 target/execution')
    f=s['frontier']; req(f['e8_bc2_37_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7302 and f['e8_bc2_38_executed'] is False and f['e8_bc2_38_target_unknown_count']==34 and f['e8_bc2_38_target_unknown_parent_indices_sha256']==UNKNOWN34_SHA,'frontier')
    a=s['intermediate_audit_boundary']; req(a['last_hostile_audit_status']=='PASS' and a['last_hostile_audit_exact_head']==AUDIT37_HEAD and a['last_hostile_audit_review_id']==AUDIT37_REVIEW and a['bc2_38_execution_authorized'] is True and a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False,'audit consumption')
    cur=s['current']; req(cur['status']=='BC2_38_TARGETED_REPLAY_EXECUTION_AUTHORIZED' and cur['next_route']=='BC2_38_REFINE_REMAINING_FRESH_UNKNOWN_SET','route'); ns=s['next_step']; req(ns['id']=='BC2_38_REFINE_REMAINING_FRESH_UNKNOWN_SET' and ns['bc2_38_execution_authorized'] is True and ns['bc2_39_blocked_until_bc2_38_hostile_audit_pass'] is True and ns['main_promotion_authorized'] is False and ns['merge_authorized'] is False,'next-step firewall')
    for sec in ('historical_credit_firewall','firewalls'):
        for q,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+q)
    for q,v in s['credit'].items():
        if q!='level': req(v is False,'credit '+q)
    wf=WF.read_text(); req('verify_bc2_37_targeted_replay_checkpoint.py' in wf,'BC2-37 retained verifier missing'); req('authorize-bc2-37-fresh-unknown41:' not in wf and '\n  bc2-37-fresh-unknown41:' not in wf,'BC2-37 heavy not retired'); req('authorize-bc2-38-fresh-unknown34:' in wf and '\n  bc2-38-fresh-unknown34:' in wf,'BC2-38 heavy route missing')
    for v in ('verify_bc2_34_dependency_identity_repair.py','verify_bc2_25_boundary33_partition_checkpoint.py','verify_bc2_26_boundary34_partition_checkpoint.py','verify_bc2_27_boundary35_partition_checkpoint.py','verify_bc2_28_boundary38_partition_checkpoint.py','verify_bc2_29_boundary39_partition_checkpoint.py','verify_bc2_30_boundary42_partition_checkpoint.py','verify_bc2_35_targeted_replay_checkpoint.py','verify_bc2_36_targeted_replay_checkpoint.py','verify_bc2_37_targeted_replay_checkpoint.py'): subprocess.run([sys.executable,str(B2/v)],check=True)
    subprocess.run([sys.executable,'-m','py_compile',str(src38)],check=True)
    print('PASS: Stage32EX5 BC2-37 hostile audit consumed; BC2-38 exact targeted replay generation1 armed'); print('audited_lower_bound=7302 target_unknown=34 timeout_ms=140000 main_credit=NO FULL178=NO merge=NO')
if __name__=='__main__': main()
