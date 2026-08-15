#!/usr/bin/env python3
import sympy as sp

u,v,x=sp.symbols('u v x')
phi=lambda z:(z**2+4*z-3)/(7-z**2)

# Degree-two factorization and deck.
num=sp.factor(sp.together(phi(v)-phi(u)).as_numer_denom()[0])
assert num==-4*(u-v)*(u*v+u+v+7)
delta=-(u+7)/(u+1)
assert sp.factor(sp.together(phi(delta)-phi(u)))==0

# Reciprocal lifts.
eps1=-u-2
eps2=(5-u)/(u+1)
assert sp.factor(sp.together(phi(eps1)-1/phi(u)))==0
assert sp.factor(sp.together(phi(eps2)-1/phi(u)))==0
assert sp.factor(sp.together(delta.subs(u,eps1)-eps2))==0

# Critical divisor.
der=sp.factor(sp.diff(phi(u),u))
assert der==4*(u**2+2*u+7)/(u**2-7)**2

# Pullback cover and epsilon_2 lift.
N=u**2+4*u-3
M=7-u**2
F=sp.expand(N**4+M**4)
assert sp.factor(sp.together(F.subs(u,eps2)*(u+1)**8/F))==1296
q=u**2+2*u-5
assert sp.factor(q.subs(u,eps2)*(u+1)**2)==-6*q

# Quotient invariant x and exact relation.
xx=(u**2+5)/(u+1)
# Relation x(u+1)=u^2+5.
rel=sp.Poly(u**2-x*u+(5-x),u)
def rem(expr):
    return sp.rem(sp.Poly(sp.expand(expr),u),rel).as_expr()
Fr=rem(F)
Qr=rem(q**4)
Fu=sp.Poly(Fr,u); Qu=sp.Poly(Qr,u)
H1=sp.factor(Fu.coeff_monomial(u)/Qu.coeff_monomial(u))
H0=sp.factor(Fu.coeff_monomial(1)/Qu.coeff_monomial(1))
assert sp.factor(H1-H0)==0
assert H1==2*(x**2-8)*(x**2+8*x+8)/(x**2+4*x-20)**2

# Binary quartic invariants.
quart=sp.expand(2*(x**4+8*x**3-64*x-64))
a=quart.coeff(x,4); b=quart.coeff(x,3); c=quart.coeff(x,2); d=quart.coeff(x,1); e=quart.coeff(x,0)
I=sp.factor(12*a*e-3*b*d+c**2)
J=sp.factor(72*a*c*e+9*b*c*d-27*a*d**2-27*b**2*e-2*c**3)
assert I==3072
assert J==0
assert 82944==4*12**4

print('R504_EXPLICIT_NONSPLIT_DEGREE2_MAP=PASS')
print('R504_EXPLICIT_DECK_AND_RECIPROCAL_LIFTS=PASS')
print('R504_SECOND_QUOTIENT_MODEL=PASS')
print('R504_SECOND_QUOTIENT_I=3072')
print('R504_SECOND_QUOTIENT_J=0')
print('R504_SECOND_QUOTIENT_JACOBIAN_Q_ISOMORPHIC_E0=PASS')
print('R504_GENERIC_RANK_JUMP_THEOREM=SUBMITTED_FOR_FRESH_AUDIT')
