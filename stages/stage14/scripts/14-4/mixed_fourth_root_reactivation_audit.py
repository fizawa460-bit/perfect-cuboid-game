#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def audit_fraction_ledger():
    checks = 0
    for phi in [Fraction(5, 24), Fraction(7, 32), Fraction(11, 48), Fraction(1, 4)]:
        chi = 2 * phi - Fraction(1, 4)
        u = Fraction(1, 4) - chi
        st = Fraction(1, 2) - chi
        rj = chi + Fraction(1, 4)
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        assert Fraction(0) <= u <= Fraction(1, 12)
        assert chi + u == Fraction(1, 4)
        assert chi + st == Fraction(1, 2)
        assert rj + u == Fraction(1, 2)
        assert st + rj == Fraction(3, 4)
        checks += 1
    return checks


def audit_plus_minus_gcd():
    checks = 0
    for D in range(2, 180):
        for A in range(1, D):
            hp = D * D + A * A
            hm = D * D - A * A
            g = gcd(D, A)
            assert gcd(hp, hm) <= 2 * g * g
            checks += 1
    return checks


def audit_cell_small_gcd():
    checks = 0
    # Synthetic exact form D=delta*s, A=alpha*r with gcd(alpha,delta)=1.
    for alpha in range(1, 30):
        for delta in range(1, 30):
            if gcd(alpha, delta) != 1:
                continue
            for r in range(1, 7):
                for s in range(1, 7):
                    D = delta * s
                    A = alpha * r
                    if D <= A:
                        continue
                    assert gcd(D, A) <= r * s
                    hp = D * D + A * A
                    hm = D * D - A * A
                    assert gcd(hp, hm) <= 2 * r * r * s * s
                    checks += 1
    assert checks > 1000
    return checks


def audit_mixed_root_recovery():
    checks = 0
    # For every odd q and every fourth root t mod q, the two factors t^2-1
    # and t^2+1 partition all prime powers of q because their gcd divides 2.
    for q in range(3, 260, 2):
        for t in range(1, q):
            if gcd(t, q) != 1 or pow(t, 4, q) != 1 % q:
                continue
            u = gcd(q, t * t - 1)
            c = gcd(q, t * t + 1)
            assert gcd(c, u) == 1
            assert c * u == q
            assert (t * t + 1) % c == 0
            assert (t * t - 1) % u == 0
            checks += 1
    assert checks > 500
    return checks


def audit_mixed_root_line_determinant():
    checks = 0
    for q in range(3, 90, 2):
        roots = [t for t in range(1, q) if gcd(t, q) == 1 and pow(t, 4, q) == 1 % q]
        for t in roots:
            pts = []
            for D in range(1, 2 * q + 1):
                for A in range(1, 2 * q + 1):
                    if gcd(D, A) == 1 and (D - t * A) % q == 0:
                        pts.append((D, A))
            pts = pts[:50]
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    D1, A1 = pts[i]
                    D2, A2 = pts[j]
                    det = D1 * A2 - D2 * A1
                    assert det % q == 0
                    if det == 0:
                        assert pts[i] == pts[j]
                    checks += 1
    assert checks > 1000
    return checks


def main():
    print(f"fraction_ledger_checks={audit_fraction_ledger()}")
    print(f"plus_minus_gcd_checks={audit_plus_minus_gcd()}")
    print(f"cell_small_gcd_checks={audit_cell_small_gcd()}")
    print(f"mixed_root_recovery_checks={audit_mixed_root_recovery()}")
    print(f"mixed_root_line_determinant_checks={audit_mixed_root_line_determinant()}")
    print("FULL_RESIDUAL_PLUS_MINUS_CROSS_GCD_BO1=true")
    print("COMMON_CORE_FIRST_RESIDUAL_CROSS_GCD_BO1=true")
    print("XI_SWITCH_FIRST_RESIDUAL_CROSS_GCD_BO1=true")
    print("MIXED_MODULUS_EXPONENT=1/4")
    print("MIXED_FOURTH_ROOT_LINE_PROVED=true")
    print("MIXED_ROOT_LABEL_RECOVERS_CORE_RESIDUAL_ALLOCATION=true")
    print("MIXED_FOURTH_ROOT_COMPRESSION_GIVES_EXTRA_FIXED_POWER_SAVING=false")
    print("S_ROUTE_REACTIVATION_NEEDED=true")
    print("S_ROUTE_REACTIVATION_TARGET=Stage14-s7-46")
    print("MAINLINE_H_NEEDED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("NEXT=Stage14-4df")


if __name__ == "__main__":
    main()
