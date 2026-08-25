#!/usr/bin/env python3
"""Exact full-ct fixed-subgroup reduction for all elementary index-512 glue.

Starting from the exact structural census, this shard upgrades the ct[2]-only
filter to the complete fixed-subgroup type on Q=H^perp/H.  It counts H, not
scaled action choices.  A positive survivor remains only a candidate: the
finite quadratic form, cc/joint fixed types, simultaneous V4 conjugacy, and
non-elementary order-512 glue are still open.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
H0=json.loads((HERE/'elementary-index512-glue-candidate.json').read_text())
H0V4=json.loads((HERE/'elementary-index512-candidate-v4-rejection-retained.json').read_text())
STRUCT=json.loads((HERE/'elementary-index512-structural-reduction.json').read_text())

if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20': raise SystemExit('scaled action choices lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88': raise SystemExit('target V4 fixed lock moved')
if STRUCT['canonical_sha256']!='5b0ef2f83adb76eec3030e233c524cbfd7737dcbee361e9185ec0b741d6e93c3': raise SystemExit('structural reduction lock moved')
if H0V4['source_certificate_canonical_sha256']!='b9eb4a02564fc47cc99e234107fa6a6affc2d7021c4fa8b0488385c6cb2ed183': raise SystemExit('H0 exact V4 regression lock moved')
target=(int(TGT['ct_fixed_subgroup']['two_torsion_order_log2']),int(TGT['ct_fixed_subgroup']['four_torsion_order_log2']),int(TGT['ct_fixed_subgroup']['order_log2']))
if target!=(13,19,22): raise SystemExit('target ct fixed signature regression')
if STRUCT['elementary_candidates_after_ct_fixed_two_torsion_total']!=3782165: raise SystemExit('structural survivor census regression')

# Small exact F2 toolkit. Vectors are integers with bit coordinates.
def rank(vs):
    piv={}
    for x in vs:
        y=int(x)
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:piv[p]=y;break
    return len(piv)
def canon(vs):
    piv={}
    for x in vs:
        y=int(x)
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:
                for q in list(piv):
                    if (piv[q]>>p)&1:piv[q]^=y
                piv[p]=y;break
    return tuple(piv[p] for p in sorted(piv,reverse=True))
def contains(B,x):return rank(list(B)+[x])==len(B)
def span(B):
    B=list(B)
    for m in range(1<<len(B)):
        x=0
        for i,b in enumerate(B):
            if (m>>i)&1:x^=b
        yield x
def rref_subspaces(n,k):
    if k==0:
        yield ();return
    for pivots in itertools.combinations(range(n),k):
        ps=set(pivots);free=[j for j in range(n) if j not in ps]
        slots=[(r,j) for j in free for r,p in enumerate(pivots) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in pivots]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:rows[r]|=1<<j
            yield canon(rows)
def extend_basis(B,n):
    cur=list(canon(B));out=[]
    for i in range(n):
        e=1<<i
        if rank(cur+[e])>len(cur):cur.append(e);out.append(e)
    return out
def nullspace_basis(rows,n):
    A=[int(r) for r in rows if r];r=0;piv=[]
    for c in range(n):
        z=next((i for i in range(r,len(A)) if (A[i]>>c)&1),None)
        if z is None:continue
        A[r],A[z]=A[z],A[r]
        for i in range(len(A)):
            if i!=r and ((A[i]>>c)&1):A[i]^=A[r]
        piv.append(c);r+=1
        if r==len(A):break
    A=A[:r];free=[c for c in range(n) if c not in piv];out=[]
    for f in free:
        x=1<<f
        for row,p in zip(A,piv):
            if (row>>f)&1:x|=1<<p
        out.append(x)
    out=canon(out)
    if any(any((x&row).bit_count()%2 for row in rows) for x in out):raise SystemExit('nullspace verification failed')
    return out
def intersection(A,B):
    B=canon(B)
    return canon([x for x in span(canon(A)) if contains(B,x)])

def KtoX(k):
    x=0
    if k&1:x^=(1<<0)|(1<<1)
    if k&2:x^=(1<<2)|(1<<3)
    if k&4:x^=(1<<4)|(1<<5)
    for j in range(4):
        if (k>>(3+j))&1:x^=1<<(6+j)
    return x
def TtoX(b):
    x=0
    if b&1:x^=1<<0
    if b&2:x^=1<<2
    if b&4:x^=1<<4
    return x
def Ncc(x):
    y=0
    for u,v in ((0,1),(2,3),(4,5)):
        if ((x>>u)^(x>>v))&1:y|=(1<<u)|(1<<v)
    return y
def rad_basis(P):return intersection(P,nullspace_basis(P,10))
def rad_dim(P):return len(rad_basis(P))
def invariant_P(d):
    seen=set()
    for b in range(4):
        if d-b<b:continue
        for B in rref_subspaces(3,b):
            comp=extend_basis(B,7);qdim=d-2*b
            if not (0<=qdim<=len(comp)):continue
            for Cq in rref_subspaces(len(comp),qdim):
                C=[]
                for cv in Cq:
                    z=0
                    for j,q in enumerate(comp):
                        if (cv>>j)&1:z^=q
                    C.append(z)
                A=list(canon(list(B)+C));acomp=extend_basis(A,7);slots=b*len(acomp)
                for mask in range(1<<slots):
                    lifts=[]
                    for i,bb in enumerate(B):
                        z=0
                        for j,q in enumerate(acomp):
                            if (mask>>(i*len(acomp)+j))&1:z^=q
                        lifts.append(TtoX(bb)^KtoX(z))
                    P=canon([KtoX(a) for a in A]+lifts)
                    if P in seen:raise SystemExit('duplicate invariant P')
                    seen.add(P);yield P,b

def kb_map(x,mask):
    y=0
    for j,(u,v) in enumerate(((0,1),(2,3),(4,5))):
        if (mask>>j)&1:
            if (x>>u)&1:y|=1<<v
            if (x>>v)&1:y|=1<<u
    return y
def allowed_dim(P,mask):
    B=nullspace_basis(P,10)
    imgs=[kb_map(x,mask) for x in B]
    return len(B)-(rank(list(P)+imgs)-len(P))
def good_dim(P,R,delta_kernel_basis,mask):
    # a must lie in R, in ker(delta), and satisfy K_mask(a) in P.
    D=intersection(R,delta_kernel_basis)
    imgs=[kb_map(x,mask) for x in D]
    return len(D)-(rank(list(P)+imgs)-len(P))

# Fixed-subgroup formulas.  For s=dim(H cap Y), d=dim P=9-s:
#   log2 |Fix(ct,Q)|    = 15+s+dim A_t,
#   log2 |Fix(ct,Q)[4]|= 15+s+dim G_t,
# where A_t={a in P^perp: K_t(a) in P} and
# G_t={a in rad(P): delta(a)=0, K_t(a) in P}.
# The ct[2] filter already enforces rank(delta)=1 and gives log2=13.
# Since dim(P^perp)=s+1, s=2 has total fixed order <=2^20, so it can
# never match the endpoint total order 2^22.
s2_before=int(STRUCT['elementary_candidates_after_ct_fixed_two_torsion_by_s']['2'])
if s2_before!=365157:raise SystemExit('s2 structural count regression')
s2_after_full_ct=0

# For s=3, P has dimension 6 and rad(P) dimension 2.  The identity Kb choice
# has A_t=P^perp of dimension 4, so the endpoint total order is attainable.
# Any matching Kb choice must have dim A_t=4.  Then G_t=rad(P) cap ker(delta),
# and endpoint |Fix[4]|=2^19 is equivalent to delta being nonzero on rad(P).
# delta is an arbitrary nonzero functional on W=P/N(P).  If rbar is the
# dimension of the image of rad(P) in W, the exact number of such functionals
# is 2^m-2^(m-rbar), m=dim W=6-b.
p_stats=Counter();survivors_by_b=Counter();p_total=0
for P,b in invariant_P(6):
    if rad_dim(P)!=2:continue
    p_total+=1
    R=rad_basis(P);NP=canon([Ncc(x) for x in P])
    if len(NP)!=b:raise SystemExit('N(P) dimension regression')
    rbar=2-len(intersection(R,NP));m=6-b
    if rbar not in (1,2):raise SystemExit('unexpected radical image dimension')
    p_stats[(b,rbar)]+=1
    ndelta=(1<<m)-(1<<(m-rbar))
    survivors_by_b[b]+=7*ndelta
if p_total!=24880:raise SystemExit(f's3 target-rad P total regression {p_total}')
expected_p_stats=Counter({(0,2):112,(1,1):3840,(1,2):3008,(2,1):13056,(2,2):4864})
if p_stats!=expected_p_stats:raise SystemExit(f's3 radical-image census regression {p_stats}')
if survivors_by_b!=Counter({0:37632,1:935424,2:1139712}):raise SystemExit(f'full ct survivor by-b regression {survivors_by_b}')
s3_after_full_ct=sum(survivors_by_b.values())
if s3_after_full_ct!=2112768:raise SystemExit(f'full ct s3 survivor regression {s3_after_full_ct}')
if int(STRUCT['elementary_candidates_after_ct_fixed_two_torsion_by_s']['3'])!=3417008:raise SystemExit('s3 structural count regression')

# Independent formula regression against the earlier exact Smith computation
# for explicit H0.  H0 has s=4 and no graph quotient, hence delta=0.  The four
# mixed-piece ct bits do not change these filtration counts; each Kb mask has
# multiplicity 16.  The formula must reproduce the exact retained census.
C=[[int(v)&1 for v in r] for r in H0['candidate_code_basis_f2']]
S0=canon([sum((r[10+j]&1)<<j for j in range(4)) for r in C if not any(r[:10])])
P0=canon([sum((r[j]&1)<<j for j in range(10)) for r in C])
if len(S0)!=4 or len(P0)!=5 or rad_dim(P0)!=1:raise SystemExit('H0 structural regression')
R0=rad_basis(P0);h0sig=Counter()
for mask in range(8):
    ad=allowed_dim(P0,mask)
    gd=len(R0)-(rank(list(P0)+[kb_map(x,mask) for x in R0])-len(P0))
    h0sig[(14,19+gd,19+ad)]+=16
expected_h0=Counter()
for k,v in H0V4['candidate_ct_fixed_signature_census'].items():expected_h0[tuple(int(x) for x in k.split(','))]=int(v)
if h0sig!=expected_h0:raise SystemExit(f'fixed-filtration formula failed H0 exact Smith regression {h0sig}')

before=STRUCT['elementary_candidates_after_ct_fixed_two_torsion_total'];after=s3_after_full_ct
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_FULL_CT_FIXED_TYPE_REDUCTION_V1',
 'source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256'],'structural_reduction_sha256':STRUCT['canonical_sha256'],'h0_exact_v4_certificate_sha256':H0V4['source_certificate_canonical_sha256']},
 'target_ct_fixed_signature_log2_K2_K4_K':list(target),
 'target_ct_fixed_subgroup':TGT['ct_fixed_subgroup']['group'],
 'fixed_filtration_formula_exact':{'K2_log2':'14-rank(delta_H)','K4_log2':'15+s+dim(rad(P) cap ker(delta) cap K_t^-1(P))','K_log2':'15+s+dim(P^perp cap K_t^-1(P))'},
 'formula_independently_regressed_against_exact_H0_smith_census':True,
 'h0_formula_signature_census':{','.join(map(str,k)):v for k,v in sorted(h0sig.items())},
 'elementary_candidates_after_ct2_before_full_ct':before,
 's2_rejected_by_total_ct_fixed_order':True,
 's2_before_full_ct':s2_before,'s2_after_full_ct':s2_after_full_ct,
 's3_radical_image_P_census_by_b_rbar':{f'{b},{r}':n for (b,r),n in sorted(p_stats.items())},
 's3_survivors_after_full_ct_by_b':{str(b):n for b,n in sorted(survivors_by_b.items())},
 's3_after_full_ct':s3_after_full_ct,
 'elementary_candidates_after_full_ct_fixed_type_total':after,
 'reduction_factor_from_ct2':before/after,
 'all_elementary_order512_glue_rejected':False,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-CENSUS-2112768-ELEMENTARY-H-BY-FINITE-Q-FORM-CC-JOINT-V4-AND-SIMULTANEOUS-CONJUGACY',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-2112768-Q-CC-JOINT-V4-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-full-ct-fixed-type-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before_full_ct':before,'s2_rejected':s2_before,'s3_after_full_ct':s3_after_full_ct,'after_full_ct':after,'p_stats':cert['s3_radical_image_P_census_by_b_rbar'],'survivors_by_b':cert['s3_survivors_after_full_ct_by_b'],'h0_formula_regression':True,'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
