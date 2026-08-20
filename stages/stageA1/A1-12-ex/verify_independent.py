#!/usr/bin/env python3
"""Independent A1-12-ex verifier.

Deliberately does not import A1-12/verify.py.  It uses SymPy for the
birational identities, a separately written elliptic-curve group law for
finite fields, and a direct 0..M-1 scan instead of the A1-12 CRT combiner.
"""
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, lcm

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Direct family-to-square identities and birational algebra
# ---------------------------------------------------------------------------
X = sp.symbols("X", nonzero=True)
k = X**2
z_from_family = k + 1/k
assert sp.factor(z_from_family + 2 - (X + 1/X)**2) == 0
assert sp.factor(z_from_family - 2 - (X - 1/X)**2) == 0

x, y, z, v = sp.symbols("x y z v")
E_rhs = x**3 + x**2 + 95*x + 703
y_line = -z*(x - 3) - 32
factorization = sp.factor(y_line**2 - E_rhs)
expected_factorization = -(x - 3) * (x**2 + (4-z**2)*x + 3*z**2 - 64*z + 107)
assert sp.expand(factorization - expected_factorization) == 0
Q = z**4 - 20*z**2 + 256*z - 412
disc = sp.expand((4-z**2)**2 - 4*(3*z**2 - 64*z + 107))
assert sp.expand(disc - Q) == 0

x_inv = (v + z**2 - 4) / 2
y_inv = -z*(x_inv - 3) - 32
# On the quartic v^2=Q(z), the Weierstrass residual must be divisible by v^2-Q.
residual = sp.factor(y_inv**2 - (x_inv**3 + x_inv**2 + 95*x_inv + 703))
quotient, remainder = sp.div(sp.together(residual).as_numer_denom()[0], v**2-Q, domain=sp.QQ[z,v])
assert remainder == 0

# ---------------------------------------------------------------------------
# 2. Independent rational group-law spot checks / involution checks
# ---------------------------------------------------------------------------
A2 = Fraction(1)
A4 = Fraction(95)
P_Q = (Fraction(3), Fraction(32))


def qadd(P, R):
    if P is None:
        return R
    if R is None:
        return P
    x1, y1 = P
    x2, y2 = R
    if x1 == x2 and y1 == -y2:
        return None
    if P == R:
        if y1 == 0:
            return None
        m = (3*x1*x1 + 2*A2*x1 + A4) / (2*y1)
    else:
        m = (y2-y1)/(x2-x1)
    x3 = m*m - A2 - x1 - x2
    y3 = -y1 - m*(x3-x1)
    return (x3, y3)


def qmul(n):
    if n < 0:
        R = qmul(-n)
        return None if R is None else (R[0], -R[1])
    R = None
    B = P_Q
    while n:
        if n & 1:
            R = qadd(R, B)
        B = qadd(B, B)
        n >>= 1
    return R


def quartic_map(R):
    if R is None:
        return ("inf", None)
    xx, yy = R
    if xx == 3 and yy == 32:
        return ("inf", None)
    if xx == 3 and yy == -32:
        return (Fraction(2), Fraction(6))
    zz = -(yy + 32)/(xx - 3)
    vv = 2*xx + 4 - zz*zz
    qv = zz**4 - 20*zz**2 + 256*zz - 412
    assert vv*vv == qv
    return zz, vv

assert quartic_map(qmul(-1)) == (Fraction(2), Fraction(6))
assert quartic_map(qmul(2)) == (Fraction(2), Fraction(-6))
assert quartic_map(qmul(3)) == (Fraction(26,3), Fraction(694,9))
assert quartic_map(qmul(-2)) == (Fraction(26,3), Fraction(-694,9))
for n in range(-12, 14):
    a = quartic_map(qmul(n))
    b = quartic_map(qmul(1-n))
    if a[0] == "inf" or b[0] == "inf":
        continue
    assert a[0] == b[0]
    assert a[1] == -b[1]

# ---------------------------------------------------------------------------
# 3. Independent finite-field group law and residue sieve
# ---------------------------------------------------------------------------
DELTA = -249036800
assert DELTA == -(2**19)*(5**2)*19


def invmod(a, p):
    return pow(a % p, -1, p)


def fp_add(P, R, p):
    if P is None:
        return R
    if R is None:
        return P
    x1, y1 = P
    x2, y2 = R
    if x1 == x2 and (y1+y2) % p == 0:
        return None
    if P == R:
        if y1 % p == 0:
            return None
        m = ((3*x1*x1 + 2*x1 + 95) * invmod(2*y1, p)) % p
    else:
        m = ((y2-y1) * invmod(x2-x1, p)) % p
    x3 = (m*m - 1 - x1 - x2) % p
    y3 = (-y1 - m*(x3-x1)) % p
    return (x3, y3)


def subgroup_cycle(p):
    P = (3 % p, 32 % p)
    out = [None]
    R = None
    # Point order is <= #E(F_p) <= p+1+2sqrt(p).
    bound = p + 1 + 2*isqrt(p) + 3
    for _ in range(1, bound+1):
        R = fp_add(R, P, p)
        out.append(R)
        if R is None:
            return out
    raise AssertionError("point order not found")


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    t = pow(a, (p-1)//2, p)
    return 1 if t == 1 else -1


def z_reduction(R, p):
    if R is None:
        return None  # O: pole retained
    xx, yy = R
    if xx == 3 % p:
        if yy == 32 % p:
            return None  # P: pole retained
        assert yy == (-32) % p
        return 2 % p     # -P: removable value
    return (-(yy+32) * invmod(xx-3, p)) % p


def sieve_at_prime(p):
    assert DELTA % p != 0
    cyc = subgroup_cycle(p)
    order = len(cyc)-1
    allowed = set()
    for n in range(order):
        zz = z_reduction(cyc[n], p)
        if zz is None:
            allowed.add(n)
        elif legendre(zz+2, p) >= 0 and legendre(zz-2, p) >= 0:
            allowed.add(n)
    return order, allowed

EXPECTED = {
    7:   (9,  {0,1,2,8}),
    23:  (29, {0,1,2,28}),
    37:  (10, {0,1,2,9}),
    257: (22, {0,1,2,21}),
    263: (34, {0,1,2,33}),
    863: (21, {0,1,2,20}),
}
for p, expected in EXPECTED.items():
    got = sieve_at_prime(p)
    assert got == expected, (p, got, expected)

# ---------------------------------------------------------------------------
# 4. Direct full scan of all M residues -- no CRT merge routine
# ---------------------------------------------------------------------------
orders = [9,29,10,22,34,21]
M = 1
for m in orders:
    M = lcm(M, m)
assert M == 3416490

survivors = []
for n in range(M):
    ok = True
    for m in orders:
        if n % m not in (0,1,2,m-1):
            ok = False
            break
    if ok:
        survivors.append(n)

assert len(survivors) == 384
assert all(((1-r) % M) in set(survivors) for r in survivors)
digest = sha256(",".join(str(r) for r in survivors).encode()).hexdigest()
assert digest == "63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874"

print("family z+2/z-2 direct square identities: PASS")
print("birational identities: PASS")
print("rational multiplier involution spot checks: PASS")
for p in EXPECTED:
    order, allowed = sieve_at_prime(p)
    print(f"p={p} ordP={order} allowed={sorted(allowed)}")
print(f"full_residue_scan={M}")
print(f"surviving_classes={len(survivors)}")
print(f"sha256={digest}")
print("A1-12-ex independent elementary certification: PASS")
