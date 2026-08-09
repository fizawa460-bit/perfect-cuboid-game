#!/usr/bin/env python3
import json

def roots_minus_one(p):
    return [a for a in range(p) if (a*a+1)%p==0]

def primes(n):
    out=[]
    for p in range(3,n+1,2):
        if all(p%d for d in range(3,int(p**0.5)+1,2)):
            out.append(p)
    return out

rows=[]
for p in primes(101):
    r=roots_minus_one(p)
    expected=2 if p%4==1 else 0
    assert len(r)==expected
    rows.append({'p':p,'mod4':p%4,'roots':r,'count':len(r),'density':len(r)/p})

result={
  'claim':'q^2=-1 mod p has two classes for p=1 mod 4 and none for p=3 mod 4',
  'checked_primes_through':101,
  'rows':rows,
  'fixed_positive_density_sieve':False,
  'independence_product_assumed':False,
}
print(json.dumps(result,indent=2))
