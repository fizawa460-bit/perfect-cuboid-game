#!/usr/bin/env python3
from fractions import Fraction
from math import sqrt


def require(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def chi_y(m):
    # Perfect-cuboid resolution: K^2=16, c2=80.
    return (
        -Fraction(32, 3) * m**3
        - 40 * m**2
        - Fraction(64, 3) * m
        + 8
    )


def chi0_a1(m):
    s = m % 6
    if s == 0:
        return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 + Fraction(1,6)*m
    if s == 1:
        return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 - Fraction(1,12)*m - Fraction(35,108)
    if s == 2:
        return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 + Fraction(7,18)*m + Fraction(5,27)
    if s == 3:
        return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 - Fraction(1,12)*m - Fraction(1,4)
    if s == 4:
        return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 + Fraction(1,6)*m - Fraction(2,27)
    return Fraction(11,108)*m**3 + Fraction(11,36)*m**2 + Fraction(5,36)*m - Fraction(7,108)


def chi1_a1(m):
    s = m % 3
    if s == 0:
        return Fraction(4,27)*m**3 + Fraction(4,9)*m**2 + Fraction(1,3)*m
    if s == 1:
        return Fraction(4,27)*m**3 + Fraction(4,9)*m**2 + Fraction(1,3)*m + Fraction(2,27)
    return Fraction(4,27)*m**3 + Fraction(4,9)*m**2 + Fraction(1,9)*m - Fraction(5,27)


def btva_partial_lower(m, r):
    # Proposition 3.1 with ell=48 A1 singularities.
    return chi_y(m) + 48 * chi1_a1(m) + r * chi0_a1(m)


def cubic_coeff_for_support(N):
    # r=48-N exceptional components removed in BTVA's notation.
    # chiY cubic -32/3, 48*chi1 cubic 48*4/27,
    # r*chi0 cubic r*11/108.
    return (
        -Fraction(32,3)
        + 48*Fraction(4,27)
        + (48-N)*Fraction(11,108)
    )


def one_layer_cost(m):
    # Internal local-model count used only for scale bookkeeping.
    if m % 2 == 0:
        return 3*m*m//4
    return (m-1)*(3*m+1)//4


def main():
    # BTVA support threshold.
    require(cubic_coeff_for_support(13) == Fraction(1,108), "N13 cubic coefficient")
    require(cubic_coeff_for_support(14) == -Fraction(5,54), "N14 cubic coefficient")
    for N in range(0,14):
        require(cubic_coeff_for_support(N) > 0, f"N={N} should have positive cubic coefficient")
    for N in range(14,49):
        require(cubic_coeff_for_support(N) < 0, f"N={N} should have negative cubic coefficient")

    # Exact check of the BTVA statement that r=35 first turns positive at m=862.
    require(all(btva_partial_lower(m,35) <= 0 for m in range(3,862)), "r35 no earlier positive order")
    require(btva_partial_lower(862,35) == 7320, "r35 m862 exact lower bound")

    # r=34 / N=14 exact residue-class factorization:
    # m=6q+s gives -2*P_s(q).
    def P(s,q):
        if s == 0:
            return 10*q**3 + 149*q**2 - q - 4
        if s == 1:
            return 10*q**3 + 154*q**2 + 75*q + 8
        if s == 2:
            return (2*q+1)*(5*q**2 + 77*q + 17)
        if s == 3:
            return 10*q**3 + 164*q**2 + 181*q + 51
        if s == 4:
            return 10*q**3 + 169*q**2 + 211*q + 64
        return (q+1)*(10*q**2 + 164*q + 139)

    for s in range(6):
        for q in range(0,40):
            m=6*q+s
            if m >= 3:
                require(btva_partial_lower(m,34) == -2*P(s,q), f"r34 factorization s={s} q={q}")

    # Positivity of P_s on the relevant domains is elementary.
    # s=0 only occurs with q>=1 for m>=3; then
    # 149q^2-q >=148q and 10q^3-4>0.
    require(P(0,1)>0, "s0 base positivity")
    for s in range(1,6):
        qmin = 0 if s >= 3 else 1
        require(P(s,qmin)>0, f"s{s} base positivity")
    require(all(btva_partial_lower(m,34) < 0 for m in range(3,10000)), "r34 sampled sign regression")

    # Revived-Z forced-minimal density: positive through N=13, negative at N=14.
    vals={}
    for N in range(10,15):
        vals[N]=2-sqrt(3*N/28)-sqrt((N-8)/8)
    require(all(vals[N]>0 for N in range(10,14)), "minimal-density positivity N10..13")
    require(vals[14]<0, "minimal-density sign break N14")

    # A fixed number of one-layer conditions is quadratic in m, so cannot
    # alter a nonzero cubic leading coefficient.
    for m in range(1,200):
        d=one_layer_cost(m)
        require(d >= 0 and d <= m*m, "one-layer O(m^2) bound")
    require(one_layer_cost(10000) * 10000 < 10000**4, "quadratic-vs-cubic scale sanity")

    print("PASS: BTVA finite support through N<=13; N14 cubic deficit -5/54; fixed-depth O(m^2) cannot change cubic sign")
    for N in range(10,15):
        print(f"f({N})={vals[N]:.12f}")


if __name__ == "__main__":
    main()
