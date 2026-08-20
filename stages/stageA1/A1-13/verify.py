#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256
from math import gcd, lcm


# E: y^2 = x^3 + x^2 + 95x + 703
O = None
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
        lam = (3 * x1 * x1 + 2 * x1 + 95) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - 1 - x1 - x2
    y3 = -(y1 + lam * (x3 - x1))
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
    vn = vp_int(a.numerator, p)
    vd = vp_int(a.denominator, p)
    num = (a.numerator // (p**vn)) % p
    den = (a.denominator // (p**vd)) % p
    return (num * pow(den, -1, p)) % p


def local_t(point):
    x, y = point
    return -x / y


def quartic_z(point):
    if point is None:
        return None
    x, y = point
    if x == 3 and y == 32:
        return None
    if x == 3 and y == -32:
        return Fraction(2)
    return -(y + 32) / (x - 3)


# Exact line identity controlling the divisor of z-2.
# (-2x-26)^2 - (x^3+x^2+95x+703) = -(x-3)^2(x+3).
def lhs_line(x):
    return (-2 * x - 26) ** 2 - (x**3 + x**2 + 95 * x + 703)


def rhs_line(x):
    return -((x - 3) ** 2) * (x + 3)


# Degree <=3 identity: four exact evaluations suffice.
for xx in [-7, -3, 0, 5]:
    assert lhs_line(xx) == rhs_line(xx)

# Known special points.
assert mul_q(-1) == (Fraction(3), Fraction(-32))
assert mul_q(2) == (Fraction(-3), Fraction(-20))
assert quartic_z(mul_q(-1)) == 2
assert quartic_z(mul_q(2)) == 2

# Formal-group depth at p=7.
p9 = mul_q(9)
t9 = local_t(p9)
assert p9 == (
    Fraction(244695292924563763, 53070230469113361),
    Fraction(-434024672226074853059906272, 12225776733946406608383609),
)
assert vp_frac(t9, 7) == 1
assert unit_mod_p(t9 / 7, 7) == 2

# Every nonzero k mod 7 remains in E_1 \ E_2; 7*(9P)=63P enters E_2.
for k in range(1, 7):
    assert vp_frac(local_t(mul_q(9 * k)), 7) == 1
assert vp_frac(local_t(mul_q(63)), 7) == 2

# Exact representative valuation table for the four A1-12 residue centers.
# For r=0,1 the exact center is a pole; all other first-order lifts have
# both square functions of valuation -1. For r=2,-1, z-2 has a simple zero
# at the exact center and valuation 1 on every other first-order lift.
for r in [0, 1]:
    for k in range(1, 7):
        n = r + 9 * k
        z = quartic_z(mul_q(n))
        assert z is not None
        assert vp_frac(z + 2, 7) == -1
        assert vp_frac(z - 2, 7) == -1

for r in [2, -1]:
    assert quartic_z(mul_q(r)) == 2
    for k in range(1, 7):
        n = r + 9 * k
        z = quartic_z(mul_q(n))
        assert z is not None
        assert vp_frac(z + 2, 7) == 0
        assert vp_frac(z - 2, 7) == 1

# Therefore the necessary prime-power condition is n mod 63 in {0,1,2,-1}.
ALLOWED63 = {0, 1, 2, 62}

# Recompute the exact A1-12 CRT residue set from its audited local data.
A1_12 = [
    (9, {0, 1, 2, 8}),
    (29, {0, 1, 2, 28}),
    (10, {0, 1, 2, 9}),
    (22, {0, 1, 2, 21}),
    (34, {0, 1, 2, 33}),
    (21, {0, 1, 2, 20}),
]


def combine(m1, r1, m2, r2):
    g = gcd(m1, m2)
    modulus = lcm(m1, m2)
    out = set()
    for a in r1:
        for b in r2:
            if (b - a) % g:
                continue
            mm = m2 // g
            if mm == 1:
                k = 0
            else:
                k = (((b - a) // g) * pow(m1 // g, -1, mm)) % mm
            out.add((a + m1 * k) % modulus)
    return modulus, out


modulus = 1
residues = {0}
for order, allowed in A1_12:
    modulus, residues = combine(modulus, residues, order, allowed)

assert modulus == 3416490
assert len(residues) == 384
assert modulus % 63 == 0

refined = {r for r in residues if r % 63 in ALLOWED63}
assert len(refined) == 256
assert refined < residues
assert all(((1 - r) % modulus) in refined for r in refined)

digest = sha256(",".join(str(x) for x in sorted(refined)).encode()).hexdigest()
assert digest == "f08de28f142bf79dd88bbee5725e87c4dd0692091d0e85a645275dc1bfca6fc0"

print("A1-13 line/divisor identity: PASS")
print("v7(t(9P))=1 and v7(t(63P))=2: PASS")
print("first-order lift valuation table: PASS")
print("allowed_mod_63=[0,1,2,62]")
print(f"combined_modulus={modulus}")
print(f"A1_12_surviving_classes={len(residues)}")
print(f"A1_13_surviving_classes={len(refined)}")
print(f"A1_13_surviving_class_sha256={digest}")
print("A1-13 7-adic prime-power refinement: PASS")
