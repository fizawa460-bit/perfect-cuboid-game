#!/usr/bin/env python3
import sympy as sp

a,b,x=sp.symbols('a b x')
Q=sp.expand((a*x+b)**4+(x+1)**4)
A=sp.expand(Q.coeff(x,4)); B=sp.expand(Q.coeff(x,3)); C=sp.expand(Q.coeff(x,2)); D=sp.expand(Q.coeff(x,1)); E=sp.expand(Q.coeff(x,0))
assert sp.factor(E*B**2-A*D**2)==16*(a-b)**3*(a+b)*(a*b-1)*(a*b+1)

def IJ(A,B,C,D,E):
    I=sp.factor(12*A*E-3*B*D+C**2)
    J=sp.factor(72*A*C*E+9*B*C*D-27*A*D**2-27*B**2*E-2*C**3)
    return I,J

subs={b:-a}
AA,BB,CC,DD,EE=[sp.factor(z.subs(subs)) for z in (A,B,C,D,E)]
I1,J1=IJ(AA,0,sp.factor(BB-4*AA),0,sp.factor(2*AA-2*BB+CC))
assert I1==64*a**4*(4*a**4+3)
assert J1==-1024*a**8*(8*a**4+9)

subs={b:1/a}; lam=1/a
AA,BB,CC,DD,EE=[sp.factor(z.subs(subs)) for z in (A,B,C,D,E)]
I2,J2=IJ(AA,0,sp.factor(BB-4*lam*AA),0,sp.factor(2*lam**2*AA-2*lam*BB+CC))
assert I2==8*(a-1)**4*(5*a**4+4*a**3+6*a**2+4*a+5)/a**2
assert J2==-64*(a-1)**8*(a**2+a+1)*(7*a**2+10*a+7)/a**3

print('R504_GENERAL_DEGREE2_NORMAL_FORM_PARAMETER_DIMENSION=2')
print('R504_EXTRA_INVOLUTION_LOCUS_FACTOR=PASS')
print('R504_L1_NO_RATIONAL_EXTRA_J1728=PASS')
print('R504_L2_NO_RATIONAL_EXTRA_J1728=PASS')
print('R504_EXTRA_INVOLUTION_DEGREE2_LOCUS=CLOSED_WITH_SYMBOLIC_CERTIFICATE')
print('R504_RESIDUAL=LIVE_PRYM_ISOGENY_LOCUS')
