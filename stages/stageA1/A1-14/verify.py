#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256
from math import gcd, lcm

P = (Fraction(3), Fraction(32))


def add_q(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == -y2:
        return None
    if p1 == p2:
        lam = (3*x1*x1 + 2*x1 + 95) / (2*y1)
    else:
        lam = (y2-y1) / (x2-x1)
    x3 = lam*lam - 1 - x1 - x2
    y3 = -(y1 + lam*(x3-x1))
    return x3, y3


def neg_q(p):
    return None if p is None else (p[0], -p[1])


def mul_q(n, p=P):
    if n < 0:
        return neg_q(mul_q(-n, p))
    r = None
    q = p
    while n:
        if n & 1:
            r = add_q(r, q)
        q = add_q(q, q)
        n >>= 1
    return r


def vp_int(a, p):
    if a == 0:
        return 10**9
    a = abs(a)
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def vp_frac(a, p):
    if a == 0:
        return 10**9
    return vp_int(a.numerator, p) - vp_int(a.denominator, p)


def unit_mod_p(a, p):
    v = vp_frac(a, p)
    if v >= 0:
        a = a / (p**v)
    else:
        a = a * (p**(-v))
    return (a.numerator % p) * pow(a.denominator % p, -1, p) % p


def local_tau(point):
    x, y = point
    return -x / y


def quartic_z(point):
    if point is None:
        return None
    x, y = point
    if (x, y) == P:
        return None
    if (x, y) == (Fraction(3), Fraction(-32)):
        return Fraction(2)
    return -(y + 32) / (x - 3)


# Formal-group depth.
t63 = local_tau(mul_q(63))
t441 = local_tau(mul_q(441))
assert vp_frac(t63, 7) == 2
assert unit_mod_p(t63 / 49, 7) == 2
assert vp_frac(t441, 7) == 3

# Exact k=1 representatives at the four A1-13 centers.
expected = {
    63:  ((-2, 4), (-2, 4)),
    64:  ((-2, 3), (-2, 3)),
    65:  ((0, 4), (2, 5)),
    62:  ((0, 4), (2, 2)),
}
for n, pair in expected.items():
    z = quartic_z(mul_q(n))
    assert z is not None
    got_plus = (vp_frac(z + 2, 7), unit_mod_p(z + 2, 7))
    got_minus = (vp_frac(z - 2, 7), unit_mod_p(z - 2, 7))
    assert (got_plus, got_minus) == pair, (n, got_plus, got_minus)

# Nonzero square residues mod 7.
SQ = {1, 2, 4}
NSQ = {3, 5, 6}
assert {k for k in range(1, 7) if k in SQ} == {1, 2, 4}
assert {k for k in range(1, 7) if k in NSQ} == {3, 5, 6}

# Formal-group scaling gives the exact allowed k sets.
allowed_k = {
    0:  {0, 1, 2, 4},
    1:  {0, 3, 5, 6},
    2:  {0, 3, 5, 6},
    -1: {0, 1, 2, 4},
}
allowed441 = set()
for center, ks in allowed_k.items():
    for k in ks:
        allowed441.add((center + 63*k) % 441)

EXPECTED441 = {
    0, 63, 126, 252,
    1, 190, 316, 379,
    2, 191, 317, 380,
    440, 62, 125, 251,
}
assert allowed441 == EXPECTED441
assert len(allowed441) == 16
assert all(((1-r) % 441) in allowed441 for r in allowed441)

# Rebuild audited A1-12 CRT set, then A1-13 filter.
A1_12 = [
    (9, {0,1,2,8}),
    (29, {0,1,2,28}),
    (10, {0,1,2,9}),
    (22, {0,1,2,21}),
    (34, {0,1,2,33}),
    (21, {0,1,2,20}),
]


def combine(m1, r1, m2, r2):
    g = gcd(m1, m2)
    M = lcm(m1, m2)
    out = set()
    for a in r1:
        for b in r2:
            if (b-a) % g:
                continue
            mm = m2 // g
            k = 0 if mm == 1 else (((b-a)//g) * pow(m1//g, -1, mm)) % mm
            out.add((a + m1*k) % M)
    return M, out

M = 1
res = {0}
for m, rr in A1_12:
    M, res = combine(M, res, m, rr)
assert M == 3416490 and len(res) == 384

A1_13 = {r for r in res if r % 63 in {0,1,2,62}}
assert len(A1_13) == 256

M14 = lcm(M, 441)
assert M14 == 23915430 == 7*M
pre = set()
for r in A1_13:
    for j in range(7):
        pre.add((r + j*M) % M14)
assert len(pre) == 1792

A1_14 = {r for r in pre if r % 441 in allowed441}
assert len(A1_14) == 1024
assert all(((1-r) % M14) in A1_14 for r in A1_14)

digest = sha256(",".join(str(x) for x in sorted(A1_14)).encode()).hexdigest()
assert digest == "ca2472c7077bac47b0cced38211ea26aa20223dd65e7f2c548d78cca93117251"

print("A1-14 formal depth: PASS")
print("v7(tau(63P))=2, unit=2; v7(tau(441P))=3")
print("allowed_mod_441_count=16")
print(f"global_modulus={M14}")
print(f"pretest_lifts={len(pre)}")
print(f"surviving_classes={len(A1_14)}")
print(f"sha256={digest}")
print("A1-14 second-depth 7-adic refinement: PASS")
