#!/usr/bin/env python3
"""Generator-level exact checks for Stage30-06.

This script validates the frozen mathematical derivation only.  It deliberately
does NOT replace the independent exhaustive all-24-element Codex verification
required at Stage30-06C.
"""
from itertools import product

COORDS = ("a1","a2","a3","b1","b2","b3","c")
N = len(COORDS)

# A monomial projective transformation is represented output-wise by
# (i_exponent mod 4, source_coordinate_index).
def unit_mul(a,b): return (a+b) % 4
def unit_inv(a): return (-a) % 4
def unit_conj(a): return (-a) % 4

def compose(A,B):
    # A o B
    out=[]
    for ua,ka in A:
        ub,kb=B[ka]
        out.append((unit_mul(ua,ub),kb))
    return tuple(out)

def identity(): return tuple((0,j) for j in range(N))

def inverse(A):
    out=[None]*N
    for j,(u,k) in enumerate(A):
        out[k]=(unit_inv(u),j)
    return tuple(out)

def conjugate_coeffs(A):
    return tuple((unit_conj(u),k) for u,k in A)

def projectively_equal(A,B):
    shift=None
    for (ua,ka),(ub,kb) in zip(A,B):
        if ka != kb: return False
        d=(ua-ub)%4
        if shift is None: shift=d
        elif d != shift: return False
    return True

def power(A,n):
    z=identity()
    for _ in range(n): z=compose(A,z)
    return z

def diag_sign(negated):
    neg=set(negated)
    return tuple((2 if name in neg else 0,j) for j,name in enumerate(COORDS))

# Frozen lifts from cocycle-derivation.md.
S_HAT = (
    (2,1), # a1 -> -a2
    (2,0), # a2 -> -a1
    (2,2), # a3 -> -a3
    (0,4), # b1 -> b2
    (0,3), # b2 -> b1
    (0,5), # b3 -> b3
    (0,6), # c -> c
)
T_HAT = (
    (2,6), # a1 -> -c
    (1,1), # a2 -> i*a2
    (1,2), # a3 -> i*a3
    (1,3), # b1 -> i*b1
    (0,5), # b2 -> b3
    (0,4), # b3 -> b2
    (2,0), # c -> -a1
)
C_SIGMA = diag_sign(["a3"])

assert projectively_equal(power(S_HAT,2),identity())
assert projectively_equal(power(T_HAT,4),identity())
assert projectively_equal(power(compose(S_HAT,T_HAT),3),identity())

T2=power(T_HAT,2)
S_T2_SINV=compose(compose(S_HAT,T2),inverse(S_HAT))
V14=compose(T2,S_T2_SINV)
assert projectively_equal(T2,diag_sign(["a2","a3","b1"]))
assert projectively_equal(S_T2_SINV,diag_sign(["a1","a3","b2"]))
assert projectively_equal(V14,diag_sign(["a1","a2","b1","b2"]))

# Quadratic descent cocycle.
assert projectively_equal(power(C_SIGMA,2),identity())
assert projectively_equal(conjugate_coeffs(C_SIGMA),C_SIGMA)

# Generator semilinear identities.
assert projectively_equal(
    conjugate_coeffs(S_HAT),
    compose(compose(C_SIGMA,S_HAT),inverse(C_SIGMA)),
)
assert projectively_equal(
    conjugate_coeffs(T_HAT),
    compose(compose(C_SIGMA,inverse(T_HAT)),inverse(C_SIGMA)),
)

# Concrete PSL2(Z/4) ledger and D4-semilinear automorphism.
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%4
                       for j in range(2)) for i in range(2))
def neg(A): return tuple(tuple((-x)%4 for x in row) for row in A)
def canon(A): return min(A,neg(A),key=lambda z:sum(z,()))
def inv2(A):
    d=(A[0][0]*A[1][1]-A[0][1]*A[1][0])%4
    di={1:1,3:3}[d]
    return ((A[1][1]*di%4,(-A[0][1])*di%4),
            ((-A[1][0])*di%4,A[0][0]*di%4))

SL=[((a,b),(c,d)) for a,b,c,d in product(range(4),repeat=4)
    if (a*d-b*c)%4==1]
G=sorted({canon(A) for A in SL},key=lambda z:sum(z,()))
assert len(SL)==48 and len(G)==24
idx={g:i for i,g in enumerate(G)}
mul=[[idx[canon(mm(a,b))] for b in G] for a in G]
E=idx[canon(((1,0),(0,1)))]
S=idx[canon(((0,3),(1,0)))]
T=idx[canon(((1,1),(0,1)))]
D=((1,0),(0,3)); Di=inv2(D)
def theta(i): return idx[canon(mm(mm(D,G[i]),Di))]

assert theta(S)==S
# Find T inverse and verify theta(T)=T^-1.
Tinv=next(j for j in range(24) if mul[T][j]==E and mul[j][T]==E)
assert theta(T)==Tinv

V=sorted(idx[g] for g in G
         if tuple(tuple(x%2 for x in row) for row in g)==((1,0),(0,1)))
assert V==[4,6,12,14]
assert all(theta(v)==v for v in V)
assert mul[T][T]==12
Sinv=next(j for j in range(24) if mul[S][j]==E and mul[j][S]==E)
assert mul[mul[S][12]][Sinv]==6
assert mul[12][6]==14

print("STAGE30_06_FROZEN_GENERATOR_CHECK=PASS")
print("PGL_S_ORDER=2")
print("PGL_T_ORDER=4")
print("PGL_ST_ORDER=3")
print("V_MOD_IDS=g04,g06,g12,g14")
print("V4_SIGN_DECK_LIFT_GENERATOR_CHECK=PASS")
print("THETA_S=S")
print("THETA_T=T^-1")
print("THETA_FIXES_V_MOD_POINTWISE=true")
print("C_SIGMA=delta_a3")
print("C_SIGMA_COCYCLE_IDENTITY=PASS")
print("GENERATOR_SEMILINEAR_IDENTITIES=PASS")
print("ALL24_SEMILINEAR_VERIFICATION_DEFERRED_TO_CODEX_30_06C=true")
print("DEFECT_ELIMINATION_COUNT=0")
print("PERFECT_CUBOID_EXISTENCE_CLAIM=false")
print("PERFECT_CUBOID_NONEXISTENCE_CLAIM=false")
