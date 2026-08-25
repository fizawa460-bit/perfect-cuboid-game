#!/usr/bin/env python3
"""Exact forced-commutator reduction of the elementary index-512 census.

The exact endpoint cc and ct actions commute.  On every mixed Kc/Ka scaled
piece, however, all admissible lifts have the same forced commutator
J=[[1,8],[4,1]].  Therefore a candidate elementary glue H can support the
endpoint V4 action only if this commutator is trivial on H^perp/H.

This shard proves and counts that necessary condition over the full census
already surviving the complete ct-fixed subgroup filter.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
FULLCT=json.loads((HERE/'elementary-index512-full-ct-fixed-type-reduction.json').read_text())
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20':raise SystemExit('scaled action choices lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88':raise SystemExit('target V4 lock moved')
for k in ('kc','ka'):
    if ACT['pieces'][k]['forced_commutator']!=[[1,8],[4,1]]:raise SystemExit(f'{k} forced commutator regression')
if not TGT.get('joint_v4_fixed_subgroup_exact'):raise SystemExit('target joint V4 lock missing')
if FULLCT['elementary_candidates_after_full_ct_fixed_type_total']!=2112768:raise SystemExit('full-ct census regression')

# Exact F2 toolkit and the same exhaustive N-stable P parametrization used by
# the preceding structural shards.  Vectors are represented by integers.
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
    return canon(out)
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

# For s=3 every coisotropic S is t^perp for a unique nonzero even-weight
# t in Y=F2^4.  Let j(t) place t in X coordinates 6..9.  The parity action
# of the forced mixed-piece commutator is C(x,y)=(j(y),m(x)).  Writing H as
# the graph of phi:P->Y/S, a direct orthogonality calculation gives
#
#       C(H^perp) subset H  <=>  j(t) in P.
#
# The condition is independent of phi/delta.  Thus for each P the surviving
# number of S is exactly the number of nonzero even t with j(t) in P.
def j_of_t(t):return sum(((t>>i)&1)<<(6+i) for i in range(4))
even_t=[t for t in range(1,16) if t.bit_count()%2==0]
if len(even_t)!=7:raise SystemExit('s3 coisotropic t census regression')

p_stats=Counter();by_b=Counter();by_allowed_S=Counter();Ptotal=0
for P,b in invariant_P(6):
    if rad_dim(P)!=2:continue
    Ptotal+=1;R=rad_basis(P);NP=canon([Ncc(x) for x in P])
    if len(NP)!=b:raise SystemExit('N(P) dimension regression')
    rbar=2-len(intersection(R,NP));m=6-b
    if rbar not in (1,2):raise SystemExit('radical image dimension regression')
    ndelta=(1<<m)-(1<<(m-rbar))
    nS=sum(1 for t in even_t if contains(P,j_of_t(t)))
    if nS not in (0,1,3,7):raise SystemExit(f'unexpected allowed-S count {nS}')
    p_stats[(b,rbar,nS)]+=1
    survivors=nS*ndelta
    by_b[b]+=survivors;by_allowed_S[nS]+=survivors
if Ptotal!=24880:raise SystemExit('target-rad s3 P census regression')
expected=Counter({
 (0,2,3):98,(0,2,7):14,
 (1,1,1):2424,(1,2,1):1984,(1,1,3):1338,(1,2,3):976,(1,1,7):78,(1,2,7):48,
 (2,1,0):3456,(2,1,1):8784,(2,2,1):4096,(2,1,3):816,(2,2,3):768,
})
if p_stats!=expected:raise SystemExit(f'forced-commutator P census regression {p_stats}')
if by_b!=Counter({0:18816,1:237696,2:166656}):raise SystemExit(f'forced-commutator by-b regression {by_b}')
if by_allowed_S!=Counter({0:0,1:205824,3:195840,7:21504}):raise SystemExit(f'forced-commutator allowed-S regression {by_allowed_S}')
after=sum(by_b.values())
if after!=423168:raise SystemExit(f'forced-commutator survivor regression {after}')

cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_FORCED_COMMUTATOR_REDUCTION_V1',
 'source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256'],'full_ct_reduction_sha256':FULLCT['canonical_sha256']},
 'endpoint_cc_ct_commute_exact':True,
 'forced_mixed_piece_commutator':[[1,8],[4,1]],
 'forced_commutator_independent_of_scaled_extension':True,
 's3_commutator_triviality_equivalent_condition':'for S=t^perp with nonzero even t, j(t) belongs to P',
 'condition_independent_of_graph_phi_delta':True,
 'before_forced_commutator':FULLCT['elementary_candidates_after_full_ct_fixed_type_total'],
 's3_P_census_by_b_rbar_allowedS':{f'{b},{r},{s}':n for (b,r,s),n in sorted(p_stats.items())},
 'survivors_by_b':{str(b):n for b,n in sorted(by_b.items())},
 'survivors_by_number_of_allowed_S':{str(s):n for s,n in sorted(by_allowed_S.items())},
 'after_forced_commutator':after,
 'all_elementary_order512_glue_rejected':False,
 'actual_index512_glue_identified':False,
 'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'next_exact_leaf':'L33-07-CENSUS-423168-ELEMENTARY-H-BY-FINITE-Q-FORM-CC-JOINT-FIXED-TYPE-AND-SIMULTANEOUS-V4-CONJUGACY',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-423168-Q-CC-JOINT-V4-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-forced-commutator-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':cert['before_forced_commutator'],'after':after,'survivors_by_b':cert['survivors_by_b'],'allowed_S_weighted':cert['survivors_by_number_of_allowed_S'],'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
