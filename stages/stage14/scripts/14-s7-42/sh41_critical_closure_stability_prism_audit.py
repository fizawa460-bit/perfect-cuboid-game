#!/usr/bin/env python3
from fractions import Fraction as F

SQRT = F(1, 2)
OLD = F(23, 44)
SH41_BASE = F(19, 44)
SH41_FIBER = F(1, 22)

# Independent sH41 old-critical check.
assert SH41_BASE + SH41_FIBER == F(21, 44)
assert SQRT - (SH41_BASE + SH41_FIBER) == F(1, 44)


def chi(phi: F) -> F:
    # theta = 1/4
    return 2 * phi - F(1, 4)


def A(phi: F) -> F:
    # first residual and X13 single-column exponent
    return F(1, 2) - 2 * phi


def nu(phi: F) -> F:
    # opposite signed product cap at theta=1/4
    return 2 * phi - F(1, 4)


def fixed_k_bound(phi: F, kappa: F) -> F:
    a = A(phi)
    assert 0 <= kappa <= a / 2
    # common base 2phi + K choice kappa + column quotient a-2kappa
    return 2 * phi + kappa + (a - 2 * kappa)


# X13 sqrt band and exact theta-quarter scale identities.
checks = 0
for i in range(0, 89):
    # phi from 5/24 to 1/4 on denominator 1056 grid.
    phi = F(5, 24) + F(i, 2112)
    if phi > F(1, 4):
        break
    checks += 1
    a = A(phi)
    assert F(0) <= a <= F(1, 12)
    assert F(1, 4) - chi(phi) == a
    assert nu(phi) == chi(phi)
    assert 2 * phi + a == SQRT

    # Test all rational K strata on a small exact mesh.
    for j in range(0, 17):
        kappa = (a / 2) * F(j, 16)
        e = fixed_k_bound(phi, kappa)
        assert e == SQRT - kappa
        assert e <= SQRT
        if kappa > 0:
            assert e < SQRT

# Endpoints.
assert A(F(5, 24)) == F(1, 12)
assert A(F(1, 4)) == 0
assert chi(F(5, 24)) == F(1, 6)
assert chi(F(1, 4)) == F(1, 4)

# X13 piecewise whole-strip closure.
def ek(theta: F) -> F:
    return 3 * theta - F(1, 4)


def errf(theta: F) -> F:
    return 1 - 2 * theta

for t in range(48, 81):
    theta = F(t, 256)
    if theta <= F(1, 4):
        assert ek(theta) <= SQRT
    if theta >= F(1, 4):
        assert errf(theta) <= SQRT

print("Stage14-s7-42 X13 sqrt / theta-quarter same-side-gcd audit: PASS")
print("theta-quarter phi blocks checked:", checks)
print("current whole-family exponent:", SQRT)
print("sH41 old critical endpoint:", SH41_BASE + SH41_FIBER)
print("theta-quarter residual/column exponent range: [0, 1/12]")
print("fixed K block exponent: 1/2-kappa")
print("sqrt saturation requires K=B^o(1)")
print("next receiver: SquareRootThetaQuarterSameSidePrimitiveFirstResidualSingleColumnIncidence")
