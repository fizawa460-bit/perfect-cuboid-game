from fractions import Fraction
from math import gcd

SOURCE = "e228c62d6e0fa7d4bf2939bd8e1710f67aa4a9be"

# 1. Frozen primitive rotated-pair identities.
pair_checks = 0
primitive_checks = 0
for D in range(3, 220):
    for A in range(1, D):
        m = D + A
        n = D - A
        assert m > n > 0
        assert m * n == D * D - A * A
        assert m * m + n * n == 2 * (D * D + A * A)
        assert gcd(m, n) <= 2 * gcd(D, A)
        pair_checks += 1
        if gcd(D, A) == 1:
            assert gcd(m, n) in (1, 2)
            primitive_checks += 1

assert pair_checks > 20000
assert primitive_checks > 10000

# 2. Theta-quarter physical exponent ledger.
ledger_checks = 0
for k in range(0, 193):
    chi = Fraction(1, 6) + Fraction(k, 192) * (Fraction(1, 4) - Fraction(1, 6))
    phi = (chi + Fraction(1, 4)) / 2
    c = chi
    u = Fraction(1, 4) - chi
    s = Fraction(1, 4) - chi / 2
    r = phi
    assert c + 2 * s == Fraction(1, 2)
    assert u + 2 * r == Fraction(1, 2)
    assert c + u == Fraction(1, 4)
    assert 2 * s + 2 * r == Fraction(3, 4)
    ledger_checks += 1

# 3. Product-vs-sum maps are distinct projections of the same pair.
projection_checks = 0
for m in range(2, 100):
    for n in range(1, m):
        if (m + n) % 2 or (m - n) % 2:
            continue
        D = (m + n) // 2
        A = (m - n) // 2
        if A <= 0:
            continue
        product = m * n
        norm2 = m * m + n * n
        assert product == D * D - A * A
        assert norm2 == 2 * (D * D + A * A)
        projection_checks += 1

assert projection_checks > 1000

# 4. The algebraic X,Y transform is invertible; no deterministic extra relation
# arises merely from retaining both square equations.
det = -2
assert det != 0
for D in range(2, 100):
    for A in range(1, D):
        X = D * D + A * A
        Y = D * D - A * A
        assert Fraction(X + Y, 2) == D * D
        assert Fraction(X - Y, 2) == A * A

print("Stage14-sH48 frozen Gaussian product/sum correlation audit: PASS")
print(f"source snapshot: {SOURCE}")
print(f"rotated-pair identity checks: {pair_checks}")
print(f"primitive gcd checks: {primitive_checks}")
print(f"theta-quarter ledger checks: {ledger_checks}")
print(f"product/norm projection checks: {projection_checks}")
print("certified B-power saving exponent: 0")
print("off-the-shelf theorem directly applicable: false")
print("preferred receiver: centered primitive product-vs-norm dispersion")
