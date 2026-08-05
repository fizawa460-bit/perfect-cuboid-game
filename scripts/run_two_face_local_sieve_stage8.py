#!/usr/bin/env python3
"""Run stage eight with the j-invariant reduced up to nonzero scalar content.

SymPy's polynomial gcd retains integer content.  For a rational map, a
nonzero constant common factor is harmless; only a positive-degree common
factor would change the map degree.  This wrapper replaces the symbolic
routine accordingly and then delegates to the main audit module.
"""

from __future__ import annotations

import sympy as sp

import audit_two_face_local_sieve_stage8 as stage8


def symbolic_j_map() -> dict[str, object]:
    t, s, X = sp.symbols("t s X")
    a2 = sp.expand(4 * t**2 + (1 + t**2) ** 2)
    a4 = sp.expand(4 * t**2 * (1 + t**2) ** 2)
    b2 = 4 * a2
    b4 = 2 * a4
    b6 = sp.Integer(0)
    b8 = -a4**2
    c4 = sp.factor(b2**2 - 24 * b4)
    delta = sp.factor(-b2**2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6)

    expected_c4 = 16 * (
        t**4 - 2 * t**3 + 2 * t**2 + 2 * t + 1
    ) * (
        t**4 + 2 * t**3 + 2 * t**2 - 2 * t + 1
    )
    expected_delta = 256 * t**4 * (t - 1) ** 4 * (t + 1) ** 4 * (t**2 + 1) ** 4
    if sp.expand(c4 - expected_c4) != 0:
        raise ArithmeticError("unexpected c4 factorization")
    if sp.expand(delta - expected_delta) != 0:
        raise ArithmeticError("unexpected discriminant factorization")

    raw_numerator = sp.factor(c4**3)
    raw_denominator = sp.factor(delta)
    polynomial_gcd = sp.factor(
        sp.gcd(sp.Poly(raw_numerator, t), sp.Poly(raw_denominator, t)).as_expr()
    )
    if sp.degree(polynomial_gcd, t) != 0:
        raise ArithmeticError(
            f"j numerator and denominator have a positive-degree common factor {polynomial_gcd}"
        )

    reduced = sp.cancel(raw_numerator / raw_denominator)
    numerator, denominator = (sp.factor(part) for part in sp.fraction(reduced))
    numerator_degree = sp.degree(numerator, t)
    denominator_degree = sp.degree(denominator, t)
    map_degree = max(numerator_degree, denominator_degree)
    infinity_pole_order = map_degree - denominator_degree
    if (numerator_degree, denominator_degree, map_degree, infinity_pole_order) != (24, 20, 24, 4):
        raise ArithmeticError("unexpected j-map degrees")

    transformed_rhs = sp.factor(
        s**12
        * (
            (X / s**4)
            * (X / s**4 + 4 / s**2)
            * (X / s**4 + (1 + 1 / s**2) ** 2)
        )
    )
    expected_transformed_rhs = sp.factor(X * (X + 4 * s**2) * (X + (1 + s**2) ** 2))
    if sp.factor(transformed_rhs - expected_transformed_rhs) != 0:
        raise ArithmeticError("reciprocal model at infinity did not match")

    fibers = [
        {"place": "t=0", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {"place": "t=1", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {"place": "t=-1", "ord_delta": 4, "ord_c4": 0, "kodaira_type": "I4"},
        {
            "place": "t=i",
            "field": "Q(i)",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
        },
        {
            "place": "t=-i",
            "field": "Q(i)",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
        },
        {
            "place": "t=infinity",
            "ord_delta": 4,
            "ord_c4": 0,
            "kodaira_type": "I4",
            "verification": "reciprocal minimal model equals the t=0 model",
        },
    ]

    return {
        "weierstrass_model": "y^2=x(x+4t^2)(x+(1+t^2)^2)",
        "a2": str(a2),
        "a4": str(a4),
        "c4_factorized": str(c4),
        "delta_factorized": str(delta),
        "j_factorized": f"({numerator})/({denominator})",
        "j_numerator_denominator_polynomial_gcd": str(polynomial_gcd),
        "j_common_factor_is_constant_only": True,
        "j_numerator_degree": int(numerator_degree),
        "j_denominator_degree": int(denominator_degree),
        "j_map_degree": int(map_degree),
        "infinity_pole_order": int(infinity_pole_order),
        "finite_discriminant_factors": ["t", "t-1", "t+1", "t^2+1"],
        "singular_fibers": fibers,
        "euler_number_sum": sum(int(fiber["ord_delta"]) for fiber in fibers),
        "scope_note": (
            "degree 24 is obtained from this explicit reduced rational function; it is not "
            "inferred from the K3 property alone"
        ),
    }


stage8.symbolic_j_map = symbolic_j_map

if __name__ == "__main__":
    raise SystemExit(stage8.main())
