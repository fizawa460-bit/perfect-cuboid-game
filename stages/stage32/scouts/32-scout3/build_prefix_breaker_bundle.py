#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

N=63; M=140; MAGIC="S32_D16_AUT_CANONICAL_BUNDLE_V1"

def csha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def load_hperp(p:pathlib.Path):
    with p.open() as f:
        if f.readline().strip()!="S32_D16_AUT_CANON_HPERP_V1": raise RuntimeError("bad hperp magic")
        f.readline(); f.readline(); input_sha=f.readline().strip(); n,m=map(int,f.readline().split())
        if (n,m)!=(N,M): raise RuntimeError("bad dims")
        for _ in range(N): f.readline()
        p0=[]; lin=[]
        for _ in range(M):
            r=list(map(int,f.readline().split())); p0.append(r[0]); lin.append(r[2:])
    return input_sha,p0,lin

def load_bundle(p:pathlib.Path):
    with p.open() as f:
        if f.readline().strip()!=MAGIC: raise RuntimeError("bad bundle magic")
        input_sha=f.readline().strip(); aut_sha=f.readline().strip(); f.readline(); seed=f.readline().strip()
        n,m,k,g=map(int,f.readline().split()); weights=list(map(int,f.readline().split()))
        if (n,m)!=(N,M) or len(weights)!=M: raise RuntimeError("bad bundle dims")
        for _ in range(k): f.readline()
        group=[tuple(map(int,f.readline().split())) for _ in range(g)]
    return input_sha,aut_sha,seed,weights,group

def row_for(p,weights,p0,lin):
    dw=[weights[p[i]]-weights[i] for i in range(M)]
    c0=sum(dw[i]*p0[i] for i in range(M))
    coeff=tuple(sum(dw[i]*lin[i][j] for i in range(M)) for j in range(N))
    return c0,coeff

def rank_key(item):
    p,(c0,c)=item
    nz=[i for i,x in enumerate(c) if x]
    first=nz[0] if nz else N
    # Reward impact concentrated toward the front of the DFS coordinate order.
    early=sum(abs(c[j])*(N-j) for j in range(N))
    prefix8=sum(abs(c[j]) for j in range(8))
    prefix16=sum(abs(c[j]) for j in range(16))
    tie=hashlib.sha256(bytes(p)).digest()
    return (first,-prefix8,-prefix16,-early,tie,p)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',type=pathlib.Path,required=True); ap.add_argument('--bundle',type=pathlib.Path,required=True); ap.add_argument('--count',type=int,required=True); ap.add_argument('--output',type=pathlib.Path,required=True); ap.add_argument('--summary',type=pathlib.Path,required=True); a=ap.parse_args()
    hin,p0,lin=load_hperp(a.input); bin_sha,aut_sha,seed,w,group=load_bundle(a.bundle)
    if hin!=bin_sha: raise RuntimeError("input sha mismatch")
    ident=tuple(range(M)); candidates=[]
    for p in group:
        if p==ident: continue
        row=row_for(p,w,p0,lin)
        if row[0]==0 and not any(row[1]): continue
        candidates.append((p,row))
    candidates.sort(key=rank_key)
    selected=candidates[:a.count]
    if len(selected)!=a.count: raise RuntimeError("not enough breakers")
    rows=[r for _,r in selected]
    payload={"input_sha":hin,"aut_sha":aut_sha,"seed":seed,"weights":w,"breakers":[[c0,list(c)] for c0,c in rows],"group":[list(p) for p in group],"selection":"PREFIX_FRONTLOADED_V1"}
    sha=csha(payload)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with a.output.open('w') as f:
        f.write(MAGIC+'\n'+hin+'\n'+aut_sha+'\n'+sha+'\n'+seed+'\n')
        f.write(f"{N} {M} {a.count} {len(group)}\n"); f.write(' '.join(map(str,w))+'\n')
        for c0,c in rows: f.write(str(c0)+' '+' '.join(map(str,c))+'\n')
        for p in group: f.write(' '.join(map(str,p))+'\n')
    firsts=[next((i for i,x in enumerate(c) if x),N) for _,c in rows]
    s={"schema":"STAGE32_SCOUT3_PREFIX_BREAKERS_V1","count":a.count,"bundle_sha256":sha,"first_nonzero_min":min(firsts),"first_nonzero_max":max(firsts),"first_nonzero_hist":{str(i):firsts.count(i) for i in sorted(set(firsts))},"SCOUT_ONLY":True,"D16_B12_NUMERICAL_CREDIT":False}
    a.summary.write_text(json.dumps(s,indent=2,sort_keys=True)+'\n'); print(json.dumps(s,sort_keys=True))
if __name__=='__main__': main()
