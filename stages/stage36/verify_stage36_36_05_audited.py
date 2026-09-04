#!/usr/bin/env python3
from __future__ import annotations
import hashlib,itertools,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-05/uniform-ramification-support.json"
ROADMAP=ROOT/"stages/stage36/ROADMAP.md"
CERT_BLOB="193d0165b242d799bc981774783a5160c1ac58dc"
AUDITED_MERGE="353d9057d1d5bd9b25a287672906a27c551dede9"
CURRENT_BASE="ee3e7aafd1742c5d96e2871f117412ef0823d57e"
SCHEMA="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V11_36_05_AUDITED_BLOCKED"
AUTH={
 "pr":1569,
 "hostile_audit_review":5118563918,
 "audited_head":"cf430199171c98ed5f9eaaadeb8d2d40268ca6ba",
 "merged_main_sha":AUDITED_MERGE,
 "exact_head_ci_run":33928640974,
 "exact_head_ci_job":101202500740,
 "certificate_blob_sha":CERT_BLOB,
 "legal_outcome":"BLOCKED_MOVING_RAMIFICATION_SUPPORT",
 "verdict":"PASS",
}
LINES={
 "A1":(1,0,0),"A2":(0,1,0),"A3":(0,0,1),
 "B3":(1,1,0),"B2":(1,0,1),"B1":(0,1,1),"C":(1,1,1),
}

def blob_sha(path):
 data=path.read_bytes()
 return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)
def det(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def main():
 req(blob_sha(CERT)==CERT_BLOB,"36-05 audited certificate blob drift")
 cert=json.loads(CERT.read_text())
 req(cert.get("schema")=="STAGE36_36_05_UNIFORM_RAMIFICATION_SUPPORT_V1","36-05 audited certificate schema moved")
 req(cert.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT","36-05 audited legal outcome moved")
 req(cert.get("pass_condition")=={
   "UNIFORM_FINITE_RAMIFICATION_SUPPORT_PROVED":False,
   "FINITE_EXHAUSTIVE_H_TWIST_FAMILY":False,
   "ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM":False,
 },"36-05 audited pass-condition moved")
 geo=cert.get("fixed_geometric_support",{})
 nonzero_abs=sorted({abs(det(*(LINES[k] for k in comb))) for comb in itertools.combinations(LINES,3) if det(*(LINES[k] for k in comb))})
 req(nonzero_abs==[1,2] and geo.get("absolute_nonzero_triple_determinants")==[1,2],"36-05 determinant spectrum moved")
 req(geo.get("seven_line_arrangement_combinatorial_bad_prime_candidates")==[2],"36-05 combinatorial bad-prime candidate moved")
 req(geo.get("FULL_C_H_GOOD_REDUCTION_OUTSIDE_2_PROVED") is False,"36-05 full-quotient good reduction overclaimed")
 gap=cert.get("arithmetic_specialization_gap",{})
 for key in ["UNIFORM_Q_PRIME_SUPPORT_PROVED","numerator_denominator_support_controlled_uniformly","primitive_receiver_gcd_resultant_support_theorem_available","S_integrality_theorem_available","ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM","PHYSICAL_RECEIVER_POINT_FAMILY_EXHIBITED"]:
  req(gap.get(key) is False,f"36-05 arithmetic firewall moved: {key}")
 req(cert.get("arsenal_locks",{}).get("S34-W01",{}).get("triggered") is False,"S34-W01 falsely triggered")
 req(all(v is False for v in cert.get("claims",{}).values()),"36-05 certificate leaked higher credit")
 roadmap=ROADMAP.read_text()
 req("BLOCKED_MOVING_RAMIFICATION_SUPPORT" in roadmap and "36-09 — RECEIVER-MATCHED REPLACEMENT / BREADTH GATE" in roadmap,"36-05 blocked routing authority moved")

 s=json.loads(STATE.read_text())
 req(s.get("schema")==SCHEMA and s.get("status")=="ACTIVE","36-05 audited lifecycle moved")
 req(s.get("base_main_sha")==CURRENT_BASE,"36-05 audited current base moved")
 req(s.get("stage36_36_05_authority")==AUTH,"36-05 audited authority block moved")
 u=s.get("completed_units",{}).get("36-05",{})
 req(u.get("status")=="AUDITED_BLOCKED_MOVING_RAMIFICATION_SUPPORT","36-05 audited unit status moved")
 req(u.get("certificate_blob_sha")==CERT_BLOB,"36-05 audited unit blob moved")
 req(u.get("hostile_audit_review")==5118563918 and u.get("audited_head")==AUTH["audited_head"],"36-05 audit provenance moved")
 req(u.get("exact_head_ci_run")==33928640974 and u.get("exact_head_ci_job")==101202500740,"36-05 audit CI provenance moved")
 req(u.get("merged_main_sha")==AUDITED_MERGE and u.get("promotion_status")=="AUDITED","36-05 merge/promotion provenance moved")
 req(u.get("UNIFORM_FINITE_RAMIFICATION_SUPPORT_PROVED") is False and u.get("FINITE_EXHAUSTIVE_H_TWIST_FAMILY") is False,"36-05 false gates moved")
 req(u.get("ARBITRARY_PRIME_PHYSICAL_RECEIVER_POINT_CLAIM") is False and u.get("NEW_THEOREM_CREDIT") is False,"36-05 credit firewall moved")
 g=s.get("promotion_gates",{})
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
  req(g.get(key) is False,f"later gate prematurely promoted: {key}")
 cur=s.get("current",{})
 req(cur.get("unit")=="36-09" and cur.get("next_exact_leaf")=="36-09_RECEIVER_MATCHED_REPLACEMENT_BREADTH_GATE","36-09 routing moved")
 req(cur.get("36_06_entry_allowed") is False and cur.get("36_09_entry_allowed") is True,"36-05 blocked routing gate moved")
 req("36-06" not in s.get("completed_units",{}) and "36-09" not in s.get("completed_units",{}),"later leaf started during promotion")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_05_AUDITED_BLOCKED_SUCCESSOR_REPLAY")
 print(f"review={AUTH['hostile_audit_review']}; audited_head={AUTH['audited_head']}; exact_head_ci={AUTH['exact_head_ci_run']}/{AUTH['exact_head_ci_job']}")
 print(f"certificate_blob={CERT_BLOB}; audited_merge={AUDITED_MERGE}; current_base={CURRENT_BASE}")
 print("36-05 blocked audited; 36-06 forbidden; routed to unstarted 36-09; no higher credit")

if __name__=="__main__":
 main()
