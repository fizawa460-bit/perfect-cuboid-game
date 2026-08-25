#!/usr/bin/env python3
"""Fast exact scout for the full 2Q q-value profile on formal-Q4 survivors.

The expensive 1,020,880-section Q4 census is not rerun.  Its formally certified
survivor membership is imported from the retained 2.5KB bitsets, source-locked
to formal Q4 certificate cc7350....  Everything after that import is exact:
we rebuild the k1/k2 skeleton universes and integral affine dimensions, decode
exactly 3,187+294 surviving skeleton orbits, reconstruct the formal weighted
Q4 survivor totals, and compare the complete 2Q quadratic-value profile.

For K=H^perp, G=K/H and V=parity(K)=W^perp,
  q(2x) numerator = 4*wt_X(v)+2*wt_Y(v) mod 16.
The q-value depends only on v.  Uniform fibres of K->V and K->2G imply that
the profile on 2G is the V-profile multiplied by |2G|/|V|=2^(9-k), since the
formal Q4 group order fixes |2G|=2^14 and dim V=5+k.

This is an exact necessary finite-q invariant, not full finite-q isometry or
action conjugacy.  Planning credit only until the discovered counts are locked.
"""
import hashlib,itertools,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
BITSET_LOCK='d4a96195628a12f1b69da4a1ed82b5cf638b29dbff304b9ce2083a875ee49471'
Q4_CERT_LOCK='cc7350ecd3a5f7d1c3eca0b96649df0fb1219283190f806ec1e537d28cbd4b19'
TARGET_Q_LOCK='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
X_MASK=(1<<10)-1

ret=json.loads((HERE/'nonelementary-k12-full-q4-survivor-bitsets-retained.json').read_text())
r0=dict(ret); got=r0.pop('canonical_sha256',None)
raw=json.dumps(r0,sort_keys=True,separators=(',',':')).encode()
if got!=BITSET_LOCK or hashlib.sha256(raw).hexdigest()!=BITSET_LOCK: raise SystemExit('Q4 survivor bitset retained lock moved')
if ret.get('source_full_q4_certificate_sha256')!=Q4_CERT_LOCK: raise SystemExit('formal Q4 provenance moved')
if not ret.get('full_Q4_condition_certified') or not ret.get('whole_affine_fibre_semantics'): raise SystemExit('Q4 retained firewall moved')

target=json.loads((HERE/'picard-discriminant-compact.json').read_text())
if target.get('canonical_sha256')!=TARGET_Q_LOCK: raise SystemExit('endpoint finite-q source lock moved')
mods=list(map(int,target['discriminant_moduli'])); B=[[int(x) for x in row] for row in target['discriminant_bilinear_numerator_over_8_reduced']]
if mods!=[2]*4+[4]*6+[8]*4: raise SystemExit('endpoint group structure moved')

def endpoint_2q_profile():
    prof=Counter()
    for v in itertools.product(*[range(0,m,2) for m in mods]):
        prof[sum(v[i]*B[i][j]*v[j] for i in range(14) for j in range(14))%16]+=1
    return prof
TARGET=endpoint_2q_profile()
if TARGET!=Counter({0:8192,8:8192}): raise SystemExit(f'endpoint 2Q profile moved {TARGET}')

# Rebuild exact skeleton representatives and integral affine dimensions only.
ns=runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
pre=json.loads((HERE/'nonelementary-k12-integral-cc-ct-scout.json').read_text())
if pre.get('canonical_sha256')!='04348ed4a491efd9481c303c0eb3e3b73d6d00de5f3c1122385477d03b7529c2': raise SystemExit('integral source moved')
canon=ns['canon']; sources={'k1':ns['k1'],'k2':ns['k2']}

def decode(part):
    n=int(part['skeleton_orbit_universe']); data=bytes.fromhex(part['survivor_bitset_hex'])
    if len(data)!=(n+7)//8: raise SystemExit('bitset length regression')
    out=[i for i in range(n) if (data[i//8]>>(i%8))&1]
    if len(out)!=int(part['surviving_skeleton_orbits']): raise SystemExit('bitset population regression')
    if any((data[i//8]>>(i%8))&1 for i in range(n,len(data)*8)): raise SystemExit('nonzero trailing bit')
    return out

def kernel_basis(rows,n=14):
    rr=canon(rows); piv=[int(r).bit_length()-1 for r in rr]; ps=set(piv); out=[]
    for f in range(n):
        if f in ps: continue
        x=1<<f
        for r,p in zip(rr,piv):
            if (int(r)&x).bit_count()&1: x^=1<<p
        if any((int(r)&x).bit_count()&1 for r in rr): raise SystemExit('Wperp kernel regression')
        out.append(x)
    return tuple(out)
def span(basis):
    out=[0]
    for b in basis: out += [x^int(b) for x in out]
    return out

def full_profile(w,k):
    vb=kernel_basis(w)
    if len(vb)!=5+k: raise SystemExit('V dimension regression')
    small=Counter((4*(v&X_MASK).bit_count()+2*(v>>10).bit_count())%16 for v in span(vb))
    if any(q not in (0,8) for q in small): raise SystemExit(f'predecessor 2Q support lost {small}')
    mult=1<<(9-k); full=Counter({q:n*mult for q,n in small.items()})
    if sum(full.values())!=1<<14: raise SystemExit('2Q size regression')
    return small,full

def process(label):
    k=1 if label=='k1' else 2; src=sources[label]; pp=pre[label]; rp=ret[label]
    keep=decode(rp); reps=src['orbit_representatives']; records=pp['records']
    if len(reps)!=int(rp['skeleton_orbit_universe']) or len(records)!=len(reps): raise SystemExit('universe regression')
    before=after=0; passed=[]; hist=Counter()
    for idx in keep:
        r=reps[idx]; w=tuple(map(int,r['W_basis_bits'])); orbit=int(r['orbit_size']); dim=int(records[idx]['chosen_cc_dim'])
        weight=orbit*(1<<dim); before+=weight
        small,full=full_profile(w,k); hist[tuple(sorted(full.items()))]+=1
        if full==TARGET:
            after+=weight; passed.append({'orbit_index':idx,'orbit_size':orbit,'dimension':dim,'small_V_profile':{str(q):n for q,n in sorted(small.items())}})
    if before!=int(rp['full_Q4_surviving_H']): raise SystemExit(f'{label} Q4 weighted reconstruction failed {before}')
    return {'Q4_surviving_skeleton_orbits':len(keep),'Q4_surviving_H':before,
            'skeleton_orbits_matching_exact_2Q_profile':len(passed),'weighted_H_matching_exact_2Q_profile':after,
            'weighted_H_rejected_by_exact_2Q_profile':before-after,
            'profile_histogram':{str(dict(key)):v for key,v in sorted(hist.items(),key=lambda z:str(z[0]))},
            'matching_orbit_records':passed}

a=process('k1'); b=process('k2')
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_Q4_2Q_EXACT_PROFILE_FAST_SCOUT_V1',
 'source_Q4_survivor_bitsets_sha256':BITSET_LOCK,'source_formal_Q4_certificate_sha256':Q4_CERT_LOCK,
 'source_endpoint_finite_q_sha256':TARGET_Q_LOCK,'endpoint_2Q_profile_mod16':{str(q):n for q,n in sorted(TARGET.items())},
 'source_profile_formula_mod16':'4*wt_X(v)+2*wt_Y(v), v in V=W^perp','uniform_profile_multiplier':'2^(9-k)',
 'Q4_membership_imported_from_formal_retained_bitset':True,'section_independent':True,'k1':a,'k2':b,
 'combined_Q4_surviving_H':a['Q4_surviving_H']+b['Q4_surviving_H'],
 'combined_H_matching_exact_2Q_profile':a['weighted_H_matching_exact_2Q_profile']+b['weighted_H_matching_exact_2Q_profile'],
 'combined_skeleton_orbits_matching_exact_2Q_profile':a['skeleton_orbits_matching_exact_2Q_profile']+b['skeleton_orbits_matching_exact_2Q_profile'],
 'planning_only':True,'exact_2Q_profile_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-q4-2q-exact-profile-fast-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1_orbits_after':a['skeleton_orbits_matching_exact_2Q_profile'],'k1_H_after':a['weighted_H_matching_exact_2Q_profile'],
 'k2_orbits_after':b['skeleton_orbits_matching_exact_2Q_profile'],'k2_H_after':b['weighted_H_matching_exact_2Q_profile'],
 'combined_orbits_after':cert['combined_skeleton_orbits_matching_exact_2Q_profile'],'combined_H_after':cert['combined_H_matching_exact_2Q_profile'],
 'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
