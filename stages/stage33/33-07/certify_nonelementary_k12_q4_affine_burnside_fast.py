#!/usr/bin/env python3
"""Exact retained-Q4 Burnside certificate for k1/k2 non-elementary survivors.

The expensive full-Q4 census is imported through the retained survivor bitsets
whose canonical SHA is source-locked to formal Q4 certificate cc7350....  The
k1/k2 skeleton universes, integral cc affine loci, source symmetry action,
stabilizers, fixed affine sets and Burnside sums are all rebuilt exactly.

For each Q4-surviving skeleton orbit the formal Q4 result says the whole affine
fibre survives.  Therefore the order-288 source symmetry acts on the surviving
set and fixed fibres can be counted by exact F2 elimination, without listing
10,880,256 H.

No finite-q/action-conjugacy/actual-glue/HS/endpoint/theorem credit is granted.
"""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
BITSET_LOCK='d4a96195628a12f1b69da4a1ed82b5cf638b29dbff304b9ce2083a875ee49471'
Q4_CERT_LOCK='cc7350ecd3a5f7d1c3eca0b96649df0fb1219283190f806ec1e537d28cbd4b19'
INTEGRAL_LOCK='04348ed4a491efd9481c303c0eb3e3b73d6d00de5f3c1122385477d03b7529c2'

ret=json.loads((HERE/'nonelementary-k12-full-q4-survivor-bitsets-retained.json').read_text())
r0=dict(ret); declared=r0.pop('canonical_sha256',None)
if declared!=BITSET_LOCK or hashlib.sha256(json.dumps(r0,sort_keys=True,separators=(',',':')).encode()).hexdigest()!=BITSET_LOCK:
    raise SystemExit('retained Q4 survivor bitset lock moved')
if ret.get('source_full_q4_certificate_sha256')!=Q4_CERT_LOCK or not ret.get('whole_affine_fibre_semantics'):
    raise SystemExit('formal Q4 retained provenance moved')

ns=runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
pre=json.loads((HERE/'nonelementary-k12-integral-cc-ct-scout.json').read_text())
if pre.get('canonical_sha256')!=INTEGRAL_LOCK: raise SystemExit('integral affine source moved')
canon=ns['canon']; complement=ns['complement']; span_coordinate_map=ns['span_coordinate_map']
section_equations=ns['section_equations']; stability_equations=ns['stability_equations']; CC=ns['cc'][0]

def rank(rows): return len(canon(rows))
def affine_rank(rows,nvar):
    piv={}; maskall=(1<<nvar)-1
    for mask,rhs in rows:
        value=int(mask)|((int(rhs)&1)<<nvar); coef=value&maskall
        while coef:
            p=coef.bit_length()-1
            if p in piv: value^=piv[p]; coef=value&maskall
            else: piv[p]=value; break
        if not coef and ((value>>nvar)&1): return len(piv),False
    return len(piv),True

def decode(part):
    n=int(part['skeleton_orbit_universe']); data=bytes.fromhex(part['survivor_bitset_hex'])
    if len(data)!=(n+7)//8: raise SystemExit('bitset length regression')
    out=[i for i in range(n) if (data[i//8]>>(i%8))&1]
    if len(out)!=int(part['surviving_skeleton_orbits']): raise SystemExit('bitset population regression')
    if any((data[i//8]>>(i%8))&1 for i in range(n,len(data)*8)): raise SystemExit('nonzero trailing bit')
    return out

def affine_action(p_basis,w_basis,qbasis,coords,perm,transport):
    k=len(p_basis); wdim=len(w_basis); q=len(qbasis); nvar=k*q
    tp=tuple(transport(v,perm) for v in p_basis); pcoords=span_coordinate_map(tp)
    rows=[0]*nvar; const=0
    for og,target in enumerate(p_basis):
        comb=pcoords.get(target)
        if comb is None: raise SystemExit('stabilizer lost P')
        selected=[j for j in range(k) if (comb>>j)&1]; carry=0
        for c in range(14):
            total=sum((tp[j]>>c)&1 for j in selected); tb=(target>>c)&1
            if (total-tb)%2: raise SystemExit('carry parity regression')
            if ((total-tb)//2)&1: carry|=1<<c
        cq=coords[carry]>>wdim
        for ob in range(q):
            if (cq>>ob)&1: const|=1<<(q*og+ob)
        for ig in selected:
            for ib,v in enumerate(qbasis):
                tv=transport(v,perm); oq=coords[tv]>>wdim; iv=q*ig+ib
                for ob in range(q):
                    if (oq>>ob)&1: rows[q*og+ob]^=1<<iv
    return rows,const

def verify_preservation(eqs,rows,const,nvar):
    br,ok=affine_rank(eqs,nvar)
    if not ok: raise SystemExit('source affine locus inconsistent')
    for mask,rhs in eqs:
        tm=0; tc=0
        for out in range(nvar):
            if (int(mask)>>out)&1: tm^=rows[out]; tc^=(const>>out)&1
        nr,nok=affine_rank(eqs+[(tm,int(rhs)^tc)],nvar)
        if not nok or nr!=br: raise SystemExit('symmetry does not preserve affine locus')

def process(label,source,source_ns,prepart,retpart):
    keep=decode(retpart); reps=source['orbit_representatives']; records=prepart['records']
    if len(reps)!=int(retpart['skeleton_orbit_universe']) or len(records)!=len(reps): raise SystemExit('skeleton universe moved')
    sym=tuple(source_ns['sym']); transport=source_ns['transport']; move=source_ns['move']
    if len(sym)!=288 or len(set(sym))!=288: raise SystemExit('symmetry order regression')
    total_h=0; total_orbits=0; stab_hist=Counter(); dim_hist=Counter(); fixed_hist=Counter(); recs=[]
    for idx in keep:
        r=reps[idx]; p=tuple(map(int,r['P_basis_bits'])); w=tuple(map(int,r['W_basis_bits'])); orbit=int(r['orbit_size'])
        k=len(p); qb=complement(w,canon(1<<j for j in range(14))); q=len(qb); nvar=k*q; coords=span_coordinate_map(w+qb)
        if len(coords)!=(1<<14): raise SystemExit('coordinate-map completeness regression')
        eqs=section_equations(p,qb)+stability_equations(p,w,qb,CC); er,ok=affine_rank(eqs,nvar)
        if not ok: raise SystemExit('integral affine locus inconsistent')
        dim=nvar-er
        if dim!=int(records[idx]['chosen_cc_dim']): raise SystemExit('integral affine dimension moved')
        stabilizer=[g for g in sym if move((p,w),g)==(p,w)]
        if len(stabilizer)*orbit!=288: raise SystemExit('orbit-stabilizer regression')
        fsum=0; local=Counter()
        for g in stabilizer:
            rows,const=affine_action(p,w,qb,coords,g,transport)
            if rank(rows)!=nvar: raise SystemExit('affine linear action singular')
            verify_preservation(eqs,rows,const,nvar)
            fixed=list(eqs)+[(rows[out]^(1<<out),(const>>out)&1) for out in range(nvar)]
            fr,fok=affine_rank(fixed,nvar); fc=(1<<(nvar-fr)) if fok else 0
            fsum+=fc; local[-1 if fc==0 else fc.bit_length()-1]+=1
        if fsum%len(stabilizer): raise SystemExit('Burnside divisibility regression')
        fibre_orbits=fsum//len(stabilizer); total_h+=orbit*(1<<dim); total_orbits+=fibre_orbits
        stab_hist[len(stabilizer)]+=1; dim_hist[dim]+=1; fixed_hist.update(local)
        recs.append({'skeleton_orbit_index':idx,'skeleton_orbit_size':orbit,'stabilizer_order':len(stabilizer),
                     'integral_affine_dimension':dim,'Q4_surviving_affine_section_count':1<<dim,
                     'exact_stabilizer_fibre_orbits':fibre_orbits})
    if total_h!=int(retpart['full_Q4_surviving_H']): raise SystemExit(f'{label} Q4 weighted reconstruction failed')
    return {'Q4_surviving_skeleton_orbits':len(keep),'Q4_surviving_H_reconstructed':total_h,
            'exact_full_symmetry_orbits_after_Q4':total_orbits,
            'stabilizer_order_histogram':{str(k):v for k,v in sorted(stab_hist.items())},
            'integral_affine_dimension_histogram':{str(k):v for k,v in sorted(dim_hist.items())},
            'fixed_count_log2_histogram_minus1_is_zero':{str(k):v for k,v in sorted(fixed_hist.items())},'records':recs}

a=process('k1',ns['k1'],ns['k1ns'],pre['k1'],ret['k1']); b=process('k2',ns['k2'],ns['k2ns'],pre['k2'],ret['k2'])
if a['exact_full_symmetry_orbits_after_Q4']!=77076 or b['exact_full_symmetry_orbits_after_Q4']!=303496:
    raise SystemExit(f'Burnside regression {a["exact_full_symmetry_orbits_after_Q4"]} {b["exact_full_symmetry_orbits_after_Q4"]}')
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_Q4_AFFINE_BURNSIDE_FAST_CERT_V1',
 'source_Q4_survivor_bitsets_sha256':BITSET_LOCK,'source_formal_Q4_certificate_sha256':Q4_CERT_LOCK,'source_integral_action_sha256':INTEGRAL_LOCK,
 'k1':a,'k2':b,'combined_Q4_surviving_H':10880256,'combined_exact_full_symmetry_orbits_after_Q4':a['exact_full_symmetry_orbits_after_Q4']+b['exact_full_symmetry_orbits_after_Q4'],
 'Q4_membership_imported_from_formal_retained_bitset':True,'fixed_sets_counted_by_exact_F2_elimination':True,'burnside_exact':True,'burnside_certified':True,
 'lift_sections_enumerated_for_burnside':False,'fast_or_canonical_traversal_used':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'next':'L33-07-IMPOSE-ENDPOINT-FINITE-Q-INVARIANTS-ON-380572-Q4-SURVIVING-FULL-SYMMETRY-ORBITS'}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-q4-affine-burnside-fast-certified.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1_orbits':a['exact_full_symmetry_orbits_after_Q4'],'k2_orbits':b['exact_full_symmetry_orbits_after_Q4'],
 'combined_orbits':cert['combined_exact_full_symmetry_orbits_after_Q4'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
