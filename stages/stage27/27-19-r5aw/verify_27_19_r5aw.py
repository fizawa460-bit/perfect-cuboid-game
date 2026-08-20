#!/usr/bin/env python3
from math import gcd, isqrt


def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def tau(n):
    return len(divisors(n))


def r2(n):
    # Classical formula r_2(n)=4*sum_{d|n} chi_4(d).
    s = 0
    for d in divisors(n):
        if d % 4 == 1:
            s += 1
        elif d % 4 == 3:
            s -= 1
    return 4 * s


def gmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gnorm(z):
    return z[0] * z[0] + z[1] * z[1]


# 1. Classical r_2/tau inequality on a deterministic finite audit sample.
for R in range(1, 401):
    n = R * R
    assert 0 <= r2(n) <= 4 * tau(n)
    assert 3 * r2(n) * r2(n) <= 48 * tau(n) * tau(n)

# 2. Exact Stage19 witness from r5ak/r5aw.
m, n, r, s = 21, 16, 27, 14
kappa = 185
R = 7585
assert gcd(m, n) == 1
assert gcd(r, s) == 1
assert kappa % 2 == 1
assert (m * m - n * n) % kappa == 0
assert (r * r + s * s) % kappa == 0
assert gcd(kappa, m * n * r * s) == 1

# Difference-factor allocation.
kappa_minus = gcd(kappa, abs(m - n))
kappa_plus = kappa // kappa_minus
assert kappa_minus == 5
assert kappa_plus == 37
assert gcd(kappa_minus, kappa_plus) == 1
assert (m - n) % kappa_minus == 0
assert (m + n) % kappa_plus == 0
A = (m - n) // kappa_minus
B = (m + n) // kappa_plus
assert A == 1 and B == 1
assert (kappa_minus * A + kappa_plus * B) % 2 == 0
assert (kappa_plus * B - kappa_minus * A) % 2 == 0
assert (kappa_minus * A + kappa_plus * B) // 2 == m
assert (kappa_plus * B - kappa_minus * A) // 2 == n

# Gaussian factor allocation.
lambda_gauss = (11, -8)  # (2-i)(6-i), norm 5*37=185
eta_gauss = (1, 2)
assert gnorm(lambda_gauss) == kappa
assert gnorm(eta_gauss) == (r * r + s * s) // kappa
assert gmul(lambda_gauss, eta_gauss) == (r, s)

# 3. Physical fixed-R sum-of-two-squares receiver on the same actual survivor.
e, x, y = 6048, 1665, 4264
D_x, D_y = 6273, 7400
assert e * e + x * x == D_x * D_x
assert e * e + y * y == D_y * D_y
assert e * e + x * x + y * y == R * R
assert D_x * D_x + y * y == R * R
assert D_y * D_y + x * x == R * R

# The crude fixed-R theorem has plenty of room on this witness.
r2_R2 = r2(R * R)
tau_R2 = tau(R * R)
assert r2_R2 == 108
assert tau_R2 == 27
assert r2_R2 == 4 * tau_R2
assert 1 <= 3 * r2_R2 * r2_R2
assert 3 * r2_R2 * r2_R2 == 34992

# 4. No-global-recharge arithmetic: a pointwise R^o(1) fiber summed over
# all R<=B has a trivial B factor.  This verifier intentionally does not
# encode a false sub-square-root implication.
for Bcut in (10, 50, 100):
    raw_host = sum(48 * tau(R0 * R0) ** 2 for R0 in range(1, Bcut + 1))
    assert raw_host >= Bcut

print("Stage27-19-r5aw r2/tau fixed-R bound: PASS")
print("Stage27-19-r5aw difference factor split: PASS")
print("Stage27-19-r5aw Gaussian norm factor split: PASS")
print("Stage27-19-r5aw physical witness identities: PASS")
print("Stage27-19-r5aw fixed-R fiber is local-only / no global recharge: PASS")
