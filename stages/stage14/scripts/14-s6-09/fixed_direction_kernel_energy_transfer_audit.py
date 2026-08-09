#!/usr/bin/env python3
"""Deterministic audit for Stage14-s6-09.

Checks on actual physical ordered edges through d<=50,000:
- exact identification of the s6 cross-square with the merged t36 quartic;
- physical target squareclass is exactly [-1];
- branch-point nondegeneracy;
- fixed-F2 fibers map injectively to primitive F3 slopes;
- every pair inside one physical fixed-F2 fiber is a t36 same-squareclass collision;
- exponent ledger for the active-direction barrier.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S607 = ROOT / 'stages/stage14/scripts/14-s6-07/dual_half_angle_gcd_matrix_audit.py'
T36 = ROOT / 'stages/stage14/14-t36/result.md'
S608 = ROOT / 'stages/stage14/14-s6-08/result.md'
BL = ROOT / 'stages/stage14/14-4bl/result.md'


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def main():
    # Locked merged-predecessor boundaries.
    t36 = T36.read_text()
    s608 = S608.read_text()
    bl = BL.read_text()
    assert 'STAGE14_T36=COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_AND_FIBER_SQRT_SAVING' in t36
    assert 'FIXED_DIRECTION_SQUARECLASS_ENERGY=J*B^o(1)' in t36
    assert 'STAGE14_S6_08=COMPLETE_NORMALIZED_CROSS_SQUARE_RESONANCE_AND_KERNEL_COLLISION_RECEIVER' in s608
    assert 'NORMALIZED_BIQUADRATIC_KERNEL_COLLISION_EXACT=true' in s608
    assert 'STAGE14_4BL=DUAL_COMPACT_HALF_ANGLE_CRITICAL_SQUARE_REDUCTION' in bl
    assert 'SMALL_PARTNER_LEG_EDGE_BOUND=B^(20/21+o(1))' in bl

    mod = runpy.run_path(str(S607))
    rows = mod['ordered_physical_edges']()
    audit_row = mod['audit_row']
    half_angles = mod['half_angles']
    assert rows

    direction_slopes = {}
    quartic_checks = 0
    collision_checks = 0

    for F1, F2, space_d in rows:
        out = audit_row(F1, F2, space_d)
        F3 = out['F3']
        _, a, b = half_angles(F2)
        _, c, d = half_angles(F3)

        assert a > 0 and b > 0 and c > 0 and d > 0
        assert a != b and c != d

        # s6-08 raw cross-square.
        delta0 = (
            (a * d - b * c)
            * (a * d + b * c)
            * (b * d - a * c)
            * (b * d + a * c)
        )
        assert delta0 > 0 and is_square(delta0)

        # Exact t36 quartic at (p,q)=(c,d).
        fab = (b * b * c * c - a * a * d * d) * (
            b * b * d * d - a * a * c * c
        )
        assert fab == -delta0
        assert fab < 0 and is_square(-fab)
        quartic_checks += 1

        # No branch point: c/d != +-a/b, +-b/a.  All variables positive,
        # so it is enough to exclude the two positive roots.
        assert b * c != a * d
        assert a * c != b * d

        # Primitive transferred face slope is a bounded-multiplicity lift.
        x = Fraction(c, d)
        key = (F2, a, b)
        direction_slopes.setdefault(key, set())
        assert x not in direction_slopes[key], ('duplicate F3 slope in physical fiber', key, x)
        direction_slopes[key].add(x)

    # Every pair of physical slopes in one fixed direction has the same
    # squareclass [-1], so the product of their t36 quartic values is square.
    for (F2, a, b), slopes in direction_slopes.items():
        vals = []
        for x in slopes:
            p, q = x.numerator, x.denominator
            val = (b * b * p * p - a * a * q * q) * (
                b * b * q * q - a * a * p * p
            )
            assert val < 0 and is_square(-val)
            vals.append(val)
        for i in range(len(vals)):
            for j in range(i, len(vals)):
                assert vals[i] * vals[j] > 0
                assert is_square(vals[i] * vals[j])
                collision_checks += 1

    max_fiber = max(len(v) for v in direction_slopes.values())

    # Exact exponent ledger.
    assert Fraction(1, 1) - Fraction(41, 42) == Fraction(1, 42)
    assert Fraction(41, 42) - Fraction(20, 21) == Fraction(1, 42)
    assert Fraction(41, 42) - Fraction(1, 2) == Fraction(10, 21)

    print(f'ordered physical incidences audited={len(rows)}')
    print(f'fixed F2 direction fibers={len(direction_slopes)}')
    print(f'max frozen physical F3 multiplicity={max_fiber}')
    print(f'exact t36 quartic identifications={quartic_checks}')
    print(f'within-fiber squareclass collision checks={collision_checks}')
    print('MERGED_T36_BOUNDARY_AUDIT=true')
    print('MERGED_S6_08_BOUNDARY_AUDIT=true')
    print('MERGED_4BL_BOUNDARY_AUDIT=true')
    print('S6_T36_QUARTIC_ISOMORPHISM_AUDIT=true')
    print('PHYSICAL_TARGET_SQUARECLASS_MINUS_ONE_AUDIT=true')
    print('FIXED_DIRECTION_BRANCH_NONDEGENERACY_AUDIT=true')
    print('PHYSICAL_F3_SLOPE_INJECTIVITY_AUDIT=true')
    print('FIXED_DIRECTION_SAME_SQUARECLASS_COLLISION_AUDIT=true')
    print('ACTIVE_DIRECTION_EXPONENT_LEDGER_AUDIT=true')
    print('ALL_AUDITS_PASS=true')


if __name__ == '__main__':
    main()
