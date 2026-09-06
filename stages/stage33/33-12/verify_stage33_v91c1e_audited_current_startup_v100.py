#!/usr/bin/env python3
"""Verify V91C1E hostile-audited merged authority startup and V91C1F readiness."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"; STATE=H/"MAIN-STATE.json"; CERT=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"; V25=D/"j2-genuine-h2-mu2-kummer-adapter-v25.json"
STATE_SHA="77af1a7d8c42a2202f80ea447575916cae5a411d63789bc40988d5b89cbbabfc"; CERT_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; V25_SHA="d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"; NEXT="V91C1F_MATERIALIZE_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_FROM_LITERAL_A2_02_CECH_SEED_TO_MARKED_PROPER14"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b); return o
s,c,v25=load(STATE,STATE_SHA),load(CERT,CERT_SHA),load(V25,V25_SHA)
assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT" and s["branch_exact_frontier_authority"]==str(CERT.relative_to(H.parents[1]))
g=s["authority_audit_gate"]; assert g["pr"]==1639 and g["status"]=="HOSTILE_AUDITED_MERGED_AUTHORITY" and g["hostile_audit_review"]==5123392163 and g["exact_audited_head"]=="86eae9776d15479310ff6843d38614cb03498e21" and g["hostile_audit_verdict"]=="PASS" and g["audit_pass_credit"] is True and g["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887"
assert c["type_safe_adapter_audit"]["full_surface_kummer_extension_class_missing"] is True and c["type_safe_adapter_audit"]["literal_h2_seed_to_marked_proper14_quotient_map_materialized_by_locked_assets"] is False
assert v25["canonical_sha256"]==V25_SHA and v25["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True and v25["current_named_source"]["proper14_mask_decimal"]==25
f=s["current_exact_frontier"]; assert f["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True and f["a2_02_marked_brauer_image_computed"] is False and f["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False and f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
cont=s["continuation_provenance"]; assert cont["v91c1c_pr"]==1620 and cont["hostile_audit_pass_claimed"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is True and s["firewalls"]["merge_allowed"] is False and s["stage33_progress"]=="6/11"
print(json.dumps({"success":True,"marker":"V100_V91C1E_AUDITED_AUTHORITY_STARTUP","state_sha256":STATE_SHA,"certificate_sha256":CERT_SHA,"v25_sha256":V25_SHA,"next_exact_leaf":NEXT},sort_keys=True))
