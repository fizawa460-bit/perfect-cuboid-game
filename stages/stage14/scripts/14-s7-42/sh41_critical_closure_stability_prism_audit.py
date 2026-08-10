#!/usr/bin/env python3
from fractions import Fraction as F

TH0 = F(23, 88)
PH0 = F(19, 88)
CHI0 = F(9, 44)
OLD = F(23, 44)
BASE = F(19, 44)
HFIB = F(1, 22)
SQRT = F(1, 2)

assert BASE + HFIB == F(21, 44)
assert OLD - (BASE + HFIB) == F(1, 22)
assert SQRT - (BASE + HFIB) == F(1, 44)
assert 2 * TH0 + 2 * PH0 - F(3, 4) == CHI0


def env(theta: F, phi: F, s: F = F(0)) -> F:
    es = max(2 * theta, 1 - 2 * theta)
    ek = 3 * theta - F(1, 4)
    erc = 2 - 4 * theta - 2 * phi
    eh = 3 * phi - F(1, 8) - 3 * s
    return min(es, ek, erc, eh)


assert env(TH0, PH0) == OLD

# Exact one-sided near-critical approach: the pointwise H replacement alone
# does not yield an explicit fixed global delta.
for n in (100, 200, 500, 1000):
    eps = F(1, n)
    assert env(TH0, PH0 + eps) == OLD - 2 * eps
    assert env(TH0, PH0 - eps) == OLD - 3 * eps


def inherited_domain(theta: F, phi: F, s: F) -> bool:
    if not (F(3, 16) <= theta <= F(5, 16)):
        return False
    if not (F(1, 8) <= phi <= F(1, 4)):
        return False
    if not (F(0) <= theta - phi <= F(1, 8)):
        return False
    if theta + phi < F(3, 8):
        return False
    chi = 2 * theta + 2 * phi - F(3, 4)
    if chi > F(1, 4):
        return False
    if s < 0:
        return False
    return True


def danger_formula(theta: F, phi: F, s: F) -> bool:
    return (
        theta > F(1, 4)
        and 2 * theta + phi < F(3, 4)
        and phi - s > F(5, 24)
        and inherited_domain(theta, phi, s)
    )


# Exhaustive rational mesh: on the inherited low-core region, env>1/2 iff
# the three displayed danger inequalities hold.
checks = 0
for ti in range(48, 81):
    theta = F(ti, 256)
    for pi in range(32, 65):
        phi = F(pi, 256)
        for si in range(0, 17):
            s = F(si, 256)
            if not inherited_domain(theta, phi, s):
                continue
            checks += 1
            assert (env(theta, phi, s) > SQRT) == danger_formula(theta, phi, s)

# s=0 projection is the open triangle with closure vertices
# (1/4,5/24), (1/4,1/4), (13/48,5/24).
A = (F(1, 4), F(5, 24))
B = (F(1, 4), F(1, 4))
C = (F(13, 48), F(5, 24))
assert F(1, 4) < TH0 < F(13, 48)
assert F(5, 24) < PH0 < F(3, 4) - 2 * TH0

# The critical point is strictly inside the s=0 danger triangle.
assert danger_formula(TH0, PH0, F(0))

print("Stage14-s7-42 sH41 critical-closure / stability-prism audit: PASS")
print("mesh inherited blocks checked:", checks)
print("old critical exponent:", OLD)
print("sH41 critical endpoint exponent:", BASE + HFIB)
print("critical margin below sqrt:", SQRT - (BASE + HFIB))
print("current whole-family exponent remains:", OLD)
print("s=0 danger triangle vertices:", A, B, C)
print("next receiver: HalfBarrierNormalizedCrossRootSameSideSquareRemovedReverseReciprocalStabilityPrism")
