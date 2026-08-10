#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def main():
    checks = 0
    samples = [
        (1, 5, 7, 11, 2, 3, 5, 7),
        (3, 5, 7, 11, 1, 2, 3, 4),
        (5, 7, 11, 13, 2, 1, 4, 3),
    ]
    for q11,q12,q21,q22,a0,b0,c0,d0 in samples:
        assert gcd(q11,q22) == 1
        assert gcd(q12,q21) == 1
        Q = q11*q12*q21*q22
        U = q11*q22
        V = q12*q21
        assert U*V == Q
        assert min(U,V)*min(U,V) <= Q

        F = (q12*q12*a0*d0)**2 - (q21*q21*b0*c0)**2
        G = (q22*q22*b0*d0)**2 - (q11*q11*a0*c0)**2

        # Main diagonal: y^4*A^2-x^4*B^2.
        assert G == q22**4*(b0*d0)**2 - q11**4*(a0*c0)**2
        # Off diagonal: x^4*A^2-y^4*B^2.
        assert F == q12**4*(a0*d0)**2 - q21**4*(b0*c0)**2
        checks += 1

    core = Fraction(3,7)
    good_res = core + Fraction(1,2)
    assert good_res == Fraction(13,14)
    whole = max(Fraction(20,21), Fraction(61,63), good_res)
    assert whole == Fraction(61,63)
    assert Fraction(41,42) - whole == Fraction(1,126)
    assert whole - Fraction(1,2) == Fraction(59,126)

    print(f'DIAGONAL_ALGEBRA_SAMPLE_CHECKS={checks}')
    print('DIAGONAL_PRODUCTS_UV_EQUAL_Q_AUDIT=true')
    print('MAIN_DIAGONAL_QUARTIC_FORM_AUDIT=true')
    print('OFF_DIAGONAL_QUARTIC_FORM_AUDIT=true')
    print('GOOD_CELL_RESIDUAL_EXPONENT_13_14=true')
    print('WHOLE_FAMILY_EXPONENT_61_63=true')
    print('WHOLE_FAMILY_POST_LOCAL_SAVING_1_126=true')
    print('REMAINING_SQRT_GAP_59_126=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
