#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'; ROOT=HERE.parents[0]
STAGE32_MAIN=ROOT/'stage32'/'MAIN-STATE.json'; CROSS=ROOT/'stage32'/'proof'/'CROSS-LANE-DEMANDS.json'; WF=ROOT.parent/'.github/workflows/stage32-ex5-main.yml'
CURRENT_MAIN='4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c'; MAIN_BLOB='73cc6ef56647a4be9119e89bf42c8ba4d96d54c9'; CROSS_BLOB='bbf4fc2460bad22c65359bc17aa89f8717e259a2'
AUDIT37_HEAD='9852fcec959962607da3290100291a60185e7104'; AUDIT37_REVIEW=5189412496
CP38_BLOB='91eca02054cd2dbf702dd4a7635398ef76ee832f'; CP38_CANON='88b41680df6bb78f8b7f8ca00cde121d909a39e7b3c29eef765edb77b2c022ba'; RK38_BLOB='87855350c6240cd524069490f85858b11099da60'; VER38_BLOB='934f19363549d652c18b02934c1f963a19204664'; UNKNOWN30_SHA='d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7'; TARGET34_SHA='b2b0d1ef7d667fc380457818aa352e770f41fcdef7ca34c9ea88372c3193f891'
SRC38_BLOB='6fb0af6c77e44edfa5d2b8a13fbde73bfbd468aa'; PF38_BLOB='aa959e57cfe9f9ffc136c9722c96ed0ec9770f7e'; PF38_CANON='22b74170a7ebb556fc97315f147c1fe90bb80d225fbd611f60b4ff8bed6fe964'
def req(x,m):
    if not x: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None); return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    s=json.loads((HERE/'MAIN-STATE.json').read_text()); req(s['schema']=='STAGE32EX5_MAIN_COMPACT_STATE_V30_BC2_38_TARGETED_REPLAY_AUDIT_BOUNDARY','schema')
    b=s['bootstrap']; req(b['active_work_pr']==1776 and b['work_branch']=='stage32ex5-bc2-25-boundary33-mainbatch' and b['current_main_sha_observed']==CURRENT_MAIN and b['merge_authorized'] is False,'bootstrap')
    req(blob(STAGE32_MAIN)==MAIN_BLOB,'MAIN blob'); ma=json.loads(STAGE32_MAIN.read_text()); mf=ma['current_exact_frontier']; req(ma['schema']=='STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED' and mf['authoritative_remaining_strata']==17128 and mf['authoritative_remaining_terminals']==47598978285064933757427 and mf['full178_numerical_census_complete'] is False,'MAIN authority')
    req(blob(CROSS)==CROSS_BLOB,'cross blob'); cl=json.loads(CROSS.read_text()); req([d for d in cl['demands'] if d.get('producer_lane')=='EX5' and d.get('status')=='OPEN']==[],'OPEN EX5 demand')
    cp38=B2/'bc2-38-fresh-unknown34-replay-checkpoint.json'; rk38=HERE/'runkeys/bc2-38-fresh-unknown34-replay.json'; ver38=B2/'verify_bc2_38_targeted_replay_checkpoint.py'; req(blob(cp38)==CP38_BLOB and blob(rk38)==RK38_BLOB and blob(ver38)==VER38_BLOB,'BC2-38 retained identity')
    cp=json.loads(cp38.read_text()); r=cp['replay']; req((r['parents_checked'],r['unsat_count'],r['unknown_count'],r['sat_count'])==(34,4,30,0) and r['unknown_parent_indices_sha256']==UNKNOWN30_SHA and r['status_stream_sha256']=='839233bb8552e4da7589616439cb614c07ceb018643f4f6d9bf3bf3f175fdeb5','BC2-38 partition'); req(cp['target']['parent_indices_sha256']==TARGET34_SHA and cp['target']['prior_audited_unsat_count']==7302,'BC2-38 target'); req(cp['credit']['known_parent_unsat_count_lower_bound']==7306 and cp['credit']['stage32_main_credit'] is False and cp['credit']['full178_complete'] is False,'BC2-38 candidate credit')
    src38=B2/'bc2_38_replay_explicit_fresh_unknown34.py'; pf38=B2/'bc2-38-fresh-unknown34-replay-preflight.json'; req(blob(src38)==SRC38_BLOB and blob(pf38)==PF38_BLOB,'BC2-38 source/preflight identity'); pf=json.loads(pf38.read_text()); req(pf['canonical_sha256_without_this_field']==PF38_CANON and canon(pf)==PF38_CANON,'BC2-38 preflight canonical')
    rk=json.loads(rk38.read_text()); req(rk['schema']=='STAGE32EX5_BC2_38_FRESH_UNKNOWN34_REPLAY_RUNKEY_V1' and rk['generation']==1 and rk['armed'] is False,'BC2-38 consumed runkey'); cr=rk['consumed_run']; req(cr['accepted_for_hostile_audit'] is True and cr['exact_head']=='d26a27e8564458f3d575ec58601b2226fc23944f' and cr['workflow_run_id']==34742297972 and cr['artifact_id']==10313851431 and cr['new_unsat_count']==4 and cr['remaining_unknown_count']==30 and cr['known_parent_unsat_count_lower_bound']==7306,'BC2-38 run receipt')
    pa=s['prior_audited_authority']['bc2_37_pr_1776']; req(pa['hostile_audit_status']=='PASS' and pa['audit_checkpoint_exact_head']==AUDIT37_HEAD and pa['hostile_audit_review_id']==AUDIT37_REVIEW and pa['stage32_main_credit'] is False,'BC2-37 external audit receipt')
    f=s['frontier']; req(f['e8_bc2_37_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7302 and f['e8_bc2_38_executed'] is True and f['e8_bc2_38_audited'] is False and f['e8_bc2_38_target_unknown_count']==34 and f['e8_bc2_38_target_unknown_parent_indices_sha256']==TARGET34_SHA and f['e8_bc2_38_new_parent_unsat_count']==4 and f['e8_bc2_38_remaining_unknown_count']==30 and f['e8_bc2_38_remaining_unknown_parent_indices_sha256']==UNKNOWN30_SHA and f['e8_bc2_38_candidate_known_parent_unsat_count_lower_bound']==7306,'frontier')
    a=s['intermediate_audit_boundary']; req(a['last_hostile_audit_status']=='PASS' and a['last_hostile_audit_exact_head']==AUDIT37_HEAD and a['last_hostile_audit_review_id']==AUDIT37_REVIEW and a['bc2_38_execution_authorized'] is False and a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True,'audit boundary')
    cur=s['current']; req(cur['status']=='BC2_38_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and cur['next_route']=='HOSTILE_AUDIT_BC2_38_TARGETED_REPLAY','route'); ns=s['next_step']; req(ns['id']=='HOSTILE_AUDIT_BC2_38_TARGETED_REPLAY' and ns['bc2_38_execution_authorized'] is False and ns['bc2_39_blocked_until_bc2_38_hostile_audit_pass'] is True and ns['main_promotion_authorized'] is False and ns['merge_authorized'] is False,'next-step firewall')
    for sec in ('historical_credit_firewall','firewalls'):
        for q,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+q)
    for q,v in s['credit'].items():
        if q!='level': req(v is False,'credit '+q)
    wf=WF.read_text(); req('verify_bc2_38_targeted_replay_checkpoint.py' in wf,'BC2-38 retained verifier missing'); req('authorize-bc2-38-fresh-unknown34:' not in wf and '\n  bc2-38-fresh-unknown34:' not in wf,'BC2-38 heavy not retired')
    subprocess.run([sys.executable,str(ver38)],check=True); subprocess.run([sys.executable,'-m','py_compile',str(src38)],check=True)
    print('PASS: Stage32EX5 BC2-38 targeted replay retained as hostile-audit boundary'); print('candidate_lower_bound=7306 audited_lower_bound=7302 retained_unknown=30 main_credit=NO FULL178=NO merge=NO')
if __name__=='__main__': main()
