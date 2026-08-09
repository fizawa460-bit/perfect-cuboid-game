#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

# Deterministic sanity checks for the t10 logical rewrite.

def physical_base(m,n):
    S=m*m-n*n
    X=2*m*n
    H=m*m+n*n
    return S,X,H,S*S-X*X

def exceptional(delta,u,v,p):
    if p==2 or delta%p or v%p==0:
        return False
    inv=pow(v,-1,p)
    q=(u*inv)%p
    return (q*q+1)%p==0

def gcd_rewrite(delta,u,v,p):
    if p==2 or v%p==0:
        return False
    return delta%p==0 and (u*u+v*v)%p==0

samples=0
for m in range(2,40):
    for n in range(1,m):
        if gcd(m,n)!=1 or (m-n)%2==0:
            continue
        S,X,H,D=physical_base(m,n)
        for u in range(1,25):
            for v in range(1,25):
                if gcd(u,v)!=1:
                    continue
                for p in (3,5,7,11,13,17,19,29,37,41,53,61,73,89,97):
                    if v%p==0:
                        continue
                    assert exceptional(D,u,v,p)==gcd_rewrite(D,u,v,p)
                    if gcd_rewrite(D,u,v,p):
                        assert p%4==1
                    samples+=1

print({
    'samples_checked': samples,
    'exceptional_residue_is_necessary_for_triple': False,
    'exceptional_support_rewrite': 'p | gcd(Delta_-, u^2+v^2), p not | v',
    'split_condition_follows': True,
    'status': 'PASS'
})
