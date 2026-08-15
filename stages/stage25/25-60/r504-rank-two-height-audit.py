#!/usr/bin/env python3
import sympy as sp

u=sp.symbols('u')
N=u**2+4*u-3
M=7-u**2
H=sp.expand(N**4+M**4)
F=u**4+2*u**2-16*u+17
G=u**4+8*u**3+26*u**2+56*u+73
S=u**4+4*u**3+22*u**2+36*u+53

# V4 involutions and exact differential characters.
delta=-(u+7)/(u+1)
eps=(5-u)/(u+1)
eps1=-u-2
assert sp.factor(H.subs(u,delta)-1296*H/(u+1)**8)==0
assert sp.factor(H.subs(u,eps)-1296*H/(u+1)**8)==0
assert sp.factor(H.subs(u,eps1)-H)==0

omega_P=u**2+2*u+7
omega_R=u**2+2*u-5

def pull_ratio(f,g,yscale):
    return sp.factor(f.subs(u,g)*sp.diff(g,u)/(yscale*f))

assert pull_ratio(omega_P,delta,36/(u+1)**4)==1
assert pull_ratio(omega_P,eps,36/(u+1)**4)==-1
assert pull_ratio(omega_R,delta,36/(u+1)**4)==-1
assert pull_ratio(omega_R,eps,36/(u+1)**4)==1

# Fast exact arithmetic in Q(u).
K=sp.QQ.frac_field(u)
def KQ(expr):
    return K.from_sympy(expr)

Nk=KQ(N); Mk=KQ(M); Hk=KQ(H)
Fk=KQ(F); Gk=KQ(G); Sk=KQ(S)
P=(-4*Nk**2*Mk**2,4*Nk*Mk*(Nk**4-Mk**4))
R=(4*Sk**2,4*Sk*(Fk**2-Gk**2))

def neg(Q):
    return None if Q is None else (Q[0],-Q[1])

def add(A,B):
    if A is None:
        return B
    if B is None:
        return A
    x1,y1=A; x2,y2=B
    if x1==x2:
        if y1==-y2:
            return None
        lam=(3*x1*x1-4*Hk*Hk)/(2*y1)
    else:
        lam=(y2-y1)/(x2-x1)
    x3=lam*lam-x1-x2
    y3=-y1+lam*(x1-x3)
    return x3,y3

def mul(n,Q):
    if n<0:
        return neg(mul(-n,Q))
    out=None
    base=Q
    while n:
        if n&1:
            out=add(out,base)
        n//=2
        if n:
            base=add(base,base)
    return out

def degree_rf(f):
    return max(f.numer.degree(),f.denom.degree())

def degree_x_over_H(a,b):
    Q=add(mul(a,P),mul(b,R))
    return degree_rf(Q[0]/Hk)

# Basis norms and representative regression points support the Rosati formula.
assert degree_x_over_H(1,0)==8
assert degree_x_over_H(0,1)==8
for a,b in [(1,1),(1,-1),(1,2),(1,-2),(3,0),(3,2)]:
    assert degree_x_over_H(a,b)==8*(a*a+b*b)

# The physical x/H receiver is degree four in t.
t=sp.symbols('t')
psi=sp.cancel(-4*t**2/(t**4+1))
psi_num,psi_den=psi.as_numer_denom()
assert max(sp.degree(psi_num,t),sp.degree(psi_den,t))==4

# Prior hostile-audited P+2R witness remains a valid norm-5 physical class.
A=u**10+4*u**9-15*u**8-320*u**7-1814*u**6-5976*u**5-14686*u**4-19936*u**3-29883*u**2-14284*u-64099
B=u**10+16*u**9+93*u**8+464*u**7+1658*u**6+4368*u**5+6346*u**4-2576*u**3-38763*u**2-82272*u-119319
C=u**16+16*u**15+216*u**14+1904*u**13+11532*u**12+51024*u**11+176584*u**10+498992*u**9+1465974*u**8+4632112*u**7+16670632*u**6+49968720*u**5+132646892*u**4+257203824*u**3+414710328*u**2+414710032*u+297433361
assert sp.factor(A**4+B**4-H*C**2)==0
assert max(sp.degree(A,u),sp.degree(B,u))==10
assert sp.degree(H*C,u)==24

# Conditional enumeration only: IF the physical coset is proved to be a odd / b even,
# then norm 1 is +/-P and the next norm is 5 at +/-P +/-2R.
# This script does not prove that mod-2 coset identification.
allowed=[]
for a in range(-9,10,2):
    for b in range(-8,9,2):
        n=a*a+b*b
        allowed.append((n,a,b))
allowed.sort()
assert allowed[0][0]==1
nondeg=[row for row in allowed if not (row[0]==1 and row[2]==0)]
assert nondeg[0][0]==5
assert {(a,b) for n,a,b in nondeg if n==5}=={(-1,-2),(-1,2),(1,-2),(1,2)}

print('R504_RANK_TWO_DIFFERENTIAL_CHARACTER_SPLIT=PASS')
print('R504_ROSATI_ORTHOGONALITY_PREMISES=PASS')
print('R504_ROSATI_NORM_P=8')
print('R504_ROSATI_NORM_R=8')
print('R504_RANK_TWO_HEIGHT_FORM_REGRESSION=PASS')
print('R504_PHYSICAL_RECEIVER_X_OVER_H_DEGREE_IN_T=4')
print('R504_PHYSICAL_COSET_PARITY=UNVERIFIED_AUDIT_BLOCKER')
print('R504_CONDITIONAL_A_ODD_B_EVEN_MIN_NORM=5')
print('R504_P_PLUS_2R_PREVIOUS_PHYSICAL_WITNESS=PASS')
print('R504_RANK_TWO_GROWING_LATTICE_UNIFORM_AGGREGATION_PROVED=false')
print('GLOBAL_STAGE25_LOWER_CHANGED=false')
