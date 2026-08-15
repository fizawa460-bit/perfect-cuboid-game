#!/usr/bin/env python3
import sympy as sp

A,B,C,D,d=sp.symbols('A B C D d')
Delta=A*D-B*C
M=sp.Matrix([[A,B],[C,D]])
Gs={
    'neg':sp.Matrix([[-1,0],[0,1]]),
    'inv':sp.Matrix([[0,1],[1,0]]),
    'ninv':sp.Matrix([[0,-1],[1,0]]),
}
Tc={name:sp.simplify(Delta*(M.inv()*G*M)) for name,G in Gs.items()}
assert Tc['neg']==sp.Matrix([[-A*D-B*C,-2*B*D],[2*A*C,A*D+B*C]])
assert Tc['inv']==sp.Matrix([[-A*B+C*D,-B**2+D**2],[A**2-C**2,A*B-C*D]])
assert Tc['ninv']==sp.Matrix([[-A*B-C*D,-B**2-D**2],[A**2+C**2,A*B+C*D]])

# N1: BD=4dAC -> lift discriminant Delta^2.
S1=sp.factor((A*D+B*C)**2-16*d*A**2*C**2)
assert sp.factor(S1.subs(d,B*D/(4*A*C)))==Delta**2

# N2: D^2-B^2+4d(A^2-C^2)=0 -> lift discriminant Delta^2.
S2=sp.factor((-A*B+C*D)**2-4*d*(A**2-C**2)**2)
assert sp.factor(S2.subs(d,(B**2-D**2)/(4*(A**2-C**2))))==Delta**2

# N3: B^2+D^2=4d(A^2+C^2) -> obstruction -Delta^2.
S3=sp.factor((-A*B-C*D)**2-4*d*(A**2+C**2)**2)
assert sp.factor(S3.subs(d,(B**2+D**2)/(4*(A**2+C**2))))==-Delta**2

# Direct deck-centralizer computation.
u,t,p,q=sp.symbols('u t p q')
eps=(p*u+d*q)/(-q*u-p)
expr=sp.together(eps+d/eps)
num,den=expr.as_numer_denom()
mod=sp.Poly(u**2-t*u+d,u)
def rem(z): return sp.rem(sp.Poly(sp.expand(z),u),mod).as_expr()
T=sp.factor(rem(num)/rem(den))
assert T==-(4*d*p*q+d*q**2*t+p**2*t)/(d*q**2+p**2+p*q*t)

print('R504_NONSPLIT_TRANSPORTED_INVOLUTIONS=PASS')
print('R504_NONSPLIT_N1_LIFT_DISCRIMINANT=DELTA_SQUARED')
print('R504_NONSPLIT_N2_LIFT_DISCRIMINANT=DELTA_SQUARED')
print('R504_NONSPLIT_N3_LIFT_OBSTRUCTION=MINUS_DELTA_SQUARED')
print('R504_NONSPLIT_COMMUTING_LIFT_CLASSIFICATION=PASS')
