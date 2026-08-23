#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def assert_square(n, r):
    assert r * r == n

def is_square(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n

# Tiny exact bivariate polynomial ring Q[t,u], keys=(deg_t,deg_u).
def pclean(p):
    return {k: Fraction(v) for k, v in p.items() if v}

def padd(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, Fraction(0)) + v
    return pclean(c)

def pscale(a, s):
    return pclean({k: Fraction(s) * v for k, v in a.items()})

def pmul(a, b):
    c = {}
    for (i,j), x in a.items():
        for (k,l), y in b.items():
            key = (i+k, j+l)
            c[key] = c.get(key, Fraction(0)) + x*y
    return pclean(c)

def ppow(a, n):
    r = {(0,0): Fraction(1)}
    for _ in range(n):
        r = pmul(r, a)
    return r

def const(c): return {(0,0): Fraction(c)}
T = {(1,0): Fraction(1)}
U = {(0,1): Fraction(1)}

# 1. Verify the exact birational derivation identity used in birational-map.json.
# Shift Y=t+1 gives f=t^4+12t^3+48t^2+56t+20 and W^2=20f.
ft = padd(padd(padd(padd(ppow(T,4), pscale(ppow(T,3),12)), pscale(ppow(T,2),48)), pscale(T,56)), const(20))
W = padd(padd(pmul(U, ppow(T,2)), pscale(T,-28)), const(-20))
lhs = padd(ppow(W,2), pscale(ft,-20))
A = padd(ppow(U,2), const(-20))
B = padd(pscale(U,56), const(240))
C = padd(pscale(U,40), const(176))
quad = padd(padd(pmul(A,ppow(T,2)), pscale(pmul(B,T),-1)), pscale(C,-1))
rhs = pmul(ppow(T,2), quad)
assert lhs == rhs

# Discriminant identity.
disc = padd(ppow(B,2), pscale(pmul(A,C),4))
expected_disc = pscale(pmul(padd(U,const(4)), padd(padd(ppow(U,2),pscale(U,20)),const(68))),160)
assert disc == expected_disc

# Shift U0=u+8: (u+4)(u^2+20u+68)=U0^3-44U0+112.
U0 = padd(U,const(8))
left_shift = pmul(padd(U,const(4)), padd(padd(ppow(U,2),pscale(U,20)),const(68)))
right_shift = padd(padd(ppow(U0,3), pscale(U0,-44)), const(112))
assert left_shift == right_shift

# 2. Freeze/check Magma execution and complete quartic list.
mag = load("magma-execution.json")
ip = load("integral-points-certificate.json")
assert mag["status"] == "SUCCESS_NO_RUNTIME_ERROR"
assert mag["calculator"]["magma_version"] == "2.29-9"
assert mag["calculator"]["runtime_error_seen"] is False
assert mag["workflow"]["artifact_sha256"] == "32c6f9ab32b60faa29b7a8cf7cfc3133115ea19ece422facf51ff255089f8a17"
expected_C = {(-1,-1),(-1,1),(1,-1),(1,1),(11,-37),(11,37)}
cert_C = {tuple(p) for p in ip["complete_C_integral_points"]}
assert cert_C == expected_C
assert ip["status"] == "COMPLETE_DIRECT_QUARTIC_ENUMERATION"
assert ip["heuristic_height_bound_used"] is False
assert ip["database_count_used_as_completeness"] is False

# Verify every certified C and U point by exact integer arithmetic.
def f(Y): return Y**4 + 8*Y**3 + 18*Y**2 - 8*Y + 1
for Y,Z in cert_C:
    assert 20*Z*Z == f(Y)
    UU = 10*Z
    assert UU*UU == 5*f(Y)
for Y,UU in map(tuple, ip["signed_Q_integral_points"]):
    assert UU*UU == 5*f(Y)
assert {tuple(p) for p in mag["quartic"]["signed_integral_points"]} == {tuple(p) for p in ip["signed_Q_integral_points"]}

# 3. Verify explicit C->E formulas on every nonexceptional certified integral point.
def Eeq(x,y): return y*y == x*x*x - 275*x + 1750

def forward(Y,Z):
    assert Y != 1
    x = Fraction(10*(2*Y*Y + 3*Y + 5*Z), (Y-1)**2)
    y = Fraction(25*(3*Y**3 + 15*Y**2 + 14*Y*Z + 3*Y + 6*Z - 1), (Y-1)**3)
    assert Eeq(x,y)
    return x,y

images = {
    (-1,1):(10,0),
    (-1,-1):(-15,-50),
    (11,37):(46,294),
    (11,-37):(9,-2),
}
for cp, ep in images.items():
    assert forward(*cp) == tuple(map(Fraction,ep))
assert Eeq(Fraction(9),Fraction(2))
# Exceptional extension is C(1,1)->O and inverse finite point (9,2)->C(1,-1).

def inverse(x,y):
    x,y = Fraction(x),Fraction(y)
    assert Eeq(x,y)
    u = Fraction(2,5)*x - 8
    v = Fraction(16,5)*y
    assert u*u != 20
    t = (v + 56*u + 240) / (2*(u*u-20))
    Y = 1+t
    W = u*t*t - 20 - 28*t
    Z = W/20
    return Y,Z

finite_inverse = {
    (10,0):(-1,1),
    (-15,-50):(-1,-1),
    (9,2):(1,-1),
    (46,294):(11,37),
    (9,-2):(11,-37),
}
for ep, cp in finite_inverse.items():
    assert inverse(*ep) == tuple(map(Fraction,cp))

# 4. Independent elementary check of the seven E-integral x/y values.
# With X=x-10, y^2=X(X^2+30X+25).  The valuation argument in result.md
# forces X=+/-s^2.  Enumerate the two resulting finite factor problems exactly.
pos_squares = set()
for a in range(1,201):
    if 200 % a: continue
    b = 200 // a
    if a > b or (a+b) % 2: continue
    s2 = (a+b)//2 - 15
    if s2 >= 0 and is_square(s2):
        pos_squares.add(s2)
assert pos_squares == {0,36}
neg_squares = set()
for s in range(0,6):
    val = 200 - (s*s-15)**2
    if is_square(val):
        neg_squares.add(s*s)
assert neg_squares == {1,25}
xvals = {10+s2 for s2 in pos_squares} | {10-s2 for s2 in neg_squares}
assert xvals == {-15,9,10,46}
Epts = set()
for x in xvals:
    rhsE = x**3 - 275*x + 1750
    r = isqrt(rhsE)
    assert r*r == rhsE
    Epts.add((x,r))
    if r: Epts.add((x,-r))
assert Epts == {(-15,-50),(-15,50),(9,-2),(9,2),(10,0),(46,-294),(46,294)}

# 5. Exhaustive prime-family reconstruction from complete C(Z).
rec = load("reconstruction-ledger.json")
# Case I uses Y=-p. Only negative Y is -1, so no prime p.
negative_Y = {-Y for Y,Z in cert_C if Y < 0}
assert negative_Y == {1}
# Case II uses Y=p. Positive possible Y are 1 and 11; only 11 is prime.
positive_Y = {Y for Y,Z in cert_C if Y > 0}
assert positive_Y == {1,11}
p = 11
q = (p*p + 2*p - 1)//2
assert q == 71 and gcd(p,q) == 1 and p < q and p%2 == q%2 == 1
a,b,c = 4*p*q, q*q-4*p*p, 2*(q*q-p*p)
assert (a,b,c) == (3124,4557,9840)
AB = a*a+b*b; AC=a*a+c*c; BC=b*b+c*c; SPACE=a*a+b*b+c*c
assert_square(AB,5525); assert_square(AC,10324); assert_square(SPACE,11285)
r = isqrt(BC)
assert r == 10843 and r*r == 117570649 and (r+1)*(r+1) == 117592336 and BC == 117591849
assert not is_square(BC)
assert rec["perfect_cuboid_survivor_count"] == 0
assert rec["prime_sophie_germain_subfamily_excluded"] is True
assert rec["coverage"] == "THIN_PRIME_SUBFAMILY_ONLY"

print("STAGE31_VERIFY=PASS")
print("C_ANOM_INTEGRAL_POINT_COUNT=6")
print("E_ANOM_INTEGRAL_POINT_COUNT=7")
print("PRIME_SOPHIE_GERMAIN_SUBFAMILY_SURVIVOR_COUNT=0")
print("PERFECT_CUBOID_GLOBAL_CLAIM=false")
