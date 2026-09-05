#!/usr/bin/env python3
"""Verify V91C1E adapter-preflight candidate startup."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"; STATE=H/"MAIN-STATE.json"; CERT=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"
STATE_SHA="d5a9b2802558a9354c4501da6e86bef015aebee343b8791161b5bff0467295cb"; CERT_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; NEXT="V91C1F_MATERIALIZE_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_FROM_LITERAL_A2_02_CECH_SEED_TO_MARKED_PROPER14"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b); return o
s,c=load(STATE,STATE_SHA),load(CERT,CERT_SHA)
assert s["authority_sync"]["frontier_authority"]=="V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY" and s["authority_sync"]["branch_candidate_frontier"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT"
g=s["candidate_audit_gate"]; assert g["pr"]==1639 and g["status"]=="PENDING_HOSTILE_AUDIT" and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False
assert c["type_safe_adapter_audit"]["full_surface_kummer_extension_class_missing"] is True and c["type_safe_adapter_audit"]["literal_h2_seed_to_marked_proper14_quotient_map_materialized_by_locked_assets"] is False
assert c["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False and c["exact_consequence"]["repository_wide_absence_claim"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["firewalls"]["merge_allowed"] is False and s["stage33_progress"]=="6/11"
print(json.dumps({"success":True,"marker":"V99_V91C1E_ADAPTER_PREFLIGHT_CANDIDATE_STARTUP","state_sha256":STATE_SHA,"certificate_sha256":CERT_SHA,"next_exact_leaf":NEXT},sort_keys=True))
