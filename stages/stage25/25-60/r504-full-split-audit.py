#!/usr/bin/env python3
import sympy as sp

A,B,C,D,x=sp.symbols('A B C D x')
Q=sp.expand((A*x+B)**4+(C*x+D)**4)
q4=sp.expand(Q.coeff(x,4)); q3=sp.expand(Q.coeff(x,3)); q2=sp.expand(Q.coeff(x,2)); q1=sp.expand(Q.coeff(x,1)); q0=sp.expand(Q.coeff(x,0))
assert sp.factor(q0*q3**2-q4*q1**2)==16*(A*B-C*D)*(A*B+C*D)*(A*D-B*C)**3*(A*D+B*C)

def IJ(a,b,c,d,e):
    I=sp.factor(12*a*e-3*b*d+c*c)
    J=sp.factor(72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c**3)
    return I,J

# S1: AB=CD, lambda=B/C.
sub1={D:A*B/C}; lam1=B/C
aa,bb,cc=[sp.factor(z.subs(sub1)) for z in (q4,q3,q2)]
I1,J1=IJ(aa,0,sp.factor(bb-4*lam1*aa),0,sp.factor(2*lam1**2*aa-2*lam1*bb+cc))
assert I1==8*B**2*(A-C)**4*(5*A**4+4*A**3*C+6*A**2*C**2+4*A*C**3+5*C**4)/C**2
assert J1==-64*B**3*(A-C)**8*(A**2+A*C+C**2)*(7*A**2+10*A*C+7*C**2)/C**3

# S2: AB=-CD has negative square lift parameter.
L2=sp.factor((q1/q3).subs({D:-A*B/C}))
assert L2==-B**2/C**2

# S3: AD=-BC, lambda=B/A.
sub3={D:-B*C/A}; lam3=B/A
aa,bb,cc=[sp.factor(z.subs(sub3)) for z in (q4,q3,q2)]
I3,J3=IJ(aa,0,sp.factor(bb-4*lam3*aa),0,sp.factor(2*lam3**2*aa-2*lam3*bb+cc))
assert I3==64*B**2*C**4*(3*A**4+4*C**4)/A**2
assert J3==-1024*B**3*C**8*(9*A**4+8*C**4)/A**3

print('R504_FULL_SPLIT_FACTOR_CERTIFICATE=PASS')
print('R504_FULL_SPLIT_S1_QUOTIENT_INVARIANTS=PASS')
print('R504_FULL_SPLIT_S2_Q_LIFT_OBSTRUCTION=PASS')
print('R504_FULL_SPLIT_S3_QUOTIENT_INVARIANTS=PASS')
print('R504_FULL_SPLIT_RECIPROCAL_ANALYSIS=PASS')
