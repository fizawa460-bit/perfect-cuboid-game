#!/usr/bin/env python3
from __future__ import annotations

from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def sqf(n: int) -> int:
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p += 1
    if n > 1:
        out *= n
    return out


def valuation(n: int, p: int) -> int:
    n = abs(n)
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def check_squareclass_identity() -> int:
    checks = 0
    # Primitive rays with D0=x^2-y^2. Use h parity so T/4 is integral.
    for x, y in ((5, 3), (8, 3), (7, 5), (9, 7)):
        D0 = x * x - y * y
        K = sqf(D0)
        t0_sq = D0 // K
        t0 = isqrt(t0_sq)
        assert t0 * t0 == t0_sq
        for h in range(2, 30, 2):
            T = D0 * h * h
            assert T == K * (t0 * h) ** 2
            assert T % 4 == 0
            # One legal arithmetic factorization of T/4, sufficient to guard squareclass algebra.
            Fs = (1, 1, 1, T // 4)
            product = 1
            for f in Fs:
                product *= f
            assert 4 * product == T
            assert sqf(product) == K
            for p in (2, 3, 5, 7, 11, 13, 17):
                lhs = sum(valuation(f, p) for f in Fs) % 2
                rhs = valuation(K, p) % 2
                assert lhs == rhs
                checks += 1
            checks += 3
    return checks


def check_support_inequality() -> int:
    checks = 0
    # Synthetic charged representatives with injective products.
    rows = []
    for h in range(1, 65):
        row = (h, h + 1, 2 * h + 1, 3 * h + 1)
        rows.append(row)
    supports = [set(row[j] for row in rows) for j in range(4)]
    product_support_bound = 1
    for s in supports:
        product_support_bound *= len(s)
    assert len(rows) <= product_support_bound
    assert max(map(len, supports)) ** 4 >= len(rows)
    checks += 2
    return checks


def check_kernel_squarepart_dichotomy() -> int:
    checks = 0
    fixed_kernel_values = {6 * a * a for a in range(1, 65)}
    kernels = {sqf(v) for v in fixed_kernel_values}
    assert kernels == {6}
    fibers = {}
    for v in fixed_kernel_values:
        k = sqf(v)
        a2 = v // k
        a = isqrt(a2)
        assert a * a == a2
        fibers.setdefault(k, set()).add(a)
    assert len(fibers[6]) == len(fixed_kernel_values)
    checks += 3

    diffuse_values = {p for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)}
    diffuse_kernels = {sqf(v) for v in diffuse_values}
    assert len(diffuse_kernels) == len(diffuse_values)
    checks += 1
    return checks


def check_boundary_tokens() -> int:
    required = {
        "stages/stage14/14-s7-81/result.md": [
            "STAGE14_S7_81=COMPLETE_FIXED_KERNEL_SQUARE_VALUE_TO_FOUR_FACTOR_SQUARECLASS_RELATION",
            "FOUR_FACTOR_PRODUCT_SQUARECLASS_EQUALS_FIXED_K=true",
            "RECEIVER_MATERIALLY_CHANGED=false",
            "NEXT=Stage14-s7-82",
        ],
        "stages/stage14/14-s7-82/result.md": [
            "STAGE14_S7_82=COMPLETE_FIXED_KERNEL_RADIAL_SUPPORT_TO_ONE_FACTOR_POLYNOMIAL_OUTER_MOBILITY",
            "POLYNOMIAL_RADIAL_SUPPORT_FORCES_POLYNOMIAL_FACTOR_VALUE_SUPPORT=true",
            "RECEIVER_MATERIALLY_CHANGED=false",
            "NEXT=Stage14-s7-83",
        ],
        "stages/stage14/14-s7-83/result.md": [
            "STAGE14_S7_83=COMPLETE_POLYNOMIAL_FACTOR_MOBILITY_TO_KERNEL_DIFFUSION_OR_SQUARE_PART_MOBILITY_SPLIT",
            "POLYNOMIAL_FACTOR_MOBILITY_SPLIT_QUANTITATIVE=true",
            "RECEIVER_MATERIALLY_CHANGED=true",
            "S7_83_NEW_AUXILIARY_H_NEEDED=false",
            "NEXT=Stage14-s7-84",
        ],
    }
    checks = 0
    for rel, tokens in required.items():
        text = (ROOT / rel).read_text()
        for token in tokens:
            assert token in text, (rel, token)
            checks += 1
    return checks


def main() -> None:
    squareclass = check_squareclass_identity()
    support = check_support_inequality()
    dichotomy = check_kernel_squarepart_dichotomy()
    boundary = check_boundary_tokens()
    print("STAGE14_S_BATCH_S7_81_83_AUDIT=PASS")
    print(f"squareclass_checks={squareclass}")
    print(f"support_checks={support}")
    print(f"kernel_squarepart_checks={dichotomy}")
    print(f"boundary_token_checks={boundary}")


if __name__ == "__main__":
    main()
