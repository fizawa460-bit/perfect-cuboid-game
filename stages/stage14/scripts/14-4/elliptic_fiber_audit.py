#!/usr/bin/env python3
"""Stage14-4ad deterministic audit of the elliptic-fiber reduction.

The script independently enumerates the Stage14-4ab two-face primitive-face
bijection at B=10000 and verifies the product-Pythagorean identity, normalized
square condition, Jacobi quartic and its explicit Weierstrass/Legendre-type
model for every raw-pair hit.

It also reports the frozen finite effective exponents used only as diagnostics.
"""

from fractions import Fraction
from math import gcd, isqrt, log, sqrt
import json
from pathlib import Path

B_AUDIT = 10_000
EXPECTED_EXACTLY_TWO = (9, 11, 5)
EXPECTED_TRIPLE = 0
OUTPUT = Path("stages/stage14/data/14-4/elliptic_fiber_audit.json")

FROZEN_TOTALS = [
    (100_000, 89),
    (200_000, 116),
    (500_000, 188),
    (1_000_000, 255),
    (2_000_000, 356),
]


def is_square(n: int) -> bool:
    r = isqrt(n)
    return r * r == n


def primitive_oriented_faces(bound: int):
    """Return (S,X,H,m,n,role) with H<=bound and S distinguished."""
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


def verify_fiber(S1, X1, H1, S2, X2, H2, g, d):
    """Verify all Stage14-4ad identities for one raw-pair hit."""
    # Product-Pythagorean closure.
    assert (X1 * X2) ** 2 + (g * d) ** 2 == (H1 * H2) ** 2

    rho1 = Fraction(X1, H1)
    rho2 = Fraction(X2, H2)
    s1 = Fraction(S1, H1)
    s2 = Fraction(S2, H2)
    z = Fraction(g * d, H1 * H2)

    assert rho1 * rho1 + s1 * s1 == 1
    assert rho2 * rho2 + s2 * s2 == 1
    assert z * z == 1 - (rho1 * rho2) ** 2

    # Rational unit-circle chart for the second face.
    # q=rho2/(1+s2), so rho2=2q/(1+q^2).
    q = rho2 / (1 + s2)
    assert q != 0
    assert rho2 == 2 * q / (1 + q * q)
    assert s2 == (1 - q * q) / (1 + q * q)

    # Jacobi quartic.
    A = 1 - 2 * rho1 * rho1
    W = z * (1 + q * q)
    assert W * W == q ** 4 + 2 * A * q * q + 1
    discriminant_core = A * A - 1
    assert discriminant_core == -4 * rho1 * rho1 * (1 - rho1 * rho1)
    assert discriminant_core != 0

    # Explicit Jacobi-quartic -> cubic transform.
    X0 = (W + 1) / (q * q)
    U = A + X0
    V = q * (X0 * X0 - 1) / 2
    assert 2 * V * V == U ** 3 - 2 * A * U ** 2 + (A * A - 1) * U

    # Factor with r=X1/H1, s=S1/H1 and scale to Legendre-type model.
    assert A == 2 * s1 * s1 - 1
    assert 2 * V * V == U * (U - 2 * s1 * s1) * (U + 2 * rho1 * rho1)

    t1 = Fraction(X1, S1)
    XE = U / (2 * s1 * s1)
    YE = V / (2 * s1 ** 3)
    assert YE * YE == XE * (XE - 1) * (XE + t1 * t1)

    # j(t1) is finite and varies with t1; non-isotriviality is symbolic.
    j = 256 * (1 + t1 * t1 + t1 ** 4) ** 3 / (t1 ** 4 * (1 + t1 * t1) ** 2)
    assert j > 0

    return {
        "rho1": f"{rho1.numerator}/{rho1.denominator}",
        "rho2": f"{rho2.numerator}/{rho2.denominator}",
        "t1": f"{t1.numerator}/{t1.denominator}",
        "jacobi_A": f"{A.numerator}/{A.denominator}",
        "j_invariant": f"{j.numerator}/{j.denominator}",
    }


def census_and_audit(bound: int):
    faces = primitive_oriented_faces(bound)
    exact = {"a": 0, "b": 0, "c": 0}
    triple = 0
    raw_hits = 0
    checked = 0
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

            u = beta * H1
            d2 = u * u + y * y
            d = isqrt(d2)
            if d * d != d2 or d > bound:
                continue

            v = alpha * H2
            assert e * e + x * x == u * u
            assert e * e + y * y == v * v
            assert v * v + x * x == d * d
            assert gcd(e, x, y) == 1

            raw_hits += 1
            result = verify_fiber(S1, X1, H1, S2, X2, H2, g, d)
            checked += 1
            if len(sample) < 5:
                sample.append(
                    {
                        "face1": [S1, X1, H1],
                        "face2": [S2, X2, H2],
                        "g": g,
                        "cuboid": [e, x, y, d],
                        **result,
                    }
                )

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

    got = (exact["a"], exact["b"], exact["c"])
    assert got == EXPECTED_EXACTLY_TWO
    assert triple == EXPECTED_TRIPLE
    assert raw_hits == sum(EXPECTED_EXACTLY_TWO) + 3 * EXPECTED_TRIPLE
    assert checked == raw_hits

    return {
        "B": bound,
        "oriented_primitive_face_data": len(faces),
        "raw_pair_incidences": raw_hits,
        "elliptic_fibers_checked": checked,
        "exactly_two": exact,
        "triple": triple,
        "sample_fibers": sample,
        "all_product_identities_pass": True,
        "all_normalized_square_conditions_pass": True,
        "all_jacobi_quartics_pass": True,
        "all_nonsingularity_checks_pass": True,
        "all_cubic_transforms_pass": True,
        "all_legendre_type_models_pass": True,
    }


def effective_exponents():
    adjacent = []
    for (b1, n1), (b2, n2) in zip(FROZEN_TOTALS, FROZEN_TOTALS[1:]):
        theta = log(n2 / n1) / log(b2 / b1)
        adjacent.append({"B1": b1, "B2": b2, "theta": theta})

    wider = []
    for i in range(len(FROZEN_TOTALS)):
        for j in range(i + 2, len(FROZEN_TOTALS)):
            b1, n1 = FROZEN_TOTALS[i]
            b2, n2 = FROZEN_TOTALS[j]
            theta = log(n2 / n1) / log(b2 / b1)
            wider.append({"B1": b1, "B2": b2, "theta": theta})

    late = [(b, n / sqrt(b)) for b, n in FROZEN_TOTALS if b >= 200_000]
    vals = [v for _, v in late]
    mean = sum(vals) / len(vals)
    variance = sum((v - mean) ** 2 for v in vals) / len(vals)
    cv = sqrt(variance) / mean

    return {
        "adjacent": adjacent,
        "wider": wider,
        "late_N2_over_sqrtB": [{"B": b, "value": v} for b, v in late],
        "late_mean": mean,
        "late_coefficient_of_variation": cv,
    }


def main():
    report = {
        "metadata": {
            "stage": "14-4ad",
            "title": "Elliptic-fibration square-thinning audit",
            "audit_bound": B_AUDIT,
        },
        "stage13_quantifier_boundary": {
            "local_multiplier": "lambda_p=(p+5)/(2(p+1)) for inert p=3 mod 4",
            "proof_order": "fix finite prime set; B->infinity; then number of primes -> infinity",
            "zero_density_imported": True,
            "power_saving_imported": False,
            "growing_modulus_imported": False,
        },
        "exact_structural_identities": {
            "product_pythagorean": "(X1 X2)^2 + (g d)^2 = (H1 H2)^2",
            "normalized": "1-(rho1 rho2)^2 is a rational square",
            "jacobi_quartic": "W^2=q^4+2Aq^2+1, A=1-2rho1^2",
            "cubic": "2V^2=U^3-2AU^2+(A^2-1)U",
            "elliptic_fiber": "Y^2=X(X-1)(X+t1^2)",
            "j_invariant": "256(1+t1^2+t1^4)^3/(t1^4(1+t1^2)^2)",
            "non_isotrivial": True,
        },
        "finite_audit": census_and_audit(B_AUDIT),
        "finite_growth_diagnostic": effective_exponents(),
        "decision": {
            "STAGE14_4AD": "COMPLETE",
            "PRODUCT_PYTHAGOREAN_CLOSURE_IDENTITY": True,
            "SECOND_FACE_FIXED_FIBER_GENUS": 1,
            "ELLIPTIC_FIBRATION_NON_ISOTRIVIAL": True,
            "R03_FIXED_PRIME_SIEVE_GIVES_ZERO_DENSITY": True,
            "R03_FIXED_PRIME_SIEVE_GIVES_POWER_SAVING": False,
            "SQRT_B_FINITE_CANDIDATE_SURVIVES": True,
            "SQRT_B_ASYMPTOTIC_CLAIM": False,
            "TRUE_GROWTH_ORDER_IDENTIFIED": False,
            "NEXT": "Stage14-4ae elliptic-fibration height/rank analysis",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
