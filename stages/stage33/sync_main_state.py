#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at V91C1E hostile-audited authority / V91C1F ready."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"; V1E=D/"e3-v91c1e-a2-02-marked-brauer-image-adapter-preflight.json"; V25=D/"j2-genuine-h2-mu2-kummer-adapter-v25.json"
STATE_SHA="77af1a7d8c42a2202f80ea447575916cae5a411d63789bc40988d5b89cbbabfc"; CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"; V1D_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"; V1E_SHA="5dfbdf3dcd00f769d5550125cf7ca004ce4bf12aed5d3707cf9ddfc8dc292a4f"; V25_SHA="d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c"
NEXT="V91C1F_MATERIALIZE_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING_FROM_LITERAL_A2_02_CECH_SEED_TO_MARKED_PROPER14"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); q=b.pop("canonical_sha256"); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text()); cb=dict(ctl); q=cb.pop("projection_canonical_sha256"); assert q==CONTROLLER_SHA==csha(cb) and ctl["merge_allowed"] is False
 d,e,v25=load(V1D,V1D_SHA),load(V1E,V1E_SHA),load(V25,V25_SHA)
 assert d["exact_consequence"]["a2_02_full_surface_cech_cartier_seed_assembly_materialized"] is True
 assert e["exact_consequence"]["a2_02_marked_brauer_image_computed"] is False and e["type_safe_adapter_audit"]["full_surface_kummer_extension_class_missing"] is True and e["next_exact_leaf"]==NEXT
 assert v25["genuine_h2_mu2_adapter"]["full_surface_named_j2_h2_mu2_lift_materialized"] is True and v25["current_named_source"]["proper14_mask_decimal"]==25
 s=load(OUT,STATE_SHA); assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V37_V91C1E_HOSTILE_AUDITED_MERGED_AUTHORITY_V91C1F_READY"
 assert s["authority_sync"]["frontier_authority"]=="V91C1E_A2_02_MARKED_BRAUER_IMAGE_ADAPTER_PREFLIGHT" and s["authority_sync"]["branch_candidate_frontier"] is None
 g=s["authority_audit_gate"]; assert g["pr"]==1639 and g["authority_certificate_sha256"]==V1E_SHA and g["hostile_audit_review"]==5123392163 and g["exact_audited_head"]=="86eae9776d15479310ff6843d38614cb03498e21" and g["hostile_audit_verdict"]=="PASS" and g["audit_pass_credit"] is True and g["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887" and g["merged"] is True and g["merge_allowed"] is False
 p=s["audit_provenance"]; assert p["v91c1e_pr"]==1639 and p["hostile_audit_review"]==5123392163 and p["exact_audited_head"]=="86eae9776d15479310ff6843d38614cb03498e21" and p["hostile_audit_verdict"]=="PASS" and p["merge_commit"]=="dbcff26c0267416caa4fdd0515293396d0f86887"
 old=p["prior_v91c1d"]; assert old["pr"]==1634 and old["hostile_audit_review"]==5123292911 and old["hostile_audit_verdict"]=="PASS" and old["merge_commit"]=="cf5389b857ee52225ed44543ff7ac8d05387583a"
 c=s["continuation_provenance"]; assert c["v91c1c_pr"]==1620 and c["user_authorized_merge"] is True and c["user_judged_mathematics_pass"] is True and c["hostile_audit_pass_claimed"] is False
 f=s["current_exact_frontier"]; assert f["j2_adapted_columns_materialized"]==1 and f["j2_adapted_columns_total"]==10 and f["original_standard_columns_materialized"]==0
 assert f["literal_h2_seed_to_marked_proper14_quotient_map_materialized"] is False and f["a2_02_marked_brauer_image_computed"] is False and f["a2_02_claimed_mask20_image"] is False and f["a2_02_claimed_e3_coefficient"] is False and f["e3_genuine_full_surface_h2_mu2_lift_materialized"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is True and s["execution_gate"]["advance_scope"]=="V91C1F_SOURCE_BOUND_KUMMER_QUOTIENT_MARKING"
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V100_V91C1E_HOSTILE_AUDITED_MERGED_AUTHORITY_V91C1F_READY","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
