#!/usr/bin/env python3
"""Deterministic audit for Stage14-4dc.

This audit is deliberately elementary.  It validates the exact exponent ledger,
the coefficient-free Gaussian product reparameterization, the divisor-fiber
bookkeeping, and the transverse-resultant no-go used by Stage14-4dc.  Finite
checks are regressions only; they are not substitutes for the requested H
average theorem.
"""

from fractions import Fraction
from itertools import permutations
from json import loads
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4dc/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/gaussian_product_rootline_h_gate_summary.json"


def determinant(matrix):
    n = len(matrix)
    total = 0
    for perm in permutations(range(n)):
        inv = sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])
        term = 1
        for i, j in enumerate(perm):
            term *= matrix[i][j]
        total += -term if inv % 2 else term
    return total


def divisor_count(n):
    x = n
    ans = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            ans *= e + 1
        p += 1 if p == 2 else 2
    if x > 1:
        ans *= 2
    return ans


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = isqrt(n)
    p = 3
    while p <= r:
        if n % p == 0:
            return False
        p += 2
    return True


def roots_minus_one(p):
    return [x for x in range(1, p) if (x * x + 1) % p == 0]


def audit_fraction_ledger():
    # 5/24=55/264 and 1/4=66/264, so this exact grid contains both endpoints.
    checks = 0
    for k in range(55, 67):
        phi = Fraction(k, 264)
        chi = 2 * phi - Fraction(1, 4)
        aphi = Fraction(1, 2) - 2 * phi
        uv_line = 2 * phi - chi
        pq_line = Fraction(1, 2) - chi
        assert Fraction(5, 24) <= phi <= Fraction(1, 4)
        assert Fraction(1, 6) <= chi <= Fraction(1, 4)
        assert Fraction(0) <= aphi <= Fraction(1, 12)
        assert uv_line == Fraction(1, 4)
        assert aphi + uv_line == pq_line
        assert chi + pq_line == Fraction(1, 2)
        checks += 1

    # Endpoint locks.
    phi = Fraction(5, 24)
    chi = 2 * phi - Fraction(1, 4)
    assert chi == Fraction(1, 6)
    assert Fraction(1, 2) - 2 * phi == Fraction(1, 12)
    assert Fraction(1, 2) - chi == Fraction(1, 3)

    phi = Fraction(1, 4)
    chi = 2 * phi - Fraction(1, 4)
    assert chi == Fraction(1, 4)
    assert Fraction(1, 2) - 2 * phi == 0
    assert Fraction(1, 2) - chi == Fraction(1, 4)
    return checks


def audit_resultant_and_local_transversality():
    # Sylvester matrix for f=t^2+1 and g=t^2-1.
    sylvester = [
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, -1, 0],
        [0, 1, 0, -1],
    ]
    res = determinant(sylvester)
    assert abs(res) == 4

    orientation_checks = 0
    prime_checks = 0
    for p in range(5, 150):
        if not is_prime(p) or p % 4 != 1:
            continue
        roots = roots_minus_one(p)
        assert len(roots) == 2
        for rho in roots:
            assert (rho * rho + 1) % p == 0
            for sigma in (1, p - 1):
                assert (sigma * sigma - 1) % p == 0
                # A rational cross determinant or cross sum cannot carry p.
                assert (rho - sigma) % p != 0
                assert (rho + sigma) % p != 0
                # Quadratic cross norms do carry p, but only as a formal
                # consequence of rho^2=-1 and sigma^2=1.
                assert (rho * rho + sigma * sigma) % p == 0
                assert ((rho * sigma) ** 2 + 1) % p == 0
                orientation_checks += 1
        prime_checks += 1
    assert prime_checks > 0
    return res, prime_checks, orientation_checks


def audit_product_split_fibers():
    # Every preimage P=a0*U, Q=b0*V is a pair of divisor choices.  The
    # physical coprimality/range masks can only reduce this ambient fiber.
    checks = 0
    max_fiber = 0
    for P in range(1, 65):
        for Q in range(1, 65):
            fiber = 0
            for a0 in range(1, P + 1):
                if P % a0:
                    continue
                U = P // a0
                for b0 in range(1, Q + 1):
                    if Q % b0:
                        continue
                    V = Q // b0
                    assert a0 * U == P and b0 * V == Q
                    fiber += 1
            expected = divisor_count(P) * divisor_count(Q)
            assert fiber == expected
            max_fiber = max(max_fiber, fiber)
            checks += 1
    return checks, max_fiber


def audit_endpoint_small_primitivity_model():
    # Synthetic exact model for P=(D+A)/g, Q=(D-A)/g.  With gcd(alpha,delta)=1
    # and small r,s, gcd(P,Q) is supported by 2*r*s after removing g.
    checks = 0
    for alpha in range(1, 15):
        for delta in range(alpha + 1, 18):
            if gcd(alpha, delta) != 1:
                continue
            for r in range(1, 5):
                for s in range(1, 5):
                    A = alpha * r
                    D = delta * s
                    if D <= A:
                        continue
                    x = D + A
                    y = D - A
                    g = gcd(x, y)
                    P = x // g
                    Q = y // g
                    assert gcd(P, Q) == 1
                    assert P > 0 and Q > 0
                    checks += 1
    assert checks > 0
    return checks


def audit_boundaries():
    text = RESULT.read_text(encoding="utf-8")
    required = [
        "STAGE14_4DC=COMPLETE_GAUSSIAN_PRODUCT_ROOT_LINE_COMPRESSION_TRANSVERSE_RESULTANT_NOGO_AND_MAINLINE_H_GATE",
        "GAUSSIAN_PRODUCT_ROOT_LINE_EXPONENT=1/2-chi",
        "PRODUCT_PAIR_TO_RESIDUAL_PRIMITIVE_SPLIT_MULTIPLICITY=Bo1",
        "PRODUCT_PAIR_TO_SINGLE_COLUMN_MULTIPLICITY=Bo1",
        "TRANSVERSE_ROOT_POLYNOMIAL_RESULTANT=4",
        "RATIONAL_CROSS_DETERMINANT_COPRIME_TO_FULL_GOOD_CORE=true",
        "GAUSSIAN_CROSS_NORM_SECOND_MODULUS_ALLOWED=false",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2",
        "SQRT_B_UPPER_BOUND_PROVED=true",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
        "MAINLINE_H_NEEDED=true",
        "MAINLINE_BLOCKED_BY_H=true",
        "NEXT=Stage14-4dd_after_H",
    ]
    for token in required:
        assert token in text, token

    summary = loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["current_whole_family_exponent"] == "1/2"
    assert summary["sqrt_upper_bound_proved"] is True
    assert summary["strict_subsqrt_power_saving_proved"] is False
    assert summary["transverse_resultant"]["resultant"] == 4
    assert summary["mainline_h_needed"] is True
    assert summary["mainline_blocked_by_h"] is True
    assert summary["next"] == "Stage14-4dd_after_H"


def main():
    ledger_checks = audit_fraction_ledger()
    resultant, prime_checks, orientation_checks = audit_resultant_and_local_transversality()
    split_checks, max_fiber = audit_product_split_fibers()
    primitive_checks = audit_endpoint_small_primitivity_model()
    audit_boundaries()

    print("STAGE14_4DC_AUDIT=PASS")
    print(f"fraction_ledger_checks={ledger_checks}")
    print(f"transverse_resultant={resultant}")
    print(f"good_prime_checks={prime_checks}")
    print(f"local_orientation_checks={orientation_checks}")
    print(f"product_split_checks={split_checks}")
    print(f"max_small_product_split_fiber={max_fiber}")
    print(f"primitive_product_model_checks={primitive_checks}")
    print("whole_family_exponent=1/2")
    print("strict_subsqrt_power_saving_proved=false")
    print("mainline_h_needed=true")


if __name__ == "__main__":
    main()
