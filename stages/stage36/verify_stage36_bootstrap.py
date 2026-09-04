#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE_PATH=ROOT/"stages/stage36/MAIN-STATE.json"
INITIAL_BASE="c20ee71d91af850103fd7406f9b1072448a11fcf"
PENDING_36_01_BASE="5ed32fa53bdecb735f461d7c27e85851d9ad8c21"
AUDITED_36_01_MERGE="8c59c81bcf0bcd442705cfb7a3db297253b34679"
PENDING_36_02_BASE="a873c8fca0074aa966a22e36475a3551a378560d"
AUDITED_36_02_PR_MERGE="4c93ccb79e95cbcd9e2416ad3b6a3f4788d6f586"
AUDITED_36_02_PROMOTION_MERGE="26fb608cb2551ab2102ae36ad3b57c063959df58"
PENDING_36_03_BASE="bdd707e52ded061014bfbb6158762e8b997e7a38"
AUDITED_36_03_MERGE="45f290a443cf71b1fc62f031994122c3fa58f0e9"
AUDITED_36_03_PROMOTION_MERGE="efe25f4ef74dc776da7ccad3f5cd786b0b2906e4"
PENDING_36_04_BASE="4ec2b9af886f9ac9be13c3324788c26625c9e5d9"
AUDITED_36_04_MERGE="de1df3d25c39306e5601646309b38aaad56967bd"
PENDING_36_05_BASE="09d42186c06cd906042f2ca3f16a9deaf4f1b4a3"
AUDITED_36_05_MERGE="353d9057d1d5bd9b25a287672906a27c551dede9"
V11_BASE="ee3e7aafd1742c5d96e2871f117412ef0823d57e"
V12_BASE="99c5f1634dd59d4bc5698cbb775801dd9d000827"
FRESHNESS_36_04={"sync_pr":1565,"main_sha":PENDING_36_04_BASE,"merge_commit":"b900a925ce25556bf85c929b1c73aff414c77430","scope":"Stage32-only advance via #1563; no Stage36, Stage29 Campedelli/sign-cover source, or Arsenal authority changes"}
PROMO_36_04={"pr":1568,"exact_head":"53b0c3b2a84ef200848d6b4b515c94589798d295","exact_head_ci_run":33924921726,"exact_head_ci_job":101191239139,"merged_main_sha":"dca962cdf37d4252316885dc57f3c0a591db4ecb","scope":"mechanical audited-state promotion only","NEW_THEOREM_CREDIT":False}
PROMO_36_05={"pr":1573,"exact_head":"741eb0ef6f07ef6551602c84a1b7493977023feb","exact_head_ci_run":33930463014,"exact_head_ci_job":101207828353,"merged_main_sha":V12_BASE,"scope":"mechanical audited-state promotion of blocked 36-05 authority only; route to unstarted 36-09","NEW_THEOREM_CREDIT":False}
SOURCES={
"stage29_active_kernel_ledger":("stages/stage29/29-16/active-kernel-ledger.json","5d6d4c7709b57064aea5dc0ece672c5170c39550"),
"stage29_endpoint_hub_graph":("stages/stage29/29-06/endpoint-hub-graph.json","7ea59474767f81fbaa4837c8cbc94b535560617b"),
"stage29_campedelli_route_contract":("stages/stage29/29-02hb/route-contract.json","75045d8f15786836e8a7383fc07ef95161fa86e7"),
"stage29_campedelli_arithmetic_routing":("stages/stage29/29-02hb/arithmetic-routing.md","ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
"stage29_campedelli_quotient_adapter":("stages/stage29/29-02hb/campedelli-quotient-adapter.md","5f959d60106243bb31df06a3961ab04182d78fc7"),
"stage29_campedelli_source_lock":("stages/stage29/29-02hb/source-lock.md","713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d")}
FRONTIER={"ten_Q_defined_kernels":True,"H_group":"(Z/2)^3","canonical_quotient_degree":8,"resolved_etale_quotient_degree":8,"certified_Q_symmetry_orbit_sizes":[6,2,2],"geometric_Qi_orbit_sizes":[8,2],"exact_Q_isomorphism_class_count_proved":False,"execution_representative_count":3,"endpoint_to_every_audited_quotient_Q_point_push":True,"quotient_Q_point_implies_endpoint_Q_point":False,"H1_without_ramification_is_finite":False}
V1="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V1_INITIAL"; V2="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V2_36_01_PENDING_AUDIT"; V3="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V3_36_01_AUDITED"; V4="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V4_36_02_PENDING_AUDIT"; V5="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V5_36_02_AUDITED"; V6="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V6_36_03_PENDING_AUDIT"; V7="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V7_36_03_AUDITED"; V8="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V8_36_04_PENDING_AUDIT"; V9="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V9_36_04_AUDITED"; V10="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V10_36_05_PENDING_AUDIT"; V11="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V11_36_05_AUDITED_BLOCKED"; V12="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V12_36_09_BREADTH_GATE_PENDING_AUDIT"
def blob_sha(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)
def main():
 s=json.loads(STATE_PATH.read_text()); schema=s.get("schema")
 req(schema in {V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12},"unrecognized Stage36 successor schema")
 req(s.get("stage")=="36","Stage36 number moved")
 k=s.get("source_kernel",{}); req(k.get("kernel")=="K16-C3-CAMPEDELLI-UNIFORM-TORSOR" and k.get("execution_class")==3,"source kernel moved"); req(k.get("children")==["R29-CAMP2"] and k.get("parent_routes")==["Q11-CAMPEDELLI"],"source route moved"); req(k.get("endpoint_decision_capable") is True,"endpoint capability moved")
 expected={key:{"path":rel,"blob_sha":sha} for key,(rel,sha) in SOURCES.items()}; req(s.get("source_locks")==expected,"source-lock set moved")
 for key,(rel,sha) in SOURCES.items(): req(blob_sha(ROOT/rel)==sha,f"source blob mismatch: {key}")
 req(s.get("audited_frontier")==FRONTIER,"imported Stage29 frontier moved")
 sibling=s.get("sibling_interfaces",{}).get("K16-C2-BRAUER-EXPLICIT-CHAIN",{}); req(sibling.get("receiver")=="R29-CAMP4" and sibling.get("relationship")=="SIBLING_ASSET_PROVIDER_ONLY","sibling interface moved"); req(sibling.get("automatic_authority_merge") is False and sibling.get("automatic_R29_CAMP2_closure") is False,"sibling auto-credit enabled")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher credit is true")
 if schema==V1: req(s.get("status")=="PLANNED_NOT_STARTED" and s.get("base_main_sha")==INITIAL_BASE,"V1 lifecycle moved"); req(s.get("completed_units")=={},"36-01 started in V1"); return
 if schema==V2: req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==PENDING_36_01_BASE,"V2 lifecycle moved"); return
 u1=s.get("completed_units",{}).get("36-01",{}); req(u1.get("status")=="AUDITED_PASS" and u1.get("promotion_status")=="AUDITED","36-01 audited status moved"); req(u1.get("hostile_audit_review")==5112705173 and u1.get("audited_head")=="e2f6c5a2f34d76c1f17f90983a4e7fea62816621" and u1.get("merged_main_sha")==AUDITED_36_01_MERGE,"36-01 authority moved")
 g=s.get("promotion_gates",{}); req(g.get("source_authority_lock_complete") is True,"36-01 gate lost")
 if schema==V3: req(s.get("base_main_sha")==AUDITED_36_01_MERGE,"V3 base moved"); return
 if schema==V4: req(s.get("base_main_sha")==PENDING_36_02_BASE and g.get("three_Q_representatives_exact") is False,"V4 boundary moved"); return
 a2=s.get("stage36_36_02_authority",{}); req(a2.get("hostile_audit_review")==5113379283 and a2.get("audited_head")=="3a78f9ff156b53f509625d353df48d1b3e02b836" and a2.get("merged_main_sha")==AUDITED_36_02_PR_MERGE,"36-02 authority moved"); req(g.get("three_Q_representatives_exact") is True,"36-02 gate lost")
 if schema==V5: req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_36_02_PR_MERGE,"V5 lifecycle moved"); return
 p2=s.get("stage36_36_02_promotion",{}); req(p2.get("pr")==1548 and p2.get("merged_main_sha")==AUDITED_36_02_PROMOTION_MERGE and p2.get("NEW_THEOREM_CREDIT") is False,"36-02 promotion moved")
 if schema==V6: req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==PENDING_36_03_BASE,"V6 lifecycle moved"); return
 a3=s.get("stage36_36_03_authority",{}); req(a3.get("hostile_audit_review")==5113890803 and a3.get("audited_head")=="5fd7af75ede4cd2eceb70f9f21bd2b98ec5453a6" and a3.get("merged_main_sha")==AUDITED_36_03_MERGE,"36-03 authority moved"); req(g.get("physical_open_push_and_boundary_complete") is True,"36-03 gate lost")
 if schema==V7: req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_36_03_MERGE,"V7 lifecycle moved"); return
 p3=s.get("stage36_36_03_promotion",{}); req(p3.get("pr")==1557 and p3.get("exact_head")=="27f3374356282dae8c8ffb1cb8c3bd110e1d2b38","36-03 promotion identity moved"); req(p3.get("exact_head_ci_run")==33882496508 and p3.get("exact_head_ci_job")==101054258088 and p3.get("merged_main_sha")==AUDITED_36_03_PROMOTION_MERGE,"36-03 promotion CI/merge moved"); req(p3.get("NEW_THEOREM_CREDIT") is False,"36-03 promotion leaked theorem credit")
 if schema==V8: req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==PENDING_36_04_BASE,"V8 lifecycle moved"); req(s.get("freshness_sync_36_04")==FRESHNESS_36_04,"V8 freshness sync moved"); return
 req(g.get("pointwise_H_torsor_class_explicit") is True and s.get("completed_units",{}).get("36-04",{}).get("promotion_status")=="AUDITED","36-04 audited authority lost")
 if schema==V9: req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==AUDITED_36_04_MERGE,"V9 lifecycle moved"); return
 req(s.get("stage36_36_04_promotion")==PROMO_36_04,"36-04 promotion provenance moved")
 if schema==V10:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==PENDING_36_05_BASE,"V10 lifecycle moved")
  u5=s.get("completed_units",{}).get("36-05",{}); req(u5.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT" and u5.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","V10 blocked outcome moved")
  req(s.get("current",{}).get("unit")=="36-05" and s.get("current",{}).get("36_06_entry_allowed") is False,"V10 36-06 boundary moved"); return
 a5=s.get("stage36_36_05_authority",{}); req(a5.get("pr")==1569 and a5.get("hostile_audit_review")==5118563918 and a5.get("audited_head")=="cf430199171c98ed5f9eaaadeb8d2d40268ca6ba","36-05 authority moved")
 req(a5.get("merged_main_sha")==AUDITED_36_05_MERGE and a5.get("exact_head_ci_run")==33928640974 and a5.get("exact_head_ci_job")==101202500740,"36-05 merge/CI authority moved")
 req(a5.get("certificate_blob_sha")=="193d0165b242d799bc981774783a5160c1ac58dc" and a5.get("legal_outcome")=="BLOCKED_MOVING_RAMIFICATION_SUPPORT" and a5.get("verdict")=="PASS","36-05 authority semantics moved")
 u5=s.get("completed_units",{}).get("36-05",{}); req(u5.get("promotion_status")=="AUDITED" and u5.get("UNIFORM_FINITE_RAMIFICATION_SUPPORT_PROVED") is False and u5.get("FINITE_EXHAUSTIVE_H_TWIST_FAMILY") is False,"36-05 blocked audit promotion moved")
 if schema==V11:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==V11_BASE,"V11 lifecycle moved")
  req(s.get("current",{}).get("unit")=="36-09" and s.get("current",{}).get("36_06_entry_allowed") is False and s.get("current",{}).get("36_09_entry_allowed") is True,"V11 route moved")
  req("36-09" not in s.get("completed_units",{}),"36-09 started in V11"); return
 req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==V12_BASE,"V12 lifecycle moved")
 req(s.get("stage36_36_05_promotion")==PROMO_36_05,"36-05 promotion provenance moved in V12")
 u9=s.get("completed_units",{}).get("36-09",{}); req(u9.get("promotion_status")=="PROVISIONAL_NOT_AUDITED" and u9.get("SELECTED_NEXT_ROUTE")=="36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","V12 36-09 boundary moved")
 req(u9.get("RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED") is False,"V12 replacement theorem credit leaked")
 cur=s.get("current",{}); req(cur.get("unit")=="36-09" and cur.get("36_06_entry_allowed") is False and cur.get("36_09A_entry_allowed") is False,"V12 successor gate moved")
 req("36-09A" not in s.get("completed_units",{}),"36-09A started before hostile audit")
 for rel in ["stages/stage36/ROADMAP.md","stages/stage36/MAIN-START-HERE.md","stages/stage36/MAIN-BATCH-HANDOFF.md"]: req((ROOT/rel).exists(),f"missing Stage36 file: {rel}")
 print("PASS STAGE36_BOOTSTRAP_AUTHORITY_SUCCESSOR_SAFE"); print(f"schema={schema}; source_blob_locks=6; Q symmetry 6+2+2; H=(Z/2)^3"); print("no route/theorem/endpoint/perfect-cuboid credit")
if __name__=="__main__": main()
