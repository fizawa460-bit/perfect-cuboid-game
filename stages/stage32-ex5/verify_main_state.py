#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
B2=HERE/'breadth-cycle-2'
STATE=HERE/'MAIN-STATE.json'
SYNC=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260914.json'
CP39=B2/'bc2-39-fresh-unknown30-replay-checkpoint.json'
V39=B2/'verify_bc2_39_targeted_replay_checkpoint.py'
PASS39=B2/'bc2-39-hostile-audit-pass-receipt.json'
PREFLIGHT40=B2/'bc2-40-fresh-unknown23-replay-preflight.json'
PRODUCER40=B2/'bc2_40_replay_explicit_fresh_unknown23.py'
WORKFLOW=HERE.parent.parent/'.github/workflows/stage32-ex5-main.yml'

SYNC_BLOB='c9a3a878413df5afc634f99b94707534412b5d84'
SYNC_CANON='fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c'
CP39_BLOB='43565b80d730caa5db8e3c95aa0a1e58217155cf'
CP39_CANON='77f9339f99070b35df09ac4f88c458ab23220fffa5679a9c1c125b429cb3f86e'
PASS39_BLOB='061c5345e465c7f43a0369dd3a44363a95ecf24a'
PASS39_CANON='bd1abc34b2225cef146f3c79eab5d09d3fcf2b1b4fc7dc6ff3cda6e1b362eefb'
PREFLIGHT40_BLOB='155924fa925f2433b394debc8d3bdde0375093fa'
PREFLIGHT40_CANON='935929b0a206fbbefb9657b6b2d7f65be76174506624445582b22252c0c5590c'
PRODUCER40_BLOB='acccc2360a2b113b4d568c86bb4be48152a68013'
UNKNOWN23_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
AUDIT39_HEAD='4b974550d9ad030973fec99e19a090f6785f8aa8'
AUDIT39_REVIEW=5193423203
V32='STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY'
V33='STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT'

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    s=json.loads(STATE.read_text())
    req(s['bootstrap']['active_work_pr']==1776 and s['bootstrap']['merge_authorized'] is False,'bootstrap')
    req(blob(SYNC)==SYNC_BLOB,'live MAIN sync blob')
    sync=json.loads(SYNC.read_text())
    req(sync['canonical_sha256_without_this_field']==SYNC_CANON and canon(sync)==SYNC_CANON,'live MAIN sync canonical')
    lm=sync['live_main_state']
    req(lm['authoritative_remaining_strata']==17128 and lm['certified_remaining_terminal_upper_bound']==26876434389242951089388 and lm['full178_complete'] is False,'MAIN authority sync')
    req(blob(CP39)==CP39_BLOB,'BC2-39 checkpoint blob')
    cp=json.loads(CP39.read_text())
    req(cp['canonical_sha256_without_this_field']==CP39_CANON and canon(cp)==CP39_CANON,'BC2-39 checkpoint canonical')
    r=cp['replay']
    req((r['unsat_count'],r['unknown_count'],r['sat_count'])==(7,23,0) and r['unknown_parent_indices_sha256']==UNKNOWN23_SHA,'BC2-39 partition')

    if s['schema']==V32:
        f=s['frontier']; a=s['intermediate_audit_boundary']
        req(f['e8_known_parent_unsat_count_lower_bound']==7306 and f['e8_bc2_39_candidate_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_audited'] is False,'V32 quarantine')
        req(a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True,'V32 audit freeze')
        print('PASS: Stage32EX5 V32 BC2-39 hostile-audit boundary')
        return

    req(s['schema']==V33,'V33 schema')
    req(blob(PASS39)==PASS39_BLOB,'BC2-39 audit PASS receipt blob')
    receipt=json.loads(PASS39.read_text())
    req(receipt['canonical_sha256_without_this_field']==PASS39_CANON and canon(receipt)==PASS39_CANON,'BC2-39 audit PASS receipt canonical')
    req(receipt['audit']=={'exact_head':AUDIT39_HEAD,'review_id':AUDIT39_REVIEW,'status':'PASS'},'BC2-39 audit identity')
    rr=receipt['result']
    req((rr['prior_audited_lower_bound'],rr['new_exact_unsat'],rr['post_audit_lower_bound'],rr['remaining_unknown_count'],rr['sat_count'])==(7306,7,7313,23,0),'BC2-39 PASS result counts')
    req(rr['remaining_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'BC2-39 PASS remaining identity')
    req(receipt['activation']['bc2_40_preflight_staged'] is True and receipt['activation']['live_main_state_consumed'] is False,'BC2-39 retained pre-migration activation semantics')
    req(all(v is False for v in receipt['firewalls'].values()),'BC2-39 PASS receipt firewall')

    req(blob(PREFLIGHT40)==PREFLIGHT40_BLOB,'BC2-40 preflight blob')
    pf=json.loads(PREFLIGHT40.read_text())
    req(pf['canonical_sha256_without_this_field']==PREFLIGHT40_CANON and canon(pf)==PREFLIGHT40_CANON,'BC2-40 preflight canonical')
    req(blob(PRODUCER40)==PRODUCER40_BLOB,'BC2-40 producer blob')
    req(pf['source_locks']['producer_git_blob_sha']==PRODUCER40_BLOB,'BC2-40 producer source lock')
    ac=pf['audit_consumption']
    req(ac['audit_pass_receipt_canonical']==PASS39_CANON and ac['bc2_39_hostile_audit_exact_head']==AUDIT39_HEAD and ac['bc2_39_hostile_audit_review_id']==AUDIT39_REVIEW and ac['bc2_39_hostile_audit_status']=='PASS' and ac['live_main_state_consumed'] is False,'BC2-40 staged audit identity')
    req(pf['status']=='PREFLIGHT_STAGED_LIVE_AUTHORITY_NOT_ACTIVATED' and pf['next_gate']=='VERIFY_AND_ACTIVATE_A_SEPARATE_LIVE_STATE_SCHEMA_MIGRATION_BEFORE_ANY_BC2_40_RUNKEY','BC2-40 staged migration gate')
    req(pf['target']['audited_unknown_parent_count']==23 and pf['target']['audited_unknown_parent_indices_sha256']==UNKNOWN23_SHA and pf['target']['prior_audited_unsat_count']==7313,'BC2-40 target')
    ex=pf['execution']; req(ex['per_parent_timeout_ms']==180000 and ex['effective_heavy_concurrency']==1 and ex['heavy_scaleout_authorized'] is False and ex['runkey_armed'] is False,'BC2-40 execution preflight')
    req(pf['firewalls']['bc2_40_execution_authorized'] is False and pf['firewalls']['main_promotion'] is False and pf['firewalls']['merge_authorized'] is False,'BC2-40 preflight firewalls')

    f=s['frontier']; a=s['intermediate_audit_boundary']; cur=s['current']; nx=s['next_step']; prog=s['retained_exact_progress']; ma=s['stage32_main_authority']
    req(f['e8_bc2_39_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'V33 audited frontier')
    req(f['e8_bc2_40_preflight_ready'] is True and f['e8_bc2_40_execution_authorized'] is False and f['e8_bc2_40_target_unknown_count']==23 and f['e8_bc2_40_target_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'V33 BC2-40 frontier')
    req(cur['status']=='BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT_READY_NOT_ARMED' and cur['next_route']=='BC2_40_FRESH_RUNKEY_AUTHORIZATION' and cur['blocker']=='BC2_40_FRESH_SEMANTIC_RUNKEY_NOT_ARMED','V33 route')
    req(a['last_hostile_audit_exact_head']==AUDIT39_HEAD and a['last_hostile_audit_review_id']==AUDIT39_REVIEW and a['last_hostile_audit_status']=='PASS','V33 audit receipt')
    req(a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False and a['bc2_40_execution_authorized'] is False,'V33 no audit/heavy boundary')
    req(nx['bc2_40_runkey_armed'] is False and nx['heavy_scaleout_authorized'] is False and nx['main_promotion_authorized'] is False and nx['merge_authorized'] is False,'V33 next gate')
    req(s['execution']['dedicated_runkey'] is None and s['execution']['effective_heavy_concurrency']==0 and s['execution']['runkey_armed'] is False and s['execution']['heavy_scaleout_authorized'] is False,'V33 heavy remains unarmed')
    req(prog['bc2_39_audit_pass_receipt_git_blob_sha']==PASS39_BLOB and prog['bc2_39_audit_pass_receipt_canonical']==PASS39_CANON,'V33 PASS receipt lock')
    req(prog['bc2_40_preflight_git_blob_sha']==PREFLIGHT40_BLOB and prog['bc2_40_preflight_canonical']==PREFLIGHT40_CANON and prog['bc2_40_producer_git_blob_sha']==PRODUCER40_BLOB,'V33 BC2-40 source locks')
    req(ma['current_main_schema']=='STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED' and ma['authoritative_remaining_strata']==17128 and ma['certified_remaining_terminal_upper_bound']==26876434389242951089388 and ma['full178_numerical_census_complete'] is False and ma['ex5_auto_promotes_to_main'] is False,'V33 live MAIN authority')
    expected_working={
        'stages/stage32-ex5/breadth-cycle-2/bc2-39-hostile-audit-pass-receipt.json',
        'stages/stage32-ex5/breadth-cycle-2/bc2-40-fresh-unknown23-replay-preflight.json',
        'stages/stage32-ex5/breadth-cycle-2/bc2_40_replay_explicit_fresh_unknown23.py',
        'stages/stage32-ex5/verify_main_state.py',
    }
    req(set(s['current_leaf_working_set'])==expected_working,'V33 bounded working set')
    for sec in ('historical_credit_firewall','firewalls'):
        for k,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+k)
    for k,v in s['credit'].items():
        if k!='level': req(v is False,'credit '+k)

    wf=WORKFLOW.read_text()
    req('authorize-bc2-40' not in wf and '\n  bc2-40' not in wf,'BC2-40 heavy must remain unarmed')
    subprocess.run([sys.executable,str(V39)],check=True)
    subprocess.run([sys.executable,'-m','py_compile',str(PRODUCER40)],check=True)
    print('PASS: Stage32EX5 V33 consumed BC2-39 PASS receipt and activated only the BC2-40 preflight route')
    print('audited_lower_bound=7313 retained_unknown=23 bc2_40_timeout_ms=180000 heavy=NOT_ARMED main_credit=NO merge=NO')

if __name__=='__main__': main()
