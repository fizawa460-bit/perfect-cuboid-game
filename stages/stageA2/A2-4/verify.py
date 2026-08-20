#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def is_square_int(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_square_frac(q):
    if q < 0:
        return False
    return is_square_int(q.numerator) and is_square_int(q.denominator)


def q18(z):
    return z**4 - 40*z**2 + 256*z - 112


def f1(z):
    return z**2 - 8*z + 28


def f2(z):
    return z**2 + 8*z - 4


# Exact quotient factorization.
for z in [Fraction(-7, 3), Fraction(0), Fraction(2), Fraction(11, 5)]:
    assert q18(z) == f1(z) * f2(z)

# Binary gcd identities used in the first squareclass split.
for a in range(-25, 26):
    for b in range(1, 26):
        if gcd(a, b) != 1:
            continue
        F1 = a*a - 8*a*b + 28*b*b
        F2 = a*a + 8*a*b - 4*b*b
        assert gcd(F1, b) == 1
        assert gcd(F2, b) == 1
        assert gcd(abs(F1), abs(F2)) & ~255 == 0  # gcd divides 2^8

# Projective mod-5 obstruction for delta=2 in the first split.
sq5 = {0, 1, 4}
# Infinity B=0: A^2=2R^2 has no nonzero projective solution.
assert all(((a*a - 2*r*r) % 5 != 0) for a in range(1, 5) for r in range(5))
# Affine B=1: no simultaneous pair.
first_delta2_affine = []
for a in range(5):
    F1 = (a*a - 8*a + 28) % 5
    F2 = (a*a + 8*a - 4) % 5
    if (F1 * 3) % 5 in sq5 and (F2 * 3) % 5 in sq5:  # divide by 2 mod 5
        first_delta2_affine.append(a)
assert first_delta2_affine == []

# Rational parameterization of U^2=f1(z) through (2,4).
def z_of_t(t):
    return (2*t*t - 8*t - 6) / (t*t - 1)


def u_of_t(t):
    return -4*(t*t + t + 1) / (t*t - 1)


for t in [Fraction(-3), Fraction(-1, 2), Fraction(0), Fraction(2), Fraction(7, 3)]:
    z = z_of_t(t)
    u = u_of_t(t)
    assert u*u == f1(z)
    rhs = Fraction(16) * (t*t - 5*t - 5) * (t*t - t - 1) / (t*t - 1)**2
    assert f2(z) == rhs
    recon = -Fraction(16) * (2*t + 1) * (t*t - 2*t - 2) / (t*t - 1)**2
    assert z*z - 4 == recon

# Excluded wall t=-1/2 maps to z=2,U=4.
assert z_of_t(Fraction(-1, 2)) == 2
assert u_of_t(Fraction(-1, 2)) == 4

# Second binary gcd identity.
for a in range(-25, 26):
    for b in range(1, 26):
        if gcd(a, b) != 1:
            continue
        A = a*a - 5*a*b - 5*b*b
        B = a*a - a*b - b*b
        assert gcd(A, b) == 1
        assert gcd(abs(A), abs(B)) <= 4
        assert 4 % gcd(abs(A), abs(B)) == 0

# Projective mod-5 obstruction for delta=+2 and -2 in the second split.
# At infinity b=0, A=B=a^2; both +/-2 are nonsquares mod 5.
for delta in (2, -2):
    dinv = pow(delta % 5, -1, 5)
    assert dinv not in sq5
    affine = []
    for a in range(5):
        A = (a*a - 5*a - 5) % 5
        B = (a*a - a - 1) % 5
        if (A * dinv) % 5 in sq5 and (B * dinv) % 5 in sq5:
            affine.append(a)
    assert affine == []

# Known surviving branch points / routing landmarks.
# Cplus t=-1 is a projective quartic-infinity landmark.
t = Fraction(-1)
assert t*t - 5*t - 5 == 1
assert t*t - t - 1 == 1
# Cminus t=1 is the other quartic-infinity landmark.
t = Fraction(1)
assert -(t*t - 5*t - 5) == 9
assert -(t*t - t - 1) == 1
# Cminus t=-1/2 is the excluded affine wall z=2.
t = Fraction(-1, 2)
assert -(t*t - 5*t - 5) == Fraction(9, 4)
assert -(t*t - t - 1) == Fraction(1, 4)
assert is_square_frac(-(t*t - 5*t - 5))
assert is_square_frac(-(t*t - t - 1))

print("A2-4 Q18 factorization: PASS")
print("A2-4 first squareclass support {1,2}: PASS")
print("A2-4 first delta=2 Q5 obstruction: PASS")
print("A2-4 conic t-parameter identities: PASS")
print("A2-4 second squareclass support {+1,-1,+2,-2}: PASS")
print("A2-4 second +/-2 Q5 obstruction: PASS")
print("A2-4 first reconstruction t-cover identity: PASS")
print("A2-4 exact factor-cover descent: PASS")
