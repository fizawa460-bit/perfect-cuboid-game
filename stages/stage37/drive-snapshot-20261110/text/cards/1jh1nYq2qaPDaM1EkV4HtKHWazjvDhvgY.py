"""Exact local and normalization checks; no claim that test tuples are physical endpoints."""
from math import gcd, isqrt
from fractions import Fraction
import json

def odd_primes(n):
    n=abs(n); out=[]
    while n and n%2==0: n//=2
    p=3
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0: n//=p
        p+=2
    if n>1: out.append(n)
    return out

def vp(n,p):
    if not n: return None
    n=abs(n); v=0
    while n%p==0: n//=p; v+=1
    return v

def local_square(n,p):
    if not n: return True
    v=vp(n,p)
    return v%2==0 and pow((n//p**v)%p,(p-1)//2,p)==1

tuples=0; local_checks=0; local_odd_b=0; global_hits=0; parity_checks=0
for a in range(1,21):
 for b in range(1,21):
  if gcd(a,b)!=1: continue
  for s in range(-20,21):
   if not s: continue
   primes=odd_primes(a*b*s)
   for t in range(1,21):
    if gcd(s,t)!=1: continue
    N=a*a+b*b
    Q=N*s*s-12*a*b*s*t+4*a*a*t*t
    J=N*s*s-16*a*b*s*t+48*a*a*t*t
    Phi=N*s**4-16*a*b*s**3*t+(44*a*a-4*b*b)*s*s*t*t+48*a*b*s*t**3-16*a*a*t**4
    assert Phi+4*t*t*Q==s*s*J
    if not Q: continue
    C=Fraction(N*Q,(2*a*b*s)**2).denominator
    norm=-N*Phi
    tuples+=1
    if norm>=0 and isqrt(norm)**2==norm:
        global_hits+=1
        for p in odd_primes(C):
            if vp(C,p)%2:
                assert b%p==0 and p%4==1 and pow(11%p,(p-1)//2,p)==1
    for p in primes:
        if b%p and (not norm or vp(norm,p)%2==0):
            assert vp(C,p)%2==0
            parity_checks+=1
        if not local_square(norm,p): continue
        local_checks+=1
        if vp(C,p)%2:
            assert b%p==0
            assert s%p and t%p
            assert p%4==1 and pow(11%p,(p-1)//2,p)==1
            assert 0<vp(Q,p)<2*vp(b,p)
            assert vp(C,p)==2*vp(b,p)-vp(Q,p)
            local_odd_b+=1

# Necessary p-adic compatibility is weaker than actual realization or real positivity.
a,b,s,t,p=1,5,1,1,5
N=26; Q=-30; Phi=114
assert local_square(-N*Phi,p)
assert Fraction(N*Q,(2*a*b*s)**2)==Fraction(-39,5)

denominator_cases=0
for V in [1,2,10,100,1000]:
 for H in [1,2,5,20,100]:
    candidates=set()
    for d in range(1,H+1,2):
        if any(vp(d,p)>1 for p in odd_primes(d)): continue
        if any(p%4!=1 or pow(11%p,(p-1)//2,p)!=1 for p in odd_primes(d)): continue
        for e in [1,2]:
            for k in range(1,isqrt(V//(e*d))+1): candidates.add(e*d*k*k)
    assert len(candidates)<=V
    assert len(candidates)**2<=16*V*H
    denominator_cases+=1

out={'card':'M3-T11-125','status':'PASS','primitive_tuples':tuples,
     'odd_prime_parity_checks':parity_checks,'local_square_checks':local_checks,
     'local_odd_b_denominator_cases':local_odd_b,
     'necessary_global_square_locus_hits':global_hits,'denominator_box_cases':denominator_cases,
     'local_counterexample_to_all_denominators_square':{'tuple':[1,5,1,1],'prime':5,'theta':'-39/5','physical_realization_asserted':False},
     'scope':'Necessary homogeneous square locus and local tests only; no cuboid existence or asymptotic proof by enumeration.',
     'global_fixed_power_saving':False,'primary_gate_closed':False}
assert local_odd_b>0 and global_hits>0
with open('M3-T11-125-verification.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
