#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
B2=HERE/'breadth-cycle-2'
STATE=HERE/'MAIN-STATE.json'
SYNC_V33=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260914.json'
SYNC_V34=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260915.json'
CP39=B2/'bc2-39-fresh-unknown30-replay-checkpoint.json'
V39=B2/'verify_bc2_39_targeted_replay_checkpoint.py'
PASS39=B2/'bc2-39-hostile-audit-pass-receipt.json'
PREFLIGHT40=B2/'bc2-40-fresh-unknown23-replay-preflight.json'
PRODUCER40=B2/'bc2_40_replay_explicit_fresh_unknown23.py'
RESUME40=B2/'verify_bc2_40_resume_first_contract.py'
CONTRACT40=B2/'bc2-40-resume-first-contract.json'
RETRY40_1=B2/'bc2-40-generation1-no-heavy-retry-receipt.json'
RETRY40_2=B2/'bc2-40-generation2-no-heavy-retry-receipt.json'
HELPER40=B2/'bc2_40_resume_execute.py'
WORKER40=B2/'bc2_40_replay_parent_unit.py'
AGG40=B2/'bc2_40_resume_aggregate.py'
RUNKEY40=HERE/'runkeys'/'bc2-40-fresh-unknown23-replay.json'
RESUME_WORKFLOW=HERE.parent.parent/'.github/workflows/stage32-ex5-bc2-40-resume.yml'
LEGACY_WORKFLOW=HERE.parent.parent/'.github/workflows/stage32-ex5-main.yml'

SYNC_V33_BLOB='c9a3a878413df5afc634f99b94707534412b5d84'
SYNC_V33_CANON='fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c'
SYNC_V34_BLOB='1698915fe01af97f5f60f90645792fb6c3d33576'
SYNC_V34_CANON='677b9e595f271a669c32ca2849dd6dc010de363d1df359c70e0b970162757565'
CP39_BLOB='43565b80d730caa5db8e3c95aa0a1e58217155cf'
CP39_CANON='77f9339f99070b35df09ac4f88c458ab23220fffa5679a9c1c125b429cb3f86e'
PASS39_BLOB='061c5345e465c7f43a0369dd3a44363a95ecf24a'
PASS39_CANON='bd1abc34b2225cef146f3c79eab5d09d3fcf2b1b4fc7dc6ff3cda6e1b362eefb'
PREFLIGHT40_BLOB='155924fa925f2433b394debc8d3bdde0375093fa'
PREFLIGHT40_CANON='935929b0a206fbbefb9657b6b2d7f65be76174506624445582b22252c0c5590c'
PRODUCER40_BLOB='acccc2360a2b113b4d568c86bb4be48152a68013'
CONTRACT40_BLOB='750f26b6485041031e5a2be31ce2fa52ab99d80b'
CONTRACT40_CANON='0404db1edffc4b899f29dd6693fb2c84f857a3071dfd5ca653d1a97002f7a7ba'
RETRY40_1_BLOB='f25d2cf24a761ef9e60da98f83c1e52468a834c0'
RETRY40_1_CANON='33cb5f4117c4b639a42cc670eaceff5faaf9497132a26808b0cbee3e65d892e9'
RETRY40_2_BLOB='5827bc1af0ec8f4a5fff6bb6df68836427a838ff'
RETRY40_2_CANON='b2ace1e9695f4db57c2d662d9494f1728f7927d64e31725e6c36231dd420ae1b'
HELPER40_BLOB='5b262f1c05d82ae3203a689522f476d83406dbb8'
WORKER40_BLOB='a28061b99527c6585c3f4016992d1ef6e47b42de'
AGG40_BLOB='76c1d5e9f45d113ccb17e8149b2d840e2278b301'
UNKNOWN23_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
AUDIT39_HEAD='4b974550d9ad030973fec99e19a090f6785f8aa8'
AUDIT39_REVIEW=5193423203
CURRENT_MAIN='117310b6a9d40273683cab8c08cc9e5e0cc584d9'
MAIN_STATE_BLOB='b8df16056625db5fbb1947f1e927593de258f1ff'
MAIN_STATE_CANON='bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d'
CROSS_BLOB='e2949866d41a78ff9169bdb23a2fcefb6d0f5dcd'
CROSS_CANON='a5a85f824ba8fe466dbd13a7118bc0e95220cd5925d2af273653d86746a71228'
V32='STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY'
V33='STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT'
V34='STAGE32EX5_MAIN_COMPACT_STATE_V34_BC2_40_RESUME_RUNKEY_ARMED_EXECUTION'
RUNKEY_V2='STAGE32EX5_BC2_40_RESUME_RUNKEY_V2'
RUNKEY_PATH='stages/stage32-ex5/runkeys/bc2-40-fresh-unknown23-replay.json'
TARGET23=[1056,1103,1206,1243,1703,1706,1717,1733,1798,2092,2122,2187,2407,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def verify_sync(path:Path, expected_blob:str, expected_canon:str, require_current:bool):
    req(path.is_file(),'live MAIN sync missing')
    req(blob(path)==expected_blob,'live MAIN sync blob')
    sync=json.loads(path.read_text())
    req(sync['canonical_sha256_without_this_field']==expected_canon and canon(sync)==expected_canon,'live MAIN sync canonical')
    lm=sync['live_main_state']; lr=sync['live_cross_lane_registry']
    req(lm['authoritative_remaining_strata']==17128 and lm['certified_remaining_terminal_upper_bound']==26876434389242951089388 and lm['full178_complete'] is False,'MAIN authority sync')
    req(lr['open_ex5_producer_demand_count']==0,'OPEN EX5 producer demand')
    if require_current:
        req(sync['live_exact_head']==CURRENT_MAIN,'current main exact head')
        req(lm['git_blob_sha']==MAIN_STATE_BLOB and lm['canonical_sha256']==MAIN_STATE_CANON,'current MAIN state identity')
        req(lr['git_blob_sha']==CROSS_BLOB and lr['canonical_sha256']==CROSS_CANON,'current cross-lane identity')
    return sync

def main():
    s=json.loads(STATE.read_text()); schema=s['schema']
    req(s['bootstrap']['active_work_pr']==1776 and s['bootstrap']['merge_authorized'] is False,'bootstrap')
    if schema==V34:
        verify_sync(SYNC_V34,SYNC_V34_BLOB,SYNC_V34_CANON,True)
    else:
        verify_sync(SYNC_V33,SYNC_V33_BLOB,SYNC_V33_CANON,False)

    req(blob(CP39)==CP39_BLOB,'BC2-39 checkpoint blob')
    cp=json.loads(CP39.read_text())
    req(cp['canonical_sha256_without_this_field']==CP39_CANON and canon(cp)==CP39_CANON,'BC2-39 checkpoint canonical')
    r=cp['replay']
    req((r['unsat_count'],r['unknown_count'],r['sat_count'])==(7,23,0) and r['unknown_parent_indices_sha256']==UNKNOWN23_SHA,'BC2-39 partition')

    if schema==V32:
        f=s['frontier']; a=s['intermediate_audit_boundary']
        req(f['e8_known_parent_unsat_count_lower_bound']==7306 and f['e8_bc2_39_candidate_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_audited'] is False,'V32 quarantine')
        req(a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True,'V32 audit freeze')
        print('PASS: Stage32EX5 V32 BC2-39 hostile-audit boundary')
        return

    req(schema in {V33,V34},'V33/V34 schema')
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
    req(f['e8_bc2_39_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'audited frontier')
    req(f['e8_bc2_40_preflight_ready'] is True and f['e8_bc2_40_target_unknown_count']==23 and f['e8_bc2_40_target_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'BC2-40 frontier identity')
    req(a['last_hostile_audit_exact_head']==AUDIT39_HEAD and a['last_hostile_audit_review_id']==AUDIT39_REVIEW and a['last_hostile_audit_status']=='PASS','audit receipt')
    req(a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False,'no audit freeze at authorization boundary')
    req(prog['bc2_39_audit_pass_receipt_git_blob_sha']==PASS39_BLOB and prog['bc2_39_audit_pass_receipt_canonical']==PASS39_CANON,'PASS receipt lock')
    req(prog['bc2_40_preflight_git_blob_sha']==PREFLIGHT40_BLOB and prog['bc2_40_preflight_canonical']==PREFLIGHT40_CANON and prog['bc2_40_producer_git_blob_sha']==PRODUCER40_BLOB,'BC2-40 source locks')
    req(ma['current_main_schema']=='STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED' and ma['authoritative_remaining_strata']==17128 and ma['certified_remaining_terminal_upper_bound']==26876434389242951089388 and ma['full178_numerical_census_complete'] is False and ma['ex5_auto_promotes_to_main'] is False,'live MAIN authority')
    for sec in ('historical_credit_firewall','firewalls'):
        for k,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+k)
    for k,v in s['credit'].items():
        if k!='level': req(v is False,'credit '+k)

    wf=RESUME_WORKFLOW.read_text()
    req('# Trigger lifecycle: ACTIVE_AUTO' in wf and RUNKEY_V2 in wf,'BC2-40 V2 workflow lifecycle/schema')
    req('authorize-bc2-40-resume-v2:' in wf and '\n  bc2-40-resume-heavy:' in wf and 'LIVE-MAIN-COORDINATION-SYNC-20260915.json' in wf,'BC2-40 V2 gate missing')
    req(wf.count('ref: ${{ github.event.pull_request.head.sha }}')==3,'BC2-40 exact PR-head checkout count')
    legacy=LEGACY_WORKFLOW.read_text()
    req('authorize-bc2-40-fresh-unknown23:' not in legacy and '\n  bc2-40-fresh-unknown23:' not in legacy,'legacy BC2-40 V1 runtime jobs resurrected')
    req(RUNKEY_V2 not in legacy,'legacy EX5 main must not authorize V2 runkey')

    if schema==V33:
        req(f['e8_bc2_40_execution_authorized'] is False,'V33 BC2-40 must be unauthorized')
        req(cur['status']=='BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT_READY_NOT_ARMED' and cur['next_route']=='BC2_40_FRESH_RUNKEY_AUTHORIZATION' and cur['blocker']=='BC2_40_FRESH_SEMANTIC_RUNKEY_NOT_ARMED','V33 route')
        req(a['bc2_40_execution_authorized'] is False,'V33 audit boundary authorization')
        req(nx['bc2_40_runkey_armed'] is False and nx['heavy_scaleout_authorized'] is False and nx['main_promotion_authorized'] is False and nx['merge_authorized'] is False,'V33 next gate')
        req(s['execution']['dedicated_runkey'] is None and s['execution']['effective_heavy_concurrency']==0 and s['execution']['runkey_armed'] is False and s['execution']['heavy_scaleout_authorized'] is False,'V33 heavy remains unarmed')
        expected_working={
            'stages/stage32-ex5/breadth-cycle-2/bc2-39-hostile-audit-pass-receipt.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2-40-fresh-unknown23-replay-preflight.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2_40_replay_explicit_fresh_unknown23.py',
            'stages/stage32-ex5/verify_main_state.py',
        }
        req(set(s['current_leaf_working_set'])==expected_working,'V33 bounded working set')
        req(not RUNKEY40.exists(),'BC2-40 runkey must remain absent while V33 cold gate is validated')
    else:
        req(f['e8_bc2_40_execution_authorized'] is True and f['e8_bc2_40_executed'] is False,'V34 BC2-40 authorization frontier')
        req(cur['status']=='BC2_40_RESUME_RUNKEY_ARMED_EXECUTION_AUTHORIZED' and cur['next_route']=='BC2_40_RESUME_EXECUTE_MISSING_PARENT_UNITS' and cur['blocker']=='BC2_40_RESUME_HEAVY_PENDING','V34 route')
        req(a['bc2_40_execution_authorized'] is True,'V34 audit boundary authorization')
        req(nx['bc2_40_runkey_armed'] is True and nx['heavy_scaleout_authorized'] is False and nx['main_promotion_authorized'] is False and nx['merge_authorized'] is False,'V34 next gate')
        se=s['execution']; req(se['dedicated_runkey']==RUNKEY_PATH and se['effective_heavy_concurrency']==1 and se['per_parent_timeout_ms']==180000 and se['runkey_armed'] is True and se['heavy_scaleout_authorized'] is False and se['workflow']=='.github/workflows/stage32-ex5-bc2-40-resume.yml','V34 execution')
        req(RUNKEY40.is_file(),'V34 runkey missing')
        rk=json.loads(RUNKEY40.read_text()); req(rk['schema']==RUNKEY_V2 and rk['generation']==3 and rk['armed'] is True and rk['canonical_sha256_without_this_field']==canon(rk),'V34 runkey identity/canonical')
        req(rk['target']=={'fresh_unknown_parent_count':23,'fresh_unknown_parent_indices_sha256':UNKNOWN23_SHA,'prior_audited_unsat_count':7313},'V34 runkey target')
        req(rk['audit_consumption']=={'bc2_39_hostile_audit_status':'PASS','bc2_39_hostile_audit_exact_head':AUDIT39_HEAD,'bc2_39_hostile_audit_review_id':AUDIT39_REVIEW},'V34 runkey audit consumption')
        rex=rk['execution']; req(rex['per_parent_timeout_ms']==180000 and rex['effective_heavy_concurrency']==1 and rex['heavy_scaleout_authorized'] is False and rex['artifact_retention_days']==2,'V34 runkey execution')
        resume=rk['resume']; req(resume['partition_key']=='parent_index' and resume['carry_dir']=='stages/stage32-ex5/breadth-cycle-2/bc2-40-resume-carry' and resume['carried_parent_indices']==[] and resume['missing_parent_indices']==TARGET23 and resume['schedule_only_missing_parent_indices']==TARGET23,'V34 generation-3 resume partition')

        req(blob(RETRY40_1)==RETRY40_1_BLOB,'generation-1 retry receipt blob')
        retry1=json.loads(RETRY40_1.read_text()); req(retry1['canonical_sha256_without_this_field']==RETRY40_1_CANON and canon(retry1)==RETRY40_1_CANON,'generation-1 retry receipt canonical')
        req(retry1['generation1']['heavy_started'] is False and retry1['generation1']['authorization_result'] is False and retry1['retry_contract']['next_generation']==2,'generation-1 no-heavy provenance')

        req(blob(RETRY40_2)==RETRY40_2_BLOB,'generation-2 retry receipt blob')
        retry2=json.loads(RETRY40_2.read_text()); req(retry2['canonical_sha256_without_this_field']==RETRY40_2_CANON and canon(retry2)==RETRY40_2_CANON,'generation-2 retry receipt canonical')
        req(retry2['generation2']['heavy_started'] is False and retry2['generation2']['authorization_result'] is False and retry2['retry_contract']['next_generation']==3,'generation-2 no-heavy provenance')
        req(retry2['defect']['kind']=='PR_MERGE_PARENT_DELTA_MISMATCH' and retry2['defect']['corrected_workflow_git_blob_sha']=='eac5501973b98e7df01786fd8188581f7f470c9d','generation-2 defect provenance')

        dep=rk['dependency_locks']; req(dep['resume_contract_canonical']==CONTRACT40_CANON and dep['resume_contract_git_blob_sha']==CONTRACT40_BLOB and dep['resume_helper_git_blob_sha']==HELPER40_BLOB and dep['parent_worker_git_blob_sha']==WORKER40_BLOB and dep['resume_aggregator_git_blob_sha']==AGG40_BLOB and dep['current_main_exact_head']==CURRENT_MAIN,'V34 dependency locks')
        req(dep['generation1_retry_receipt_canonical']==RETRY40_1_CANON and dep['generation1_retry_receipt_git_blob_sha']==RETRY40_1_BLOB,'V34 generation-1 retry receipt locks')
        req(dep['generation2_retry_receipt_canonical']==RETRY40_2_CANON and dep['generation2_retry_receipt_git_blob_sha']==RETRY40_2_BLOB,'V34 generation-2 retry receipt locks')
        req(blob(CONTRACT40)==CONTRACT40_BLOB and json.loads(CONTRACT40.read_text())['canonical_sha256_without_this_field']==CONTRACT40_CANON,'V34 contract lock')
        req(blob(HELPER40)==HELPER40_BLOB and blob(WORKER40)==WORKER40_BLOB and blob(AGG40)==AGG40_BLOB,'V34 executable locks')
        req(prog['bc2_40_resume_contract_canonical']==CONTRACT40_CANON and prog['bc2_40_resume_contract_git_blob_sha']==CONTRACT40_BLOB,'V34 retained contract lock')
        req(prog['bc2_40_generation1_retry_receipt_canonical']==RETRY40_1_CANON and prog['bc2_40_generation1_retry_receipt_git_blob_sha']==RETRY40_1_BLOB,'V34 retained generation-1 retry receipt lock')
        req(prog['bc2_40_generation2_retry_receipt_canonical']==RETRY40_2_CANON and prog['bc2_40_generation2_retry_receipt_git_blob_sha']==RETRY40_2_BLOB,'V34 retained generation-2 retry receipt lock')
        req(s['bootstrap']['live_main_sync_path']=='stages/stage32-ex5/LIVE-MAIN-COORDINATION-SYNC-20260915.json' and s['bootstrap']['live_main_sync_blob_sha']==SYNC_V34_BLOB and s['bootstrap']['live_main_sync_canonical']==SYNC_V34_CANON,'V34 bootstrap sync lock')
        req(s['bootstrap']['current_repository_main']==CURRENT_MAIN and s['stage32_main_authority']['live_coordination_head']==CURRENT_MAIN,'V34 current main head')
        expected_working={
            'stages/stage32-ex5/breadth-cycle-2/bc2-39-hostile-audit-pass-receipt.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2-40-fresh-unknown23-replay-preflight.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2-40-resume-first-contract.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2-40-generation1-no-heavy-retry-receipt.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2-40-generation2-no-heavy-retry-receipt.json',
            'stages/stage32-ex5/breadth-cycle-2/bc2_40_replay_parent_unit.py',
            'stages/stage32-ex5/breadth-cycle-2/bc2_40_resume_aggregate.py',
            'stages/stage32-ex5/breadth-cycle-2/bc2_40_resume_execute.py',
            RUNKEY_PATH,
            'stages/stage32-ex5/verify_main_state.py',
        }
        req(set(s['current_leaf_working_set'])==expected_working,'V34 bounded working set')

    subprocess.run([sys.executable,str(V39)],check=True)
    subprocess.run([sys.executable,'-m','py_compile',str(PRODUCER40)],check=True)
    subprocess.run([sys.executable,str(RESUME40)],check=True)
    print('PASS: Stage32EX5',schema,'retains BC2-39 audited authority and fail-closed BC2-40 resume route')
    print('audited_lower_bound=7313 retained_unknown=23 partition=parent_index/23 heavy_authorized='+('YES' if schema==V34 else 'NO')+' main_credit=NO merge=NO')

if __name__=='__main__': main()
