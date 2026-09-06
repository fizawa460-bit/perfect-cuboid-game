#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'
STATE_SHA='263bfb052deb8c59b7ed93fc7790ce45533334c3e81743fa772906021b52bea1'
AUTH_SHA='d05672463ce6340773b6a4394851398360cf58b03f544ea4c00ff0d345089be2'
CAND_SHA='6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa'
CTL_SHA='02cb0f964086509f8bef4ad4dc5481f9f668b7ca8127f54ebb2952831638f773'

def csha(o):
 return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(p,h):
 o=json.loads(p.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256')
 assert q==h==csha(b),p
 return o

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
 s=load(OUT,STATE_SHA)
 au=load(D/'e3-v91c1h-a2-02-stage33-07-localization-quotient-preflight.json',AUTH_SHA)
 ca=load(D/'e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json',CAND_SHA)
 ctl=json.loads(CTL.read_text(encoding='utf-8')); cb=dict(ctl); q=cb.pop('projection_canonical_sha256')
 assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1H_A2_02_STAGE33_07_LOCALIZATION_QUOTIENT_PREFLIGHT'
 ag=s['authority_audit_gate']
 assert ag['pr']==1653
 assert ag['hostile_audit_review']==5124792802
 assert ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='d7750f80571a8da7f4edfee43924121efa5aa15a'
 assert ag['merge_commit']=='7a608ee2511192af8e293d88f8a7117aa5ad19d9'
 assert ag['merged'] is True and ag['audit_pass_credit'] is True
 cg=s['candidate_audit_gate']
 assert cg['candidate']=='V91C1T_A2_02_SWAP23_PIC2_ADAPTER_PREFLIGHT'
 assert cg['pr']==1661 and cg['status']=='PENDING_HOSTILE_AUDIT'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert ca['exact_consequence']['literal_swap23_full_codim1_difference_nonzero'] is True
 assert ca['exact_consequence']['pic2_cech_difference_class_computed'] is False
 assert ca['exact_consequence']['a2_02_swap23_seed_fixed_mod_pic2'] is False
 assert ca['exact_consequence']['a2_02_marked_brauer_image_excluded_from_mask20'] is False
 assert s['current_exact_frontier']['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert s['current_exact_frontier']['a2_02_marked_brauer_image_computed'] is False
 assert s['current_exact_frontier']['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
 assert s['stage33_progress']=='6/11'
 assert s['execution_gate']['advance_allowed'] is False
 assert s['firewalls']['merge_allowed'] is False
 if a.write:
  OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
 if a.check or not a.write:
  print(json.dumps({'success':True,'marker':'V104_V91C1H_AUDITED_MERGED_V91C1T_SWAP23_PIC2_ADAPTER_PREFLIGHT_PENDING_HOSTILE_AUDIT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':s['current']['next_exact_leaf']},sort_keys=True))

if __name__=='__main__':
 main()
