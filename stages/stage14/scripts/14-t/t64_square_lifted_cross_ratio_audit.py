#!/usr/bin/env python3
"""Stage14-t64: square-lifted cross-ratio / Jacobi-fibration audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T55_RESULT = ROOT / "stages/stage14/14-t55/result.md"
T63_RESULT = ROOT / "stages/stage14/14-t63/result.md"


def square_fraction(q: Fraction) -> bool:
    if q <= 0:
        return False
    a, b = q.numerator, q.denominator
    ra, rb = isqrt(a), isqrt(b)
    return ra * ra == a and rb * rb == b


def cayley(z: Fraction) -> Fraction:
    assert z != 1
    return (1 + z) / (1 - z)


def main() -> None:
    t55 = T55_RESULT.read_text()
    t63 = T63_RESULT.read_text()
    assert "STAGE14_T55=COMPLETE_SHARED_U_PROJECTIVE_TRACE_AND_CENTERED_SELECTOR_REDUCTION" in t55
    assert "STAGE14_T63=COMPLETE_TH17_CONSUMPTION_AND_TRANSVERSE_VERTICAL_DEFECT_REDUCTION" in t63

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    by_kernel = defaultdict(list)
    cross_ratio_checks = 0
    chamber_checks = 0
    mobius_checks = 0
    cayley_checks = 0
    jacobi_checks = 0
    exact_values = Counter()

    for st in reps:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        t = Fraction(a, b)
        x = Fraction(p, q)
        T = t * t
        X = x * x
        assert 0 < t < x < 1

        A = b * b * p * p - a * a * q * q
        B = b * b * q * q - a * a * p * p
        assert A > 0 and B > 0
        R = Fraction(A, B)
        assert R == (X - T) / (1 - T * X)
        assert Fraction(st["F"], 1) / R == B * B
        cross_ratio_checks += 1

        assert 0 < R < 1
        chamber_checks += 1

        kappa = st["kernel"]
        d2 = st["F"] // kappa
        d = isqrt(d2)
        assert d * d == d2
        w = Fraction(d, B)
        assert R == kappa * w * w

        s = R
        assert X == (T + s) / (1 + s * T)
        mobius_checks += 1

        assert cayley(X) == cayley(T) * cayley(s)
        lhs_int = Fraction(p * p + q * q, q * q - p * p)
        rhs_int = Fraction(a * a + b * b, b * b - a * a) * cayley(s)
        assert lhs_int == rhs_int
        cayley_checks += 1

        y = x * (1 + s * t * t)
        assert y * y == (t * t + s) * (1 + s * t * t)
        assert s not in (0, 1, -1)
        jacobi_checks += 1

        by_kernel[kappa].append(R)
        exact_values[R] += 1

    same_kernel_pair_checks = 0
    distinct_cross_ratio_same_class = 0
    for vals in by_kernel.values():
        for i, r1 in enumerate(vals):
            for r2 in vals[i + 1:]:
                assert square_fraction(r1 / r2)
                same_kernel_pair_checks += 1
                if r1 != r2:
                    distinct_cross_ratio_same_class += 1

    assert same_kernel_pair_checks > 0
    assert distinct_cross_ratio_same_class > 0

    kernel_items = list(by_kernel.items())
    cross_kernel_checks = 0
    for i, (k1, vals1) in enumerate(kernel_items):
        for k2, vals2 in kernel_items[i + 1:]:
            assert k1 != k2
            for r1 in vals1:
                for r2 in vals2:
                    assert not square_fraction(r1 / r2)
                    cross_kernel_checks += 1

    report = {
        "stage": "14-t64",
        "reciprocal_states": len(reps),
        "cross_ratio_checks": cross_ratio_checks,
        "physical_unit_interval_checks": chamber_checks,
        "mobius_transport_checks": mobius_checks,
        "cayley_product_checks": cayley_checks,
        "jacobi_square_lift_checks": jacobi_checks,
        "same_kernel_square_quotient_pair_checks": same_kernel_pair_checks,
        "cross_kernel_non_square_quotient_checks": cross_kernel_checks,
        "same_class_distinct_exact_cross_ratio_pairs": distinct_cross_ratio_same_class,
        "distinct_exact_cross_ratio_values": len(exact_values),
        "max_exact_cross_ratio_multiplicity": max(exact_values.values()),
        "identity": "R=(X-T)/(1-TX), T=t^2, X=x^2",
        "mobius": "X=(T+s)/(1+sT), s=R=kappa*w^2",
        "cayley": "C(X)=C(T)C(s)",
        "jacobi": "y^2=(t^2+s)(1+s*t^2)",
        "boundary": {
            "STAGE14_T64": "COMPLETE_SQUARE_LIFTED_CROSS_RATIO_QUOTIENT_AND_JACOBI_FIBRATION",
            "EXACT_RATIONAL_CROSS_RATIO_COORDINATE_PROVED": True,
            "FIXED_SQUARECLASS_EVEN_QUOTIENT_RATIONAL": True,
            "CAYLEY_MULTIPLICATIVE_IDENTITY_PROVED": True,
            "PHYSICAL_SQUARE_LIFT_JACOBI_QUARTIC_PROVED": True,
            "TRANSVERSE_EQUAL_SQUARECLASS_EQUALS_CROSS_RATIO_SQUARE_QUOTIENT": True,
            "SHARED_U_TRANSVERSE_JACOBI_SQUARE_LIFT_INCIDENCE_PROVED": False,
            "SHARED_U_TRANSVERSE_VERTICAL_KUMMER_DISPERSION_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH18_NEEDED": False,
            "NEXT": "Stage14-t65",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
