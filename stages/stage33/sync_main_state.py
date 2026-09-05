#!/usr/bin/env python3
"""Generate/check Stage33 MAIN compact state at V91C1D candidate pending hostile audit."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1C=D/"e3-v91c1c-a2-02-strict-transform-prime-refinement.json"; V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
STATE_SHA="b71b48a78ee4b7eccee0a5063dfc8466e8b753d1cc89b1499ae6290f395fe5c4"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
LOCKS={V1C:"ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6",V1D:"fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"}
NEXT="V91C1E_COMPUTE_TYPE_SAFE_MARKED_BRAUER_IMAGE_OF_A2_02_FULL_SURFACE_CECH_CARTIER_SEED_AND_TEST_MASK20_WITHOUT_POSITIONAL_IDENTIFICATION"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256"); assert h==LOCKS[p]==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text(encoding="utf-8")); cb=dict(ctl); ch=cb.pop("projection_canonical_sha256"); assert ch==CONTROLLER_SHA==csha(cb); assert ctl["merge_allowed"] is False
 c,d=load(V1C),load(V1D); assert c["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
 e=d["exact_consequence"]
 for k in ("a2_02_codimension_one_and_resolution_exceptional_residue_audit_complete","a2_02_purity_offboundary_correction_materialized","a2_02_prime_level_cech_transition_data_materialized","a2_02_cartier_transition_binding_materialized","a2_02_full_surface_cech_cartier_seed_assembly_materialized"): assert e[k] is True
 for k in ("a2_02_marked_brauer_image_computed","a2_02_marked_brauer_image_equal_mask20","a2_02_claimed_e3_coefficient","genuine_full_surface_h2_mu2_lift_for_e3"): assert e[k] is False
 assert d["next_exact_leaf"]==NEXT and d["entry_authority"]["v91c1c_hostile_audit_pass_claimed"] is False
 s=json.loads(OUT.read_text(encoding="utf-8")); sb=dict(s); sh=sb.pop("canonical_sha256"); assert sh==STATE_SHA==csha(sb)
 assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V34_V91C1D_CANDIDATE_PENDING_HOSTILE_AUDIT"
 assert s["authority_sync"]["frontier_authority"]=="V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT"
 assert s["authority_sync"]["branch_candidate_frontier"]=="V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY"
 g=s["candidate_audit_gate"]; assert g["pr"]==1634 and g["status"]=="PENDING_HOSTILE_AUDIT" and g["hostile_audit_verdict"]=="NOT_RUN" and g["audit_pass_credit"] is False and g["merge_allowed"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is False and s["execution_gate"]["advance_scope"]=="HOSTILE_AUDIT_V91C1D_CANDIDATE"
 assert s["continuation_provenance"]["user_authorized_merge"] is True and s["continuation_provenance"]["hostile_audit_pass_claimed"] is False
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA
 assert OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V97_V91C1D_CANDIDATE_PENDING_HOSTILE_AUDIT","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"candidate":s["authority_sync"]["branch_candidate_frontier"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
