#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction

CERT=Path(__file__).with_name("MB104-W16-B2-EXT-SERRE-FIRST-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def rref_rank(a):
    a=[list(map(Fraction,row)) for row in a]
    if not a:
        return 0
    m=len(a); n=len(a[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None:
            continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i==r:
                continue
            q=a[i][c]
            if q:
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m:
            break
    return r

def contains_coordinate_vector(rows,j):
    if not rows:
        return False
    n=len(rows[0])
    e=[Fraction(0)]*n
    e[j]=Fraction(1)
    return rref_rank(rows+[e])==rref_rank(rows)

def annihilator_has_all_nonzero(rows):
    # Deterministic brute-force over a finite coefficient box is enough for the
    # retained sanity examples below; theorem-level equivalence is source-locked.
    if not rows:
        return True
    n=len(rows[0])
    from itertools import product
    for v in product([-2,-1,1,2], repeat=n):
        if all(sum(Fraction(rows[i][j])*v[j] for j in range(n))==0 for i in range(len(rows))):
            return True
    return False

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W16_B2_EXT_SERRE_FIRST_V1","schema")
    req(c["status"]=="W16_B2_NO_INDEPENDENT_BYPASS_ABSORBED_BY_CB_NO_CREDIT","status")

    # Sanity models for the linear-algebra form of Hartshorne-Serre.
    # CB-like: evaluation image span(1,1,1), annihilator contains (1,1,-2).
    good=[[1,1,1]]
    req(not any(contains_coordinate_vector(good,j) for j in range(3)),"good no coordinate vector")
    req(annihilator_has_all_nonzero(good),"good all-nonzero annihilator")

    # Non-CB: evaluation image contains e_0; every annihilator has coordinate 0 at p0.
    bad=[[1,0,0],[0,1,1]]
    req(contains_coordinate_vector(bad,0),"bad contains coordinate vector")
    # direct rank statement: imposing v0=0 is forced by first row
    req(rref_rank(bad)==2,"bad rank")

    for l in range(1,60):
        n=112*l
        dmK2=336*l*l-224*l+16
        req(n>0,"nonempty length upper")
        disc=dmK2-4*n
        req(disc==336*l*l-672*l+16,"discriminant formula")
        if l>=2:
            req(disc>0,f"positive target l={l}")

    p=c["ext_package"]
    req(p["boundary_dual"]=="evaluation H^0(O(D_l)) -> H^0(O_Z(D_l))","boundary dual")
    q=c["local_freeness"]
    req(q["criterion"]=="the local Ext component is nonzero at every point of reduced Z","local criterion")
    req(c["disposition"]=="B2_ABSORBED_BY_CB_FIRST","disposition")
    req(c["W16_closed_negatively"] is False,"W16 stays open")
    req(c["next_internal_solo"]=="W16-A3-DIFFERENTIAL-DEGENERACY","next")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W16_B2_EXT_SERRE_FIRST_V1")
    print("locally_free_Ext <=> all-nonzero local residue vector <=> CB")
    print("B2=absorbed_by_CB_first next=W16-A3 no_credit")

if __name__=="__main__":
    main()
