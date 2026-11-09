#!/usr/bin/env python3
"""Separate mpmath interval evaluation of the same finite formula (not an audit)."""
from pathlib import Path
from fractions import Fraction
import json
if not __debug__: raise RuntimeError('Certification requires Python without -O')
from mpmath import iv
iv.dps=55
HERE=Path(__file__).resolve().parent
p=json.loads((HERE/'finite_bound_parameters393.json').read_text())
Q=lambda s:iv.mpf(Fraction(s).numerator)/Fraction(s).denominator
g,a,b,delta,c,d=[Q(p[k]) for k in ['gamma','alpha','beta','delta2','alpha1','alpha2']]
R=lambda s:(s+a)/((s+b)*(s+c)*(s+d))
T=lambda s:(iv.gamma((1-s)/2)/iv.gamma((s+1)/2+g))**56*(iv.gamma(1-s/2)/iv.gamma(1+s/2+g))**49
L=(b-a)*T(-b)/((c-b)*(d-b))
# gamma=delta, so T(-delta)=1 identically: no analytic gamma bound needed.
M=(delta-a)/(2*(delta-b)*(c-delta))
y=iv.log(L/M)/(delta-b)
t0=R(0)/R(1)*(iv.gamma(1+g)/iv.gamma(Q('1/2')+g))**7*(Q('1/2')+g)**49*iv.pi**(Q('105/2'))
D=json.loads((HERE/'parent392'/'different392.json').read_text())['absolute_discriminant']
B=iv.sqrt(D)/(t0*iv.exp(y))
lo=Q('133050646407933378580664821548066/10000');hi=Q('133050646407933378580664821548067/10000')
assert bool(lo<B) and bool(B<hi)
print(json.dumps({'engine':'mpmath.iv','decimal_precision':55,'bound_interval':str(B),'same_rational_enclosure':True,'independent_mathematical_audit':False},indent=2))
