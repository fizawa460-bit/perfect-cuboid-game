#!/usr/bin/env python3
"""Exact abstract type reduction for order-512 isotropic glue H.

Let A0 have 2-group type lambda=(4^4,3^10), endpoint Q type
kappa=(3^4,2^6,1^4), and |H|=2^9. Nondegeneracy plus isotropy gives
  0 -> Hperp -> A0 -> H^* ~= H -> 0
  0 -> H -> Hperp -> Q -> 0.
For a finite abelian p-group exact sequence, type compatibility is equivalent
to positivity of the relevant Littlewood-Richardson coefficient. Since H has
size 9 boxes, both tests can be performed by exact LR-tableau enumeration.
This is an abstract-group necessary filter only; it does not construct an
isotropic embedding or prove a quadratic/action match.
"""
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
LAM=(4,4,4,4)+(3,)*10
KAP=(3,)*4+(2,)*6+(1,)*4

def parts(n,m=None):
    if n==0: yield (); return
    m=min(n,n if m is None else m)
    for a in range(m,0,-1):
        for r in parts(n-a,a): yield (a,)+r

def pad(p,n): return p+(0,)*(n-len(p))
def contained(beta,alpha):
    n=max(len(beta),len(alpha)); b=pad(beta,n); a=pad(alpha,n)
    return all(a[i]<=b[i] for i in range(n))

def lr_positive(alpha,gamma,beta):
    if sum(alpha)+sum(gamma)!=sum(beta) or not contained(beta,alpha): return False
    rows=len(beta); a=pad(alpha,rows); b=pad(beta,rows)
    cells=[(r,c) for r in range(rows) for c in range(b[r],a[r],-1)]
    used=[0]*len(gamma); tab={}
    def rec(k):
        if k==len(cells): return True
        r,c=cells[k]; right=tab.get((r,c+1)); above=tab.get((r-1,c))
        for lab in range(1,len(gamma)+1):
            i=lab-1
            if used[i]>=gamma[i]: continue
            if right is not None and lab>right: continue
            if above is not None and above>=lab: continue
            used[i]+=1
            ok=all(used[j]>=used[j+1] for j in range(len(used)-1))
            if ok:
                tab[(r,c)]=lab
                if rec(k+1): return True
                del tab[(r,c)]
            used[i]-=1
        return False
    return rec(0)

mus=[p for p in parts(9,4) if len(p)<=14]
nus=[p for p in parts(37,4) if len(p)<=14 and contained(LAM,p) and contained(p,KAP)]
if len(mus)!=18: raise SystemExit(f'order512 type census regression {len(mus)}')
if len(nus)!=21: raise SystemExit(f'intermediate type census regression {len(nus)}')
adm={}
for mu in mus:
    w=[nu for nu in nus if lr_positive(nu,mu,LAM) and lr_positive(KAP,mu,nu)]
    if w: adm[mu]=w
expected=[
 (3,3,1,1,1),(3,2,2,1,1),(3,2,1,1,1,1),(3,1,1,1,1,1,1),
 (2,2,2,2,1),(2,2,2,1,1,1),(2,2,1,1,1,1,1),(2,1,1,1,1,1,1,1),
 (1,1,1,1,1,1,1,1,1),
]
if list(adm)!=expected: raise SystemExit(f'admissible H type regression {list(adm)}')
counts={','.join(map(str,k)):len(v) for k,v in adm.items()}
if counts!={'3,3,1,1,1':1,'3,2,2,1,1':3,'3,2,1,1,1,1':5,'3,1,1,1,1,1,1':3,'2,2,2,2,1':5,'2,2,2,1,1,1':11,'2,2,1,1,1,1,1':12,'2,1,1,1,1,1,1,1':9,'1,1,1,1,1,1,1,1,1':5}: raise SystemExit('witness count regression')
rejected=[p for p in mus if p not in adm]
if not all((4 in p) for p in rejected[:6]): pass
cert={
 'schema':'STAGE33_07_INDEX512_ABSTRACT_GLUE_TYPES_LR_V1',
 'ambient_type_partition':list(LAM),'endpoint_quotient_type_partition':list(KAP),
 'order512_abstract_H_type_count_before':18,
 'intermediate_Hperp_type_count_considered':21,
 'abstract_H_types_after_two_exact_sequence_LR_filter':[list(x) for x in expected],
 'abstract_H_type_count_after':9,
 'elementary_type':[1]*9,'non_elementary_type_count_after':8,
 'intermediate_witness_type_counts':counts,
 'all_H_types_with_exponent_16_rejected':all(4 not in x for x in expected),
 'filter_status':'NECESSARY_ABSTRACT_GROUP_TYPE_FILTER_ONLY',
 'isotropic_embedding_constructed':False,'quadratic_form_match_certified':False,'V4_action_match_certified':False,
 'actual_index512_glue_identified':False,
 'next_exact_leaf_non_elementary':'L33-07-CLASSIFY-8-NONELEMENTARY-H-TYPES-BY-ISOTROPIC-EMBEDDING-QUADRATIC-FORM-AND-V4-ACTION',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'index512-abstract-glue-types-lr.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':18,'after':9,'non_elementary_after':8,'all_exponent16_types_rejected':True,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
