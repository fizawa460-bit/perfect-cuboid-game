#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations
from json import loads
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4dc/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/gaussian_product_rootline_h_gate_summary.json"


def det(a):
    n = len(a)
    total = 0
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = 1
        for i, j in enumerate(p):
            term *= a[i][j]
        total += -term if inv % 2 else term
    return total


def tau(n):
    x, ans, p = n, 1, 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            ans *= e + 1
        p += 1 if p == 2 else 2
    return ans * (2 if x > 1 else 1)


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for p in range(3, isqrt(n) + 1, 2):
        if n % p == 0:
            return False
    return True


def ledger_audit():
    checks = 0
    for k in range(55, 67):  # [5/24,1/4] on denominator 264
        phi = Fraction(k, 264)
        chi = 2 * phi - Fraction(1, 4)
        A = Fraction(1, 2) - 2 * phi
        uv = 2 * phi - chi
        pq = Fraction(1, 2) - chi
        assert Fraction(5, 24) <= phi <= Fraction(1, 4)
        assert uv == Fraction(1, 4)
        assert A + uv == pq
        assert chi + pq == Fraction(1, 2)
        checks += 1
    assert (2 * Fraction(5, 24) - Fraction(1, 4)) == Fraction(1, 6)
    assert Fraction(1, 2) - (2 * Fraction(5, 24) - Fraction(1, 4)) == Fraction(1, 3)
    assert Fraction(1, 2) - (2 * Fraction(1, 4) - Fraction(1, 4)) == Fraction(1, 4)
    return checks


def resultant_audit():
    syl = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1]]
    result = abs(det(syl))
    assert result == 4
    primes = orientations = 0
    for p in range(5, 150):
        if not prime(p) or p % 4 != 1:
            continue
        roots = [r for r in range(1, p) if (r * r + 1) % p == 0]
        assert len(roots) == 2
        for rho in roots:
            for sigma in (1, p - 1):
                assert (rho - sigma) % p
                assert (rho + sigma) % p
                assert (rho * rho + sigma * sigma) % p == 0
                assert ((rho * sigma) ** 2 + 1) % p == 0
                orientations += 1
        primes += 1
    assert primes > 0
    return result, primes, orientations


def split_audit():
    checks = max_fiber = 0
    for P in range(1, 49):
        for Q in range(1, 49):
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
            assert fiber == tau(P) * tau(Q)
            max_fiber = max(max_fiber, fiber)
            checks += 1
    return checks, max_fiber


def primitive_model_audit():
    checks = 0
    for alpha in range(1, 12):
        for delta in range(alpha + 1, 15):
            if gcd(alpha, delta) != 1:
                continue
            for r in range(1, 4):
                for s in range(1, 4):
                    A, D = alpha * r, delta * s
                    if D <= A:
                        continue
                    g = gcd(D + A, D - A)
                    P, Q = (D + A) // g, (D - A) // g
                    assert gcd(P, Q) == 1
                    checks += 1
    assert checks
    return checks


def boundary_audit():
    text = RESULT.read_text(encoding="utf-8")
    tokens = [
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
    for token in tokens:
        assert token in text, token
    data = loads(SUMMARY.read_text(encoding="utf-8"))
    assert data["current_whole_family_exponent"] == "1/2"
    assert data["resultant_no_go"]["resultant"] == 4
    assert data["mainline_h_needed"] is True
    assert data["mainline_blocked_by_h"] is True


def main():
    ledger = ledger_audit()
    resultant, primes, orientations = resultant_audit()
    splits, max_fiber = split_audit()
    primitive = primitive_model_audit()
    boundary_audit()
    print("STAGE14_4DC_AUDIT=PASS")
    print(f"fraction_ledger_checks={ledger}")
    print(f"transverse_resultant={resultant}")
    print(f"good_prime_checks={primes}")
    print(f"local_orientation_checks={orientations}")
    print(f"product_split_checks={splits}")
    print(f"max_small_product_split_fiber={max_fiber}")
    print(f"primitive_product_model_checks={primitive}")
    print("whole_family_exponent=1/2")
    print("mainline_h_needed=true")


if __name__ == "__main__":
    main()
