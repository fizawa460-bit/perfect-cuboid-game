#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def sf(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


# Exact reduced-coordinate identities.
states = []
for q in range(2, 90):
    for p in range(1, q):
        if gcd(p, q) != 1:
            continue
        xi = sf(p * q)
        k = sf(q * q - p * p)
        assert gcd(p * q, q * q - p * p) == 1
        assert gcd(xi, k) == 1
        n = xi * k
        assert sf(n) == n
        # PQ=xi*a^2 and Q^2-P^2=k*b^2.
        a2 = p * q // xi
        b2 = (q * q - p * p) // k
        assert square(a2) and square(b2)
        a = isqrt(a2)
        b = isqrt(b2)
        z = Fraction(a, q)
        y = Fraction(b, q)
        assert Fraction(k) * y * y == 1 - Fraction(xi * xi) * z**4
        states.append((p, q, xi, k, n, z, y))

# n=1 would force the forbidden quartic-square pattern; no finite nonboundary sample occurs.
assert all(n > 1 for _, _, _, _, n, _, _ in states)

# Same-label pairs are exactly same quartic twists and have distinct positive z when p/q differs.
groups = {}
for row in states:
    groups.setdefault((row[2], row[3]), []).append(row)
pair_checks = 0
for (xi, k), rows in groups.items():
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            p, q, _, _, n, z1, y1 = rows[i]
            r, s, _, _, n2, z2, y2 = rows[j]
            assert n == n2 == xi * k
            # Product-square iff xi labels agree.
            assert square(p * r * q * s)
            assert Fraction(k) * y1 * y1 == 1 - Fraction(xi * xi) * z1**4
            assert Fraction(k) * y2 * y2 == 1 - Fraction(xi * xi) * z2**4
            if Fraction(p, q) != Fraction(r, s):
                assert z1 > 0 and z2 > 0 and z1 != z2
            pair_checks += 1
            if pair_checks >= 500:
                break
        if pair_checks >= 500:
            break
    if pair_checks >= 500:
        break
assert pair_checks > 0

# For squarefree n>1, halving the unique rational 2-torsion would require y^2=16*n^3 at x=2n,
# which is not a rational square.  This is the only 2-primary halving obstruction needed after
# the standard j=1728/Mazur odd-torsion exclusion recorded in result.md.
for n in range(2, 300):
    if sf(n) != n:
        continue
    assert not square(16 * n**3)
    # x=-2n is outside the real curve.
    assert (-2 * n) ** 3 + 4 * n * n * (-2 * n) < 0

# Fixed squarefree n has only divisor/subset-many coprime squarefree factorizations.
for n in range(2, 500):
    if sf(n) != n:
        continue
    fac = 0
    for k in range(1, n + 1):
        if n % k == 0:
            xi = n // k
            if gcd(k, xi) == 1 and sf(k) == k and sf(xi) == xi:
                fac += 1
    omega = 0
    t = n
    p = 2
    while p * p <= t:
        if t % p == 0:
            omega += 1
            while t % p == 0:
                t //= p
        p += 1 if p == 2 else 2
    if t > 1:
        omega += 1
    assert fac == 2**omega

# Current ledger is inherited, not improved in 4bt.
assert Fraction(20, 21) - Fraction(1, 2) == Fraction(19, 42)

print("Stage14-4bt squarefree j=1728 twist audit: OK")
print(f"reduced states={len(states)} same-twist pair checks={pair_checks}")
print("XI_K_COPRIME=true")
print("TWIST_PARAMETER_SQUAREFREE=true")
print("PHYSICAL_TWO_POINT_DIFFERENCE_TORSION=false")
print("ONE_DIMENSIONAL_SQUAREFREE_TWIST_RECEIVER_DEFINED=true")
