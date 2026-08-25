#!/usr/bin/env python3
"""Formalize the exact 2Q q-value profile filter discovered on Q4 survivors.

This reruns the retained-Q4 exact scout, locks its exhaustive output, and emits
compact survivor bitsets for the next finite-q leaf.  The underlying test is
section-independent and exact: every H in a retained skeleton fibre has the
same 2Q quadratic-value profile.
"""
import hashlib,json,runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
SCOUT_LOCK='bf083cf26236e49f6596bd0ccb8b63e50a8734a70418a4064f100eada758456d'
BITSET_LOCK='d4a96195628a12f1b69da4a1ed82b5cf638b29dbff304b9ce2083a875ee49471'
Q4_CERT_LOCK='cc7350ecd3a5f7d1c3eca0b96649df0fb1219283190f806ec1e537d28cbd4b19'
TARGET_Q_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
runpy.run_path(str(HERE/'profile_nonelementary_k12_q4_2q_exact_profile_fast.py'))
x=json.loads((HERE/'nonelementary-k12-q4-2q-exact-profile-fast-scout.json').read_text())
if x.get('canonical_sha256')!=SCOUT_LOCK: raise SystemExit('exact 2Q scout moved')
if x.get('source_Q4_survivor_bitsets_sha256')!=BITSET_LOCK or x.get('source_formal_Q4_certificate_sha256')!=Q4_CERT_LOCK:
    raise SystemExit('Q4 provenance moved')
if x.get('source_endpoint_finite_q_sha256')!=TARGET_Q_LOCK or x.get('endpoint_2Q_profile_mod16')!={'0':8192,'8':8192}:
    raise SystemExit('endpoint 2Q target moved')
expected={'k1':(3187,2012416,2227,1493632),'k2':(294,8867840,294,8867840)}
for label,(before_o,before_h,after_o,after_h) in expected.items():
    p=x[label]
    got=(p['Q4_surviving_skeleton_orbits'],p['Q4_surviving_H'],p['skeleton_orbits_matching_exact_2Q_profile'],p['weighted_H_matching_exact_2Q_profile'])
    if got!=(before_o,before_h,after_o,after_h): raise SystemExit(f'{label} 2Q census moved: {got}')
if x['combined_skeleton_orbits_matching_exact_2Q_profile']!=2521 or x['combined_H_matching_exact_2Q_profile']!=10361472:
    raise SystemExit('combined 2Q census moved')

def bithex(n,records):
    b=bytearray((n+7)//8)
    for r in records:
        i=int(r['orbit_index'])
        if not 0<=i<n: raise SystemExit('orbit index outside universe')
        if (b[i//8]>>(i%8))&1: raise SystemExit('duplicate matching orbit index')
        b[i//8]|=1<<(i%8)
    return b.hex()
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K12_Q4_2Q_EXACT_PROFILE_CERT_V1',
 'source_exact_2Q_scout_sha256':SCOUT_LOCK,
 'source_Q4_survivor_bitsets_sha256':BITSET_LOCK,
 'source_formal_Q4_certificate_sha256':Q4_CERT_LOCK,
 'source_endpoint_finite_q_sha256':TARGET_Q_LOCK,
 'endpoint_2Q_profile_mod16':{'0':8192,'8':8192},
 'proof_identity':'q(2x) numerator = 4*wt_X(v)+2*wt_Y(v) mod16 for v=parity(x) in W^perp; uniform K->V and K->2G fibres scale the V-profile by 2^(9-k)',
 'section_independent':True,
 'k1':{'Q4_surviving_skeleton_orbits':3187,'Q4_surviving_H':2012416,
       'skeleton_orbits_matching_exact_2Q_profile':2227,'weighted_H_matching_exact_2Q_profile':1493632,
       'weighted_H_rejected_by_exact_2Q_profile':518784,'skeleton_orbit_universe':4595,
       'matching_orbit_bitset_hex':bithex(4595,x['k1']['matching_orbit_records'])},
 'k2':{'Q4_surviving_skeleton_orbits':294,'Q4_surviving_H':8867840,
       'skeleton_orbits_matching_exact_2Q_profile':294,'weighted_H_matching_exact_2Q_profile':8867840,
       'weighted_H_rejected_by_exact_2Q_profile':0,'skeleton_orbit_universe':427,
       'matching_orbit_bitset_hex':bithex(427,x['k2']['matching_orbit_records'])},
 'combined_Q4_surviving_H':10880256,
 'combined_skeleton_orbits_matching_exact_2Q_profile':2521,
 'combined_H_matching_exact_2Q_profile':10361472,
 'combined_H_rejected_by_exact_2Q_profile':518784,
 'exact_2Q_profile_certified':True,'planning_only':False,
 'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'next':'L33-07-COMPARE-Q2-QUADRATIC-JORDAN-DATA-ON-2521-SKELETON-ORBITS-THEN-FULL-FINITE-Q'}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-q4-2q-exact-profile-certified.json').write_text(json.dumps(cert,sort_keys=True,separators=(',',':'))+'\n')
print(json.dumps({'success':True,'k1_orbits':2227,'k1_H':1493632,'k2_orbits':294,'k2_H':8867840,
 'combined_orbits':2521,'combined_H':10361472,'rejected_H':518784,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
