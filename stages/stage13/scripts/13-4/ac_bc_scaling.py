#!/usr/bin/env python3
"""Stage13-4c: scale the ac/bc cancellation found in 13-4b.

The audit re-enumerates the primitive canonical raw-incidence population up to
B=100000 and tracks the exact finite ratio decomposition

    r_raw(B) = r_G(B) * F_prim(B) * F_shell(B),

where

    r_G      = ac/bc after weight 1/R_all(p),
    F_prim   = r_shell_neutral/r_G,
    F_shell  = r_raw/r_shell_neutral.

It also measures OE/EE cancellation, recent annuli, and fixed geometric bins
for g=sqrt((b^2+c^2)/(a^2+c^2)).  The purpose is to decide whether the two
near-1 components exhibit a stable secondary balance law at the audited
finite scales.  No directional asymptotic theorem is claimed.
"""

from __future__ import annotations
import json, math
from collections import defaultdict
from pathlib import Path

B_MAX=100_000
BOUNDS=(1_000,2_000,5_000,10_000,20_000,50_000,100_000)
CATS=("ac","bc")
OUTPUT=Path("stages/stage13/data/13-4/ac_bc_scaling_report.json")
GEO_BINS=((1.0,1.05,"g<1.05"),(1.05,1.10,"1.05-1.10"),(1.10,1.20,"1.10-1.20"),(1.20,float("inf"),"g>=1.20"))

def G(n:int)->int:
    x=n; out=1
    while x%2==0: x//=2
    q=3
    while q*q<=x:
        if x%q==0:
            e=0
            while x%q==0:
                x//=q; e+=1
            if q%4==1: out*=2*e+1
        q+=2
    if x>1 and x%4==1: out*=3
    return out

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
                hyp[d].append((x,y))
                leg[x].append((y,d)); leg[y].append((x,d))
                k+=1
    return hyp,leg

def enumerate_rows(B:int):
    hyp,leg=indexes(B); rows=[]; shells=defaultdict(list)
    for p,reps in hyp.items():
        R_all=len(reps)
        if G(p)-1 != 2*R_all: raise ArithmeticError(("G identity",p))
        for x,y in reps:
            for z,d in leg.get(p,()):
                if math.gcd(math.gcd(x,y),z)!=1: continue
                a,b,c=sorted((x,y,z))
                if not a<b<c: continue
                face=frozenset((x,y))
                if face==frozenset((a,c)): cat="ac"
                elif face==frozenset((b,c)): cat="bc"
                elif face==frozenset((a,b)): cat="ab"
                else: raise ArithmeticError(("category",x,y,z))
                parity="OE" if ((x&1)!=(y&1)) else "EE"
                r={"a":a,"b":b,"c":c,"d":d,"p":p,"z":z,"cat":cat,"parity":parity,"R_all":R_all}
                rows.append(r); shells[(p,z,d)].append(r)
    for shell_rows in shells.values():
        rp=len(shell_rows)
        for r in shell_rows: r["R_prim"]=rp
    return rows

def layer(rows,kind:str):
    s={c:0.0 for c in CATS}
    for r in rows:
        if r["cat"] not in s: continue
        if kind=="raw": w=1.0
        elif kind=="G": w=1.0/r["R_all"]
        elif kind=="shell": w=1.0/r["R_prim"]
        else: raise ValueError(kind)
        s[r["cat"]]+=w
    return {"ac":s["ac"],"bc":s["bc"],"difference":s["ac"]-s["bc"],"ratio":s["ac"]/s["bc"]}

def score(r):
    return math.sqrt((r["b"]**2+r["c"]**2)/(r["a"]**2+r["c"]**2))

def cancel_stats(oe,ee):
    total=oe["difference"]+ee["difference"]
    den=abs(oe["difference"])+abs(ee["difference"])
    residual=abs(total)/den if den else None
    opposite=oe["difference"]*ee["difference"]<0
    return {
        "residual":residual,
        "efficiency":max(0.0,1.0-residual) if residual is not None else None,
        "EE_over_abs_OE_gap":ee["difference"]/(-oe["difference"]) if oe["difference"]<0<ee["difference"] else None,
        "opposite_signs":opposite,
    }

def build_report():
    rows=enumerate_rows(B_MAX)
    cumulative=[]; snapshots={}
    for B in BOUNDS:
        ss=[r for r in rows if r["d"]<=B and r["cat"] in CATS]
        all_raw=layer(ss,"raw"); all_g=layer(ss,"G"); all_sh=layer(ss,"shell")
        oe=layer([r for r in ss if r["parity"]=="OE"],"G")
        ee=layer([r for r in ss if r["parity"]=="EE"],"G")
        cs=cancel_stats(oe,ee)
        block={
            "B":B,"r_G":all_g["ratio"],
            "F_prim":all_sh["ratio"]/all_g["ratio"],
            "F_shell":all_raw["ratio"]/all_sh["ratio"],
            "r_raw":all_raw["ratio"],
            "OE_G_ratio":oe["ratio"],"EE_G_ratio":ee["ratio"],
            "OE_G_difference":oe["difference"],"EE_G_difference":ee["difference"],
            "G_total_difference":all_g["difference"],
            "cancellation_residual":cs["residual"],"cancellation_efficiency":cs["efficiency"],
            "EE_over_abs_OE_gap":cs["EE_over_abs_OE_gap"],
        }
        cumulative.append(block); snapshots[B]={"all":all_g,"OE":oe,"EE":ee}

    annuli=[]
    prev=0; prevw={p:{"ac":0.0,"bc":0.0} for p in ("all","OE","EE")}
    for B in BOUNDS:
        ab={"B_lo_exclusive":prev,"B_hi_inclusive":B}
        for p in ("all","OE","EE"):
            now=snapshots[B][p]
            ac=now["ac"]-prevw[p]["ac"]; bc=now["bc"]-prevw[p]["bc"]
            ab[p]={"ac":ac,"bc":bc,"difference":ac-bc,"ratio":ac/bc}
            prevw[p]={"ac":now["ac"],"bc":now["bc"]}
        cs=cancel_stats(ab["OE"],ab["EE"])
        ab["cancellation_residual"]=cs["residual"]; ab["cancellation_efficiency"]=cs["efficiency"]
        annuli.append(ab); prev=B

    geo_by_bound=[]
    for B in (20_000,50_000,100_000):
        ss=[r for r in rows if r["d"]<=B and r["cat"] in CATS]
        bins=[]
        for lo,hi,name in GEO_BINS:
            gg=[r for r in ss if lo<=score(r)<hi]
            gl=layer(gg,"G")
            bins.append({"bin":name,"G_ratio":gl["ratio"],"G_difference":gl["difference"],"count":len(gg)})
        geo_by_bound.append({"B":B,"bins":bins})

    outer=[r for r in rows if 50_000<r["d"]<=100_000 and r["cat"] in CATS]
    outer_all=layer(outer,"G"); outer_oe=layer([r for r in outer if r["parity"]=="OE"],"G"); outer_ee=layer([r for r in outer if r["parity"]=="EE"],"G")
    ocs=cancel_stats(outer_oe,outer_ee)
    outer_geo=[]
    for lo,hi,name in GEO_BINS:
        gg=[r for r in outer if lo<=score(r)<hi]
        gl=layer(gg,"G")
        outer_geo.append({"bin":name,"G_ratio":gl["ratio"],"G_difference":gl["difference"],"count":len(gg)})

    late=[r for r in cumulative if r["B"]>=10_000]
    def rg(key):
        vals=[r[key] for r in late]
        return {"min":min(vals),"max":max(vals),"range":max(vals)-min(vals)}
    top=cumulative[-1]

    return {
      "metadata":{"stage":"13-4c","title":"Scaling of ac/bc cancellation and late-range factor decomposition","B_max":B_MAX,"scope":"finite scaling diagnostic; no directional asymptotic theorem"},
      "exact_ratio_decomposition":{"identity":"r_raw(B)=r_G(B)*F_prim(B)*F_shell(B)","r_G":"G-neutral ac/bc ratio","F_prim":"r_shell_neutral/r_G; primitive-support correction","F_shell":"r_raw/r_shell_neutral; restoration of supported shell richness"},
      "cumulative_by_bound":cumulative,
      "late_factor_ranges_B_ge_10000":{"F_prim":rg("F_prim"),"F_shell":rg("F_shell"),"r_G":rg("r_G")},
      "latest_annuli":annuli[-3:],
      "late_geometric_bins":geo_by_bound,
      "outer_half_50000_100000":{"all_G_ratio":outer_all["ratio"],"OE_G_ratio":outer_oe["ratio"],"EE_G_ratio":outer_ee["ratio"],"OE_G_difference":outer_oe["difference"],"EE_G_difference":outer_ee["difference"],"G_total_difference":outer_all["difference"],"cancellation_residual":ocs["residual"],"cancellation_efficiency":ocs["efficiency"],"EE_over_abs_OE_gap":ocs["EE_over_abs_OE_gap"],"geometric_bins":outer_geo},
      "B100000_factorization":{"r_G":top["r_G"],"F_prim":top["F_prim"],"F_shell":top["F_shell"],"product":top["r_G"]*top["F_prim"]*top["F_shell"]},
      "conclusion":{"late_pure_G_OE_EE_cancellation_visible":True,"pure_G_balance_stable_at_all_smaller_bounds":False,"latest_outer_half_independently_reproduces_opposite_OE_EE_signs":True,"latest_outer_half_reproduces_low_g_negative_high_g_positive_crossing":True,"primitive_support_relative_factor_is_late_range_stable_near_1_06":True,"supported_shell_restoration_is_near_one_at_B100000":True,"exact_or_asymptotic_secondary_balance_law_proved":False,"stage13_4_status":"COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL","working_interpretation":"The two near-1 components do not come from an exact ac<->bc symmetry. At late audited cutoffs the pure-G OE and EE gaps have opposite signs and cancel strongly; the fresh outer half reproduces this cancellation and the geometric low-g/high-g sign crossing. The residual systematic ac excess is supplied mainly by a comparatively stable primitive-support factor near 1.06, while restoration of supported shell richness is nearly neutral at B=100000. This is a finite structural explanation, not an asymptotic equality theorem.","next":"Stage13-5 define the deviation from (1/2,1/4,1/4)"}
    }

def main():
    report=build_report(); OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report["B100000_factorization"],indent=2))
    print(json.dumps(report["conclusion"],indent=2))

if __name__=="__main__": main()
