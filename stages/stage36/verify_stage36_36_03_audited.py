#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE_PATH=ROOT/"stages/stage36/MAIN-STATE.json"
CERT_PATH=ROOT/"stages/stage36/36-03/physical-open-boundary.json"
AUDITED_CERT_BLOB="fc1947b2de08f7d8a104bdc91902b20e88635349"
AUDITED_HEAD="5fd7af75ede4cd2eceb70f9f21bd2b98ec5453a6"
AUDIT_REVIEW=5113890803
AUDIT_CI_RUN=33880359998
AUDIT_CI_JOB=101047238497
AUDITED_MERGE="45f290a443cf71b1fc62f031994122c3fa58f0e9"
PROMOTION_MERGE="efe25f4ef74dc776da7ccad3f5cd786b0b2906e4"
V8_BASE="4ec2b9af886f9ac9be13c3324788c26625c9e5d9"
V9_BASE="de1df3d25c39306e5601646309b38aaad56967bd"
V10_BASE="09d42186c06cd906042f2ca3f16a9deaf4f1b4a3"
V11_BASE="ee3e7aafd1742c5d96e2871f117412ef0823d57e"
V12_BASE="dc5898281a7ccea25d8ee0c1ae9953a18941ec08"
PROMO_36_05_MERGE="99c5f1634dd59d4bc5698cbb775801dd9d000827"
FRESHNESS_36_04={"sync_pr":1565,"main_sha":V8_BASE,"merge_commit":"b900a925ce25556bf85c929b1c73aff414c77430","scope":"Stage32-only advance via #1563; no Stage36, Stage29 Campedelli/sign-cover source, or Arsenal authority changes"}
PROMO_36_04={"pr":1568,"exact_head":"53b0c3b2a84ef200848d6b4b515c94589798d295","exact_head_ci_run":33924921726,"exact_head_ci_job":101191239139,"merged_main_sha":"dca962cdf37d4252316885dc57f3c0a591db4ecb","scope":"mechanical audited-state promotion only","NEW_THEOREM_CREDIT":False}
PROMO_36_05={"pr":1573,"exact_head":"741eb0ef6f07ef6551602c84a1b7493977023feb","exact_head_ci_run":33930463014,"exact_head_ci_job":101207828353,"merged_main_sha":PROMO_36_05_MERGE,"scope":"mechanical audited-state promotion of blocked 36-05 authority only; route to unstarted 36-09","NEW_THEOREM_CREDIT":False}
V7="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V7_36_03_AUDITED"
V8="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V8_36_04_PENDING_AUDIT"
V9="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V9_36_04_AUDITED"
V10="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V10_36_05_PENDING_AUDIT"
V11="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V11_36_05_AUDITED_BLOCKED"
V12="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V12_36_09_BREADTH_GATE_PENDING_AUDIT"

def blob_sha(path):
 d=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)

def main():
 req(blob_sha(CERT_PATH)==AUDITED_CERT_BLOB,"36-03 audited certificate blob drift")
 cert=json.loads(CERT_PATH.read_text())
 req(cert.get("schema")=="STAGE36_36_03_PHYSICAL_OPEN_PUSH_BOUNDARY_V1","36-03 audited schema moved")
 req(cert.get("pass_condition")=={"ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT":True,"CONVERSE_LIFT_CLAIM":False},"36-03 pass condition moved")
 req(cert.get("scheme_vs_rational_firewall",{}).get("U_H_Q_equals_q_H_of_U_Q_claimed") is False,"36-03 lift firewall moved")
 req(cert.get("restricted_receiver_preparation",{}).get("receiver_intersection_exclusion_executed") is False,"36-03 S34-W03 execution drift")
 req(all(v is False for v in cert.get("claims",{}).values()),"36-03 audited certificate leaked higher credit")
 s=json.loads(STATE_PATH.read_text()); schema=s.get("schema")
 req(schema in {V7,V8,V9,V10,V11,V12},"36-03 audited successor schema moved")
 req(s.get("stage36_36_03_authority")=={"pr":1553,"hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"merged_main_sha":AUDITED_MERGE,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"certificate_blob_sha":AUDITED_CERT_BLOB,"verdict":"PASS"},"36-03 authority block moved")
 req(s.get("completed_units",{}).get("36-03")=={"leaf":"36-03_PHYSICAL_OPEN_PUSH_AND_BOUNDARY","status":"AUDITED_PASS","certificate":"stages/stage36/36-03/physical-open-boundary.json","verifier":"stages/stage36/verify_stage36_36_03.py","successor_verifier":"stages/stage36/verify_stage36_36_03_audited.py","hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"merged_main_sha":AUDITED_MERGE,"certificate_blob_sha":AUDITED_CERT_BLOB,"ENDPOINT_TO_EACH_Q_REPRESENTATIVE_PUSH_EXACT":True,"CONVERSE_LIFT_CLAIM":False,"NEW_THEOREM_CREDIT":False,"promotion_status":"AUDITED"},"36-03 completed-unit provenance moved")
 g=s.get("promotion_gates",{})
 for key in ["source_authority_lock_complete","three_Q_representatives_exact","physical_open_push_and_boundary_complete"]: req(g.get(key) is True,f"audited predecessor gate lost: {key}")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 if schema==V7:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_MERGE,"V7 lifecycle moved"); req(s.get("current",{}).get("unit")=="36-04" and "36-04" not in s.get("completed_units",{}),"V7 successor moved")
 elif schema==V8:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V8_BASE,"V8 lifecycle moved"); req(s.get("freshness_sync_36_04")==FRESHNESS_36_04,"V8 freshness sync moved")
 elif schema==V9:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==V9_BASE,"V9 lifecycle moved"); req(s.get("completed_units",{}).get("36-04",{}).get("promotion_status")=="AUDITED","V9 36-04 audit provenance lost")
 elif schema==V10:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V10_BASE,"V10 lifecycle moved"); req(s.get("stage36_36_04_promotion")==PROMO_36_04,"36-04 promotion provenance moved")
  u=s.get("completed_units",{}).get("36-05",{}); req(u.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT" and u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","V10 36-05 boundary moved")
 elif schema==V11:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==V11_BASE,"V11 lifecycle moved")
  req(s.get("stage36_36_04_promotion")==PROMO_36_04,"36-04 promotion provenance moved in V11")
  u=s.get("completed_units",{}).get("36-05",{}); req(u.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT" and u.get("promotion_status")=="AUDITED","V11 36-05 audit promotion moved")
  req(u.get("hostile_audit_review")==5118563918 and u.get("exact_head_ci_run")==33928640974 and u.get("exact_head_ci_job")==101202500740,"V11 36-05 audit provenance moved")
  req(s.get("current",{}).get("unit")=="36-09" and s.get("current",{}).get("36_06_entry_allowed") is False,"V11 blocked-route successor moved")
 else:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V12_BASE,"V12 lifecycle moved")
  req(s.get("stage36_36_05_promotion")==PROMO_36_05,"36-05 promotion provenance moved in V12")
  u=s.get("completed_units",{}).get("36-09",{}); req(u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED" and u.get("RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED") is False,"V12 breadth gate credit moved")
  req(s.get("current",{}).get("36_09A_entry_allowed") is False and "36-09A" not in s.get("completed_units",{}),"36-09A started before audit")
 promo=s.get("stage36_36_03_promotion",{})
 req(promo.get("pr")==1557 and promo.get("exact_head")=="27f3374356282dae8c8ffb1cb8c3bd110e1d2b38","36-03 promotion identity moved")
 req(promo.get("exact_head_ci_run")==33882496508 and promo.get("exact_head_ci_job")==101054258088,"36-03 promotion CI moved")
 req(promo.get("merged_main_sha")==PROMOTION_MERGE and promo.get("NEW_THEOREM_CREDIT") is False,"36-03 promotion provenance moved")
 print("PASS STAGE36_36_03_AUDITED_SUCCESSOR_REPLAY")
 print(f"hostile_audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}; exact_head_ci={AUDIT_CI_RUN}/{AUDIT_CI_JOB}")
 print(f"certificate_blob={AUDITED_CERT_BLOB}; successor_schema={schema}")
 print("no finite-twist/receiver/endpoint/perfect-cuboid credit")
if __name__=="__main__": main()
