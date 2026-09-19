#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction
from pathlib import Path

AUDIT_HEAD = "b28adadc95776762754e1415a0ecab0da1d4cd8e"
ARCHIVE_HEAD = "ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"

AUDIT_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-Z33-SPAN5-HYPERPLANE-CONTACT-EQUALITY-20260919.md":
        "65656518d30f69ab3a4a892c8d4ae1d5ed72670e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-Z-REVIVED-DEEPENING-PASS-2-20260919.md":
        "1ea3003c1587d94a9301fe08f50c0c97a529b85f",
}

ARCHIVE_LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CLASSIFICATION.md":
        "c3bcc580b5bd43b7805c7227c7420445f14c4b8c",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CERTIFICATE.json":
        "3bc4453affce96e87a60864c99f745bb4c28c794",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16.md":
        "593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json":
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md":
        "1dfafccb9559c98ccf71cc4b98449d784941d48f",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json":
        "f63d08b9005762a02935a727f35e6581ae52aaab",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md":
        "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_genus1_span5_hyperplane_aut_orbits.cpp":
        "0c5b460b76b69e41e6009be2e92b7c051f003c22",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-SATAKE-BOUNDARY-SOURCE-NOTE.md":
        "bea35571b1b8ad8fc14c9a5a9a7342e63fe2c398",
    "stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md":
        "512fcc70afb1acf16956fd4b7a2b9b935a052150",
}

# Gaussian rationals are pairs (real,imag), each Fraction.
def Z(a=0, b=0):
    return (Fraction(a), Fraction(b))

O = Z()
U = Z(1)
I = Z(0, 1)

def add(x,y): return (x[0]+y[0], x[1]+y[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def neg(x): return (-x[0],-x[1])
def scale(x,n): return (x[0]*n,x[1]*n)
def zero(x): return x[0] == 0 and x[1] == 0

def inv(x):
    d=x[0]*x[0]+x[1]*x[1]
    if d == 0:
        raise ZeroDivisionError
    return (x[0]/d,-x[1]/d)

def dot(a,b):
    s=O
    for x,y in zip(a,b):
        s=add(s,mul(x,y))
    return s

def rref(M):
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]) if m else 0
    piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if not zero(A[i][c])),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        q=inv(A[r][c])
        A[r]=[mul(v,q) for v in A[r]]
        for i in range(m):
            if i == r or zero(A[i][c]):
                continue
            f=A[i][c]
            A[i]=[sub(A[i][j],mul(f,A[r][j])) for j in range(n)]
        piv.append(c); r+=1
        if r == m:
            break
    return A,piv

def rank(M):
    return len(rref(M)[1])

def nullspace(M):
    R,piv=rref(M)
    n=len(R[0]) if R else 0
    free=[c for c in range(n) if c not in piv]
    out=[]
    for f in free:
        v=[O for _ in range(n)]
        v[f]=U
        for rr,pc in enumerate(piv):
            v[pc]=neg(R[rr][f])
        out.append(v)
    return out

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[O for _ in range(7)]
                    z[j]=Z(sa)
                    q=[t for t in range(3) if t != j]
                    z[3+q[0]]=Z(s1); z[3+q[1]]=Z(s2); z[6]=U
                    out.append(z)
    for j in range(3):
        q=[t for t in range(3) if t != j]
        a,b=q
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[O for _ in range(7)]
                    z[a]=U; z[b]=Z(0,sr)
                    z[3+a]=Z(0,ep); z[3+b]=Z(-eq*sr)
                    out.append(z)
    return out

def jac(z):
    specs=(
        ((0,2),(1,2),(5,-2)),
        ((1,2),(2,2),(3,-2)),
        ((0,2),(2,2),(4,-2)),
        ((0,2),(1,2),(2,2),(6,-2)),
    )
    J=[]
    for spec in specs:
        row=[O for _ in range(7)]
        for k,c in spec:
            row[k]=scale(z[k],c)
        J.append(row)
    return J

def qvals(v):
    sq=lambda x:mul(x,x)
    return [
        sub(add(sq(v[0]),sq(v[1])),sq(v[5])),
        sub(add(sq(v[1]),sq(v[2])),sq(v[3])),
        sub(add(sq(v[0]),sq(v[2])),sq(v[4])),
        sub(add(add(sq(v[0]),sq(v[1])),sq(v[2])),sq(v[6])),
    ]

def tangent(z):
    J=jac(z)
    k=next(i for i,x in enumerate(z) if not zero(x))
    gauge=[O for _ in range(7)]; gauge[k]=U
    B=nullspace(J+[gauge])
    if len(B) != 3:
        raise SystemExit("FAIL tangent dimension")
    JT=[list(x) for x in zip(*J)]
    L=nullspace(JT)
    if len(L) != 1:
        raise SystemExit("FAIL A1 left kernel")
    return B,L[0]

def lincomb(B,t):
    v=[O for _ in range(7)]
    for a,b in zip(t,B):
        v=[add(v[i],mul(a,b[i])) for i in range(7)]
    return v

def local_signature(z,h):
    B,L=tangent(z)
    hr=[dot(h,b) for b in B]
    zb=[j for j in range(3) if zero(z[3+j])]
    if len(zb) != 1:
        raise SystemExit("FAIL unique Satake boundary coordinate")
    bg=[O for _ in range(7)]; bg[3+zb[0]]=U
    br=[dot(bg,b) for b in B]

    if all(zero(x) for x in hr):
        return "ord2"

    rr=rank([br,hr])
    if rr == 1:
        return 2
    if rr != 2:
        raise SystemExit("FAIL local fixed-bin rank")
    n=nullspace([br,hr])
    if len(n) != 1:
        raise SystemExit("FAIL common tangent dimension")
    v=lincomb(B,n[0])
    obstruction=dot(L,qvals(v))
    return 1 if zero(obstruction) else 0

def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def check_root(root,head,locks,label):
    got=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    if got != head:
        raise SystemExit(f"FAIL {label} HEAD {got}")
    for rel,want in locks.items():
        p=root/rel
        if not p.is_file() or blob(p) != want:
            raise SystemExit(f"FAIL {label} source-lock {rel}")

def H(*pairs):
    return [Z(a,b) for a,b in pairs]

REPS = [
    ("I24-O4",24,4,"0000ffffff00",H((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)),0,{0:24,1:0,2:0}),
    ("I24-O24",24,24,"005a5affa5a5",H((1,0),(1,0),(0,0),(0,0),(0,0),(-1,0),(0,0)),0,{0:24,1:0,2:0}),
    ("I20-O48",20,48,"0000ff33330f",H((-1,0),(0,0),(0,0),(-1,0),(0,0),(0,0),(1,0)),0,{0:8,1:8,2:4}),
    ("I19-O48",19,48,"003c3c163333",H((0,0),(0,0),(-1,0),(-1,0),(-1,0),(0,0),(1,0)),3,{0:16,1:0,2:0}),
    ("I16-O3",16,3,"0000ff0000ff",H((0,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)),0,{0:0,1:0,2:16}),
    ("I16-O24",16,24,"000f0f000f0f",H((-1,0),(-1,0),(0,-1),(0,0),(0,0),(0,0),(1,0)),0,{0:0,1:16,2:0}),
    ("I15-O256",15,256,"111919162121",H((0,1),(0,1),(-1,0),(-1,0),(-1,0),(0,-1),(1,0)),0,{0:9,1:6,2:0}),
    ("I14-O96",14,96,"0000185aa566",H((0,0),(-1,0),(1,0),(0,0),(1,0),(1,0),(0,0)),2,{0:12,1:0,2:0}),
    ("I14-O192A",14,192,"00033c123303",H((-1,1),(0,0),(0,-1),(-1,0),(0,-1),(0,0),(1,0)),0,{0:14,1:0,2:0}),
    ("I14-O192B",14,192,"00033c123330",H((1,1),(0,0),(0,1),(-1,0),(0,1),(0,0),(1,0)),0,{0:14,1:0,2:0}),
    ("I14-O384A",14,384,"0005185aa524",H((0,-1),(-1,0),(1,-1),(0,0),(1,-1),(1,0),(0,0)),0,{0:10,1:4,2:0}),
    ("I14-O384B",14,384,"0005185aa581",H((0,1),(-1,0),(-1,-1),(0,0),(-1,-1),(1,0),(0,0)),0,{0:10,1:4,2:0}),
]

GEN_SRC = [
    (1,0,2,4,3,5,6),
    (2,1,0,5,4,3,6),
    (6,1,2,3,5,4,0),
    (0,1,2,3,4,5,6),
    (0,1,2,3,4,5,6),
    (0,1,2,3,4,5,6),
    (0,1,2,3,4,5,6),
    (0,1,2,3,4,5,6),
    (0,1,2,3,4,5,6),
]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audit-root",required=True)
    ap.add_argument("--archive-root",required=True)
    args=ap.parse_args()
    check_root(Path(args.audit_root),AUDIT_HEAD,AUDIT_LOCKS,"audit")
    check_root(Path(args.archive_root),ARCHIVE_HEAD,ARCHIVE_LOCKS,"archive")

    # The exact generators permute b1,b2,b3 among themselves, so the unordered
    # pair of Satake distinguished directions transports orbitwise.
    for s in GEN_SRC:
        if set(s[3:6]) != {3,4,5}:
            raise SystemExit("FAIL Aut generator does not preserve Satake boundary divisor")

    V=nodes()
    if len(V) != 48:
        raise SystemExit("FAIL node count")

    computed=[]
    for oid,inc,osz,mask,h,want_ord2,want_fixed in REPS:
        support=[i for i,z in enumerate(V) if zero(dot(h,z))]
        gotmask=sum(1<<i for i in support)
        if f"{gotmask:012x}" != mask or len(support) != inc:
            raise SystemExit(f"FAIL support {oid}")
        cnt={0:0,1:0,2:0}; ord2=0
        for i in support:
            s=local_signature(V[i],h)
            if s == "ord2":
                ord2 += 1
            else:
                cnt[s] += 1
        if ord2 != want_ord2 or cnt != want_fixed:
            raise SystemExit(f"FAIL local taxonomy {oid}: {ord2} {cnt}")
        computed.append([oid,inc,osz,mask,ord2,[cnt[0],cnt[1],cnt[2]]])

    # Orbit-size accounting is the archived complete 12-orbit quotient.
    dist={}
    for _,inc,osz,_,_,_ in computed:
        dist[inc]=dist.get(inc,0)+osz
    if dist != {24:28,20:48,19:48,16:27,15:256,14:1248}:
        raise SystemExit("FAIL orbit accounting")

    cert=json.loads(Path(__file__).with_name(
        "MB104-Z33A-SPAN5-SIMPLE-CONTACT-ORBIT-CERTIFICATE.json").read_text())
    if cert["schema"] != "STAGE32_MB104_Z33A_SPAN5_SIMPLE_CONTACT_ORBITS_V1":
        raise SystemExit("FAIL certificate schema")
    table={row[0]:row for row in cert["orbit_table"]}
    for row in computed:
        c=table[row[0]]
        if c[1:6] != row[1:6]:
            raise SystemExit(f"FAIL certificate taxonomy {row[0]}")

    # BTVA N>=14 plus two order>=2 nodes closes the incidence-14 size-96 orbit.
    row=next(x for x in computed if x[0]=="I14-O96")
    if row[1]-row[4] >= 14:
        raise SystemExit("FAIL I14-O96 should have <14 eligible nodes")

    for k,v in cert["credit_firewall"].items():
        if v is not False:
            raise SystemExit("FAIL credit firewall "+k)

    print("PASS STAGE32_MB104_Z33A_SPAN5_SIMPLE_CONTACT_ORBITS_V1")
    for row in computed:
        print(row[0], "inc=",row[1],"orbit=",row[2],"order2=",row[4],"fixed0/1/2=",row[5])
    print("I14-O96=excluded_from_unbounded_Z33_sector")
    print("whole_span5_closed=false credit=zero")

if __name__ == "__main__":
    main()
