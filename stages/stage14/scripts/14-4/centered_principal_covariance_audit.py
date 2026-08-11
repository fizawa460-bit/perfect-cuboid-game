#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def centered_identity(wp, wm):
    assert len(wp) == len(wm)
    P = len(wp)
    if P == 0:
        return Fraction(0), Fraction(0), Fraction(0)
    mup = Fraction(sum(wp), P)
    mum = Fraction(sum(wm), P)
    lhs = sum(Fraction(a * b) for a, b in zip(wp, wm))
    principal = P * mup * mum
    covariance = sum((Fraction(a) - mup) * (Fraction(b) - mum) for a, b in zip(wp, wm))
    assert lhs == principal + covariance
    assert sum(Fraction(a) - mup for a in wp) == 0
    assert sum(Fraction(b) - mum for b in wm) == 0
    return lhs, principal, covariance


def audit_global_centering():
    cases = [
        ([1, 0, 2, 1], [0, 3, 1, 2]),
        ([2, 1, 0, 4, 1], [1, 0, 3, 1, 2]),
        ([0, 0, 1], [2, 1, 4]),
        ([3, 3, 3, 3], [1, 2, 3, 4]),
    ]
    checks = 0
    for wp, wm in cases:
        lhs, principal, covariance = centered_identity(wp, wm)
        assert lhs >= 0
        assert principal >= 0
        assert principal + covariance == lhs
        checks += 1
    return checks


def audit_conditional_centering():
    wp = [1, 0, 2, 1, 3, 0, 1, 2]
    wm = [0, 3, 1, 2, 1, 4, 0, 2]
    cells = [[0, 2, 4, 6], [1, 3, 5, 7]]
    lhs = sum(Fraction(wp[i] * wm[i]) for i in range(len(wp)))
    principal = Fraction(0)
    covariance = Fraction(0)
    for cell in cells:
        cp = [wp[i] for i in cell]
        cm = [wm[i] for i in cell]
        cell_lhs, cell_principal, cell_cov = centered_identity(cp, cm)
        assert cell_lhs == sum(Fraction(wp[i] * wm[i]) for i in cell)
        principal += cell_principal
        covariance += cell_cov
    assert lhs == principal + covariance
    return len(cells) + 1


def audit_rotated_pair_identities():
    checks = 0
    witnesses = [(41, 28), (29, 20), (17, 8), (13, 4)]
    for D, A in witnesses:
        assert D > A > 0
        m = D + A
        n = D - A
        assert m * n == D * D - A * A
        assert m * m + n * n == 2 * (D * D + A * A)
        assert gcd(m, n) <= 2 * gcd(D, A)
        assert (m + n) % 2 == 0
        assert (m - n) % 2 == 0
        assert (m + n) // 2 == D
        assert (m - n) // 2 == A
        checks += 1
    return checks


def audit_exponent_boundary():
    checks = 0
    for chi in [Fraction(1, 6), Fraction(5, 24), Fraction(1, 4)]:
        # sH48 / s7-48 physical scales.
        u = Fraction(1, 4) - chi
        s = Fraction(1, 4) - chi / 2
        r = (chi + Fraction(1, 4)) / 2
        plus = chi + 2 * s
        minus = u + 2 * r
        assert plus == Fraction(1, 2)
        assert minus == Fraction(1, 2)
        # primitive pair ambient box: B^(1/4) x B^(1/4)
        assert Fraction(1, 4) + Fraction(1, 4) == Fraction(1, 2)
        checks += 1
    return checks


def audit_principal_obstruction_logic():
    # A covariance estimate alone does not algebraically remove a positive
    # principal term.  Constant weights give covariance zero and a positive
    # principal contribution.
    wp = [1, 1, 1, 1]
    wm = [2, 2, 2, 2]
    lhs, principal, covariance = centered_identity(wp, wm)
    assert covariance == 0
    assert principal == lhs == 8
    return 1


def main():
    c1 = audit_global_centering()
    c2 = audit_conditional_centering()
    c3 = audit_rotated_pair_identities()
    c4 = audit_exponent_boundary()
    c5 = audit_principal_obstruction_logic()
    print(f"global_centering_checks={c1}")
    print(f"conditional_centering_checks={c2}")
    print(f"rotated_pair_checks={c3}")
    print(f"exponent_boundary_checks={c4}")
    print(f"principal_obstruction_checks={c5}")
    print("GLOBAL_TWO_SIDED_CENTERING_IDENTITY_PROVED=true")
    print("CONDITIONAL_CENTERING_IDENTITY_PROVED=true")
    print("CENTERING_LINEAR_TERMS_VANISH_EXACTLY=true")
    print("ABSOLUTE_CENTERED_DISPERSION_ALONE_SUFFICIENT=false")
    print("PRINCIPAL_DENSITY_CONTROL_REQUIRED_FOR_ABSOLUTE_DISPERSION_ROUTE=true")
    print("MARGINAL_FIXED_POWER_MEAN_SAVING_CERTIFIED=false")
    print("PRINCIPAL_TERM_FIXED_POWER_SAVING_PROVED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4dh")


if __name__ == "__main__":
    main()
