#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

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

D_MINUS = {1, -1, 3, -3}
D_PLUS = {1, -1, 13, -13, 19, -19, 247, -247}
D_ZERO = {
    1, -1, 3, -3, 13, -13, 19, -19,
    39, -39, 57, -57, 247, -247, 741, -741,
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
            return False
    return True


def H(a, b):
    return a**4 - 20*a*a*b*b + 256*a*b**3 - 412*b**4


def primitive_h_mod32_values():
    vals = set()
    for a in range(32):
        for b in range(32):
            if gcd(gcd(a, b), 32) != 1:
                continue
            vals.add(H(a, b) % 32)
    return vals


def q2_allowed_delta_residues_mod32():
    hvals = primitive_h_mod32_values()
    sq = {x*x % 32 for x in range(32)}
    allowed = set()
    for d in range(1, 32, 2):
        if hvals & {d*s % 32 for s in sq}:
            allowed.add(d)
    return allowed


def q2_filter(classes):
    return {d for d in classes if d % 8 == 1}


def main():
    assert -48*BASE_A == -368064
    assert -864*BASE_B == -422889984

    coeffs = {}
    for d in TARGETS:
        coeffs[d] = (BASE_A*d*d, BASE_B*d*d*d)

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

    assert rejected[0][4] == 5184
    assert valuation(rejected[0][4].numerator, 2) == 6
    assert rejected[1][4] == 324
    assert valuation(rejected[1][4].numerator, 2) == 2

    # Exact 2-adic residue firewall for T_delta: H(a,b)=delta*V^2.
    # A Q_2 point can be represented by a primitive 2-adic pair (a,b),
    # so reduction modulo 32 must appear below.
    assert primitive_h_mod32_values() == {1, 4, 17}
    assert q2_allowed_delta_residues_mod32() == {1, 9, 17, 25}
    # These are exactly the odd residue classes congruent to 1 mod 8.
    assert all(d % 8 == 1 for d in q2_allowed_delta_residues_mod32())

    assert q2_filter(D_MINUS) == {1}
    assert q2_filter(D_PLUS) == {1, -247}
    assert q2_filter(D_ZERO) == {1, -39, 57, -247}

    original_ten = set(TARGETS)
    assert q2_filter(original_ten) == {-39, 57, -247}
    assert original_ten - q2_filter(original_ten) == {
        13, -13, 39, -57, 247, 741, -741
    }

    # Relevance firewall: for a point lifted from C, A1-8 already has
    # Q(z)=Y^2, so the signed squareclass of Q(z) is delta=+1.
    first_two_cover_relevant_delta = 1
    assert first_two_cover_relevant_delta in D_MINUS
    assert first_two_cover_relevant_delta in D_PLUS
    assert first_two_cover_relevant_delta in D_ZERO

    print("false_same_j_adapters_rejected=5")
    print("primitive_H_mod32_values={1,4,17}")
    print("q2_delta_condition=delta == 1 mod 8")
    print("Gminus_q2_survivors=+1")
    print("Gplus_q2_survivors=+1,-247")
    print("G0_q2_survivors=+1,-39,+57,-247")
    print("first_two_cover_relevant_delta=+1")
    print("A1-11 audit repair verification: PASS")


if __name__ == "__main__":
    main()
