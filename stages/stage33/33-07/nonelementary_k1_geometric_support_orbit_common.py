#!/usr/bin/env python3
"""Pure-geometric k=1 support-orbit helpers after exact Q[2]/2Q support.

Only the order-288 integral source-coordinate symmetry is used. No arithmetic
cc/ct action is loaded. The 63 rank-one E7 choices are partitioned into
source-symmetry P-orbits; for a fixed P representative, W is quotiented by the
stabilizer of P. This equals quotienting (P,W) by the full source symmetry,
but avoids materializing all 20,487,593 support skeletons at once.
"""
import itertools
import json
import runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
X_MASK=(1<<10)-1
J=X_MASK

base_ns=runpy.run_path(str(HERE/'certify_nonelementary_sign_q2_structural_reduction.py'))
q8_ns=runpy.run_path(str(HERE/'certify_nonelementary_target_q8_exponent_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_q2_support_reduction.py'))
runpy.run_path(str(HERE/'certify_nonelementary_k12_2q_support_reduction.py'))
twoq=json.loads((HERE/'nonelementary-k12-2q-support-reduction.json').read_text())
if twoq.get('schema')!='STAGE33_07_NONELEMENTARY_K12_2Q_SUPPORT_REDUCTION_V1':
    raise SystemExit('2Q predecessor schema regression')
if twoq['summary_by_number_of_Z4_factors']['1']['structural_H_after_endpoint_2Q_support_necessary_condition']!=1311205952:
    raise SystemExit('k1 2Q predecessor total moved')

subspaces=base_ns['subspaces'];span=base_ns['span'];rank=base_ns['rank'];canon=base_ns['canon'];red_to_full=base_ns['red_to_full'];eqrc=base_ns['eq_rank_and_consistency']
coisotropic=q8_ns['coisotropic']

def contains(B,x):return rank(list(B)+[x])==len(B)
def complement(base,whole):
    cur=list(canon(base));out=[]
    for v in canon(whole):
        if rank(cur+[v])>len(cur):cur.append(v);out.append(v)
    return tuple(out)
def perp(B,n):return canon(x for x in range(1,1<<n) if all((x&b).bit_count()%2==0 for b in B))
def rref_subspaces(n,k):
    if k==0:yield ();return
    for piv in itertools.combinations(range(n),k):
        ps=set(piv);free=[j for j in range(n) if j not in ps];slots=[(r,j) for j in free for r,p in enumerate(piv) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in piv]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:rows[r]|=1<<j
            yield canon(rows)
def ambient_subspaces_containing(base,ambient,target):
    base=canon(base);qb=complement(base,ambient);need=target-len(base)
    for abstract in rref_subspaces(len(qb),need):
        lifted=[]
        for row in abstract:
            v=0
            for j,b in enumerate(qb):
                if (row>>j)&1:v^=b
            lifted.append(v)
        out=canon(base+tuple(lifted))
        if len(out)!=target:raise SystemExit('ambient lift rank regression')
        yield out
def lambda_rep(U):
    T=perp(U,4);sol=[]
    for y in range(16):
        if all(((y&t).bit_count()&1)==((t.bit_count()//2)&1) for t in [0]+[x for x in range(1,16) if contains(T,x)]):sol.append(y)
    if len(sol)!=(1<<len(U)):raise SystemExit('lambda coset regression')
    return min(sol)
def graph_skeletons(dx,R,U):
    y0=lambda_rep(U);base=canon(tuple(dx)+(J,));extra=complement(base,R);ycomp=complement(U,canon(1<<j for j in range(4)))
    slots=[(i,j) for i in range(len(extra)) for j in range(len(ycomp))]
    for mask in range(1<<len(slots)):
        rows=list(dx)+[u<<10 for u in U]+[J|(y0<<10)]
        for i,x in enumerate(extra):
            y=0
            for bit,(ii,j) in enumerate(slots):
                if ii==i and (mask>>bit)&1:y^=ycomp[j]
            rows.append(x|(y<<10))
        W=canon(rows)
        if len(W)!=8:raise SystemExit('k1 W rank regression')
        yield W

def symmetries():
    for kbp in itertools.permutations(range(3)):
        for sm in range(8):
            for kap in itertools.permutations(range(3)):
                p=list(range(14))
                for old in range(3):
                    new=kbp[old];sw=(sm>>old)&1;p[2*old]=2*new+sw;p[2*old+1]=2*new+(1-sw)
                p[6]=6;p[10]=10
                for old in range(3):
                    new=kap[old];p[7+old]=7+new;p[11+old]=11+new
                yield tuple(p)
SYM=tuple(symmetries())
if len(SYM)!=288 or len(set(SYM))!=288:raise SystemExit('source symmetry order regression')
def transport(v,g):
    out=0
    for old,new in enumerate(g):
        if (int(v)>>old)&1:out|=1<<new
    return out

def reduced_from_full(p):
    p=int(p);r=0
    for j in range(3):
        a=(p>>(2*j))&1;b=(p>>(2*j+1))&1
        if a!=b:raise SystemExit('Kb pair left reduced E7 code')
        if a:r|=1<<j
    for j in range(4):
        if (p>>(10+j))&1:r|=1<<(3+j)
    if p!=red_to_full(r):raise SystemExit('full/reduced roundtrip regression')
    return r

def eligible_P():
    out=[]
    for rp in sorted(subspaces[1]):
        supp=0
        for v in span(rp):supp|=v
        if supp.bit_count()>8:continue
        t=rank([v&0b111 for v in rp]);eqrank,ok=eqrc(rp)
        if not ok or t>2 or eqrank!=0:continue
        out.append(red_to_full(rp[0]))
    if len(out)!=63 or len(set(out))!=63:raise SystemExit(f'k1 P universe regression {len(out)}')
    return tuple(sorted(out))
ELIGIBLE_P=eligible_P();ELIGIBLE_SET=set(ELIGIBLE_P)

def p_orbits():
    unseen=set(ELIGIBLE_P);out=[]
    while unseen:
        seed=min(unseen);orb={transport(seed,g) for g in SYM}
        if not orb<=ELIGIBLE_SET:raise SystemExit('P universe not symmetry-stable')
        unseen.difference_update(orb);rep=min(orb);stab=tuple(g for g in SYM if transport(rep,g)==rep)
        if len(orb)*len(stab)!=288:raise SystemExit('P orbit-stabilizer regression')
        out.append((rep,tuple(sorted(orb)),stab))
    out.sort(key=lambda z:z[0])
    if len(out)!=15 or sum(len(z[1]) for z in out)!=63:raise SystemExit(f'P orbit census regression {len(out)}')
    return tuple(out)
P_ORBITS=p_orbits()

def enumerate_W_for_P(p):
    rp=(reduced_from_full(p),);supp=rp[0];t=rank([rp[0]&0b111]);eqrank,ok=eqrc(rp)
    if not ok or eqrank!=0 or t not in (0,1):raise SystemExit('k1 P shape regression')
    pb=canon((int(p),));px=canon(v&X_MASK for v in pb);x0=perp(px,10)
    xe=canon(v for v in range(1,1<<10) if contains(x0,v) and v.bit_count()%2==0)
    dx=canon((1<<(2*j))|(1<<(2*j+1)) for j in range(3) if (supp>>j)&1)
    dy=canon(1<<j for j in range(4) if (supp>>(3+j))&1);base=canon(tuple(dx)+(J,))
    seen=set()
    for U in coisotropic:
        if any(not contains(U,v) for v in dy):continue
        rdim=8-len(U)
        if len(base)>rdim or any(not contains(xe,b) for b in base):continue
        for R in ambient_subspaces_containing(base,xe,rdim):
            for W in graph_skeletons(dx,R,U):
                if not contains(W,p):continue
                if W in seen:raise SystemExit('duplicate W for fixed k1 P')
                seen.add(W)
    return seen
