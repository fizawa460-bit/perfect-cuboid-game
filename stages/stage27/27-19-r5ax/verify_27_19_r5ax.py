#!/usr/bin/env python3
from math import gcd


def gmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]


# Audited nondegenerate Stage19 witness.
m, n, r, s = 21, 16, 27, 14
delta, c0, cs, cn = 2, 3, 7, 1
C = c0 * cs * cn
mu, nu, rho, sigma = 1, 8, 9, 1
kappa = 185

assert m == c0 * cs * mu
assert n == delta * cn * nu
assert r == c0 * cn * rho
assert s == delta * cs * sigma
assert gcd(m, n) == 1
assert gcd(r, s) == 1
assert (m * m - n * n) % kappa == 0
assert (r * r + s * s) % kappa == 0
assert gcd(kappa, m * n * r * s) == 1

# Difference packet: exact boundary identity.
kappa_minus = gcd(kappa, abs(m - n))
kappa_plus = kappa // kappa_minus
A = (m - n) // kappa_minus
B = (m + n) // kappa_plus
assert (kappa_minus, kappa_plus, A, B) == (5, 37, 1, 1)
assert gcd(kappa_minus, kappa_plus) == 1
assert m == (kappa_minus * A + kappa_plus * B) // 2
assert n == (kappa_plus * B - kappa_minus * A) // 2
D_value = kappa_plus * kappa_plus * B * B - kappa_minus * kappa_minus * A * A
assert D_value == 4 * m * n
assert D_value == 4 * delta * C * mu * nu
assert D_value == 1344

# Gaussian packet: exact boundary identity and determinant.
lambda_gauss = (11, -8)
eta_gauss = (1, 2)
assert gnorm(lambda_gauss) == kappa
assert gmul(lambda_gauss, eta_gauss) == (r, s)
a, b = lambda_gauss
u_g, v_g = eta_gauss
r2 = a * u_g - b * v_g
s2 = a * v_g + b * u_g
assert (r2, s2) == (r, s)
assert a * a + b * b == kappa
assert r2 * s2 == delta * C * rho * sigma
assert r2 * s2 == 378
assert a * a + b * b == abs(a * a - (-b) * b)  # determinant [[a,-b],[b,a]]

# Difference allocation is unique prime-by-prime for odd squarefree kappa
# whenever gcd(kappa,m*n)=1. Verify this exact property on the witness.
for p in (5, 37):
    assert kappa % p == 0
    assert gcd(p, m * n) == 1
    hits = int((m - n) % p == 0) + int((m + n) % p == 0)
    assert hits == 1

# The fixed-R theorem from r5aw converts global polynomial exponent questions
# into occupied-R support questions.  The inequality is purely combinatorial:
# support <= total <= max_fiber * support.
fibers = [0, 1, 3, 0, 2, 0, 4]
support = sum(v > 0 for v in fibers)
total = sum(fibers)
max_fiber = max(fibers)
assert support <= total <= max_fiber * support

# A change of variables alone does not create a quantitative saving: the
# witness pair products are exactly preserved by both packet maps.
assert m * n == delta * C * mu * nu
assert r * s == delta * C * rho * sigma

print("Stage27-19-r5ax difference boundary identity: PASS")
print("Stage27-19-r5ax Gaussian boundary identity/determinant: PASS")
print("Stage27-19-r5ax witness pair-product preservation: PASS")
print("Stage27-19-r5ax occupied-R support inequality sanity: PASS")
print("Stage27-19-r5ax factor packet is reparametrization; no K-power asserted: PASS")
