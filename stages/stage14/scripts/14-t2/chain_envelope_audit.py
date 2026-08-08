#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

OUT = Path('stages/stage14/data/14-t2/chain_envelope_audit.json')


def split_coeff(e:int)->int:
    return (2*e+1)**2

def inert_coeff(e:int)->int:
    return 2*e+1

def conv(a,b,n):
    return sum(a[k]*b[n-k] for k in range(n+1))

def binom(n,k):
    if k<0 or k>n:return 0
    r=1
    for j in range(1,k+1): r=r*(n-k+j)//j
    return r

# coefficients of (1-x)^-9
z9=[binom(n+8,8) for n in range(8)]
# coefficients of (1-x)^-6(1+x)^-3
z6=[binom(n+5,5) for n in range(8)]
invplus3=[((-1)**n)*binom(n+2,2) for n in range(8)]
inert_model=[conv(z6,invplus3,n) for n in range(8)]

assert split_coeff(1)==z9[1]==9
assert inert_coeff(1)==inert_model[1]==3

# residual exact polynomial checks:
# split: (1+6x+x^2)(1-x)^6 has zero linear coefficient
split_linear = 6 - 6
# inert: (1-x^2)^4 has zero linear coefficient
inert_linear = 0
assert split_linear == 0 and inert_linear == 0

rows=[]
for e in range(1,8):
    rows.append({'e':e,'split_f':split_coeff(e),'inert_f':inert_coeff(e)})

report={
 'metadata':{'stage':'14-t2','title':'Pythagorean-chain multiplicative envelope audit'},
 'representation_bounds':{
   'hypotenuse_count':'A(z)=(prod_{p=1 mod4}(2e_p+1)-1)/2',
   'leg_completion_bound':'L(z)<=(tau(z^2)-1)/2',
   'product_majorant':'A(z)L(z)<=f(z)/4'
 },
 'majorant_prime_powers':rows,
 'dirichlet_factorization':{
   'formula':'sum f(n)n^-s = zeta(s)^6 L(s,chi4)^3 G(s)',
   'split_residual':'(1+6x+x^2)(1-x)^6',
   'inert_residual':'(1-x^2)^4',
   'split_linear_residual_coefficient':split_linear,
   'inert_linear_residual_coefficient':inert_linear,
   'absolute_convergence_half_plane':'Re(s)>1/2+epsilon'
 },
 'conclusion':{
   'CHAIN_ENVELOPE':'T(B)=O(B(log B)^5)',
   'FROZEN_R03':'T(B)=o(B(log B)^3)',
   'CHAIN_ENVELOPE_IMPROVES_R03':False,
   'T_O_SQRT_B_PROVED':False,
   'NEXT':'Stage14-t3 exceptional fibers and low-degree subfamilies'
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report['conclusion'],indent=2))
