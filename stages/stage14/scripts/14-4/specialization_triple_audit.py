#!/usr/bin/env python3
"""Stage14-4af deterministic audit.

Checks the Pythagorean-base change, rational 4-torsion boundary points,
physical raw-pair non-8-torsion at B=10000, and the fixed-base triple
fiber-product branch geometry used in the Stage14-4af proof note.
"""

from collections import defaultdict
from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path

B_AUDIT = 10_000
EXPECTED_EXACTLY_TWO = (9, 11, 5)
EXPECTED_TRIPLE = 0
OUTPUT = Path("stages/stage14/data/14-4/specialization_triple_audit.json")


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


def ec_add(P, Q, t):
    """Group law on Y^2=X^3+(t^2-1)X^2-t^2 X."""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    a2 = t * t - 1
    a4 = -t * t
    if x1 == x2 and y1 == -y2:
        return None
    if P == Q:
        if y1 == 0:
            return None
        slope = (3 * x1 * x1 + 2 * a2 * x1 + a4) / (2 * y1)
    else:
        if x1 == x2:
            return None
        slope = (y2 - y1) / (x2 - x1)
    x3 = slope * slope - a2 - x1 - x2
    y3 = -y1 + slope * (x1 - x3)
    return x3, y3


def ec_mul(n, P, t):
    R = None
    Q = P
    while n:
        if n & 1:
            R = ec_add(R, Q, t)
        Q = ec_add(Q, Q, t)
        n >>= 1
    return R


def elliptic_point(S1, X1, H1, S2, X2, H2, g, d):
    rho1 = Fraction(X1, H1)
    s1 = Fraction(S1, H1)
    rho2 = Fraction(X2, H2)
    s2 = Fraction(S2, H2)
    z = Fraction(g * d, H1 * H2)

    q = rho2 / (1 + s2)
    A = 1 - 2 * rho1 * rho1
    W = z * (1 + q * q)
    X0 = (W + 1) / (q * q)
    U = A + X0
    V = q * (X0 * X0 - 1) / 2

    t = Fraction(X1, S1)
    X = U / (2 * s1 * s1)
    Y = V / (2 * s1 ** 3)
    assert Y * Y == X * (X - 1) * (X + t * t)
    assert q == X / (s1 * Y)
    return t, q, (X, Y)


def fracstr(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


def run_audit(bound: int):
    faces = primitive_oriented_faces(bound)

    pythagorean_base_checks = 0
    torsion_boundary_checks = 0
    triple_branch_checks = 0

    for S1, X1, H1, *_ in faces:
        t = Fraction(X1, S1)
        h = Fraction(H1, S1)
        s = Fraction(S1, H1)
        u = Fraction(X1, H1 + S1)

        # Rational parametrization of the Pythagorean base.
        assert 0 < u < 1
        assert t == 2 * u / (1 - u * u)
        assert h == (1 + u * u) / (1 - u * u)
        assert h * h == 1 + t * t
        pythagorean_base_checks += 1

        # Explicit rational halves of (1,0).  Their q-images are boundary q=+/-1.
        for eps in (1, -1):
            x4 = 1 + eps * h
            y4 = h * x4
            P4 = (x4, y4)
            assert ec_mul(2, P4, t) == (Fraction(1), Fraction(0))
            assert ec_mul(4, P4, t) is None
            assert x4 / (s * y4) == 1
            assert x4 / (s * (-y4)) == -1
            torsion_boundary_checks += 1

        # Space and third-face quartics are nonsingular with disjoint branch sets.
        A = (1 - t * t) / (1 + t * t)
        C = 2 / (t * t) - 1
        assert A * A != 1
        assert t != 1  # t=1 is not a rational Pythagorean slope.
        assert C * C != 1
        assert A - C == -Fraction(2, 1) / (t * t * (1 + t * t))
        triple_branch_checks += 1

    exact = {"a": 0, "b": 0, "c": 0}
    triple = 0
    raw = 0
    unique_bases = set()
    per_base = defaultdict(int)
    q_denominators = []
    all_physical_hits_not_killed_by_8 = True
    samples = []

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

            face_diag = beta * H1
            d2 = face_diag * face_diag + y * y
            d = isqrt(d2)
            if d * d != d2 or d > bound:
                continue

            raw += 1
            t, q, P = elliptic_point(S1, X1, H1, S2, X2, H2, g, d)
            assert 0 < q < 1
            if ec_mul(8, P, t) is None:
                all_physical_hits_not_killed_by_8 = False

            base = (S1, X1, H1)
            unique_bases.add(base)
            per_base[base] += 1
            q_denominators.append(q.denominator)

            if e < x:
                direction = "a"
            elif e < y:
                direction = "b"
            else:
                direction = "c"

            third = is_square(x * x + y * y)
            if third:
                triple += 1
            else:
                exact[direction] += 1

            if len(samples) < 6:
                samples.append(
                    {
                        "F1": [S1, X1, H1],
                        "F2": [S2, X2, H2],
                        "g": g,
                        "cuboid": [e, x, y, d],
                        "t1": fracstr(t),
                        "q": fracstr(q),
                        "q_denominator": q.denominator,
                        "eight_P_is_identity": ec_mul(8, P, t) is None,
                        "third_face_square": third,
                    }
                )

    got = (exact["a"], exact["b"], exact["c"])
    assert got == EXPECTED_EXACTLY_TWO
    assert triple == EXPECTED_TRIPLE
    assert raw == sum(EXPECTED_EXACTLY_TWO) + 3 * EXPECTED_TRIPLE

    report = {
        "metadata": {
            "stage": "14-4af",
            "title": "Pythagorean-base specialization and triple-fiber audit",
            "audit_bound": bound,
        },
        "pythagorean_base_change": {
            "parameter": "u=X1/(H1+S1), t1=2u/(1-u^2), H1/S1=(1+u^2)/(1-u^2)",
            "degree": 2,
            "branch_values_in_t": ["+i", "-i"],
            "pulled_back_singular_fibers": [
                {"u": "0", "type": "I4"},
                {"u": "infinity", "type": "I4"},
                {"u": "+1", "type": "I4"},
                {"u": "-1", "type": "I4"},
                {"u": "+i", "type": "I4"},
                {"u": "-i", "type": "I4"},
            ],
            "euler_sum": 24,
            "surface_type": "K3",
            "trivial_lattice_rank": 20,
            "geometric_picard_upper_bound": 20,
            "shioda_tate_geometric_MW_rank": 0,
            "interpretation": "rank zero persists after restricting the base to rational Pythagorean slopes",
        },
        "torsion_gate": {
            "curve": "E_t: Y^2=X(X-1)(X+t^2), with h^2=1+t^2 rational",
            "rational_2_torsion": ["(0,0)", "(1,0)", "(-t^2,0)"],
            "rational_4_torsion": "halves of (1,0): X=1+/-h; their q-images are +/-1 boundary points",
            "no_8_torsion_argument": "8-torsion would force h-1,h,h+1 to be rational squares, a 3-term square AP of common difference 1; equivalently a rational right triangle of area 1, impossible by Fermat",
            "mazur_consequence": "E_t(Q)_tors = Z/2 x Z/4 for every genuine Pythagorean base",
            "physical_consequence": "every physical q in (0,1) is non-torsion, hence every raw Stage14 pair lies on a positive-rank specialization",
        },
        "triple_gate": {
            "space_quartic": "W^2=q^4+2Aq^2+1, A=(1-t^2)/(1+t^2)",
            "third_face_quartic": "R^2=q^4+2Cq^2+1, C=2/t^2-1",
            "coefficient_difference": "A-C=-2/(t^2(1+t^2)) != 0",
            "branch_sets": "4+4 simple and disjoint branch points",
            "fiber_product_cover_degree": 4,
            "riemann_hurwitz": "2g-2=4*(-2)+8*2=8",
            "fixed_base_triple_genus": 5,
            "finiteness": "Faltings implies finitely many rational triple points for each fixed first face",
            "global_warning": "no uniform genus-5 point bound over the moving base is imported",
        },
        "finite_audit": {
            "oriented_primitive_faces": len(faces),
            "pythagorean_base_checks": pythagorean_base_checks,
            "torsion_boundary_checks": torsion_boundary_checks,
            "triple_branch_checks": triple_branch_checks,
            "raw_pair_incidences": raw,
            "exactly_two": exact,
            "triple": triple,
            "distinct_first_face_fibers_with_hits": len(unique_bases),
            "raw_hit_multiplicity_over_distinct_first_faces": sorted(per_base.values(), reverse=True),
            "q_denominator_min": min(q_denominators),
            "q_denominator_max": max(q_denominators),
            "all_physical_hits_not_killed_by_8": all_physical_hits_not_killed_by_8,
            "samples": samples,
        },
        "literature_boundary": {
            "halbeisen_hungerbuehler_2022": "adjacent positive-rank/torsion framework for Pythagorean-pair elliptic curves; not the Stage14 signed lcm-height family",
            "love_2024": "adjacent root-number/product-of-slopes family y^2=x(x+1)(x+t^2); not imported as a Stage14 rank-frequency theorem",
            "novelty_claim": False,
        },
        "decision": {
            "STAGE14_4AF": "COMPLETE",
            "PYTHAGOREAN_BASE_CHANGE_K3": True,
            "PYTHAGOREAN_BASE_GENERIC_MW_RANK": 0,
            "TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES": True,
            "PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION": True,
            "TRIPLE_FIXED_BASE_GENUS": 5,
            "TRIPLE_FIXED_BASE_RATIONAL_POINTS_FINITE": True,
            "SQRT_B_FINITE_CANDIDATE_SURVIVES": True,
            "SQRT_B_ASYMPTOTIC_CLAIM": False,
            "TRUE_GROWTH_ORDER_IDENTIFIED": False,
            "NEXT": "Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control",
        },
    }
    return report


def main():
    report = run_audit(B_AUDIT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
