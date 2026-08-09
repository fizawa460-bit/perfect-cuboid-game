#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-s6-04.

The theorem-level claims in result.md are exact algebraic arguments.  This audit
checks the witness-square resonance, the D^2 congruence-line structure, the
root-count envelope, and the inherited anisotropic size forcing on finite data.
"""

from __future__ import annotations

import math
import runpy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
PREV = ROOT / "stages/stage14/scripts/14-s6-01/integral_witness_packet_audit.py"
ns = runpy.run_path(str(PREV))
collect_square_product_witnesses = ns["collect_square_product_witnesses"]
signed_squarefree_kernel = ns["signed_squarefree_kernel"]
factorint = ns["factorint"]


def omega_odd(n: int) -> int:
    return sum(1 for p in factorint(n) if p != 2)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v


def packet_data(record):
    m, n, S, X, H, D, A, Y, Gs = record
    ds = []
    us = []
    for G in Gs:
        d, u = signed_squarefree_kernel(G)
        ds.append(d)
        us.append(u)
    d0, d1, d2 = ds
    u0, u1, u2 = us
    k2 = d0 * d1 * d2
    assert k2 > 0
    k = math.isqrt(k2)
    assert k * k == k2
    return (m, n, S, X, H, D, A, Y, Gs, ds, us, k)


def phi_values(S, X, H, D, ds, us):
    d0, d1, d2 = ds
    u0, u1, u2 = us
    phi0 = d0 * (d0 * u0 * u0 - S * S * D * D) * (
        d0 * u0 * u0 + X * X * D * D
    )
    phi1 = d1 * (d1 * u1 * u1 + S * S * D * D) * (
        d1 * u1 * u1 + H * H * D * D
    )
    phi2 = d2 * (d2 * u2 * u2 - X * X * D * D) * (
        d2 * u2 * u2 - H * H * D * D
    )
    return (phi0, phi1, phi2)


def check_exact_witness_resonance(records) -> tuple[int, int, int]:
    prime_pool = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    identity_checks = 0
    character_one = 0
    character_zero = 0

    for rec in records:
        _, _, S, X, H, D, _, _, _, ds, us, k = packet_data(rec)
        d0, d1, d2 = ds
        u0, u1, u2 = us
        phis = phi_values(S, X, H, D, ds, us)
        roots = (k * u1 * u2, k * u0 * u2, k * u0 * u1)

        for phi, root in zip(phis, roots):
            assert phi == root * root
            identity_checks += 1

        for i, (phi, root) in enumerate(zip(phis, roots)):
            di = ds[i]
            for p in prime_pool:
                if (2 * abs(di) * S * X * H) % p == 0:
                    continue
                val = legendre(phi, p)
                if root % p == 0:
                    assert val == 0
                    character_zero += 1
                else:
                    assert val == 1
                    character_one += 1

    assert character_one > 0
    return identity_checks, character_one, character_zero


def check_denominator_congruence(records) -> tuple[int, int]:
    congruence_checks = 0
    nontrivial_D = 0

    for rec in records:
        _, _, S, X, H, D, _, _, _, ds, us, _ = packet_data(rec)
        d0, d1, d2 = ds
        u0, u1, u2 = us

        assert d2 * u2 * u2 - d1 * u1 * u1 == H * H * D * D
        assert math.gcd(D, abs(d1 * d2 * u1 * u2)) == 1
        q = D * D
        assert (d2 * u2 * u2 - d1 * u1 * u1) % q == 0

        if D > 1:
            nontrivial_D += 1
            inv_u1 = pow(u1, -1, q)
            inv_d2 = pow(d2 % q, -1, q)
            r = (u2 * inv_u1) % q
            target = (d1 * inv_d2) % q
            assert (r * r - target) % q == 0
            assert (u2 - r * u1) % q == 0

        # inherited s6-03 anisotropic forcing
        assert D <= 2 * max(u1, u2)
        congruence_checks += 1

    assert nontrivial_D > 0
    return congruence_checks, nontrivial_D


def check_root_count_envelope() -> tuple[int, int]:
    cases = 0
    max_roots = 0
    for D in range(2, 31):
        q = D * D
        # t=1 is a soluble unit ratio and is enough to stress the maximal
        # 2-primary multiplicity as well as all odd CRT factors.
        roots = [r for r in range(q) if math.gcd(r, D) == 1 and (r * r - 1) % q == 0]
        envelope = 4 * (2 ** omega_odd(D))
        assert len(roots) <= envelope
        max_roots = max(max_roots, len(roots))
        cases += 1
    return cases, max_roots


def check_rectangle_line_cover() -> tuple[int, int]:
    checks = 0
    total_pairs = 0
    for D in range(2, 11):
        q = D * D
        roots = [r for r in range(q) if math.gcd(r, D) == 1 and (r * r - 1) % q == 0]
        U1, U2 = 29, 37
        pairs = []
        for u1 in range(1, U1 + 1):
            if math.gcd(u1, D) != 1:
                continue
            for u2 in range(1, U2 + 1):
                if math.gcd(u2, D) != 1:
                    continue
                if (u2 * u2 - u1 * u1) % q == 0:
                    pairs.append((u1, u2))
                    assert any((u2 - r * u1) % q == 0 for r in roots)

        # Safe finite version of O(R*(UV/q + min(U,V) + 1)).
        rhs = len(roots) * (U1 * U2 / q + min(U1, U2) + 1)
        assert len(pairs) <= math.ceil(rhs)
        checks += 1
        total_pairs += len(pairs)
    return checks, total_pairs


def main() -> None:
    records = collect_square_product_witnesses(24)
    assert len(records) == 24

    identity_checks, char_one, char_zero = check_exact_witness_resonance(records)
    congruence_checks, nontrivial_D = check_denominator_congruence(records)
    root_cases, max_roots = check_root_count_envelope()
    rectangle_checks, total_pairs = check_rectangle_line_cover()

    print(f"FINITE_WITNESSES={len(records)}")
    print(f"CENTERED_QUARTIC_IDENTITY_CHECKS={identity_checks}")
    print(f"GOOD_PRIME_CHARACTER_ONE_CHECKS={char_one}")
    print(f"GOOD_PRIME_CHARACTER_ZERO_CHECKS={char_zero}")
    print(f"DENOMINATOR_CONGRUENCE_CHECKS={congruence_checks}")
    print(f"WITNESSES_WITH_D_GT_1={nontrivial_D}")
    print(f"ROOT_COUNT_CASES={root_cases}")
    print(f"MAX_ROOTS_SEEN={max_roots}")
    print(f"RECTANGLE_LINE_COVER_CHECKS={rectangle_checks}")
    print(f"RECTANGLE_SOLUTION_PAIRS={total_pairs}")
    print("EXACT_WITNESS_RESONANCE_AUDIT=true")
    print("DENOMINATOR_D2_MODULUS_AUDIT=true")
    print("DENOMINATOR_ROOT_MULTIPLICITY_AUDIT=true")
    print("DENOMINATOR_LINE_COVER_AUDIT=true")
    print("ANISOTROPIC_D_FORCING_REGRESSION=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
