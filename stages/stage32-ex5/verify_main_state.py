#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
B2=HERE/'breadth-cycle-2'
STATE=HERE/'MAIN-STATE.json'
SYNC=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260915.json'
CAND=B2/'bc2-40-generation4-complete-candidate.json'
PASSREC=B2/'bc2-40-hostile-audit-pass-consumption.json'
V39=B2/'verify_bc2_39_targeted_replay_checkpoint.py'
RESUME=B2/'verify_bc2_40_resume_first_contract.py'
V41=B2/'verify_bc2_41_first_e8_block_main_subtraction_adapter_candidate.py'

V35='STAGE32EX5_MAIN_COMPACT_STATE_V35_BC2_40_AUDIT_PASS_CONSUMED'
MAIN='117310b6a9d40273683cab8c08cc9e5e0cc584d9'
CAND_BLOB='e7862c66ffa6f55c5bf51e7cd76c2e6671bcbeb0'
CAND_CANON='e60f3b862a031d402031d3e293208066189c06e5e77f8ed9198cadd692e50599'
PASS_CANON='2e5ce31e9193a4437c9149556904bd20d5ecdab2fa8edd175e518efda5d799e3'
AUDIT_HEAD='b3b16f3db20074e3dbdb1851ad123d5c2004b843'
AUDIT_REVIEW=5204245683

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)

def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()

def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def checked(path, expected_canon, label, expected_blob=None):
    req(path.is_file(),label+' missing')
    if expected_blob is not None: req(blob(path)==expected_blob,label+' blob')
    o=json.loads(path.read_text())
    req(o.get('canonical_sha256_without_this_field')==expected_canon,label+' canonical field')
    req(canon(o)==expected_canon,label+' canonical replay')
    return o

def main():
    s=json.loads(STATE.read_text())
    req(s['schema']==V35,'schema')
    req(s['bootstrap']['active_work_pr']==1776 and s['bootstrap']['merge_authorized'] is False,'bootstrap')

    sync=json.loads(SYNC.read_text())
    req(sync['live_exact_head']==MAIN,'live main head')
    lm=sync['live_main_state']
    req(lm['authoritative_remaining_strata']==17128,'MAIN strata')
    req(lm['certified_remaining_terminal_upper_bound']==26876434389242951089388,'MAIN terminal upper bound')
    req(lm['full178_complete'] is False,'MAIN FULL178 firewall')

    c=checked(CAND,CAND_CANON,'BC2-40 complete candidate',CAND_BLOB)
    er=c['exact_result']
    req(er['status']=='COMPLETE_EXACT_UNION' and er['complete_parent_count']==23 and er['expected_parent_count']==23,'candidate complete union')
    req(er['new_exact_parent_unsat_count']==23 and er['unknown_count']==0 and er['sat_count']==0,'candidate result')
    req(er['gap_count']==0 and er['overlap_count']==0 and er['coverage_exact'] is True,'candidate exact coverage')
    req(er['known_parent_unsat_count_lower_bound_audited']==7313 and er['known_parent_unsat_count_lower_bound_candidate']==7336,'candidate lower bounds')
    req(er['whole_first_block_picard64_unsat_candidate'] is True and er['whole_stratum_closed'] is False,'candidate scope')

    r=checked(PASSREC,PASS_CANON,'BC2-40 audit PASS consumption')
    a=r['audit']; co=r['consumption']; ev=r['evidence']
    req(a['exact_head']==AUDIT_HEAD and a['review_id']==AUDIT_REVIEW and a['pr']==1776,'audit provenance')
    req(a['delta_commits_from_bc2_39_audit']==72 and a['merge_ready_freshness']=='CLEAR','audit freshness')
    req(co['ex5_audited_known_parent_unsat_lower_bound_before']==7313 and co['ex5_audited_known_parent_unsat_lower_bound_after']==7336,'audit consumption lower bound')
    req(co['new_exact_parent_unsat_count']==23 and co['remaining_unknown_count']==0 and co['sat_count']==0,'audit consumption result')
    req(co['first_e8_block_picard64_obstruction_closed'] is True,'first e8 block closure')
    req(co['stage32_main_subtraction_authorized'] is False and co['new_heavy_authorized'] is False and co['merge_authorized'] is False,'consumption firewalls')
    req(ev['complete_candidate_canonical_sha256']==CAND_CANON and ev['complete_candidate_git_blob_sha']==CAND_BLOB,'candidate binding')
    req(ev['workflow_run_id']==34910430722 and ev['heavy_job_id']==104196535142,'compute provenance')

    f=s['frontier']
    req(f['e8_bc2_40_audited'] is True,'BC2-40 audited')
    req(f['e8_bc2_40_hostile_audit_exact_head']==AUDIT_HEAD and f['e8_bc2_40_hostile_audit_review_id']==AUDIT_REVIEW,'BC2-40 audit binding')
    req(f['e8_bc2_40_executed'] is True and f['e8_bc2_40_remaining_unknown_count']==0 and f['e8_bc2_40_sat_count']==0,'BC2-40 execution')
    req(f['e8_known_parent_unsat_count_lower_bound']==7336 and f['e8_whole_first_block_unsat'] is True,'EX5 audited 7336')
    req(f['population_wide_main_consumable_result_complete'] is False,'MAIN adapter firewall')
    req(f['whole_g1_d008_e4_stratum_closed'] is False,'whole stratum firewall')

    ib=s['intermediate_audit_boundary']
    req(ib['last_hostile_audit_exact_head']==AUDIT_HEAD and ib['last_hostile_audit_review_id']==AUDIT_REVIEW and ib['last_hostile_audit_status']=='PASS','audit boundary')
    req(ib['new_audit_boundary_exists'] is False and ib['re_audit_required'] is False,'audit consumed')

    ex=s['execution']; nx=s['next_step']
    req(ex['runkey_armed'] is False and ex['new_generation_rearm_authorized'] is False and ex['heavy_scaleout_authorized'] is False,'no new heavy')
    req(nx['main_promotion_authorized'] is False and nx['merge_authorized'] is False and nx['n350_registration_authorized'] is False,'next-step firewalls')
    req(nx['generation4_rearm_authorized'] is False,'generation4 consumed')

    for sec in ('historical_credit_firewall','firewalls'):
        req(all(v is False for v in s[sec].values()),sec)
    req(all(v is False for k,v in s['credit'].items() if k!='level'),'credit firewall')
    req(s['stage32_main_authority']['ex5_auto_promotes_to_main'] is False,'no EX5 auto-promotion')
    req(s['stage32_main_authority']['full178_numerical_census_complete'] is False,'FULL178 not complete')

    subprocess.run([sys.executable,str(V39)],check=True)
    subprocess.run([sys.executable,str(RESUME)],check=True)
    subprocess.run([sys.executable,str(V41)],check=True)

    print('PASS: Stage32EX5 BC2-40 hostile-audit PASS consumed; EX5 audited lower bound=7336; first e8 block Picard64 obstruction closed; BC2-41 113-terminal MAIN subtraction candidate retained audit-required; MAIN credit=NO new heavy=NO merge=NO')

if __name__=='__main__':
    main()
