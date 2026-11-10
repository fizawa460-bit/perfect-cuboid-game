"""Exact-integer replay of151's arithmetic lemmas, not a cuboid search."""
import itertools, json, math
from pathlib import Path

def mul(z,w):
    a,b=z; c,d=w
    return a*c-b*d,a*d+b*c
def norm(z): return z[0]*z[0]+z[1]*z[1]
def add(z,w): return z[0]+w[0],z[1]+w[1]
def div(z,w):
    v=mul(z,(w[0],-w[1])); n=norm(w)
    if v[0]%n or v[1]%n: return None
    return v[0]//n,v[1]//n
def power(z,n):
    a=(1,0)
    for _ in range(n): a=mul(a,z)
    return a
def isprime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

checks=hits=highhits=0
for m in range(1,13):
    gs=[(a,b) for a in range(-m,m+1) for b in range(-m,m+1) if a*a+b*b==m*m]
    for r in (2,3):
        for tup in itertools.product(gs,repeat=r):
            C=(0,0)
            for z in tup: C=add(C,mul(z,z))
            assert norm(C)<=r*r*m**4
            for p,pi in [(5,(2,1)),(13,(3,2)),(17,(4,1)),(29,(5,2))]:
                checks+=1
                if C!=(0,0) and div(C,power(pi,2)) is not None:
                    hits+=1
                    assert p<=r*m*m
                if r==3 and C!=(0,0):
                    for n in (1,2,3):
                        if div(C,power(pi,2*n)) is not None:
                            highhits+=1
                            assert p**n<=3*m*m

witnesses=[]
for q in range(7,200001):
    if q%4!=1 or not isprime(q): continue
    m=1;k=0
    while 3*m*m<q: m*=5;k+=1
    R=m*q
    assert q<=3*m*m and m<=3*q*q
    assert 3*R*R<25*q**3
    witnesses.append((R,q,k))
assert len({R for R,q,k in witnesses})==len(witnesses)
report={'status':'PASS','gaussian_tuple_prime_checks':checks,'nonzero_pi_squared_hits':hits,
        'higher_valuation_hits':highhits,'m_range':[1,12],'prime_limit':200000,
        'distinct_relaxed_support_witnesses':len(witnesses),
        'counts_by_cutoff':{str(B):sum(R<=B for R,q,k in witnesses) for B in (1000,10000,100000,1000000,10000000)},
        'scope':'Exact finite replay supplements the proof; no physical existence or nonexistence is inferred.'}
Path(__file__).with_name('verification151.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
