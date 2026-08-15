#!/usr/bin/env python3
import sympy as sp
A,B,C,D,d=sp.symbols('A B C D d')
Delta=A*D-B*C
M=sp.Matrix([[A,B],[C,D]])
Gs={'neg':sp.Matrix([[-1,0],[0,1]]),'inv':sp.Matrix([[0,1],[1,0]]),'ninv':sp.Matrix([[0,-1],[1,0]])}
Tc={name:sp.simplify(Delta*(M.inv()*G*M)) for name,G in Gs.items()}
expected={
'neg':sp.Matrix([[-A*D-B*C,-2*B*D],[2*A*C,A*D+B*C]]),
'inv':sp.Matrix([[-A*B+C*D,-B**2+D**2],[A**2-C**2,A*B-C*D]]),
'ninv':sp.Matrix([[-A*B-C*D,-B**2-D**2],[A**2+C**2,A*B+C*D]])}
for name in expected:
    for i in range(2):
        for j in range(2):
            assert sp.factor(Tc[name][i,j]-expected[name][i,j])==0
S1=sp.factor((A*D+B*C)**2-16*d*A**2*C**2)
assert sp.factor(S1.subs(d,B*D/(4*A*C))-Delta**2)==0
S2=sp.factor((-A*B+C*D)**2-4*d*(A**2-C**2)**2)
assert sp.factor(S2.subs(d,(B**2-D**2)/(4*(A**2-C**2)))-Delta**2)==0
S3=sp.factor((-A*B-C*D)**2-4*d*(A**2+C**2)**2)
assert sp.factor(S3.subs(d,(B**2+D**2)/(4*(A**2+C**2)))+Delta**2)==0
u,t,p,q=sp.symbols('u t p q')
eps=(p*u+d*q)/(-q*u-p)
expr=sp.together(eps+d/eps)
num,den=expr.as_numer_denom()
mod=sp.Poly(u**2-t*u+d,u)
def rem(z): return sp.rem(sp.Poly(sp.expand(z),u),mod).as_expr()
T=sp.factor(rem(num)/rem(den))
target=-(4*d*p*q+d*q**2*t+p**2*t)/(d*q**2+p**2+p*q*t)
assert sp.factor(T-target)==0
print('R504_NONSPLIT_TRANSPORTED_INVOLUTIONS=PASS')
print('R504_NONSPLIT_N1_LIFT_DISCRIMINANT=DELTA_SQUARED')
print('R504_NONSPLIT_N2_LIFT_DISCRIMINANT=DELTA_SQUARED')
print('R504_NONSPLIT_N3_LIFT_OBSTRUCTION=MINUS_DELTA_SQUARED')
print('R504_NONSPLIT_COMMUTING_LIFT_CLASSIFICATION=PASS')
