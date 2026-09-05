#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-04/h-torsor-lift-class.json"
CERT_BLOB="a06e201a9b554da71c5e75d8f8541e7284f8d020"
AUTH={"pr":1560,"hostile_audit_review":5118098931,"hostile_audited_head":"ce3eea151743b4ce031c84f09abd17221b7fe019","hostile_audit_ci_run":33921903342,"hostile_audit_ci_job":101181884820,"final_user_approved_head":"dcdae282120f29a42679b654e21bd35f843e4cbf","final_exact_head_ci_run":33923997348,"final_exact_head_ci_job":101188362782,"merged_main_sha":"de1df3d25c39306e5601646309b38aaad56967bd","certificate_blob_sha":CERT_BLOB,"verdict":"PASS_WITH_FRESHNESS_ONLY_FINAL_HEAD_USER_APPROVED"}
UNIT={"leaf":"36-04_EXPLICIT_H_TORSOR_AND_LIFT_CLASS","status":"AUDITED_PASS","certificate":"stages/stage36/36-04/h-torsor-lift-class.json","verifier":"stages/stage36/verify_stage36_36_04.py","successor_verifier":"stages/stage36/verify_stage36_36_04_audited.py","hostile_audit_review":5118098931,"hostile_audited_head":"ce3eea151743b4ce031c84f09abd17221b7fe019","hostile_audit_ci_run":33921903342,"hostile_audit_ci_job":101181884820,"final_user_approved_head":"dcdae282120f29a42679b654e21bd35f843e4cbf","final_exact_head_ci_run":33923997348,"final_exact_head_ci_job":101188362782,"merged_main_sha":"de1df3d25c39306e5601646309b38aaad56967bd","certificate_blob_sha":CERT_BLOB,"POINTWISE_H_TORSOR_CLASS_EXPLICIT":True,"FINITE_TWIST_FAMILY_PROVED":False,"NEW_THEOREM_CREDIT":False,"promotion_status":"AUDITED"}
PROMO={"pr":1568,"exact_head":"53b0c3b2a84ef200848d6b4b515c94589798d295","exact_head_ci_run":33924921726,"exact_head_ci_job":101191239139,"merged_main_sha":"dca962cdf37d4252316885dc57f3c0a591db4ecb","scope":"mechanical audited-state promotion only","NEW_THEOREM_CREDIT":False}
PROMO_36_05={"pr":1573,"exact_head":"741eb0ef6f07ef6551602c84a1b7493977023feb","exact_head_ci_run":33930463014,"exact_head_ci_job":101207828353,"merged_main_sha":"99c5f1634dd59d4bc5698cbb775801dd9d000827","scope":"mechanical audited-state promotion of blocked 36-05 authority only; route to unstarted 36-09","NEW_THEOREM_CREDIT":False}
AUTH_36_09={"pr":1575,"hostile_audit_review":5118953320,"audited_head":"2f9562775aa386fdc547c0f4dcf87c81abae3663","merged_main_sha":"05bc30f346e56ab5e13a54c6da6cab67f528fbaa","exact_head_ci_run":33932204413,"exact_head_ci_job":101212944063,"certificate_blob_sha":"0c6019d70346b531a9b703d6f74e346302273655","selected_next_route":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","verdict":"PASS"}
V9="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V9_36_04_AUDITED"; V10="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V10_36_05_PENDING_AUDIT"; V11="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V11_36_05_AUDITED_BLOCKED"; V12="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V12_36_09_BREADTH_GATE_PENDING_AUDIT"; V13="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V13_36_09_AUDITED"
BASE={V9:AUTH["merged_main_sha"],V10:"09d42186c06cd906042f2ca3f16a9deaf4f1b4a3",V11:"ee3e7aafd1742c5d96e2871f117412ef0823d57e",V12:"dc5898281a7ccea25d8ee0c1ae9953a18941ec08",V13:"05bc30f346e56ab5e13a54c6da6cab67f528fbaa"}
def blob_sha(path):
 data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(x,msg):
 if not x: raise SystemExit(msg)
def main():
 req(blob_sha(CERT)==CERT_BLOB,"36-04 audited certificate blob drift"); cert=json.loads(CERT.read_text())
 req(cert.get("schema")=="STAGE36_36_04_EXPLICIT_H_TORSOR_LIFT_CLASS_V1","36-04 cert schema moved"); req(cert.get("pass_condition")=={"POINTWISE_H_TORSOR_CLASS_EXPLICIT":True,"FINITE_TWIST_FAMILY_PROVED":False},"36-04 pass condition moved"); req(cert.get("pointwise_class",{}).get("degree")==8,"36-04 torsor degree moved"); req(all(v is False for v in cert.get("claims",{}).values()),"36-04 cert leaked higher credit")
 s=json.loads(STATE.read_text()); schema=s.get("schema"); req(schema in BASE,"36-04 audited successor schema moved"); req(s.get("base_main_sha")==BASE[schema],"36-04 successor base moved"); req(s.get("stage36_36_04_authority")==AUTH,"36-04 authority block moved"); req(s.get("completed_units",{}).get("36-04")==UNIT,"36-04 completed-unit provenance moved")
 g=s.get("promotion_gates",{}); [req(g.get(k) is True,f"audited predecessor gate lost: {k}") for k in ["source_authority_lock_complete","three_Q_representatives_exact","physical_open_push_and_boundary_complete","pointwise_H_torsor_class_explicit"]]
 [req(g.get(k) is False,f"later gate prematurely promoted: {k}") for k in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]]
 if schema in {V10,V11,V12,V13}: req(s.get("stage36_36_04_promotion")==PROMO,"36-04 promotion provenance moved")
 if schema in {V12,V13}: req(s.get("stage36_36_05_promotion")==PROMO_36_05,"36-05 promotion provenance moved")
 if schema==V13:
  req(s.get("status")=="ACTIVE" and s.get("stage36_36_09_authority")==AUTH_36_09,"V13 36-09 authority moved"); u=s.get("completed_units",{}).get("36-09",{}); req(u.get("promotion_status")=="AUDITED" and u.get("hostile_audit_review")==5118953320 and u.get("RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED") is False,"V13 36-09 audit promotion moved"); req(s.get("current",{}).get("unit")=="36-09A" and s.get("current",{}).get("36_09A_entry_allowed") is True and "36-09A" not in s.get("completed_units",{}),"V13 36-09A boundary moved")
 elif schema==V12: req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("current",{}).get("36_09A_entry_allowed") is False,"V12 36-09 boundary moved")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_04_AUDITED_SUCCESSOR_REPLAY"); print(f"certificate_blob={CERT_BLOB}; successor_schema={schema}"); print("pointwise H-torsor class exact; finite twist family remains false; no higher credit")
if __name__=="__main__": main()
