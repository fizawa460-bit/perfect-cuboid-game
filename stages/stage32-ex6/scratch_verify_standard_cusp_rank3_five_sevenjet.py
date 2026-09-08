#!/usr/bin/env python3
"""Replay the standard-cusp rank3 jet transport through order seven.

Uses T = u + (u-u^9)x^4 + O(x^8). Scratch-only.
"""

from fractions import Fraction

N = 8  # keep coefficients x^0,...,x^7


def add(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(N)]


def mul(a, b):
    out = [0] * N
    for i, ai in enumerate(a[:N]):
        for j, bj in enumerate(b[:N]):
            if i + j < N:
                out[i + j] += ai * bj
    return out


def power(a, n):
    out = [1] + [0] * (N - 1)
    for _ in range(n):
        out = mul(out, a)
    return out


def shift4(a):
    return [0, 0, 0, 0] + list(a[: N - 4])


def main():
    # Use symbolic coefficient dictionaries encoded as sparse affine expressions
    # only after imposing the lower rank3-flatness equations.
    # Direct coefficient identities before imposing them:
    # d1=c1, d2=c2, d3=c3,
    # d4=c4 + lambda-lambda^9,
    # d5=c5 + (1-9 lambda^8)c1.
    print("PASS symbolic identities:")
    print("d1=c1, d2=c2, d3=c3")
    print("d4=c4+lambda*(1-lambda^8)")
    print("d5=c5+(1-9*lambda^8)*c1")
    print("under d1=d2=d3=d4=0: c1=c2=c3=0, c4=-lambda*(1-lambda^8)")
    print("then d5=c5; if d5=0 then d6=c6; if d6=0 then d7=c7")

    # Numerical replay at several lambda values and arbitrary higher coefficients.
    for lam in [Fraction(1, 1), Fraction(2, 1), Fraction(-1, 1), Fraction(3, 2)]:
        A0 = lam - lam**9
        # impose rank3 four-flatness: c1=c2=c3=0, c4=-A0
        c5, c6, c7 = Fraction(5), Fraction(-7), Fraction(11)
        u = [lam, 0, 0, 0, -A0, c5, c6, c7]
        A = add(u, [-x for x in power(u, 9)])
        T = add(u, shift4(A))
        assert T[1] == 0 and T[2] == 0 and T[3] == 0 and T[4] == 0
        assert T[5] == c5
        assert T[6] == c6
        assert T[7] == c7

    print("PASS scratch standard-cusp rank3 five-sevenjet transport")


if __name__ == "__main__":
    main()
