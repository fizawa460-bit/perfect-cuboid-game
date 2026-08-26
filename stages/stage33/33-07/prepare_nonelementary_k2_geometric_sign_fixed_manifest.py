#!/usr/bin/env python3
"""Prepare exact k=2 Q2-affine seven-geometric-sign fixed-filtration manifest."""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
from nonelementary_k2_geometric_sign_fixed_common import *
HERE=Path(__file__).resolve().parent
Q2LOCK='f9dd684e2813acdbec07fc59575d9d487828c97f6fa8f111983fec5a6fe6b9b0'
ENDLOCK='9f9dec186d3401d75f4aad4e7e4b819529362880091f0070548cb2bf3b13fbf3'
Q2=HERE/'nonelementary-k2-geometric-q2-affine.json'
END=HERE/'endpoint-coordinate-sign-discriminant-actions-split.json'
OUT=HERE/'nonelementary-k2-geometric-sign-fixed-manifest.json'

def load(p,lock=None):
 d=json.loads(p.read_text());s=d.get('canonical_sha256');u=dict(d);u.pop('canonical_sha256',None);h=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 if s!=h or (lock and s!=lock):raise SystemExit(f'hash regression {p.name}: {s} {h}')
 return d
q2=load(Q2,Q2LOCK);end=load(END,ENDLOCK)
if q2.get('arithmetic_generators_used')!=[] or len(q2.get('records',[]))!=867:raise SystemExit('Q2 source firewall/universe regression')
if q2.get('Q2_profile_surviving_representative_sections')!=2183168 or q2.get('Q2_profile_surviving_weighted_H')!=129468416:raise SystemExit('Q2 source count regression')
if end.get('schema')!='STAGE33_07_ENDPOINT_COORDINATE_SIGN_DISCRIMINANT_ACTIONS_SPLIT_V2' or len(end.get('sign_actions_mixed_moduli',[]))!=7:raise SystemExit('endpoint sign source regression')
if not end.get('all_actions_well_defined_involutions_and_q_isometries') or not end.get('seven_sign_involutions_commute') or not end.get('seven_sign_product_identity'):raise SystemExit('endpoint sign relation regression')
if end.get('discriminant_moduli')!=TARGET_MODS:raise SystemExit('endpoint sign moduli regression')
endpoint_q2=tuple(fixed_log2_from_action(A,TARGET_MODS,2) for A in end['sign_actions_mixed_moduli'])
endpoint_q4=tuple(fixed_log2_from_action(A,TARGET_MODS,4) for A in end['sign_actions_mixed_moduli'])
if endpoint_q2!=(12,)*7 or endpoint_q4!=(14,)*7:raise SystemExit(f'endpoint fixed filtration moved {endpoint_q2} {endpoint_q4}')
runpy.run_path(str(HERE/'prepare_nonelementary_k2_geometric_q4_manifest.py'))
man=load(HERE/'nonelementary-k2-geometric-q4-manifest.json')
if man.get('arithmetic_generators_used')!=[] or man.get('orbit_count')!=1496:raise SystemExit('geometric manifest firewall/universe regression')
mr={int(r['orbit_index']):r for r in man['records']}
records=[];base_reject=Counter();profile=Counter();rep=weighted=0
for qr in q2['records']:
 oi=int(qr['orbit_index']);r=mr[oi]
 if not all_sections_stable_under_signs(r):raise SystemExit(f'geometric sign failed section-independent H stability orbit {oi}')
 rr=tuple(map(int,qr['Q2_survivor_affine_rref_augmented']));free=free_variables(rr);dim=int(qr['Q2_survivor_affine_dimension'])
 if len(free)!=dim:raise SystemExit('Q2 affine dimension regression')
 sol=solution_from_free(rr,free,0);Hrows=reconstruct_H(r,sol);verify_isotropic_H(Hrows)
 q2logs=tuple(fixed_Qpower_log2_direct(Hrows,i,2) for i in range(7))
 q4logs=tuple(fixed_Qpower_log2_direct(Hrows,i,4) for i in range(7))
 preferred=None;reason=None
 for i,x in enumerate(q2logs):
  if x!=12:preferred=i;reason='Q2';break
 if preferred is None:
  for i,x in enumerate(q4logs):
   if x!=14:preferred=i;reason='Q4';break
 if preferred is None:raise SystemExit(f'base section unexpectedly passes fixed filtration orbit {oi}')
 base_reject[reason]+=1;profile[(q2logs,q4logs)]+=1
 n=int(qr['Q2_profile_surviving_representative_sections']);w=int(qr['weighted_H_after_Q2_profile']);rep+=n;weighted+=w
 records.append({
  'orbit_index':oi,'orbit_size':int(qr['orbit_size']),'t':int(qr['t']),
  'P_basis_bits':list(map(int,r['P_basis_bits'])),'W_basis_bits':list(map(int,r['W_basis_bits'])),'quotient_basis_bits':list(map(int,r['quotient_basis_bits'])),
  'Q2_survivor_affine_dimension':dim,'Q2_survivor_affine_rref_augmented':list(rr),
  'representative_section_count':n,'weighted_H_count':w,
  'preferred_first_sign_index':preferred,'base_rejection_layer':reason,
  'base_fixed_Q2_log2':list(q2logs),'base_fixed_Q4_log2':list(q4logs),
 })
if (rep,weighted)!=(2183168,129468416):raise SystemExit('manifest total regression')
if base_reject!=Counter({'Q2':455,'Q4':412}):raise SystemExit(f'base rejection census moved {base_reject}')
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_SIGN_FIXED_MANIFEST_V1',
 'source_Q2_affine_sha256':Q2LOCK,'source_endpoint_coordinate_sign_sha256':ENDLOCK,'source_geometric_q4_manifest_sha256':man['canonical_sha256'],
 'arithmetic_generators_used':[],'geometric_coordinate_signs_used':7,
 'source_sign_description':'+1 on one coordinate-K3 rank-2 block and -1 on the other six blocks in L0=<8>^10+<16>^4',
 'all_867_families_H_stable_under_all_seven_signs_for_every_affine_section':True,
 'stability_reason':'for order4 h=p+2c the sign difference is 2*(p on negated blocks), independent of correction c, and lies in the order2 subgroup W; order2 generators are sign-fixed',
 'endpoint_fixed_Q2_log2_by_sign':list(endpoint_q2),'endpoint_fixed_Q4_log2_by_sign':list(endpoint_q4),
 'family_count':867,'representative_section_count':rep,'weighted_H_count':weighted,
 'base_section_early_rejection_layer_counts':dict(sorted(base_reject.items())),
 'all_base_sections_rejected_by_fixed_filtration':True,
 'base_section_profile_distinct_count':len(profile),
 'records':records,
 'full_affine_fixed_filtration_census_certified':False,'k2_nonelementary_type_rejected':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'families':867,'sections':rep,'weighted_H':weighted,'base_rejection_layers':dict(base_reject),'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
