#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json"
CERT_BLOB="da9143e587506522ed966d380d9980ff1875db0d"
BASE="32d35dd4372ceab3d67704290d48f6b6df8912bb"
SCHEMA="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V16_36_09B_PENDING_HOSTILE_AUDIT"
LEGAL="BLOCKED_NO_PROOF_CAPABLE_B_PLUS_K_JOINT_TEST"
NEXT="36-09C_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_PREFLIGHT"
SOURCES={
 "stage36_roadmap":("stages/stage36/ROADMAP.md","eeedda0e89e24f851c989b5ec83e7b320e1ad99e"),
 "stage36_36_02_representatives":("stages/stage36/36-02/representative-inventory.json","88130b9380a677a191f91c24df87618e65be0a2f"),
 "stage36_36_03_physical_receiver":("stages/stage36/36-03/physical-open-boundary.json","fc1947b2de08f7d8a104bdc91902b20e88635349"),
 "stage36_36_04_torsor_class":("stages/stage36/36-04/h-torsor-lift-class.json","a06e201a9b554da71c5e75d8f8541e7284f8d020"),
 "stage36_36_05_ramification_block":("stages/stage36/36-05/uniform-ramification-support.json","193d0165b242d799bc981774783a5160c1ac58dc"),
 "stage36_36_09_breadth_gate":("stages/stage36/36-09/replacement-breadth-gate.json","0c6019d70346b531a9b703d6f74e346302273655"),
 "stage36_36_09A_camp4_preflight":("stages/stage36/36-09A/camp4-brauer-compatibility-preflight.json","66f31c03e5a978783a60b036322538f173a2f411"),
 "cycle_safety_protocol":("docs/research-os/policies/cycle-exploration-safety-protocol.md","4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37"),
}
ARSENAL={
 "router":("docs/arsenal/index.json","aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
 "S30-WF02":("docs/arsenal/cards/workflows/S30-WF02.md","38e4625155eb079bbe3d50d663c6256559319886"),
 "S30-WF03":("docs/arsenal/cards/workflows/S30-WF03.md","12740198aba19ade18302819f8e890dbda4eb701"),
 "S34-WF01":("docs/arsenal/cards/workflows/S34-WF01.md","1ebba4ec402e14d536284a06c5ac32625c6b8cec"),
 "S34-W03":("docs/arsenal/cards/formal/S34-W03.md","1d5275321f42768a6414d4610ac912c63be43f96"),
}
PROMO={"pr":1582,"exact_head":"2af6edb984e0c0a51e945f886939a09b442c3218","exact_head_ci_run":33951928420,"exact_head_ci_job":101268232176,"merged_main_sha":BASE,"scope":"mechanical audited-state promotion of 36-09A user-approved authority only; authorize unstarted 36-09B preflight","NEW_THEOREM_CREDIT":False}

def blob_sha(path:Path)->str:
 data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)

def main()->None:
 req(blob_sha(CERT)==CERT_BLOB,"36-09B certificate blob drift")
 c=json.loads(CERT.read_text())
 req(c.get("schema")=="STAGE36_36_09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT_V1","36-09B schema moved")
 req(c.get("status")=="BLOCKED_NO_PROOF_CAPABLE_B_PLUS_K_JOINT_TEST_PENDING_HOSTILE_AUDIT","36-09B status moved")
 req(c.get("base_main_sha")==BASE,"36-09B base moved")
 req(c.get("entry_authority")=={"stage36_36_09A_promotion_pr":1582,"promotion_exact_head":"2af6edb984e0c0a51e945f886939a09b442c3218","promotion_exact_head_ci_run":33951928420,"promotion_exact_head_ci_job":101268232176,"promotion_merged_main_sha":BASE,"selected_route":"36-09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT"},"36-09B entry authority moved")
 for key,(rel,sha) in SOURCES.items():
  req(c.get("source_locks",{}).get(key)=={"path":rel,"blob_sha":sha},f"36-09B source declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"36-09B source blob drift: {key}")
 for key,(rel,sha) in ARSENAL.items():
  row=c.get("arsenal_locks",{}).get(key,{})
  req(row.get("path")==rel and row.get("blob_sha")==sha,f"36-09B Arsenal declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"36-09B Arsenal blob drift: {key}")

 # S34-W03 requires an actual auxiliary branch B, receiver condition K, and exhaustive joint test.
 w03=(ROOT/ARSENAL["S34-W03"][0]).read_text()
 for text in [
  "an exact source/receiver contract showing every target point lies on `B` and also satisfies `K`",
  "an exact local or global test for the **joint** `B + K` system",
  "exhaustive treatment of the relevant projective residue classes or quotient points",
  "explicit classification of zero-factor/pole/infinity/degenerate points",
  "factor cover Q-pointset complete = not implied",
 ]: req(text in w03,f"S34-W03 required hypothesis/credit text moved: {text}")

 # Exact receiver and K exist.
 phys=json.loads((ROOT/SOURCES["stage36_36_03_physical_receiver"][0]).read_text())
 rr=phys.get("restricted_receiver_preparation",{})
 req(rr.get("S34_W03_prepared") is True,"36-03 S34-W03 preparation moved")
 req(rr.get("exact_restricted_open")=="U_H=q_H(U) for each audited representative","36-03 exact restricted receiver moved")
 req(rr.get("receiver_intersection_exclusion_executed") is False and rr.get("receiver_closed") is False,"36-03 prematurely claimed S34-W03 closure")
 t=json.loads((ROOT/SOURCES["stage36_36_04_torsor_class"][0]).read_text())
 pc=t.get("pointwise_class",{})
 req("all three G_ci(q) are rational squares" in pc.get("rational_lift_iff",""),"36-04 exact K/lift criterion moved")
 req(pc.get("physical_lift_scope")=="q_H^{-1}(U_H)=U, hence any rational lift stays in U","36-04 physical lift scope moved")
 deg=t.get("degenerate_cases",{})
 req(deg.get("coordinate_zero")=="excluded by U_H" and deg.get("noncoordinate_zero")=="covered by exact chart switch over all allowed strata","36-04 K boundary treatment moved")

 # But audited direct arithmetic wall forbids treating pointwise squareclasses as a finite branch list.
 ram=json.loads((ROOT/SOURCES["stage36_36_05_ramification_block"][0]).read_text())
 req(ram.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT","36-05 block moved")
 gap=ram.get("arithmetic_specialization_gap",{})
 req(gap.get("UNIFORM_Q_PRIME_SUPPORT_PROVED") is False,"36-05 uniform support unexpectedly proved")
 req(gap.get("primitive_receiver_gcd_resultant_support_theorem_available") is False,"36-05 valuation-support theorem unexpectedly available")
 req(ram.get("pass_condition",{}).get("FINITE_EXHAUSTIVE_H_TWIST_FAMILY") is False,"36-05 finite twist family unexpectedly available")

 # Breadth ledger already named the missing B; 36-09A made B4 live after blocking B5.
 breadth=json.loads((ROOT/SOURCES["stage36_36_09_breadth_gate"][0]).read_text())
 b4=next(x for x in breadth["cycle_audit"]["candidate_ledger"] if x["id"]=="B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION")
 req(b4.get("status")=="UNTESTED" and "no exhaustive auxiliary branch B" in b4.get("reason",""),"36-09 B4 original gap moved")
 a=json.loads((ROOT/SOURCES["stage36_36_09A_camp4_preflight"][0]).read_text())
 cyc_a=a.get("cycle_update",{})
 req(cyc_a.get("B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION")=="LIVE","36-09A B4 handoff moved")
 req((cyc_a.get("live_candidate_count"),cyc_a.get("untested_candidate_count"),cyc_a.get("blocked_candidate_count"),cyc_a.get("dominated_candidate_count"))==(1,5,3,1),"36-09A candidate counts moved")

 h=c.get("S34_W03_hypothesis_audit",{})
 req(h.get("EXACT_SOURCE_RECEIVER_CONTRACT") is True and h.get("EXACT_ADDITIONAL_RECEIVER_CONDITION_K") is True,"36-09B falsely lost receiver/K")
 for key in ["EXHAUSTIVE_AUXILIARY_BRANCH_B_SOURCE_LOCKED","B_IS_PROOF_CAPABLE_REDUCTION_RATHER_THAN_ORIGINAL_SURFACE_IN_DISGUISE","EXACT_JOINT_B_PLUS_K_LOCAL_OR_GLOBAL_TEST","EXHAUSTIVE_RELEVANT_PROJECTIVE_RESIDUES_OR_QUOTIENT_POINTS","ZERO_POLE_INFINITY_DEGENERATE_CLASSIFICATION_FOR_JOINT_SYSTEM","S34_W03_EXECUTABLE_NOW"]:
  req(h.get(key) is False,f"36-09B S34-W03 hypothesis overclaim: {key}")
 req(c.get("legal_outcome")==LEGAL,"36-09B legal outcome moved")
 why=c.get("why_pointwise_torsor_equations_do_not_complete_B4",{})
 req(why.get("pointwise_degree8_cover_available") is True and why.get("finite_chart_selection_available") is True,"36-09B pointwise cover facts moved")
 req(why.get("finite_exhaustive_arithmetic_twist_or_squareclass_family_available") is False and why.get("proof_capable_lower_dimensional_or_locally_closed_branch_family_available") is False,"36-09B branch-family credit leaked")

 cyc=c.get("cycle_update",{})
 req(cyc.get("route_status")=="BLOCKED_NO_NEW_INFORMATION","36-09B cycle status moved")
 req(cyc.get("B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION")==LEGAL,"36-09B B4 block moved")
 req(cyc.get("B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION")=="LIVE","36-09B next live candidate moved")
 req((cyc.get("live_candidate_count"),cyc.get("untested_candidate_count"),cyc.get("blocked_candidate_count"),cyc.get("dominated_candidate_count"))==(1,4,4,1),"36-09B cycle counts moved")
 req(cyc.get("split_triggered") is False and cyc.get("parking_audit_complete") is False,"36-09B split/parking moved")
 req(cyc.get("selected_next_route_after_hostile_audit")==NEXT,"36-09B successor moved")
 policy=(ROOT/SOURCES["cycle_safety_protocol"][0]).read_text()
 req("BLOCKED_NO_NEW_INFORMATION" in policy and "A `BLOCK` is not a command to stop the research cycle" in policy,"cycle block-routing policy moved")
 req("Do not park a receiver merely because the currently preferred route is blocked" in policy,"cycle parking policy moved")
 req(all(v is False for v in c.get("claims",{}).values()),"36-09B certificate leaked theorem/receiver credit")

 s=json.loads(STATE.read_text())
 req(s.get("schema")==SCHEMA and s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==BASE,"V16 lifecycle moved")
 req(s.get("stage36_36_09A_promotion")==PROMO,"36-09A promotion provenance moved")
 u=s.get("completed_units",{}).get("36-09B",{})
 req(u.get("certificate_blob_sha")==CERT_BLOB and u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","36-09B provisional authority moved")
 req(u.get("legal_outcome")==LEGAL and u.get("S34_W03_EXECUTABLE_NOW") is False,"36-09B state outcome moved")
 req(u.get("NEXT_ROUTE_AFTER_AUDIT")==NEXT,"36-09B state successor moved")
 cur=s.get("current",{})
 req(cur.get("unit")=="36-09B" and cur.get("36_09B_entry_allowed") is True and cur.get("36_09C_entry_allowed") is False,"36-09B/09C gate moved")
 req(cur.get("provisional_successor_after_hostile_audit")==NEXT,"36-09C provisional successor moved")
 req("36-09C" not in s.get("completed_units",{}),"36-09C started before 36-09B hostile audit")
 req(s.get("anti_loop",{}).get("do_not_start_36_09C_before_36_09B_hostile_audit") is True,"36-09C anti-loop moved")
 g=s.get("promotion_gates",{})
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
  req(g.get(key) is False,f"later Stage36 gate prematurely promoted: {key}")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT")
 print("exact receiver and K exist; S34-W03 not executable because proof-capable B and exhaustive joint B+K test are absent")
 print(f"legal_outcome={LEGAL}; cycle=B4 blocked, B2 LIVE; next_after_audit={NEXT}")
 print("no S34-W03 branch closure, quotient emptiness, replacement theorem, receiver, endpoint, or perfect-cuboid credit")
if __name__=="__main__": main()
