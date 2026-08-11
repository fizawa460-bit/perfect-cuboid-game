#!/usr/bin/env python3
from fractions import Fraction as F

def mplus(a,b): return min(a,b)-a*b

def gamma(a,b,p): return p-a*b

def eta(a,b,p):
    m=mplus(a,b)
    return F(0) if m==0 else max(F(0),gamma(a,b,p))/m

# Exact Frechet checks on a rational mesh.
checks=0
for ai in range(1,10):
    a=F(ai,10)
    for bi in range(1,10):
        b=F(bi,10)
        lo=max(F(0),a+b-1)
        hi=min(a,b)
        assert mplus(a,b)==hi-a*b
        for pi in range(0,11):
            p=lo+(hi-lo)*F(pi,10)
            g=max(F(0),gamma(a,b,p))
            assert g<=mplus(a,b)
            e=eta(a,b,p)
            assert 0<=e<=1
            checks+=1

# Counterexample to any implication eta=B^{-o(1)} => eta near 1.
a=b=F(1,2); p=F(3,8)
assert gamma(a,b,p)==F(1,8)
assert mplus(a,b)==F(1,4)
assert eta(a,b,p)==F(1,2)

print('Stage14-s7-57 Bernoulli Frechet audit: PASS')
print('mesh checks:', checks)
print('interior counterexample eta:', eta(a,b,p))
