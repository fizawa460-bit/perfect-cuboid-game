#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-09A/camp4-brauer-compatibility-preflight.json"
CERT_BLOB="66f31c03e5a978783a60b036322538f173a2f411"
SCHEMA="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V15_36_09A_AUDITED_USER_APPROVED"
BASE="05c229420a7c73886fedbece2d746b36ed3d91d5"
FINAL_HEAD="bc94e9c7aa8be2cd1c14dec63d001282cb6bb781"
FINAL_CI_RUN=33950158090
FINAL_CI_JOB=101263286962
FAIL_REVIEW_1=5120057949
REAUDIT_REQUEST=5120188273
FINAL_FAIL_REVIEW=5120235515
PREMERGE_UNRELATED_MAIN="3d63864b0a10a53549f64a9e0dc3acf6f59ef9c0"
MERGE=BASE
LEGAL="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE"

AUTH={
 "pr":1580,
 "hostile_audit_request_review":5119927945,
 "freshness_fail_review_1":FAIL_REVIEW_1,
 "hostile_reaudit_request_review":REAUDIT_REQUEST,
 "final_freshness_only_fail_review":FINAL_FAIL_REVIEW,
 "final_user_approved_head":FINAL_HEAD,
 "final_exact_head_ci_run":FINAL_CI_RUN,
 "final_exact_head_ci_job":FINAL_CI_JOB,
 "certificate_blob_sha":CERT_BLOB,
 "legal_outcome":LEGAL,
 "premerge_unrelated_main_sha":PREMERGE_UNRELATED_MAIN,
 "merged_main_sha":MERGE,
 "verdict":"USER_APPROVED_PASS_AFTER_FRESHNESS_ONLY_FAIL"
}
UNIT={
 "leaf":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT",
 "status":"AUDITED_BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE_USER_APPROVED",
 "certificate":"stages/stage36/36-09A/camp4-brauer-compatibility-preflight.json",
 "certificate_blob_sha":CERT_BLOB,
 "verifier":"stages/stage36/verify_stage36_36_09A.py",
 "successor_verifier":"stages/stage36/verify_stage36_36_09A_audited.py",
 "legal_outcome":LEGAL,
 "CAMP2_QFORM_OPEN_BRIDGE_EXACT":True,
 "CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED":False,
 "CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED":False,
 "NEXT_ROUTE_AFTER_AUDIT":"36-09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT",
 "NEW_THEOREM_CREDIT":False,
 "promotion_status":"AUDITED",
 "hostile_audit_request_review":5119927945,
 "freshness_fail_review_1":FAIL_REVIEW_1,
 "hostile_reaudit_request_review":REAUDIT_REQUEST,
 "final_freshness_only_fail_review":FINAL_FAIL_REVIEW,
 "final_user_approved_head":FINAL_HEAD,
 "final_exact_head_ci_run":FINAL_CI_RUN,
 "final_exact_head_ci_job":FINAL_CI_JOB,
 "merged_main_sha":MERGE,
 "verdict":"USER_APPROVED_PASS_AFTER_FRESHNESS_ONLY_FAIL"
}

def blob_sha(path:Path)->str:
 data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)
def git(*args:str)->str:
 return subprocess.check_output(["git",*args],cwd=ROOT,text=True).strip()

def main()->None:
 req(blob_sha(CERT)==CERT_BLOB,"36-09A audited certificate blob drift")
 c=json.loads(CERT.read_text())
 req(c.get("schema")=="STAGE36_36_09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT_V1","36-09A certificate schema moved")
 req(c.get("legal_outcome")==LEGAL,"36-09A legal outcome moved")
 checks=c.get("compatibility_checks",{})
 req(checks.get("EXACT_Q_FORM_AND_OPEN_MORPHISM_AVAILABLE") is True,"36-09A exact quotient/open bridge lost")
 req(checks.get("CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED") is False,"36-09A compatibility credit leaked")
 req(checks.get("CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED") is False,"36-09A incompatibility credit leaked")
 req(all(v is False for v in c.get("claims",{}).values()),"36-09A certificate higher credit leaked")

 s=json.loads(STATE.read_text())
 req(s.get("schema")==SCHEMA,"36-09A audited successor schema moved")
 req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==BASE,"36-09A audited lifecycle/base moved")
 req(s.get("stage36_36_09A_authority")==AUTH,"36-09A user-approved authority block moved")
 req(s.get("completed_units",{}).get("36-09A")==UNIT,"36-09A completed-unit authority moved")
 # The final hostile result was freshness-only FAIL. Do not rewrite it into a hostile PASS.
 req("hostile_audit_review" not in AUTH,"36-09A falsely recorded a hostile PASS review")
 req(AUTH["verdict"]=="USER_APPROVED_PASS_AFTER_FRESHNESS_ONLY_FAIL","36-09A user-approved verdict moved")

 # Merge ancestry must retain both the unrelated latest main and the exact user-approved Stage36 head.
 req(git("merge-base","--is-ancestor",PREMERGE_UNRELATED_MAIN,MERGE)=="","unreachable") if False else None
 subprocess.check_call(["git","merge-base","--is-ancestor",PREMERGE_UNRELATED_MAIN,MERGE],cwd=ROOT)
 subprocess.check_call(["git","merge-base","--is-ancestor",FINAL_HEAD,MERGE],cwd=ROOT)

 cur=s.get("current",{})
 req(cur.get("unit")=="36-09B" and cur.get("next_exact_leaf")=="36-09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT","36-09B successor routing moved")
 req(cur.get("36_06_entry_allowed") is False and cur.get("36_09A_entry_allowed") is False and cur.get("36_09B_entry_allowed") is True,"36-09B entry boundary moved")
 req("36-09B" not in s.get("completed_units",{}),"36-09B executed inside 36-09A mechanical promotion")
 anti=s.get("anti_loop",{})
 req(anti.get("do_not_start_36_09B_before_36_09A_authority_resolution") is True,"36-09B authority-resolution anti-loop moved")
 g=s.get("promotion_gates",{})
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
  req(g.get(key) is False,f"later gate prematurely promoted: {key}")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_09A_AUDITED_USER_APPROVED_SUCCESSOR_REPLAY")
 print(f"final_head={FINAL_HEAD}; exact_head_ci={FINAL_CI_RUN}/{FINAL_CI_JOB}; merge={MERGE}")
 print(f"final_hostile_review={FINAL_FAIL_REVIEW} freshness-only FAIL; authority=USER_APPROVED_PASS")
 print(f"certificate_blob={CERT_BLOB}; next=36-09B unstarted; no compatibility/Brauer/receiver/endpoint credit")
if __name__=="__main__": main()
