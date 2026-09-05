#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE_PATH=ROOT/"stages/stage36/MAIN-STATE.json"
SOURCES={"stage29_active_kernel_ledger":("stages/stage29/29-16/active-kernel-ledger.json","5d6d4c7709b57064aea5dc0ece672c5170c39550"),"stage29_endpoint_hub_graph":("stages/stage29/29-06/endpoint-hub-graph.json","7ea59474767f81fbaa4837c8cbc94b535560617b"),"stage29_campedelli_route_contract":("stages/stage29/29-02hb/route-contract.json","75045d8f15786836e8a7383fc07ef95161fa86e7"),"stage29_campedelli_arithmetic_routing":("stages/stage29/29-02hb/arithmetic-routing.md","ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),"stage29_campedelli_quotient_adapter":("stages/stage29/29-02hb/campedelli-quotient-adapter.md","5f959d60106243bb31df06a3961ab04182d78fc7"),"stage29_campedelli_source_lock":("stages/stage29/29-02hb/source-lock.md","713f22bb1347b8c6d5f8b32bfc2a24b3ce8b2e5d")}
FRONTIER={"ten_Q_defined_kernels":True,"H_group":"(Z/2)^3","canonical_quotient_degree":8,"resolved_etale_quotient_degree":8,"certified_Q_symmetry_orbit_sizes":[6,2,2],"geometric_Qi_orbit_sizes":[8,2],"exact_Q_isomorphism_class_count_proved":False,"execution_representative_count":3,"endpoint_to_every_audited_quotient_Q_point_push":True,"quotient_Q_point_implies_endpoint_Q_point":False,"H1_without_ramification_is_finite":False}
V12="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V12_36_09_BREADTH_GATE_PENDING_AUDIT"; V13="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V13_36_09_AUDITED"
BASE12="dc5898281a7ccea25d8ee0c1ae9953a18941ec08"; BASE13="05bc30f346e56ab5e13a54c6da6cab67f528fbaa"
AUTH36_09={"pr":1575,"hostile_audit_review":5118953320,"audited_head":"2f9562775aa386fdc547c0f4dcf87c81abae3663","merged_main_sha":BASE13,"exact_head_ci_run":33932204413,"exact_head_ci_job":101212944063,"certificate_blob_sha":"0c6019d70346b531a9b703d6f74e346302273655","selected_next_route":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT","verdict":"PASS"}
def blob_sha(p):
 d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()
def req(ok,msg):
 if not ok: raise SystemExit(msg)
def main():
 s=json.loads(STATE_PATH.read_text()); schema=s.get("schema"); req(schema in {V12,V13},"unrecognized Stage36 current schema"); req(s.get("stage")=="36","Stage36 number moved")
 k=s.get("source_kernel",{}); req(k.get("kernel")=="K16-C3-CAMPEDELLI-UNIFORM-TORSOR" and k.get("execution_class")==3 and k.get("children")==["R29-CAMP2"] and k.get("parent_routes")==["Q11-CAMPEDELLI"],"source kernel/route moved"); req(k.get("endpoint_decision_capable") is True,"endpoint capability moved")
 expected={key:{"path":rel,"blob_sha":sha} for key,(rel,sha) in SOURCES.items()}; req(s.get("source_locks")==expected,"source-lock set moved")
 for key,(rel,sha) in SOURCES.items(): req(blob_sha(ROOT/rel)==sha,f"source blob mismatch: {key}")
 req(s.get("audited_frontier")==FRONTIER,"imported Stage29 frontier moved")
 sibling=s.get("sibling_interfaces",{}).get("K16-C2-BRAUER-EXPLICIT-CHAIN",{}); req(sibling.get("receiver")=="R29-CAMP4" and sibling.get("relationship")=="SIBLING_ASSET_PROVIDER_ONLY" and sibling.get("automatic_authority_merge") is False and sibling.get("automatic_R29_CAMP2_closure") is False,"sibling interface/credit moved")
 # Immutable predecessor identities.
 req(s.get("stage36_36_02_authority",{}).get("hostile_audit_review")==5113379283 and s.get("stage36_36_02_authority",{}).get("exact_head_ci_run")==33876389406 and s.get("stage36_36_02_authority",{}).get("exact_head_ci_job")==101034265419,"36-02 authority moved")
 req(s.get("stage36_36_03_authority",{}).get("hostile_audit_review")==5113890803 and s.get("stage36_36_03_authority",{}).get("exact_head_ci_run")==33880359998 and s.get("stage36_36_03_authority",{}).get("exact_head_ci_job")==101047238497,"36-03 authority moved")
 req(s.get("stage36_36_04_authority",{}).get("hostile_audit_review")==5118098931 and s.get("stage36_36_04_authority",{}).get("final_exact_head_ci_run")==33923997348 and s.get("stage36_36_04_authority",{}).get("final_exact_head_ci_job")==101188362782,"36-04 authority moved")
 req(s.get("stage36_36_05_authority",{}).get("hostile_audit_review")==5118563918 and s.get("stage36_36_05_authority",{}).get("exact_head_ci_run")==33928640974 and s.get("stage36_36_05_authority",{}).get("exact_head_ci_job")==101202500740,"36-05 authority moved")
 g=s.get("promotion_gates",{}); req(g.get("source_authority_lock_complete") and g.get("three_Q_representatives_exact") and g.get("physical_open_push_and_boundary_complete") and g.get("pointwise_H_torsor_class_explicit"),"audited early gates lost")
 for key in ["uniform_finite_ramification_support_proved","finite_exhaustive_H_twist_family_proved","local_solubility_filter_exhaustive","all_global_survivors_closed","quotient_Q_point_emptiness_proved","receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]: req(g.get(key) is False,f"later gate prematurely promoted: {key}")
 if schema==V12:
  req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==BASE12,"V12 lifecycle moved"); u=s.get("completed_units",{}).get("36-09",{}); req(u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED" and s.get("current",{}).get("unit")=="36-09" and s.get("current",{}).get("36_09A_entry_allowed") is False,"V12 36-09 boundary moved")
 else:
  req(s.get("status")=="ACTIVE" and s.get("base_main_sha")==BASE13,"V13 lifecycle moved"); req(s.get("stage36_36_09_authority")==AUTH36_09,"36-09 authority block moved"); u=s.get("completed_units",{}).get("36-09",{}); req(u.get("promotion_status")=="AUDITED" and u.get("hostile_audit_review")==5118953320 and u.get("audited_head")==AUTH36_09["audited_head"] and u.get("exact_head_ci_run")==33932204413 and u.get("exact_head_ci_job")==101212944063 and u.get("merged_main_sha")==BASE13,"V13 36-09 provenance moved"); req(u.get("RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED") is False,"V13 replacement theorem credit leaked"); cur=s.get("current",{}); req(cur.get("unit")=="36-09A" and cur.get("36_06_entry_allowed") is False and cur.get("36_09A_entry_allowed") is True and "36-09A" not in s.get("completed_units",{}),"V13 successor boundary moved")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher credit is true")
 for rel in ["stages/stage36/ROADMAP.md","stages/stage36/MAIN-START-HERE.md","stages/stage36/MAIN-BATCH-HANDOFF.md"]: req((ROOT/rel).exists(),f"missing Stage36 file: {rel}")
 print("PASS STAGE36_BOOTSTRAP_AUTHORITY_SUCCESSOR_SAFE"); print(f"schema={schema}; source_blob_locks=6; Q symmetry 6+2+2; H=(Z/2)^3"); print("no route/theorem/endpoint/perfect-cuboid credit")
if __name__=="__main__": main()
