#!/usr/bin/env python3
"""Stage35EX C35-10: exact symbolic Selmer-class & signed6 downstream bridge.
Python3+SymPy. No external tools, no numerical roots.
Proof of algebraic identities only, NOT final upstream physical-mask certification.
"""
import sympy as S
T=S.symbols('t'); u=S.symbols('u');D,V,B=S.symbols('D V B', nonzero=True)
P=T**6-5*T**5-8*T**4-5*T**3-8*T**2-5*T-1
U1=(-1-17*T-5*T**2-13*T**3-17*T**4+3*T**5)/4
U2=(13+40*T+11*T**2+32*T**3+33*T**4-6*T**5)/4
R_T=(5+17*T+5*T**2+13*T**3+17*T**4-3*T**5)/4
R_D=(-9-19*T-9*T**2-25*T**3-15*T**4+3*T**5)/4
red=lambda p:S.rem(S.Poly(S.expand(p),T,domain=S.QQ), S.Poly(P,T,domain=S.QQ)).as_expr()
assert S.expand(red(R_T**2*U2+T))==0
assert S.expand(red(R_D**2*U1*U2-(T**2+T-1)))==0
assert S.resultant(P,T,T)==-1  # N_K/Q(t)=-1
assert S.resultant(P,T**2+T-1,T)==-256
f=lambda x:S.expand(x*P.subs(T,-x))
X=S.symbols('x');curve=f(X)
assert S.rem(curve-16*X**2,X**2-X-1,X)==0
print('PASS_EXPLICIT_GLOBAL_KUMMER_SQUARE_ROOTS: T0 -> -U2, D2 -> U1U2')
# E:y^2=x^3+B^2 x^2-D^2 x, P_orig=(D,B D)
# 2P_orig has coordinates (D^2/B^2, -D^3/B^3).
m=(D+B**2)/B
x2=S.factor(m**2-B**2-2*D)
y2=S.factor(-B*D+m*(D-x2))
assert S.simplify(x2-D**2/B**2)==0
assert S.simplify(y2+D**3/B**3)==0
assert S.simplify((B**2*x2)-D**2)==0
assert S.simplify((B**3*y2)+D**3)==0
print('PASS_ELLIPTIC_2P_SCALE: Rstar=(D^2,-D^3)')
# General E*: doubling has square x-coordinate, and translation by T0 has x=b/x.
z,a,b=S.symbols('z a b', nonzero=True)
fy=z**3+a*z**2+b*z
xd=S.factor((3*z**2+2*a*z+b)**2/(4*fy)-a-2*z)
assert S.factor(xd-(z**2-b)**2/(4*fy))==0
assert S.factor(fy/z**2-a-z-b/z)==0
print('PASS_EVEN_MULTIPLE_X_SQUARE_AND_TRANSLATE_T0_B_OVER_X')

# Independent psi2,psi3,psi4 formulas for E*: Y^2=X^3+VX^2-D^2 V X.
b2=4*V;b4=-2*D**2*V;b6=0;b8=-D**4*V**2
psi2=-2*D**3
xx=D**2
psi3=S.expand(3*xx**4+b2*xx**3+3*b4*xx**2+3*b6*xx+b8)
psi4=S.expand(psi2*(2*xx**6+b2*xx**5+5*b4*xx**4+10*b6*xx**3+10*b8*xx**2+(b2*b8-b4*b6)*xx+b4*b8-b6**2))
assert S.expand(psi3-D**4*(D**2-V)*(3*D**2+V))==0
assert S.expand(psi4+4*D**9*(D**6-3*V*D**4-5*V**2*D**2-V**3))==0
W5=S.expand(psi4*psi2**3-psi3**3)
W7=S.expand(W5*psi3**3-psi2*psi4**3)
F=V**3+D**2*V**2-13*D**4*V-5*D**6
G=V**3+5*D**2*V**2+11*D**4*V-D**6
H1=V**6+2*D**2*V**5-33*D**4*V**4-116*D**6*V**3-65*D**8*V**2-46*D**10*V+D**12
H2=V**6+10*D**2*V**5+55*D**4*V**4+156*D**6*V**3+111*D**8*V**2-70*D**10*V-7*D**12
assert S.expand(W5-D**12*F*G)==0
assert S.expand(W7+D**24*H1*H2)==0
print('PASS_INDEPENDENT_DIVISION_POLYNOMIALS_W5_W7')
q=u*(u+1)
P_u=P.subs(T,u)
Q_u=S.expand(P_u.subs(u,-1-u))
h1q=1+2*q-33*q**2-116*q**3-65*q**4-46*q**5+q**6
assert S.expand(h1q-P_u*Q_u)==0
assert S.expand(Q_u-P_u.subs(u,-1-u))==0
print('PASS_H1_SPLIT_PQ_AND_REFLECTION')
# For B-odd primitive Pythagorean A even, 4|A and gcd(B,AC)=1.
# For even n=6, translate by 2-torsion T0: X(T0+nR*)=-D^2 V/X(nR*)
# Thus sigma_n=B^2*(1-D^2/X(nR*)) where X(nR*) is a rational square.
# psi-identity phi_n=D^2 W_n^2-W_{n-1}W_{n+1}, and phi_n=X(nR*) W_n^2 is itself a square.
# Therefore sigma_n= -(B/sqrt(phi_n))^2 W_{n-1}W_{n+1}.
# Its square forces -W5 W7 to be square, and coprime odd 1 mod8 blocks F,G,H1,H2 square.
# H1 splits K=B^12 P(u), L=B^12Q(u), each 7mod8 and gcd(K,L)=1,
# so K,L are negative integer squares; then -P(u) rational square.
assert S.factor(-W5*W7-D**36*F*G*H1*H2)==0
# Original u=t^2, y^2=-P(u), C3: Y^2=-uP(u) via Y=t*y; C3' x=-t^2.
assert S.expand(f(-u)-(-u*P_u))==0
print('PASS_RECEIVER_MAP_C3PRIME: x=-t^2, Y=t*y; branch x!=0 for A>0')
print('SCOPE: conditional on S263 sigma_6 square and S321/S322 gcd/sign hypotheses; no original upstream physical Q-mask proof')
