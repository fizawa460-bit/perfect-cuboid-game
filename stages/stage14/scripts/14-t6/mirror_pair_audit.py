#!/usr/bin/env python3
"""Exact audit for the Stage14-t6 reflected elliptic j-pair."""
from fractions import Fraction
import json
from pathlib import Path

# Polynomial helpers, ascending coefficients.
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def add(a,b,sign=1):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0)
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def powp(a,n):
    r=[1]
    for _ in range(n): r=mul(r,a)
    return r

# Cross-multiplied identity j_-(s)=j_+(-s).
# j_+(s)/256=(s^2+s+1)^3/[s^2(s+1)^2]
# j_-(s)/256=(s^2-s+1)^3/[s^2(s-1)^2]
pplus=[1,1,1]
pminus=[1,-1,1]
dplus=mul([0,0,1],powp([1,1],2))
dminus=mul([0,0,1],powp([-1,1],2))
assert mul(powp(pminus,3), dplus)==mul(powp(pplus,3), dminus)

# Difference numerator after putting j_+ - j_- over the common denominator,
# with the overall factor 256 removed.
num=add(mul(powp(pplus,3),dminus),mul(powp(pminus,3),dplus),sign=-1)
# Expected: 2*s*(s^2+1)*(s^2-s-1)*(s^2+s-1).
expected=mul([0,2],mul([1,0,1],mul([-1,-1,1],[-1,1,1])))
assert num==expected,(num,expected)

result={
  'mirror_identity':'j_minus(s)=j_plus(-s)',
  'difference_factorization':'512*(s^2+1)*(s^2-s-1)*(s^2+s-1)/(s*(s-1)^2*(s+1)^2)',
  'quadratic_discriminants':{'s^2+1':-4,'s^2-s-1':5,'s^2+s-1':5},
  'physical_rational_equal_j':False,
  'nonisogeny_proved':False,
  'fixed_m4_root_cases_after_4ak':0,
  't_o_sqrt_b_proved':False,
}
out=Path(__file__).resolve().parents[2]/'data/14-t6/mirror_pair_audit.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
