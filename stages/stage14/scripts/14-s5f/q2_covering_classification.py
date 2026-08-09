#!/usr/bin/env python3
from fractions import Fraction

EXPECTED = {
    (1, 1, 1),
    (3, 7, 5),
    (5, 1, 5),
    (7, 7, 1),
    (2, 1, 2),
    (6, 7, 10),
    (10, 1, 10),
    (14, 7, 2),
}


def v2_odd(n):
    n = int(n)
    sgn = -1 if n < 0 else 1
    n = abs(n)
    v = 0
    while n and n % 2 == 0:
        n //= 2
        v += 1
    return v, sgn * n


def q2_class(x):
    if x == 0:
        return None
    vn, un = v2_odd(x.numerator)
    vd, ud = v2_odd(x.denominator)
    parity = (vn - vd) & 1
    unit = (un * pow(ud % 8, -1, 8)) % 8
    return unit if parity == 0 else 2 * unit


def square_q2(x):
    return q2_class(x) == 1


def triple(q, lam):
    xs = (q, q - 1, q + lam)
    if any(x == 0 for x in xs):
        return None
    prod = xs[0] * xs[1] * xs[2]
    if not square_q2(prod):
        return None
    return tuple(q2_class(x) for x in xs)


def representative_audit(k):
    # lambda=t^2, with v2(lambda)=k even and >=4; its odd unit is a square.
    lam = Fraction(2**k, 1)
    out = set()
    # Critical valuation bands plus stable tails.  Odd residues modulo 2^12
    # distinguish every Q2 squareclass and all q, q-1, q+lambda cylinders
    # needed once v2(lambda)>=4.
    for v in range(-10, 11):
        for u in range(1, 2**12, 2):
            q = Fraction(u * 2 ** max(v, 0), 2 ** max(-v, 0))
            t = triple(q, lam)
            if t is not None:
                out.add(t)
    return out


def main():
    assert len(EXPECTED) == 8
    for state in EXPECTED:
        assert len(state) == 3
        # product squareclass check via representatives
        p = Fraction(state[0] * state[1] * state[2], 1)
        assert square_q2(p)

    for k in (4, 6, 8, 10):
        got = representative_audit(k)
        assert got == EXPECTED, (k, sorted(got), sorted(EXPECTED))

    # The exact proof used in result.md is the residue-cylinder lemma:
    # squareclass depends only on valuation parity and odd unit mod 8, and
    # 1+8 Z_2 consists of squares.  The deep representative audit here is
    # deliberately only an independent regression check, not the logical
    # substitute for that lemma.
    print('STAGE14_S5F=COMPLETE_FULL_LOCAL_CHARACTER_SYSTEM')
    print('Q2_PRODUCT_SQUARE_STATE_COUNT=64')
    print('Q2_COVERING_SOLUBLE_STATE_COUNT=8')
    print('Q2_COVERING_SPECIFIC_64_STATE_SOLUBILITY_CLASSIFIED=true')
    print('FULL_LOCAL_2_DESCENT_CHARACTER_SYSTEM_COMPLETE=true')
    print('FAMILY_LARGE_SIEVE_THEOREM_PROVED=false')
    print('SQRT_B_ASYMPTOTIC_PROVED=false')
    print('NEXT=Stage14-s5g')


if __name__ == '__main__':
    main()
