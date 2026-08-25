#!/usr/bin/env python3
"""Exact Q[2] cc/joint-V4 reduction of the elementary index-512 census.

For Q=H^perp/H, the endpoint requires
  dim_F2 Fix(cc,Q[2]) = 10,
  dim_F2 Fix(<cc,ct>,Q[2]) = 9.
This shard counts those conditions on every elementary H surviving the full ct
fixed type and forced mixed-piece commutator filters.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACT=json.loads((HERE/'coordinate-k3-scaled-action-choices-retained.json').read_text())
TGT=json.loads((HERE/'target-discriminant-v4-fixed-module.json').read_text())
COMM=json.loads((HERE/'elementary-index512-forced-commutator-reduction.json').read_text())
if ACT['canonical_sha256']!='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20':raise SystemExit('scaled action lock moved')
if TGT['canonical_sha256']!='a396d928ebe2a9dbc7b04aaf38b9fa30c3ef9366b1a2050409195642a690da88':raise SystemExit('target V4 lock moved')
if COMM['after_forced_commutator']!=423168:raise SystemExit('forced-commutator census regression')
if TGT['cc_fixed_subgroup']['two_torsion_order_log2']!=10:raise SystemExit('target cc Q2 regression')
if TGT['joint_v4_fixed_subgroup']['two_torsion_order_log2']!=9:raise SystemExit('target joint Q2 regression')
if ACT['pieces']['kb']['cc_actions']!=[[[0,7],[7,0]],[[4,7],[7,4]],[[0,1],[1,0]],[[4,1],[1,4]]]:raise SystemExit('Kb cc extension lock moved')
if ACT['pieces']['kc']['cc_actions']!=[[[7,0],[0,1]],[[7,8],[4,1]]]:raise SystemExit('Kc cc extension lock moved')
if ACT['pieces']['ka']['cc_actions']!=[[[1,0],[0,15]],[[1,8],[4,15]]]:raise SystemExit('Ka cc extension lock moved')

# On Q[2], the Kb diagonal-4 choice has zero half-lift effect and changing
# the Kb swap sign changes the half-lift cocycle only by D=im(cc-I) on V.
# Kc/Ka off-diagonal extension differences vanish on halves of V=A0[2].
# Hence the fixed dimensions below are independent of all 1024 scaled cc
# extension choices.  Only the extension-independent A0[2] swap action and
# the cocycle modulo H+D are relevant.

# F2 toolkit.
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
    if k&1:x^=3
    if k&2:x^=12
    if k&4:x^=48
    for j in range(4):
        if (k>>(3+j))&1:x^=1<<(6+j)
    return x
def TtoX(b):
    x=0
    if b&1:x^=1
    if b&2:x^=4
    if b&4:x^=16
    return x
def Ncc(x):
    y=0
    for u,v in ((0,1),(2,3),(4,5)):
        if ((x>>u)^(x>>v))&1:y|=(1<<u)|(1<<v)
    return y
def rad_basis(P):return intersection(P,nullspace_basis(P,10))
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
def quotient_coordinates(P,NP):
    B=list(canon(NP));U=[];cur=list(B)
    for p in canon(P):
        if rank(cur+[p])>len(cur):cur.append(p);U.append(p)
    if len(cur)!=len(P):raise SystemExit('quotient basis construction failed')
    mp={}
    for m in range(1<<len(cur)):
        x=0
        for i,v in enumerate(cur):
            if (m>>i)&1:x^=v
        mp[x]=m
    if len(mp)!=64:raise SystemExit('P coordinate map regression')
    return len(B),len(U),mp
def dot(x,y):return (x&y).bit_count()&1
def Sbasis(t):return tuple(x<<10 for x in nullspace_basis([t],4))
def jt(t):return sum(((t>>i)&1)<<(6+i) for i in range(4))
EVEN_T=[t for t in range(1,16) if t.bit_count()%2==0]
D=(3,12,48) # im(cc-I) on V=A0[2]

def Fcc(h):
    # Half-lift cc cocycle modulo D: Kc contributes X6; Ka contributes Y11..13.
    out=((h>>6)&1)<<6
    for j in (11,12,13):
        if (h>>j)&1:out|=1<<j
    return out

pair_counts=Counter();pair_by_b=Counter();total=0
for P,b in invariant_P(6):
    R=rad_basis(P)
    if len(R)!=2:continue
    NP=canon([Ncc(x) for x in P])
    if len(NP)!=b:raise SystemExit('N(P) dimension regression')
    qstart,m,cmap=quotient_coordinates(P,NP)
    allowed_t=[t for t in EVEN_T if contains(P,jt(t))] # forced commutator filter
    if not allowed_t:continue
    dmask=[dm for dm in range(1,1<<m) if any((((cmap[r]>>qstart)&dm).bit_count()&1) for r in R)] # full ct type
    K=canon([p for p in span(P) if Ncc(p)==0])
    if len(K)!=6-b:raise SystemExit('P fixed-space dimension regression')
    Pb=list(canon(P));pc=[cmap[p]>>qstart for p in Pb];kc=[cmap[k]>>qstart for k in K]
    for t in allowed_t:
        J=jt(t);sb=Sbasis(t);ybit=1<<(10+((t&-t).bit_length()-1))
        pell=[dot(p,J) for p in Pb];kell=[dot(k,J) for k in K]
        for dm in dmask:
            total+=1
            # lambda = delta + ell gives the graph H={(p,y):t.y=lambda(p)}.
            lp=[e^((u&dm).bit_count()&1) for e,u in zip(pell,pc)]
            H=[p|(ybit if v else 0) for p,v in zip(Pb,lp)]+list(sb)
            if rank(H)!=9:raise SystemExit('H rank regression')
            HD=H+list(D);rHD=rank(HD);kN=14-rHD
            lk=[e^((u&dm).bit_count()&1) for e,u in zip(kell,kc)]
            Hsig=[k|(ybit if v else 0) for k,v in zip(K,lk)]+list(sb)
            FH=[Fcc(h) for h in Hsig]
            rcc=rank(HD+FH)-rHD
            ecc=len(Hsig)-rcc
            ccfix=ecc+kN
            # ct fixes a Q[2] class precisely when delta(p)=0.  Restrict that
            # one functional to Hsig and append it as an independent tagged
            # coordinate to the cc compatibility map.
            db=[((u&dm).bit_count()&1) for u in kc]+[0]*len(sb)
            aug=[FH[i]|(db[i]<<14) for i in range(len(Hsig))]
            rjoint=rank(HD+aug)-rHD
            ejoint=len(Hsig)-rjoint
            jointfix=ejoint+kN
            pair_counts[(ccfix,jointfix)]+=1
            pair_by_b[(b,ccfix,jointfix)]+=1
if total!=423168:raise SystemExit(f'input census reconstruction regression {total}')
expected=Counter({(10,9):161792,(10,10):40192,(11,10):87936,(11,11):8832,(9,9):52224,(9,8):47616,(12,11):24576})
if pair_counts!=expected:raise SystemExit(f'Q2 V4 signature census regression {pair_counts}')
expected_by_b=Counter({
 (0,12,11):18816,
 (1,10,9):139008,(1,10,10):12288,(1,11,10):77184,(1,11,11):3456,(1,12,11):5760,
 (2,9,8):47616,(2,9,9):52224,(2,10,9):22784,(2,10,10):27904,(2,11,10):10752,(2,11,11):5376,
})
if pair_by_b!=expected_by_b:raise SystemExit(f'Q2 V4 by-b census regression {pair_by_b}')
after=pair_counts[(10,9)]
if after!=161792:raise SystemExit('target Q2 V4 survivor regression')
cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_Q2_V4_REDUCTION_V1',
 'source_locks':{'scaled_action_choices_sha256':ACT['canonical_sha256'],'target_v4_fixed_module_sha256':TGT['canonical_sha256'],'forced_commutator_reduction_sha256':COMM['canonical_sha256']},
 'scaled_cc_raw_choice_count':1024,
 'q2_cc_and_joint_fixed_dimensions_independent_of_scaled_extension_choice':True,
 'target_cc_Q2_fixed_dimension':10,'target_joint_v4_Q2_fixed_dimension':9,
 'before_q2_v4_filter':423168,
 'cc_Q2_fixed_dimension_census':{str(k):sum(n for (c,j),n in pair_counts.items() if c==k) for k in sorted({c for c,j in pair_counts})},
 'cc_joint_Q2_dimension_pair_census':{f'{c},{j}':n for (c,j),n in sorted(pair_counts.items())},
 'target_cc_Q2_survivors':sum(n for (c,j),n in pair_counts.items() if c==10),
 'target_cc_and_joint_Q2_survivors':after,
 'target_survivors_by_b':{str(b):pair_by_b[(b,10,9)] for b in (0,1,2)},
 'all_elementary_order512_glue_rejected':False,'actual_index512_glue_identified':False,'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'next_exact_leaf':'L33-07-CENSUS-161792-ELEMENTARY-H-BY-FULL-CC-JOINT-FIXED-TYPE-FINITE-Q-FORM-AND-SIMULTANEOUS-V4-CONJUGACY',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-GLUE-161792-FULL-CC-JOINT-Q-V4-CENSUS-PLUS-NONELEMENTARY-GLUE',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-q2-v4-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'before':423168,'cc_Q2_target':cert['target_cc_Q2_survivors'],'joint_Q2_target':after,'pair_census':cert['cc_joint_Q2_dimension_pair_census'],'target_by_b':cert['target_survivors_by_b'],'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
