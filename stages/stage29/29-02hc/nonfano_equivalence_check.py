#!/usr/bin/env python3
"""Exact adversarial checks for Stage29-02hc.

Certifies the branch-arrangement identification but also tests the load-bearing
Q-form issue: whether any PGL3(Q) equivalence lifts from the cuboid sign cover
to the standard non-Fano N=2 Kummer cover.  It also separates Suciu's central
unbranched congruence cover from the projective 64-sheet endpoint open cover.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

CUBOID = [
    (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1), (1,1,1),
]
NONFANO = [
    (1,0,0), (0,1,0), (0,0,1),
    (1,-1,0), (1,0,-1), (0,1,-1), (1,1,-1),
]
# Dual action for x=X, y=-Y, z=Z-X.
A0 = [[Fraction(1),0,-1],[0,-1,0],[0,0,1]]
# Under A0 the cuboid frame {x,y,z,x+y+z} maps to this NF frame.
NF_FRAME = (0,1,4,5)


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def inv3(m):
    d=det3(m); assert d
    a,b,c=m[0]; d0,e,f=m[1]; g,h,i=m[2]
    cof=[[e*i-f*h, -(d0*i-f*g), d0*h-e*g],
         [-(b*i-c*h), a*i-c*g, -(a*h-b*g)],
         [b*f-c*e, -(a*f-c*d0), a*e-b*d0]]
    return [[Fraction(cof[j][r],d) for j in range(3)] for r in range(3)]


def matvec(m,v):
    return tuple(sum(Fraction(m[r][c])*v[c] for c in range(3)) for r in range(3))


def matmul(a,b):
    return [[sum(Fraction(a[i][k])*Fraction(b[k][j]) for k in range(3))
             for j in range(3)] for i in range(3)]


def matcols(cols):
    return [[Fraction(cols[c][r]) for c in range(3)] for r in range(3)]


def proportional_scalar(v,w):
    lam=None
    for vi,wi in zip(v,w):
        vi,wi=Fraction(vi),Fraction(wi)
        if wi:
            q=vi/wi
            if lam is None: lam=q
            elif q != lam: return None
        elif vi:
            return None
    return lam


def squareclass_q(q):
    q=Fraction(q); sign=-1 if q<0 else 1
    parity={}
    for value in (abs(q.numerator),q.denominator):
        p=2
        while p*p<=value:
            while value%p==0:
                parity[p]=parity.get(p,0)^1; value//=p
            p+=1
        if value>1: parity[value]=parity.get(value,0)^1
    out=sign
    for p,bit in parity.items():
        if bit: out*=p
    return out


def frame_projectivity(lines,frame,targets):
    src=[lines[i] for i in frame]; tgt=[lines[i] for i in targets]
    s=matcols(src[:3]); t=matcols(tgt[:3])
    sinv=inv3(s); tinv=inv3(t)
    cs=matvec(sinv,src[3]); ct=matvec(tinv,tgt[3])
    lam=[ct[j]/cs[j] for j in range(3)]
    ds=[[lam[i]*sinv[i][j] for j in range(3)] for i in range(3)]
    return [[sum(t[r][k]*ds[k][c] for k in range(3)) for c in range(3)]
            for r in range(3)]


def line_action(m,source,target):
    mapping=[]; scalars=[]
    for v in source:
        mv=matvec(m,v)
        matches=[]
        for j,w in enumerate(target):
            lam=proportional_scalar(mv,w)
            if lam not in (None,0): matches.append((j,lam))
        assert len(matches)==1
        mapping.append(matches[0][0]); scalars.append(matches[0][1])
    assert len(set(mapping))==7
    return mapping,scalars


# Displayed branch equivalence and its nontrivial Q-squareclass cocycle.
display_map,display_scalars=line_action(A0,CUBOID,NONFANO)
assert display_map == [0,1,4,3,2,6,5]
display_classes=[squareclass_q(x) for x in display_scalars]
assert display_classes == [1,-1,-1,1,1,-1,-1]
ref=display_classes[6]
relative=[c*ref for c in display_classes[:6]]
assert relative == [-1,1,1,-1,-1,1]

# Exhaust all 24 PGL3(Q) equivalences.  Every such equivalence is a fixed A0
# followed by an automorphism of the standard NF arrangement.
autos=[]; seen=set()
for targets in permutations(NF_FRAME):
    b=frame_projectivity(NONFANO,NF_FRAME,targets)
    mapping,_=line_action(b,NONFANO,NONFANO)
    key=tuple(mapping)
    if key not in seen:
        seen.add(key); autos.append(b)
assert len(autos)==24

eq_classes=[]
for b in autos:
    m=matmul(b,A0)
    _,scalars=line_action(m,CUBOID,NONFANO)
    eq_classes.append([squareclass_q(s) for s in scalars])
assert len(eq_classes)==24
q_lifts=sum(len(set(c))==1 for c in eq_classes)
assert q_lifts==0
# All occurring classes are +/-1; adjoining i kills the only obstruction.
assert all(set(abs(x) for x in c)=={1} for c in eq_classes)
qi_lifts=24
# Count patterns modulo an irrelevant common -1 multiplier.
pattern_counts=Counter(min(sum(x==-1 for x in c),sum(x==1 for x in c)) for c in eq_classes)
assert pattern_counts == Counter({2:12,3:6,1:6})

# Incidence ledger.
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def canon(v):
    v=tuple(Fraction(x) for x in v)
    for x in v:
        if x: return tuple(y/x for y in v)
    raise ValueError("zero vector")

def dot(a,b): return sum(x*y for x,y in zip(a,b))
pts={}
for i,j in combinations(range(7),2):
    p=canon(cross(CUBOID[i],CUBOID[j]))
    pts[p]={k for k,l in enumerate(CUBOID) if dot(l,p)==0}
assert sum(len(v)==3 for v in pts.values())==6
assert sum(len(v)==2 for v in pts.values())==3
assert len(pts)==9

# Hirzebruch N=2 compact invariants.
N=2; n=7; s=9; m2=3; m3=6
b2=m2+2*m3; assert b2==15
degree=N**(n-1); triple_fiber=N**(n-1-3); nodes=m3*triple_fiber
c1sq=((3*b2-s-5*n+9)*N*N-4*(b2-n)*N+(b2+n+m2))*N**(n-3)
c2=((b2-2*n+3)*N*N-2*(b2-n)*N+(b2+s-m2))*N**(n-3)
compact_b1=9*(N-1)*(N-2)
q=compact_b1//2; chi=(c1sq+c2)//12; pg=chi-1+q
assert (degree,triple_fiber,nodes,c1sq,c2,compact_b1,q,chi,pg)==(64,8,48,16,80,0,0,8,7)

# Suciu Example 10.5's X_N formula is for the central arrangement cover.
# Since G ~= G_projective x Z, the projective cover removes the C* factor.
central_open_b1=9*N*N-3
projective_open_b1=central_open_b1-1
assert (central_open_b1,projective_open_b1)==(33,32)

print("PGL3_Q_BRANCH_EQUIVALENCE=PASS")
print("PGL3_Q_EQUIVALENCES_TOTAL=24")
print("STANDARD_NF_Q_COVER_LIFTABLE_EQUIVALENCES=0")
print("QI_COVER_LIFTABLE_EQUIVALENCES=24")
print("DISPLAYED_LINE_MULTIPLIER_CLASSES=+,-,-,+,+,-,-")
print("DISPLAYED_RELATIVE_TWIST=-,+,+,-,-,+")
print("Q_FORM_STANDARD_NF_COVER_IDENTIFICATION=FAIL_AS_STATED")
print("QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=PASS")
print("INCIDENCE=t3:6,t2:3,total:9")
print("HIRZEBRUCH_N2_DEGREE=64")
print("TRIPLE_FIBER=8")
print("NODES=48")
print("C1SQ=16")
print("C2=80")
print("COMPACT_B1=0")
print("Q=0")
print("CHI_O=8")
print("PG=7")
print("CENTRAL_OPEN_B1_N2=33")
print("PROJECTIVE_OPEN_B1_N2=32")
