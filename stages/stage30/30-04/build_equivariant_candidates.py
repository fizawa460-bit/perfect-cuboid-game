#!/usr/bin/env python3
"""Build Stage30-04 finite arrangement/modular S4 equivariant candidates."""
from itertools import product, combinations, permutations
from pathlib import Path
import json

A4=("A1","A2","A3","C"); A3=("B1","B2","B3")
M4=("h0","h1","h2","h3"); M3=("v0","v1","v2")
A7=A4+A3; M7=M4+M3
sA={"A1":"A2","A2":"A1","A3":"A3","C":"C","B1":"B2","B2":"B1","B3":"B3"}
tA={"A1":"A2","A2":"A3","A3":"C","C":"A1","B1":"B3","B2":"B2","B3":"B1"}

def compose(p,q,X): return {x:p[q[x]] for x in X}
def ident(X): return {x:x for x in X}
def pclosure(gens,X):
    key=lambda p:tuple(p[x] for x in X)
    e=ident(X); seen={key(e):e}; q=[e]
    while q:
        a=q.pop()
        for g in gens:
            b=compose(g,a,X); k=key(b)
            if k not in seen: seen[k]=b; q.append(b)
    return list(seen.values())

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%4 for j in range(2)) for i in range(2))
def neg(A): return tuple(tuple((-x)%4 for x in r) for r in A)
def canon(A): return min(A,neg(A),key=lambda z:sum(z,()))
I=((1,0),(0,1)); S=canon(((0,3),(1,0))); T=canon(((1,1),(0,1)))
SL=[((a,b),(c,d)) for a,b,c,d in product(range(4),repeat=4) if (a*d-b*c)%4==1]
G=sorted({canon(A) for A in SL},key=lambda z:sum(z,()))
ix={g:i for i,g in enumerate(G)}
mul=[[ix[canon(mm(a,b))] for b in G] for a in G]
e=ix[canon(I)]
inv={}
for a in range(24):
    inv[a]=next(b for b in range(24) if mul[a][b]==e and mul[b][a]==e)
V=[ix[g] for g in G if tuple(tuple(x%2 for x in r) for r in g)==((1,0),(0,1))]
O3=sorted(set(V)-{e})
def subclose(gs):
    H={e,*gs}
    while True:
        N=set(H)
        for a in tuple(H):
            for b in tuple(H): N.add(mul[a][b])
        if N==H:return frozenset(H)
        H=N
subs={subclose(gs) for r in (1,2) for gs in combinations(range(24),r)}
Hs=sorted([H for H in subs if len(H)==6 and set(H)&set(V)=={e}],key=lambda H:tuple(sorted(H)))
assert len(Hs)==4
hi={H:i for i,H in enumerate(Hs)}
def cj(g,h):return mul[mul[g][h]][inv[g]]
def a3(g):return {f"v{i}":f"v{O3.index(cj(g,h))}" for i,h in enumerate(O3)}
def a4(g):
    out={}
    for i,H in enumerate(Hs):
        K=frozenset(cj(g,h) for h in H); out[f"h{i}"]=f"h{hi[K]}"
    return out
sM={**a4(ix[S]),**a3(ix[S])}; tM={**a4(ix[T]),**a3(ix[T])}
GA=pclosure([sA,tA],A7); GM=pclosure([sM,tM],M7)
assert len(GA)==len(GM)==24
by4={tuple(g[x] for x in M4):g for g in GM}
def invmap(f):return {v:k for k,v in f.items()}
def tr(a,f,target):
    fi=invmap(f); return {y:f[a[fi[y]]] for y in target}

rows=[]
for p4 in permutations(M4):
    f4=dict(zip(A4,p4)); phi=[]
    for a in GA:
        z=tr({x:a[x] for x in A4},f4,M4)
        g=by4.get(tuple(z[x] for x in M4))
        if g is None: break
        phi.append(g)
    if len(phi)!=24:continue
    for p3 in permutations(M3):
        f3=dict(zip(A3,p3))
        if all(tr({x:a[x] for x in A3},f3,M3)=={x:g[x] for x in M3}
               for a,g in zip(GA,phi)):
            rows.append((tuple(f4[x] for x in A4),tuple(f3[x] for x in A3)))
rows=sorted(rows)
assert len(rows)==24
candidates=[]
for i,(p4,p3) in enumerate(rows):
    candidates.append({"candidate_id":f"qicand-{i:02d}","omega4_image":list(p4),
                       "omega3_image":list(p3),"C_image":p4[3]})
counts={h:sum(c["C_image"]==h for c in candidates) for h in M4}
assert counts=={"h0":6,"h1":6,"h2":6,"h3":6}
canonical=next(c["candidate_id"] for c in candidates
               if c["omega4_image"]==["h3","h2","h0","h1"]
               and c["omega3_image"]==["v0","v1","v2"])
out={
 "schema":"STAGE30_04_QI_FINITE_EQUIVARIANT_CANDIDATES_V1",
 "source_stage":"30-02C_AUDITED_TASK_A",
 "source_geometric_anchor_proved":False,
 "q_descent_credit":False,
 "omega4_source_order":list(A4),"omega3_source_order":list(A3),
 "omega4_target_order":list(M4),"omega3_target_order":list(M3),
 "candidate_count":24,"candidate_count_by_C_image":counts,
 "canonical_generator_matched_candidate":canonical,
 "canonical_generator_match":{"s_arr_to":"S_mod","t_arr_to":"T_mod",
   "omega4_image":["h3","h2","h0","h1"],"omega3_image":["v0","v1","v2"]},
 "candidates":candidates,
 "firewalls":{"abstract_S4_isomorphism_is_geometric_adapter":False,
   "finite_equivariance_implies_QI_geometric_anchor":False,
   "finite_equivariance_implies_Q_descent":False,"defect_elimination_count":0,
   "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
Path(__file__).with_name("equivariant-candidates.json").write_text(
    json.dumps(out,indent=2,sort_keys=True)+"\n")
print("SURVIVING_EQUIVARIANT_IDENTIFICATION_COUNT=24")
print("CANONICAL_GENERATOR_MATCHED_CANDIDATE="+canonical)
print("SOURCE_GEOMETRIC_ANCHOR_PROVED=false")
