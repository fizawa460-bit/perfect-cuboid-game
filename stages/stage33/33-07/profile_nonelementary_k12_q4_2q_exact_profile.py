#!/usr/bin/env python3
"""Exact scout: full 2Q quadratic-value profile on every k1/k2 Q4 survivor.

For K=H^perp and G=K/H, the parity image of K is V=W^perp.  For x in K
with parity v, the quadratic numerator of the doubled quotient class 2x is

    4*wt_X(v) + 2*wt_Y(v)  (mod 16).

This value depends only on v.  The map K -> 2G has a kernel of constant size,
and the parity map K -> V also has constant-size fibres.  Consequently the
full q-value profile on 2G is exactly the profile on V multiplied by the
constant |2G|/|V|.  The certified Q4 image-order leaf fixes the target group
structure, hence |2G|=2^14; dim(V)=5+k, so the multiplier is 2^(9-k).

Thus each surviving skeleton can be checked by only 64 (k=1) or 128 (k=2)
parity vectors.  The test is independent of the affine lift section and may
reject an entire Q4-surviving fibre exactly.  This is a necessary finite-q
invariant only; it is not full finite-q isometry or action conjugacy.
"""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
Q4_CERT_LOCK='cc7350ecd3a5f7d1c3eca0b96649df0fb1219283190f806ec1e537d28cbd4b19'
TARGET_Q_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
X_MASK=(1<<10)-1

q4=json.loads((HERE/'nonelementary-k12-full-q4-certified.json').read_text())
if q4.get('canonical_sha256')!=Q4_CERT_LOCK: raise SystemExit('formal Q4 certificate moved')
if not q4.get('full_Q4_condition_certified') or not q4.get('all_affine_sections_exhausted'):
    raise SystemExit('formal Q4 predecessor is not exhaustive')
if q4.get('combined_full_Q4_surviving_H')!=10880256: raise SystemExit('Q4 survivor total moved')

target=json.loads((HERE/'picard-discriminant-compact.json').read_text())
if target.get('canonical_sha256')!=TARGET_Q_LOCK: raise SystemExit('endpoint finite-q source lock moved')
mods=list(map(int,target['discriminant_moduli']))
B=[[int(x) for x in row] for row in target['discriminant_bilinear_numerator_over_8_reduced']]
if mods!=[2]*4+[4]*6+[8]*4: raise SystemExit('endpoint group structure moved')

# Independently recompute the endpoint 2Q profile in the retained Smith basis.
def target_2q_profile():
    choices=[list(range(0,m,2)) for m in mods]
    prof=Counter()
    import itertools
    for v in itertools.product(*choices):
        q=sum(v[i]*B[i][j]*v[j] for i in range(14) for j in range(14))%16
        prof[q]+=1
    return prof
TARGET_PROFILE=target_2q_profile()
if TARGET_PROFILE!=Counter({0:8192,8:8192}): raise SystemExit(f'endpoint 2Q profile moved: {TARGET_PROFILE}')

# Rebuild exact k1/k2 skeleton representatives.  This source is already after
# the Q[2] and 2Q support reductions, so any value 4 or 12 below is a regression.
ns=runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
sources={'k1':ns['k1'],'k2':ns['k2']}
canon=ns['canon']

def kernel_basis(rows,n=14):
    rr=canon(rows); piv=[int(r).bit_length()-1 for r in rr]; ps=set(piv)
    out=[]
    for f in range(n):
        if f in ps: continue
        x=1<<f
        for r,p in zip(rr,piv):
            if ((int(r)&x).bit_count()&1): x^=1<<p
        if any((int(r)&x).bit_count()&1 for r in rr): raise SystemExit('orthogonal-kernel construction failed')
        out.append(x)
    if len(out)!=n-len(rr): raise SystemExit('orthogonal-kernel dimension regression')
    return tuple(out)

def span(basis):
    vals=[0]
    for b in basis: vals += [x^int(b) for x in vals]
    return tuple(vals)

def small_profile(w,k):
    vb=kernel_basis(w,14)
    if len(vb)!=5+k: raise SystemExit('V=Wperp dimension regression')
    prof=Counter()
    for v in span(vb):
        q=(4*(v&X_MASK).bit_count()+2*(v>>10).bit_count())%16
        prof[q]+=1
    if any(q not in (0,8) for q in prof): raise SystemExit(f'2Q support predecessor regression: {prof}')
    scale=1<<(9-k)
    full=Counter({q:n*scale for q,n in prof.items()})
    if sum(full.values())!=1<<14: raise SystemExit('2Q cardinality reconstruction regression')
    return prof,full

def survivor_map(part):
    out={}
    for r in part['surviving_orbit_records']:
        idx=int(r['orbit_index'])
        if int(r['representative_section_survivors'])!=(1<<int(r['dimension'])):
            raise SystemExit('Q4 survivor fibre is not whole')
        out[idx]=r
    return out

def process(label,source,q4part):
    k=1 if label=='k1' else 2
    keep=survivor_map(q4part); reps=source['orbit_representatives']
    hist=Counter(); passed=[]; before=after=0
    for idx in sorted(keep):
        r=reps[idx]; w=tuple(map(int,r['W_basis_bits'])); orbit=int(r['orbit_size'])
        rec=keep[idx]; weight=orbit*(1<<int(rec['dimension'])); before+=weight
        small,full=small_profile(w,k)
        key=tuple(sorted(full.items())); hist[key]+=1
        if full==TARGET_PROFILE:
            after+=weight
            passed.append({'orbit_index':idx,'orbit_size':orbit,'dimension':int(rec['dimension']),
                           'small_V_profile_mod16':{str(q):n for q,n in sorted(small.items())}})
    if before!=int(q4part['full_Q4_surviving_H']): raise SystemExit('Q4 weighted predecessor reconstruction failed')
    return {'Q4_surviving_skeleton_orbits':len(keep),'Q4_surviving_H':before,
            'skeleton_orbits_matching_exact_2Q_profile':len(passed),
            'weighted_H_matching_exact_2Q_profile':after,'weighted_H_rejected_by_exact_2Q_profile':before-after,
            'profile_histogram':{str(dict(k)):v for k,v in sorted(hist.items(),key=lambda z:str(z[0]))},
            'matching_orbit_records':passed}

out1=process('k1',sources['k1'],q4['k1']); out2=process('k2',sources['k2'],q4['k2'])
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_Q4_2Q_EXACT_PROFILE_SCOUT_V1',
      'source_Q4_certificate_sha256':Q4_CERT_LOCK,'source_endpoint_finite_q_sha256':TARGET_Q_LOCK,
      'endpoint_2Q_profile_mod16':{str(q):n for q,n in sorted(TARGET_PROFILE.items())},
      'source_profile_formula_mod16':'4*wt_X(v)+2*wt_Y(v), v in V=W^perp',
      'uniform_profile_multiplier':'|2G|/|V|=2^(9-k)',
      'section_independent':True,'k1':out1,'k2':out2,
      'combined_Q4_surviving_H':out1['Q4_surviving_H']+out2['Q4_surviving_H'],
      'combined_H_matching_exact_2Q_profile':out1['weighted_H_matching_exact_2Q_profile']+out2['weighted_H_matching_exact_2Q_profile'],
      'combined_skeleton_orbits_matching_exact_2Q_profile':out1['skeleton_orbits_matching_exact_2Q_profile']+out2['skeleton_orbits_matching_exact_2Q_profile'],
      'exact_2Q_profile_certified':False,'planning_only':True,'endpoint_finite_q_certified':False,
      'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,
      'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
      'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
      'next':'L33-07-FORMALIZE-EXACT-2Q-PROFILE-THEN-COMPARE-Q2-JORDAN-ARF-INVARIANT'}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-q4-2q-exact-profile-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,
                  'k1_orbits_after':out1['skeleton_orbits_matching_exact_2Q_profile'],'k1_H_after':out1['weighted_H_matching_exact_2Q_profile'],
                  'k2_orbits_after':out2['skeleton_orbits_matching_exact_2Q_profile'],'k2_H_after':out2['weighted_H_matching_exact_2Q_profile'],
                  'combined_orbits_after':cert['combined_skeleton_orbits_matching_exact_2Q_profile'],
                  'combined_H_after':cert['combined_H_matching_exact_2Q_profile'],
                  'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
