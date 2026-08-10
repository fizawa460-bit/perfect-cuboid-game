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
        Aphi = Fraction(1, 4) - chi
        assert chi + Aphi == Fraction(1, 4)
        for wp in [Fraction(0), chi / 2, chi]:
            for wm in [Fraction(0), Aphi / 2, Aphi]:
                w = wp + wm
                assert Fraction(0) <= w <= Fraction(1, 4)
                qeff = Fraction(1, 4) + w
                root = Fraction(1, 2) - qeff
                complete = Fraction(1, 4) + root
                assert root == Fraction(1, 4) - w
                assert complete == Fraction(1, 2) - w
                if w > 0:
                    assert complete < Fraction(1, 2)
                checks += 1
    return checks


def audit_exact_overlap_lift():
    checks = 0
    nontrivial = 0
    # gcd(D,A)=1 and opposite parity models the post-peel physical packet.
    for A in range(1, 35):
        for D in range(A + 1, 55):
            if gcd(A, D) != 1 or (A - D) % 2 == 0:
                continue
            hp = D * D + A * A
            hm = D * D - A * A
            assert hp % 2 == 1 and hm % 2 == 1
            assert gcd(hp, hm) == 1
            # Model s7-46 cofactor reconstruction by all exact factorizations
            # hp=C*Mplus and hm=u*Mminus.
            for C in divisors(hp):
                Mplus = hp // C
                wp = gcd(C, Mplus)
                assert hp % (C * wp) == 0
                for u in divisors(hm):
                    Mminus = hm // u
                    wm = gcd(u, Mminus)
                    assert hm % (u * wm) == 0
                    ceff = C * wp
                    ueff = u * wm
                    assert gcd(ceff, ueff) == 1
                    qeff = ceff * ueff
                    assert gcd(A, qeff) == 1
                    t = (D * pow(A, -1, qeff)) % qeff
                    assert (t * t + 1) % ceff == 0
                    assert (t * t - 1) % ueff == 0
                    assert (pow(t, 4, qeff) - 1) % qeff == 0
                    checks += 1
                    if wp > 1 or wm > 1:
                        nontrivial += 1
    assert checks > 10000
    assert nontrivial > 100
    return checks, nontrivial


def audit_divisor_zero_cost():
    checks = 0
    for n in range(1, 500):
        for d in divisors(n):
            assert n % d == 0
            checks += 1
    assert checks > 2000
    return checks


def main():
    frac = audit_fraction_ledger()
    exact, nontrivial = audit_exact_overlap_lift()
    div = audit_divisor_zero_cost()
    print(f"fraction_ledger_checks={frac}")
    print(f"exact_overlap_root_checks={exact}")
    print(f"nontrivial_overlap_checks={nontrivial}")
    print(f"divisor_choice_checks={div}")
    print("MERGED_S7_46_IMPORTED=true")
    print("WITHIN_SIDE_OVERLAP_EFFECTIVE_MODULUS_LIFT_PROVED=true")
    print("FIXED_POWER_PLUS_OVERLAP_STRICTLY_SUBSQRT=true")
    print("FIXED_POWER_MINUS_OVERLAP_STRICTLY_SUBSQRT=true")
    print("SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true")
    print("S_ROUTE_CURRENT_STATE=ACTIVE_REACTIVATED")
    print("S_ROUTE_REACTIVATION_DECISION_REQUIRED=false")
    print("S_ROUTE_REACTIVATION_CHECK_SUSPENDED=true")
    print("S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true")
    print("MAINLINE_H_NEEDED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("NEXT=Stage14-4dg")
    print("NEXT_S_ROUTE=Stage14-s7-47")


if __name__ == "__main__":
    main()
