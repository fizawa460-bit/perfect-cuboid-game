#!/usr/bin/env python3
"""Independent verifier for Stage30-04 finite equivariant candidate certificate."""
from itertools import product, combinations, permutations
from pathlib import Path
import json
C=json.loads(Path(__file__).with_name("equivariant-candidates.json").read_text())
A4=("A1","A2","A3","C"); A3=("B1","B2","B3")
M4=("h0","h1","h2","h3"); M3=("v0","v1","v2")
A7=A4+A3; M7=M4+M3
sA={"A1":"A2","A2":"A1","A3":"A3","C":"C","B1":"B2","B2":"B1","B3":"B3"}
tA={"A1":"A2","A2":"A3","A3":"C","C":"A1","B1":"B3","B2":"B2","B3":"B1"}
def cp(p,q,X):return {x:p[q[x]] for x in X}
def cl(gs,X):
    key=lambda p:tuple(p[x] for x in X); e={x:x for x in X}
    D={key(e):e};Q=[e]
    while Q:
        a=Q.pop()
        for g in gs:
            b=cp(g,a,X);k=key(b)
            if k not in D:D[k]=b;Q.append(b)
    return list(D.values())
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%4 for j in range(2)) for i in range(2))
def ng(A):return tuple(tuple((-x)%4 for x in r) for r in A)
def ca(A):return min(A,ng(A),key=lambda z:sum(z,()))
I=((1,0),(0,1));S=ca(((0,3),(1,0)));T=ca(((1,1),(0,1)))
SL=[((a,b),(c,d)) for a,b,c,d in product(range(4),repeat=4) if (a*d-b*c)%4==1]
G=sorted({ca(A) for A in SL},key=lambda z:sum(z,()));ix={g:i for i,g in enumerate(G)}
mul=[[ix[ca(mm(a,b))] for b in G] for a in G];e=ix[ca(I)]
iv={a:next(b for b in range(24) if mul[a][b]==e and mul[b][a]==e) for a in range(24)}
V=[ix[g] for g in G if tuple(tuple(x%2 for x in r) for r in g)==((1,0),(0,1))]
O3=sorted(set(V)-{e})
def sc(gs):
    H={e,*gs}
    while True:
        N=set(H)
        for a in tuple(H):
            for b in tuple(H):N.add(mul[a][b])
        if N==H:return frozenset(H)
        H=N
subs={sc(gs) for r in (1,2) for gs in combinations(range(24),r)}
Hs=sorted([H for H in subs if len(H)==6 and set(H)&set(V)=={e}],key=lambda H:tuple(sorted(H)))
assert len(Hs)==4;hi={H:i for i,H in enumerate(Hs)}
def cj(g,h):return mul[mul[g][h]][iv[g]]
def a3(g):return {f"v{i}":f"v{O3.index(cj(g,h))}" for i,h in enumerate(O3)}
def a4(g):
    d={}
    for i,H in enumerate(Hs):
        K=frozenset(cj(g,h) for h in H);d[f"h{i}"]=f"h{hi[K]}"
    return d
sM={**a4(ix[S]),**a3(ix[S])};tM={**a4(ix[T]),**a3(ix[T])}
GA=cl([sA,tA],A7);GM=cl([sM,tM],M7);assert len(GA)==len(GM)==24
by4={tuple(g[x] for x in M4):g for g in GM}
def im(f):return {v:k for k,v in f.items()}
def tr(a,f,TG):
    fi=im(f);return {y:f[a[fi[y]]] for y in TG}
fresh=[]
for p4 in permutations(M4):
    f4=dict(zip(A4,p4));phi=[]
    for a in GA:
        z=tr({x:a[x] for x in A4},f4,M4)
        g=by4.get(tuple(z[x] for x in M4))
        if g is None:break
        phi.append(g)
    if len(phi)!=24:continue
    for p3 in permutations(M3):
        f3=dict(zip(A3,p3))
        if all(tr({x:a[x] for x in A3},f3,M3)=={x:g[x] for x in M3}
               for a,g in zip(GA,phi)):
            fresh.append((tuple(p4),tuple(p3)))
fresh=sorted(fresh)
stored=sorted((tuple(c["omega4_image"]),tuple(c["omega3_image"])) for c in C["candidates"])
assert fresh==stored and len(fresh)==C["candidate_count"]==24
counts={h:sum(c["C_image"]==h for c in C["candidates"]) for h in M4}
assert counts==C["candidate_count_by_C_image"]=={"h0":6,"h1":6,"h2":6,"h3":6}
assert C["canonical_generator_matched_candidate"]=="qicand-22"
assert C["source_geometric_anchor_proved"] is False and C["q_descent_credit"] is False
assert C["firewalls"]["defect_elimination_count"]==0
print("EXHAUSTIVE_4x3_BIJECTION_SEARCH=PASS")
print("SURVIVING_EQUIVARIANT_IDENTIFICATION_COUNT=24")
print("C_IMAGE_MULTIPLICITIES=h0:6,h1:6,h2:6,h3:6")
print("SOURCE_GEOMETRIC_ANCHOR_PROVED=false")
