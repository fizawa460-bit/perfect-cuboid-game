"""Stage35EX C35-09: direct O_K/8 coset membership, no c3_selmer vec_2 / coords_unit2 / unit_class_basis.
Uses *exact* K integral-basis multiplication + norm from kfield/c3_selmer, checks field arithmetic.
Combines independent C35-07 p3461 residues and 2 real root sign witnesses.
"""
from fractions import Fraction as F
from itertools import product
import sys,os
sys.path.insert(0,os.path.dirname(__file__))
import c3_selmer as S
import independent_3461 as P3
import kfield as KF
p=2
z=(0,0,0,0,0,0)
o=(1,0,0,0,0,0)
# Independent multiplication from polynomial arithmetic & rational basis vector conversion.
assert all(KF.to_basis(KF.polmulmod(KF.B[i],KF.B[j]))==list(map(F,KF.MTi[i][j])) for i in range(6) for j in range(6))
def m8(x,y):
    return tuple(sum(x[i]*y[j]*int(KF.MTi[i][j][k]) for i in range(6) for j in range(6))%8 for k in range(6))
# Construct complete exact set of square units modulo 8 (squares mod8 depend only on residues mod4).
R2=[]
for x in product(range(2),repeat=6):
    if int(S.norm(list(map(F,x))))%2==1:R2.append(x)
assert len(R2)==48,('unit mod2 wrong',len(R2))
SQ8={m8(x,x) for x in product(range(4),repeat=6) if (tuple(v%2 for v in x) in R2)}
assert len(SQ8)==1536
assert (len(R2)*4**6)//len(SQ8)==128
S.PI2=[F(x) for x in (-2,-1,1,2,1,0)]
pi2=S.PI2
assert S.norm(pi2)==4

def qc(a):
    va=S.v2(a)
    aa=F(a)/F(2)**va
    assert aa.denominator%2==1
    return (va%2,int(aa.numerator*pow(aa.denominator,-1,8)%8))
def kcls(alpha):
    q=S.norm(alpha); nv=S.v2(q)
    assert nv%2==0
    v=nv//2
    alpha_u=S.mul(alpha,S.pw(pi2,-v))
    u=tuple(int(c.numerator*pow(c.denominator,-1,8)%8) for c in alpha_u)
    assert int(S.norm(list(map(F,u))))%2==1
    return v%2,u

def lc(a,alpha):
    (va,qu)=qc(a);v,u=kcls(alpha)
    return (va,qu,v,u)
def mult(a,b):
    return (a[0]^b[0],a[1]*b[1]%8,a[2]^b[2],m8(a[3],b[3]))
identity=(0,1,0,o)
def equals(a,b):
    return a[:3]==b[:3] and m8(a[3],b[3]) in SQ8

# Local witness validity from exact polynomial evaluation plus 2-adic Hensel (no random sqrt oracle).
def prodquad(v,w,c,d):
    a,b=v;A,B=w
    return (a*A+c*b*B,a*B+b*A+d*b*B)
def eval_quad_ft(z,c,d):
    out=(0,0)
    for coef in [0,-1,5,-8,5,-8,5,1][::-1]:
        out=prodquad(out,z,c,d)
        out=(out[0]+coef,out[1])
    return out
# Rational x=-180: v2(ft(x))=2 and the unit part is 1 modulo 8.
fx=S.ft(F(-180))
assert S.v2(fx)==2 and S.frac_mod(fx/F(4),8)==1
# beta²=-1014 ramified quadratic: (1+6beta)^2=ft(29+beta) mod16.
r=eval_quad_ft((29,1),-1014,0)
assert r==(255954225577,-4752847252)
y0=prodquad((1,6),(1,6),-1014,0)
assert all((i-j)%16==0 for i,j in zip(r,y0))
# alpha²=alpha+1 unramified quadratic: (4+3alpha)^2=ft(16+alpha)/16 mod16.
r=eval_quad_ft((16,1),1,1)
assert r==(373869200,178849552) and all(v%16==0 for v in r)
y0=prodquad((4,3),(4,3),1,1)
assert all((i//16-j)%16==0 for i,j in zip(r,y0))
# Unit roots modulo local maximal ideals; 16O provides v(error)>2v(2).
print('EXPLICIT_Q2_QUADRATIC_WITNESS_HENSEL_PASS')
# Exact four legitimate Jacobian 2-classes over Q2 via C35-06 Hensel checks
witness_raw=[(F(-1),S.T_EL),(F(-180),S.point_image(F(-180))[1]),
    (F(1855),S.from_pow([1855,58,1])),(F(271),S.from_pow([271,33,1]))]
witnesses=[lc(a,b) for a,b in witness_raw]
ws=[]
for mask in range(16):
    v=identity
    for j,w in enumerate(witnesses):
        if mask>>j&1:v=mult(v,w)
    ws.append(v)
assert all(not equals(ws[i],ws[j]) for i in range(16) for j in range(i+1,16))
print('DIRECT_Q2_4_WITNESSES_INDEPENDENT_PASS')
print('O_K_mod8 units',len(R2)*4**6,'square units',len(SQ8),'classes',128)
print('original-coordinate-free p2 local witness cosets verified',len(ws))

# Combine exact global seven S generators, using *separate* 3461 residue-field evaluator.
Sgen=P3.GEN
l2=[lc(S.norm(g),g) for g in Sgen]
# Real signed embeddings: exact rational isolating intervals and rational interval arithmetic.
import sympy as sp
zsym=sp.Symbol('t')
Pexact=sum(F(c)*zsym**i for i,c in enumerate(KF.P))
assert sp.Poly(Pexact,zsym).count_roots(-sp.oo,sp.oo)==2
root_bounds=[(F(-1138303094908890,10**15),F(-1138303094908888,10**15)),(F(6404530824861865,10**15),F(6404530824861868,10**15))]
def po_eval(cs,z):
    v=F(0)
    for c in cs[::-1]:v=v*z+c
    return v
for lo,hi in root_bounds:
    assert po_eval(KF.P,lo)*po_eval(KF.P,hi)<0

def interval_horner(cs,lo,hi):
    l=F(0);r=F(0)
    for c in cs[::-1]:
        vals=(l*lo,l*hi,r*lo,r*hi)
        l=min(vals)+c;r=max(vals)+c
    return l,r

def real_vec(a,alpha):
    cs=KF.to_pow(alpha)
    out=[0 if a>0 else 1]
    for lo,hi in root_bounds:
        l,r=interval_horner(cs,lo,hi)
        assert l>0 or r<0,('interval sign unproven',l,r)
        out.append(0 if l>0 else 1)
    return out
inf=[real_vec(S.norm(g),g) for g in Sgen]
realW=real_vec(*S.point_image(F(0)))
assert inf==[S.vec_inf(S.norm(g),g) for g in Sgen]
assert realW==S.vec_inf(*S.point_image(F(0)))
print('EXACT_RATIONAL_INTERVAL_REAL_SIGNS_PASS')
L3461=P3.xs
assert len(l2)==len(inf)==len(L3461)==7
# P3 class_unit receives (alpha,n); point_image returns (n,alpha)
p3461_span=[]
for x in (-99,-98):
    n,a=S.point_image(F(x))
    p3461_span.append(P3.class_unit(a,n))
assert p3461_span==[[0,1,0,0,0,1],[0,1,0,1,0,1]]

def vxor(a,b):return [i^j for i,j in zip(a,b)]
def local_real_in_span(v):return v==[0,0,0] or v==realW
def local3461_in_span(v):return any(v==vxor(vxor([0]*6, p3461_span[0] if (mask&1) else [0]*6),p3461_span[1] if(mask&2) else [0]*6) for mask in range(4))
survivors=[];passed_inf=[];passed_p2=[];passed_p3=[]
for mask in range(128):
    v2=identity;vR=[0,0,0];v3=[0]*6
    for j in range(7):
        if mask>>j&1:
            v2=mult(v2,l2[j]);vR=vxor(vR,inf[j]);v3=vxor(v3,L3461[j])
    r0=local_real_in_span(vR)
    r2=any(equals(v2,w) for w in ws)
    r3=local3461_in_span(v3)
    if r0:passed_inf.append(mask)
    if r2:passed_p2.append(mask)
    if r3:passed_p3.append(mask)
    if r0 and r2 and r3:survivors.append(mask)
print('surviving after real',len(passed_inf),'after Q2',len(passed_p2),'after Q3461',len(passed_p3))
print('FULL_DIRECT_Q2_COSET_AND_INDEPENDENT_P3461_SURVIVORS',survivors)
assert survivors==[0,3,5,6]
print('PASS_DIRECT_2ADIC_SQUARE_COSET_SEL2_DIM2')
