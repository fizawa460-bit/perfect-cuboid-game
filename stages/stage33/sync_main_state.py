#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at V91C1E adapter-preflight candidate."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"; V1E=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"
STATE_SHA="d5a9b2802558a9354c4501da6e86bef015aebee343b8791161b5bff0467295cb"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"; V1D_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"; V1E_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"
NEXT="V91C1F_MATERIALIZE_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_FROM_LITERAL_A2_02_CECH_SEED_TO_MARKED_PROPER14"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text()); cb=dict(ctl); q=cb.pop("projection_canonical_sha256"); assert q==CONTROLLER_SHA==csha(cb) and ctl["merge_allowed"] is False
 d,e=load(V1D,V1D_SHA),load(V1E,V1E_SHA); assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
 assert e["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False and e["type_safe_adapter_audit"]["full_surface_kummer_extension_class_missing"] is True and e["next_exact_leaf"]==NEXT
 s=load(OUT,STATE_SHA); assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V36_V91C1E_ADAPTER_PREFLIGHT_CANDIDATE_PENDING_HOSTILE_AUDIT"
 assert s["authority_sync"]["frontier_authority"]=="V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY" and s["authority_sync"]["branch_candidate_frontier"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT"
 g=s["candidate_audit_gate"]; assert g["pr"]==1639 and g["candidate_certificate_sha256"]==V1E_SHA and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False and g["merge_allowed"] is False and g["status"]=="PENDING_HOSTILE_AUDIT"
 p=s["audit_provenance"]; assert p["v91c1d_pr"]==1634 and p["hostile_audit_review"]==5123292911 and p["hostile_audit_verdict"]=="PASS" and p["merge_commit"]=="cf5389b857ee52225ed44543ff7ac8d05387583a"
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1E_CANDIDATE"
 assert s["current_exact_frontier"]["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False and s["current_exact_frontier"]["a2_02_marked_brauer_image_computed"] is False
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V99_V91C1E_ADAPTER_PREFLIGHT_CANDIDATE_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"candidate":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
