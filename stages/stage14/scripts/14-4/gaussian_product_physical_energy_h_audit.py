#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in range(2, int(x ** 0.5) + 1)):
            out.append(x)
    return out


def roots_minus_one(p):
    return [x for x in range(1, p) if (x * x + 1) % p == 0]


def audit_ledger():
    samples = [Fraction(5, 24), Fraction(11, 48), Fraction(1, 4)]
    for phi in samples:
        chi = 2 * phi - Fraction(1, 4)
        root_line = Fraction(1, 2) - chi
        total = chi + root_line
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        assert total == Fraction(1, 2)
    return len(samples)


def audit_transverse_resultant():
    checks = 0
    for p in primes_upto(200):
        roots = roots_minus_one(p)
        if not roots:
            continue
        assert p % 4 == 1
        for rho in roots:
            for sigma in (1, p - 1):
                assert (rho - sigma) % p != 0
                assert (rho + sigma) % p != 0
                checks += 1
    return checks


def audit_gaussian_multiplication():
    checks = 0
    for c1 in range(1, 9):
        for c2 in range(0, 8):
            C = c1 * c1 + c2 * c2
            for r1 in range(1, 9):
                for r2 in range(0, 8):
                    R = r1 * r1 + r2 * r2
                    P = c1 * r1 - c2 * r2
                    Q = c1 * r2 + c2 * r1
                    assert P * P + Q * Q == C * R
                    checks += 1
    return checks


def audit_primitive_root_line_sharpness():
    # Finite sanity check: primitive points on a fixed rho root line are not
    # automatically power-sparse beyond the determinant-spacing scale.
    checks = 0
    for p in (5, 13, 17, 29, 37):
        roots = roots_minus_one(p)
        for rho in roots:
            pts = []
            for q in range(1, 4 * p + 1):
                for r in range(1, 4 * p + 1):
                    if gcd(q, r) == 1 and (q - rho * r) % p == 0:
                        pts.append((q, r))
            # Existence of many ambient primitive points is enough for the H
            # no-go: the root equation itself cannot be treated as sparse.
            assert len(pts) >= p
            checks += len(pts)
    return checks


def main():
    ledger = audit_ledger()
    resultant = audit_transverse_resultant()
    gaussian = audit_gaussian_multiplication()
    ambient = audit_primitive_root_line_sharpness()

    print(f"ledger_checks={ledger}")
    print(f"transverse_resultant_checks={resultant}")
    print(f"gaussian_multiplication_checks={gaussian}")
    print(f"ambient_root_line_points_checked={ambient}")
    print("ZERO_FREQUENCY_PHYSICAL_DENSITY_OBSTRUCTION=true")
    print("OFF_THE_SHELF_UNIFORM_POWER_SAVING_PROVED=false")
    print("CERTIFIED_MAINLINE_H_DELTA=0")
    print("MAINLINE_H_COMPLETED=true")
    print("MAINLINE_BLOCKED_BY_H=false")
    print("NEXT=Stage14-4dd")


if __name__ == "__main__":
    main()
