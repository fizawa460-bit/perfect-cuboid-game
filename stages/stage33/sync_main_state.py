#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at V91C1C candidate pending hostile audit."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; S07=H/"33-07"
OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V91C1A=D/"e3-v91c1a-a2-02-literal-boundary-seed-localization.json"; V91C1B=D/"e3-v91c1b-a2-02-resolved-valuation-carrier-preflight.json"; V91C1C=D/"e3-v91c1c-a2-02-strict-transform-prime-refinement.json"; GALOIS=S07/"galois-known-class-permutations.json"
STATE_SHA="1293cadb099b9e1935badc0572f3d98906e905df849dd653829ed0cddceca942"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
LOCKS={V91C1A:"7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403",V91C1B:"4398be760e937e1aba279af5fd099b029dc9998675503b5df7130e714ee81387",V91C1C:"ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6",GALOIS:"e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30"}
NEXT="V91C1D_MATERIALIZE_A2_02_PURITY_OFFBOUNDARY_CORRECTION_AND_PRIME_LEVEL_CECH_CARTIER_TRANSITION_DATA"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(path):
 o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256"); assert h==LOCKS[path]==csha(b),path; return o
def validate_sources():
 ctl=json.loads(CONTROLLER.read_text(encoding="utf-8")); b=dict(ctl); h=b.pop("projection_canonical_sha256"); assert h==CONTROLLER_SHA==csha(b); assert ctl["merge_allowed"] is False and ctl["execution"]["merge_allowed"] is False
 a,b1,c1,g=load(V91C1A),load(V91C1B),load(V91C1C),load(GALOIS)
 assert a["selection_semantics"]["selected_direction_is_claimed_e3_coefficient"] is False
 assert b1["next_exact_leaf"].startswith("V91C1C_REFINE_A2_02_") and b1["credit_firewall"]["merge_allowed"] is False
 assert c1["entry_authority"]["audited_authority"]=="V91C1A" and c1["entry_authority"]["v91c1b_hostile_audit_pass_claimed"] is False
 assert c1["exact_consequence"]["resolved_full_surface_height_one_attachment_for_a2_02_complete"] is True and c1["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
 assert c1["exact_consequence"]["purity_offboundary_correction_materialized"] is False and c1["next_exact_leaf"]==NEXT
 assert g["known_curve_count"]==92 and g["known_class_count"]==140
def validate_state(s):
 b=dict(s); h=b.pop("canonical_sha256"); assert h==STATE_SHA==csha(b)
 assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V32_V91C1C_CANDIDATE_PENDING_HOSTILE_AUDIT"
 a=s["authority_sync"]; assert a["frontier_authority"]=="V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED" and a["branch_candidate_frontier"]=="V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT"
 gate=s["candidate_audit_gate"]; assert gate["pr"]==1620 and gate["hostile_audit_verdict"]=="NOT_RUN" and gate["hostile_audit_review"] is None and gate["audit_pass_credit"] is False and gate["merge_allowed"] is False and gate["status"]=="PENDING_HOSTILE_AUDIT"
 f=s["current_exact_frontier"]
 for k in ("a2_02_resolved_exceptional_valuation_attachment_materialized","a2_02_strict_transform_carrier_prime_refinement_complete","a2_02_prime_level_cc_ct_transport_complete","a2_02_resolved_full_surface_height_one_attachment_complete"): assert f[k] is True
 for k in ("a2_02_purity_offboundary_correction_materialized","a2_02_full_surface_cech_transition_glue_materialized","a2_02_cartier_transition_binding_materialized","a2_02_claimed_e3_coefficient","a2_02_claimed_mask20_image","e3_marked_brauer_image_from_boundary_functions_materialized","e3_complete_residue_audit_materialized","e3_genuine_full_surface_h2_mu2_lift_materialized"): assert f[k] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1C_CANDIDATE"
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA
 assert s["discovery_policy"]["fixed_per_object_search_count_cap"] is None and s["discovery_policy"]["repeated_bounded_repository_search_allowed"] is True and s["discovery_policy"]["each_repeat_requires_materially_new_mathematical_signal"] is True and s["discovery_policy"]["unbounded_repository_search_allowed"] is False
 assert s["anti_loop_policy"]["do_not_treat_v91c1c_candidate_as_audited_authority_before_hostile_audit"] is True
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); args=ap.parse_args(); validate_sources(); s=json.loads(OUT.read_text(encoding="utf-8")); validate_state(s)
 if args.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
 if args.check or not args.write:
  assert OUT.stat().st_size<9800
  print(json.dumps({"success":True,"marker":"V95_V91C1C_CANDIDATE_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"audited_frontier":s["authority_sync"]["frontier_authority"],"candidate_frontier":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
