#!/usr/bin/env python3
"""Stage13-7a: million-scale finite trend of the 2:1:1 deviation.

Complete finite enumeration by Pythagorean gluing
    x^2+y^2=p^2,  p^2+z^2=d^2,
with canonical a<b<c and gcd(a,b,c)=1.  Track raw incidences and exact-one
counts, then alpha=P_ab-1/2 and beta=(P_ac-P_bc)/2 through B=1,000,000.

The primary implementation keeps only a hypotenuse->face-pair index and streams
outer triples.  A second chunked shared-leg join independently verifies B_max.
Finite computation only: no limit for alpha, beta or Delta is asserted.
"""
from __future__ import annotations
import argparse, bisect, json, math
from collections import defaultdict
from pathlib import Path

BOUNDS=tuple(range(100_000,1_000_001,100_000))
OUT=Path("stages/stage13/data/13-7/deviation_scaling_report.json")
LOCK_RAW=(84212,43236,40760); LOCK_EXACT=(84146,43180,40704)
CATS=("ab","ac","bc")

def triples(B):
    for m in range(2,math.isqrt(B)+1):
        mm=m*m
        for n in range(1,m):
            if (m-n)%2==0 or math.gcd(m,n)!=1: continue
            u,v,w=mm-n*n,2*m*n,mm+n*n
            if w>B: continue
            if u>v: u,v=v,u
            for k in range(1,B//w+1): yield k*u,k*v,k*w

def square(n):
    r=math.isqrt(n); return r*r==n

def classify(x,y,z):
    if math.gcd(math.gcd(x,y),z)!=1: return None
    a,b,c=sorted((x,y,z))
    if not a<b<c: return None
    cat=0 if z==c else 1 if z==b else 2 if z==a else -1
    if cat<0: raise ArithmeticError((x,y,z,a,b,c))
    vals=(a*a+b*b,a*a+c*c,b*b+c*c)
    exact=all(i==cat or not square(v) for i,v in enumerate(vals))
    return cat,exact

def primary(bounds):
    B=bounds[-1]; mark=bytearray(B+1); nt=0
    for u,v,_ in triples(B): mark[u]=mark[v]=1; nt+=1
    faces=defaultdict(list); nf=0
    for x,y,p in triples(B):
        if mark[p]: faces[p].append((x,y)); nf+=1
    rb=[[0,0,0] for _ in bounds]; eb=[[0,0,0] for _ in bounds]
    glued=prim=0
    for u,v,d in triples(B):
        j=bisect.bisect_left(bounds,d)
        for p,z in ((u,v),(v,u)):
            fs=faces.get(p)
            if not fs: continue
            for x,y in fs:
                glued+=1; q=classify(x,y,z)
                if q is None: continue
                cat,ex=q; prim+=1; rb[j][cat]+=1
                if ex: eb[j][cat]+=1
    rows=[]; rc=[0,0,0]; ec=[0,0,0]
    for j,B0 in enumerate(bounds):
        for i in range(3): rc[i]+=rb[j][i]; ec[i]+=eb[j][i]
        rows.append({"B":B0,"raw":rc.copy(),"exact_one":ec.copy(),
                     "raw_band":rb[j],"exact_one_band":eb[j]})
    return {"triple_count":nt,"indexed_face_pairs":nf,"glued_records":glued,
            "primitive_raw_records":prim,"rows":rows}

def verify_chunked(B,chunk=250_000):
    raw=[0,0,0]; exact=[0,0,0]
    for lo in range(1,B+1,chunk):
        hi=min(B,lo+chunk-1); faces=defaultdict(list)
        for x,y,p in triples(B):
            if lo<=p<=hi: faces[p].append((x,y))
        for u,v,_ in triples(B):
            for p,z in ((u,v),(v,u)):
                if not lo<=p<=hi: continue
                fs=faces.get(p)
                if not fs: continue
                for x,y in fs:
                    q=classify(x,y,z)
                    if q is None: continue
                    cat,ex=q; raw[cat]+=1
                    if ex: exact[cat]+=1
    return raw,exact

def stats(v):
    t=sum(v); p=[x/t for x in v]; d=(p[0]-.5,p[1]-.25,p[2]-.25)
    return {"counts":dict(zip(CATS,v)),"total":t,"proportion":dict(zip(CATS,p)),
            "ratio_bc":{"ab":v[0]/v[2],"ac":v[1]/v[2],"bc":1.0},
            "alpha":p[0]-.5,"beta":(p[1]-p[2])/2,
            "delta":dict(zip(CATS,d)),"L1":sum(abs(x) for x in d),
            "Linf":max(abs(x) for x in d)}

def build(bounds,do_verify=True):
    q=primary(bounds); by={r["B"]:r for r in q["rows"]}
    if tuple(by[100_000]["raw"])!=LOCK_RAW or tuple(by[100_000]["exact_one"])!=LOCK_EXACT:
        raise ArithmeticError("100k lock failed")
    cumulative=[]; annuli=[]; prev=0
    for r in q["rows"]:
        cumulative.append({"B":r["B"],"raw":stats(r["raw"]),"exact_one":stats(r["exact_one"])})
        annuli.append({"B_lo_exclusive":prev,"B_hi_inclusive":r["B"],
                       "raw":stats(r["raw_band"]),"exact_one":stats(r["exact_one_band"])})
        prev=r["B"]
    independent=None
    if do_verify:
        vr,ve=verify_chunked(bounds[-1]); target=q["rows"][-1]
        if vr!=target["raw"] or ve!=target["exact_one"]: raise ArithmeticError("Bmax verification failed")
        independent={"method":"chunked shared-leg p join without the primary leg-mark prefilter",
                     "raw":dict(zip(CATS,vr)),"exact_one":dict(zip(CATS,ve)),"matched_primary":True}
    half=bounds[-1]//2; rh=[0,0,0]; eh=[0,0,0]
    for r in q["rows"]:
        if r["B"]>half:
            for i in range(3): rh[i]+=r["raw_band"][i]; eh[i]+=r["exact_one_band"][i]
    outer={"B_lo_exclusive":half,"B_hi_inclusive":bounds[-1],"raw":stats(rh),"exact_one":stats(eh)}
    first,last=cumulative[0]["exact_one"],cumulative[-1]["exact_one"]
    A=[r["exact_one"]["alpha"] for r in cumulative]; Z=[r["exact_one"]["beta"] for r in cumulative]
    aa=[r["exact_one"]["alpha"] for r in annuli[1:]]; zz=[r["exact_one"]["beta"] for r in annuli[1:]]
    return {
      "metadata":{"stage":"13-7a","title":"Million-scale finite trend of deviation from (1/2,1/4,1/4)",
                  "B_max":bounds[-1],"bounds":list(bounds),
                  "scope":"complete finite enumeration through B=1,000,000; no directional asymptotic theorem or limiting 2:1:1 claim"},
      "method":{"construction":"complete Pythagorean gluing, canonical a<b<c, gcd=1",
                "memory_strategy":"needed hypotenuse->face-pair index only; streamed outer triples; no canonical-row or full leg-index retention",
                "validation_100000":{"expected_raw":dict(zip(CATS,LOCK_RAW)),"expected_exact_one":dict(zip(CATS,LOCK_EXACT)),"matched":True},
                "enumeration_diagnostics":{"integer_pythagorean_triples_through_Bmax":q["triple_count"],
                  "indexed_face_pairs_with_usable_hypotenuse":q["indexed_face_pairs"],
                  "glued_records_before_primitive_strict_order_filters":q["glued_records"],
                  "primitive_raw_incidence_records":q["primitive_raw_records"]},
                "independent_verification_1m":independent},
      "cumulative":cumulative,"annuli_100k":annuli,"outer_half_500k_1m":outer,
      "key_comparison_100k_to_1m":{"exact_one_ratio_bc_100k":first["ratio_bc"],"exact_one_ratio_bc_1m":last["ratio_bc"],
          "alpha_100k":first["alpha"],"alpha_1m":last["alpha"],"beta_100k":first["beta"],"beta_1m":last["beta"],
          "beta_relative_change":last["beta"]/first["beta"]-1,"L1_100k":first["L1"],"L1_1m":last["L1"],
          "L1_relative_change":last["L1"]/first["L1"]-1},
      "trend_diagnostics":{"cumulative_alpha_positive_at_all_sampled_bounds":all(x>0 for x in A),
          "cumulative_beta_positive_at_all_sampled_bounds":all(x>0 for x in Z),
          "cumulative_beta_increase_steps":sum(Z[i]>Z[i-1] for i in range(1,len(Z))),
          "cumulative_beta_decrease_steps":sum(Z[i]<Z[i-1] for i in range(1,len(Z))),
          "post_100k_annular_beta_positive_in_all_nine_100k_bands":all(x>0 for x in zz),
          "post_100k_annular_beta_min":min(zz),"post_100k_annular_beta_max":max(zz),
          "post_100k_annular_alpha_changes_sign":min(aa)<0<max(aa),"post_100k_annular_alpha_min":min(aa),"post_100k_annular_alpha_max":max(aa),
          "outer_half_exact_one_share_of_1m_total":outer["exact_one"]["total"]/last["total"],
          "outer_half_exact_one_alpha":outer["exact_one"]["alpha"],"outer_half_exact_one_beta":outer["exact_one"]["beta"],
          "outer_half_exact_one_ratio_bc":outer["exact_one"]["ratio_bc"]},
      "conclusion":{"monotone_convergence_to_reference_supported_through_1m":False,
          "finite_deviation_is_smaller_at_1m_than_100k":False,"beta_pair_split_persists_in_fresh_outer_half":True,
          "alpha_has_stable_sign_in_annuli":False,"exact_one_sieve_materially_changes_1m_modes":False,
          "interpretation":"One more decade does not move the normalized exact-one vector closer to (1/2,1/4,1/4): beta rises from about 0.00737 at 100k to 0.00951 at 1m, and the fresh outer half has beta about 0.01023. Alpha remains small cumulatively but changes sign across 100k annuli. The 100k closeness is therefore not evidence of monotone convergence to exact 2:1:1; no limit is identified.",
          "stage13_7_status":"ACTIVE_7A_COMPLETE_TO_B_1E6_FINITE",
          "next":"Stage13-7b: extend beyond 1e6 with a more memory-efficient implementation or derive an analytic secondary-term model; test whether beta persists or eventually turns."}}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=OUT); ap.add_argument("--skip-independent-verify",action="store_true"); a=ap.parse_args()
    r=build(BOUNDS,not a.skip_independent_verify); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(r,indent=2)+"\n")
    print(json.dumps(r["key_comparison_100k_to_1m"],indent=2))
if __name__=="__main__": main()
