#!/usr/bin/env python3
"""Exact planning scout: Burnside quotient of k1/k2 integral-cc affine fibres.

Uses only the retained order-288 integral coordinate symmetry.  Fixed sets are
counted by exact F2 elimination; no lift section is sampled or canonicalized.
"""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
SCOUT_LOCK='04348ed4a491efd9481c303c0eb3e3b73d6d00de5f3c1122385477d03b7529c2'
ns=runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
pre=json.loads((HERE/'nonelementary-k12-integral-cc-ct-scout.json').read_text())
if pre.get('canonical_sha256')!=SCOUT_LOCK: raise SystemExit('integral-action source moved')
canon=ns['canon']; complement=ns['complement']; span_coordinate_map=ns['span_coordinate_map']; section_equations=ns['section_equations']; stability_equations=ns['stability_equations']; CC=ns['cc'][0]

def rank(rows): return len(canon(rows))
def affine_rank(rows,nvar):
    piv={}
    for mask,rhs in rows:
        value=int(mask)|((int(rhs)&1)<<nvar); coef=value&((1<<nvar)-1)
        while coef:
            p=coef.bit_length()-1
            if p in piv: value^=piv[p]; coef=value&((1<<nvar)-1)
            else: piv[p]=value; break
        if not coef and ((value>>nvar)&1): return len(piv),False
    return len(piv),True

def affine_action(p_basis,w_basis,qbasis,coords,perm,transport):
    k=len(p_basis); wdim=len(w_basis); q=len(qbasis); nvar=k*q
    tp=tuple(transport(v,perm) for v in p_basis); pcoords=span_coordinate_map(tp)
    rows=[0]*nvar; const=0
    for og,target in enumerate(p_basis):
        comb=pcoords.get(target)
        if comb is None: raise SystemExit('stabilizer lost P')
        selected=[j for j in range(k) if (comb>>j)&1]
        carry=0
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
        tm=0;tc=0
        for out in range(nvar):
            if (int(mask)>>out)&1:
                tm^=rows[out];tc^=(const>>out)&1
        nr,nok=affine_rank(eqs+[(tm,int(rhs)^tc)],nvar)
        if not nok or nr!=br: raise SystemExit('symmetry does not preserve integral affine locus')

def process(label,source,source_ns,prepart):
    sym=tuple(source_ns['sym']); transport=source_ns['transport']; move=source_ns['move']
    if len(sym)!=288 or len(set(sym))!=288: raise SystemExit('symmetry order regression')
    total_h=0;total_orbits=0;stab_hist=Counter();dim_hist=Counter();fixed_hist=Counter();records=[]
    reps=source['orbit_representatives']
    for idx,r in enumerate(reps):
        p=tuple(map(int,r['P_basis_bits']));w=tuple(map(int,r['W_basis_bits']));orbit=int(r['orbit_size']);k=len(p)
        qb=complement(w,canon(1<<j for j in range(14)));q=len(qb);nvar=k*q;coords=span_coordinate_map(w+qb)
        if len(coords)!=(1<<14): raise SystemExit('coordinate-map completeness regression')
        eqs=section_equations(p,qb)+stability_equations(p,w,qb,CC)
        er,ok=affine_rank(eqs,nvar)
        if not ok: raise SystemExit('integral affine locus inconsistent')
        dim=nvar-er
        if dim!=int(prepart['records'][idx]['chosen_cc_dim']): raise SystemExit('integral dimension moved')
        stabilizer=[g for g in sym if move((p,w),g)==(p,w)]
        if len(stabilizer)*orbit!=288: raise SystemExit('orbit-stabilizer regression')
        fsum=0;local=Counter()
        for g in stabilizer:
            rows,const=affine_action(p,w,qb,coords,g,transport)
            if rank(rows)!=nvar: raise SystemExit('affine linear action singular')
            verify_preservation(eqs,rows,const,nvar)
            fixed=list(eqs)
            for out in range(nvar): fixed.append((rows[out]^(1<<out),(const>>out)&1))
            fr,fok=affine_rank(fixed,nvar);fc=(1<<(nvar-fr)) if fok else 0
            fsum+=fc;local[-1 if fc==0 else fc.bit_length()-1]+=1
        if fsum%len(stabilizer): raise SystemExit('Burnside divisibility regression')
        fibre_orbits=fsum//len(stabilizer); total_h+=orbit*(1<<dim); total_orbits+=fibre_orbits
        stab_hist[len(stabilizer)]+=1;dim_hist[dim]+=1;fixed_hist.update(local)
        records.append({'skeleton_orbit_index':idx,'skeleton_orbit_size':orbit,'stabilizer_order':len(stabilizer),'integral_affine_dimension':dim,'integral_affine_section_count':1<<dim,'exact_stabilizer_fibre_orbits':fibre_orbits})
    return {'skeleton_orbits':len(reps),'integral_H_reconstructed':total_h,'exact_full_symmetry_orbits':total_orbits,'stabilizer_order_histogram':{str(k):v for k,v in sorted(stab_hist.items())},'integral_affine_dimension_histogram':{str(k):v for k,v in sorted(dim_hist.items())},'fixed_count_log2_histogram_minus1_is_zero':{str(k):v for k,v in sorted(fixed_hist.items())},'records':records}

out1=process('k1',ns['k1'],ns['k1ns'],pre['k1']);out2=process('k2',ns['k2'],ns['k2ns'],pre['k2'])
if out1['integral_H_reconstructed']!=2928832 or out2['integral_H_reconstructed']!=11866112: raise SystemExit('integral H predecessor regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_INTEGRAL_AFFINE_BURNSIDE_SCOUT_V1','source_integral_action_scout_sha256':SCOUT_LOCK,'k1':out1,'k2':out2,'combined_integral_H':14794944,'combined_exact_full_symmetry_orbits':out1['exact_full_symmetry_orbits']+out2['exact_full_symmetry_orbits'],'fixed_sets_counted_by_exact_F2_elimination':True,'burnside_exact':True,'lift_sections_enumerated':False,'planning_only':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest();(HERE/'nonelementary-k12-integral-affine-burnside-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1_orbits':out1['exact_full_symmetry_orbits'],'k2_orbits':out2['exact_full_symmetry_orbits'],'combined_orbits':cert['combined_exact_full_symmetry_orbits'],'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
