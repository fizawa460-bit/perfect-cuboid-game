#!/usr/bin/env python3
from fractions import Fraction

BASE_A = 7668
BASE_B = 489456
TARGETS = [13, -13, 39, -39, 57, -57, 247, -247, 741, -741]

CANDIDATES = {
    "32110.x1": ([1, 1, 1, 250, 2985], 13),
    "256880.cx1": ([0, 1, 0, 4000, -183052], -13),
    "32490.s1": ([1, -1, 0, 4806, 241650], 57),
    "259920.fm1": ([0, 0, 0, 76893, -15542494], -57),
    "288990.bg1": ([1, -1, 0, 2250, -78350], -39),
}


def invariants(a):
    a1, a2, a3, a4, a6 = a
    b2 = a1*a1 + 4*a2
    b4 = 2*a4 + a1*a3
    b6 = a3*a3 + 4*a6
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    return c4, c6


def valuation(n, p):
    n = abs(n)
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def rational_fourth_power(q):
    q = Fraction(q)
    if q <= 0:
        return False
    for n in (q.numerator, q.denominator):
        m = n
        p = 2
        while p*p <= m:
            if m % p == 0:
                v = 0
                while m % p == 0:
                    m //= p
                    v += 1
                if v % 4:
                    return False
            p += 1
        if m > 1:
            return False  # remaining prime has exponent 1
    return True


def main():
    assert -48*BASE_A == -368064
    assert -864*BASE_B == -422889984

    coeffs = {}
    for d in TARGETS:
        A = BASE_A*d*d
        B = BASE_B*d*d*d
        coeffs[d] = (A, B)

    assert coeffs[13] == (1295892, 1075334832)
    assert coeffs[-13] == (1295892, -1075334832)
    assert coeffs[39] == (11663028, 29034040464)
    assert coeffs[-39] == (11663028, -29034040464)
    assert coeffs[57] == (24913332, 90643825008)
    assert coeffs[-57] == (24913332, -90643825008)
    assert coeffs[247] == (467817012, 7375721612688)
    assert coeffs[-247] == (467817012, -7375721612688)
    assert coeffs[741] == (4210353108, 199144483542576)
    assert coeffs[-741] == (4210353108, -199144483542576)

    rejected = []
    for label, (ainvs, d) in CANDIDATES.items():
        c4, c6 = invariants(ainvs)
        target_c4 = -368064*d*d
        target_c6 = -422889984*d*d*d
        r4 = Fraction(target_c4, c4)
        r6 = Fraction(target_c6, c6)
        assert not rational_fourth_power(r4)
        rejected.append((label, d, c4, c6, r4, r6))

    # Two explicit valuation witnesses used in result.md.
    r_32110 = rejected[0][4]
    r_256880 = rejected[1][4]
    assert r_32110 == 5184 and valuation(r_32110.numerator, 2) == 6
    assert r_256880 == 324 and valuation(r_256880.numerator, 2) == 2

    print("target_twists=10")
    print("false_same_j_adapters_rejected=5")
    for row in rejected:
        print(row[0], "delta=", row[1], "c4_ratio=", row[4], "c6_ratio=", row[5])
    print("A1-11 exact adapter firewall: PASS")


if __name__ == "__main__":
    main()
