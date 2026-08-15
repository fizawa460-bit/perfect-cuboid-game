#!/usr/bin/env python3
import sympy as sp

u=sp.symbols('u')
N=u**2+4*u-3
M=7-u**2
H=sp.expand(N**4+M**4)
F=u**4+2*u**2-16*u+17
G=u**4+8*u**3+26*u**2+56*u+73
S=u**4+4*u**3+22*u**2+36*u+53

assert sp.factor(H-2*F*G)==0
assert sp.factor(F**2+G**2-2*S**2)==0

P=(sp.factor(-4*N**2*M**2),sp.factor(4*N*M*(N**4-M**4)))
R=(sp.factor(4*S**2),sp.factor(4*S*(F**2-G**2)))

def on_curve(Q):
    x,y=Q
    return sp.factor(y**2-x**3+4*H**2*x)==0

assert on_curve(P)
assert on_curve(R)

def add(P,Q):
    x1,y1=P; x2,y2=Q
    if sp.factor(x1-x2)==0:
        lam=sp.factor((3*x1**2-4*H**2)/(2*y1))
    else:
        lam=sp.factor((y2-y1)/(x2-x1))
    x3=sp.factor(lam**2-x1-x2)
    y3=sp.factor(-y1+lam*(x1-x3))
    return x3,y3

PR=add(P,R)
PmR=add(P,(R[0],-R[1]))
R2=add(R,R)
P2R=add(P,R2)

# The first two combinations checked here do not lie on the physical Q(u)-quartic cover.
# Their recovered t^2 is a rational square times a nonsquare rational constant.
Tplus=u**4+4*u**3+6*u**2+4*u-107
Tminus=u**4+4*u**3+6*u**2+4*u-11
rp_plus=sp.factor(8*(u+1)**3*Tplus/((u**2-4*u+13)*(u**2+8*u+25)))
rp_minus=sp.factor(16*(u+1)*Tminus/((u**2+1)*(u**2+4*u+5)))
assert sp.factor(PR[0]+4*rp_plus**2)==0
assert sp.factor(PmR[0]+4*rp_minus**2)==0
assert sp.factor((4*H+PR[1]/rp_plus)/(8*rp_plus**2)-Tplus**2/(32*(u+1)**6))==0
assert sp.factor((4*H+PmR[1]/rp_minus)/(8*rp_minus**2)-Tminus**2/(128*(u+1)**2))==0

A=u**10+4*u**9-15*u**8-320*u**7-1814*u**6-5976*u**5-14686*u**4-19936*u**3-29883*u**2-14284*u-64099
B=u**10+16*u**9+93*u**8+464*u**7+1658*u**6+4368*u**5+6346*u**4-2576*u**3-38763*u**2-82272*u-119319
C=u**16+16*u**15+216*u**14+1904*u**13+11532*u**12+51024*u**11+176584*u**10+498992*u**9+1465974*u**8+4632112*u**7+16670632*u**6+49968720*u**5+132646892*u**4+257203824*u**3+414710328*u**2+414710032*u+297433361

assert sp.factor(P2R[0]+4*(A*B/C)**2)==0
assert sp.factor(A**4+B**4-H*C**2)==0

# Physical Stage19 family, dehomogenized at b=1.
E=sp.factor(2*N*M*A*B)
X=sp.factor(N**2*B**2-M**2*A**2)
Y=sp.factor(N**2*A**2-M**2*B**2)
D=sp.factor(H*C)
HX=sp.factor(N**2*B**2+M**2*A**2)
HY=sp.factor(N**2*A**2+M**2*B**2)
assert sp.factor(E**2+X**2-HX**2)==0
assert sp.factor(E**2+Y**2-HY**2)==0
assert sp.factor(E**2+X**2+Y**2-D**2)==0
for q in (E,X,Y,D,HX,HY):
    assert sp.degree(q,u)<=24
assert max(sp.degree(q,u) for q in (E,X,Y,D))==24

# Resultant support for bounded primitive gcd.
assert sp.resultant(N,M,u)==-96
resAB=abs(int(sp.resultant(A,B,u)))
assert sp.factorint(resAB)=={2:115,3:49}

# Missing third face: square part times a squarefree degree-44 factor.
missing=sp.factor(X**2+Y**2)
fac=sp.factor_list(missing)
assert fac[0]==256
assert sorted((sp.degree(q,u),e) for q,e in fac[1])==[(1,2),(8,1),(12,1),(12,1),(12,1)]
Q44=sp.prod(q for q,e in fac[1] if e%2==1)
assert sp.degree(Q44,u)==44
Q11=sp.Poly(Q44,u,modulus=11)
assert sp.gcd(Q11,Q11.diff()).degree()==0

# Nonconstant multiplicity witness.
r0=sp.Rational(E.subs(u,0),X.subs(u,0))
r1=sp.Rational(E.subs(u,1),X.subs(u,1))
assert r0!=r1

print('R504_SECOND_POLYNOMIAL_MW_SECTION=PASS')
print('R504_P_PLUS_R_PHYSICAL_LIFT=false')
print('R504_P_MINUS_R_PHYSICAL_LIFT=false')
print('R504_P_PLUS_2R_PHYSICAL_LIFT=PASS')
print('R504_P_PLUS_2R_QUARTIC_IDENTITY=PASS')
print('R504_P_PLUS_2R_PHYSICAL_HEIGHT_DEGREE=24')
print('R504_P_PLUS_2R_PRIMITIVE_GCD_BOUND=O(1)')
print('R504_P_PLUS_2R_THIRD_FACE_EXCEPTION_GENUS=21')
print('R504_P_PLUS_2R_EXACT_FAMILY_GROWTH=Theta(B^(1/12))')
print('GLOBAL_STAGE25_LOWER_CHANGED=false')
