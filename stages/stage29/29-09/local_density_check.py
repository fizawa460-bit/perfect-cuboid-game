#!/usr/bin/env python3
"""Exact finite-field regression for Stage29-09 seven-form local arithmetic."""

from fractions import Fraction


def primes_below(n):
    out = []
    for x in range(3, n, 2):
        if all(x % d for d in range(3, int(x**0.5) + 1, 2)):
            out.append(x)
    return out


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def projective_points(p):
    # Unique representatives with first nonzero coordinate normalized to 1.
    for y in range(p):
        for z in range(p):
            yield (1, y, z)
    for z in range(p):
        yield (0, 1, z)
    yield (0, 0, 1)


def seven_values(P, p):
    x, y, z = P
    return (
        x % p,
        y % p,
        z % p,
        (x + y) % p,
        (x + z) % p,
        (y + z) % p,
        (x + y + z) % p,
    )


def eligible(P, p):
    vals = seven_values(P, p)
    signs = {chi(v, p) for v in vals if v}
    return len(signs) <= 1


def enumerate_A(p):
    host = [0, 0, 0, 0]
    A = [0, 0, 0, 0]
    for P in projective_points(p):
        vals = seven_values(P, p)
        k = sum(v == 0 for v in vals)
        assert 0 <= k <= 3
        host[k] += 1
        if eligible(P, p):
            A[k] += 1
    return host, A


def elliptic_trace(p):
    # E: y^2 = x^3 - x.
    points = 1  # point at infinity
    for x in range(p):
        rhs = (x * x * x - x) % p
        points += 1 if rhs == 0 else 1 + chi(rhs, p)
    return p + 1 - points


def predicted_branch_counts(p):
    eps = chi(-1, p)
    eta = chi(2, p)
    aE = elliptic_trace(p)
    A1 = (
        Fraction(3 * (p - 4 - eps), 4)
        + Fraction((1 + eps) * (p - 5), 8)
        + Fraction(3 * (1 + eps) * (p - 11 - 4 * eta - aE), 16)
    )
    A2 = Fraction(3 * (1 + eps) * (1 + eta), 4)
    A3 = Fraction(3 * (3 + eps), 2)
    assert A1.denominator == A2.denominator == A3.denominator == 1
    return int(A1), int(A2), int(A3), aE


def q_values(p):
    eps = chi(-1, p)
    q1 = Fraction(1, 2 * (p + 1))
    q2 = q1 * q1
    q3 = Fraction(
        p * p - (3 + eps) * p + 1,
        8 * (p + 1) ** 2 * (p * p + 1),
    )
    return q1, q2, q3


def main():
    print("p eps eta aE host0 A0 A1 A2 A3 Sbar delta_p")
    for p in primes_below(100):
        host, A = enumerate_A(p)
        A1, A2, A3, aE = predicted_branch_counts(p)
        assert host[0] == (p - 3) ** 2
        assert A[1:] == [A1, A2, A3]

        # Exact normal-cover fiber identity: eligible depth-k fiber has 2^(6-k) points.
        sbar = sum(A[k] * 2 ** (6 - k) for k in range(4))

        q1, q2, q3 = q_values(p)
        delta = (
            Fraction(A[0], 1)
            + A[1] * q1
            + A[2] * q2
            + A[3] * q3
        ) / (p * p + p + 1)

        print(
            p,
            chi(-1, p),
            chi(2, p),
            aE,
            host[0],
            *A,
            sbar,
            f"{delta.numerator}/{delta.denominator}",
        )

    print("PASS: exact branch formulas and odd-prime density ledger verified below 100")


if __name__ == "__main__":
    main()
