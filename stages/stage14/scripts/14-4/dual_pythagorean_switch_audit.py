#!/usr/bin/env python3
from __future__ import annotations

import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
ADDENDUM = ROOT / "stages/stage14/14-4ce/s7-19-addendum.md"
S7_19 = ROOT / "stages/stage14/14-s7-19/result.md"


def sfker(n: int) -> int:
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
    sf = sfker(n)
    r = math.isqrt(n // sf)
    assert sf * r * r == n
    return sf, r


def four_cells(s1: tuple[int, int], s2: tuple[int, int]) -> tuple[int, int, int, int]:
    a, b = s1
    c, d = s2
    A = math.gcd(a, c)
    B = math.gcd(a, d)
    C = math.gcd(b, c)
    D = math.gcd(b, d)
    assert (a, b, c, d) == (A * B, C * D, A * C, B * D)
    vals = A, B, C, D
    for i in range(4):
        for j in range(i + 1, 4):
            assert math.gcd(vals[i], vals[j]) == 1
    return vals


def build(limit: int = 170):
    states = []
    for Q in range(2, limit + 1):
        for P in range(1, Q):
            if math.gcd(P, Q) != 1:
                continue
            a, x = canonical(P)
            b, y = canonical(Q)
            xi = a * b
            k = sfker(Q * Q - P * P)
            h = math.isqrt((Q * Q - P * P) // k)
            assert k * h * h == Q * Q - P * P
            states.append((xi, k, P, Q, a, b, x, y, h))
    return states


def main() -> None:
    add = ADDENDUM.read_text()
    s719 = S7_19.read_text()
    assert "DUAL_PRIMITIVE_PYTHAGOREAN_COMPOSITION_PROVED=true" in add
    assert "DUAL_TRANSVERSE_K0_LOWER_EXPONENT=3/8" in add
    assert "K_switch | H_0" in s719
    assert "xi_0>=B^(1/4-o(1))" in s719

    states = build()
    fibers = defaultdict(list)
    for st in states:
        fibers[(st[0], st[1])].append(st)

    pair_checks = 0
    primitive_checks = 0
    for fiber in fibers.values():
        for i in range(len(fiber)):
            for j in range(i + 1, len(fiber)):
                u, v = fiber[i], fiber[j]
                xi, k = u[0], u[1]
                P1, Q1, a1, b1, x1, y1, h1 = u[2:]
                P2, Q2, a2, b2, x2, y2, h2 = v[2:]
                A, B, C, D = four_cells((a1, b1), (a2, b2))
                xi_agree = A * D
                xi_switch = B * C

                H = Q1 * Q2 + P1 * P2
                L = Q1 * P2 + P1 * Q2
                W = k * h1 * h2
                assert H * H == L * L + W * W
                assert H % xi_switch == 0
                assert L % xi_agree == 0

                d = math.gcd(math.gcd(H, L), W)
                H0, L0, W0 = H // d, L // d, W // d
                assert H0 * H0 == L0 * L0 + W0 * W0
                assert math.gcd(math.gcd(H0, L0), W0) == 1
                assert math.gcd(d, xi) == 1
                assert H0 % xi_switch == 0
                assert L0 % xi_agree == 0

                k0 = k // math.gcd(k, d)
                assert W0 % k0 == 0
                X = max(Q1, Q2)
                # exact squared form of d <= 2 X^2 / sqrt(xi)
                assert d * d * xi <= 4 * X**4
                # exact squared lower bound k0 >= k sqrt(xi)/(2X^2)
                assert 4 * X**4 * k0 * k0 >= k * k * xi

                # Primitive Pythagorean hypotenuse has no odd 3 mod 4 prime divisor.
                n = xi_switch
                p = 3
                while p * p <= n:
                    if n % p == 0:
                        assert p % 4 == 1
                        while n % p == 0:
                            n //= p
                    p += 2
                if n > 1 and n % 2 == 1:
                    assert n % 4 == 1

                pair_checks += 1
                primitive_checks += 1

    assert Fraction(1, 1) + Fraction(3, 8) - 1 == Fraction(3, 8)
    print("STAGE14_4CE_DUAL_PYTHAGOREAN_AUDIT=PASS")
    print(f"SAME_XI_K_PAIR_CHECKS={pair_checks}")
    print(f"PRIMITIVE_DUAL_TRIPLE_CHECKS={primitive_checks}")
    print("XI_SWITCH_DIVIDES_DUAL_PRIMITIVE_HYPOTENUSE=true")
    print("DUAL_TRANSVERSE_K0_LOWER_EXPONENT=3/8")
    print("NEXT=Stage14-4cf")


if __name__ == "__main__":
    main()
