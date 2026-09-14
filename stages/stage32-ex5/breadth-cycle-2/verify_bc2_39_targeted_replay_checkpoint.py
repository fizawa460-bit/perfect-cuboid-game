#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
CHECKPOINT=HERE/'bc2-39-fresh-unknown30-replay-checkpoint.json'
RUNKEY=ROOT/'runkeys/bc2-39-fresh-unknown30-replay.json'
SOURCE=HERE/'bc2_39_replay_explicit_fresh_unknown30.py'
PREFLIGHT=HERE/'bc2-39-fresh-unknown30-replay-preflight.json'
RETRY=HERE/'bc2-39-generation1-no-heavy-retry-receipt.json'
B38=HERE/'bc2_38_replay_explicit_fresh_unknown34.py'
CP38=HERE/'bc2-38-fresh-unknown34-replay-checkpoint.json'
B32=HERE/'bc2_32_replay_explicit_fresh_unknown170.py'
B19=HERE/'bc2_19_n354_survivor_normal_positivity_mass_replay.py'
B18=HERE/'bc2_18_n354_survivor_exceptional_mod8_decomposition.py'
STATE=ROOT/'MAIN-STATE.json'
WORKFLOW=HERE.parents[2]/'.github/workflows/stage32-ex5-main.yml'

CP_BLOB='43565b80d730caa5db8e3c95aa0a1e58217155cf'
CP_CANON='77f9339f99070b35df09ac4f88c458ab23220fffa5679a9c1c125b429cb3f86e'
RUNKEY_BLOB='2e0f7467ffd5b16dc9f2e8feaefaedbee5ffbfab'
SOURCE_BLOB='e322029cfc4476ce8cf3685ca04f35b58e2ce9f2'
PREFLIGHT_BLOB='e3dab72865d734f2420fb71ddf3c29115f9df68e'
PREFLIGHT_CANON='7bda94c5869c988892c979873f13a1c311debedbbe9fcc670a253e339fb5e435'
RETRY_BLOB='a812727a9e5dfa29e88fd74aee292386a5231e64'
RETRY_CANON='cb0a292479cf230f96a052d771a448cbc8e4b5254ed4ae31297ca470fa929d79'
B38_BLOB='6fb0af6c77e44edfa5d2b8a13fbde73bfbd468aa'
CP38_BLOB='91eca02054cd2dbf702dd4a7635398ef76ee832f'
B32_BLOB='7cfe8450cb9b9ab7f04da797d487655505598b93'
B19_BLOB='b2899aa228e7a3ee97526e3787ffbefa483530b4'
B18_BLOB='1e2ed93cae3c5b446c8d90c1ae2250be83289c79'
TARGET_SHA='d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7'
UNKNOWN_SHA='29cba46b566de1e0ccad58e0f16897a1fd9fab60d06109e73772628170d68c02'
STATUS_SHA='7c6b390281a2ee68fac023d1e0130103609a0d2ed2b22e36aa2ca0b89facbfb8'
UNSAT=[1048,1050,1216,1218,1251,1719,2634]
UNKNOWN=[1056,1103,1206,1243,1703,1706,1717,1733,1798,2092,2122,2187,2407,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]
V32='STAGE32EX5_MAIN_COMPACT_STATE_V32_BC2_39_TARGETED_REPLAY_AUDIT_BOUNDARY'
V33='STAGE32EX5_MAIN_COMPACT_STATE_V33_BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT'
V34='STAGE32EX5_MAIN_COMPACT_STATE_V34_BC2_40_RESUME_RUNKEY_ARMED_EXECUTION'

def req(v,m):
    if not v: raise SystemExit('FAIL: '+m)
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],text=True).strip()
def canon(o):
    q=dict(o); q.pop('canonical_sha256_without_this_field',None)
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
    req(blob(CHECKPOINT)==CP_BLOB,'checkpoint blob')
    cp=json.loads(CHECKPOINT.read_text())
    req(cp['schema']=='STAGE32EX5_BC2_39_FRESH_UNKNOWN30_REPLAY_V1' and cp['canonical_sha256_without_this_field']==CP_CANON and canon(cp)==CP_CANON,'checkpoint canonical')
    r=cp['replay']
    req((r['parents_checked'],r['unsat_count'],r['unknown_count'],r['sat_count'])==(30,7,23,0) and r['per_parent_timeout_ms']==160000 and r['unknown_parent_indices_sha256']==UNKNOWN_SHA and r['status_stream_sha256']==STATUS_SHA,'partition/hash')
    req(r['unsat_parent_indices']==UNSAT and r['unknown_parent_indices']==UNKNOWN and r['sat_parent_indices']==[] and set(UNSAT).isdisjoint(UNKNOWN),'partition identity')
    t=cp['target']
    req(t['audited_bc2_38_unknown_count']==30 and t['parent_indices_sha256']==TARGET_SHA and t['prior_audited_unsat_count']==7306 and sorted(t['parent_indices'])==sorted(UNSAT+UNKNOWN),'target')
    req(cp['credit']['known_parent_unsat_count_lower_bound']==7313 and cp['credit']['new_exact_parent_unsat_count']==7 and cp['credit']['stage32_main_credit'] is False and cp['credit']['full178_complete'] is False,'credit')
    req(cp['firewalls']['timeout_unknown_relabelled_unsat'] is False and cp['firewalls']['unknown_dropped'] is False and cp['firewalls']['main_promotion'] is False and cp['firewalls']['merge_authorized'] is False,'firewalls')

    req(blob(SOURCE)==SOURCE_BLOB and blob(PREFLIGHT)==PREFLIGHT_BLOB and blob(RETRY)==RETRY_BLOB and blob(B38)==B38_BLOB and blob(CP38)==CP38_BLOB and blob(B32)==B32_BLOB and blob(B19)==B19_BLOB and blob(B18)==B18_BLOB,'source identity')
    pf=json.loads(PREFLIGHT.read_text()); req(pf['canonical_sha256_without_this_field']==PREFLIGHT_CANON and canon(pf)==PREFLIGHT_CANON,'preflight canonical')
    rr=json.loads(RETRY.read_text()); req(rr['canonical_sha256_without_this_field']==RETRY_CANON and canon(rr)==RETRY_CANON and rr['generation1']['heavy_started'] is False and rr['retry_contract']['next_generation']==2,'retry receipt')
    req(blob(RUNKEY)==RUNKEY_BLOB,'consumed runkey blob')
    rk=json.loads(RUNKEY.read_text()); req(rk['generation']==2 and rk['armed'] is False,'runkey consumed')
    cr=rk['consumed_run']
    req(cr['accepted_for_hostile_audit'] is True and cr['exact_head']=='38a62af36630b0d7a899f68bcd2295f0a07aaea6' and cr['workflow_run_id']==34794585988 and cr['authorize_job_id']==103825118780 and cr['compute_job_id']==103825180872 and cr['artifact_id']==10330073656,'run receipt')
    req(cr['artifact_zip_sha256']=='fb26723ef7abcfcacd2a241bcfbacdd07684b765e54e777bc36c2b586f305fd7' and cr['raw_json_sha256']=='143b2ea64d1a7aad4ac1008d0837198d5f0f5b2b430a4b62886e5da1ebbbc966' and cr['checkpoint_git_blob_sha']==CP_BLOB and cr['checkpoint_canonical']==CP_CANON,'artifact receipt')
    req((cr['new_unsat_count'],cr['remaining_unknown_count'],cr['sat_count'],cr['known_parent_unsat_count_lower_bound'])==(7,23,0,7313) and cr['remaining_unknown_parent_indices_sha256']==UNKNOWN_SHA and cr['status_stream_sha256']==STATUS_SHA,'run counts')

    s=json.loads(STATE.read_text()); schema=s['schema']
    if schema==V32:
        f=s['frontier']; a=s['intermediate_audit_boundary']; cur=s['current']
        req(f['e8_bc2_39_executed'] is True and f['e8_bc2_39_audited'] is False and f['e8_bc2_39_new_parent_unsat_count']==7 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN_SHA and f['e8_known_parent_unsat_count_lower_bound']==7306 and f['e8_bc2_39_candidate_known_parent_unsat_count_lower_bound']==7313,'V32 frontier')
        req(cur['status']=='BC2_39_TARGETED_REPLAY_EXECUTED_AUDIT_REQUIRED' and a['freeze_active'] is True and a['new_audit_boundary_exists'] is True and a['re_audit_required'] is True,'V32 audit boundary')
    else:
        req(schema in {V33,V34},'V33/V34 schema')
        f=s['frontier']; a=s['intermediate_audit_boundary']; cur=s['current']
        req(f['e8_bc2_39_audited'] is True and f['e8_known_parent_unsat_count_lower_bound']==7313 and f['e8_bc2_39_remaining_unknown_count']==23 and f['e8_bc2_39_remaining_unknown_parent_indices_sha256']==UNKNOWN_SHA,'consumed frontier')
        req(f['e8_bc2_39_hostile_audit_exact_head']=='4b974550d9ad030973fec99e19a090f6785f8aa8' and f['e8_bc2_39_hostile_audit_review_id']==5193423203,'hostile audit identity')
        req(a['last_hostile_audit_exact_head']=='4b974550d9ad030973fec99e19a090f6785f8aa8' and a['last_hostile_audit_review_id']==5193423203 and a['freeze_active'] is False and a['new_audit_boundary_exists'] is False and a['re_audit_required'] is False,'audit receipt')
        if schema==V33:
            req(cur['status']=='BC2_39_AUDIT_CONSUMED_BC2_40_PREFLIGHT_READY_NOT_ARMED' and cur['next_route']=='BC2_40_FRESH_RUNKEY_AUTHORIZATION' and a['bc2_40_execution_authorized'] is False and f['e8_bc2_40_execution_authorized'] is False,'V33 routing')
        else:
            req(cur['status']=='BC2_40_RESUME_RUNKEY_ARMED_EXECUTION_AUTHORIZED' and cur['next_route']=='BC2_40_RESUME_EXECUTE_MISSING_PARENT_UNITS' and cur['blocker']=='BC2_40_RESUME_HEAVY_PENDING','V34 routing')
            req(a['bc2_40_execution_authorized'] is True and f['e8_bc2_40_execution_authorized'] is True and f['e8_bc2_40_executed'] is False,'V34 authorization')

    wf=WORKFLOW.read_text()
    req('verify_bc2_39_targeted_replay_checkpoint.py' in wf and 'authorize-bc2-39-fresh-unknown30:' not in wf and '\n  bc2-39-fresh-unknown30:' not in wf,'BC2-39 workflow lifecycle')
    print('PASS: Stage32EX5 BC2-39 retained evidence remains fail-closed across audit consumption')
    print('bc2_39=7_NEW_UNSAT_23_RETAINED_UNKNOWN_0_SAT; audited_after_review=7313')
if __name__=='__main__': main()
