#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def rad_odd(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    r = 1
    p = 3
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        r *= n
    return r


def rad_all(n: int) -> int:
    n = abs(n)
    r = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            r *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        r *= n
    return r


def prime_factors(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def squarefree_divisors(r: int):
    ps = prime_factors(r)
    for mask in range(1 << len(ps)):
        d = 1
        for i, p in enumerate(ps):
            if mask >> i & 1:
                d *= p
        yield d


def crt(a: int, m: int, b: int, n: int) -> int:
    return (a + ((b - a) * pow(m, -1, n) % n) * m) % (m * n)


def unit_line_cover_slopes(A: int, B: int, q: int):
    states = [(0, 1)]
    for p in prime_factors(q):
        roots = [r for r in range(1, p) if (A * r * r - B) % p == 0]
        if not roots:
            # For a non-residue ratio the true solution is only (0,0) mod p;
            # any unit line contains it, so slope 1 is a safe upper cover.
            roots = [1]
        nxt = []
        for old, mod in states:
            for r in roots:
                nxt.append((crt(old, mod, r, p), mod * p))
        states = nxt
    return [r % q for r, _ in states]


def audit_upstream():
    requirements = {
        "stages/stage14/14-4bi-L/result.md": [
            "STAGE14_4BI_L=COMPOSITE_EDGE_KERNEL_INCIDENCE_AND_LARGE_KERNEL_DICHOTOMY_CLOSED",
            "ARBITRARY_LARGE_KERNEL_REMAINDER_OPEN=false",
        ],
        "stages/stage14/14-s6-03/result.md": [
            "STAGE14_S6_03=COMPLETE_CENTERED_QUARTIC_AUXILIARY_SIEVE_AND_SMALL_DENOMINATOR_REDUCTION",
            "ONLY_COORDINATE_LEVEL_COMPLEMENT=SMALL_DENOMINATOR",
            "EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true",
        ],
    }
    for rel, flags in requirements.items():
        text = (ROOT / rel).read_text()
        for flag in flags:
            assert flag in text, (rel, flag)


def audit_full_radical_divisibility():
    checks = 0
    for m in range(2, 35):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            assert S * S + X * X == H * H
            RS, RX, RH = rad_odd(S), rad_odd(X), rad_odd(H)
            assert math.gcd(RS, RX) == math.gcd(RS, RH) == math.gcd(RX, RH) == 1
            for edge, R in [(S, RS), (X, RX), (H, RH)]:
                for k in squarefree_divisors(R):
                    assert edge % k == 0
                    assert (k * (edge // k) ** 2) % R == 0
                    checks += 1
    return checks


def audit_line_cover():
    checks = 0
    for q in [3, 5, 7, 15, 21, 35, 105]:
        units = [x for x in [1, 2, 4, 8, 11, 13, 17] if math.gcd(x, q) == 1]
        for A in units:
            for B in units:
                slopes = unit_line_cover_slopes(A, B, q)
                assert len(slopes) <= 2 ** len(prime_factors(q))
                for x in range(q):
                    for y in range(q):
                        if (A * x * x - B * y * y) % q == 0:
                            assert any((x - r * y) % q == 0 for r in slopes)
                checks += 1
    return checks


def audit_rectangle_bound():
    checks = 0
    for q in [5, 7, 15, 21, 35]:
        for r in range(1, q):
            if math.gcd(r, q) != 1:
                continue
            for U, V in [(3, 7), (5, 11), (8, 13), (13, 21), (21, 34)]:
                n = sum(
                    1
                    for x in range(1, U + 1)
                    for y in range(1, V + 1)
                    if (x - r * y) % q == 0
                )
                assert n <= math.ceil(U * V / q + min(U, V) + 1)
                checks += 1
    return checks


def audit_short_transfer():
    # Directly audit the inequality used in the proof:
    # H^2 D^2/c <= 4 H U^2 and c<=H => D<=2U.
    checks = 0
    for H in [5, 13, 25, 65, 85, 125]:
        for c in [d for d in range(1, H + 1) if H % d == 0]:
            for U in range(1, 20):
                for D in range(1, 2 * U + 4):
                    if H * H * D * D / c <= 4 * H * U * U:
                        assert D <= 2 * U
                        checks += 1
    return checks


def radical_poor_diagnostic():
    B = 5000
    out = {}
    for rho in [0.25, 1 / 3, 0.5]:
        R = int(B ** rho)
        count = sum(1 for n in range(1, B + 1) if rad_all(n) <= R)
        out[str(rho)] = {"R": R, "count": count}
    return out


def main():
    audit_upstream()
    full_radical_checks = audit_full_radical_divisibility()
    line_checks = audit_line_cover()
    rectangle_checks = audit_rectangle_bound()
    short_checks = audit_short_transfer()
    diag = radical_poor_diagnostic()

    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)

    summary = json.loads(
        (ROOT / "stages/stage14/data/14-4/radical_smallD_core_summary.json").read_text()
    )
    assert summary["imports"]["stage14_s6_03"] is True
    assert summary["claims"]["FULL_ODD_EDGE_RADICAL_CONGRUENCES_PROVED"] is True
    assert summary["claims"]["SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION"] is False
    assert summary["claims"]["ONLY_COORDINATE_LEVEL_COMPLEMENT_IS_SMALL_DENOMINATOR"] is True
    assert summary["claims"]["S_ROUTE_GLOBAL_POSITIVE_SAVING_PROVED"] is False
    assert summary["exponents"]["required_post_local_saving"] == "10/21"

    print(f"FULL_RADICAL_DIVISIBILITY_CHECKS={full_radical_checks}")
    print(f"CRT_LINE_COVER_CHECKS={line_checks}")
    print(f"RECTANGLE_BOUND_CHECKS={rectangle_checks}")
    print(f"SHORT_TRANSFER_CHECKS={short_checks}")
    print("RADICAL_POOR_DIAGNOSTIC=" + json.dumps(diag, sort_keys=True))
    print("FULL_ODD_EDGE_RADICAL_CONGRUENCE_AUDIT=true")
    print("SMALL_KERNEL_INTRINSIC_MODULUS_OBSTRUCTION=false")
    print("ONLY_COORDINATE_LEVEL_COMPLEMENT=SMALL_DENOMINATOR")
    print("POST_LOCAL_REQUIRED_DELTA=10/21")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
