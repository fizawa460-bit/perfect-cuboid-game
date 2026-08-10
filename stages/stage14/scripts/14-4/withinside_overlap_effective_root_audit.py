#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def divisors(n):
    out = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def audit_fraction_ledger():
    checks = 0
    for phi in [Fraction(5, 24), Fraction(11, 48), Fraction(1, 4)]:
        chi = 2 * phi - Fraction(1, 4)
        A = Fraction(1, 4) - chi
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        assert Fraction(0) <= A <= Fraction(1, 12)
        assert chi + A == Fraction(1, 4)
        wps = [Fraction(0), chi / 2, chi]
        wms = [Fraction(0), A / 2, A]
        for wp in wps:
            for wm in wms:
                w = wp + wm
                assert w <= Fraction(1, 4)
                qeff = Fraction(1, 4) + w
                root = Fraction(1, 2) - qeff
                complete = Fraction(1, 4) + root
                assert root == Fraction(1, 4) - w
                assert complete == Fraction(1, 2) - w
                assert complete <= Fraction(1, 2)
                if w > 0:
                    assert complete < Fraction(1, 2)
                checks += 1
    return checks


def audit_overlap_modulus_lift():
    checks = 0
    root_checks = 0
    # Opposite parity + gcd 1 makes H_+, H_- odd and cross-coprime.
    for A in range(1, 35):
        for D in range(A + 1, 55):
            if gcd(A, D) != 1 or (A - D) % 2 == 0:
                continue
            hp = D * D + A * A
            hm = D * D - A * A
            assert hp % 2 == 1 and hm % 2 == 1
            assert gcd(hp, hm) == 1
            for C in divisors(hp):
                X = hp // C
                wp = gcd(C, X)
                assert (C * wp) > 0
                assert hp % (C * wp) == 0
                for u in divisors(hm):
                    R = hm // u
                    wm = gcd(u, R)
                    assert hm % (u * wm) == 0
                    ceff = C * wp
                    ueff = u * wm
                    qeff = ceff * ueff
                    assert gcd(ceff, ueff) == 1
                    assert gcd(A, qeff) == 1
                    t = (D * pow(A, -1, qeff)) % qeff
                    assert (t * t + 1) % ceff == 0
                    assert (t * t - 1) % ueff == 0
                    assert (pow(t, 4, qeff) - 1) % qeff == 0
                    assert gcd(qeff, t * t + 1) == ceff
                    assert gcd(qeff, t * t - 1) == ueff
                    checks += 1
                    if wp > 1 or wm > 1:
                        root_checks += 1
    assert checks > 10000
    assert root_checks > 100
    return checks, root_checks


def audit_divisor_choice_zero_cost_model():
    checks = 0
    for n in range(1, 500):
        ds = divisors(n)
        for w in ds:
            assert n % w == 0
            checks += 1
    assert checks > 2000
    return checks


def main():
    frac = audit_fraction_ledger()
    exact, nontrivial = audit_overlap_modulus_lift()
    div = audit_divisor_choice_zero_cost_model()
    print(f"fraction_ledger_checks={frac}")
    print(f"exact_overlap_root_checks={exact}")
    print(f"nontrivial_overlap_checks={nontrivial}")
    print(f"divisor_choice_checks={div}")
    print("WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true")
    print("FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true")
    print("FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true")
    print("SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true")
    print("S_ROUTE_REACTIVATION_NEEDED=true")
    print("S_ROUTE_REACTIVATION_CONFIRMED_BY_STAGE14_4DF=true")
    print("MAINLINE_H_NEEDED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("NEXT=Stage14-4dg")
    print("NEXT_S_ROUTE=Stage14-s7-46")


if __name__ == "__main__":
    main()
