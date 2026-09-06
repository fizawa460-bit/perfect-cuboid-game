#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

H=Path(__file__).resolve().parent
D=H/'33-12'
OUT=H/'MAIN-STATE.json'
CTL=H/'controller.json'
STATE_SHA='a1102c55582f9ce09bd19384a881eda2824dad4a2912f2d69bbd0d2dcc6b4713'
AUTH_SHA='6c064cf02fb7a0908242317bf7ac1b20b0586751b78e07b26d6c7889060ffdfa'
CAND_SHA='7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34'
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
 au=load(D/'e3-v91c1t-a2-02-swap23-pic2-adapter-preflight.json',AUTH_SHA)
 ca=load(D/'e3-v91c1u-a2-02-known140-locator-preflight.json',CAND_SHA)
 ctl=json.loads(CTL.read_text(encoding='utf-8')); cb=dict(ctl); q=cb.pop('projection_canonical_sha256')
 assert q==CTL_SHA==csha(cb) and ctl['merge_allowed'] is False
 assert s['authority_sync']['frontier_authority']=='V91C1T_A2_02_SWAP23_PIC2_ADAPTER_PREFLIGHT'
 ag=s['authority_audit_gate']
 assert ag['pr']==1661 and ag['hostile_audit_review']==5124888078 and ag['hostile_audit_verdict']=='PASS'
 assert ag['exact_audited_head']=='da521c5091f42f4e9f40d71a81f484f232b6a5d5'
 assert ag['merge_commit']=='f6b1d047dfd238de80ed8f5c267609d01ea1a3bb'
 assert ag['merged'] is True and ag['audit_pass_credit'] is True
 cg=s['candidate_audit_gate']
 assert cg['candidate']=='V91C1U_A2_02_KNOWN140_LOCATOR_PREFLIGHT'
 assert cg['pr']==1663 and cg['status']=='PENDING_HOSTILE_AUDIT'
 assert cg['audit_pass_credit'] is False and cg['merge_allowed'] is False
 assert au['canonical_sha256']==AUTH_SHA and ca['canonical_sha256']==CAND_SHA
 assert au['exact_consequence']['literal_swap23_full_codim1_difference_nonzero'] is True
 assert au['exact_consequence']['pic2_cech_difference_class_computed'] is False
 assert ca['materialized_capabilities']['known_surface_class_count']==140
 assert ca['materialized_capabilities']['known_surface_classes_recoverable_in_primitive_indlist_picard64'] is True
 assert ca['locator_audit']['strict_actual_prime_to_known140_class_index_materialized'] is False
 assert ca['locator_audit']['exceptional_id_to_known140_class_index_materialized'] is False
 f=s['current_exact_frontier']
 assert f['a2_02_known140_picard64_recovery_materialized'] is True
 assert f['a2_02_swap23_strict_prime_to_known140_locator_materialized'] is False
 assert f['a2_02_swap23_exceptional_id_to_known140_locator_materialized'] is False
 assert f['a2_02_swap23_actual_divisor_to_retained_picard64_adapter_materialized'] is False
 assert f['pic2_cech_difference_class_computed'] is False
 assert f['a2_02_swap23_seed_fixed_mod_pic2'] is False
 assert f['a2_02_marked_brauer_image_computed'] is False
 assert f['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
 assert s['stage33_progress']=='6/11' and s['execution_gate']['advance_allowed'] is False and s['firewalls']['merge_allowed'] is False
 if a.write:
  OUT.write_text(json.dumps(s,sort_keys=True,separators=(',',':'))+'\n',encoding='utf-8')
 if a.check or not a.write:
  print(json.dumps({'success':True,'marker':'V105_V91C1T_AUDITED_MERGED_V91C1U_KNOWN140_LOCATOR_PREFLIGHT_PENDING_HOSTILE_AUDIT','state_sha256':STATE_SHA,'authority_sha256':AUTH_SHA,'candidate_sha256':CAND_SHA,'next_exact_leaf':s['current']['next_exact_leaf']},sort_keys=True))

if __name__=='__main__':
 main()
