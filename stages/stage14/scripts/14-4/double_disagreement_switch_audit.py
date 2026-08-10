#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4ce/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/double_disagreement_switch_summary.json"
FOUR_CD = ROOT / "stages/stage14/14-4cd/result.md"
S7_18 = ROOT / "stages/stage14/14-s7-18/result.md"


def build_spf(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    for p in range(2, int(limit**0.5) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


LIMIT = 260
SPF = build_spf(LIMIT * LIMIT + 1)


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    while n > 1:
        p = SPF[n]
        out.append(p)
        while n % p == 0:
            n //= p
    return out


def squarefree_kernel(n: int) -> int:
    k = 1
    while n > 1:
        p = SPF[n]
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            k *= p
    return k


def canonical(n: int) -> tuple[int, int]:
    sf = squarefree_kernel(n)
    q = n // sf
    r = math.isqrt(q)
    assert r * r == q
    return sf, r


def xi_cells(a1: int, b1: int, a2: int, b2: int) -> tuple[int, int, int, int]:
    A = math.gcd(a1, a2)
    B = a1 // A
    C = a2 // A
    D = math.gcd(b1, b2)
    assert A * B == a1
    assert C * D == b1
    assert A * C == a2
    assert B * D == b2
    return A, B, C, D


def k_cells(km1: int, kp1: int, km2: int, kp2: int) -> tuple[int, int, int, int]:
    alpha = math.gcd(km1, km2)
    beta = km1 // alpha
    gamma = km2 // alpha
    delta = math.gcd(kp1, kp2)
    assert alpha * beta == km1
    assert gamma * delta == kp1
    assert alpha * gamma == km2
    assert beta * delta == kp2
    return alpha, beta, gamma, delta


def pairwise_coprime(vals: tuple[int, ...]) -> bool:
    return all(math.gcd(vals[i], vals[j]) == 1 for i in range(len(vals)) for j in range(i + 1, len(vals)))


def check_docs() -> None:
    result = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    four_cd = FOUR_CD.read_text()
    s7_18 = S7_18.read_text()

    required = [
        "STAGE14_4CE=COMPLETE_DUAL_ALLOCATION_INJECTIVITY_AND_DOUBLE_DISAGREEMENT_REDUCTION",
        "XI_FIXED_SPLIT_INJECTIVE_IF_xi2_k_GT_2_X4=true",
        "FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4",
        "FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8",
        "FOUR_CD_ENDPOINT_DOUBLE_SWITCH_PRODUCT_LOWER_EXPONENT=5/8",
        "ODD_XI_SWITCH_PRIMES_ARE_1_MOD_4=true",
        "ODD_K_SWITCH_PRIMES_ARE_1_MOD_4=true",
        "MAINLINE_H_NEEDED=false",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "NEXT=Stage14-4cf",
    ]
    for token in required:
        assert token in result, token

    assert "STAGE14_4CD=FOUR_ROOT_LATTICE_CONGRUENCE_AND_MAXIMAL_K_ENDPOINT_LOCALIZATION" in four_cd
    assert "SEVEN_EIGHT_RESIDUAL_REQUIRES_K_EXPONENT=1-o(1)" in four_cd
    assert "STAGE14_S7_18=COMPLETE_SAME_SPLIT_COLLISION_ELIMINATION_AND_LARGE_CROSS_SPLIT_DISAGREEMENT_REDUCTION" in s7_18
    assert "FOUR_CD_ENDPOINT_SWITCH_PRODUCT_LOWER_EXPONENT=3/8" in s7_18

    assert summary["current_physical_upper_bound_exponent"] == "7/8"
    assert summary["four_cd_endpoint_xi_switch_lower_exponent"] == "1/4"
    assert summary["four_cd_endpoint_k_switch_lower_exponent"] == "3/8"
    assert summary["four_cd_endpoint_double_switch_product_lower_exponent"] == "5/8"
    assert summary["mainline_h_needed"] is False
    assert summary["next"] == "Stage14-4cf"


def enumerate_states() -> dict[tuple[int, int], list[tuple[int, ...]]]:
    groups: dict[tuple[int, int], list[tuple[int, ...]]] = defaultdict(list)
    for Q in range(2, LIMIT + 1):
        for P in range(1, Q):
            if math.gcd(P, Q) != 1:
                continue
            a, x = canonical(P)
            b, y = canonical(Q)
            xi = a * b
            D = Q * Q - P * P
            k, h = canonical(D)
            g = math.gcd(Q - P, Q + P)
            assert g in (1, 2)
            km, r = canonical((Q - P) // g)
            kp, s = canonical((Q + P) // g)
            assert km * kp == k
            assert math.gcd(a, b) == math.gcd(x, y) == 1
            assert math.gcd(xi, k * h) == 1
            assert b * b * y**4 - a * a * x**4 == k * h * h
            groups[(xi, k)].append((P, Q, a, b, x, y, h, km, kp, r, s))
    return groups


def check_collision_geometry() -> tuple[int, int, int]:
    groups = enumerate_states()
    collision_pairs = 0
    xi_switch_pairs = 0
    k_switch_pairs = 0

    for (xi, k), states in groups.items():
        if len(states) < 2:
            continue
        for s1, s2 in itertools.combinations(states, 2):
            collision_pairs += 1
            P1, Q1, a1, b1, x1, y1, h1, km1, kp1, r1, t1 = s1
            P2, Q2, a2, b2, x2, y2, h2, km2, kp2, r2, t2 = s2
            X = max(Q1, Q2)

            A, B, C, D = xi_cells(a1, b1, a2, b2)
            assert pairwise_coprime((A, B, C, D))
            assert A * B * C * D == xi
            Xi_agree = A * D
            Xi_switch = B * C
            assert Xi_agree * Xi_switch == xi

            # Universal off-diagonal necessary bound proved in 4ce.
            assert Xi_agree * Xi_agree * k <= 2 * X**4

            if Xi_switch > 1:
                xi_switch_pairs += 1
                for p in prime_factors(Xi_switch):
                    if p != 2:
                        assert p % 4 == 1

            alpha, beta, gamma, delta = k_cells(km1, kp1, km2, kp2)
            assert pairwise_coprime((alpha, beta, gamma, delta))
            assert alpha * beta * gamma * delta == k
            K_switch = beta * gamma
            if K_switch > 1:
                k_switch_pairs += 1
                for p in prime_factors(K_switch):
                    if p != 2:
                        assert p % 4 == 1

            # Statewise residue graph, verified prime-by-prime by Euler criterion.
            for p in prime_factors(Xi_switch):
                if p == 2:
                    continue
                assert pow(k % p, (p - 1) // 2, p) == 1
            for p in prime_factors(K_switch):
                if p == 2:
                    continue
                assert pow(xi % p, (p - 1) // 2, p) == 1

    assert collision_pairs > 0
    assert xi_switch_pairs > 0
    assert k_switch_pairs > 0
    return collision_pairs, xi_switch_pairs, k_switch_pairs


def check_exponents() -> None:
    gamma = Fraction(3, 4)
    kappa_old = Fraction(3, 4)
    kappa_endpoint = Fraction(1, 1)

    xi_switch_old = gamma + kappa_old / 2 - 1
    xi_switch_endpoint = gamma + kappa_endpoint / 2 - 1
    k_switch_endpoint = kappa_endpoint + gamma / 2 - 1

    assert xi_switch_old == Fraction(1, 8)
    assert xi_switch_endpoint == Fraction(1, 4)
    assert k_switch_endpoint == Fraction(3, 8)
    assert xi_switch_endpoint + k_switch_endpoint == Fraction(5, 8)

    # Fixed-allocation injectivity has a 1/4 exponent margin already on the old shell.
    assert 2 * gamma + kappa_old - 2 == Fraction(1, 4)


def main() -> None:
    check_docs()
    check_exponents()
    collisions, xi_switch, k_switch = check_collision_geometry()
    print("STAGE14_4CE_AUDIT=PASS")
    print(f"FINITE_COLLISION_PAIRS={collisions}")
    print(f"FINITE_XI_SWITCH_PAIRS={xi_switch}")
    print(f"FINITE_K_SWITCH_PAIRS={k_switch}")
    print("XI_FIXED_SPLIT_INJECTIVE_IF_xi2_k_GT_2_X4=true")
    print("FOUR_CD_ENDPOINT_XI_SWITCH_LOWER_EXPONENT=1/4")
    print("FOUR_CD_ENDPOINT_K_SWITCH_LOWER_EXPONENT=3/8")
    print("FOUR_CD_ENDPOINT_DOUBLE_SWITCH_PRODUCT_LOWER_EXPONENT=5/8")
    print("ODD_SWITCH_PRIMES_ARE_1_MOD_4=true")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("MAINLINE_H_NEEDED=false")
    print("NEXT=Stage14-4cf")


if __name__ == "__main__":
    main()
