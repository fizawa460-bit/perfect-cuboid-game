#!/usr/bin/env python3
import sympy as sp
A,B,C,D,x=sp.symbols('A B C D x')
Q=sp.expand((A*x+B)**4+(C*x+D)**4)
q4=sp.expand(Q.coeff(x,4)); q3=sp.expand(Q.coeff(x,3)); q2=sp.expand(Q.coeff(x,2)); q1=sp.expand(Q.coeff(x,1)); q0=sp.expand(Q.coeff(x,0))
expected=16*(A*B-C*D)*(A*B+C*D)*(A*D-B*C)**3*(A*D+B*C)
assert sp.factor(q0*q3**2-q4*q1**2-expected)==0

def IJ(a,b,c,d,e):
    return (sp.factor(12*a*e-3*b*d+c*c), sp.factor(72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c**3))
sub1={D:A*B/C}; lam1=B/C
aa,bb,cc=[sp.factor(z.subs(sub1)) for z in (q4,q3,q2)]
I1,J1=IJ(aa,0,sp.factor(bb-4*lam1*aa),0,sp.factor(2*lam1**2*aa-2*lam1*bb+cc))
assert sp.factor(I1-8*B**2*(A-C)**4*(5*A**4+4*A**3*C+6*A**2*C**2+4*A*C**3+5*C**4)/C**2)==0
assert sp.factor(J1+64*B**3*(A-C)**8*(A**2+A*C+C**2)*(7*A**2+10*A*C+7*C**2)/C**3)==0
L2=sp.factor((q1/q3).subs({D:-A*B/C}))
assert sp.factor(L2+B**2/C**2)==0
sub3={D:-B*C/A}; lam3=B/A
aa,bb,cc=[sp.factor(z.subs(sub3)) for z in (q4,q3,q2)]
I3,J3=IJ(aa,0,sp.factor(bb-4*lam3*aa),0,sp.factor(2*lam3**2*aa-2*lam3*bb+cc))
assert sp.factor(I3-64*B**2*C**4*(3*A**4+4*C**4)/A**2)==0
assert sp.factor(J3+1024*B**3*C**8*(9*A**4+8*C**4)/A**3)==0
print('R504_FULL_SPLIT_FACTOR_CERTIFICATE=PASS')
print('R504_FULL_SPLIT_RECIPROCAL_ANALYSIS=PASS')
