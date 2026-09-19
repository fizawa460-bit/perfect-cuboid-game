#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ARCHIVE_HEAD="ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11"
ARCHIVE_LOCKS={
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY-CERTIFICATE.json":
  "62a2d01447016731001d35cc5915880daa2bfada",
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY-CERTIFICATE.json":
  "1c03b78456a704e50f8af0640e1d23dc36948a3c",
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-SIX-BRANCH-HURWITZ-PASSPORT.md":
  "d421c11ecd6577234823b6e9604c8cc99ce48fec",
 "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md":
  "a29161602c0b38f0607794e56e61068b8cb9735d",
}
CERT="MB104-P6D-FULL-DECK-EQUALITY-PASSPORT-CERTIFICATE.json"
CERT_BLOB="04fc76c79cc5c1e0c8092bf203828484e1c8d1d8"
NOTE="MB104-P6D-FULL-DECK-EQUALITY-PASSPORT-20260919.md"
NOTE_BLOB="efd3334a22603a971d72ab2d858be4e5d25f4b99"
MASK=int("0000093f442e",16)

def req(c,m):
    if not c: raise SystemExit("FAIL: "+m)

def blob(p:Path):
    b=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def check_archive(root:Path):
    got=subprocess.check_output(["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
    req(got==ARCHIVE_HEAD,"archive HEAD")
    for rel,want in ARCHIVE_LOCKS.items():
        p=root/rel
        req(p.is_file() and blob(p)==want,"archive source "+rel)

def nodes():
    v=[]
    for j in range(3):
      for sa in (1,-1):
       for s1 in (1,-1):
        for s2 in (1,-1):
         z=[0j]*7
         z[j]=sa
         o=[t for t in range(3) if t!=j]
         z[3+o[0]]=s1;z[3+o[1]]=s2;z[6]=1
         v.append(tuple(z))
    for j in range(3):
      o=[t for t in range(3) if t!=j];a,b=o
      for sr in (1,-1):
       for ep in (1,-1):
        for eq in (1,-1):
         z=[0j]*7
         z[a]=1;z[b]=1j*sr;z[3+a]=1j*ep;z[3+b]=-eq*sr
         v.append(tuple(z))
    req(len(v)==48,"48 nodes")
    return v

def node_type(z):
    zz=[j for j in range(3) if z[3+j]==0]
    req(len(zz)==1,"unique b-zero")
    return zz[0]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--archive-root",required=True)
    args=ap.parse_args()
    check_archive(Path(args.archive_root))

    here=Path(__file__).resolve().parent
    req(blob(here/CERT)==CERT_BLOB,"certificate blob")
    req(blob(here/NOTE)==NOTE_BLOB,"note blob")
    cert=json.loads((here/CERT).read_text())
    req(cert["schema"]=="STAGE32_MB104_P6D_FULL_DECK_EQUALITY_PASSPORT_V1","schema")

    V=nodes()
    S=[i for i in range(48) if (MASK>>i)&1]
    req(S==cert["support"]["nodes"],"support")
    counts=[0,0,0]
    for i in S: counts[node_type(V[i])]+=1
    req(counts==[6,2,6],"node-type counts")
    req(counts==cert["support"]["beauville_node_type_counts"],"certificate node types")
    req(all(x>0 for x in counts),"all three types occur")

    # F2^3 group fact: three distinct elements in one nonzero coset
    # of a rank-two subspace generate the full rank-three group.
    G0={(0,0,0),(1,0,0),(0,1,0),(1,1,0)}
    outside={(0,0,1),(1,0,1),(0,1,1),(1,1,1)}
    s1,s2,s3=(0,0,1),(1,0,1),(0,1,1)
    def add(a,b): return tuple(x^y for x,y in zip(a,b))
    span={(0,0,0)}
    for s in (s1,s2,s3):
        span |= {add(x,s) for x in list(span)}
    req(len(span)==8,"three outside involutions generate G")
    req(len(span & G0)==4,"full G0 stabilizer")
    req(cert["full_deck_consequence"]["component_degree_e"]==4,"e=4")

    # Equality arithmetic.
    # d=112l, e=4 -> product projection degree = 14*e*l = 56l.
    req(cert["full_deck_consequence"]["projection_bidegree"]==["56l","56l"],"projection degrees")
    u=[48,16,48]
    r=[(112-x)//2 for x in u]
    req(r==[32,48,32],"type-pair ramification")
    req(sum(u)==112 and sum(r)==112,"six-value totals")
    req(cert["six_branch_passport"]["type_pair_unramified_totals"]==["48l","16l","48l"],"cert u totals")
    req(cert["six_branch_passport"]["type_pair_ramification_totals"]==["32l","48l","32l"],"cert r totals")

    us=[24,24,8,8,24,24]
    rs=[16,16,24,24,16,16]
    req(all(us[i]+2*rs[i]==56 for i in range(6)),"symmetric split fiber equations")
    req(sum(us)==112 and sum(rs)==112,"symmetric split RH")

    # Old spin saturation requires 7 nodes * 8l = 56l in one Weierstrass fiber.
    req(max(counts)==6,"max type count")
    req(max(counts)*8 < 56,"no forced full fiber saturation")
    req(cert["spin_comparison"]["unsquared_spin_equality_forced_by_retained_packet"] is False,
        "spin firewall")

    for k,v in cert["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_P6D_FULL_DECK_EQUALITY_PASSPORT_V1")
    print("node_types=6,2,6 -> full G0 stabilizer -> e=4")
    print("product_bidegree=56l,56l etale")
    print("six-value pair u=48l,16l,48l; r=32l,48l,32l")
    print("no seven-node fiber saturation; old U12 spin equality not forced")
    print("whole_P6_closed=false credit=zero")

if __name__=="__main__":
    main()
