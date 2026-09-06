#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at V91C1F audited authority / V91C1G V4-naturality candidate."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1F=D/"e3-v91c1f-a2-02-source-bound-kummer-quotient-marking-obstruction.json"
V1G=D/"e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json"
BR=H/"33-07"/"proper-brauer2-from-discriminant.json"
STATE_SHA="e708fec595ab7008fe18316742f2af11911e15dbd9cdb521a15d10e5eacf72ef"
CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
V1F_SHA="4f6d18c35ce9cf8bb6efd2493ce66667bebf97870d731f06f17f76200932d273"
V1G_SHA="2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370"
BR_SHA="c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf"
NEXT="V91C1H_CONSTRUCT_SOURCE_BOUND_MARKED_BRAUER_FUNCTIONAL_OR_DIRECT_QUOTIENT_EVALUATION_FOR_A2_02_THEN_TEST_MASK20"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text()); cb=dict(ctl); q=cb.pop("projection_canonical_sha256"); assert q==CONTROLLER_SHA==csha(cb) and ctl["merge_allowed"] is False
 f,g,br=load(V1F,V1F_SHA),load(V1G,V1G_SHA),load(BR,BR_SHA); s=load(OUT,STATE_SHA)
 assert f["construction_result"]["exact_obstruction_materialized"] is True and f["construction_result"]["a2_02_marked_brauer_image_computed"] is False
 assert g["proper14_fixed_subspace_test"]["joint_v4_fixed_dimension_f2"]==10 and g["proper14_fixed_subspace_test"]["mask20_joint_v4_fixed"] is True
 assert g["proper14_fixed_subspace_test"]["v4_naturality_uniquely_identifies_mask20"] is False
 assert br["proper_Br2_joint_v4_fixed_dimension_f2"]==10
 assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V39_V91C1G_V4_NATURALITY_FIXED_SUBSPACE_CANDIDATE_PENDING_HOSTILE_AUDIT"
 assert s["authority_sync"]["frontier_authority"]=="V91C1F_A2_02_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_TYPE_PROVENANCE_OBSTRUCTION"
 assert s["authority_sync"]["branch_candidate_frontier"]=="V91C1G_A2_02_V4_NATURALITY_FIXED_SUBSPACE_PREFLIGHT"
 ag=s["authority_audit_gate"]; assert ag["pr"]==1646 and ag["hostile_audit_review"]==5123592182 and ag["exact_audited_head"]=="5471181a4decdc319cf3f00080d85da6d6e9fbb0" and ag["hostile_audit_verdict"]=="PASS" and ag["audit_pass_credit"] is True and ag["merge_commit"]=="749e06f82a3ffa1e9cb4e831760244e9237f34a4"
 cg=s["candidate_audit_gate"]; assert cg["pr"]==1649 and cg["candidate_certificate_sha256"]==V1G_SHA and cg["hostile_audit_review"] is None and cg["hostile_audit_verdict"]=="NOT_RUN" and cg["audit_pass_credit"] is False and cg["status"]=="PENDING_HOSTILE_AUDIT"
 cont=s["continuation_provenance"]; assert cont["v91c1c_pr"]==1620 and cont["hostile_audit_pass_claimed"] is False
 x=s["current_exact_frontier"]; assert x["a2_02_v4_naturality_constraint_materialized"] is True and x["a2_02_unknown_brauer_image_joint_v4_fixed_subspace_dimension_f2"]==10 and x["e3_mask20_joint_v4_fixed"] is True
 assert x["a2_02_marked_brauer_image_computed"] is False and x["a2_02_claimed_mask20_image"] is False and x["a2_02_claimed_e3_coefficient"] is False and x["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1G_CANDIDATE"
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V102_V91C1F_AUDITED_V91C1G_V4_NATURALITY_CANDIDATE_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"candidate":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
