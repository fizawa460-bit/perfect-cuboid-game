#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at V91C1E audited authority / V91C1F obstruction candidate."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1E=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"; V1F=D/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"; V25=D/"j2-genuine-h2-mu2-kummer-adapter-v25.json"
STATE_SHA="9eab75f049be7fffd40ed99d497f746fa28f1b6b100c00d730877d330d95c64b"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"; V1E_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; V1F_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"; V25_SHA="d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"
NEXT="V91C1G_CONSTRUCT_SOURCE_SPECIFIC_A2_02_BRAUER_IMAGE_WITNESS_OR_GEOMETRIC_QUOTIENT_ADAPTER_THEN_TEST_MASK20"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text()); cb=dict(ctl); q=cb.pop("projection_canonical_sha256"); assert q==CONTROLLER_SHA==csha(cb) and ctl["merge_allowed"] is False
 e,f,v25=load(V1E,V1E_SHA),load(V1F,V1F_SHA),load(V25,V25_SHA)
 assert e["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False
 assert f["construction_result"]["exact_obstruction_materialized"] is True and f["construction_result"]["source_bound_kummer_quotient_marking_materialized"] is False and f["next_exact_leaf"]==NEXT
 assert v25["current_named_source"]["proper14_mask_decimal"]==25 and v25["genuine_h2_mu2_adapter"]["named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate"] is True
 s=load(OUT,STATE_SHA); assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V38_V91C1F_TYPE_PROVENANCE_OBSTRUCTION_CANDIDATE_PENDING_HOSTILE_AUDIT"
 assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT" and s["authority_sync"]["branch_candidate_frontier"]=="V91C1F_A2_02_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_TYPE_PROVENANCE_OBSTRUCTION"
 a1=s["authority_audit_gate"]; assert a1["pr"]==1639 and a1["hostile_audit_review"]==5123392163 and a1["exact_audited_head"]=="86eae9776d15479310ff6843d38614cb03498e21" and a1["hostile_audit_verdict"]=="PASS" and a1["audit_pass_credit"] is True and a1["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887"
 g=s["candidate_audit_gate"]; assert g["pr"]==1646 and g["candidate_certificate_sha256"]==V1F_SHA and g["hostile_audit_review"] is None and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False and g["merge_allowed"] is False and g["status"]=="PENDING_HOSTILE_AUDIT"
 p=s["audit_provenance"]; assert p["v91c1e_pr"]==1639 and p["hostile_audit_review"]==5123392163 and p["hostile_audit_verdict"]=="PASS"
 old=p["prior_v91c1d"]; assert old["pr"]==1634 and old["hostile_audit_review"]==5123292911 and old["hostile_audit_verdict"]=="PASS"
 c=s["continuation_provenance"]; assert c["v91c1c_pr"]==1620 and c["user_authorized_merge"] is True and c["user_judged_mathematics_pass"] is True and c["hostile_audit_pass_claimed"] is False
 x=s["current_exact_frontier"]; assert x["v91c1f_type_provenance_obstruction_materialized"] is True and x["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False and x["a2_02_marked_brauer_image_computed"] is False and x["a2_02_claimed_mask20_image"] is False and x["a2_02_claimed_e3_coefficient"] is False and x["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1F_CANDIDATE"
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V101_V91C1E_AUDITED_V91C1F_OBSTRUCTION_CANDIDATE_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"candidate":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
