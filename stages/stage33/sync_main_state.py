#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
H=Path(__file__).resolve().parent; D=H/'33-12'; OUT=H/'MAIN-STATE.json'; CTL=H/'controller.json'
STATE_SHA='30914ca4245ade106985f44d9c64cc79ffd9bc6c4cf04ba6ad3eff4bbf45518d'; CAND_SHA='d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2'; AUTH_SHA='2a176993614fac6f4b1555855794642702f3eeb055d710b8f04ac5097e9fb370'; CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,h):
 o=json.loads(p.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==h==csha(b),p; return o
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA); au=load(D/'e3-v91c1g-a2-02-v4-naturality-fixed-subspace-preflight.json',AUTH_SHA); ca=load(D/'e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json',CAND_SHA)
 ctl=json.loads(CTL.read_text()); cb=dict(ctl); q=cb.pop('projection_canonical_sha256'); assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1G_A2_02_V4_NATURALITY_FIXED_SUBSPACE_PREFLIGHT'
 assert s['candidate_audit_gate']['pr']==1653 and s['candidate_audit_gate']['status']=='PENDING_HOSTILE_AUDIT' and s['candidate_audit_gate']['audit_pass_credit'] is False
 ag=s['authority_audit_gate']; assert ag['pr']==1649 and ag['hostile_audit_review']==5123633478 and ag['hostile_audit_verdict']=='PASS' and ag['merge_commit']=='43f3f3b135a2f5664cb8cc736d6db0b37d7b79da'
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['stage33_07_route_audit']['localization_extension_class_computed'] is False and ca['stage33_07_route_audit']['localization_connecting_map_delta_loc_evaluated'] is False
 assert s['current_exact_frontier']['a2_02_marked_brauer_image_computed'] is False and s['current_exact_frontier']['a2_02_claimed_mask20_image'] is False and s['current_exact_frontier']['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
 assert s['continuation_provenance']['v91c1c_pr']==1620 and s['continuation_provenance']['hostile_audit_pass_claimed'] is False
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write: OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n')
 if a.check or not a.write: print(json.dumps({'success':True,'marker':'V103_V91C1G_AUDITED_V91C1H_LOCALIZATION_PREFLIGHT_PENDING_HOSTILE_AUDIT','state_sha256':STATE_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':s['current']['next_exact_leaf']},sort_keys=True))
if __name__=='__main__': main()
