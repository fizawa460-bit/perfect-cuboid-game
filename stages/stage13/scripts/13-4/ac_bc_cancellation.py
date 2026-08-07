#!/usr/bin/env python3
"""Stage13-4b: ac/bc cancellation structure.

This audit re-enumerates the primitive canonical raw-incidence population up to
B=100000 and separates three finite weights:

  raw           : weight 1 per incidence
  G_neutral     : weight 1/R_all(p), R_all=(G(p)-1)/2
  shell_neutral : weight 1/R_prim(p,z,d)

Since
  1/R_prim = (R_all/R_prim) * (1/R_all),
the transition G_neutral -> shell_neutral isolates the primitive-support
correction C=R_all/R_prim.

The audit then splits ac/bc by OE/EE parity and by the fixed geometric score

  g = sqrt((b^2+c^2)/(a^2+c^2)) = w_ac/w_bc,

to test whether the near equality after pure-G deweighting comes from an exact
ac<->bc symmetry or from cross-stratum cancellation.

Finite diagnostic only: no categorywise asymptotic theorem is claimed.
"""

from __future__ import annotations
import json, math
from collections import defaultdict
from pathlib import Path

B_MAX = 100_000
BOUNDS = (1_000,2_000,5_000,10_000,20_000,50_000,100_000)
CATS = ("ac","bc")
OUTPUT = Path("stages/stage13/data/13-4/ac_bc_cancellation_report.json")
GEO_BINS = (
    (1.0,1.05,"g<1.05"),
    (1.05,1.10,"1.05-1.10"),
    (1.10,1.20,"1.10-1.20"),
    (1.20,float("inf"),"g>=1.20"),
)

def G(n:int)->int:
    x=n; out=1
    while x%2==0:
        x//=2
    q=3
    while q*q<=x:
        if x%q==0:
            e=0
            while x%q==0:
                x//=q; e+=1
            if q%4==1:
                out*=2*e+1
        q+=2
    if x>1 and x%4==1:
        out*=3
    return out

def indexes(B:int):
    hyp=defaultdict(list); leg=defaultdict(list)
    for m in range(2,math.isqrt(B)+1):
        for n in range(1,m):
            if (m-n)%2==0 or math.gcd(m,n)!=1:
                continue
            u,v,w=m*m-n*n,2*m*n,m*m+n*n
            if w>B:
                continue
            if u>v:
                u,v=v,u
            k=1
            while k*w<=B:
                x,y,d=k*u,k*v,k*w
                hyp[d].append((x,y))
                leg[x].append((y,d)); leg[y].append((x,d))
                k+=1
    return hyp,leg

def enumerate_rows(B:int):
    hyp,leg=indexes(B)
    rows=[]
    shells=defaultdict(list)
    for p,reps in hyp.items():
        R_all=len(reps)
        if G(p)-1 != 2*R_all:
            raise ArithmeticError(("G identity",p,G(p),R_all))
        for x,y in reps:
            for z,d in leg.get(p,()):
                if math.gcd(math.gcd(x,y),z)!=1:
                    continue
                a,b,c=sorted((x,y,z))
                if not a<b<c:
                    continue
                face=frozenset((x,y))
                if face==frozenset((a,c)):
                    cat="ac"
                elif face==frozenset((b,c)):
                    cat="bc"
                elif face==frozenset((a,b)):
                    cat="ab"
                else:
                    raise ArithmeticError(("category",x,y,z))
                parity="OE" if ((x&1)!=(y&1)) else "EE"
                r={"a":a,"b":b,"c":c,"d":d,"p":p,"z":z,
                   "cat":cat,"parity":parity,"R_all":R_all}
                rows.append(r); shells[(p,z,d)].append(r)
    for shell_rows in shells.values():
        rp=len(shell_rows)
        for r in shell_rows:
            r["R_prim"]=rp
    return rows

def layer(rows, kind:str):
    s={c:0.0 for c in CATS}
    for r in rows:
        if r["cat"] not in s:
            continue
        if kind=="raw":
            w=1.0
        elif kind=="G_neutral":
            w=1.0/r["R_all"]
        elif kind=="shell_neutral":
            w=1.0/r["R_prim"]
        else:
            raise ValueError(kind)
        s[r["cat"]]+=w
    return {
        "ac":s["ac"],"bc":s["bc"],
        "difference":s["ac"]-s["bc"],
        "ratio_ac_over_bc":s["ac"]/s["bc"],
    }

def subset_layers(rows):
    return {k:layer(rows,k) for k in ("raw","G_neutral","shell_neutral")}

def geometry_score(r):
    return math.sqrt((r["b"]**2+r["c"]**2)/(r["a"]**2+r["c"]**2))

def build_report():
    rows=enumerate_rows(B_MAX)

    by_bound=[]
    for B in BOUNDS:
        block={"B":B}
        for p in ("all","OE","EE"):
            ss=[r for r in rows if r["d"]<=B and r["cat"] in CATS
                and (p=="all" or r["parity"]==p)]
            block[p]=subset_layers(ss)
        by_bound.append(block)

    top=[r for r in rows if r["cat"] in CATS]
    support={}
    for p in ("all","OE","EE"):
        ss=[r for r in top if p=="all" or r["parity"]==p]
        support[p]={}
        for c in CATS:
            cc=[r for r in ss if r["cat"]==c]
            gn=sum(1/r["R_all"] for r in cc)
            sn=sum(1/r["R_prim"] for r in cc)
            support[p][c]={
                "G_neutral_weight":gn,
                "shell_neutral_weight":sn,
                "mean_C_Rall_over_Rprim_under_Gneutral":sn/gn,
                "incidence_mean_support_fraction_Rprim_over_Rall":
                    sum(r["R_prim"]/r["R_all"] for r in cc)/len(cc),
            }

    geo=[]
    for lo,hi,name in GEO_BINS:
        ss=[r for r in top if lo<=geometry_score(r)<hi]
        block={"bin":name,"g_min":lo,
               "g_max_exclusive":None if math.isinf(hi) else hi,
               "count":len(ss)}
        for p in ("all","OE","EE"):
            pp=[r for r in ss if p=="all" or r["parity"]==p]
            block[p]=subset_layers(pp)
        geo.append(block)

    outer={}
    for p in ("all","OE","EE"):
        ss=[r for r in top if 50_000<r["d"]<=100_000
            and (p=="all" or r["parity"]==p)]
        outer[p]=subset_layers(ss)

    last=by_bound[-1]
    conclusion={
        "pure_G_near_equality_is_parity_cancellation_at_B100000": True,
        "pure_G_near_equality_stable_at_all_smaller_bounds": False,
        "primitive_support_correction_favors_ac_over_bc": True,
        "geometric_subregions_have_equal_ac_bc_after_G_neutralization": False,
        "exact_weight_preserving_ac_bc_involution_at_B100000_for_raw_or_G_neutral": False,
        "reason_no_exact_involution":
            "The corresponding finite total weights are unequal; a cutoff-preserving "
            "weight-preserving involution exchanging ac and bc would force exact equality.",
        "working_interpretation":
            "At B=100000 the near ac=bc equality after pure-G deweighting is not a "
            "universal local symmetry. OE contributes a negative ac-bc gap and EE a "
            "positive gap of comparable size; low-g geometric regions are bc-heavy "
            "while high-g regions are ac-heavy. Primitive-support correction then pushes "
            "ac upward relative to bc. The observed two near-1 components are therefore "
            "supported by cross-stratum cancellation rather than an exact ac<->bc involution.",
        "next":
            "Stage13-4c: test how the OE/EE and geometric cancellation scales with B and "
            "whether a stable secondary balance law can be isolated.",
    }

    return {
        "metadata":{
            "stage":"13-4b",
            "title":"ac/bc parity-cancellation, pure-G, primitive-support and geometric-region diagnostic",
            "B_max":B_MAX,
            "geometry_score":"g=sqrt((b^2+c^2)/(a^2+c^2)) = w_ac/w_bc on 0<a<b<c",
            "scope":"finite structural diagnostic; no directional asymptotic theorem",
        },
        "exact_weight_relation":{
            "R_all":"(G(p)-1)/2",
            "R_prim":"number of primitive-supported unordered face representations on shell (p,z,d)",
            "C":"R_all/R_prim",
            "identity":"1/R_prim = C*(1/R_all)",
            "interpretation":
                "G_neutral -> shell_neutral isolates the primitive-support correction C; "
                "shell_neutral -> raw restores supported shell richness R_prim.",
        },
        "rows_by_bound":by_bound,
        "B100000_support_correction":support,
        "B100000_geometric_bins":geo,
        "outer_half_50000_100000":outer,
        "B100000_cancellation_summary":{
            "G_neutral_OE_difference":last["OE"]["G_neutral"]["difference"],
            "G_neutral_EE_difference":last["EE"]["G_neutral"]["difference"],
            "G_neutral_total_difference":last["all"]["G_neutral"]["difference"],
            "G_neutral_OE_ratio":last["OE"]["G_neutral"]["ratio_ac_over_bc"],
            "G_neutral_EE_ratio":last["EE"]["G_neutral"]["ratio_ac_over_bc"],
            "G_neutral_total_ratio":last["all"]["G_neutral"]["ratio_ac_over_bc"],
            "outer_half_G_neutral_total_ratio":outer["all"]["G_neutral"]["ratio_ac_over_bc"],
            "outer_half_G_neutral_OE_ratio":outer["OE"]["G_neutral"]["ratio_ac_over_bc"],
            "outer_half_G_neutral_EE_ratio":outer["EE"]["G_neutral"]["ratio_ac_over_bc"],
        },
        "conclusion":conclusion,
    }

def main():
    report=build_report()
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report["B100000_cancellation_summary"],indent=2))
    print(json.dumps(report["conclusion"],indent=2))

if __name__=="__main__":
    main()
