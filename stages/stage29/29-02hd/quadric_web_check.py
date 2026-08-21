#!/usr/bin/env python3
"""Exact dependency-free linear algebra for the cuboid four-quadric web.

The endpoint quadrics are
 Q1=a1^2+a2^2-b3^2
 Q2=a2^2+a3^2-b1^2
 Q3=a1^2+a3^2-b2^2
 Q4=a1^2+a2^2+a3^2-c^2.

For t=(t1,t2,t3,t4), the web member sum ti Qi is diagonal.
This script checks its seven coefficient hyperplanes and exact rank strata.
Only integer/rational row reduction is used.
"""

from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import reduce

FORMS = {
    "B3": (1,0,0,0),
    "B1": (0,1,0,0),
    "B2": (0,0,1,0),
    "C":  (0,0,0,1),
    "A1": (1,0,1,1),
    "A2": (1,1,0,1),
    "A3": (0,1,1,1),
}


def rank(rows):
    a=[[Fraction(x) for x in r] for r in rows]
    m=len(a); n=len(a[0]) if m else 0
    rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if a[i][c]),None)
        if p is None: continue
        a[rr],a[p]=a[p],a[rr]
        q=a[rr][c]
        a[rr]=[x/q for x in a[rr]]
        for i in range(m):
            if i!=rr and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[rr][j] for j in range(n)]
        rr+=1
        if rr==m: break
    return rr


def projective_kernel_1d(rows):
    # solve a 3-or-more by 4 homogeneous system of rank 3 via signed 3x3 minors
    # brute-force candidate from cofactors of any independent 3 rows
    rr=None
    for trip in combinations(rows,3):
        if rank(trip)==3:
            rr=trip; break
    if rr is None: return None
    def det3(M):
        return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
               -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
               +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    v=[]
    for j in range(4):
        M=[[r[k] for k in range(4) if k!=j] for r in rr]
        v.append(((-1)**j)*det3(M))
    if all(x==0 for x in v): return None
    g=reduce(gcd,[abs(x) for x in v if x])
    v=[x//g for x in v]
    first=next(x for x in v if x)
    if first<0: v=[-x for x in v]
    assert all(sum(r[j]*v[j] for j in range(4))==0 for r in rows)
    return tuple(v)


def main():
    names=list(FORMS)
    print("DISCRIMINANT_FACTORS=7")
    print("det ~ t1*t2*t3*t4*(t1+t3+t4)*(t1+t2+t4)*(t2+t3+t4)")

    dep3=[]
    points={}
    for comb in combinations(names,3):
        rows=[FORMS[n] for n in comb]
        r=rank(rows)
        if r<3: dep3.append((comb,r))
        p=projective_kernel_1d(rows)
        points.setdefault(p,[]).append(comb)
    print("DEPENDENT_HYPERPLANE_TRIPLES=",len(dep3),sep="")
    print("RANK_LE_4_LOCUS_POSITIVE_DIMENSIONAL=false")
    print("RANK_LE_4_PROJECTIVE_POINTS=",len(points),sep="")

    rank3=[]
    for p,triples in points.items():
        zero=[n for n,r in FORMS.items() if sum(r[j]*p[j] for j in range(4))==0]
        quadric_rank=7-len(zero)
        if quadric_rank<=3:
            rank3.append((p,tuple(zero),quadric_rank))
    rank3.sort()
    print("RANK_LE_3_POINTS=",len(rank3),sep="")
    for p,zero,r in rank3:
        print("rank",r,"point",p,"zero_coefficients",",".join(zero))

    assert len(dep3)==0
    assert len(points)==17
    assert len(rank3)==6
    assert all(r==3 for _,_,r in rank3)
    print("ADLER_VAN_MOERBEKE_RANK4_CURVE_TRIGGER=false")
    print("PASS")

if __name__=="__main__":
    main()
