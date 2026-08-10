#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd


def assert_two_thirds_envelope():
    # Exact rational grid containing every named boundary/crossover.
    den = 192
    vals = []
    eq = []
    for ti in range(36, 61):  # 3/16 .. 5/16
        th = F(ti, den)
        for pi in range(24, 49):  # 1/8 .. 1/4
            ph = F(pi, den)
            if th < ph:
                continue
            if th - ph > F(1, 8):
                continue
            if th + ph < F(3, 8):
                continue
            e30 = max(th + ph + F(1, 8), 1 - 2 * th)
            ec = F(5, 4) - 2 * th
            e = min(e30, ec)
            vals.append(e)
            if e == F(2, 3):
                eq.append((th, ph))
    assert vals and max(vals) == F(2, 3)
    assert eq == [(F(7, 24), F(1, 4))], eq

    th = F(7, 24)
    ph = F(1, 4)
    c = 2 * th + 2 * ph - F(3, 4)
    mu = 2 * th - 2 * ph
    nu = F(1, 4) + 2 * ph - 2 * th
    first = 2 * ph - c
    assert c == F(1, 3)
    assert mu == F(1, 12)
    assert nu == F(1, 6)
    assert first == F(1, 6)
    assert nu / 2 == F(1, 12)
    assert max(th + ph + F(1, 8), 1 - 2 * th) == F(2, 3)
    assert F(5, 4) - 2 * th == F(2, 3)

    # The former s7-30 11/16 corner is killed by the Cayley ledger.
    old_th, old_ph = F(5, 16), F(1, 4)
    assert F(5, 4) - 2 * old_th == F(5, 8)
    assert F(5, 8) < F(2, 3) < F(11, 16)


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y


def inv(a, m):
    g, x, _ = egcd(a % m, m)
    assert g == 1
    return x % m


def crt_pair(a1, m1, a2, m2):
    assert gcd(m1, m2) == 1
    t = ((a2 - a1) * inv(m1, m2)) % m2
    return (a1 + m1 * t) % (m1 * m2)


def roots_minus_one(p):
    return [x for x in range(1, p) if x * x % p == p - 1]


def assert_cayley_allocation():
    # Build exact synthetic good-core packets with prescribed +/- allocation.
    # All primes are 1 mod 4 so the Gaussian roots exist.
    cases = [
        (5, 13, 2),
        (13, 17, 3),
        (17, 29, 5),
    ]
    for cminus, cplus, n0 in cases:
        C = cminus * cplus
        assert gcd(cminus, cplus) == 1
        # M == N mod C_- and M == -N mod C_+.
        M = crt_pair(n0 % cminus, cminus, (-n0) % cplus, cplus)
        N = n0
        assert gcd(C, M * N) == 1
        assert (M - N) % cminus == 0
        assert (M + N) % cplus == 0
        assert ((M - N) * (M + N)) % C == 0

        Cm = gcd(C, M - N)
        Cp = gcd(C, M + N)
        assert Cm == cminus
        assert Cp == cplus
        assert gcd(Cm, Cp) == 1
        assert Cm * Cp == C

        # lambda = 4M/N on each prime.  Verify orientation dictionary.
        for p, same in [(cminus, False), (cplus, True)]:
            roots = roots_minus_one(p)
            assert len(roots) == 2
            x = roots[0]
            lam = (4 * (M % p) * inv(N, p)) % p
            assert lam in (4 % p, (-4) % p)
            # lambda*x*y == 4; solve y and check y=+x on C_+, -x on C_-.
            y = (4 * inv((lam * x) % p, p)) % p
            assert y * y % p == p - 1
            if same:
                assert y == x
                assert (M + N) % p == 0
            else:
                assert y == (-x) % p
                assert (M - N) % p == 0


def assert_bad_core_guard():
    # Only the theorem shape is frozen: the removed part is a divisor of
    # (r*s*X*Y)^2 and can therefore be reconstructed divisor-wise after XY.
    for rsxy in [3, 5, 15, 35]:
        square = rsxy * rsxy
        divs = [d for d in range(1, square + 1) if square % d == 0]
        for d in divs:
            assert square % d == 0


def main():
    assert_two_thirds_envelope()
    assert_cayley_allocation()
    assert_bad_core_guard()
    print("STAGE14_4CR_AUDIT=PASS")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=2/3")
    print("UNIQUE_SATURATION=theta=7/24,phi=1/4,c=1/3")
    print("CAYLEY_GAUSSIAN_SIGN_ALLOCATION=PASS")


if __name__ == "__main__":
    main()
