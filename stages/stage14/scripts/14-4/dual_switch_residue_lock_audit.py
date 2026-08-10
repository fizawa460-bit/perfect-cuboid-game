#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4ce/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/dual_switch_residue_lock_summary.json"
FOUR_CD = ROOT / "stages/stage14/14-4cd/result.md"
S7_18 = ROOT / "stages/stage14/14-s7-18/result.md"


def squarefree_kernel(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def canonical(n: int) -> tuple[int, int]:
    sf = squarefree_kernel(n)
    q = n // sf
    r = math.isqrt(q)
    assert r * r == q
    return sf, r


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


def legendre(a: int, p: int) -> int:
    a %= p
    assert p % 2 == 1 and a != 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def four_cells(split1: tuple[int, int], split2: tuple[int, int]) -> tuple[int, int, int, int]:
    a, b = split1
    c, d = split2
    A = math.gcd(a, c)
    B = math.gcd(a, d)
    C = math.gcd(b, c)
    D = math.gcd(b, d)
    assert a == A * B
    assert b == C * D
    assert c == A * C
    assert d == B * D
    vals = (A, B, C, D)
    for i in range(4):
        for j in range(i + 1, 4):
            assert math.gcd(vals[i], vals[j]) == 1
    return vals


def check_docs() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    four_cd = FOUR_CD.read_text()
    s7 = S7_18.read_text()

    required = [
        "STAGE14_4CE=COMPLETE_DUAL_SPLIT_SWITCH_RIGIDITY_AND_PRIMEWISE_RESIDUE_LOCK",
        "CROSS_XI_SPLIT_AGREEMENT_NECESSARY_BOUND=(Xi_agree)^2*k<=2*X^4",
        "FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4",
        "FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8",
        "ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true",
        "ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "MAINLINE_H_NEEDED=false",
        "NEXT=Stage14-4cf",
    ]
    for token in required:
        assert token in result, token

    assert "ENDPOINT_QUADRATIC_RESIDUE_SIGNATURE_EXACT=true" in four_cd
    assert "FOUR_CD_ENDPOINT_SWITCH_PRODUCT_LOWER_EXPONENT=3/8" in s7
    assert "FIXED_SPLIT_CRITICAL_COLLISIONS_EXIST=false" in s7

    assert summary["endpoint_xi_switch_lower_exponent"] == "1/4"
    assert summary["endpoint_k_switch_lower_exponent"] == "3/8"
    assert summary["mainline_h_needed"] is False
    assert summary["current_physical_upper_bound_exponent"] == "7/8"
    assert summary["next"] == "Stage14-4cf"


def build_states(limit: int = 180) -> list[dict[str, int]]:
    states: list[dict[str, int]] = []
    for Q in range(2, limit + 1):
        for P in range(1, Q):
            if math.gcd(P, Q) != 1:
                continue
            a, x = canonical(P)
            b, y = canonical(Q)
            xi = a * b
            assert xi == squarefree_kernel(P * Q)

            g = math.gcd(Q - P, Q + P)
            assert g in (1, 2)
            km, r = canonical((Q - P) // g)
            kp, s = canonical((Q + P) // g)
            k = km * kp
            assert k == squarefree_kernel(Q * Q - P * P)
            assert math.gcd(xi, k) == 1

            diff = Q * Q - P * P
            h2 = diff // k
            h = math.isqrt(h2)
            assert h * h == h2

            # 4cd odd-prime signature.
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

            states.append({
                "P": P, "Q": Q,
                "a": a, "b": b, "x": x, "y": y,
                "xi": xi, "k": k, "h": h,
                "km": km, "kp": kp, "r": r, "s": s, "g": g,
            })
    return states


def check_collision_pairs(states: list[dict[str, int]]) -> tuple[int, int, int]:
    fibers: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for st in states:
        fibers[(st["xi"], st["k"])].append(st)

    pairs = 0
    endpoint_injective_checks = 0
    switch_prime_checks = 0

    for fiber in fibers.values():
        for i in range(len(fiber)):
            for j in range(i + 1, len(fiber)):
                u, v = fiber[i], fiber[j]
                pairs += 1
                xi, k = u["xi"], u["k"]
                X = max(u["Q"], v["Q"])

                A, B, C, D = four_cells((u["a"], u["b"]), (v["a"], v["b"]))
                alpha, beta, gamma, delta = four_cells((u["km"], u["kp"]), (v["km"], v["kp"]))

                xi_agree = A * D
                xi_switch = B * C
                k_agree = alpha * delta
                k_switch = beta * gamma
                assert xi_agree * xi_switch == xi
                assert k_agree * k_switch == k

                # In the fixed-xi-split injective range, every off-diagonal pair
                # must satisfy the new cross-xi agreement bound.
                if xi * xi * k > 2 * X**4:
                    assert xi_agree * xi_agree * k <= 2 * X**4
                    endpoint_injective_checks += 1

                # Symmetric switch lower bound follows algebraically.
                assert xi_switch * xi_agree == xi
                if xi_agree > 0:
                    lhs = xi_switch * math.sqrt(2) * X * X
                    rhs = xi * math.sqrt(k)
                    # Floating comparison only checks the rearrangement with slack;
                    # the exact integer assertion above is authoritative.
                    if xi_agree * xi_agree * k <= 2 * X**4:
                        assert lhs + 1e-9 >= rhs

                # Every odd prime that changes side must be 1 mod 4.
                for n in (xi_switch, k_switch):
                    for ell in prime_factors(n):
                        if ell == 2:
                            continue
                        assert ell % 4 == 1
                        switch_prime_checks += 1

                # Retain the primewise residue conditions, not only a product sign.
                for ell in prime_factors(xi_switch):
                    if ell != 2:
                        assert legendre(k, ell) == 1
                for ell in prime_factors(k_switch):
                    if ell != 2:
                        assert legendre(xi, ell) == 1

    return pairs, endpoint_injective_checks, switch_prime_checks


def check_exponents() -> None:
    xi = Fraction(3, 4)
    k = Fraction(1, 1)
    X = Fraction(1, 2)
    xi_switch = xi + k / 2 - 2 * X
    k_switch = k + xi / 2 - 2 * X
    assert xi_switch == Fraction(1, 4)
    assert k_switch == Fraction(3, 8)
    assert 2 * xi + k - 4 * X == Fraction(1, 2)  # fixed xi-split injectivity margin


def main() -> None:
    check_docs()
    states = build_states()
    pairs, endpoint_checks, switch_checks = check_collision_pairs(states)
    check_exponents()
    print("STAGE14_4CE_AUDIT=PASS")
    print(f"REDUCED_STATES={len(states)}")
    print(f"SAME_XI_K_OFFDIAGONAL_PAIRS={pairs}")
    print(f"FIXED_XI_SPLIT_INJECTIVE_RANGE_PAIR_CHECKS={endpoint_checks}")
    print(f"ODD_SWITCH_PRIME_CHECKS={switch_checks}")
    print("FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4")
    print("FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8")
    print("ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true")
    print("ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4cf")


if __name__ == "__main__":
    main()
