#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at audited V91C1E + V91C1F-S1 candidate."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1E=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"; F1=D/"e3-v91c1f-s1-a2-02-source-bound-kummer-quotient-marking-contract.json"
STATE_SHA="c105bed2d0dc24822eac019463a82f3baad42bdbd4cf7cef6e806296c3bbf949"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"; V1E_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; F1_SHA="3f9bee9108bbf93b304c6d0fdae4235717c3fe919647c882fcc4ef5e822d3c93"
NEXT="V91C1F_S2_COMPUTE_SOURCE_BOUND_MARKED_BRAUER_QUOTIENT_EVALUATION_OF_LITERAL_A2_02_CECH_CARTIER_SEED_THEN_TEST_PROPER14_MASK20"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text()); cb=dict(ctl); q=cb.pop("projection_canonical_sha256"); assert q==CONTROLLER_SHA==csha(cb) and ctl["merge_allowed"] is False
 e,f1=load(V1E,V1E_SHA),load(F1,F1_SHA); assert e["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
 assert f1["exact_consequence"]["v25_success_condition_reduced_to_source_coordinate_identity_witness"] is True and f1["required_source_bound_marking_witness"]["materialized"] is False and f1["next_exact_leaf"]==NEXT
 s=load(OUT,STATE_SHA); assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V37_V91C1E_AUDITED_V91C1F_S1_SOURCE_MARKING_CONTRACT_CANDIDATE"
 assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT" and s["authority_sync"]["branch_candidate_frontier"]=="V91C1F_S1_A2_02_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_CONTRACT"
 p=s["audit_provenance"]; assert p["v91c1e_pr"]==1639 and p["hostile_audit_review"]==5123392163 and p["exact_audited_head"]=="86eae9776d15479310ff6843d38614cb03498e21" and p["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887"
 g=s["candidate_audit_gate"]; assert g["pr"]==1645 and g["candidate_certificate_sha256"]==F1_SHA and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False and g["merge_allowed"] is False
 x=s["current_exact_frontier"]; assert x["j2_adapted_columns_materialized"]==1 and x["j2_adapted_columns_total"]==10 and x["original_standard_columns_materialized"]==0
 assert x["v91c1f_s1_source_coordinate_identity_contract_materialized"] is True and x["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False and x["a2_02_marked_brauer_image_computed"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1F_S1_CANDIDATE"
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V100_V91C1E_AUDITED_V91C1F_S1_CANDIDATE","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"candidate":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
