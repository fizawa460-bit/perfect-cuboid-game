#!/usr/bin/env python3
"""Check Stage33 MAIN compact state at hostile-audited/merged V91C1D authority."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/"33-12"; OUT=H/"MAIN-STATE.json"; CONTROLLER=H/"controller.json"
V1D=D/"e3-v91c1d-a2-02-purity-cech-cartier-assembly.json"
STATE_SHA="07805326657173a91204aedc680469b35f32fcf49215f300888f6b3dad7f8701"
CONTROLLER_SHA="02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773"
V1D_SHA="fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14"
NEXT="V91C1E_COMPUTE_TYPE_SAFE_MARKED_BRAUER_IMAGE_OF_A2_02_FULL_SURFACE_CECH_CARTIER_SEED_AND_TEST_MASK20_WITHOUT_POSITIONAL_IDENTIFICATION"
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load(p,expected):
 o=json.loads(p.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256"); assert h==expected==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--check",action="store_true"); ap.add_argument("--write",action="store_true"); a=ap.parse_args()
 ctl=json.loads(CONTROLLER.read_text(encoding="utf-8")); cb=dict(ctl); ch=cb.pop("projection_canonical_sha256"); assert ch==CONTROLLER_SHA==csha(cb); assert ctl["merge_allowed"] is False
 d=load(V1D,V1D_SHA); e=d["exact_consequence"]
 for k in ("a2_02_codimension_one_and_resolution_exceptional_residue_audit_complete","a2_02_purity_offboundary_correction_materialized","a2_02_prime_level_cech_transition_data_materialized","a2_02_cartier_transition_binding_materialized","a2_02_full_surface_cech_cartier_seed_assembly_materialized"): assert e[k] is True
 for k in ("a2_02_marked_brauer_image_computed","a2_02_marked_brauer_image_equal_mask20","a2_02_claimed_e3_coefficient","genuine_full_surface_h2_mu2_lift_for_e3"): assert e[k] is False
 assert d["next_exact_leaf"]==NEXT
 s=json.loads(OUT.read_text(encoding="utf-8")); sb=dict(s); sh=sb.pop("canonical_sha256"); assert sh==STATE_SHA==csha(sb)
 assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V35_V91C1D_HOSTILE_AUDITED_MERGED"
 assert s["authority_sync"]["frontier_authority"]=="V91C1D_A2_02_PURITY_CECH_CARTIER_ASSEMBLY" and s["authority_sync"]["branch_candidate_frontier"] is None
 p=s["audit_provenance"]; assert p["v91c1d_pr"]==1634 and p["hostile_audit_review"]==5123292911 and p["hostile_audit_verdict"]=="PASS" and p["audit_pass_credit"] is True and p["exact_audited_head"]=="1c76c3164681f225c42905067ee0d7d6c4a17418" and p["merge_commit"]=="cf5389b857ee52225ed44543ff7ac8d05387583a" and p["merged_after_hostile_pass"] is True
 assert s["continuation_provenance"]["v91c1c_pr"]==1620 and s["continuation_provenance"]["hostile_audit_pass_claimed"] is False
 assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is True and s["execution_gate"]["advance_scope"]=="V91C1E_MARKED_BRAUER_IMAGE_PRELIGHT_AND_EXACT_COMPUTATION"
 assert s["current_exact_frontier"]["a2_02_marked_brauer_image_computed"] is False and s["current_exact_frontier"]["a2_02_claimed_mask20_image"] is False
 assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False and s["controller_projection_canonical_sha256"]==CONTROLLER_SHA and OUT.stat().st_size<9800
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
 if a.check or not a.write: print(json.dumps({"success":True,"marker":"V98_V91C1D_HOSTILE_AUDITED_MERGED_V91C1E_ACTIVE","state_sha256":STATE_SHA,"authority":s["authority_sync"]["frontier_authority"],"next_exact_leaf":NEXT},sort_keys=True))
if __name__=="__main__": main()
