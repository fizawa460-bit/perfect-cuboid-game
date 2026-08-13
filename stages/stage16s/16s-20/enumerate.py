#!/usr/bin/env python3
"""Stage16S-20 deterministic finite census."""

import argparse, csv
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path

DEFAULT = (50,100,200,400,800,1200,1600,2000)

def square(n):
    r=isqrt(n)
    return r*r==n

def faces(a,b,c):
    return sum((square(a*a+b*b), square(a*a+c*c), square(b*b+c*c)))

def enumerate_fast(B):
    B2=B*B
    idx=defaultdict(list)
    for a in range(1,B):
        rem=B2-a*a-1
        if rem<=0: continue
        for b in range(a+1,isqrt(rem)+1):
            idx[a*a+b*b].append((a,b))
    out={}
    for d in range(1,B+1):
        d2=d*d
        for c in range(1,d):
            for a,b in idx.get(d2-c*c,()):
                if b>=c or gcd(gcd(a,b),c)!=1: continue
                out[(a,b,c)]=(d,faces(a,b,c))
    return out

def enumerate_brute(B):
    B2=B*B
    out={}
    for a in range(1,B):
        for b in range(a+1,B):
            ab=a*a+b*b
            if ab>=B2: break
            for c in range(b+1,isqrt(B2-ab)+1):
                if gcd(gcd(a,b),c)!=1: continue
                r2=ab+c*c
                if square(r2):
                    out[(a,b,c)]=(isqrt(r2),faces(a,b,c))
    return out

def rows(records, thresholds):
    ans=[]
    for B in thresholds:
        split=[0,0,0,0]
        for d,k in records.values():
            if d<=B: split[k]+=1
        ans.append({"B":B,"space_at_least":sum(split),"space_only":split[0],
                    "face1":split[1],"face2":split[2],"face3":split[3]})
    return ans

FIELDS=("B","space_at_least","space_only","face1","face2","face3")

def read(path):
    with path.open(newline="",encoding="utf-8") as f:
        return [{k:int(v) for k,v in r.items()} for r in csv.DictReader(f)]

def write(path,data):
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(data)

def stage17(path):
    with path.open(newline="",encoding="utf-8") as f:
        return {int(r["B"]):int(r["N1"]) for r in csv.DictReader(f)}

def verify(data_path, small, stage17_path):
    fast=enumerate_fast(small)
    brute=enumerate_brute(small)
    if fast!=brute:
        raise SystemExit("small-cutoff optimized/brute mismatch")
    frozen=read(data_path)
    ts=tuple(r["B"] for r in frozen)
    if not ts or ts!=tuple(sorted(set(ts))):
        raise SystemExit("thresholds must be strictly increasing")
    regen=rows(enumerate_fast(max(ts)),ts)
    if regen!=frozen:
        raise SystemExit(f"frozen census mismatch: {regen}")
    for r in frozen:
        if r["space_at_least"]!=r["space_only"]+r["face1"]+r["face2"]+r["face3"]:
            raise SystemExit(f"face split mismatch at B={r['B']}")
    if stage17_path:
        ref=stage17(stage17_path)
        for r in frozen:
            if r["B"] in ref and r["face1"]!=ref[r["B"]]:
                raise SystemExit(f"Stage17 interface mismatch at B={r['B']}")
    print(f"SMALL_CUTOFF_CROSSCHECK_B={small}:PASS")
    print(f"FROZEN_CENSUS_MAX_B={max(ts)}:PASS")
    if stage17_path: print("STAGE17_EXACT_ONE_INTERFACE=PASS")
    print("STAGE16S_20_VERIFY=PASS")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    p.add_argument("--verify",type=Path)
    p.add_argument("--stage17-counts",type=Path)
    p.add_argument("--self-check-b",type=int,default=200)
    p.add_argument("--thresholds",default=",".join(map(str,DEFAULT)))
    a=p.parse_args()
    if a.verify:
        verify(a.verify,a.self_check_b,a.stage17_counts); return
    ts=tuple(int(x) for x in a.thresholds.split(",") if x)
    if not ts or ts!=tuple(sorted(set(ts))) or ts[0]<=0:
        raise SystemExit("thresholds must be positive and strictly increasing")
    data=rows(enumerate_fast(max(ts)),ts)
    if a.output: write(a.output,data)
    else:
        w=csv.DictWriter(__import__("sys").stdout,fieldnames=FIELDS); w.writeheader(); w.writerows(data)

if __name__=="__main__":
    main()
