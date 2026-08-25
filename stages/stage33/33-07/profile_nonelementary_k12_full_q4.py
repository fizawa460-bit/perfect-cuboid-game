#!/usr/bin/env python3
"""Exhaust full Q[4] image-order on every compressed k=1,2 affine section.

Planning leaf. No canonical traversal or representative pruning inside a fibre:
all affine sections over every exact skeleton-orbit representative are visited.
Symmetry is used only for the already-certified skeleton orbit weighting.
"""
import hashlib,json,runpy
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
INTEGRAL_SCOUT_LOCK='04348ed4a491efd9481c303c0eb3e3b73d6d00de5f3c1122385477d03b7529c2'
X_MASK=(1<<10)-1
ns=runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
pre=json.loads((HERE/'nonelementary-k12-integral-cc-ct-scout.json').read_text())
if pre.get('canonical_sha256')!=INTEGRAL_SCOUT_LOCK: raise SystemExit('integral action source moved')
canon=ns['canon']; complement=ns['complement']; section_equations=ns['section_equations']; stability_equations=ns['stability_equations']; affine_rref=ns['affine_rref']; CC=ns['cc'][0]
sources={'k1':ns['k1'],'k2':ns['k2']}

def rank(rows): return len(canon(rows))
def free_variables(reduced,nvar):
    piv=set()
    for value in reduced:
        coef=int(value)&((1<<nvar)-1)
        piv.add(coef.bit_length()-1)
    return tuple(i for i in range(nvar) if i not in piv)
def solution_from_free(reduced,nvar,free_mask):
    free=free_variables(reduced,nvar); sol=0
    for j,v in enumerate(free):
        if (int(free_mask)>>j)&1: sol|=1<<v
    for value in reversed(reduced):
        coef=int(value)&((1<<nvar)-1); p=coef.bit_length()-1
        rhs=((int(value)>>nvar)&1)^((coef&sol).bit_count()&1)
        if rhs: sol|=1<<p
    for value in reduced:
        coef=int(value)&((1<<nvar)-1); rhs=(int(value)>>nvar)&1
        if ((coef&sol).bit_count()&1)!=rhs: raise SystemExit('affine solution reconstruction regression')
    return sol

def add_mod4(a,b): return tuple((int(x)+int(y))%4 for x,y in zip(a,b))
def add_selected_rows(rows,mask):
    out=(0,)*14
    for i,row in enumerate(rows):
        if (int(mask)>>i)&1: out=add_mod4(out,row)
    return out

def kernel_coefficients(p_basis):
    k=len(p_basis)
    return canon(c for c in range(1,1<<k) if all(sum(((c>>i)&1)*((int(p_basis[i])>>j)&1) for i in range(k))%2==0 for j in range(10)))
def root_mod4(u):
    r=[0]*14
    for i in range(10):
        if int(u[i])%2: raise SystemExit('fourth-root X parity regression')
        r[i]=(int(u[i])//2)%2
    for i in range(10,14): r[i]=int(u[i])%4
    return tuple(r)
def functional_mask_even(root,hgens):
    mask=0
    for j,h in enumerate(hgens):
        v=sum(int(root[i])*int(h[i]) for i in range(14))%4
        if v%2: raise SystemExit('theta image lost exponent two under maximal Q2')
        if (v//2)&1: mask|=1<<j
    return mask

def h_generators(p_basis,w_basis,qbasis,solution):
    k=len(p_basis); q=len(qbasis); order4=[]
    for g,p in enumerate(p_basis):
        correction=0
        for bit,v in enumerate(qbasis):
            if (int(solution)>>(q*g+bit))&1: correction^=int(v)
        order4.append(tuple((((int(p)>>c)&1)+2*((correction>>c)&1))%4 for c in range(14)))
    wc=complement(p_basis,w_basis)
    if len(wc)!=9-2*k: raise SystemExit('W/P rank regression')
    order2=[tuple(2*((int(w)>>c)&1) for c in range(14)) for w in wc]
    h=tuple(order4+order2)
    if len(h)!=9-k: raise SystemExit('H generator count regression')
    return h

def theta_masks(p_basis,w_basis,qbasis,solution):
    k=len(p_basis); h=h_generators(p_basis,w_basis,qbasis,solution); masks=[]
    for c in range(10):
        root=[0]*14; root[c]=2; masks.append(functional_mask_even(tuple(root),h))
    for w in w_basis:
        u=tuple(2*((int(w)>>c)&1) for c in range(14)); masks.append(functional_mask_even(root_mod4(u),h))
    for coeff in kernel_coefficients(p_basis):
        u=add_selected_rows(h[:k],coeff); masks.append(functional_mask_even(root_mod4(u),h))
    return tuple(masks)

def process(label,source,prepart):
    total_rep=0; total_weighted=0; surv_rep=0; surv_weighted=0; rank_hist=Counter(); target_hist=Counter(); dim_hist=Counter(); orbit_survivors=[]
    records=prepart['records']
    if len(records)!=len(source['orbit_representatives']): raise SystemExit('integral record count regression')
    for idx,r in enumerate(source['orbit_representatives']):
        p=tuple(map(int,r['P_basis_bits'])); w=tuple(map(int,r['W_basis_bits'])); orbit=int(r['orbit_size']); k=len(p)
        qb=complement(w,canon(1<<j for j in range(14))); q=len(qb); nvar=k*q
        reduced=affine_rref(section_equations(p,qb)+stability_equations(p,w,qb,CC),nvar)
        if reduced is None: raise SystemExit('integral cc fibre inconsistent')
        dim=nvar-len(reduced); dim_hist[dim]+=1
        if dim!=int(records[idx]['chosen_cc_dim']): raise SystemExit('integral affine dimension moved')
        t=rank([x&X_MASK for x in p]); target=4-t
        if target not in (2,3,4): raise SystemExit('target theta rank regression')
        local=0
        for free in range(1<<dim):
            sol=solution_from_free(reduced,nvar,free)
            rr=rank(theta_masks(p,w,qb,sol)); rank_hist[rr]+=1; target_hist[(target,rr)]+=1
            total_rep+=1; total_weighted+=orbit
            if rr==target: local+=1; surv_rep+=1; surv_weighted+=orbit
        if local: orbit_survivors.append({'orbit_index':idx,'orbit_size':orbit,'t':t,'target_rank':target,'dimension':dim,'representative_section_survivors':local})
    return {'skeleton_orbits':len(source['orbit_representatives']),'representative_sections_checked':total_rep,'weighted_H_checked':total_weighted,'representative_section_survivors':surv_rep,'weighted_H_survivors':surv_weighted,'theta_rank_histogram':{str(k):v for k,v in sorted(rank_hist.items())},'target_vs_rank_histogram':{f'{a}:{b}':v for (a,b),v in sorted(target_hist.items())},'affine_dimension_histogram':{str(k):v for k,v in sorted(dim_hist.items())},'surviving_orbit_records':orbit_survivors}

out1=process('k1',sources['k1'],pre['k1']); out2=process('k2',sources['k2'],pre['k2'])
if out1['representative_sections_checked']!=142032 or out2['representative_sections_checked']!=878848: raise SystemExit('representative section coverage regression')
if out1['weighted_H_checked']!=2928832 or out2['weighted_H_checked']!=11866112: raise SystemExit('weighted integral-action predecessor regression')
cert={'schema':'STAGE33_07_NONELEMENTARY_K12_FULL_Q4_SCOUT_V1','source_integral_action_scout_sha256':INTEGRAL_SCOUT_LOCK,'k1':out1,'k2':out2,'combined_representative_sections_checked':out1['representative_sections_checked']+out2['representative_sections_checked'],'combined_weighted_H_checked':out1['weighted_H_checked']+out2['weighted_H_checked'],'combined_weighted_H_survivors':out1['weighted_H_survivors']+out2['weighted_H_survivors'],'all_affine_sections_exhausted':True,'fast_or_canonical_traversal_used':False,'planning_only':True,'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest(); (HERE/'nonelementary-k12-full-q4-scout.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1_survivors':out1['weighted_H_survivors'],'k2_survivors':out2['weighted_H_survivors'],'combined_survivors':cert['combined_weighted_H_survivors'],'representative_sections_checked':cert['combined_representative_sections_checked'],'sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
