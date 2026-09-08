#!/usr/bin/env python3
import json
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = json.loads((ROOT / "stages/stage32-ex4/ex4-r3-kuusalo-second-generator-pair-preflight-scratch.json").read_text())
R2 = json.loads((ROOT / "stages/stage32-ex4/ex4-r2-kuusalo-period-to-retained-b5-lattice-adapter-preflight-scratch.json").read_text())

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def neg(A): return [[-x for x in row] for row in A]
def key(A): return tuple(tuple(row) for row in A)
def mpow(A,n):
    R=eye(len(A))
    for _ in range(n): R=mm(R,A)
    return R

def inv_unimodular(A):
    n=len(A); M=[list(map(int,A[i]))+eye(n)[i] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if abs(M[i][c])==1)
        M[c],M[p]=M[p],M[c]
        if M[c][c]==-1: M[c]=[-x for x in M[c]]
        for i in range(n):
            if i==c: continue
            q=M[i][c]
            if q: M[i]=[M[i][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def mv(A,v): return [sum(A[i][j]*v[j] for j in range(4)) for i in range(4)]
def mod2(v): return tuple(x%2 for x in v)

S = [[1,1,0,-2],[0,-1,0,0],[0,1,1,1],[0,0,0,-1]]
T = [[1,1,0,0],[-1,0,0,0],[0,0,1,1],[0,0,-1,0]]
U = [[1,1,0,-2],[0,-2,1,1],[0,1,0,0],[0,0,0,-1]]
Ui = inv_unimodular(U)
f1 = [[1,1,-1,0],[0,-1,1,-1],[1,0,1,-1],[1,1,0,-1]]
f2 = [[0,0,0,-1],[0,0,-1,1],[1,1,-1,0],[1,0,0,-1]]
G0 = [[0,1,0,0],[-1,-1,1,0],[-1,-1,0,1],[-1,0,0,0]]

assert mpow(f1,4)==neg(eye(4))
assert mpow(f1,8)==eye(4)
assert mpow(f2,3)==eye(4)
assert mpow(mm(f1,f2),2)==eye(4)

grp={key(eye(4)):eye(4)}
q=deque([eye(4)])
while q:
    g=q.popleft()
    for a in (S,T):
        h=mm(g,a)
        if key(h) not in grp:
            grp[key(h)]=h; q.append(h)
assert len(grp)==48

def ginv(g):
    I=eye(4)
    for h in grp.values():
        if mm(g,h)==I and mm(h,g)==I: return h
    raise AssertionError("inverse not found")

Hd=[mm(mm(Ui,g),U) for g in grp.values()]
adapters=[mm(H,G0) for H in Hd]
assert len({key(x) for x in adapters})==48

def conj_raw(G,F):
    Gi=inv_unimodular(G)
    return mm(mm(mm(mm(U,G),F),Gi),Ui)

Ti=mpow(T,5)
A=mm(S,Ti)
B=neg(T)
assert mpow(A,8)==eye(4)
assert mpow(B,3)==eye(4)
assert mpow(mm(A,B),2)==eye(4)

v=[1,1,1,1]
lines={(0,0,1,0):"L1",(0,0,0,1):"L2",(0,0,1,1):"L3"}
pairs=Counter(); adapter_lines=Counter(); first=Counter(); second=Counter()
Aonly=[]; Bonly=[]; both=[]
for G in adapters:
    M1=conj_raw(G,f1); M2=conj_raw(G,f2)
    p=(key(M1),key(M2)); pairs[p]+=1
    first[key(M1)]+=1; second[key(M2)]+=1
    line=lines[mod2(mv(mm(U,G),v))]
    adapter_lines[line]+=1
    if M1==A: Aonly.append(line)
    if M2==B: Bonly.append(line)
    if M1==A and M2==B: both.append(line)

assert len(pairs)==24 and set(pairs.values())=={2}
assert len(first)==6 and set(first.values())=={8}
assert len(second)==8 and set(second.values())=={6}
assert adapter_lines==Counter({"L1":16,"L2":16,"L3":16})
assert len(Aonly)==8 and Counter(Aonly)==Counter({"L2":8})
assert len(Bonly)==6 and Counter(Bonly)==Counter({"L1":2,"L2":2,"L3":2})
assert len(both)==2 and Counter(both)==Counter({"L2":2})

orbit=set()
for h in grp.values():
    hi=ginv(h)
    orbit.add((key(mm(mm(h,A),hi)), key(mm(mm(h,B),hi))))
assert orbit==set(pairs)

pair_lines=Counter()
for p in pairs:
    ls=set()
    for G in adapters:
        M1=conj_raw(G,f1); M2=conj_raw(G,f2)
        if (key(M1),key(M2))==p:
            ls.add(lines[mod2(mv(mm(U,G),v))])
    assert len(ls)==1
    pair_lines[next(iter(ls))]+=1
assert pair_lines==Counter({"L1":8,"L2":8,"L3":8})

assert R2["canonical_sha256_without_this_field"] == ART["prior_r2"]["canonical_sha256"]
assert ART["source_pair"]["relations"]["generated_group_order"] == 48
assert ART["simultaneous_transport_across_r2_adapters"]["distinct_ordered_target_pairs"] == 24
assert ART["simultaneous_transport_across_r2_adapters"]["delta_line_counts_across_24_projective_pairs"] == {"L1":8,"L2":8,"L3":8}
assert ART["literal_constraints"]["fix_both"]["conditional_residue"] == 97
assert ART["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert ART["decision"]["Q602_excluded"] is False
assert ART["decision"]["O210_excluded"] is False

print("Stage32EX4 R3 Kuusalo second-generator pair preflight: PASS")
print("source_group=48 target_pair_orbit=24 multiplicity=2 projective_line_counts=8/8/8")
print("literal_A_only=8->L2; literal_B_only=6->2/2/2; literal_pair=2->L2 conditional_residue=97 absolute=false")
