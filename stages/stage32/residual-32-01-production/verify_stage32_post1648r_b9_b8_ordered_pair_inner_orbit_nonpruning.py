#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
N_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
J_PATH = HERE / "post1648j-cecotti-trace-orientation-correction.json"
Q_PATH = HERE / "post1648q-full-torus-translation-conjugacy-nonpruning.json"
R_PATH = HERE / "post1648r-b9-b8-ordered-pair-inner-orbit-nonpruning.json"

N_CANON="060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
N_BLOB="0ee05f679c7706113feed2c217e08a95b3bd6f06"
J_CANON="3f6fd55ced259c6f28949df61865e22d43a669a50bdaf2adf5ddcd88411a48ec"
J_BLOB="17641753c33ae46e9b7517dc85a915edd70d2057"
Q_CANON="9d7cec0d381e4524873be1dd1837e55fb99b1f38ec384ac79cface5bfe26af18"
Q_BLOB="8a4808087722a567bbfb654b66d4611125c64765"
R_CANON="41974bb8c5b4f36a9cf5895fa52a5af81b17aa8bd4d9ced1915173573a0bad9a"

def canonical(obj):
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

# Exact field Q(sqrt(2), i). Entries are ((a,b),(c,d)) = a+b*sqrt2 + i(c+d*sqrt2).
def ks_add(x,y): return (x[0]+y[0],x[1]+y[1])
def ks_mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def K(a=0,b=0,c=0,d=0): return ((Fraction(a),Fraction(b)),(Fraction(c),Fraction(d)))
def Kadd(x,y): return (ks_add(x[0],y[0]),ks_add(x[1],y[1]))
def Kneg(x): return ((-x[0][0],-x[0][1]),(-x[1][0],-x[1][1]))
def Kmul(x,y):
    uu=ks_mul(x[0],y[0]); vv=ks_mul(x[1],y[1])
    uv=ks_add(ks_mul(x[0],y[1]),ks_mul(x[1],y[0]))
    return ((uu[0]-vv[0],uu[1]-vv[1]),uv)
K0=K(); K1=K(1); KR=K(d=1)
def KM(A,B): return [[Kadd(Kmul(A[i][0],B[0][j]),Kmul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]
KI=[[K1,K0],[K0,K1]]; KNEG=[[Kneg(K1),K0],[K0,Kneg(K1)]]
def Kpow(A,n):
    out=KI
    for _ in range(n): out=KM(out,A)
    return out
def Ktr(A): return Kadd(A[0][0],A[1][1])
def Kdet(A): return Kadd(Kmul(A[0][0],A[1][1]),Kneg(Kmul(A[0][1],A[1][0])))
def Kinv(A):
    d=Kdet(A)
    assert d in (K1,K(-1))
    dinv=d
    return [[Kmul(dinv,A[1][1]),Kmul(dinv,Kneg(A[0][1]))],
            [Kmul(dinv,Kneg(A[1][0])),Kmul(dinv,A[0][0])]]

h=Fraction(1,2)
# B9 pullback on (dx/y, x dx/y): eigenvalues zeta8,zeta8^3, trace +r, det -1.
z8=K(b=h,d=h); z83=K(b=-h,d=h)
A_pull=[[z8,K0],[K0,z83]]
# B8 pullback matrix is the exact post1648J phi6 matrix.
B_pull=[[K(a=h,c=-h),K(a=-h,c=-h)],[K(a=h,c=-h),K(a=h,c=h)]]
# Retained O-lattice/N representation is homology/torus action, contragredient to pullback.
A_src=Kinv(A_pull); B_src=Kinv(B_pull)

# Target G12 over Q(r), r^2=-2.
def q(a=0,b=0): return (Fraction(a),Fraction(b))
def qadd(x,y): return (x[0]+y[0],x[1]+y[1])
def qneg(x): return (-x[0],-x[1])
def qmul(x,y): return (x[0]*y[0]-2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def QM(A,B): return tuple(tuple(qadd(qmul(A[i][0],B[0][j]),qmul(A[i][1],B[1][j])) for j in range(2)) for i in range(2))
QI=((q(1),q()),(q(),q(1))); QNEG=((q(-1),q()),(q(),q(-1)))
def Qpow(A,n):
    out=QI
    for _ in range(n): out=QM(out,A)
    return out
def Qtr(A): return qadd(A[0][0],A[1][1])
def Qdet(A): return qadd(qmul(A[0][0],A[1][1]),qneg(qmul(A[0][1],A[1][0])))
def qkey(A): return tuple(v for row in A for e in row for v in e)

S=((q(1),q(1,1)),(q(),q(-1)))
T=((q(1),q(1)),(q(-1),q()))
G={qkey(QI):QI}; queue=[QI]
for X in queue:
    for g in (S,T):
        Y=QM(X,g); k=qkey(Y)
        if k not in G: G[k]=Y; queue.append(Y)

def real4(A):
    alpha,beta=A[0]; gamma,delta=A[1]
    aa,ab=alpha; ba,bb=beta; ca,cb=gamma; da,db=delta
    return [[aa,ba,-2*ab,-2*bb],[ca,da,-2*cb,-2*db],[ab,bb,aa,ba],[cb,db,ca,da]]
def mv4mod2(M,v): return tuple(int(sum(M[i][j]*v[j] for j in range(4)))%2 for i in range(4))
LINES={"L1":(0,0,1,0),"L2":(0,0,0,1),"L3":(0,0,1,1)}
def fixed_line(A):
    M=real4(A); out=[name for name,v in LINES.items() if mv4mod2(M,v)==v]
    assert len(out)==1; return out[0]
def subgroup_size(A,B):
    seen={qkey(QI):QI}; qq=[QI]
    for X in qq:
        for g in (A,B):
            Y=QM(X,g); k=qkey(Y)
            if k not in seen: seen[k]=Y; qq.append(Y)
    return len(seen)
def word_matrix(word):
    out=QI
    for tok in word.split("*"): out=QM(out,S if tok=="S" else T)
    return out

def main():
    n=json.loads(N_PATH.read_text()); j=json.loads(J_PATH.read_text()); qc=json.loads(Q_PATH.read_text()); r=json.loads(R_PATH.read_text())
    assert canonical(n)==N_CANON==n["canonical_sha256_without_this_field"] and blob(N_PATH)==N_BLOB
    assert canonical(j)==J_CANON==j["canonical_sha256_without_this_field"] and blob(J_PATH)==J_BLOB
    assert canonical(qc)==Q_CANON==qc["canonical_sha256_without_this_field"] and blob(Q_PATH)==Q_BLOB
    assert canonical(r)==R_CANON==r["canonical_sha256_without_this_field"]

    # Verify the convention conversion and full source pair relations.
    assert Ktr(A_pull)==KR and Kdet(A_pull)==K(-1)
    assert Ktr(A_src)==Kneg(KR) and Kdet(A_src)==K(-1) and Kpow(A_src,4)==KNEG
    assert Ktr(B_pull)==K1 and Kdet(B_pull)==K1
    assert Ktr(B_src)==K1 and Kdet(B_src)==K1 and Kpow(B_src,3)==KNEG
    AB=KM(A_src,B_src)
    assert Kpow(AB,2)==KI and Ktr(AB)==K0 and Kdet(AB)==K(-1)
    conv=r["representation_convention"]
    assert conv["B9_trace_conversion"]=="+r with determinant -1 becomes -r"
    assert conv["B8_trace_conversion"]=="1 with determinant 1 remains 1"
    assert j["exact_curve_differential_representation"]["traces"]["phi6"]=="1"

    assert len(G)==48
    els=list(G.values())
    As=[A for A in els if Qpow(A,4)==QNEG and Qtr(A)==q(0,-1) and Qdet(A)==q(-1)]
    Bs=[B for B in els if Qpow(B,3)==QNEG and Qtr(B)==q(1) and Qdet(B)==q(1)]
    assert len(As)==6 and len(Bs)==8

    # The repaired convention must recover exactly the six B9 images materialized by N.
    nwords={w for ws in n["exact_enumeration"]["short_target_words_by_fixed_line"].values() for w in ws}
    assert {qkey(word_matrix(w)) for w in nwords}=={qkey(A) for A in As}

    pairs=[]; line_counts={"L1":0,"L2":0,"L3":0}
    for A in As:
        for B in Bs:
            ABt=QM(A,B)
            if Qpow(ABt,2)!=QI or Qtr(ABt)!=q() or Qdet(ABt)!=q(-1): continue
            assert subgroup_size(A,B)==48
            pairs.append((A,B)); line_counts[fixed_line(A)]+=1

    assert len(pairs)==24 and line_counts=={"L1":8,"L2":8,"L3":8}
    exact=r["target_exact_pair_enumeration"]
    assert exact["target_group_order"]==48
    assert exact["B9_candidates_with_full_invariants"]==6
    assert exact["B9_candidates_equal_post1648N_six_images"] is True
    assert exact["B8_candidates_with_full_invariants"]==8
    assert exact["ordered_pairs_satisfying_all_source_pair_invariants"]==24
    assert exact["all_24_pairs_generate_G12"] is True
    assert exact["B9_fixed_W_line_counts"]==line_counts
    assert exact["possible_delta0inf_residues_decimal"]==[73,97,235]

    dec=r["decision"]
    assert dec["named_B9_B8_pair_breaks_inner_conjugacy_ambiguity"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"]==[73,97,235]
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert r["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False

    print("POST1648R_B9_B8_ORDERED_PAIR_INNER_ORBIT_NONPRUNING_COMPLETE")
    print("representation_convention=homology_torus_contragredient; B9_trace=-r")
    print("ordered_pairs=24 all_generate_G12=true")
    print("B9_fixed_W_line_counts=L1:8,L2:8,L3:8")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")

if __name__=="__main__": main()
