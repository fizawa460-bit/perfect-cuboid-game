#!/usr/bin/env python3
"""Stage13-3c: parity / 2-adic split of Stage13 raw incidences."""

from __future__ import annotations
import argparse, json, math
from collections import Counter, defaultdict
from pathlib import Path

BOUNDS=(1000,2000,5000,10000,20000,50000,100000)
OUT=Path("stages/stage13/data/13-3/parity_2adic_report.json")
CATS=("ab","ac","bc"); PAIRS=((0,1),(0,2),(1,2)); POS=("a","b","c")
LOCK=(84212,43236,40760)

def sq(n:int)->bool:
    r=math.isqrt(n); return r*r==n

def v2(n:int)->int:
    return (n & -n).bit_length()-1

def indexes(B:int):
    hyp=defaultdict(list); leg=defaultdict(list)
    for m in range(2,math.isqrt(B)+1):
        for n in range(1,m):
            if (m-n)%2==0 or math.gcd(m,n)!=1: continue
            u,v,w=m*m-n*n,2*m*n,m*m+n*n
            if w>B: continue
            if u>v: u,v=v,u
            k=1
            while k*w<=B:
                x,y,d=k*u,k*v,k*w
                hyp[d].append((x,y)); leg[x].append((y,d)); leg[y].append((x,d))
                k+=1
    return hyp,leg

def objects(B:int):
    hyp,leg=indexes(B); out={}
    for p,xy in hyp.items():
        for x,y in xy:
            for z,d in leg.get(p,()):
                a,b,c=sorted((x,y,z))
                if not a<b<c or math.gcd(math.gcd(a,b),c)!=1: continue
                key=(a,b,c,d)
                if key in out: continue
                vals=(a*a+b*b,a*a+c*c,b*b+c*c)
                mask=sum((1<<i) for i,q in enumerate(vals) if sq(q))
                if not mask or a*a+b*b+c*c!=d*d: raise ArithmeticError(key)
                out[key]=mask
    return out

def ratio(v):
    return {"ab":v[0]/v[2],"ac":v[1]/v[2],"bc":1.0}

def prop(v):
    s=sum(v); return {"ab":v[0]/s,"ac":v[1]/s,"bc":v[2]/s}

def tv(a,b):
    keys=set(a)|set(b)
    return .5*sum(abs(a.get(k,0)-b.get(k,0)) for k in keys)

def cap(t): return "4+" if t>=4 else str(t)

def audit(B:int):
    M=objects(B); raw=[0,0,0]; oe=[0,0,0]; ee=[0,0,0]
    odd_obj=Counter(); sig={c:Counter() for c in CATS}
    for (a,b,c,d),mask in M.items():
        s=(a,b,c); odd=[i for i,x in enumerate(s) if x&1]
        if len(odd)!=1 or d%2!=1: raise ArithmeticError(("odd",a,b,c,d))
        o=odd[0]; odd_obj[POS[o]]+=1
        ev=[i for i in range(3) if i!=o]
        if min(v2(s[i]) for i in ev)<2: raise ArithmeticError(("v2",a,b,c,d))
        for ci,(i,j) in enumerate(PAIRS):
            if not mask&(1<<ci): continue
            raw[ci]+=1
            if o in (i,j):
                oe[ci]+=1
                ef=i if i!=o else j
                er=next(k for k in ev if k!=ef)
                key=f"OE/{cap(v2(s[ef]))}/{cap(v2(s[er]))}"
            else:
                ee[ci]+=1
                vv=sorted((v2(s[i]),v2(s[j])))
                if vv[0]==vv[1]: raise ArithmeticError(("EE",a,b,c,d))
                key=f"EE/{cap(vv[0])}/{cap(vv[1])}"
            sig[CATS[ci]][key]+=1
    if [oe[i]+ee[i] for i in range(3)]!=raw: raise ArithmeticError("split")
    dist={}
    for c in CATS:
        t=sum(sig[c].values()); dist[c]={k:n/t for k,n in sig[c].items()}
    return {
      "B":B,"objects":len(M),"raw":dict(zip(CATS,raw)),
      "odd_position_objects":{p:odd_obj[p] for p in POS},
      "OE":{"count":dict(zip(CATS,oe)),"ratio_bc":ratio(oe),"proportion":prop(oe)},
      "EE":{"count":dict(zip(CATS,ee)),"ratio_bc":ratio(ee),"proportion":prop(ee)},
      "OE_share":sum(oe)/sum(raw),"EE_share":sum(ee)/sum(raw),
      "signature_tv":{"ab_ac":tv(dist["ab"],dist["ac"]),
                      "ab_bc":tv(dist["ab"],dist["bc"]),
                      "ac_bc":tv(dist["ac"],dist["bc"])},
    }

def build(bounds):
    rows=[audit(B) for B in bounds]
    r=next((x for x in rows if x["B"]==100000),None)
    if r and tuple(r["raw"][c] for c in CATS)!=LOCK: raise ArithmeticError("13-3a lock")
    return {
      "stage":"13-3c",
      "scope":"primitive canonical raw incidence; same population as Stage13-3a",
      "exact_facts":[
        "primitive space-diagonal solutions have exactly one odd edge and odd d",
        "an integral face forces both even edges to be divisible by 4",
        "V_ab,V_ac,V_bc are coordinate permutations, so a standalone p=2 local density is category-symmetric"
      ],
      "rows":rows,
      "conclusion":{
        "coarse_parity_common_sieve":True,
        "finite_OE_EE_coupling_visible":True,
        "p2_complete_flattening_explanation":False,
        "next":"Stage13-3d representation/fiber multiplicity"
      }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bounds",nargs="+",type=int,default=list(BOUNDS))
    ap.add_argument("--output",type=Path,default=OUT)
    a=ap.parse_args(); bounds=tuple(sorted(set(a.bounds)))
    report=build(bounds); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report["conclusion"],indent=2))

if __name__=="__main__": main()
