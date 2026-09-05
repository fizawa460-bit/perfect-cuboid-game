#!/usr/bin/env python3
"""Verify Stage33 MAIN V91C1C candidate startup while audited authority remains V91C1A."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"
STATE=H/"MAIN-STATE.json"; CAND=D/"e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
STATE_SHA="1293cadb099b9e1935badc0572f3d98906e905df849dd653829ed0cddceca942"; CAND_SHA="ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6"
NEXT="V91C1D_MATERIALIZE_A2_02_PURITY_OFFBOUNDARY_CORRECTION_AND_PRIME_LEVEL_CECH_CARTIER_TRANSITION_DATA"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
s=load(STATE,STATE_SHA); c=load(CAND,CAND_SHA)
assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V32_V91C1C_CANDIDATE_PENDING_HOSTILE_AUDIT"
a=s["authority_sync"]; assert a["frontier_authority"]=="V91C1A_A2_02_LITERAL_BOUNDARY_PACKAGE_LOCALIZED" and a["branch_candidate_frontier"]=="V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT" and "PENDING_HOSTILE_AUDIT" in a["status"]
g=s["candidate_audit_gate"]; assert g["pr"]==1620 and g["candidate_certificate_sha256"]==CAND_SHA and g["hostile_audit_verdict"]=="NOT_RUN" and g["hostile_audit_review"] is None and g["audit_pass_credit"] is False and g["merge_allowed"] is False and g["status"]=="PENDING_HOSTILE_AUDIT"
assert s["branch_exact_frontier_authority"].endswith("e3-v91c1a-a2-02-literal-boundary-seed-localization.json") and s["branch_exact_frontier_candidate"].endswith("e3-v91c1c-a2-02-strict-transform-prime-refinement.json")
f=s["current_exact_frontier"]
for k in ("a2_02_resolved_exceptional_valuation_attachment_materialized","a2_02_strict_transform_carrier_prime_refinement_complete","a2_02_prime_level_cc_ct_transport_complete","a2_02_resolved_full_surface_height_one_attachment_complete"): assert f[k] is True
for k in ("a2_02_purity_offboundary_correction_materialized","a2_02_full_surface_cech_transition_glue_materialized","a2_02_cartier_transition_binding_materialized","a2_02_claimed_e3_coefficient","a2_02_claimed_mask20_image","e3_marked_brauer_image_from_boundary_functions_materialized","e3_complete_residue_audit_materialized","e3_genuine_full_surface_h2_mu2_lift_materialized"): assert f[k] is False
assert c["exact_consequence"]["resolved_full_surface_height_one_attachment_for_a2_02_complete"] is True and c["exact_consequence"]["purity_offboundary_correction_materialized"] is False
assert s["current"]["next_exact_leaf"]==NEXT==c["next_exact_leaf"] and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1C_CANDIDATE"
assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False
assert "stages/stage33/33-12/e3-v91c1c-a2-02-strict-transform-prime-refinement.json" in s["current_leaf_working_set"] and s["anti_loop_policy"]["do_not_treat_v91c1c_candidate_as_audited_authority_before_hostile_audit"] is True
print(json.dumps({"success":True,"marker":"V95_V91C1C_CANDIDATE_STARTUP_EXACT","state_sha256":STATE_SHA,"candidate_sha256":CAND_SHA,"audited_frontier":a["frontier_authority"],"candidate_frontier":a["branch_candidate_frontier"],"audit_status":g["status"],"next_exact_leaf":NEXT,"stage33_progress":"6/11"},sort_keys=True))
