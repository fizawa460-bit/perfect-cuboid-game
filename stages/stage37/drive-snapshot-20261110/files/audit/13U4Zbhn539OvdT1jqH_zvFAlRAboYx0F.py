"""Sound finite-modulus obstruction sieve for two-isogeny descent.
Survival means UNKNOWN, not locally/globally soluble. No GRH/BSD assumptions.
"""
from math import gcd, isqrt
from itertools import product
import json

def primes(n):
    out=[]; q=2
    while q*q<=n:
        if n%q==0:
            out.append(q)
            while n%q==0:n//=q
        q+=1
    if n>1:out.append(n)
    return out

def divisors_squarefree(n):
    ds=[1]
    for p in primes(n):ds += [p*d for d in ds[:]]
    return sorted(ds)

def sf(n):
    ans=1
    for p in primes(n):
        e=0
        while n%p==0:n//=p;e+=1
        if e%2:ans*=p
    return ans

def obstruction(a,b,d,q,k):
    mod=q**k
    squares={w*w%mod for w in range(mod)}
    # Any primitive (z,t) has t a unit OR z a unit. Scaling by a unit
    # multiplies the quartic by a fourth power and preserves being square.
    for z in range(mod):
        if (d*z**4+a*z*z+b//d)%mod in squares:return False
    for t in range(0,mod,q):
        if (d+a*t*t+(b//d)*t**4)%mod in squares:return False
    return True

def sieve(a,b,ds,tests):
    eliminated={}; survivors=[]
    for d in ds:
        for q,k in tests:
            if obstruction(a,b,d,q,k):
                eliminated[d]=[q,k];break
        else:survivors.append(d)
    return survivors,eliminated

def certify(m,n):
    assert m>n>0 and gcd(m,n)==1 and (m-n)%2
    u,v,w=m*m-n*n,2*m*n,m*m+n*n
    s=v*v+w*w
    a,b=-2*s,u**4
    ap,bp=4*s,16*v*v*w*w
    tests=[(2,6),(3,4),(5,3),(7,2),(11,2),(13,2)]
    tests += [(q,2 if q<40 else 1) for q in primes(u*v*w) if q not in (2,3,5,7,11,13)]
    e,eproof=sieve(a,b,divisors_squarefree(u),tests) # all negative d excluded over R
    dp=divisors_squarefree(2*v*w)
    ep,epproof=sieve(ap,bp,sorted(dp+[-d for d in dp]),tests)
    torsion_classes=sorted([1,-1,sf(v*w),-sf(v*w)])
    assert set(torsion_classes)<=set(ep), (m,n,ep,torsion_classes)
    closed_rank_zero=(e==[1] and ep==torsion_classes)
    return dict(m=m,n=n,U=u,V=v,W=w,E_survivors=e,Eprime_survivors=ep,
                known_Eprime_classes=torsion_classes,rank_zero_certified=closed_rank_zero,
                E_obstructions=eproof,Eprime_obstructions=epproof,tests=tests)

if __name__=='__main__':
    rows=[certify(m,n) for m in range(2,13) for n in range(1,m)
          if gcd(m,n)==1 and (m-n)%2]
    with open('ti003_certificates.json','w') as f:json.dump(rows,f,indent=2)
    print('Rank-zero certificates:',[(r['m'],r['n']) for r in rows if r['rank_zero_certified']])
    print('Total:',len(rows),'Certified:',sum(r['rank_zero_certified'] for r in rows))
    print('All others UNKNOWN; survivor counts:',[(r['m'],r['n'],len(r['E_survivors']),len(r['Eprime_survivors'])) for r in rows if not r['rank_zero_certified']])
