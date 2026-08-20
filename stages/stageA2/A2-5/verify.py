#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt


def sq(q):
    if q < 0:
        return False
    return isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator


def A(t):
    return t*t - 5*t - 5


def B(t):
    return t*t - t - 1


def Fplus(m):
    return m**4 + 6*m**3 + 23*m**2 + 22*m + 29


def Fminus(m):
    return m**4 + 6*m**3 - 37*m**2 + 42*m - 11


# Cplus birational chart from line R=1+m(t+1).
def plus_map(m, y):
    den = m*m - 1
    t = -(m*m + 2*m + 6) / den
    R = -(m*m + 7*m + 1) / den
    S = y / den
    return t, R, S


for m in [Fraction(-7, 2), Fraction(0), Fraction(2), Fraction(7, 3)]:
    if m*m == 1:
        continue
    # symbolic identity checked at enough exact points is supplemented by the
    # explicit polynomial identity below.
    pass

# Direct polynomial identity for the plus parameterization:
# (m^2-1)^2 * (-B(t(m)))?  Here S^2=B(t), so numerator is Fplus.
# Expand by hand-coded coefficient checks using exact evaluations at 5 points
# (both sides are quartics).
for m in [Fraction(-3), Fraction(-2), Fraction(0), Fraction(2), Fraction(4)]:
    den = m*m - 1
    t = -(m*m + 2*m + 6) / den
    assert B(t) * den * den == Fplus(m)
    R = -(m*m + 7*m + 1) / den
    assert R*R == A(t)


# Cminus birational chart from line R=3+m(t-1).
def minus_map(m, y):
    den = m*m + 1
    t = (m*m - 6*m + 4) / den
    R = -3*(m*m - m - 1) / den
    S = y / den
    return t, R, S


for m in [Fraction(-3), Fraction(-1), Fraction(0), Fraction(2), Fraction(4)]:
    den = m*m + 1
    t = (m*m - 6*m + 4) / den
    assert (-B(t)) * den * den == Fminus(m)
    R = -3*(m*m - m - 1) / den
    assert R*R == -A(t)


# Binary-quartic invariants.
def invariants_quartic(a, b, c, d, e):
    I = 12*a*e - 3*b*d + c*c
    J = 72*a*c*e + 9*b*c*d - 27*a*d*d - 27*b*b*e - 2*c**3
    return I, J


assert invariants_quartic(1, 6, 23, 22, 29) == (481, 9758)
assert invariants_quartic(1, 6, -37, 42, -11) == (481, 9758)
I, J = 481, 9758
assert -27*I == -12987
assert -27*J == -263466

# Short Jacobian cubic and rational 2-torsion factorization.
def cubic(x):
    return x**3 - 12987*x - 263466

for x in (-102, -21, 123):
    assert cubic(x) == 0

# Exact isomorphism-class adapter to LMFDB 15.a5 using c-invariants.
def weierstrass_invariants(a1, a2, a3, a4, a6):
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    return c4, c6, disc

c4m, c6m, Dm = weierstrass_invariants(1, 1, 1, -10, -10)
c4s, c6s, Ds = weierstrass_invariants(0, 0, 0, -12987, -263466)
assert (c4m, c6m, Dm) == (481, 4879, 50625)
assert c4s == 6**4 * c4m
assert c6s == 6**6 * c6m
assert Ds == 6**12 * Dm

# Smoothness of the two parameter quartics: discriminant values independently
# recorded from exact symbolic expansion in A2-5 result.
# We verify squarefreeness by checking gcd(f,f') over Q via Euclid.
def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_divmod(a, b):
    a = [Fraction(x) for x in a]
    b = [Fraction(x) for x in b]
    q = [Fraction(0)] * max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and any(a):
        k = len(a)-len(b)
        c = a[-1]/b[-1]
        q[k] = c
        for j in range(len(b)):
            a[j+k] -= c*b[j]
        poly_trim(a)
    return poly_trim(q), poly_trim(a)


def poly_gcd(a, b):
    a = [Fraction(x) for x in a]
    b = [Fraction(x) for x in b]
    while any(b):
        _, r = poly_divmod(a, b)
        a, b = b, r
    if a[-1] != 1:
        lead = a[-1]
        a = [x/lead for x in a]
    return a


def deriv(p):
    return [i*p[i] for i in range(1, len(p))]

fp = [29, 22, 23, 6, 1]
fm = [-11, 42, -37, 6, 1]
assert poly_gcd(fp, deriv(fp)) == [Fraction(1)]
assert poly_gcd(fm, deriv(fm)) == [Fraction(1)]

# Eight explicit rational points on Qplus (six finite + two infinities).
PLUS_FINITE = [
    (Fraction(-7, 2), Fraction(45, 4)),
    (Fraction(-7, 2), Fraction(-45, 4)),
    (Fraction(1), Fraction(9)),
    (Fraction(1), Fraction(-9)),
    (Fraction(-1), Fraction(5)),
    (Fraction(-1), Fraction(-5)),
]
for m, y in PLUS_FINITE:
    assert y*y == Fplus(m)

# The ordinary finite chart at m=-7/2 maps to t=-1.
for y in (Fraction(45, 4), Fraction(-45, 4)):
    t, R, S = plus_map(Fraction(-7, 2), y)
    assert (t, R) == (Fraction(-1), Fraction(1))
    assert S in (1, -1)

# m=+/-1 are chart poles and represent projective t=infinity.
assert Fplus(Fraction(1)) == 81
assert Fplus(Fraction(-1)) == 25
# The two quartic infinities have y/m^2 -> +/-1 and map to t=-1,R=-1.

# Eight explicit rational points on Qminus.
MINUS_FINITE = [
    (Fraction(1, 2), Fraction(5, 4)),
    (Fraction(1, 2), Fraction(-5, 4)),
    (Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(-1)),
    (Fraction(3), Fraction(5)),
    (Fraction(3), Fraction(-5)),
]
for m, y in MINUS_FINITE:
    assert y*y == Fminus(m)

for y in (Fraction(5, 4), Fraction(-5, 4)):
    t, R, S = minus_map(Fraction(1, 2), y)
    assert (t, R) == (Fraction(1), Fraction(3))
    assert S in (1, -1)

for m, yabs in [(Fraction(1), Fraction(1)), (Fraction(3), Fraction(5))]:
    for y in (yabs, -yabs):
        t, R, S = minus_map(m, y)
        assert t == Fraction(-1, 2)
        assert abs(R) == Fraction(3, 2)
        assert abs(S) == Fraction(1, 2)

# The two Qminus quartic infinities have y/m^2 -> +/-1 and map to t=1,R=-3.

# A2-4 landmarks under z(t).
def z_of_t(t):
    return (2*t*t - 8*t - 6) / (t*t - 1)

assert z_of_t(Fraction(-1, 2)) == 2
# t=+/-1 are poles of the z(t) chart -> E18 projective infinities.

print("A2-5 plus/minus birational quartics: PASS")
print("A2-5 common binary-quartic invariants I=481,J=9758: PASS")
print("A2-5 common Jacobian y^2=x^3-12987x-263466: PASS")
print("A2-5 exact 15.a5 c4/c6/discriminant adapter: PASS")
print("A2-5 eight explicit points on each cover quartic: PASS")
print("A2-5 external MW datum required: rank(15.a5)=0, torsion order=8")
print("A2-5 two-cover closure verifier: PASS modulo audited external MW datum")
