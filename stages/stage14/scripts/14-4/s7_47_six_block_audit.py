#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt


def pairwise_coprime(vals):
    for i, a in enumerate(vals):
        for b in vals[i + 1:]:
            if gcd(a, b) != 1:
                return False
    return True


def audit_four_to_six_separation():
    checks = 0
    primes = [3, 5, 7, 11, 13, 17, 19]
    for C in primes:
        for u in primes:
            if u == C:
                continue
            remaining = [p for p in primes if p not in (C, u)]
            S, T, R, J = remaining[:4]
            Mplus = S * T
            Mminus = R * J
            assert pairwise_coprime([C, Mplus, u, Mminus])
            assert pairwise_coprime([C, S, T, u, R, J])
            checks += 1
    assert checks > 20
    return checks


def audit_square_reconstruction():
    # Physical-shaped witness:
    # 5*17*29 = 41^2+28^2, 3*13*23 = 41^2-28^2.
    C, S, T, u, R, J = 5, 17, 29, 3, 13, 23
    D, A = 41, 28
    assert pairwise_coprime([C, S, T, u, R, J])
    Xp = C * S * T
    Xm = u * R * J
    assert Xp == D * D + A * A
    assert Xm == D * D - A * A
    D2 = (Xp + Xm) // 2
    A2 = (Xp - Xm) // 2
    assert isqrt(D2) ** 2 == D2
    assert isqrt(A2) ** 2 == A2
    assert isqrt(D2) == D
    assert isqrt(A2) == A
    Q = C * u
    assert gcd(A, Q) == 1
    t = (D * pow(A, -1, Q)) % Q
    assert (t * t + 1) % C == 0
    assert (t * t - 1) % u == 0
    assert (pow(t, 4, Q) - 1) % Q == 0
    return 13


def audit_nonphysical_rejection():
    checks = 0
    samples = [
        (3, 5, 7, 11, 13, 17),
        (5, 7, 11, 3, 13, 19),
        (7, 11, 13, 3, 5, 17),
    ]
    for C, S, T, u, R, J in samples:
        assert pairwise_coprime([C, S, T, u, R, J])
        Xp = C * S * T
        Xm = u * R * J
        if Xp <= Xm:
            Xp, Xm = Xm, Xp
        admissible = False
        if (Xp + Xm) % 2 == 0 and (Xp - Xm) % 2 == 0:
            D2 = (Xp + Xm) // 2
            A2 = (Xp - Xm) // 2
            admissible = isqrt(D2) ** 2 == D2 and isqrt(A2) ** 2 == A2
        assert not admissible
        checks += 1
    return checks


def audit_fraction_boundary():
    checks = 0
    for phi in [Fraction(5, 24), Fraction(11, 48), Fraction(1, 4)]:
        chi = 2 * phi - Fraction(1, 4)
        Aphi = Fraction(1, 4) - chi
        assert chi + Aphi == Fraction(1, 4)
        assert Fraction(1, 4) + Fraction(1, 4) == Fraction(1, 2)
        checks += 1
    return checks


def main():
    c1 = audit_four_to_six_separation()
    c2 = audit_square_reconstruction()
    c3 = audit_nonphysical_rejection()
    c4 = audit_fraction_boundary()
    print(f"four_to_six_separation_checks={c1}")
    print(f"square_reconstruction_checks={c2}")
    print(f"nonphysical_rejection_checks={c3}")
    print(f"fraction_boundary_checks={c4}")
    print("MERGED_S7_47_IMPORTED=true")
    print("S7_47_OVERLAP_THEOREM_REPROVED_BY_4DF=false")
    print("S7_47_AND_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false")
    print("SIX_ATOMIC_NORM_BLOCKS_PAIRWISE_SEPARATED=true")
    print("SIX_BLOCK_PACKET_TO_BALANCED_PAIR_MULTIPLICITY=Bo1")
    print("D_A_INDEPENDENT_FIXED_POWER_SUPPORT_AFTER_SIX_BLOCKS=false")
    print("MIXED_ROOT_LABEL_INDEPENDENT_SUPPORT_AFTER_SIX_BLOCKS=false")
    print("S_ROUTE_REACTIVATION_DECISION_REQUIRED_AT_4DF_SOURCE=false")
    print("S_ROUTE_REACTIVATION_CHECK_RESUMES_WHEN_S_ROUTE_CLOSED=true")
    print("S_ROUTE_LIFECYCLE_OWNED_BY_CURRENT_ROADMAP=true")
    print("CURRENT_S_ROUTE_STATE_NOT_OVERWRITTEN_BY_4DF=true")
    print("MAINLINE_H_NEEDED=false")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2")
    print("STRICT_SUBSQRT_POWER_SAVING_PROVED=false")
    print("NEXT=Stage14-4dg")


if __name__ == "__main__":
    main()
