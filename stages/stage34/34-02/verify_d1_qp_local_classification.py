#!/usr/bin/env python3
"""Exact local classification for the 22 Stage34-02 D1 residual squareclasses.

For a reduced q=a/b and projective x=X/Z, the split squareclass cover has

  E_h = X Z (X+Z)(b^2 X+a^2 Z) = Y^2,
  A_h = b^2 X^2+a^2 Z^2          = d U^2,
  B_h = b^2(a^2+b^2)X^2 + 4a^2b^2XZ
        + a^2(a^2+b^2)Z^2        = d V^2.

For the eight nontrivial residual classes, d is a 7-adic unit.  Any Q_7 point
can be scaled so X,Z are 7-adic integers not both divisible by 7; then Y,U,V
are integral as well.  Reduction therefore gives a point in P^1(F_7) satisfying
all three square conditions.  Exhausting the eight projective residues proves
Q_7-insolubility when none survives.

The d=1 and d=2 classes are locally soluble at every place because explicit
Q-rational points are supplied: x=0 for d=1, and x=q for d=2.
"""

from fractions import Fraction

NONTRIVIAL = [
    (80, 39, 5), (80, 39, 10), (80, 39, 13), (80, 39, 26),
    (80, 39, 65), (80, 39, 130),
    (60, 11, 5), (60, 11, 10),
]

ALL_Q = [(20,21,29),(80,39,89),(24,7,25),(84,13,85),(48,55,73),(20,99,101),(60,11,61)]


def is_square(v, p):
    v %= p
    return v == 0 or pow(v, (p - 1) // 2, p) == 1


def residues_mod_7(a, b, d):
    p = 7
    assert d % p != 0
    invd = pow(d, -1, p)
    out = []
    for X, Z in [(x, 1) for x in range(p)] + [(1, 0)]:
        E = X * Z * (X + Z) * (b*b*X + a*a*Z)
        A = b*b*X*X + a*a*Z*Z
        B = b*b*(a*a+b*b)*X*X + 4*a*a*b*b*X*Z + a*a*(a*a+b*b)*Z*Z
        if is_square(E, p) and is_square(A * invd, p) and is_square(B * invd, p):
            out.append([X % p, Z % p])
    return out


def rational_witnesses(a, b, c):
    # a^2+b^2=c^2 is part of the seven locked Paper-C q values.
    assert a*a + b*b == c*c
    q = Fraction(a, b)

    # d=1, x=0: E=0, A=q^2, B=q^2(1+q^2)=(q*c/b)^2.
    x1 = Fraction(0)
    y1 = Fraction(0)
    u1 = q
    v1 = q * Fraction(c, b)
    A1 = x1*x1 + q*q
    B1 = (1+q*q)*x1*x1 + 4*q*q*x1 + q*q*(1+q*q)
    assert y1*y1 == x1*(x1+1)*(x1+q*q)
    assert A1 == u1*u1
    assert B1 == v1*v1

    # d=2, x=q: pole point on E, but a valid rational point of the split
    # squareclass equations.  A=2q^2 and B=2q^2(q+1)^2.
    x2 = q
    y2 = q*(q+1)
    u2 = q
    v2 = q*(q+1)
    A2 = x2*x2 + q*q
    B2 = (1+q*q)*x2*x2 + 4*q*q*x2 + q*q*(1+q*q)
    assert y2*y2 == x2*(x2+1)*(x2+q*q)
    assert A2 == 2*u2*u2
    assert B2 == 2*v2*v2
    return True


for a,b,c in ALL_Q:
    assert rational_witnesses(a,b,c)

for a,b,d in NONTRIVIAL:
    r = residues_mod_7(a,b,d)
    if r:
        raise SystemExit(f"unexpected mod-7 residue for q={a}/{b}, d={d}: {r}")
    print(f"PASS Q_7 obstruction q={a}/{b} d={d}: P1(F7) residue count 0")

print("PASS D1 local classification: 14 classes Q-rationally soluble, 8 classes Q_7-insoluble")
