#!/usr/bin/env python3
import sympy as sp

u,t=sp.symbols('u t')
N=u**2+4*u-3
M=7-u**2
H=sp.expand(N**4+M**4)
F=u**4+2*u**2-16*u+17
G=u**4+8*u**3+26*u**2+56*u+73
S=u**4+4*u**3+22*u**2+36*u+53

P=(sp.factor(-4*N**2*M**2),sp.factor(4*N*M*(N**4-M**4)))
R=(sp.factor(4*S**2),sp.factor(4*S*(F**2-G**2)))

def add(A,B):
    x1,y1=A; x2,y2=B
    lam=sp.factor((y2-y1)/(x2-x1))
    x3=sp.factor(lam**2-x1-x2)
    y3=sp.factor(-y1+lam*(x1-x3))
    return x3,y3

def degree_rf(expr,var):
    num,den=sp.cancel(expr).as_numer_denom()
    return max(sp.degree(num,var),sp.degree(den,var))

PR=add(P,R)
assert degree_rf(P[0]/H,u)==8
assert degree_rf(R[0]/H,u)==8
assert degree_rf(PR[0]/H,u)==16

# The physical receiver on the fixed twist has degree four in t.
psi=sp.cancel(-4*t**2/(t**4+1))
assert degree_rf(psi,t)==4

# The hostile-audited physical parity rule has minimum nondegenerate norm five.
allowed=[]
for a in range(-11,12,2):
    for b in range(-10,11,2):
        n=a*a+b*b
        allowed.append((n,a,b))
allowed.sort()
assert allowed[0][0]==1
nondeg=[row for row in allowed if not (row[0]==1 and row[2]==0)]
assert nondeg[0][0]==5
assert {(a,b) for n,a,b in nondeg if n==5}=={(-1,-2),(-1,2),(1,-2),(1,2)}

# Combinatorial aggregation majorant used after the height theorem:
# if n>=5, B^(1/(2n)) <= B^(1/10), and a^2+b^2<=C log B
# contains O(log B) integer pairs.
n=sp.symbols('n', integer=True, positive=True)
assert sp.Rational(1,2*5)==sp.Rational(1,10)
for nn in range(5,200):
    assert sp.Rational(1,2*nn) <= sp.Rational(1,10)

# Crude lattice disk count: pairs with a^2+b^2<=N are <=(2 sqrt(N)+1)^2=O(N).
for NN in [5,10,25,100,500]:
    pts=sum(1 for a in range(-int(NN**0.5)-1,int(NN**0.5)+2)
              for b in range(-int(NN**0.5)-1,int(NN**0.5)+2)
              if a*a+b*b<=NN)
    crude=(2*int(NN**0.5)+3)**2
    assert pts<=crude

print('R504_FIXED_SECTIONS_X_OVER_H_DEGREES=8,8,16')
print('R504_PHYSICAL_RECEIVER_DEGREE_IN_T=4')
print('R504_PHYSICAL_NONDEGENERATE_MIN_NORM=5')
print('R504_PER_CLASS_EXPONENT_MAX_FROM_UNIFORM_HEIGHT=1/10')
print('R504_COEFFICIENT_DISK_COUNT_FOR_N_LE_C_LOG_B=O(log B)')
print('R504_RANK_TWO_GROWING_LATTICE_TARGET_UPPER=O(B^(1/10)*log B)')
print('R504_RANK_TWO_GROWING_LATTICE_QUARTER_UPGRADE=false')
print('NOTE=canonical-height uniformity proof is mathematical, not finite-data certified')
