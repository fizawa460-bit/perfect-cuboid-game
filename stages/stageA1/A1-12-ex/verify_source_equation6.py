#!/usr/bin/env python3
"""Source sanity check for A1-12-ex.

Checks the published equation-(6) a0 coefficient against the remaining
published a1,a2,a3 formulas at one exact integer parameter point.
"""
from math import isqrt


def square(n):
    return n >= 0 and isqrt(n) ** 2 == n


def family(c, d, G, H, coefficient):
    c2, d2 = c*c, d*d
    c4, d4 = c2*c2, d2*d2
    c8, d8 = c4*c4, d4*d4

    F = (
        -4*c2*d4*(c2-d2)*G**4
        + (c8-coefficient*c4*d4+d8)*G**3*H
        + 8*c2*d2*(c2-d2)*(2*c2+d2)*G**2*H**2
        - (c8-coefficient*c4*d4+d8)*G*H**3
        - 4*c2*d4*(c2-d2)*H**4
    )
    a0 = (c2+d2)**2 * F**2

    a1 = (
        8*c2*d2*(c4-d4)**2*(G**2+H**2)**2
        *(2*c2*d2*G**2-(c4-d4)*G*H-2*c2*d2*H**2)
        *((c4-d4)*G**2+8*c2*d2*G*H-(c4-d4)*H**2)
    )

    fs = [
        d*(c+d)*G-c*(c-d)*H,
        d*(c-d)*G+c*(c+d)*H,
        (c2-2*c*d-d2)*G+(c2+d2)*H,
        (c2+2*c*d-d2)*G+(c2+d2)*H,
        (c2+d2)*G-(c2+2*c*d-d2)*H,
        c*(c+d)*G-d*(c-d)*H,
        c*(c-d)*G+d*(c+d)*H,
        (c2+d2)*G-(c2-2*c*d-d2)*H,
    ]
    a2 = (c2-d2)**2
    for f in fs:
        a2 *= f

    a3 = (
        4*c2*d2*G*H*(G**2-H**2)
        *((c4-d4)*G+4*c2*d2*H)
        *(4*c2*d2*G-(c4-d4)*H)
        *((c4-4*c2*d2-d4)*G+(c4+4*c2*d2-d4)*H)
        *((c4+4*c2*d2-d4)*G-(c4-4*c2*d2-d4)*H)
    )
    return a0, a1, a2, a3


def cube_square_pattern(vals):
    a0,a1,a2,a3 = vals
    sums = [a0,a0+a1,a0+a2,a0+a1+a2,a0+a3,a0+a1+a3,a0+a2+a3,a0+a1+a2+a3]
    return [square(s) for s in sums]


# Exact nondegenerate test point.
params = (3, 1, 7, 1)
pat18 = cube_square_pattern(family(*params, coefficient=18))
pat8  = cube_square_pattern(family(*params, coefficient=8))

assert pat18 == [True]*8
assert pat8 == [True, False, False, False, False, False, False, False]

# Correct normalized anchor discriminant/reciprocal quotient for coefficient 18:
# D(k)=k^8-36k^6+256k^5-186k^4+256k^3-36k^2+1,
# D(k)/k^4 = Q18(k+1/k), Q18(z)=z^4-40z^2+256z-112.

print("published_coefficient_minus18_cube_check=PASS")
print("project_minus8_replacement_cube_check=FAIL_AS_EXPECTED")
print("correct_reciprocal_quartic=z^4-40*z^2+256*z-112")
print("A1-12-ex source attachment verdict: FAIL_SOURCE_COEFFICIENT_MISMATCH")
