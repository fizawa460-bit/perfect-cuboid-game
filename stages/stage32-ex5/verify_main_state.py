#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent; B2=HERE/'breadth-cycle-2'; STATE=HERE/'MAIN-STATE.json'; SYNC=HERE/'LIVE-MAIN-COORDINATION-SYNC-20260914.json'; CHECKPOINT=B2/'bc2-39-fresh-unknown30-replay-checkpoint.json'; RUNKEY=HERE/'runkeys/bc2-39-fresh-unknown30-replay.json'; RETAINED=B2/'verify_bc2_39_targeted_replay_checkpoint.py'; WORKFLOW=HERE.parent.parent/'.github/workflows/stage32-ex5-main.yml'
SYNC_BLOB='c9a3a878413df5afc634f99b94707534412b5d84'; SYNC_CANON='fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c'; CP_BLOB='43565b80d730caa5db8e3c95aa0a1e58217155cf'; CP_CANON='77f9339f99070b35df09ac4f88c458ab23220fffa5679a9c1c125b429cb3f86e'; RUNKEY_BLOB='2e0f7467ffd5b16dc9f2e8feaefaedbee5ffbfab'; RETAINED_BLOB='0746b3976b79bc26bddc141f8d023da5b780ea96'; UNKNOWN23_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None); return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    s=json.loads(STATE.read_text()); req(s['schema']=='STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY','schema'); b=s['bootstrap']; req(b['active_work_pr']==1776 and b['merge_authorized'] is False,'bootstrap')
    req(blob(SYNC)==SYNC_BLOB,'live MAIN sync blob'); sync=json.loads(SYNC.read_text()); req(sync['canonical_sha256_without_this_field']==SYNC_CANON and canon(sync)==SYNC_CANON,'live MAIN sync canonical'); lm=sync['live_main_state']; req(lm['authoritative_remaining_strata']==17128 and lm['certified_remaining_terminal_upper_bound']==26876434389242951089388 and lm['full178_complete'] is False,'MAIN authority sync')
    req(blob(CHECKPOINT)==CP_BLOB,'checkpoint blob'); cp=json.loads(CHECKPOINT.read_text()); req(cp['canonical_sha256_without_this_field']==CP_CANON and canon(cp)==CP_CANON,'checkpoint canonical'); r=cp['replay']; req((r['unsat_count'],r['unknown_count'],r['sat_count'])==(7,23,0) and r['unknown_parent_indices_sha256']==UNKNOWN23_SHA,'checkpoint partition')
    req(blob(RUNKEY)==RUNKEY_BLOB,'consumed runkey blob'); rk=json.loads(RUNKEY.read_text()); req(rk['generation']==2 and rk['armed'] is False and rk['consumed_run']['accepted_for_hostile_audit'] is True,'runkey consumed')
    req(blob(RETAINED)==RETAINED_BLOB,'retained verifier blob')
    f=s['frontier']; req(f['e8_known_parent_unsat_count_lower_bound']==7306 and f['e8_bc2_39_candidate_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_executed'] is True and f['e8_bc2_39_audited'] is False and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN23_SHA,'frontier quarantine')
    cur=s['current']; a=s['intermediate_audit_boundary']; req(cur['status']=='BC2_39_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and cur['next_route']=='HOSTILE_AUDIT_BC2_39_TARGETED_REPLAY','route'); req(a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True and a['bc2_39_execution_authorized'] is False,'audit freeze')
    for sec in ('historical_credit_firewall','firewalls'):
        for k,v in s[sec].items(): req(v is False,'firewall '+sec+'.'+k)
    for k,v in s['credit'].items():
        if k!='level': req(v is False,'credit '+k)
    wf=WORKFLOW.read_text(); req('verify_bc2_39_targeted_replay_checkpoint.py' in wf,'retained checkpoint step missing'); req('authorize-bc2-39-fresh-unknown30:' not in wf and '\n  bc2-39-fresh-unknown30:' not in wf,'BC2-39 heavy not retired')
    subprocess.run([sys.executable,str(RETAINED)],check=True)
    print('PASS: Stage32EX5 V32 BC2-39 audit boundary is frozen and fail-closed')
    print('audited_lower_bound=7306 candidate_lower_bound=7313 retained_unknown=23 sat=0 heavy=RETIRED main_credit=NO merge=NO')
if __name__=='__main__': main()
