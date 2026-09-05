#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CERT=ROOT/"stages/stage36/36-09A/camp4-brauer-compatibility-preflight.json"
CERT_BLOB="66f31c03e5a978783a60b036322538f173a2f411"
BASE="5fa33e600b81fc34f4be9b22761c8079b31d7806"
SCHEMA="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V14_36_09A_PENDING_HOSTILE_AUDIT"
PROMO_36_09={"pr":1578,"exact_head":"7adf76985ad8e56487292f42c7681d9cdf9d821c","exact_head_ci_run":33946402867,"exact_head_ci_job":101253172465,"merged_main_sha":BASE,"scope":"mechanical audited-state promotion of 36-09 breadth authority only; authorize unstarted 36-09A preflight","NEW_THEOREM_CREDIT":False}
SOURCES={
 "stage36_36_09_breadth_gate":("stages/stage36/36-09/replacement-breadth-gate.json","0c6019d70346b531a9b703d6f74e346302273655"),
 "stage36_36_03_physical_receiver":("stages/stage36/36-03/physical-open-boundary.json","fc1947b2de08f7d8a104bdc91902b20e88635349"),
 "stage29_active_kernel_ledger":("stages/stage29/29-16/active-kernel-ledger.json","5d6d4c7709b57064aea5dc0ece672c5170c39550"),
 "stage29_endpoint_hub_graph":("stages/stage29/29-06/endpoint-hub-graph.json","7ea59474767f81fbaa4837c8cbc94b535560617b"),
 "stage29_brauer_audit":("stages/stage29/29-02f/audit.md","b72f61749bcf0c2535135da11f882560c3a01cce"),
 "stage29_brauer_route_contract":("stages/stage29/29-02f/route-contract.json","3f4cb190a3a7f40776684b18ceb8096f3b48a6ad"),
 "stage29_boundary_gersten_receiver":("stages/stage29/29-02f/boundary-gersten-receiver.md","46f1e18fbd56addf28c0f957444d273ef3e86521"),
 "stage29_open_algebraic_brauer_adapter":("stages/stage29/29-02f/open-algebraic-brauer-adapter.md","2eccbf9bc6848262df7566a7f7eb436dd5b62681"),
 "stage29_campedelli_arithmetic_routing":("stages/stage29/29-02hb/arithmetic-routing.md","ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
 "stage29_campedelli_quotient_adapter":("stages/stage29/29-02hb/campedelli-quotient-adapter.md","5f959d60106243bb31df06a3961ab04182d78fc7"),
 "stage29_campedelli_route_contract":("stages/stage29/29-02hb/route-contract.json","75045d8f15786836e8a7383fc07ef95161fa86e7"),
}
ARSENAL={
 "router":("docs/arsenal/index.json","aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
 "S30-WF02":("docs/arsenal/cards/workflows/S30-WF02.md","38e4625155eb079bbe3d50d663c6256559319886"),
 "S30-WF03":("docs/arsenal/cards/workflows/S30-WF03.md","12740198aba19ade18302819f8e890dbda4eb701"),
 "S34-WF01":("docs/arsenal/cards/workflows/S34-WF01.md","1ebba4ec402e14d536284a06c5ac32625c6b8cec"),
 "S34-W03":("docs/arsenal/cards/formal/S34-W03.md","1d5275321f42768a6414d4610ac912c63be43f96"),
}

def blob_sha(path:Path)->str:
 data=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)

def main()->None:
 req(blob_sha(CERT)==CERT_BLOB,"36-09A certificate blob drift")
 c=json.loads(CERT.read_text())
 req(c.get("schema")=="STAGE36_36_09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT_V1","36-09A schema moved")
 req(c.get("status")=="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE_PENDING_HOSTILE_AUDIT","36-09A status moved")
 req(c.get("base_main_sha")==BASE,"36-09A base moved")
 entry=c.get("entry_authority",{})
 req(entry=={"stage36_36_09_promotion_pr":1578,"promotion_exact_head":"7adf76985ad8e56487292f42c7681d9cdf9d821c","promotion_exact_head_ci_run":33946402867,"promotion_exact_head_ci_job":101253172465,"promotion_merged_main_sha":BASE,"selected_route":"36-09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT"},"36-09A entry authority moved")
 for key,(rel,sha) in SOURCES.items():
  req(c.get("source_locks",{}).get(key)=={"path":rel,"blob_sha":sha},f"36-09A source declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"36-09A source blob drift: {key}")
 for key,(rel,sha) in ARSENAL.items():
  row=c.get("arsenal_locks",{}).get(key,{})
  req(row.get("path")==rel and row.get("blob_sha")==sha,f"36-09A Arsenal declaration moved: {key}")
  req(blob_sha(ROOT/rel)==sha,f"36-09A Arsenal blob drift: {key}")

 # Exact CAMP2 bridge exists; the preflight is not blocked on a Q-form/open map.
 qa=(ROOT/SOURCES["stage29_campedelli_quotient_adapter"][0]).read_text()
 req("C_H=S/H" in qa and "finite etale" in qa and "Q-defined" in qa,"CAMP2 quotient Q-form/open adapter moved")
 phys=json.loads((ROOT/SOURCES["stage36_36_03_physical_receiver"][0]).read_text())
 rr=phys.get("restricted_receiver_preparation",{})
 req(rr.get("exact_restricted_open")=="U_H=q_H(U) for each audited representative","CAMP2 restricted open moved")
 req(phys.get("scheme_vs_rational_firewall",{}).get("U_H_Q_equals_q_H_of_U_Q_claimed") is False,"CAMP2 lift firewall moved")
 bridge=c.get("exact_camp2_bridge_already_available",{})
 req(bridge.get("EXACT_Q_FORM_AND_OPEN_MORPHISM_AVAILABLE",True) is True,"internal bridge incorrectly blocked")
 req(bridge.get("LITERATURE_STANDARD_Q_MODEL_IDENTIFIED") is False and bridge.get("QUOTIENT_POINT_LIFTS_AUTOMATICALLY") is False,"Q-form/lift firewall moved")

 # Authoritative CAMP4 dependency order: BR2A/BR2B are prerequisites, not outputs already available.
 ledger=json.loads((ROOT/SOURCES["stage29_active_kernel_ledger"][0]).read_text())
 k=next(x for x in ledger["class2_kernels"] if x["kernel"]=="K16-C2-BRAUER-EXPLICIT-CHAIN")
 req("R29-CAMP4" in k["children"],"CAMP4 sibling receiver moved")
 req("R29-BR2A/R29-BR2B -> R29-CAMP4 when Campedelli pull-push compatibility is invoked" in k.get("internal_dependencies",[]),"CAMP4 dependency order moved")
 req(k.get("endpoint_decision_capable") is True,"CAMP4 kernel capability moved")
 route=json.loads((ROOT/SOURCES["stage29_brauer_route_contract"][0]).read_text())
 req(route.get("two_primary_brauer_closed") is False,"BR2A/two-primary unexpectedly closed")
 req(route.get("evaluation_maps_closed") is False,"BR2B evaluations unexpectedly closed")
 req(route.get("brauer_manin_obstruction_proved") is False,"Brauer-Manin credit unexpectedly present")
 req(route.get("receivers",{}).get("R29-BR2A")=="PhysicalOpenTwoPrimaryBrauerIntegralLattice","BR2A receiver moved")
 req(route.get("receivers",{}).get("R29-BR2B")=="PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints","BR2B receiver moved")
 audit=(ROOT/SOURCES["stage29_brauer_audit"][0]).read_text()
 req("No Brauer--Manin obstruction is claimed until local evaluation maps are computed" in audit,"Brauer evaluation firewall moved")
 gersten=(ROOT/SOURCES["stage29_boundary_gersten_receiver"][0]).read_text()
 req("Evaluation belongs to `R29-BR2B`" in gersten,"BR2B evaluation ownership moved")
 ar=(ROOT/SOURCES["stage29_campedelli_arithmetic_routing"][0]).read_text()
 req("nothing from the endpoint Brauer computation automatically pushes down or pulls back as a complete obstruction" in ar,"CAMP4 automatic-transfer firewall moved")
 req("R29-CAMP4=CampedelliBrauerAndTwoPrimaryDescentCompatibilityWith29_02f" in ar,"CAMP4 receiver definition moved")

 up=c.get("upstream_payload_audit",{})
 req(up.get("stage29_29_02f_tree_exhaustively_checked") is True and up.get("stage29_29_02f_tree_file_count")==13,"29-02f bounded tree audit moved")
 for key in ["BR2A_EXPLICIT_TWO_PRIMARY_CLASS_PACKET_CLOSED","BR2B_LOCAL_EVALUATION_MAPS_CLOSED","TWO_PRIMARY_BRAUER_CLOSED","OPEN_BOUNDARY_ODD_PRIMARY_CLOSED","BRAUER_MANIN_OBSTRUCTION_PROVED"]: req(up.get(key) is False,f"36-09A upstream credit leaked: {key}")
 req(up.get("REPO_WIDE_NONEXISTENCE_OF_ANY_FUTURE_ADAPTER_CLAIM") is False,"36-09A overclaimed repository-wide nonexistence")
 checks=c.get("compatibility_checks",{})
 req(checks.get("EXACT_Q_FORM_AND_OPEN_MORPHISM_AVAILABLE") is True,"exact quotient/open bridge lost")
 for key in ["EXPLICIT_ENDPOINT_BRAUER_CLASS_AVAILABLE_FOR_PULL_PUSH_TEST","EXPLICIT_LOCAL_EVALUATION_TABLE_AVAILABLE_FOR_PULL_PUSH_TEST","CERTIFIED_NONCONSTANT_CLASS_ON_U_DESCENDS_FROM_ANY_AUDITED_U_H","CERTIFIED_IDENTITY_ALPHA_U_EQUALS_qH_PULLBACK_ALPHA_H","CERTIFIED_LOCAL_EVALUATION_COMPATIBILITY_AT_ALL_REQUIRED_PLACES","CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED","CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED"]: req(checks.get(key) is False,f"36-09A compatibility overclaim: {key}")
 req(c.get("legal_outcome")=="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE","36-09A legal outcome moved")
 cyc=c.get("cycle_update",{})
 req(cyc.get("B5_CAMPEDELLI_BRAUER_ETALE_BRAUER")=="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE","B5 block moved")
 req(cyc.get("B4_RECEIVER_RESTRICTED_BRANCH_INTERSECTION")=="LIVE","B4 successor status moved")
 req((cyc.get("live_candidate_count"),cyc.get("untested_candidate_count"),cyc.get("blocked_candidate_count"),cyc.get("dominated_candidate_count"))==(1,5,3,1),"36-09A cycle counts moved")
 req(cyc.get("split_triggered") is False and cyc.get("parking_audit_complete") is False,"36-09A split/parking moved")
 req(cyc.get("selected_next_route_after_hostile_audit")=="36-09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT","36-09A successor route moved")
 req(c.get("arsenal_locks",{}).get("S34-W03",{}).get("application")=="SELECTED_AS_NEXT_PREFLIGHT_ONLY_NOT_EXECUTED","S34-W03 prematurely executed")
 wf03=(ROOT/ARSENAL["S30-WF03"][0]).read_text(); req("adapter completion => receiver closure without receiver contract" in wf03,"S30-WF03 credit firewall moved")
 w03=(ROOT/ARSENAL["S34-W03"][0]).read_text(); req("RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION" in w03 and "factor cover Q-pointset complete = not implied" in w03,"S34-W03 scope moved")
 req(all(v is False for v in c.get("claims",{}).values()),"36-09A certificate leaked higher credit")

 s=json.loads(STATE.read_text())
 req(s.get("schema")==SCHEMA and s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT" and s.get("base_main_sha")==BASE,"V14 lifecycle moved")
 req(s.get("stage36_36_09_promotion")==PROMO_36_09,"36-09 promotion provenance moved")
 unit=s.get("completed_units",{}).get("36-09A",{})
 req(unit.get("certificate_blob_sha")==CERT_BLOB and unit.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","36-09A provisional authority moved")
 req(unit.get("legal_outcome")=="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE","36-09A state outcome moved")
 req(unit.get("CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED") is False and unit.get("CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED") is False,"36-09A state compatibility credit leaked")
 cur=s.get("current",{})
 req(cur.get("unit")=="36-09A" and cur.get("36_09A_entry_allowed") is True,"36-09A current unit moved")
 req(cur.get("36_09B_entry_allowed") is False and cur.get("provisional_successor_after_hostile_audit")=="36-09B_RECEIVER_RESTRICTED_BRANCH_INTERSECTION_PREFLIGHT","36-09B hostile-audit boundary moved")
 req("36-09B" not in s.get("completed_units",{}),"36-09B started before 36-09A hostile audit")
 g=s.get("promotion_gates",{})
 for key in ["receiver_matched_replacement_theorem_proved","R29_CAMP2_closed","Q11_CAMPEDELLI_closed","endpoint_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]: req(g.get(key) is False,f"higher Stage36 gate leaked: {key}")
 req(all(v is False for v in s.get("claims",{}).values()),"Stage36 higher claim leaked")
 print("PASS STAGE36_36_09A_CAMP4_BRAUER_COMPATIBILITY_PREFLIGHT")
 print("CAMP2 Q-form/open bridge exact; CAMP4 compatibility not testable from retained authority because BR2A/BR2B remain open")
 print("legal_outcome=BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE; neither compatibility nor incompatibility claimed")
 print("next_after_audit=36-09B S34-W03 receiver-restricted intersection preflight; no Brauer/receiver/endpoint credit")
if __name__=="__main__": main()
