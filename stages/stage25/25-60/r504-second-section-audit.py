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

def add(P,Q):
    x1,y1=P; x2,y2=Q
    if sp.factor(x1-x2)==0:
        lam=sp.factor((3*x1**2-4*H**2)/(2*y1))
    else:
        lam=sp.factor((y2-y1)/(x2-x1))
    x3=sp.factor(lam**2-x1-x2)
    y3=sp.factor(-y1+lam*(x1-x3))
    return x3,y3

assert on_curve(P)
assert on_curve(R)
PR=add(P,R)
PmR=add(P,(R[0],-R[1]))
P2R=add(P,add(R,R))

# P +/- R do not lift over Q(u): recovered t^2 has nonsquare constants.
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

assert sp.factor(A**4+B**4-H*C**2)==0
qx=-4*A**2*B**2/C**2
qy=4*A*B*(A**4-B**4)/C**3
assert sp.factor(P2R[0]-qx)==0
assert sp.factor(P2R[1]-qy)==0

# Original physical quartic point.
t=A/B
z=M**2*C/B**2
k=N/M
assert sp.factor(t**4+1-(k**4+1)*z**2)==0

# Physical Stage19 family.
E=sp.expand(2*N*M*A*B)
X=sp.expand(N**2*B**2-M**2*A**2)
Y=sp.expand(N**2*A**2-M**2*B**2)
D=sp.expand(H*C)
HX=sp.expand(N**2*B**2+M**2*A**2)
HY=sp.expand(N**2*A**2+M**2*B**2)
assert sp.factor(E**2+X**2-HX**2)==0
assert sp.factor(E**2+Y**2-HY**2)==0
assert sp.factor(E**2+X**2+Y**2-D**2)==0
assert [sp.degree(q,u) for q in (E,X,Y,D)]==[24,23,23,24]
vals3=[int(q.subs(u,3)) for q in (E,X,Y,D)]
assert all(v>0 for v in vals3)
assert vals3[0]<vals3[1]<vals3[2]<vals3[3]

# Direct absolute primitive-gcd certificate.
resEX=abs(int(sp.resultant(sp.expand(E/2),X,u)))
resEY=abs(int(sp.resultant(sp.expand(E/2),Y,u)))
assert sp.factorint(resEX)=={2:688,3:256}
assert sp.factorint(resEY)=={2:656,3:272,7:8}

# Missing third face: square part times a squarefree degree-44 factor.
missing=sp.factor(X**2+Y**2)
fac=sp.factor_list(missing)
assert fac[0]==256
assert sorted((sp.degree(q,u),e) for q,e in fac[1])==[(1,2),(8,1),(12,1),(12,1),(12,1)]
Q44=sp.prod(q for q,e in fac[1] if e%2==1)
assert sp.degree(Q44,u)==44
Q11=sp.Poly(Q44,u,modulus=11)
assert Q11.degree()==44
assert sp.gcd(Q11,Q11.diff()).degree()==0

# Bounded multiplicity witness.
ratio=sp.cancel(E/X)
num,den=ratio.as_numer_denom()
assert sp.degree(num,u)<=24 and sp.degree(den,u)<=24
assert sp.factor(sp.diff(ratio,u))!=0

print('R504_SECOND_POLYNOMIAL_MW_SECTION=PASS')
print('R504_P_PLUS_R_PHYSICAL_LIFT=false')
print('R504_P_MINUS_R_PHYSICAL_LIFT=false')
print('R504_P_PLUS_2R_PHYSICAL_LIFT=PASS')
print('R504_P_PLUS_2R_QUARTIC_IDENTITY=PASS')
print('R504_P_PLUS_2R_PHYSICAL_HEIGHT_DEGREE=24')
print('R504_P_PLUS_2R_PRIMITIVE_GCD_BOUND=2^689*3^256')
print('R504_P_PLUS_2R_THIRD_FACE_EXCEPTION_GENUS=21')
print('R504_P_PLUS_2R_EXACT_FAMILY_GROWTH=Theta(B^(1/12))')
print('GLOBAL_STAGE25_LOWER_CHANGED=false')
