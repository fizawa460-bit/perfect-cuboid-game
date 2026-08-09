#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s6-01.

This script is finite regression evidence only.  The theorem-level statements in
result.md come from exact valuation/gcd arguments.  The audit checks those
identities on a nontrivial finite family, including witnesses with D>1.
"""

from fractions import Fraction
import math


def factorint(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def rad(n: int) -> int:
    r = 1
    for p in factorint(n):
        r *= p
    return r


def signed_squarefree_kernel(n: int) -> tuple[int, int]:
    assert n != 0
    r = 1
    for p, e in factorint(n).items():
        if e & 1:
            r *= p
    d = r if n > 0 else -r
    q = abs(n) // r
    u = math.isqrt(q)
    assert u * u == q
    return d, u


def admissible_tau_packets() -> list[tuple[int, int, int]]:
    values = (-2, -1, 1, 2)
    out = []
    for t0 in values:
        for t1 in values:
            for t2 in values:
                product = t0 * t1 * t2
                if product > 0 and math.isqrt(product) ** 2 == product:
                    out.append((t0, t1, t2))
    return out


TAU_PACKETS = admissible_tau_packets()
assert len(TAU_PACKETS) == 16


def primitive_triples(limit_m: int = 18):
    for m in range(2, limit_m + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            if (m - n) % 2 == 0:
                continue
            S = 2 * m * n
            X = m * m - n * n
            H = m * m + n * n
            assert S * S + X * X == H * H
            assert math.gcd(S, X) == math.gcd(S, H) == math.gcd(X, H) == 1
            yield m, n, S, X, H


def check_generic_gcd_support() -> int:
    checks = 0
    for m, n, S, X, H in primitive_triples(12):
        for D in range(1, 7):
            for A in range(-173, 174, 17):
                if math.gcd(A, D) != 1:
                    continue
                G0 = A
                G1 = A - S * S * D * D
                G2 = A + X * X * D * D

                assert S * S % math.gcd(G0, G1) == 0
                assert X * X % math.gcd(G0, G2) == 0
                assert H * H % math.gcd(G1, G2) == 0

                for G in (G0, G1, G2):
                    assert math.gcd(G, D) == 1
                checks += 1
    return checks


def check_witness_packet(record) -> tuple[tuple[int, int, int], int, int, int]:
    m, n, S, X, H, D, A, Y, Gs = record

    ds: list[int] = []
    us: list[int] = []
    for G in Gs:
        d, u = signed_squarefree_kernel(G)
        ds.append(d)
        us.append(u)

    dprod = ds[0] * ds[1] * ds[2]
    assert dprod > 0 and math.isqrt(dprod) ** 2 == dprod

    for d in ds:
        for p in factorint(d):
            assert (2 * S * X * H) % p == 0

    odd_parts = [abs(d) // (2 if abs(d) % 2 == 0 else 1) for d in ds]
    a = math.gcd(odd_parts[0], odd_parts[1])
    b = math.gcd(odd_parts[0], odd_parts[2])
    c = math.gcd(odd_parts[1], odd_parts[2])

    assert a * b == odd_parts[0]
    assert a * c == odd_parts[1]
    assert b * c == odd_parts[2]
    assert math.gcd(a, b) == math.gcd(a, c) == math.gcd(b, c) == 1

    assert S % a == 0
    assert X % b == 0
    assert H % c == 0

    tau = (
        ds[0] // (a * b),
        ds[1] // (a * c),
        ds[2] // (b * c),
    )
    assert tau in TAU_PACKETS

    d0, d1, d2 = ds
    u0, u1, u2 = us

    assert d0 * u0 * u0 - d1 * u1 * u1 == S * S * D * D
    assert d2 * u2 * u2 - d0 * u0 * u0 == X * X * D * D
    assert d2 * u2 * u2 - d1 * u1 * u1 == H * H * D * D

    for d, u in zip(ds, us):
        assert math.gcd(D, abs(d) * u) == 1

    # Exact refinement to the five Euclid support columns.
    a_A = math.gcd(a, rad(m))
    a_B = math.gcd(a, rad(n))
    b_C = math.gcd(b, rad(m - n))
    b_D = math.gcd(b, rad(m + n))
    assert a_A * a_B == a
    assert b_C * b_D == b
    assert c % math.gcd(c, rad(H)) == 0
    assert math.gcd(c, rad(H)) == c

    # Rational reconstruction, including D>1 witnesses.
    Z = Fraction(A, D * D)
    W = Fraction(Y, D**3)
    assert W * W == Z * (Z - S * S) * (Z + X * X)

    return tau, a, b, c


def collect_square_product_witnesses(target: int = 40):
    hits = []
    for m, n, S, X, H in primitive_triples(18):
        for D in range(1, 9):
            for A in range(-4000, 4001):
                if math.gcd(A, D) != 1:
                    continue
                Gs = (
                    A,
                    A - S * S * D * D,
                    A + X * X * D * D,
                )
                if 0 in Gs:
                    continue
                y2 = Gs[0] * Gs[1] * Gs[2]
                if y2 <= 0:
                    continue
                Y = math.isqrt(y2)
                if Y * Y != y2:
                    continue
                record = (m, n, S, X, H, D, A, Y, Gs)
                check_witness_packet(record)
                hits.append(record)
                if len(hits) >= target:
                    return hits
    return hits


def check_tau_logic() -> None:
    assert len(TAU_PACKETS) == 16
    sign_patterns = set()
    parity_patterns = set()
    for tau in TAU_PACKETS:
        signs = tuple(1 if t > 0 else -1 for t in tau)
        twos = tuple(abs(t) == 2 for t in tau)
        assert signs[0] * signs[1] * signs[2] == 1
        assert sum(twos) % 2 == 0
        sign_patterns.add(signs)
        parity_patterns.add(twos)
    assert len(sign_patterns) == 4
    assert len(parity_patterns) == 4


def main() -> None:
    check_tau_logic()
    generic_checks = check_generic_gcd_support()
    hits = collect_square_product_witnesses(40)

    assert len(hits) == 40
    denominator_nontrivial = sum(1 for rec in hits if rec[5] > 1)
    assert denominator_nontrivial >= 1

    packet_types = set()
    for rec in hits:
        packet_types.add(check_witness_packet(rec)[0])

    print(f"TAU_PACKET_COUNT={len(TAU_PACKETS)}")
    print(f"GENERIC_GCD_SUPPORT_CHECKS={generic_checks}")
    print(f"FINITE_SQUARE_PRODUCT_WITNESSES={len(hits)}")
    print(f"FINITE_WITNESSES_WITH_D_GT_1={denominator_nontrivial}")
    print(f"FINITE_TAU_PACKET_TYPES_SEEN={len(packet_types)}")
    print("PAIRWISE_GCD_SUPPORT_AUDIT=true")
    print("SIGNED_KERNEL_SUPPORT_AUDIT=true")
    print("ODD_EDGE_PACKET_FACTORIZATION_AUDIT=true")
    print("FIVE_COLUMN_REFINEMENT_AUDIT=true")
    print("TWO_QUADRIC_RECONSTRUCTION_AUDIT=true")
    print("DENOMINATOR_RATIONAL_RECONSTRUCTION_AUDIT=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
