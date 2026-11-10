"""Replay154 bridge budgets; candidate graphs are NOT physical cuboids."""
from collections import Counter
from itertools import product, combinations
from math import isqrt, comb
from fractions import Fraction as F
from pathlib import Path
import json

def primes(n):
    sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*(((n-p*p)//p)+1)
    return [p for p in range(5,n+1) if sieve[p] and p%4==1]
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def norm(z):return z[0]**2+z[1]**2
def circle(q):
    ab=next((a,isqrt(q-a*a)) for a in range(1,isqrt(q)+1) if isqrt(q-a*a)**2==q-a*a)
    z=mul(ab,ab);zc=(z[0],-z[1]);units=[(1,0),(-1,0),(0,1),(0,-1)]
    H=set(mul(u,w) for u in units for w in [(q,0),z,zc])
    assert len(H)==12 and all(norm(h)==q*q for h in H)
    return sorted(H)

allps=primes(4096);cs={};labelled=0
for q in allps:
    H=circle(q);squares=[mul(h,h) for h in H];C=Counter()
    for r in (2,3):
        mult=3 if r==2 else 1
        for gs in product(squares,repeat=r):
            z=(sum(g[0] for g in gs),sum(g[1] for g in gs))
            assert norm(z)<=r*r*q**4
            C[z]+=mult;labelled+=mult
    assert sum(C.values())==2160
    cs[q]=C

windows=[];examples=[];norm_checks=0
for T in [13,32,64,128,256,512,1024,2048]:
    ps=[p for p in allps if T<=p<=2*T];B=4*T*T;adj={q:set() for q in ps}
    for q in ps:
        for C in cs[q]:
            N=norm(C)
            if not N:continue
            candidates=[p for p in ps if p!=q and N%(p*p)==0]
            assert N<=144*T**4<T**6 and len(candidates)<=2
            norm_checks+=1
            adj[q].update(candidates)
            if q in (13,17) and candidates and len(examples)<8:
                examples.append({'q':q,'C':C,'norm_C':N,'candidate_p':candidates})
        assert len(adj[q])<=4320
    mutual=[(p,q) for p,q in combinations(ps,2) if p in adj[q] and q in adj[p]]
    products=set()
    for p,q in combinations(ps,2):
        R=p*q;assert T*T<=R<=B and p<=3*q*q and q<=3*p*p
        products.add(R)
    assert len(products)==comb(len(ps),2)
    # Abstract bidirectional degree-one graph: one matching, not an arithmetic assertion.
    matching=list(zip(ps[::2],ps[1::2]));degs=Counter(v for e in matching for v in e)
    assert max(degs.values(),default=0)<=1 and len(matching)==len(ps)//2
    windows.append({'T':T,'split_primes':len(ps),'scalar_products':len(products),
        'directed_norm_edges':sum(map(len,adj.values())),
        'mutual_norm_pairs':len(mutual),'mutual_examples':mutual[:8],
        'max_outdegree':max(map(len,adj.values()),default=0),'abstract_matching_edges':len(matching)})

# 152's numerical caps each dominate the number of covered semiprime pairs.
for s in range(101):assert 2**s>=comb(s,2)
ps=[13,17,29,37];B=4*37*37
def localF(x):return (1+23*x+23*x*x+x**3)/(1-x)**4
cover_checks=0
for mask in range(1<<len(ps)):
    S=[p for i,p in enumerate(ps) if mask>>i&1]
    W=F(64*B)
    for p in S:W*=localF(F(1,p))
    # sigma=1 replay; the written proof works for every sigma>0 and hence its infimum.
    assert W>=comb(len(S),2)
    cover_checks+=1

# Degree/height change cancels exactly, rather than improving a B exponent.
for k in range(1,101):
    d=16*k*k;sq=isqrt(d);assert sq*sq==d
    assert k*F(3,2*sq)==F(3,8)
    assert k*F(3,sq)==F(3,4)
assert F(3,8)>F(1,3) and F(1,2)>F(1,3)

out={'status':'PASS','scope':'bridge-budget and necessary-condition replay, not a physical existence/nonexistence search',
     'labelled_witness_checks':labelled,'nonzero_norm_window_checks':norm_checks,
     'windows':windows,'norm_witness_examples':examples,'cover_cap_checks':cover_checks,
     'veronese_height_checks':100,'GLOBAL_COUNTING_CREDIT':0,'GLOBAL_BRIDGE':'FAIL_FOR_TESTED_CLOSURE_CERTIFICATES'}
Path(__file__).with_name('verification154.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['norm_witness_examples']},indent=2))
