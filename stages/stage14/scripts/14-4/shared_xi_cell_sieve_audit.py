#!/usr/bin/env python3
"""Deterministic audit for Stage14-4bw.

This audit checks the exact algebraic pieces of the four-cell switch and the
18/19 exponent ledger.  The analytic input used by the stage is the standard
Weil bound for a fixed-degree nonsquare polynomial over F_p; the audit checks
that the one-cell quartics are nondegenerate on representative physical-open
packets and verifies finite-prime character sums against the degree-4 Weil
scale.
"""

from fractions import Fraction
from math import gcd, isqrt, sqrt


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p = 3 if p == 2 else p + 2
    return True


def pairwise_coprime(vals):
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if gcd(vals[i], vals[j]) != 1:
                return False
    return True


def cell_coefficients(alpha, beta, gamma, delta):
    a = alpha * beta
    b = gamma * delta
    c = alpha * gamma
    d = beta * delta
    return a, b, c, d


def audit_four_cell_identity():
    samples = [
        (1, 2, 3, 5),
        (2, 3, 5, 7),
        (3, 5, 7, 11),
        (5, 7, 11, 13),
    ]
    for cells in samples:
        assert pairwise_coprime(cells)
        assert all(is_squarefree(v) for v in cells)
        alpha, beta, gamma, delta = cells
        a, b, c, d = cell_coefficients(*cells)
        xi = alpha * beta * gamma * delta
        assert a * b == xi
        assert c * d == xi
        assert gcd(a, b) == 1
        assert gcd(c, d) == 1
        assert gcd(a, c) == alpha
        assert gcd(a, d) == beta
        assert gcd(b, c) == gamma
        assert gcd(b, d) == delta


def physical_coords(cells, sq):
    alpha, beta, gamma, delta = cells
    x, y, z, w = sq
    a, b, c, d = cell_coefficients(*cells)
    # Return numerator/denominator pairs rather than floats.
    P, Q = a * x * x, b * y * y
    R, S = c * z * z, d * w * w
    return P, Q, R, S


def find_open_samples():
    cell_samples = [
        (1, 2, 3, 5),
        (2, 3, 5, 7),
        (3, 5, 7, 11),
        (5, 7, 11, 13),
    ]
    out = []
    for cells in cell_samples:
        for x in range(1, 6):
            for y in range(2, 9):
                for z in range(1, 6):
                    for w in range(2, 9):
                        P, Q, R, S = physical_coords(cells, (x, y, z, w))
                        if P * S > R * Q and P < Q and R < S:
                            # 0 < v=R/S < u=P/Q < 1.
                            out.append((cells, (x, y, z, w), (P, Q, R, S)))
                            break
                    if out and out[-1][0] == cells:
                        break
                if out and out[-1][0] == cells:
                    break
            if out and out[-1][0] == cells:
                break
    assert len(out) >= 3
    return out


def degeneracy_differences(cells, sq):
    alpha, beta, gamma, delta = cells
    x, y, z, w = sq

    # For alpha/delta the square-polynomial degeneration is v/u=1.
    ratio_diff = (gamma * y * z) ** 4 - (beta * x * w) ** 4

    # For beta/gamma the square-polynomial degeneration is u*v=1.
    product_diff = (delta * y * w) ** 4 - (alpha * x * z) ** 4
    return ratio_diff, product_diff


def quartic_coefficients_for_alpha(cells, sq):
    alpha, beta, gamma, delta = cells
    x, y, z, w = sq
    A = (gamma * delta) ** 2 * y ** 4
    B = beta ** 2 * x ** 4
    C = (beta * delta) ** 2 * w ** 4
    D = gamma ** 2 * z ** 4
    # H(t)=(A-B t^2)(C-D t^2)
    return A, B, C, D


def audit_open_nondegeneracy():
    rows = find_open_samples()
    for cells, sq, (P, Q, R, S) in rows:
        assert 0 < R * Q < P * S
        assert P < Q and R < S
        ratio_diff, product_diff = degeneracy_differences(cells, sq)
        assert ratio_diff != 0
        assert product_diff != 0

        A, B, C, D = quartic_coefficients_for_alpha(cells, sq)
        assert A * D != B * C

        # Verify the exact alpha degeneracy identity.
        gamma = cells[2]
        beta = cells[1]
        x, y, z, w = sq
        lhs = A * D - B * C
        rhs = (cells[3] ** 2) * (
            (gamma * y * z) ** 4 - (beta * x * w) ** 4
        )
        assert lhs == rhs
    return rows


def audit_finite_weil_scale(rows):
    # For representative good primes, verify the untwisted complete
    # character sum is on the degree-4 square-root scale.  The theorem in
    # result.md uses the standard Weil bound uniformly, including additive
    # twists; this finite audit is a deterministic regression only.
    primes = [7, 11, 19, 23, 31, 43, 47]
    checked = 0
    for cells, sq, _ in rows:
        A, B, C, D = quartic_coefficients_for_alpha(cells, sq)
        disc_factor = 2 * A * B * C * D * (A * D - B * C)
        for p in primes:
            if disc_factor % p == 0:
                continue
            total = 0
            for t in range(p):
                h = (A - B * t * t) * (C - D * t * t)
                total += legendre(h, p)
            # Classical degree-4 Weil bound: <=3 sqrt(p) for the untwisted
            # squarefree quartic. Add one integer of slack for float rounding.
            assert abs(total) <= 3 * sqrt(p) + 1
            checked += 1
    assert checked >= 8
    return checked


def audit_exponent_ledger():
    theta = Fraction(9, 19)
    nu = Fraction(8, 19)
    tau = Fraction(2, 19)
    target = Fraction(18, 19)

    e_den = 2 * theta
    e_num = 1 + nu - theta
    e_thick = 1 - tau / 2
    e_numcell = 1 - (nu - 2 * tau) / 4
    e_dencell = 1 - (theta - 2 * tau) / 4

    assert e_den == target
    assert e_num == target
    assert e_thick == target
    assert e_numcell == target
    assert e_dencell == Fraction(71, 76)
    assert e_dencell < target

    old = Fraction(20, 21)
    post_local = Fraction(41, 42)
    assert old - target == Fraction(2, 399)
    assert post_local - target == Fraction(23, 798)
    assert target - Fraction(1, 2) == Fraction(17, 38)

    # Exact lower-bound proof for the minimax architecture.
    # If all four active branches were <=E, then
    # theta <= E/2,
    # nu <= E-1+theta <= 3E/2-1,
    # tau >= 2(1-E),
    # nu >= 2tau+4(1-E) >= 8(1-E).
    # Hence 8(1-E) <= 3E/2-1, i.e. E>=18/19.
    E = target
    assert 8 * (1 - E) == Fraction(8, 19)
    assert Fraction(3, 2) * E - 1 == Fraction(8, 19)
    return {
        "theta": theta,
        "nu": nu,
        "tau": tau,
        "target": target,
        "e_dencell": e_dencell,
    }


def main():
    audit_four_cell_identity()
    rows = audit_open_nondegeneracy()
    checked = audit_finite_weil_scale(rows)
    led = audit_exponent_ledger()

    print(f"OPEN_PACKET_SAMPLE_COUNT={len(rows)}")
    print(f"FINITE_GOOD_PRIME_WEIL_CHECKS={checked}")
    print(f"OPTIMAL_DENOMINATOR_CUTOFF={led['theta']}")
    print(f"OPTIMAL_NUMERATOR_CUTOFF={led['nu']}")
    print(f"OPTIMAL_SQUAREPART_THRESHOLD={led['tau']}")
    print(f"NEW_WHOLE_FAMILY_EXPONENT={led['target']}")
    print(f"DENOMINATOR_THIN_CELL_EXPONENT={led['e_dencell']}")
    print("SHARED_XI_FOUR_CELL_DECOMPOSITION_AUDIT=true")
    print("CELL_QUARTIC_PHYSICAL_NONDEGENERACY_AUDIT=true")
    print("ONE_CELL_WEIL_SCALE_FINITE_AUDIT=true")
    print("EXACT_18_19_MINIMAX_LEDGER_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
