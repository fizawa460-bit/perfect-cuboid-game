#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'
STATE=HERE/'MAIN-STATE.json'; SYNC=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260915.json'
V39=B2/'verify_bc2_39_targeted_replay_checkpoint.py'; RESUME=B2/'verify_bc2_40_resume_first_contract.py'
CONTRACT=B2/'bc2-40-resume-first-contract.json'; QUAR=B2/'bc2-40-generation3-policy-quarantine-receipt.json'; REARM=B2/'bc2-40-generation4-rearm-audit-consumption.json'
RUNKEY=HERE/'runkeys/bc2-40-fresh-unknown23-replay.json'; WF=HERE.parent.parent/'.github/workflows/stage32-ex5-bc2-40-resume.yml'
V34='STAGE32EX5_MAIN_COMPACT_STATE_V34_BC2_40_RESUME_RUNKEY_ARMED_EXECUTION'
UNKNOWN='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
MAIN='117310b6a9d40273683cab8c08cc9e5e0cc584d9'
SYNC_BLOB='1698915fe01af97f5f60f90645792fb6c3d33576'; SYNC_CANON='677b9e595f271a669c32ca2849dd6dc010de363d1df359c70e0b970162757565'
CONTRACT_BLOB='220edb27584ea99899e7e3f129869f1a1b7719a2'; CONTRACT_CANON='ff2106909f7d9e02c7300127f10463e7d4fc3415e300c10f1e8aad712b133ca1'
QUAR_BLOB='0819e7a800057873e2909513a32d3fe462fd87a6'; QUAR_CANON='c704500d036b2994680d4f42c3c8b7256c6eda02703f4cf371e97718d10ac199'
REARM_BLOB='07866a4ab965c432d94efd71d88bf98c65452ee4'; REARM_CANON='8ccd42cf0b8fb43eae3f90b51f98fa1f809883679c6a39bac59b5b058f94187f'
RUNKEY_BLOB='6e26b2f1b1b39935d2f1735576124fe2786bd1fb'; RUNKEY_CANON='acf01030540d310637c8a30395c3aec320eadfd95f0df015954df50fc8461daf'
WF_BLOB='425b0d72f1a654f53b16bf086c537e79335d6263'
TARGET=[1056,1103,1206,1243,1703,1706,1717,1733,1798,2092,2122,2187,2407,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]
def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def checked(path,b,c,label):
    req(path.is_file() and blob(path)==b,label+' blob')
    o=json.loads(path.read_text()); req(o.get('canonical_sha256_without_this_field')==c and canon(o)==c,label+' canonical'); return o
def main():
    s=json.loads(STATE.read_text()); req(s['schema']==V34,'schema'); req(s['bootstrap']['active_work_pr']==1776 and s['bootstrap']['merge_authorized'] is False,'bootstrap')
    sync=checked(SYNC,SYNC_BLOB,SYNC_CANON,'live MAIN sync'); req(sync['live_exact_head']==MAIN,'main head')
    lm=sync['live_main_state']; req(lm['authoritative_remaining_strata']==17128 and lm['certified_remaining_terminal_upper_bound']==26876434389242951089388 and lm['full178_complete'] is False,'MAIN authority')
    req(sync['live_cross_lane_registry']['open_ex5_producer_demand_count']==0,'EX5 demand')
    checked(CONTRACT,CONTRACT_BLOB,CONTRACT_CANON,'BC2-40 repaired contract')
    q=checked(QUAR,QUAR_BLOB,QUAR_CANON,'generation-3 quarantine receipt')
    req(q['generation3']['exact_head']=='7f82c49a07bb82d59603b47b436ff8e84a884fd5' and q['generation3']['workflow_run_id']==34903034534 and q['generation3']['heavy_started'] is True,'generation-3 provenance')
    req(q['defect']['kind']=='HEAVY_AUTHORIZATION_EVENT_RANGE_POLICY_VIOLATION' and q['quarantine']['credit_eligible'] is False and q['quarantine']['carry_into_credited_generation_authorized'] is False and q['quarantine']['blocks_new_bc2_40_generation'] is True,'generation-3 policy quarantine')
    ra=checked(REARM,REARM_BLOB,REARM_CANON,'generation-4 rearm audit consumption')
    opa=ra['operational_hostile_audit']; g4=ra['generation4_rearm']; req(opa=={'status':'PASS','exact_head':'dd0a7339e6d40a8208b03e1263da192d139b00d7','review_id':5203808297,'submitted_at_utc':'2026-09-14T23:19:06Z','scope':'BC2_40_GENERATION3_POLICY_QUARANTINE_AND_REPAIRED_EVENT_RANGE_AUTHORIZATION'},'generation-4 policy audit receipt')
    req(g4['authorized_by_operational_audit_consumption'] is True and g4['required_generation']==4 and g4['carried_parent_indices']==[] and g4['missing_parent_count']==23 and g4['must_use_fresh_semantic_v2_runkey'] is True and g4['event_range']=='github.event.before..github.event.pull_request.head.sha' and g4['effective_heavy_concurrency']==1 and g4['heavy_scaleout_authorized'] is False,'generation-4 rearm receipt semantics')
    req(blob(RUNKEY)==RUNKEY_BLOB,'generation-4 runkey blob'); rk=json.loads(RUNKEY.read_text()); req(rk['generation']==4 and rk['armed'] is True and rk['canonical_sha256_without_this_field']==RUNKEY_CANON and canon(rk)==RUNKEY_CANON,'generation-4 fresh runkey')
    pa=rk.get('policy_audit_consumption',{}); req(pa=={'status':'PASS','exact_head':'dd0a7339e6d40a8208b03e1263da192d139b00d7','review_id':5203808297,'generation3_credit_eligible':False,'generation3_carry_authorized':False,'generation4_rearm_authorized':True},'generation-4 runkey policy audit binding')
    dep=rk['dependency_locks']; req(dep['resume_contract_canonical']==CONTRACT_CANON and dep['resume_contract_git_blob_sha']==CONTRACT_BLOB and dep['generation3_policy_quarantine_receipt_canonical']==QUAR_CANON and dep['generation3_policy_quarantine_receipt_git_blob_sha']==QUAR_BLOB and dep['generation4_rearm_audit_receipt_canonical']==REARM_CANON and dep['generation4_rearm_audit_receipt_git_blob_sha']==REARM_BLOB,'generation-4 dependency locks')
    r=rk['resume']; req(r['partition_key']=='parent_index' and r['carried_parent_indices']==[] and r['missing_parent_indices']==TARGET and r['schedule_only_missing_parent_indices']==TARGET,'generation-4 fresh partition')
    f=s['frontier']; req(f['e8_bc2_39_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN,'BC2-39 audited frontier')
    req(f['e8_bc2_40_executed'] is False and f['e8_bc2_40_generation3_policy_credit_eligible'] is False,'BC2-40 credit quarantine')
    pq=s['workflow_policy_quarantine']; req(pq['active'] is True and pq['blocks_new_bc2_40_generation'] is False and pq['generation3_credit_eligible'] is False and pq['generation3_carry_into_credited_generation_authorized'] is False and pq['hostile_audit_required_before_generation4'] is False and pq['generation4_rearm_authorized'] is True and pq['operational_hostile_audit_status']=='PASS' and pq['operational_hostile_audit_exact_head']=='dd0a7339e6d40a8208b03e1263da192d139b00d7' and pq['operational_hostile_audit_review_id']==5203808297 and pq['generation4_rearm_receipt']=='stages/stage32-ex5/breadth-cycle-2/bc2-40-generation4-rearm-audit-consumption.json','policy quarantine consumed for generation-4 only')
    ex=s['execution']; nx=s['next_step']; req(ex['new_generation_rearm_authorized'] is True and ex['generation4_rearm_requires_hostile_audit'] is False,'execution rearm'); req(nx['generation4_rearm_authorized'] is True and nx['hostile_audit_required_before_generation4'] is False,'next-step rearm')
    req('stages/stage32-ex5/breadth-cycle-2/bc2-40-generation4-rearm-audit-consumption.json' in s['current_leaf_working_set'],'rearm receipt working set')
    for sec in ('historical_credit_firewall','firewalls'):
        req(all(v is False for v in s[sec].values()),sec)
    req(all(v is False for k,v in s['credit'].items() if k!='level'),'credit firewall')
    wf=WF.read_text(); req(blob(WF)==WF_BLOB,'workflow blob'); req('BEFORE: ${{ github.event.before }}' in wf and 'HEAD_SHA: ${{ github.event.pull_request.head.sha }}' in wf and 'HEAD^' not in wf,'event-range gate'); req(wf.count('ref: ${{ github.event.pull_request.head.sha }}')==3,'exact PR-head checkout')
    subprocess.run([sys.executable,str(V39)],check=True); subprocess.run([sys.executable,str(RESUME)],check=True)
    print('PASS: Stage32EX5 BC2-39 audited authority retained; generation-3 quarantined noncredit; repaired event-range audit PASS consumed; fresh generation-4 rearmed with zero carry')
    print('audited_lower_bound=7313 retained_unknown=23 generation3_credit=NO generation3_carry=NO generation4_rearm=YES main_credit=NO merge=NO')
if __name__=='__main__': main()
