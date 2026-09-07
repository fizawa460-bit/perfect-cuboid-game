#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
R_PATH=HERE/"post1648r-b9-b8-ordered-pair-inner-orbit-nonpruning.json"
N_PATH=HERE/"post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
S_PATH=HERE/"post1648s-inner-conjugacy-invariant-nonselection-theorem.json"
R_CANON="41974bb8c5b4f36a9cf5895fa52a5af81b17aa8bd4d9ced1915173573a0bad9a"
R_BLOB="5bd1feb89af127544bb68d682f69f29e375a675a"
N_CANON="060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
N_BLOB="0ee05f679c7706113feed2c217e08a95b3bd6f06"
S_CANON="b79aa40f805957b5e122aaff4791cab9b456409380d7f7d5214c7f3573cf3488"

def canonical(o):
    b=dict(o); b.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def blob(p):
    d=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(d)).encode()+b"\0"+d).hexdigest()

def q(a=0,b=0): return (Fraction(a),Fraction(b))
def qa(x,y): return (x[0]+y[0],x[1]+y[1])
def qn(x): return (-x[0],-x[1])
def qm(x,y): return (x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def MM(A,B): return tuple(tuple(qa(qm(A[i][0],B[0][j]),qm(A[i][1],B[1][j])) for j in range(2)) for i in range(2))
I=((q(1),q()),(q(),q(1))); NI=((q(-1),q()),(q(),q(-1)))
def tr(A): return qa(A[0][0],A[1][1])
def det(A): return qa(qm(A[0][0],A[1][1]),qn(qm(A[0][1],A[1][0])))
def pw(A,n):
    z=I
    for _ in range(n): z=MM(z,A)
    return z
def key(A): return tuple(v for row in A for e in row for v in e)
def inv(A):
    d=det(A); assert d in (q(1),q(-1)); di=d
    return ((qm(di,A[1][1]),qm(di,qn(A[0][1]))),(qm(di,qn(A[1][0])),qm(di,A[0][0])))
Sg=((q(1),q(1,1)),(q(),q(-1))); Tg=((q(1),q(1)),(q(-1),q()))
G={key(I):I}; queue=[I]
for X in queue:
    for g in (Sg,Tg):
        Y=MM(X,g); k=key(Y)
        if k not in G: G[k]=Y; queue.append(Y)

def real4(A):
    al,be=A[0]; ga,de=A[1]; aa,ab=al; ba,bb=be; ca,cb=ga; da,db=de
    return [[aa,ba,-2*ab,-2*bb],[ca,da,-2*cb,-2*db],[ab,bb,aa,ba],[cb,db,ca,da]]
def mv(M,v): return tuple(int(sum(M[i][j]*v[j] for j in range(4)))%2 for i in range(4))
LINES={"L1":(0,0,1,0),"L2":(0,0,0,1),"L3":(0,0,1,1)}
def fl(A):
    M=real4(A); z=[n for n,v in LINES.items() if mv(M,v)==v]; assert len(z)==1; return z[0]

def subgroup_size(A,B):
    seen={key(I):I}; qq=[I]
    for X in qq:
        for g in (A,B):
            Y=MM(X,g); k=key(Y)
            if k not in seen: seen[k]=Y; qq.append(Y)
    return len(seen)

def main():
    r=json.loads(R_PATH.read_text()); n=json.loads(N_PATH.read_text()); s=json.loads(S_PATH.read_text())
    assert canonical(r)==R_CANON==r["canonical_sha256_without_this_field"] and blob(R_PATH)==R_BLOB
    assert canonical(n)==N_CANON==n["canonical_sha256_without_this_field"] and blob(N_PATH)==N_BLOB
    assert canonical(s)==S_CANON==s["canonical_sha256_without_this_field"]
    assert len(G)==48
    els=list(G.values())
    As=[A for A in els if pw(A,4)==NI and tr(A)==q(0,-1) and det(A)==q(-1)]
    Bs=[B for B in els if pw(B,3)==NI and tr(B)==q(1) and det(B)==q(1)]
    pairs=[]
    for A in As:
        for B in Bs:
            AB=MM(A,B)
            if pw(AB,2)==I and tr(AB)==q() and det(AB)==q(-1):
                assert subgroup_size(A,B)==48; pairs.append((A,B))
    pairkeys={(key(A),key(B)) for A,B in pairs}; assert len(pairkeys)==24

    A0,B0=pairs[0]
    orbit=set(); stabilizer=[]
    for g in els:
        gi=inv(g); A=MM(MM(g,A0),gi); B=MM(MM(g,B0),gi)
        orbit.add((key(A),key(B)))
        if A==A0 and B==B0: stabilizer.append(g)
    assert orbit==pairkeys and len(orbit)==24
    assert len(stabilizer)==2 and {key(x) for x in stabilizer}=={key(I),key(NI)}

    line_counts={k:0 for k in LINES}
    for A,B in pairs: line_counts[fl(A)]+=1
    assert line_counts=={"L1":8,"L2":8,"L3":8}
    # Full G12 action on nonzero W-lines is transitive.
    images=set()
    v=LINES["L1"]
    for g in els:
        w=mv(real4(g),v)
        for name,x in LINES.items():
            if w==x: images.add(name)
    assert images==set(LINES)

    ex=s["exact_group_action"]
    assert ex["group_order"]==48 and ex["center_size"]==2
    assert ex["named_B9_B8_compatible_pair_count"]==24
    assert ex["pair_set_is_one_simultaneous_inner_conjugacy_orbit"] is True
    assert ex["pair_stabilizer_size"]==2 and ex["pair_stabilizer_equals_center"] is True
    assert ex["G12_action_on_W_nonzero_lines_transitive"] is True
    assert ex["B9_fixed_line_counts_over_pair_orbit"]==line_counts
    d=s["decision"]
    assert d["simultaneous_inner_conjugacy_invariant_route_closed_nonpruning"] is True
    assert d["absolute_delta0inf_retained_W_line_identified"] is False
    assert d["survivors_current_credit"]==[73,97,235]
    assert d["Q602_excluded"] is False and d["O210_excluded"] is False
    print("POST1648S_INNER_CONJUGACY_INVARIANT_NONSELECTION_THEOREM_COMPLETE")
    print("pair_orbit=24 stabilizer=center={+I,-I} W_line_action=transitive")
    print("B9_fixed_line_counts=L1:8,L2:8,L3:8")
    print("conjugacy_invariant_selector_route=closed_nonpruning")

if __name__=="__main__": main()
