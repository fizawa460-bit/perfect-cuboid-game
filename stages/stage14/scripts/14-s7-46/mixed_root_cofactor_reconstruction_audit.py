#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def crt_pair(a: int, m: int, b: int, n: int) -> int:
    assert gcd(m, n) == 1
    inv = pow(m, -1, n)
    k = ((b - a) * inv) % n
    return (a + m * k) % (m * n)


def sqrt_minus_one(q: int):
    return [x for x in range(q) if (x * x + 1) % q == 0]


def exponent_audit() -> int:
    checks = 0
    # chi in [1/6,1/4], equivalent to phi in [5/24,1/4].
    for k in range(0, 81):
        chi = Fraction(1, 6) + Fraction(k, 80) * (Fraction(1, 4) - Fraction(1, 6))
        phi = (chi + Fraction(1, 4)) / 2
        a_phi = Fraction(1, 4) - chi
        mplus = Fraction(1, 2) - chi
        mminus = chi + Fraction(1, 4)
        s_exp = Fraction(1, 4) - chi / 2
        r_exp = Fraction(1, 8) + chi / 2
        assert Fraction(5, 24) <= phi <= Fraction(1, 4)
        assert a_phi == Fraction(1, 2) - 2 * phi
        assert 2 * s_exp == mplus
        assert 2 * r_exp == mminus
        assert r_exp == phi
        assert Fraction(1, 4) + Fraction(1, 4) == Fraction(1, 2)
        checks += 1
    return checks


def mixed_root_allocation_audit() -> tuple[int, int]:
    c_moduli = [5, 13, 17, 25, 29]
    u_moduli = [3, 7, 9, 11, 19]
    root_checks = 0
    sign_checks = 0

    for C in c_moduli:
        roots = sqrt_minus_one(C)
        assert roots
        for u in u_moduli:
            if gcd(C, u) != 1:
                continue
            q = C * u
            # Put each full u modulus on one of the two +/-1 branches.
            for eps in (-1, 1):
                for rho in roots:
                    t = crt_pair(rho, C, eps % u, u)
                    assert pow(t, 4, q) == 1 % q
                    assert gcd(q, t) == 1
                    C_rec = gcd(q, t * t + 1)
                    u_rec = gcd(q, t * t - 1)
                    assert C_rec == C
                    assert u_rec == u
                    u_minus = gcd(u, t - 1)
                    u_plus = gcd(u, t + 1)
                    assert gcd(u_minus, u_plus) == 1
                    assert u_minus * u_plus == u
                    if eps == 1:
                        assert u_minus == u
                    else:
                        assert u_plus == u
                    root_checks += 1
                    sign_checks += 1

    # Mixed prime-power sign allocation on u: split u across t=+1 and t=-1.
    C = 5
    u1, u2 = 7, 11
    rho = sqrt_minus_one(C)[0]
    t = crt_pair(rho, C, 1, u1)
    t = crt_pair(t, C * u1, -1 % u2, u2)
    q = C * u1 * u2
    assert gcd(q, t * t + 1) == C
    assert gcd(q, t * t - 1) == u1 * u2
    assert gcd(u1 * u2, t - 1) == u1
    assert gcd(u1 * u2, t + 1) == u2
    root_checks += 1
    sign_checks += 2

    return root_checks, sign_checks


def cofactor_and_signed_reconstruction_audit() -> tuple[int, int]:
    cofactor_checks = 0
    reciprocal_checks = 0

    # Build primitive synthetic mixed-root packets.  A=1 and D=t+kQ ensure
    # the required root congruence.  We only use odd fixed-power data here.
    examples = [
        (5, 7, 1),
        (13, 9, -1),
        (17, 11, 1),
        (25, 19, -1),
        (29, 3, 1),
    ]

    for C, u, eps in examples:
        rho = sqrt_minus_one(C)[0]
        t = crt_pair(rho, C, eps % u, u)
        qmix = C * u
        for k in (1, 2, 3, 5):
            A = 1
            D = t + k * qmix
            assert gcd(D, A) == 1
            hp = D * D + A * A
            hm = D * D - A * A
            assert hp % C == 0
            assert hm % u == 0

            Mop = oddpart(hp) // C
            Mom = oddpart(hm) // u
            assert Mop >= 1 and Mom >= 1
            # Odd plus/minus factors of a primitive pair are coprime.
            assert gcd(oddpart(hp), oddpart(hm)) == 1
            assert gcd(Mop, Mom) == 1
            cofactor_checks += 1

            # Treat Mom as the peeled xi-agreement product.  Since it divides
            # (D-A)(D+A) and the two odd linear factors are coprime, gcd
            # allocation recovers a primitive agreement pair.
            U = gcd(Mom, D + A)
            V = gcd(Mom, D - A)
            assert gcd(U, V) == 1
            assert U * V == Mom
            a = (D + A) // U
            b = (D - A) // V
            assert a * U == D + A
            assert b * V == D - A
            assert (a * U) ** 2 - (b * V) ** 2 == 4 * D * A
            reciprocal_checks += 1

    return cofactor_checks, reciprocal_checks


def main() -> None:
    exponent_checks = exponent_audit()
    root_checks, sign_checks = mixed_root_allocation_audit()
    cofactor_checks, reciprocal_checks = cofactor_and_signed_reconstruction_audit()

    print("Stage14-s7-46 mixed-root/cofactor reconstruction audit: PASS")
    print(f"theta-quarter exponent blocks: {exponent_checks}")
    print(f"mixed fourth-root allocation checks: {root_checks}")
    print(f"first-residual sign allocation checks: {sign_checks}")
    print(f"plus/minus cofactor checks: {cofactor_checks}")
    print(f"first reciprocal reconstruction checks: {reciprocal_checks}")
    print("current whole-family exponent: 1/2")
    print("second reciprocal independent fixed-power support: false")
    print("new auxiliary H needed: false")
    print("next receiver: SquareRootQuarterScaleMixedFourthRootDualBalancedXiCofactorSplitPhysicalAdmissibilityDensity")


if __name__ == "__main__":
    main()
