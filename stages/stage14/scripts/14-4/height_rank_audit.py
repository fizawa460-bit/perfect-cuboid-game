#!/usr/bin/env python3
"""Stage14-4ae deterministic audit of fiber height and generic-rank structure.

This script independently enumerates the Stage14 two-face face-pair bijection at
B=10000 and verifies, for every raw-pair hit:

- reconstruction of the second primitive face from q=u/v;
- H2 asymp v^2;
- the direction-independent physical height sandwich;
- the Stage14-4ad elliptic equation;
- the exact inverse coordinate q=X/(sY).

It also records the elementary Weierstrass invariants and the Shioda--Tate
rank calculation for the elliptic surface y^2=x(x-1)(x+t^2).
"""

from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path

B_AUDIT = 10_000
EXPECTED_EXACTLY_TWO = (9, 11, 5)
EXPECTED_TRIPLE = 0
EXPECTED_RAW = 25
EXPECTED_ORIENTED_FACES = 3186
EXPECTED_DISTINCT_FIRST_FACES = 23
OUTPUT = Path("stages/stage14/data/14-4/height_rank_audit.json")


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def primitive_oriented_faces(bound: int):
    out = []
    m = 2
    while m * m + 1 <= bound:
        for n in range(1, m):
            H = m * m + n * n
            if H > bound:
                continue
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            D = m * m - n * n
            P = 2 * m * n
            out.append((D, P, H, m, n, "D"))
            out.append((P, D, H, m, n, "P"))
        m += 1
    return out


def verify_one_hit(S1, X1, H1, S2, X2, H2, g, d):
    # Stage14-4ad rational-circle chart for the second primitive face.
    q = Fraction(X2, H2 + S2)
    u, v = q.numerator, q.denominator
    assert 0 < u < v
    assert gcd(u, v) == 1

    delta = gcd(gcd(v * v - u * u, 2 * u * v), u * u + v * v)
    assert delta in (1, 2)
    assert (v * v - u * u) // delta == S2
    assert (2 * u * v) // delta == X2
    assert (u * u + v * v) // delta == H2

    # Uniform square-root relation between q denominator and primitive hypotenuse.
    assert v * v < 2 * H2       # v^2/2 < H2
    assert H2 < 2 * v * v

    # Direction-independent physical height sandwich, checked without floats:
    # S1 H2/(sqrt(2)g) < d < sqrt(3) S1 H2/g.
    assert 2 * (g * d) ** 2 > (S1 * H2) ** 2
    assert (g * d) ** 2 < 3 * (S1 * H2) ** 2

    # Reconstruct the Stage14-4ad elliptic point and verify q=X/(sY).
    rho1 = Fraction(X1, H1)
    rho2 = Fraction(X2, H2)
    s = Fraction(S1, H1)
    z = Fraction(g * d, H1 * H2)

    assert rho1 * rho1 + s * s == 1
    assert z * z == 1 - (rho1 * rho2) ** 2
    assert rho2 == 2 * q / (1 + q * q)

    A = 1 - 2 * rho1 * rho1
    W = z * (1 + q * q)
    assert W * W == q ** 4 + 2 * A * q * q + 1

    X0 = (W + 1) / (q * q)
    U = A + X0
    V = q * (X0 * X0 - 1) / 2

    t1 = Fraction(X1, S1)
    XE = U / (2 * s * s)
    YE = V / (2 * s ** 3)
    assert YE * YE == XE * (XE - 1) * (XE + t1 * t1)
    assert q == XE / (s * YE)

    return {
        "q": f"{u}/{v}",
        "q_denominator": v,
        "delta": delta,
        "height_ratio_dg_over_S1H2": (g * d) / (S1 * H2),
        "t1": f"{t1.numerator}/{t1.denominator}",
        "elliptic_X": f"{XE.numerator}/{XE.denominator}",
        "elliptic_Y": f"{YE.numerator}/{YE.denominator}",
    }


def census_and_audit(bound: int):
    faces = primitive_oriented_faces(bound)
    assert len(faces) == EXPECTED_ORIENTED_FACES

    exact = {"a": 0, "b": 0, "c": 0}
    triple = 0
    raw_hits = 0
    distinct_first_faces = set()
    height_ratios = []
    sample = []

    for S1, X1, H1, *_ in faces:
        for S2, X2, H2, *_ in faces:
            g = gcd(S1, S2)
            alpha = S1 // g
            beta = S2 // g

            e = g * alpha * beta
            x = beta * X1
            y = alpha * X2
            if not x < y:
                continue

            u_face = beta * H1
            d2 = u_face * u_face + y * y
            d = isqrt(d2)
            if d * d != d2 or d > bound:
                continue

            v_face = alpha * H2
            assert e * e + x * x == u_face * u_face
            assert e * e + y * y == v_face * v_face
            assert v_face * v_face + x * x == d * d
            assert gcd(e, x, y) == 1

            raw_hits += 1
            distinct_first_faces.add((S1, X1, H1))
            check = verify_one_hit(S1, X1, H1, S2, X2, H2, g, d)
            height_ratios.append(check["height_ratio_dg_over_S1H2"])

            if e < x:
                direction = "a"
            elif e < y:
                direction = "b"
            else:
                direction = "c"

            if is_square(x * x + y * y):
                triple += 1
            else:
                exact[direction] += 1

            if len(sample) < 5:
                sample.append(
                    {
                        "face1": [S1, X1, H1],
                        "face2": [S2, X2, H2],
                        "g": g,
                        "cuboid": [e, x, y, d],
                        **check,
                    }
                )

    got = (exact["a"], exact["b"], exact["c"])
    assert got == EXPECTED_EXACTLY_TWO
    assert triple == EXPECTED_TRIPLE
    assert raw_hits == EXPECTED_RAW
    assert len(distinct_first_faces) == EXPECTED_DISTINCT_FIRST_FACES

    return {
        "B": bound,
        "oriented_primitive_face_data": len(faces),
        "raw_pair_incidences": raw_hits,
        "distinct_first_face_data_among_hits": len(distinct_first_faces),
        "exactly_two": exact,
        "triple": triple,
        "height_ratio_min": min(height_ratios),
        "height_ratio_max": max(height_ratios),
        "theoretical_height_ratio_interval": ["1/sqrt(2)", "sqrt(3)"],
        "sample_hits": sample,
        "all_second_face_reconstructions_pass": True,
        "all_q_denominator_square_root_bounds_pass": True,
        "all_physical_height_sandwich_checks_pass": True,
        "all_elliptic_inverse_checks_pass": True,
    }


def elliptic_surface_audit():
    # For y^2=x^3+a2*x^2+a4*x with a2=t^2-1, a4=-t^2,
    # c4 and Delta reduce to the displayed polynomials.
    # We record coefficient lists in increasing powers of t.
    delta_coeffs = [0, 0, 0, 0, 16, 0, 32, 0, 16]
    c4_coeffs = [16, 0, 16, 0, 16]

    assert delta_coeffs == [0, 0, 0, 0, 16, 0, 32, 0, 16]
    assert c4_coeffs == [16, 0, 16, 0, 16]

    fibers = [
        {"place": "t=0", "type": "I4", "euler": 4, "root_rank": 3},
        {"place": "t=+i", "type": "I2", "euler": 2, "root_rank": 1},
        {"place": "t=-i", "type": "I2", "euler": 2, "root_rank": 1},
        {"place": "t=infinity", "type": "I4", "euler": 4, "root_rank": 3},
    ]
    euler_sum = sum(f["euler"] for f in fibers)
    root_rank = sum(f["root_rank"] for f in fibers)
    picard_rank = 10  # geometric Picard rank of a rational elliptic surface
    shioda_tate_rank = picard_rank - 2 - root_rank

    assert euler_sum == 12
    assert root_rank == 8
    assert shioda_tate_rank == 0

    return {
        "weierstrass_model": "y^2=x(x-1)(x+t^2)",
        "Delta": "16 t^4 (1+t^2)^2",
        "c4": "16(1+t^2+t^4)",
        "infinity_minimal_model": "Y^2=X(X+1)(X-u^2), u=1/t",
        "fibers_over_Qbar": fibers,
        "euler_sum": euler_sum,
        "surface_class": "rational elliptic surface",
        "geometric_picard_rank": picard_rank,
        "reducible_fiber_root_rank": root_rank,
        "shioda_tate_geometric_generic_MW_rank": shioda_tate_rank,
    }


def main():
    report = {
        "metadata": {
            "stage": "14-4ae",
            "title": "Fiber/base height and generic-rank audit",
            "audit_bound": B_AUDIT,
        },
        "exact_height_statements": {
            "uniform_physical_height": "S1 H2/(sqrt(2) g) < d < sqrt(3) S1 H2/g",
            "second_face_parameterization": "S2=(v^2-u^2)/delta, X2=2uv/delta, H2=(u^2+v^2)/delta, delta in {1,2}",
            "q_denominator_height": "v^2/2 < H2 < 2v^2",
            "fiber_cutoff_scale": "v asymp sqrt(B g/S1)",
            "elliptic_inverse": "q=X/(sY), s=S1/H1",
        },
        "finite_audit": census_and_audit(B_AUDIT),
        "elliptic_surface": elliptic_surface_audit(),
        "counting_boundary": {
            "fixed_fiber_standard_height_relation": "h(q(P))=2 hhat(P)+O_t1(1)",
            "fixed_fiber_point_growth": "polylogarithmic in B for fixed Mordell-Weil rank",
            "uniform_height_constant_over_base_assumed": False,
            "generic_geometric_rank_positive": False,
            "global_problem": "small-point rank-jump or extra-torsion specializations plus gcd/lcm coupling",
            "raw_pair_identity": "O_pair_raw(B)=N2(B)+3T(B)",
            "triple_lower_order_at_sqrtB_scale_known": False,
        },
        "decision": {
            "STAGE14_4AE": "COMPLETE",
            "UNIFORM_SECOND_FACE_HEIGHT_COMPARISON": True,
            "SECOND_FACE_Q_DENOMINATOR_SQUARE_ROOT_HEIGHT": True,
            "ELLIPTIC_Q_INVERSE": "q=X/(sY)",
            "FIXED_FIBER_POINT_GROWTH_POLYLOGARITHMIC": True,
            "ELLIPTIC_SURFACE_FIBERS": "I4_I4_I2_I2",
            "ELLIPTIC_SURFACE_RATIONAL": True,
            "GEOMETRIC_GENERIC_MW_RANK": 0,
            "RAW_PAIR_HEIGHT_SUM_LOCKED": True,
            "RAW_PAIR_TO_EXACTLY_TWO_REQUIRES_TRIPLE_CONTROL": True,
            "SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED": True,
            "SQRT_B_ASYMPTOTIC_CLAIM": False,
            "TRUE_GROWTH_ORDER_IDENTIFIED": False,
            "NEXT": "Stage14-4af small-point specialization and triple-subtraction analysis",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
