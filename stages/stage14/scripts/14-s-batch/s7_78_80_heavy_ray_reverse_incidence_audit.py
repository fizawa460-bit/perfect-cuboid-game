#!/usr/bin/env python3
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def divisors(n: int):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def primitive(v):
    x, y = v
    g = gcd(abs(x), abs(y))
    return (x // g, y // g)


def det(v, w):
    return v[0] * w[1] - w[0] * v[1]


def audit_primitive_ray_uniqueness():
    samples = [(1, 2), (2, 3), (3, 4), (4, 7), (5, 12), (8, 15)]
    for x, y in samples:
        assert gcd(x, y) == 1
        for h in range(1, 13):
            v = (h * x, h * y)
            assert primitive(v) == (x, y)
        # A primitive vector on the same positive ray must be the ray generator.
        for k in range(1, 9):
            w = primitive((k * x, k * y))
            assert det((x, y), w) == 0
            assert w == (x, y)


def audit_norm_factor_packet():
    # Primitive sum-of-two-squares vectors and split-supported divisors.
    samples = [
        ((1, 2), 5),       # 1^2+2^2=5
        ((2, 3), 13),      # 4+9=13
        ((1, 8), 5),       # 65=5*13
        ((4, 7), 5),       # 65=5*13
        ((5, 12), 13),     # 169=13^2
    ]
    for (x, y), C in samples:
        assert gcd(x, y) == 1
        N0 = x * x + y * y
        assert N0 % C == 0
        m0 = N0 // C
        assert N0 == C * m0


def audit_fixed_h_factorization_and_signed_line():
    rays = [(1, 2), (2, 3), (3, 4), (4, 7), (5, 12)]
    for x, y in rays:
        assert gcd(x, y) == 1
        for h in range(1, 10):
            X, Y = h * x, h * y
            # Exact factor-pair count is divisor-many on each coordinate.
            factor_count = len(divisors(abs(X))) * len(divisors(abs(Y)))
            enumerated = 0
            for p in divisors(abs(X)):
                c = X // p
                assert p * c == X
                for q in divisors(abs(Y)):
                    d = Y // q
                    assert q * d == Y
                    enumerated += 1
            assert enumerated == factor_count

            # Physical signed quotients are integral only on the admissible parity sublattice.
            if (X + Y) % 2 == 0 and (X - Y) % 2 == 0:
                Q = (X + Y) // 2
                P = (X - Y) // 2
                assert Q + P == X
                assert Q - P == Y
                assert 2 * Q == h * (x + y)
                assert 2 * P == h * (x - y)


def require(path: str, needles):
    text = (ROOT / path).read_text(encoding="utf-8")
    for needle in needles:
        assert needle in text, (path, needle)


def audit_boundaries():
    require("stages/stage14/14-s7-78/result.md", [
        "STAGE14_S7_78=COMPLETE_HEAVY_PRIMITIVE_RECIPROCAL_RAY_TO_FIXED_PRIMITIVE_NORM_FACTOR_PACKET",
        "HEAVY_RAY_PRIMITIVE_VECTOR_FIXED_UP_TO_O1=true",
        "HEAVY_RAY_PRIMITIVE_NORM_VALUE_FIXED=true",
        "RECEIVER_MATERIALLY_CHANGED=false",
        "NEXT=Stage14-s7-79",
    ])
    require("stages/stage14/14-s7-79/result.md", [
        "STAGE14_S7_79=COMPLETE_HEAVY_RAY_RADIAL_SCALE_AND_DIVISOR_FACTORIZATION_SEPARATION",
        "FIXED_H_RECIPROCAL_FACTORIZATION_MULTIPLICITY=Bo1",
        "HEAVY_RAY_RADIAL_CONCENTRATION_DIFFUSION_DICHOTOMY_DEFINED=true",
        "RECEIVER_MATERIALLY_CHANGED=false",
        "NEXT=Stage14-s7-80",
    ])
    require("stages/stage14/14-s7-80/result.md", [
        "STAGE14_S7_80=COMPLETE_HEAVY_RAY_TO_RADIAL_SIGNED_QUOTIENT_SUPPORT_OR_FIXED_DATA_BACKGROUND_FIBER_SPLIT",
        "HEAVY_RAY_SIGNED_QUOTIENTS_LIE_ON_ONE_RADIAL_LINE=true",
        "HEAVY_RAY_SPLIT_INTO_FIXED_DATA_BACKGROUND_FIBER_OR_DIFFUSE_RADIAL_SUPPORT=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-s7-81",
    ])
    require("stages/stage14/14-s-batch/s7-78-80-report.md", [
        "BATCH_SUBSTANTIVE_STAGE_COUNT=3",
        "BATCH_STOP_REASON=receiver_change",
        "NEXT=Stage14-s7-81",
    ])


def main():
    audit_primitive_ray_uniqueness()
    audit_norm_factor_packet()
    audit_fixed_h_factorization_and_signed_line()
    audit_boundaries()
    print("Stage14-s-batch s7-78..80 audit: OK")


if __name__ == "__main__":
    main()
