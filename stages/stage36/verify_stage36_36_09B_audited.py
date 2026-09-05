#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json'
CERT_BLOB='da9143e587506522ed966d380d9980ff1875db0d'
LEGACY_COMMIT='125504622b46e462bd5fe8d7016f18d59717d696'
LEGACY_BLOB='96a25875ddc9e98f4261f2d494f38229bd354152'
CURRENT_BASE='8211bb0ef80de61ecf39c3b97743c58f1193187a'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V17_THIN_36_09B_AUDITED_USER_APPROVED'
HEAD='fd7b5d9dfef272bee2b6676797e6d12d8b07bde0'
CI_RUN=33952496327
CI_JOB=101269772315
AUDIT_REQUEST=5120319439
LEGAL='BLOCKED_NO_PROOF_CAPABLE_B_PLUS_K_JOINT_TEST'

def blob_bytes(b:bytes)->str:
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def blob_file(p:Path)->str:
 return blob_bytes(p.read_bytes())
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)
def git_show(spec:str)->bytes:
 return subprocess.check_output(['git','show',spec],cwd=ROOT)

def main()->None:
 req(blob_file(CERT)==CERT_BLOB,'36-09B certificate blob drift')
 c=json.loads(CERT.read_text())
 req(c.get('schema')=='STAGE36_36_09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT_V1','36-09B certificate schema moved')
 req(c.get('legal_outcome')==LEGAL,'36-09B legal outcome moved')
 h=c.get('S34_W03_hypothesis_audit',{})
 req(h.get('EXACT_SOURCE_RECEIVER_CONTRACT') is True and h.get('EXACT_ADDITIONAL_RECEIVER_CONDITION_K') is True,'36-09B exact receiver/K lost')
 for k in ['EXHAUSTIVE_AUXILIARY_BRANCH_B_SOURCE_LOCKED','EXACT_JOINT_B_PLUS_K_LOCAL_OR_GLOBAL_TEST','EXHAUSTIVE_RELEVANT_PROJECTIVE_RESIDUES_OR_QUOTIENT_POINTS','S34_W03_EXECUTABLE_NOW']:
  req(h.get(k) is False,f'36-09B S34-W03 preflight overclaim: {k}')
 req(c.get('cycle_update',{}).get('route_status')=='BLOCKED_NO_NEW_INFORMATION','36-09B cycle classification moved')
 req(c.get('cycle_update',{}).get('B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION')=='LIVE','36-09C/B2 route moved')
 req(all(v is False for v in c.get('claims',{}).values()),'36-09B certificate higher credit leaked')

 legacy=git_show(f'{LEGACY_COMMIT}:stages/stage36/MAIN-STATE.json')
 req(blob_bytes(legacy)==LEGACY_BLOB,'legacy V16 state blob drift')
 old=json.loads(legacy)
 req(old.get('schema')=='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V16_36_09B_PENDING_HOSTILE_AUDIT','legacy V16 schema moved')
 ou=old.get('completed_units',{}).get('36-09B',{})
 req(ou.get('promotion_status')=='PROVISIONAL_NOT_AUDITED' and ou.get('certificate_blob_sha')==CERT_BLOB,'legacy 36-09B provisional authority moved')
 req(ou.get('legal_outcome')==LEGAL and ou.get('S34_W03_EXECUTABLE_NOW') is False,'legacy 36-09B mathematical result moved')
 oc=old.get('current',{})
 req(oc.get('unit')=='36-09B' and oc.get('36_09C_entry_allowed') is False,'legacy hostile boundary moved')

 s=json.loads(STATE.read_text())
 req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE' and s.get('base_main_sha')==CURRENT_BASE,'V17 lifecycle/base moved')
 ls=s.get('legacy_authority_snapshot',{})
 req(ls.get('commit')==LEGACY_COMMIT and ls.get('blob_sha')==LEGACY_BLOB,'V17 legacy snapshot lock moved')
 fs=s.get('freshness_sync_36_09B_promotion',{})
 req(fs.get('main_sha')==CURRENT_BASE and fs.get('advanced_from')==LEGACY_COMMIT,'36-09B promotion freshness sync moved')
 a=s.get('authority_frontier',{}).get('36-09B',{})
 expected={'status':'AUDITED_BLOCKED_NO_PROOF_CAPABLE_B_PLUS_K_JOINT_TEST_USER_APPROVED','pr':1584,'hostile_audit_request_review':AUDIT_REQUEST,'final_user_approved_head':HEAD,'exact_head_ci':f'{CI_RUN}/{CI_JOB}','certificate_blob_sha':CERT_BLOB,'merged_main_sha':LEGACY_COMMIT,'legal_outcome':LEGAL,'S34_W03_EXECUTABLE_NOW':False,'verdict':'USER_APPROVED_PASS'}
 req(a==expected,'36-09B user-approved authority block moved')
 req('hostile_audit_review' not in a,'36-09B falsely recorded hostile PASS')
 cyc=s.get('cycle_ledger',{})
 req(cyc.get('B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION')=='LIVE','B2 not live after 36-09B authority')
 req(cyc.get('B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION')=='BLOCKED_NO_PROOF_CAPABLE_B_PLUS_K_JOINT_TEST','B4 block moved')
 req(cyc.get('counts')=={'live':1,'untested':4,'blocked':4,'dominated':1},'cycle counts moved')
 cur=s.get('current',{})
 req(cur.get('unit')=='36-09C' and cur.get('next_exact_leaf')=='36-09C_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_PREFLIGHT','36-09C routing moved')
 req(cur.get('36_09C_entry_allowed') is True and cur.get('36_06_entry_allowed') is False,'36-09C/36-06 gate moved')
 g=s.get('promotion_gates',{})
 for k in ['uniform_finite_ramification_support_proved','finite_exhaustive_H_twist_family_proved','local_solubility_filter_exhaustive','all_global_survivors_closed','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
  req(g.get(k) is False,f'promotion gate leaked: {k}')
 req(all(v is False for v in s.get('claims',{}).values()),'V17 higher claim leaked')
 print('PASS STAGE36_36_09B_AUDITED_USER_APPROVED_SUCCESSOR_REPLAY')
 print(f'head={HEAD}; exact_head_ci={CI_RUN}/{CI_JOB}; authority_merge={LEGACY_COMMIT}; current_base={CURRENT_BASE}; cert={CERT_BLOB}')
 print('authority=USER_APPROVED_PASS; no hostile PASS fabricated; next=36-09C unstarted')
if __name__=='__main__': main()
