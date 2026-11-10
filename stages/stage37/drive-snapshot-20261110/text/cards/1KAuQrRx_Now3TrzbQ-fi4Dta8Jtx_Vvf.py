"""Exact finite checks for M3-T11-124; no enumeration proves the asymptotic theorem."""
from fractions import Fraction
from math import gcd, isqrt
import json

def fourth_root(n):
    r=isqrt(isqrt(n))
    assert r**4 <= n < (r+1)**4
    return r

checks=0
for U in [1,15,16,80,81,256,625,1296,4096]:
  for V in [1,2,5,11]:
    for L in range(1,10):
      labels=set()
      for m in range(L,fourth_root(U)+1):
        for a in range(m**4,U+1,m**4):
          for c in range(1,V+1):
            if gcd(a,c)==1:
              labels.add(Fraction(a,c)); labels.add(Fraction(-a,c))
      floor_sum=sum(U//m**4 for m in range(L,fourth_root(U)+1))
      assert len(labels)<=2*V*floor_sum
      assert Fraction(len(labels))<=Fraction(8*U*V,3*L**3)
      assert not labels or L**4<=U
      checks+=1

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
prime_examples={str(L):[p for p in range(L,2*L+1) if p%12==5 and prime(p)]
                for L in [10,100,1000,10000]}
for key, ps in prime_examples.items():
  L=int(key)
  for p in ps:
    theta=Fraction(p**4,1)
    assert L<=p<=2*L and theta.numerator<=(2*L)**4
    assert theta.denominator==1 and theta.numerator//p**4==1
    assert (theta.numerator//p**4)%p!=0

homogeneous_checks=0
for a in range(1,26):
 for b in range(1,26):
  if gcd(a,b)!=1: continue
  N=a*a+b*b
  for M in range(2,12):
   if N%(M*M) or gcd(N//(M*M)*a*b,M)!=1: continue
   N0=N//(M*M)
   for t0 in [1,2,3]:
    for s in [1,2,3,7]:
     t=M*M*t0
     if gcd(s,t)!=1 or gcd(s*t0,M)!=1: continue
     Pell=4*a*a*t*t-12*a*b*s*t+(b*b-11*a*a)*s*s
     theta=16*Fraction(N*Pell,(8*a*b*s)**2)+3*Fraction(N,b*b)
     Psi=N0*s*s-12*a*b*s*t0+4*a*a*M*M*t0*t0
     W=N0*Psi; H=(2*a*b*s)**2
     g=gcd(abs(W),H)
     assert theta==Fraction(M**4*W,H)
     if W:
      assert theta.numerator==M**4*(W//g)
      assert theta.denominator==H//g
      assert gcd(theta.denominator,M)==1
      assert gcd(W//g,H//g)==1
     homogeneous_checks+=1

out={'card':'M3-T11-124','status':'PASS','label_box_cases':checks,
     'homogeneous_normalization_cases':homogeneous_checks,
     'prime_relaxed_examples':{k:{'count':len(v),'first':v[:5]} for k,v in prime_examples.items()},
     'scope':'Finite sanity checks only; proofs in card. Prime examples are NOT physical endpoints.',
     'global_fixed_power_saving':False,'primary_gate_closed':False}
assert homogeneous_checks>0
with open('M3-T11-124-verification.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
