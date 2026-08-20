#!/usr/bin/env python3
from fractions import Fraction
from hashlib import sha256
from math import gcd, isqrt, lcm


# ---------- tiny exact polynomial engine in x,z ----------

def padd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + c
        if out[m] == 0:
            del out[m]
    return out


def pscale(a, c):
    return {m: c * v for m, v in a.items() if c * v}


def pmul(a, b):
    out = {}
    for (i, j), ca in a.items():
        for (k, l), cb in b.items():
            m = (i + k, j + l)
            out[m] = out.get(m, 0) + ca * cb
    return {m: c for m, c in out.items() if c}


def ppow(a, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = pmul(out, a)
    return out


ONE = {(0, 0): 1}
X = {(1, 0): 1}
Z = {(0, 1): 1}


def const(c):
    return {(0, 0): c} if c else {}


# Verify
# [-z(x-3)-32]^2 - (x^3+x^2+95x+703)
# = -(x-3)[x^2+(4-z^2)x+3z^2-64z+107].
xm3 = padd(X, const(-3))
yexpr = padd(pscale(pmul(Z, xm3), -1), const(-32))
weier_rhs = padd(
    padd(ppow(X, 3), ppow(X, 2)),
    padd(pscale(X, 95), const(703)),
)
lhs = padd(ppow(yexpr, 2), pscale(weier_rhs, -1))
inner = padd(
    ppow(X, 2),
    padd(
        pmul(padd(const(4), pscale(ppow(Z, 2), -1)), X),
        padd(pscale(ppow(Z, 2), 3), padd(pscale(Z, -64), const(107))),
    ),
)
rhs = pscale(pmul(xm3, inner), -1)
assert lhs == rhs

# Discriminant identity.
disc = padd(
    ppow(padd(const(4), pscale(ppow(Z, 2), -1)), 2),
    pscale(padd(pscale(ppow(Z, 2), 3), padd(pscale(Z, -64), const(107))), -4),
)
Qpoly = padd(
    ppow(Z, 4),
    padd(pscale(ppow(Z, 2), -20), padd(pscale(Z, 256), const(-412))),
)
assert disc == Qpoly


# ---------- exact rational group law on 6080.r1 ----------
# y^2 = x^3 + x^2 + 95x + 703
A2 = Fraction(1)
A4 = Fraction(95)
A6 = Fraction(703)
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
        lam = (3 * x1 * x1 + 2 * A2 * x1 + A4) / (2 * y1)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam - A2 - x1 - x2
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


def q_quartic(z):
    return z**4 - 20 * z**2 + 256 * z - 412


def quartic_from_e(p):
    if p is None:
        return ("inf", None)
    x, y = p
    if x == 3 and y == 32:
        return ("inf", None)
    if x == 3 and y == -32:
        return (Fraction(2), Fraction(6))
    z = -(y + 32) / (x - 3)
    v = 2 * x + 4 - z * z
    assert v * v == q_quartic(z)
    return z, v


expected = {
    -1: (Fraction(2), Fraction(6)),
    2: (Fraction(2), Fraction(-6)),
    3: (Fraction(26, 3), Fraction(694, 9)),
    -2: (Fraction(26, 3), Fraction(-694, 9)),
    4: (Fraction(-287, 30), Fraction(-54631, 900)),
    -3: (Fraction(-287, 30), Fraction(54631, 900)),
}
for n, target in expected.items():
    assert quartic_from_e(mul_q(n)) == target

# Hyperelliptic involution on the quartic is n -> 1-n.
for n in range(-8, 10):
    a = quartic_from_e(mul_q(n))
    b = quartic_from_e(mul_q(1 - n))
    if a[0] == "inf" or b[0] == "inf":
        continue
    assert a[0] == b[0]
    assert a[1] == -b[1]


# Minimal-model discriminant: bad primes are exactly 2,5,19.
b2 = 4
b4 = 190
b6 = 2812
b8 = 4 * 703 - 95 * 95
DELTA = -(b2 * b2 * b8 + 8 * b4**3 + 27 * b6**2 - 9 * b2 * b4 * b6)
assert DELTA == -249036800


# ---------- finite-field group law and multiplier sieve ----------

def invmod(a, p):
    return pow(a % p, p - 2, p)


def add_fp(p1, p2, p):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if p1 == p2:
        if y1 % p == 0:
            return None
        lam = ((3 * x1 * x1 + 2 * x1 + 95) * invmod(2 * y1, p)) % p
    else:
        lam = ((y2 - y1) * invmod(x2 - x1, p)) % p
    x3 = (lam * lam - 1 - x1 - x2) % p
    y3 = (-y1 - lam * (x3 - x1)) % p
    return x3, y3


def mul_fp(n, point, p):
    r = None
    q = point
    while n:
        if n & 1:
            r = add_fp(r, q, p)
        q = add_fp(q, q, p)
        n >>= 1
    return r


def point_order(point, p):
    r = None
    upper = p + 1 + 2 * isqrt(p) + 4
    for n in range(1, upper + 1):
        r = add_fp(r, point, p)
        if r is None:
            return n
    raise AssertionError("order not found within Hasse bound")


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def z_mod(point, p):
    # Conservative treatment of poles: O and +P are retained by caller.
    if point is None:
        return "pole"
    x, y = point
    if x == 3 % p:
        if y == 32 % p:
            return "pole"
        if y == (-32) % p:
            # tangent at -P has slope -2, hence z=2
            return 2 % p
    return (-(y + 32) * invmod(x - 3, p)) % p


def admissible_classes(p):
    assert DELTA % p != 0
    pbar = (3 % p, 32 % p)
    order = point_order(pbar, p)
    allowed = []
    for n in range(order):
        point = mul_fp(n, pbar, p)
        z = z_mod(point, p)
        if z == "pole":
            allowed.append(n)
            continue
        if legendre(z + 2, p) >= 0 and legendre(z - 2, p) >= 0:
            allowed.append(n)
    return order, allowed


EXPECTED = {
    7: (9, [0, 1, 2, 8]),
    23: (29, [0, 1, 2, 28]),
    37: (10, [0, 1, 2, 9]),
    257: (22, [0, 1, 2, 21]),
    263: (34, [0, 1, 2, 33]),
    863: (21, [0, 1, 2, 20]),
}
for p, expected_pair in EXPECTED.items():
    got = admissible_classes(p)
    assert got == expected_pair, (p, got, expected_pair)


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
for p in [7, 23, 37, 257, 263, 863]:
    order, allowed = EXPECTED[p]
    modulus, residues = combine(modulus, residues, order, set(allowed))

assert modulus == 3416490
assert len(residues) == 384
assert all(((1 - r) % modulus) in residues for r in residues)
encoded = ",".join(str(x) for x in sorted(residues)).encode()
digest = sha256(encoded).hexdigest()
assert digest == "63652cb8e25860ba40dba7ba5f99023a9a611525f7b2bd2465a79b95c268e874"

print("A1-12 exact birational identity: PASS")
print("delta1_generator_map: PASS")
for p in [7, 23, 37, 257, 263, 863]:
    order, allowed = EXPECTED[p]
    print(f"p={p} order={order} allowed={allowed}")
print(f"combined_modulus={modulus}")
print(f"surviving_classes={len(residues)}")
print(f"surviving_class_sha256={digest}")
print("A1-12 elementary MW residue sieve: PASS")
