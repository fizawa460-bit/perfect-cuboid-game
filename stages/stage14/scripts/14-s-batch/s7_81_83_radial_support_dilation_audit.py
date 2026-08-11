#!/usr/bin/env python3
from __future__ import annotations

from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def prime_valuation(n: int, p: int) -> int:
    n = abs(n)
    v = 0
    while n and n % p == 0:
        n //= p
        v += 1
    return v


def check_radial_algebra() -> int:
    checks = 0
    primitive_pairs = [(3, 1), (5, 3), (5, 1), (7, 5), (9, 7), (8, 3)]
    for x, y in primitive_pairs:
        assert x > y > 0
        assert gcd(x, y) == 1
        for h in range(1, 25):
            X, Y = h * x, h * y
            assert gcd(X, Y) == h
            assert X * X - Y * Y == h * h * (x * x - y * y)
            assert X * X + Y * Y == h * h * (x * x + y * y)
            checks += 3

            # The signed quotient formula is used only when parity makes it integral.
            if (h * (x - y)) % 2 == 0 and (h * (x + y)) % 2 == 0:
                P = h * (x - y) // 2
                Q = h * (x + y) // 2
                assert Q + P == X
                assert Q - P == Y
                checks += 2

            D0 = x * x - y * y
            for p in (2, 3, 5, 7, 11, 13):
                assert prime_valuation(h * h * D0, p) == 2 * prime_valuation(h, p) + prime_valuation(D0, p)
                checks += 1
    return checks


def check_capacity_bound() -> int:
    checks = 0
    for x, y in ((3, 1), (5, 3), (7, 5), (8, 3)):
        for R in (32, 64, 128):
            for S in (24, 48, 96):
                hs = [
                    h
                    for h in range(1, 1000)
                    if R <= h * x < 2 * R and S <= h * y < 2 * S
                ]
                cap = 1 + min(R // x, S // y)
                # Constant-factor dyadic windows permit an absolute-constant multiple.
                assert len(hs) <= 4 * cap
                checks += 1
                if hs:
                    h0 = min(hs)
                    # A realized radial scale forces the primitive vector below raw scale.
                    assert x <= (2 * R) / h0
                    assert y <= (2 * S) / h0
                    checks += 2
    return checks


def check_boundary_tokens() -> int:
    required = {
        "stages/stage14/14-s7-81/result.md": [
            "STAGE14_S7_81=COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_CAPACITY_AND_PRIMITIVE_RAY_HEIGHT_GAP",
            "HEAVY_RAY_POLYNOMIAL_MASS_FORCES_POLYNOMIAL_RADIAL_CAPACITY=true",
            "RECEIVER_MATERIALLY_CHANGED=false",
            "NEXT=Stage14-s7-82",
        ],
        "stages/stage14/14-s7-82/result.md": [
            "STAGE14_S7_82=COMPLETE_HEAVY_RAY_RADIAL_SCALE_TO_EXACT_SQUARE_DILATE_SECOND_RECIPROCAL_PACKET",
            "HEAVY_RAY_SECOND_RECIPROCAL_SQUARE_DILATE_IDENTITY_EXACT=true",
            "RADIAL_POLYNOMIAL_MOBILITY_ENTERS_AS_H_SQUARED=true",
            "RECEIVER_MATERIALLY_CHANGED=false",
            "NEXT=Stage14-s7-83",
        ],
        "stages/stage14/14-s7-83/result.md": [
            "STAGE14_S7_83=COMPLETE_HEAVY_RAY_RADIAL_SUPPORT_TO_SQUARE_DILATE_PHYSICAL_FACTOR_ACCEPTANCE_RECEIVER",
            "RADIAL_ACCEPTANCE_IS_SQUARE_DILATE_PHYSICAL_FACTOR_SUPPORT=true",
            "CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveReciprocalRayPolynomialRadialSquareDilationPhysicalFactorSupport",
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
    algebra = check_radial_algebra()
    capacity = check_capacity_bound()
    boundary = check_boundary_tokens()
    print("STAGE14_S_BATCH_S7_81_83_AUDIT=PASS")
    print(f"radial_algebra_checks={algebra}")
    print(f"capacity_checks={capacity}")
    print(f"boundary_token_checks={boundary}")


if __name__ == "__main__":
    main()
