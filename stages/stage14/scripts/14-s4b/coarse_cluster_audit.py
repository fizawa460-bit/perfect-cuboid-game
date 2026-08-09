#!/usr/bin/env python3
from collections import Counter,defaultdict
from pathlib import Path
from math import log
import json, runpy

ROOT=Path(__file__).resolve().parents[4]
S4A=ROOT/'stages/stage14/scripts/14-s4a/active_fingerprint_census.py'
FULL=ROOT/'stages/stage14/data/14-s4a/active_fingerprint_census.json'
OUT=ROOT/'stages/stage14/data/14-s4b/coarse_cluster_summary.json'

def pf(n):
    n=abs(int(n)); out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p=3 if p==2 else p+2
    if n>1: out.append(n)
    return out

def hb(x):
    return '<.25' if x<.25 else '.25-.35' if x<.35 else '.35-.45' if x<.45 else '>=.45'

def ob(k):
    return '<=7' if k<=7 else '8' if k==8 else '9' if k==9 else '>=10'

def main():
    mod=runpy.run_path(str(S4A)); mod['main']()
    d=json.load(open(FULL)); rows=d['rows']
    sig=Counter(); support_j=[]; all_supported=0; orient=Counter(); rank=Counter(); coarse_rows=[]
    for r in rows:
        S,X,H=r['face']; base=set(pf(2*S*X*H)); comps=[int(x) for x in r['kummer_square_classes']]
        csets=[set(pf(x)) for x in comps]; union=set().union(*csets)
        j=len(base&union)/len(base|union) if base|union else 1.0
        support_j.append(j); all_supported += int(union<=base)
        signs=tuple('+' if x>0 else '-' if x<0 else '0' for x in comps)
        comega=tuple(len(s) for s in csets)
        rt=f"{r['rank_lower']}..{r['rank_upper']}"
        key=(rt,r['selmer_2_rank'],r['root_number'],ob(r['omega_2SXH']),signs,comega,hb(r['canonical_over_log_mu']),'X<S' if X<S else 'X>S')
        sig[key]+=1; orient['X<S' if X<S else 'X>S']+=1; rank[(rt,r['selmer_2_rank'],r['root_number'])]+=1
        coarse_rows.append({'id':r['id'],'signature':repr(key),'support_jaccard':j,'kummer_support_subset_bad_support':union<=base})
    sizes=sorted(sig.values(),reverse=True)
    top=[{'size':n,'signature':repr(k)} for k,n in sig.most_common(20)]
    summary={
      'metadata':{'stage':'14-s4b','active_vertices':len(rows)},
      'support':{'all_kummer_prime_support_inside_2SXH':all_supported,'mean_jaccard':sum(support_j)/len(support_j),'min_jaccard':min(support_j),'max_jaccard':max(support_j)},
      'coarse_signature':{'distinct':len(sig),'largest_cluster':sizes[0],'top10_covered':sum(sizes[:10]),'top20_covered':sum(sizes[:20]),'singletons':sum(n==1 for n in sizes),'top20':top},
      'orientation':dict(orient),
      'rank_selmer_root_histogram':{repr(k):v for k,v in rank.most_common()},
      'interpretation':'Exact Kummer classes are highly diverse; this audit tests whether explainable coarse arithmetic invariants collapse them into a few dominant types. These signatures are diagnostics, not algebraic-stratum classifications.',
      'decision':{
        'STAGE14_S4B':'COMPLETE_COARSE_ARITHMETIC_CLUSTER_AUDIT',
        'COARSE_SIGNATURES_EXPLAINABLE_AND_GEOMETRY_COMPARABLE':True,
        'FINITE_CLUSTERING_PROVES_ALGEBRAIC_STRATA':False,
        'SQRT_B_ASYMPTOTIC_PROVED':False,
        'NEXT':'Stage14-s4c reverse-count higher-degree stratum proliferation required by the finite sqrt(B) signal'
      }
    }
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
