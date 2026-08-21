#!/usr/bin/env python3
"""Exact dependency-free checks for Stage29-02hc.

Checks:
1. the cuboid seven branch forms are PGL3(Q)-equivalent to Suciu's
   standard non-Fano seven forms;
2. incidence counts are t3=6,t2=3;
3. N=2 Hirzebruch formulas recover degree 64, 48 triple-locus points,
   c1^2=16,c2=80,b1=0,q=0,chi=8,pg=7.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd

CUBOID = [
    (1,0,0), (0,1,0), (0,0,1),
    (1,1,0), (1,0,1), (0,1,1), (1,1,1),
]
NONFANO = [
    (1,0,0), (0,1,0), (0,0,1),
    (1,-1,0), (1,0,-1), (0,1,-1), (1,1,-1),
]

# dual action corresponding to x=X, y=-Y, z=Z-X
A = (
    (1,0,-1),
    (0,-1,0),
    (0,0,1),
)

def matvec(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def canon(v):
    v = tuple(Fraction(x) for x in v)
    for x in v:
        if x:
            return tuple(y/x for y in v)
    raise ValueError("zero vector")

def cross(a,b):
    return (
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    )

def dot(a,b): return sum(x*y for x,y in zip(a,b))

mapped = {canon(matvec(A,v)) for v in CUBOID}
assert mapped == {canon(v) for v in NONFANO}

# Count distinct projective intersections and multiplicities.
pts = {}
for i,j in combinations(range(7),2):
    p = canon(cross(CUBOID[i], CUBOID[j]))
    pts.setdefault(p,set()).update([i,j])
for p in list(pts):
    through={i for i,l in enumerate(CUBOID) if dot(l,p)==0}
    pts[p]=through
mults={2:0,3:0}
for through in pts.values():
    mults[len(through)] = mults.get(len(through),0)+1
assert mults[3]==6
assert mults[2]==3
assert len(pts)==9

N=2
n=7
s=9
m2=3
m3=6
b2=m2*(2-1)+m3*(3-1)  # 15
assert b2==15

degree=N**(n-1)
triple_fiber=N**(n-1-3)
nodes=m3*triple_fiber

c1sq=((3*b2-s-5*n+9)*N*N - 4*(b2-n)*N + (b2+n+m2))*N**(n-3)
c2=((b2-2*n+3)*N*N - 2*(b2-n)*N + (b2+s-m2))*N**(n-3)
b1=9*(N-1)*(N-2)
q=b1//2
chi=(c1sq+c2)//12
pg=chi-1+q

assert degree==64
assert triple_fiber==8
assert nodes==48
assert c1sq==16
assert c2==80
assert b1==0
assert q==0
assert chi==8
assert pg==7

print("PGL3_Q_EQUIVALENCE=PASS")
print("INCIDENCE=t3:6,t2:3,total:9")
print(f"HIRZEBRUCH_N2_DEGREE={degree}")
print(f"TRIPLE_FIBER={triple_fiber}")
print(f"NODES={nodes}")
print(f"C1SQ={c1sq}")
print(f"C2={c2}")
print(f"B1={b1}")
print(f"Q={q}")
print(f"CHI_O={chi}")
print(f"PG={pg}")
