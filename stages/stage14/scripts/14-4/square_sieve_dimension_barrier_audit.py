#!/usr/bin/env python3
from fractions import Fraction as F


def square_sieve_exponent(d: int) -> F:
    # N(A) <= A/L + L^d, L=A^a.  Balance 1-a=d*a.
    a = F(1, d + 1)
    return F(d, d + 1), a


def global_exponents(lam: F, nu: F, tau: F):
    return {
        "E1": 2 * lam,
        "E2": 1 + nu - lam,
        "E3": 1 - F(4, 5) * tau,
        "E4": 1 - (nu - 2 * tau) / 3,
        "E5": 1 - (lam - 2 * tau) / 3,
    }


def main():
    # Dimension-law locks.
    e2, a2 = square_sieve_exponent(2)
    assert e2 == F(2, 3) and a2 == F(1, 3)
    e4, a4 = square_sieve_exponent(4)
    assert e4 == F(4, 5) and a4 == F(1, 5)

    # Naive enlargement with no forced lower bound on added cells is weaker.
    saving2 = F(1, 3)
    saving3 = F(1, 4)
    saving4 = F(1, 5)
    assert saving2 > saving3 > saving4

    # Current exact optimum from merged 4by.
    lam = F(13, 28)
    nu = F(11, 28)
    tau = F(5, 56)
    E = global_exponents(lam, nu, tau)
    ceiling = F(13, 14)
    assert E["E1"] == ceiling
    assert E["E2"] == ceiling
    assert E["E3"] == ceiling
    assert E["E4"] == ceiling
    assert E["E5"] == F(19, 21)
    assert ceiling - E["E5"] == F(1, 42)

    # Barrier algebra: if all E1..E4 <= e then
    # nu <= 3e/2 - 1 and nu >= 11(1-e)/2, forcing e>=13/14.
    e = F(13, 14)
    upper_nu = F(3, 2) * e - 1
    lower_nu = F(11, 2) * (1 - e)
    assert upper_nu == lower_nu == nu

    # Grid regression: no nearby rational threshold triple beats 13/14.
    best = (F(2, 1), None)
    den = 112
    for il in range(1, den // 2):
        l = F(il, den)
        for it in range(1, il // 2 + 1):
            t = F(it, den)
            if 2 * t >= l:
                continue
            for inu in range(2 * it + 1, il + 1):
                n = F(inu, den)
                vals = global_exponents(l, n, t)
                m = max(vals["E1"], vals["E2"], vals["E3"], vals["E4"])
                if m < best[0]:
                    best = (m, (l, n, t))
    assert best[0] >= ceiling

    print("Stage14-4bz audit: PASS")
    print("d=2 square-sieve exponent:", e2)
    print("d=4 square-sieve exponent:", e4)
    print("current ceiling:", ceiling)
    print("denominator-thin slack:", F(1, 42))
    print("grid best:", best)


if __name__ == "__main__":
    main()
