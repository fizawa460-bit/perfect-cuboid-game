#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-09/replacement-breadth-gate.json"
CERT_BLOB="0c6019d70346b531a9b703d6f74e346302273655"
AUDIT_REVIEW=5118953320
AUDITED_HEAD="2f9562775aa386fdc547c0f4dcf87c81abae3663"
AUDIT_CI_RUN=33932204413
AUDIT_CI_JOB=101212944063
AUDITED_MERGE="05bc30f346e56ab5e13a54c6da6cab67f528fbaa"
V13="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V13_36_09_AUDITED"
AUTH={"pr":1575,"hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"merged_main_sha":AUDITED_MERGE,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"certificate_blob_sha":CERT_BLOB,"selected_next_route":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","verdict":"PASS"}
UNIT={"leaf":"36-09_RECEIVER_MATCHED_REPLACEMENT_BREADTH_GATE","status":"AUDITED_BREADTH_GATE_SELECTS_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","certificate":"stages/stage36/36-09/replacement-breadth-gate.json","certificate_blob_sha":CERT_BLOB,"verifier":"stages/stage36/verify_stage36_36_09.py","successor_verifier":"stages/stage36/verify_stage36_36_09_audited.py","EXHAUSTIVE_VIEW_AUDIT":True,"BLIND_REDISCOVERY":True,"CANDIDATE_LEDGER_CLASSIFIED":True,"SELECTED_NEXT_ROUTE":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED":False,"NEW_THEOREM_CREDIT":False,"promotion_status":"AUDITED","hostile_audit_review":AUDIT_REVIEW,"audited_head":AUDITED_HEAD,"exact_head_ci_run":AUDIT_CI_RUN,"exact_head_ci_job":AUDIT_CI_JOB,"merged_main_sha":AUDITED_MERGE}

def blob_sha(path:Path)->str:
 data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)

def main()->None:
 req(blob_sha(CERT)==CERT_BLOB,"36-09 audited certificate blob drift")
 cert=json.loads(CERT.read_text())
 req(cert.get("schema")=="STAGE36_36_09_RECEIVER_MATCHED_REPLACEMENT_BREADTH_GATE_V1","36-09 certificate schema moved")
 req(cert.get("pass_condition")=={"RECEIVER_QUANTIFIERS_FROZEN":True,"EXHAUSTIVE_VIEW_AUDIT":True,"BLIND_REDISCOVERY":True,"CANDIDATE_LEDGER_CLASSIFIED":True,"ONE_ACTIVE_ROUTE_SELECTED":True,"SELECTED_NEXT_ROUTE":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED":False},"36-09 pass condition moved")
 ca=cert.get("cycle_audit",{})
 req(ca.get("EXHAUSTIVE_VIEW_AUDIT") is True and ca.get("BLIND_REDISCOVERY") is True,"36-09 breadth audit flags moved")
 req((ca.get("live_candidate_count"),ca.get("untested_candidate_count"),ca.get("blocked_candidate_count"),ca.get("dominated_candidate_count"))==(1,6,2,1),"36-09 candidate ledger counts moved")
 req(ca.get("split_triggered") is False and ca.get("parking_audit_complete") is False,"36-09 split/parking status moved")
 sel=cert.get("selected_next_route",{})
 req(sel.get("id")=="36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT" and sel.get("executes_brauer_computation_now") is False,"36-09 selected route moved or prematurely executed")
 req(sel.get("replacement_theorem_proved") is False and sel.get("receiver_closed") is False,"36-09 replacement/receiver credit leaked")
 req(all(v is False for v in cert.get("claims",{}).values()),"36-09 certificate higher credit leaked")

 s=json.loads(STATE.read_text())
 req(s.get("schema")==V13 and s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_MERGE,"V13 lifecycle moved")
 req(s.get("stage36_36_09_authority")==AUTH,"36-09 authority block moved")
 req(s.get("completed_units",{}).get("36-09")==UNIT,"36-09 completed-unit provenance moved")
 cur=s.get("current",{})
 req(cur.get("unit")=="36-09A" and cur.get("next_exact_leaf")=="36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","36-09A successor moved")
 req(cur.get("36_06_entry_allowed") is False and cur.get("36_09_entry_allowed") is False and cur.get("36_09A_entry_allowed") is True,"36-09A entry gate moved")
 req("36-09A" not in s.get("completed_units",{}),"36-09A executed inside mechanical promotion")
 g=s.get("promotion_gates",{})
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
  req(g.get(key) is False,f"later gate prematurely promoted: {key}")
 sib=s.get("sibling_interfaces",{}).get("K16-C2-BRAUER-EXPLICIT-CHAIN",{})
 req(sib.get("relationship")=="SIBLING_ASSET_PROVIDER_ONLY" and sib.get("automatic_authority_merge") is False and sib.get("automatic_R29_CAMP2_closure") is False,"CAMP4 sibling firewall moved")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_09_AUDITED_SUCCESSOR_REPLAY")
 print(f"review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}; exact_head_ci={AUDIT_CI_RUN}/{AUDIT_CI_JOB}")
 print(f"certificate_blob={CERT_BLOB}; audited_merge={AUDITED_MERGE}")
 print("36-09A preflight authorized but unstarted; no Brauer/replacement/receiver/endpoint credit")
if __name__=="__main__": main()
