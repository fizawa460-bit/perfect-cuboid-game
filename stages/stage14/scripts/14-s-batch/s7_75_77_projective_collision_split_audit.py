#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-74/result.md': [
        'POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true',
        'NEXT=Stage14-s7-75',
    ],
    'stages/stage14/14-4ej/result.md': [
        'CENTERED_ROOT_LINE_HAS_EXACT_MULTIPLICATIVE_CHARACTER_EXPANSION=true',
        'POLYNOMIAL_CORE_DISCREPANCY_IS_VARIABLE_MODULUS_CHARACTER_CORRELATION=true',
    ],
    'stages/stage14/14-4ek/result.md': [
        'FIXED_C_CHARACTER_ENERGY_PROJECTIVE_COLLISION_IDENTITY_EXACT=true',
        'POLYNOMIAL_CORE_DISCREPANCY_SPLIT_INTO_CONCENTRATED_OR_DIFFUSE_MODULUS=true',
    ],
    'stages/stage14/14-Work-bnX26/result.md': [
        'COMMON_CORRELATION_ONLY_OBSTRUCTION_LANGUAGE_PROVED=true',
        'S_ROUTE_POLYNOMIAL_CORE_CENTERED_DISCREPANCY_IS_MINIMAL_RECIPROCAL_RECEIVER=true',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Primitive integer vectors with zero determinant represent the same projective ray.
primitive = []
for x in range(-12, 13):
    for y in range(-12, 13):
        if x == 0 and y == 0:
            continue
        if gcd(abs(x), abs(y)) == 1:
            primitive.append((x, y))

for x1, y1 in primitive:
    for x2, y2 in primitive:
        if x1 * y2 - x2 * y1 != 0:
            continue
        # For primitive vectors exact proportionality is only sign equality.
        assert (x2, y2) in ((x1, y1), (-x1, -y1))

# Ray-energy inequality: sum m(m-1) <= max(m) * sum(m).
profiles = [
    [1, 1, 1],
    [7, 1, 2],
    [15, 15, 1, 1],
    [100, 3, 2, 1],
]
for ms in profiles:
    M = sum(ms)
    mmax = max(ms)
    Kray = sum(m * (m - 1) for m in ms)
    assert Kray <= mmax * M

# Nonzero projective collisions at fixed modulus are determinant movers Delta=k*C.
for C in (5, 13, 17):
    found = False
    for x1, y1 in primitive:
        if gcd(C, x1 * y1) != 1:
            continue
        for x2, y2 in primitive:
            if gcd(C, x2 * y2) != 1:
                continue
            delta = x1 * y2 - x2 * y1
            if delta and delta % C == 0:
                assert delta == (delta // C) * C
                assert delta // C != 0
                found = True
                break
        if found:
            break
    assert found, C

for rel, needles in {
    'stages/stage14/14-s7-75/result.md': [
        'DIAGONAL_COLLISIONS_CANNOT_SUPPORT_CONCENTRATED_SATURATION=true',
        'CONCENTRATED_SATURATION_FORCES_OFFDIAGONAL_PROJECTIVE_COLLISION_DENSITY_EXPONENT_ZERO=true',
        'NEXT=Stage14-s7-76',
    ],
    'stages/stage14/14-s7-76/result.md': [
        'ZERO_DETERMINANT_COLLISION_IFF_SAME_PRIMITIVE_PROJECTIVE_RAY=true',
        'OFFDIAGONAL_COLLISION_RAY_MOVER_DECOMPOSITION_EXACT=true',
        'NEXT=Stage14-s7-77',
    ],
    'stages/stage14/14-s7-77/result.md': [
        'LARGE_REPEATED_RAY_ENERGY_FORCES_HEAVY_PRIMITIVE_RAY=true',
        'NON_HEAVY_RAY_SATURATION_FORCES_GENUINE_MOVER_ENERGY=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
        'NEXT=Stage14-s7-78',
    ],
}.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

print({
    'stage_batch': '14-s7-75..77',
    'primitive_vectors_checked': len(primitive),
    'ray_energy_profiles_checked': len(profiles),
    'receiver_change_at': 'Stage14-s7-77',
    'next': 'Stage14-s7-78',
})
