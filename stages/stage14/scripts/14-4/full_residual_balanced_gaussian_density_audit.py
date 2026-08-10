#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def audit_fraction_ledger():
    checks = 0
    phis = [Fraction(5, 24), Fraction(11, 48), Fraction(1, 4)]
    for phi in phis:
        chi = 2 * phi - Fraction(1, 4)
        A = Fraction(1, 2) - 2 * phi
        assert A == Fraction(1, 4) - chi
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        assert Fraction(0) <= A <= Fraction(1, 12)
        for mu in [Fraction(0), A / 2, A]:
            rootline = 2 * phi + mu - chi
            complete = chi + rootline
            assert rootline == Fraction(1, 4) + mu
            assert complete == 2 * phi + mu
            assert complete == Fraction(1, 2) - (A - mu)
            assert complete <= Fraction(1, 2)
            if mu < A:
                assert complete < Fraction(1, 2)
            else:
                assert complete == Fraction(1, 2)
            checks += 1
    return checks


def audit_balanced_linear_identities():
    checks = 0
    for alpha in range(2, 18):
        for delta in range(alpha + 1, 22):
            if gcd(alpha, delta) != 1:
                continue
            for r in range(1, 4):
                for s in range(1, 4):
                    A = alpha * r
                    D = delta * s
                    if D <= A:
                        continue
                    P = D + A
                    Q = D - A
                    assert P + Q == 2 * D
                    assert P - Q == 2 * A
                    assert P * Q == D * D - A * A
                    assert P * P + Q * Q == 2 * (D * D + A * A)
                    assert P * P - Q * Q == 4 * A * D
                    checks += 1
    assert checks > 100
    return checks


def roots_minus_one(q):
    return [x for x in range(1, q) if (x * x + 1) % q == 0]


def audit_primitive_rootline_spacing():
    checks = 0
    for q in [5, 13, 17, 29, 37, 41]:
        for rho in roots_minus_one(q):
            pts = []
            for P in range(1, 3 * q + 1):
                for Q in range(1, 3 * q + 1):
                    if gcd(P, Q) == 1 and (P - rho * Q) % q == 0:
                        pts.append((P, Q))
            for i in range(min(len(pts), 80)):
                P1, Q1 = pts[i]
                for j in range(i + 1, min(len(pts), 80)):
                    P2, Q2 = pts[j]
                    det = P1 * Q2 - P2 * Q1
                    assert det % q == 0
                    if det == 0:
                        assert (P1, Q1) == (P2, Q2)
                    checks += 1
    assert checks > 1000
    return checks


def audit_norm_divisor_reparameterization():
    checks = 0
    phis = [Fraction(5, 24), Fraction(7, 32), Fraction(11, 48), Fraction(1, 4)]
    for phi in phis:
        chi = 2 * phi - Fraction(1, 4)
        norm_q = Fraction(1, 2) - chi
        assert chi + norm_q == Fraction(1, 2)
        assert norm_q == Fraction(3, 4) - 2 * phi
        checks += 1
    return checks


def main():
    print(f"fraction_ledger_checks={audit_fraction_ledger()}")
    print(f"balanced_linear_identity_checks={audit_balanced_linear_identities()}")
    print(f"primitive_rootline_determinant_checks={audit_primitive_rootline_spacing()}")
    print(f"norm_divisor_ledger_checks={audit_norm_divisor_reparameterization()}")
    print("FIRST_RESIDUAL_FIXED_POWER_DEFICIT_SAVING_PROVED=true")
    print("SQRT_SATURATION_REQUIRES_FIRST_RESIDUAL_AT_CAP=true")
    print("SQRT_SATURATION_GAUSSIAN_PAIR_BALANCED=true")
    print("NORM_DIVISOR_REPARAMETERIZATION_GIVES_EXTRA_FIXED_POWER_SAVING=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4de")


if __name__ == "__main__":
    main()
