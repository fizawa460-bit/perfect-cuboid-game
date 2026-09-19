#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ARCHIVE_HEAD = "ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-FEASIBILITY-CERTIFICATE.json":
        "8ec4a403d2485dbf061b8b16182aa06c62193c43",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-CERTIFICATE.json":
        "32a01bc272f14eca3e8ba3229f021f4140ab7260",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GLOBAL-EFFECTIVITY-P5-CONIC-CERTIFICATE.json":
        "7bef88be7a8a81bbcf022ef9fea4834c2dc2da39",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CONIC-MULTIBRANCH-CERTIFICATE.json":
        "b425ba24932632d28752899c6ad11cd530c7de6c",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md":
        "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json":
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json":
        "f63d08b9005762a02935a727f35e6581ae52aaab",
}

# Gaussian integers as (real, imaginary).
def g(a=0,b=0): return (a,b)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def zero(x): return x == (0,0)

def nodes():
    v=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[g() for _ in range(7)]
                    z[j]=g(sa)
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]]=g(s1); z[3+o[1]]=g(s2); z[6]=g(1)
                    v.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[g() for _ in range(7)]
                    z[a]=g(1); z[b]=g(0,sr)
                    z[3+a]=g(0,ep); z[3+b]=g(-eq*sr)
                    v.append(tuple(z))
    return v

def peq(a,b):
    k=next((j for j,x in enumerate(a) if not zero(x)),None)
    if k is None: return False
    for j in range(7):
        if mul(a[j],b[k]) != mul(b[j],a[k]):
            return False
    return True

def apply(z,n):
    a1,a2,a3,b1,b2,b3,c=z
    I=g(0,1)
    if n==0: return (a2,a1,a3,b2,b1,b3,c)
    if n==1: return (a3,a2,a1,b3,b2,b1,c)
    if n==2: return (mul(I,c),a2,a3,b1,mul(I,b3),neg(mul(I,b2)),neg(mul(I,a1)))
    y=list(z); y[n-3]=neg(y[n-3]); return tuple(y)

def perms(V):
    out=[]
    for n in range(9):
        p=[]
        for z in V:
            y=apply(z,n)
            hit=[j for j,w in enumerate(V) if peq(y,w)]
            if len(hit)!=1: raise SystemExit("FAIL generator node match")
            p.append(hit[0])
        out.append(tuple(p))
    return out

def compose(a,b): return tuple(a[b[i]] for i in range(48))

def group(gens):
    ident=tuple(range(48))
    seen={ident}; q=[ident]
    while q:
        x=q.pop()
        for a in gens:
            h=compose(a,x)
            if h not in seen:
                seen.add(h); q.append(h)
    return seen

def mask(S): return sum(1<<i for i in S)
def maskhex(S): return f"{mask(S):012x}"

def parse_row(row):
    tab={"0":g(),"1":g(1),"-1":g(-1),"i":g(0,1),"-i":g(0,-1)}
    return tuple(tab[x] for x in row)

def find_node(V,z):
    hit=[i for i,w in enumerate(V) if peq(z,w)]
    if len(hit)!=1: raise SystemExit("FAIL retained support node match")
    return hit[0]

def det(M):
    n=len(M); out=g()
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=g(1)
        for i,j in enumerate(p): t=mul(t,M[i][j])
        out=add(out,neg(t) if inv%2 else t)
    return out

def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def check_archive(root):
    got=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    if got!=ARCHIVE_HEAD: raise SystemExit("FAIL archive HEAD")
    for rel,want in LOCKS.items():
        p=root/rel
        if not p.is_file() or blob(p)!=want:
            raise SystemExit("FAIL archive source-lock "+rel)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--archive-root",required=True)
    args=ap.parse_args()
    check_archive(Path(args.archive_root))

    V=nodes()
    if len(V)!=48: raise SystemExit("FAIL 48 nodes")
    G=group(perms(V))
    if len(G)!=1536: raise SystemExit("FAIL Aut(S) order")

    # Seed one of the 32 known smooth conics:
    # a1=0, a2=-b3, a3=-b2, b1=-c.
    seed=[]
    for i,z in enumerate(V):
        a1,a2,a3,b1,b2,b3,c=z
        if zero(a1) and zero(add(a2,b3)) and zero(add(a3,b2)) and zero(add(b1,c)):
            seed.append(i)
    if len(seed)!=6: raise SystemExit("FAIL known conic seed")
    conics={tuple(sorted(p[i] for i in seed)) for p in G}
    if len(conics)!=32: raise SystemExit("FAIL 32 conics")

    # Four quartics in b1=0 section; Aut(S) gives exactly the retained 12.
    quartics=set()
    I=g(0,1)
    for eps in (1,-1):
        for delta in (1,-1):
            seedq=[]
            for i,z in enumerate(V):
                a1,a2,a3,b1,b2,b3,c=z
                if zero(b1) and zero(sub(a2,mul(g(0,eps),a3))) and zero(sub(c,mul(g(delta),a1))):
                    seedq.append(i)
            if len(seedq)!=8: raise SystemExit("FAIL quartic seed")
            for p in G: quartics.add(tuple(sorted(p[i] for i in seedq)))
    if len(quartics)!=12: raise SystemExit("FAIL 12 quartics")

    old_rows=[
      ["1","0","0","0","1","1","1"],["1","0","0","0","1","1","-1"],["1","0","0","0","1","-1","1"],
      ["0","1","0","1","0","1","1"],["0","1","0","1","0","1","-1"],["0","1","0","1","0","-1","1"],
      ["0","0","1","1","1","0","1"],["0","0","1","1","1","0","-1"],
      ["1","i","0","i","1","0","0"],["1","i","0","i","-1","0","0"],
      ["0","1","i","0","i","1","0"],["0","1","i","0","i","-1","0"],
      ["i","0","1","1","0","i","0"],["i","0","1","1","0","-i","0"],
    ]
    old=sorted(find_node(V,parse_row(r)) for r in old_rows)
    if maskhex(old)!="03c003818383": raise SystemExit("FAIL old support mask")

    oldset=set(old)
    cdist={}
    negcon=[]
    for C in conics:
        n=len(oldset & set(C))
        cdist[n]=cdist.get(n,0)+1
        if n>=4: negcon.append(C)
    if cdist!={0:4,1:11,2:8,3:8,5:1}: raise SystemExit("FAIL old conic distribution")
    if len(negcon)!=1 or maskhex(negcon[0])!="420000008282":
        raise SystemExit("FAIL old negative conic")
    if sorted(oldset & set(negcon[0])) != [1,7,9,15,41]:
        raise SystemExit("FAIL old negative conic overlap")
    oldorbit={mask(tuple(p[i] for i in old)) for p in G}
    if len(oldorbit)!=1536: raise SystemExit("FAIL old support orbit")

    new=[1,2,3,5,10,14,16,17,18,19,20,21,24,27]
    if maskhex(new)!="0000093f442e": raise SystemExit("FAIL survivor mask")
    minor=[1,2,3,5,10,14,16]
    D=det([[V[i][j] for j in range(7)] for i in minor])
    if D!=g(-16): raise SystemExit(f"FAIL survivor full-span determinant {D}")

    newset=set(new)
    cdist2={}
    for C in conics:
        n=len(newset & set(C)); cdist2[n]=cdist2.get(n,0)+1
    if cdist2!={0:4,1:8,2:12,3:8}: raise SystemExit("FAIL survivor conic distribution")
    qdist={}
    for Q in quartics:
        n=len(newset & set(Q)); qdist[n]=qdist.get(n,0)+1
    if qdist!={1:5,2:2,3:2,4:2,5:1}: raise SystemExit("FAIL survivor quartic distribution")

    cert=json.loads(Path(__file__).with_name(
        "MB104-P6A-KNOWN-LOW-DEGREE-TEST-CURVE-CERTIFICATE.json").read_text())
    if cert["schema"]!="STAGE32_MB104_P6A_KNOWN_LOW_DEGREE_TEST_CURVE_GATE_V1":
        raise SystemExit("FAIL certificate schema")
    if cert["old_F1_P6_support"]["mask_hex"]!="03c003818383":
        raise SystemExit("FAIL certificate old support")
    if cert["new_full_span_survivor"]["mask_hex"]!="0000093f442e":
        raise SystemExit("FAIL certificate survivor")
    if cert["new_full_span_survivor"]["max_conic_supported_nodes"]!=3:
        raise SystemExit("FAIL certificate conic max")
    if cert["new_full_span_survivor"]["max_quartic_supported_nodes"]!=5:
        raise SystemExit("FAIL certificate quartic max")
    for k,v in cert["credit_firewall"].items():
        if v is not False: raise SystemExit("FAIL credit "+k)

    print("PASS STAGE32_MB104_P6A_KNOWN_LOW_DEGREE_TEST_CURVE_GATE_V1")
    print("old_F1_P6_support=known_conic_fixed_component pairing=-6l orbit=1536")
    print("new_fullspan14_survivor=max_conic=3 max_quartic=5 fullspan_det=-16")
    print("whole_P6_closed=false credit=zero")

if __name__=="__main__":
    main()
