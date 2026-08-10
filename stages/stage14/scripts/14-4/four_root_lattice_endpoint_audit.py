#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4cd/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/four_root_lattice_endpoint_summary.json"
S7_15 = ROOT / "stages/stage14/14-s7-15/result.md"
TH14_LATEST = ROOT / "stages/stage14/14-tH14/LATEST.md"
TH14_R2 = ROOT / "stages/stage14/14-tH14/r2.md"
T52 = ROOT / "stages/stage14/14-t52/result.md"


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def squarefree_kernel(n: int) -> int:
    k = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            k *= p
        p += 1 if p == 2 else 2
    if n > 1:
        k *= n
    return k


def canonical(n: int) -> tuple[int, int]:
    sf = squarefree_kernel(n)
    q = n // sf
    r = math.isqrt(q)
    assert r * r == q
    return sf, r


def legendre(a: int, p: int) -> int:
    a %= p
    assert a != 0 and p % 2 == 1
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def crt_two(a: int, m: int, b: int, n: int) -> int:
    assert math.gcd(m, n) == 1
    if m == 1 and n == 1:
        return 0
    if m == 1:
        return b % n
    if n == 1:
        return a % m
    t = ((b - a) * pow(m, -1, n)) % n
    return (a + m * t) % (m * n)


def check_docs() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    s7 = S7_15.read_text()
    latest = TH14_LATEST.read_text()
    r2 = TH14_R2.read_text()
    t52 = T52.read_text()

    required_result = [
        "STAGE14_4CD=FOUR_ROOT_LATTICE_CONGRUENCE_AND_MAXIMAL_K_ENDPOINT_LOCALIZATION",
        "CRITICAL_LATTICE_SUPPORT_EXPONENT=1/8+(d+kappa)/2",
        "SEVEN_EIGHT_RESIDUAL_REQUIRES_K_EXPONENT=1-o(1)",
        "MAINLINE_H_NEEDED=false",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "NEXT=Stage14-4ce",
    ]
    for token in required_result:
        assert token in result, token

    assert "K_PARITY_NORMALIZED_SPLIT_EXACT=true" in s7
    assert "stages/stage14/14-tH14/r2.md" in latest
    assert "PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false" in latest
    assert "DUAL_QUADRATIC_LARGE_SIEVE_PRODUCT_ROW_ADAPTER_PROVED=true" in r2
    assert "PHYSICAL_WEIGHTED_SQUARECLASS_FIBER_ENERGY_PROVED=false" in r2
    assert "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false" in t52
    assert "TH15_NEEDED=false" in t52

    assert summary["current_physical_upper_bound_exponent"] == "7/8"
    assert summary["critical_lattice_support_exponent"] == "1/8+(d+kappa)/2"
    assert summary["critical_k_endpoint_exponent"] == "1"
    assert summary["critical_twist_parameter_exponent"] == "7/4+o(1)"
    assert summary["mainline_h_needed"] is False
    assert summary["next"] == "Stage14-4ce"


def check_physical_identities(limit: int = 100) -> int:
    checks = 0
    for Q in range(2, limit + 1):
        for P in range(1, Q):
            if math.gcd(P, Q) != 1:
                continue

            a, x = canonical(P)
            b, y = canonical(Q)
            g = math.gcd(Q - P, Q + P)
            assert g in (1, 2)
            A = (Q - P) // g
            C = (Q + P) // g
            assert math.gcd(A, C) == 1
            km, r = canonical(A)
            kp, s = canonical(C)
            k = km * kp
            xi = a * b

            assert squarefree_kernel(Q * Q - P * P) == k
            assert math.gcd(km, kp) == 1
            assert math.gcd(xi, k) == 1
            assert math.gcd(x, y) == 1
            assert math.gcd(r, s) == 1
            assert math.gcd(x * y, r * s) == 1

            cg = 2 // g
            assert kp * s * s - km * r * r == cg * a * x * x
            assert kp * s * s + km * r * r == cg * b * y * y

            mx = x * x
            my = y * y
            M = mx * my
            assert (kp * s * s - km * r * r) % mx == 0
            assert (kp * s * s + km * r * r) % my == 0

            lx = 0 if mx == 1 else (r * r * pow((s * s) % mx, -1, mx)) % mx
            ly = 0 if my == 1 else (-r * r * pow((s * s) % my, -1, my)) % my
            lam = crt_two(lx, mx, ly, my)
            assert (kp - lam * km) % M == 0
            if M > 1:
                assert math.gcd(lam, M) == 1

            for ell in prime_factors(a):
                if ell != 2:
                    assert legendre(k, ell) == 1
            for ell in prime_factors(b):
                if ell != 2:
                    assert legendre(-k, ell) == 1
            for ell in prime_factors(km):
                if ell != 2:
                    assert legendre(xi, ell) == 1
            for ell in prime_factors(kp):
                if ell != 2:
                    assert legendre(-xi, ell) == 1

            # Small direct rectangle regression for the exact lattice law.
            K1 = min(16, max(4, 2 * km))
            K2 = min(16, max(4, 2 * kp))
            count = 0
            for u in range(1, K1 + 1):
                for v in range(1, K2 + 1):
                    if (v - lam * u) % M == 0:
                        count += 1
            rhs = Fraction(K1 * K2, M) + K1
            assert count <= rhs
            checks += 1
    return checks


def check_exponent_ledger() -> int:
    seven_eighths = Fraction(7, 8)
    endpoint = Fraction(1, 8) + (Fraction(1, 2) + 1) / 2
    assert endpoint == seven_eighths
    assert Fraction(3, 4) + 1 == Fraction(7, 4)

    grid_checks = 0
    for di in range(0, 65):
        d = Fraction(di, 128)
        for ki in range(96, 129):
            kappa = Fraction(ki, 128)
            if kappa > d + Fraction(1, 2):
                continue
            e = Fraction(1, 8) + (d + kappa) / 2
            assert e <= seven_eighths

            eminus = Fraction(3, 8) + 3 * d / 2 - kappa / 2
            eplus = Fraction(7, 8) + d / 2 - kappa / 2
            assert eminus <= e
            assert eplus <= e

            delta = Fraction(1, 128)
            if d <= Fraction(1, 2) - delta or kappa <= 1 - delta:
                assert e <= seven_eighths - delta / 2
            grid_checks += 1
    return grid_checks


def main() -> None:
    check_docs()
    physical = check_physical_identities()
    grid = check_exponent_ledger()
    print("STAGE14_4CD_AUDIT=PASS")
    print(f"PHYSICAL_FOUR_ROOT_CHECKS={physical}")
    print(f"EXPONENT_GRID_CHECKS={grid}")
    print("DIFFERENCE_KERNEL_CONGRUENCE_LATTICE_EXACT=true")
    print("CRITICAL_LATTICE_SUPPORT_EXPONENT=1/8+(d+kappa)/2")
    print("SEVEN_EIGHT_RESIDUAL_REQUIRES_K_EXPONENT=1-o(1)")
    print("ENDPOINT_QUADRATIC_RESIDUE_SIGNATURE_EXACT=true")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4ce")


if __name__ == "__main__":
    main()
