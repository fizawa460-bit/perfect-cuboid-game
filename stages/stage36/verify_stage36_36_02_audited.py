#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE_PATH=ROOT/"stages/stage36/MAIN-STATE.json"
INV_PATH=ROOT/"stages/stage36/36-02/representative-inventory.json"
AUDITED_INVENTORY_BLOB="88130b9380a677a191f91c24df87618e65be0a2f"
AUDITED_HEAD="3a78f9ff156b53f509625d353df48d1b3e02b836"
AUDIT_REVIEW=5113379283
AUDIT_CI_RUN=33876389406
AUDIT_CI_JOB=101034265419
AUDITED_PR_MERGE="4c93ccb79e95cbcd9e2416ad3b6a3f4788d6f586"
PROMOTION_MERGE="26fb608cb2551ab2102ae36ad3b57c063959df58"
V6_BASE="bdd707e52ded061014bfbb6158762e8b997e7a38"
V7_BASE="45f290a443cf71b1fc62f031994122c3fa58f0e9"
V8_BASE="4ec2b9af886f9ac9be13c3324788c26625c9e5d9"
V9_BASE="de1df3d25c39306e5601646309b38aaad56967bd"
V10_BASE="74144644975d7800c6c5b529c5d8789f70366c2e"
HISTORICAL_BASE="a873c8fca0074aa966a22e36475a3551a378560d"
FRESHNESS_36_04={"sync_pr":1565,"main_sha":V8_BASE,"merge_commit":"b900a925ce25556bf85c929b1c73aff414c77430","scope":"Stage32-only advance via #1563; no Stage36, Stage29 Campedelli/sign-cover source, or Arsenal authority changes"}
PROMO_36_04={"pr":1568,"exact_head":"53b0c3b2a84ef200848d6b4b515c94589798d295","exact_head_ci_run":33924921726,"exact_head_ci_job":101191239139,"merged_main_sha":"dca962cdf37d4252316885dc57f3c0a591db4ecb","scope":"mechanical audited-state promotion only","NEW_THEOREM_CREDIT":False}
V5="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V5_36_02_AUDITED"
V6="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V6_36_03_PENDING_AUDIT"
V7="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V7_36_03_AUDITED"
V8="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V8_36_04_PENDING_AUDIT"
V9="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V9_36_04_AUDITED"
V10="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V10_36_05_PENDING_AUDIT"

def blob_sha(path):
 d=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)

def main():
 req(blob_sha(INV_PATH)==AUDITED_INVENTORY_BLOB,"36-02 audited inventory blob drift")
 inv=json.loads(INV_PATH.read_text())
 req(inv.get("schema")=="STAGE36_36_02_THREE_Q_REPRESENTATIVE_INVENTORY_V1","36-02 inventory schema moved")
 req(inv.get("base_main_sha")==HISTORICAL_BASE,"36-02 historical base moved")
 req(inv.get("pass_condition")=={"THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT":True,"EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM":False},"36-02 pass condition moved")
 req(inv.get("finite_reconstruction",{}).get("q_orbit_sizes")==[6,2,2],"36-02 Q orbit split moved")
 req(inv.get("finite_reconstruction",{}).get("geometric_qi_orbit_sizes")==[8,2],"36-02 Q(i) orbit split moved")
 req(set(inv.get("representatives",{}))=={"Q6_GEOM8","Q2_GEOM8","Q2_GEOM2"},"36-02 representative set moved")
 req(inv.get("degree_check",{}).get("generic_squareclass_rank")==3 and inv.get("degree_check",{}).get("canonical_quotient_degree")==8,"36-02 degree/rank moved")
 req(all(v is False for v in inv.get("claims",{}).values()),"36-02 inventory leaked higher credit")
 s=json.loads(STATE_PATH.read_text()); schema=s.get("schema")
 req(schema in {V5,V6,V7,V8,V9,V10},"36-02 audited successor schema moved")
 req(s.get("stage36_36_02_authority")=={"pr":1541,"hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"merged_main_sha":AUDITED_PR_MERGE,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"inventory_blob_sha":AUDITED_INVENTORY_BLOB,"verdict":"PASS"},"36-02 authority block moved")
 req(s.get("completed_units",{}).get("36-02")=={"leaf":"36-02_THREE_Q_REPRESENTATIVE_INVENTORY","status":"AUDITED_PASS","certificate":"stages/stage36/36-02/representative-inventory.json","verifier":"stages/stage36/verify_stage36_36_02.py","successor_verifier":"stages/stage36/verify_stage36_36_02_audited.py","hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"merged_main_sha":AUDITED_PR_MERGE,"inventory_blob_sha":AUDITED_INVENTORY_BLOB,"THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT":True,"EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM":False,"NEW_THEOREM_CREDIT":False,"promotion_status":"AUDITED"},"36-02 completed-unit provenance moved")
 g=s.get("promotion_gates",{})
 req(g.get("source_authority_lock_complete") is True and g.get("three_Q_representatives_exact") is True,"36-01/02 gates lost")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 if schema==V5:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_PR_MERGE,"V5 lifecycle moved"); req("36-03" not in s.get("completed_units",{}),"36-03 started in V5")
 elif schema==V6:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V6_BASE,"V6 lifecycle moved"); req(g.get("physical_open_push_and_boundary_complete") is False and s.get("current",{}).get("unit")=="36-03","V6 boundary moved")
 elif schema==V7:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==V7_BASE,"V7 lifecycle moved"); req(g.get("physical_open_push_and_boundary_complete") is True and s.get("current",{}).get("unit")=="36-04","V7 successor moved"); req("36-04" not in s.get("completed_units",{}),"36-04 started in V7")
 elif schema==V8:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V8_BASE,"V8 lifecycle moved"); req(s.get("freshness_sync_36_04")==FRESHNESS_36_04,"V8 freshness sync moved"); req(g.get("pointwise_H_torsor_class_explicit") is False,"V8 36-04 gate moved"); req(s.get("completed_units",{}).get("36-04",{}).get("promotion_status")=="PROVISIONAL_NOT_AUDITED","36-04 prematurely audited"); req("36-05" not in s.get("completed_units",{}),"36-05 started in V8")
 elif schema==V9:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==V9_BASE,"V9 lifecycle moved"); req(g.get("pointwise_H_torsor_class_explicit") is True,"V9 audited gate lost"); req(s.get("completed_units",{}).get("36-04",{}).get("promotion_status")=="AUDITED","36-04 audit promotion lost"); req(s.get("current",{}).get("unit")=="36-05","V9 successor moved"); req("36-05" not in s.get("completed_units",{}),"36-05 started in V9")
 else:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V10_BASE,"V10 lifecycle moved")
  req(s.get("stage36_36_04_promotion")==PROMO_36_04,"36-04 promotion provenance moved")
  req(g.get("pointwise_H_torsor_class_explicit") is True and g.get("uniform_finite_ramification_support_proved") is False,"V10 gate boundary moved")
  u=s.get("completed_units",{}).get("36-05",{}); req(u.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT" and u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","V10 36-05 boundary moved")
  req(s.get("current",{}).get("unit")=="36-05" and s.get("current",{}).get("36_06_entry_allowed") is False,"36-06 entry opened")
  req("36-06" not in s.get("completed_units",{}),"36-06 started in V10")
 if schema!=V5:
  p=s.get("stage36_36_02_promotion",{}); req(p.get("pr")==1548 and p.get("merged_main_sha")==PROMOTION_MERGE and p.get("NEW_THEOREM_CREDIT") is False,"36-02 promotion provenance moved")
 print("PASS STAGE36_36_02_AUDITED_SUCCESSOR_REPLAY")
 print(f"hostile_audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}; exact_head_ci={AUDIT_CI_RUN}/{AUDIT_CI_JOB}")
 print(f"audited_inventory_blob={AUDITED_INVENTORY_BLOB}; successor_schema={schema}")
 print("no theorem/receiver/endpoint/perfect-cuboid credit")
if __name__=="__main__": main()
