#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

# 1. The s7-50 conductor ledger is exact: plus-side complete mass 1/2,
# and any fixed-power d=B^lambda loses lambda.
ledger_checks = 0
for chi_i in range(16, 25):
    chi = Fraction(chi_i, 96)
    if not (Fraction(1, 6) <= chi <= Fraction(1, 4)):
        continue
    plus = chi + 2 * (Fraction(1, 4) - chi / 2)
    assert plus == Fraction(1, 2)
    for k in range(13):
        lam = chi * Fraction(k, 12)
        assert plus - lam == Fraction(1, 2) - lam
        ledger_checks += 1
assert ledger_checks > 50

# 2. Full-conductor endpoint means removing only a B^o factor from C;
# small integer models verify q=C/d and primitive h0.
endpoint_checks = 0
for C in range(3, 150, 2):
    for h in range(1, C):
        d = gcd(h, C)
        q = C // d
        h0 = h // d
        assert gcd(h0, q) == 1
        endpoint_checks += 1
assert endpoint_checks > 1000

# 3. Exact X15 three-projection identity and root-line equivalence.
projection_checks = 0
for D in range(2, 30):
    for A in range(1, D):
        xp = D * D + A * A
        xm = D * D - A * A
        x0 = 2 * D * A
        assert xp * xp == xm * xm + x0 * x0
        m, n = D + A, D - A
        assert m * n == xm
        assert m * m + n * n == 2 * xp
        assert m * m - n * n == 2 * x0
        projection_checks += 1
assert projection_checks > 200

# 4. Triple-centering identity: pairwise and triple covariance terms really remain.
wp = [1, 4, 2, 5]
wm = [3, 1, 6, 2]
wk = [2, 5, 1, 4]
P = len(wp)
mu_p = Fraction(sum(wp), P)
mu_m = Fraction(sum(wm), P)
mu_k = Fraction(sum(wk), P)
p0 = [Fraction(x) - mu_p for x in wp]
m0 = [Fraction(x) - mu_m for x in wm]
k0 = [Fraction(x) - mu_k for x in wk]
lhs = sum(Fraction(a*b*c) for a,b,c in zip(wp,wm,wk))
rhs = (
    P*mu_p*mu_m*mu_k
    + mu_p*sum(b*c for b,c in zip(m0,k0))
    + mu_m*sum(a*c for a,c in zip(p0,k0))
    + mu_k*sum(a*b for a,b in zip(p0,m0))
    + sum(a*b*c for a,b,c in zip(p0,m0,k0))
)
assert lhs == rhs

# 5. Boundary logic: an error O(B^(1/2-delta)) plus a principal B^(1/2)
# term still has exponent 1/2. This is arithmetic bookkeeping, not a lower bound.
for delta_i in range(1, 20):
    delta = Fraction(delta_i, 100)
    principal_exp = Fraction(1, 2)
    error_exp = Fraction(1, 2) - delta
    assert max(principal_exp, error_exp) == Fraction(1, 2)

print("Stage14-sH50 full-conductor principal-density audit: PASS")
print(f"conductor ledger checks: {ledger_checks}")
print(f"full-conductor endpoint checks: {endpoint_checks}")
print(f"three-projection checks: {projection_checks}")
print("certified whole-family delta: 0")
print("principal-density fixed-power loss certified: false")
print("main-term-scale signed anticorrelation certified: false")
print("next: Stage14-s7-51")
