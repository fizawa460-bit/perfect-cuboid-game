#!/usr/bin/env python3
"""Verify V91C1D candidate Stage33 MAIN startup under V91C1C user-authorized authority."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parents[1]; D=H/"33-12"; STATE=H/"MAIN-STATE.json"; V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
STATE_SHA="b71b48a78ee4b7eccee0a5063dfc8466e8b753d1cc89b1499ae6290f395fe5c4"; V1D_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
NEXT="V91C1E_COMPUTE_TYPE_SAFE_MARKED_BRAUER_IMAGE_OF_A2_02_FULL_SURFACE_CECH_CARTIER_SEED_AND_TEST_MASK20_WITHOUT_POSITIONAL_IDENTIFICATION"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b); return o
s=load(STATE,STATE_SHA); d=load(V1D,V1D_SHA)
assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V34_V91C1D_CANDIDATE_PENDING_HOSTILE_AUDIT"
assert s["authority_sync"]["frontier_authority"]=="V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT"
assert s["authority_sync"]["branch_candidate_frontier"]=="V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY"
g=s["candidate_audit_gate"]; assert g["pr"]==1634 and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False
assert s["continuation_provenance"]["user_authorized_merge"] is True and s["continuation_provenance"]["hostile_audit_pass_claimed"] is False
assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
assert d["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False and d["exact_consequence"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False
assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V97_V91C1D_CANDIDATE_STARTUP","state_sha256":STATE_SHA,"v91c1d_sha256":V1D_SHA,"authority":"V91C1C_USER_AUTHORIZED","candidate":"V91C1D_PENDING_HOSTILE_AUDIT","next_exact_leaf":NEXT},sort_keys=True))
