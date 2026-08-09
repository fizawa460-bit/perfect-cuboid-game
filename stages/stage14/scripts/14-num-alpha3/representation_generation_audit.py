#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, time
from collections import defaultdict
from math import gcd, isqrt


def is_square(n):
    if n < 0: return False
    r=isqrt(n); return r*r==n


def primitive_triples(bound):
    m=2
    while m*m+1<=bound:
        for n in range(1,m):
            if ((m-n)&1)==0 or gcd(m,n)!=1: continue
            u=m*m-n*n; v=2*m*n; w=m*m+n*n
            if w<=bound:
                if u>v: u,v=v,u
                yield u,v,w
        m+=1


def euclid_table(bound):
    t0=time.perf_counter(); reps=defaultdict(set); events=0
    for u,v,w in primitive_triples(bound):
        for k in range(1,bound//w+1):
            a,b=k*u,k*v
            if a>b: a,b=b,a
            reps[k*w].add((a,b)); events+=1
    return reps,{"seconds":time.perf_counter()-t0,"events":events,"diagonals":len(reps),"representations":sum(map(len,reps.values()))}


def spf_sieve(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for p in range(2,isqrt(n)+1):
        if spf[p]==p:
            for q in range(p*p,n+1,p):
                if spf[q]==q: spf[q]=p
    return spf


def factor(n,spf):
    out=[]
    while n>1:
        p=spf[n]; e=0
        while n%p==0: n//=p; e+=1
        out.append((p,e))
    return out


def prime_sum2(p):
    # audit-scale deterministic search; alpha4 may replace this by Cornacchia.
    for a in range(1,isqrt(p)+1):
        b2=p-a*a
        if b2<=0: break
        b=isqrt(b2)
        if b*b==b2:
            return a,b
    raise ArithmeticError(f"no sum-two-squares representation for p={p}")


def cmul(z,w):
    a,b=z; c,d=w
    return a*c-b*d,a*d+b*c


def cpow(z,e):
    out=(1,0); base=z
    while e:
        if e&1: out=cmul(out,base)
        base=cmul(base,base); e//=2
    return out


def gaussian_reps_for_d(d,spf,cache):
    """Generate every positive nontrivial representation d^2=a^2+b^2.

    Primes 2 and 3 mod 4 cannot create a nontrivial Gaussian direction in a
    primitive representation.  If they occur in d, they divide both legs by
    exactly their full exponent in d, so they contribute a common scalar.
    Only 1 mod 4 prime factors create the Gaussian/Girard branching.
    """
    fac=factor(d,spf)
    scalar=1
    split=[]
    for p,e in fac:
        if p==2 or p%4==3:
            scalar*=p**e
        else:
            split.append((p,e))
    if not split:
        return set()

    states={(1,0)}
    split_norm=1
    for p,e in split:
        split_norm*=p**e
        if p not in cache: cache[p]=prime_sum2(p)
        pi=cache[p]; pib=(pi[0],-pi[1]); nxt=set()
        # Norm target for the split part is split_norm^2. For p^e in d,
        # distribute all 2e Gaussian prime factors between pi and conjugate.
        for k in range(2*e+1):
            factor_z=cmul(cpow(pi,k),cpow(pib,2*e-k))
            for z in states: nxt.add(cmul(z,factor_z))
        states=nxt

    reps=set()
    for a,b in states:
        a=abs(a)*scalar; b=abs(b)*scalar
        if a==0 or b==0: continue
        if a>b: a,b=b,a
        if a*a+b*b!=d*d: raise ArithmeticError("Gaussian norm mismatch")
        reps.add((a,b))
    return reps


def gaussian_table(bound):
    t0=time.perf_counter(); spf=spf_sieve(bound); cache={}; reps={}; eligible=0
    for d in range(1,bound+1):
        fac=factor(d,spf)
        # A positive nontrivial representation exists iff d has at least one
        # prime factor 1 mod 4.  Factors 2 and 3 mod 4 are retained as scale.
        if not any(p%4==1 for p,e in fac):
            continue
        eligible+=1
        rr=gaussian_reps_for_d(d,spf,cache)
        if rr: reps[d]=rr
    return reps,{"seconds":time.perf_counter()-t0,"eligible_diagonals":eligible,"diagonals":len(reps),"representations":sum(map(len,reps.values())),"prime_sum2_cache":len(cache)}


def compare_tables(a,b,bound):
    keys=set(a)|set(b)
    bad=[]
    for d in sorted(keys):
        if a.get(d,set())!=b.get(d,set()):
            bad.append({"d":d,"euclid":sorted(a.get(d,set())),"gaussian":sorted(b.get(d,set()))})
            if len(bad)>=10: break
    if bad: raise ArithmeticError(f"representation mismatch: {bad}")
    return {"bound":bound,"all_representation_sets_equal":True,"diagonals":len(keys),"representations":sum(len(a.get(d,set())) for d in keys)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--bound",type=int,default=200000); ap.add_argument("--output")
    args=ap.parse_args(); B=args.bound
    e,ep=euclid_table(B); g,gp=gaussian_table(B); eq=compare_tables(e,g,B)
    ratio=(ep["seconds"]/gp["seconds"]) if gp["seconds"] else None
    report={"stage":"14-num-alpha3","classification":"FINITE_EXACT_REPRESENTATION_GENERATION_AUDIT","bound":B,"equality":eq,"euclid_scaled":ep,"gaussian_factor_synthesis":gp,"euclid_seconds_over_gaussian_seconds":ratio,"decision":{"REPRESENTATION_KEYSETS_EQUAL":True,"GAUSSIAN_GIRARD_SYNTHESIS_COMPLETE_ON_AUDIT_RANGE":True,"SCALED_DIAGONALS_HANDLED_EXACTLY":True,"CORNACCHIA_NOT_YET_REQUIRED":True,"SEGMENTED_CACHING_NOT_YET_BENCHMARKED":True,"ALPHA2_CI_DEPENDENCY_REQUIRED":False,"MEANINGFUL_END_TO_END_SPEEDUP_PROVED":False,"NEXT":"Stage14-num-alpha4 collision engine / generation integration"}}
    txt=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        from pathlib import Path
        p=Path(args.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(txt,encoding="utf-8")
    print(txt,end="")
if __name__=="__main__": main()
