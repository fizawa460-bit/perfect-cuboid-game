#!/usr/bin/env python3
from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'; ROOT=HERE.parents[0]
STAGE32_MAIN=ROOT/'stage32'/'MAIN-STATE.json'; CROSS=ROOT/'stage32'/'proof'/'CROSS-LANE-DEMANDS.json'; WF=ROOT.parent/'.github/workflows/stage32-ex5-main.yml'
CURRENT_MAIN='4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c'; MAIN_BLOB='73cc6ef56647a4be9119e89bf42c8ba4d96d54c9'; CROSS_BLOB='bbf4fc2460bad22c65359bc17aa89f8717e259a2'
AUDIT36_HEAD='9c63ccb48dd0e5bdeedda7739dd05e2404698465'; AUDIT36_REVIEW=5188625406
CP37_BLOB='6ac4592eded6be2bf80e88c33d0ac5944f13afaf'; RK37_BLOB='f23a9062f5211dbf0cd17dd6d9d14299551a8e51'; VER37_BLOB='744ef59e67baca75900dd25381107b35dbbf04c5'; UNKNOWN34_SHA='b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891'
def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def main():
    s=json.loads((HERE/'MAIN-STATE.json').read_text()); req(s['schema']=='STAGE32EX5_MAIN_COMPACT_STATE_V28_BC2_37_TARGETED_REPLAY_AUDIT_BOUNDARY','schema')
    b=s['bootstrap']; req(b['active_work_pr']==1776 and b['work_branch']=='stage32ex5-bc2-25-boundary33-mainbatch' and b['current_main_sha_observed']==CURRENT_MAIN and b['merge_authorized'] is False,'bootstrap')
    req(blob(STAGE32_MAIN)==MAIN_BLOB,'MAIN blob'); ma=json.loads(STAGE32_MAIN.read_text()); mf=ma['current_exact_frontier']; req(ma['schema']=='STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED' and mf['authoritative_remaining_strata']==17128 and mf['authoritative_remaining_terminals']==47598978285064933757427 and mf['full178_numerical_census_complete'] is False,'MAIN authority')
    req(blob(CROSS)==CROSS_BLOB,'cross blob'); cl=json.loads(CROSS.read_text()); req([d for d in cl['demands'] if d.get('producer_lane')=='EX5' and d.get('status')=='OPEN']==[],'OPEN EX5 demand')
    cp37=B2/'bc2-37-fresh-unknown41-replay-checkpoint.json'; rk37=HERE/'runkeys/bc2-37-fresh-unknown41-replay.json'; ver37=B2/'verify_bc2_37_targeted_replay_checkpoint.py'; req(blob(cp37)==CP37_BLOB and blob(rk37)==RK37_BLOB and blob(ver37)==VER37_BLOB,'BC2-37 retained identity')
    cp=json.loads(cp37.read_text()); r=cp['replay']; req((r['parents_checked'],r['unsat_count'],r['unknown_count'],r['sat_count'])==(41,7,34,0) and r['unknown_parent_indices_sha256']==UNKNOWN34_SHA,'BC2-37 partition'); req(cp['credit']['known_parent_unsat_count_lower_bound']==7302 and cp['credit']['stage32_main_credit'] is False and cp['credit']['full178_complete'] is False,'BC2-37 candidate credit')
    rk=json.loads(rk37.read_text()); req(rk['generation']==1 and rk['armed'] is False and rk['consumed_run']['accepted_for_hostile_audit'] is True,'BC2-37 runkey consumed')
    f=s['frontier']; req(f['e8_bc2_36_audited'] is True and f['e8_bc2_37_executed'] is True and f['e8_bc2_37_audited'] is False and f['e8_bc2_37_target_unknown_count']==41 and f['e8_bc2_37_new_parent_unsat_count']==7 and f['e8_bc2_37_remaining_unknown_count']==34 and f['e8_bc2_37_remaining_unknown_parent_indices_sha256']==UNKNOWN34_SHA and f['e8_bc2_37_sat_count']==0,'frontier partition'); req(f['e8_known_parent_unsat_count_lower_bound']==7295 and f['e8_bc2_37_candidate_known_parent_unsat_count_lower_bound']==7302,'audited/candidate separation')
    a=s['intermediate_audit_boundary']; req(a['last_hostile_audit_status']=='PASS' and a['last_hostile_audit_exact_head']==AUDIT36_HEAD and a['last_hostile_audit_review_id']==AUDIT36_REVIEW and a['bc2_37_execution_authorized'] is False and a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True,'audit freeze')
    cur=s['current']; req(cur['status']=='BC2_37_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and cur['next_route']=='HOSTILE_AUDIT_BC2_37_TARGETED_REPLAY','route'); ns=s['next_step']; req(ns['id']=='HOSTILE_AUDIT_BC2_37_TARGETED_REPLAY' and ns['bc2_38_blocked_until_bc2_37_hostile_audit_pass'] is True and ns['main_promotion_authorized'] is False and ns['merge_authorized'] is False,'next-step firewall')
    for sec in ('historical_credit_firewall','firewalls'):
        for q,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+q)
    for q,v in s['credit'].items():
        if q!='level': req(v is False,'credit '+q)
    wf=WF.read_text(); req('verify_bc2_37_targeted_replay_checkpoint.py' in wf,'BC2-37 retained verifier missing'); req('authorize-bc2-37-fresh-unknown41:' not in wf and '\n  bc2-37-fresh-unknown41:' not in wf,'BC2-37 heavy not retired')
    for v in ('verify_bc2_34_dependency_identity_repair.py','verify_bc2_25_boundary33_partition_checkpoint.py','verify_bc2_26_boundary34_partition_checkpoint.py','verify_bc2_27_boundary35_partition_checkpoint.py','verify_bc2_28_boundary38_partition_checkpoint.py','verify_bc2_29_boundary39_partition_checkpoint.py','verify_bc2_30_boundary42_partition_checkpoint.py','verify_bc2_35_targeted_replay_checkpoint.py','verify_bc2_36_targeted_replay_checkpoint.py','verify_bc2_37_targeted_replay_checkpoint.py'): subprocess.run([sys.executable,str(B2/v)],check=True)
    print('PASS: Stage32EX5 BC2-37 exact targeted replay frozen for hostile audit'); print('audited_lower_bound=7295 candidate_lower_bound=7302 remaining_unknown=34 sat=0 main_credit=NO FULL178=NO merge=NO')
if __name__=='__main__': main()
