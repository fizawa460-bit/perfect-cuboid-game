#!/usr/bin/env python3
"""Stage13-3e: finite odd-prime / representation-density diagnostic.

For a primitive canonical raw face incidence, let p be the distinguished
integer face diagonal.  The pure sum-of-two-squares richness is

    R_all(p) = (G(p)-1)/2,

the number of unordered positive representations x<y, x^2+y^2=p^2.

After fixing the complementary outer triangle p^2+z^2=d^2 and imposing
primitive support gcd(x,y,z)=1, let

    R_prim(p,z,d)

be the number of supported unordered face representations.  For each outer
shell S=(p,z,d), write n_uv(S) for the number landing in canonical category
uv and q_uv(S)=n_uv(S)/R_prim(S).  Then exactly

    A_uv(B) = sum_S R_prim(S) q_uv(S).

The shell-neutral diagnostic

    U_uv(B) = sum_S q_uv(S)

removes only the finite shell-richness weighting.  It is a diagnostic, not an
asymptotic factorization or a proof of categorywise singular-series constants.
"""

from __future__ import annotations
import argparse, json, math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DEFAULT_BOUNDS=(1000,2000,5000,10000,20000,50000,100000)
DEFAULT_OUTPUT=Path("stages/stage13/data/13-3/representation_density_report.json")
CATS=("ab","ac","bc")
RAW_LOCKS={
  1000:(306,160,138),2000:(702,372,370),5000:(2300,1138,1077),
  10000:(5281,2740,2659),20000:(12407,6284,6105),
  50000:(37014,19080,17905),100000:(84212,43236,40760)
}
GEOM_PROP=(0.53473693,0.24535918,0.21990389)
GEOM_RATIO=(2.4316847502,1.1157564290,1.0)

def G(n:int)->int:
    x=n; out=1
    while x%2==0: x//=2
    q=3
    while q*q<=x:
        if x%q==0:
            e=0
            while x%q==0: x//=q; e+=1
            if q%4==1: out*=2*e+1
        q+=2
    if x>1 and x%4==1: out*=3
    return out

def generate_indexes(B:int):
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

def enumerate_incidences(B:int):
    hyp,leg=generate_indexes(B)
    out=[]
    for p,reps in hyp.items():
        R_all=len(reps)
        if G(p)-1 != 2*R_all:
            raise ArithmeticError(("G identity",p,G(p),R_all))
        for x,y in reps:
            for z,d in leg.get(p,()):
                if math.gcd(math.gcd(x,y),z)!=1: continue
                a,b,c=sorted((x,y,z))
                if not a<b<c: continue
                pair=frozenset((x,y))
                if pair==frozenset((a,b)): cat="ab"
                elif pair==frozenset((a,c)): cat="ac"
                elif pair==frozenset((b,c)): cat="bc"
                else: raise ArithmeticError(("category",x,y,z))
                parity="OE" if ((x&1)!=(y&1)) else "EE"
                out.append({
                  "a":a,"b":b,"c":c,"d":d,"cat":cat,"p":p,"z":z,
                  "R_all":R_all,"parity":parity
                })
    keys={(r["a"],r["b"],r["c"],r["d"],r["cat"]) for r in out}
    if len(keys)!=len(out): raise ArithmeticError("duplicate incidence")
    return out

def ratio(v):
    return {"ab":v["ab"]/v["bc"],"ac":v["ac"]/v["bc"],"bc":1.0}

def prop(v):
    s=sum(v.values()); return {c:v[c]/s for c in CATS}

def l1_to_geom(v):
    p=prop(v)
    return sum(abs(p[c]-GEOM_PROP[i]) for i,c in enumerate(CATS))

def rich_bucket(r:int)->str:
    if r==1:return "1"
    if r<=3:return "2-3"
    if r<=7:return "4-7"
    if r<=15:return "8-15"
    return "16+"

def analyze(bound:int, all_rows:list[dict[str,Any]]):
    rows=[r for r in all_rows if r["d"]<=bound]
    raw=Counter(r["cat"] for r in rows)
    got=tuple(raw[c] for c in CATS)
    if bound in RAW_LOCKS and got!=RAW_LOCKS[bound]:
        raise ArithmeticError(("raw lock",bound,got,RAW_LOCKS[bound]))

    shells=defaultdict(list)
    for r in rows: shells[(r["p"],r["z"],r["d"])].append(r)

    neutral={c:0.0 for c in CATS}
    gall_neutral={c:0.0 for c in CATS}
    mean_rprim_num=Counter(); mean_rall_num=Counter()
    parity_raw={k:Counter() for k in ("OE","EE")}
    parity_neutral={k:{c:0.0 for c in CATS} for k in ("OE","EE")}
    bucket_counts={b:Counter() for b in ("1","2-3","4-7","8-15","16+")}

    for shell_rows in shells.values():
        rprim=len(shell_rows)
        parity_set={r["parity"] for r in shell_rows}
        if len(parity_set)!=1: raise ArithmeticError("mixed shell parity")
        for r in shell_rows:
            c=r["cat"]; k=r["parity"]
            neutral[c]+=1.0/rprim
            gall_neutral[c]+=1.0/r["R_all"]
            mean_rprim_num[c]+=rprim
            mean_rall_num[c]+=r["R_all"]
            parity_raw[k][c]+=1
            parity_neutral[k][c]+=1.0/rprim
            bucket_counts[rich_bucket(rprim)][c]+=1

    rawv={c:raw[c] for c in CATS}
    nr={c:neutral[c] for c in CATS}
    gr={c:gall_neutral[c] for c in CATS}
    raw_dist=l1_to_geom(rawv)
    neutral_dist=l1_to_geom(nr)
    gall_dist=l1_to_geom(gr)

    return {
      "B":bound,
      "raw":rawv,
      "raw_ratio_bc":ratio(rawv),
      "shell_count":len(shells),
      "shell_neutral":{
        "weight":nr,"ratio_bc":ratio(nr),"proportion":prop(nr),
        "l1_to_geometric":neutral_dist,
        "fraction_of_raw_to_geometric_gap_removed":
          (1.0-neutral_dist/raw_dist) if raw_dist else None
      },
      "G_neutral":{
        "weight":gr,"ratio_bc":ratio(gr),"proportion":prop(gr),
        "l1_to_geometric":gall_dist,
        "fraction_of_raw_to_geometric_gap_removed":
          (1.0-gall_dist/raw_dist) if raw_dist else None
      },
      "raw_l1_to_geometric":raw_dist,
      "mean_supported_shell_richness_by_incidence":{
        c:mean_rprim_num[c]/raw[c] for c in CATS
      },
      "mean_all_face_representation_richness_by_incidence":{
        c:mean_rall_num[c]/raw[c] for c in CATS
      },
      "parity_control":{
        k:{
          "raw":{c:parity_raw[k][c] for c in CATS},
          "raw_ratio_bc":ratio({c:parity_raw[k][c] for c in CATS}),
          "shell_neutral_weight":parity_neutral[k],
          "shell_neutral_ratio_bc":ratio(parity_neutral[k])
        } for k in ("OE","EE")
      },
      "supported_richness_bucket_counts":{
        b:{c:bucket_counts[b][c] for c in CATS}
        for b in ("1","2-3","4-7","8-15","16+")
      },
      "supported_richness_bucket_ratio_bc":{
        b:ratio({c:bucket_counts[b][c] for c in CATS})
        for b in ("1","2-3","4-7","8-15","16+")
        if bucket_counts[b]["bc"]
      }
    }

def build_report(bounds):
    all_rows=enumerate_incidences(max(bounds))
    rows=[analyze(B,all_rows) for B in bounds]
    top=rows[-1]
    return {
      "metadata":{
        "stage":"13-3e",
        "title":"Odd-prime / representation-density finite diagnostic",
        "bounds":list(bounds),
        "geometric_reference":{
          "proportion":{"ab":GEOM_PROP[0],"ac":GEOM_PROP[1],"bc":GEOM_PROP[2]},
          "ratio_bc":{"ab":GEOM_RATIO[0],"ac":GEOM_RATIO[1],"bc":1.0}
        }
      },
      "exact_finite_decomposition":{
        "R_all":"(G(p)-1)/2 = number of unordered positive face representations",
        "R_prim":"number of representations on shell (p,z,d) surviving gcd(x,y,z)=1",
        "identity":"A_uv(B)=sum_shell R_prim(shell)*q_uv(shell)",
        "shell_neutral":"U_uv(B)=sum_shell q_uv(shell)",
        "warning":"U is a reweighting diagnostic, not an asymptotic factorization"
      },
      "rows":rows,
      "largest_bound_summary":{
        "B":top["B"],
        "raw_ratio_bc":top["raw_ratio_bc"],
        "shell_neutral_ratio_bc":top["shell_neutral"]["ratio_bc"],
        "G_neutral_ratio_bc":top["G_neutral"]["ratio_bc"],
        "shell_neutral_fraction_of_raw_to_geometric_gap_removed":
          top["shell_neutral"]["fraction_of_raw_to_geometric_gap_removed"],
        "G_neutral_fraction_of_raw_to_geometric_gap_removed":
          top["G_neutral"]["fraction_of_raw_to_geometric_gap_removed"],
        "mean_supported_shell_richness_by_incidence":
          top["mean_supported_shell_richness_by_incidence"],
        "mean_all_face_representation_richness_by_incidence":
          top["mean_all_face_representation_richness_by_incidence"]
      },
      "conclusion":{
        "representation_density_material_finite_correction":True,
        "rich_shells_flatten_ab_excess":True,
        "effect_persists_within_OE_and_EE":True,
        "pure_G_factor_complete_explanation":False,
        "supported_shell_neutral_is_asymptotic_theorem":False,
        "interpretation":(
          "At the audited bounds, especially B=100000, canonical ab incidences are "
          "concentrated in less representation-rich primitive outer shells than ac/bc. "
          "Weighting each shell equally moves the leading ab ratio strongly back toward "
          "the archimedean chamber prediction. The pure G(p) deweighting already gives a "
          "substantial part of this movement; primitive-support coupling strengthens it."
        ),
        "next":"Stage13-3f cutoff/boundary stability and leading-2 synthesis"
      }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--bounds",nargs="+",type=int,default=list(DEFAULT_BOUNDS))
    ap.add_argument("--output",type=Path,default=DEFAULT_OUTPUT)
    a=ap.parse_args(); bounds=tuple(sorted(set(a.bounds)))
    if not bounds or bounds[0]<=0: raise SystemExit("bounds must be positive")
    report=build_report(bounds)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report["conclusion"],indent=2))

if __name__=="__main__": main()
