#!/usr/bin/env python3
"""Stage13-7je: exact coupled square-condition / Kummer reduction.

Stage13-7jd bounded face cuboids by treating the Yoshida elliptic fibers
independently.  Here we eliminate the elliptic x-coordinate and keep both
Pythagorean parameters at once.

For Yoshida parameters s,t the elliptic equation is equivalent, away from the
standard degenerate parameters, to

    w^2 = (s^2-t^2)(s^2 t^2-1).

With U=st, V=s/t, Z=Vw this becomes

    Z^2 = (U^3-U)(V^3-V),

so the face-cuboid locus is birational to the Kummer surface attached to
E x E for E: y^2=x^3-x.  Equivalently, U and V lie in one common quadratic
twist E_D of the congruent-number curve.

This file validates the algebra exactly over Fraction samples and records the
analytic boundary: known average 2-Selmer and integral-point results are highly
relevant but do not, by themselves, count the rational points with the coupled
primitive denominator/height condition needed here.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/face_cuboid_coupled_kummer_report.json")


def alpha_of(s: Fraction, t: Fraction) -> Fraction:
    return 2*s*(s*s-1)*(1+s*t)/(s-t)


def elliptic_rhs(s: Fraction, a: Fraction) -> Fraction:
    return a*(a-4*s*s)*(a+(s*s-1)**2)


def quartic(s: Fraction, t: Fraction) -> Fraction:
    return (s*s-t*t)*(s*s*t*t-1)


def square_prefactor(s: Fraction, t: Fraction) -> Fraction:
    return 2*s*(s*s-1)*(s*s+1)/(s-t)**2


def audit(hmax: int = 24) -> dict:
    cases = 0
    factorization_failures = 0
    homogeneous_failures = 0
    kummer_failures = 0
    positive_square_cases = 0

    for u in range(2, hmax + 1):
        for v in range(1, u):
            if math.gcd(u, v) != 1:
                continue
            s = Fraction(u, v)
            for m in range(2, hmax + 1):
                for n in range(1, m):
                    if math.gcd(m, n) != 1:
                        continue
                    t = Fraction(m, n)
                    if s == t:
                        continue
                    cases += 1

                    a = alpha_of(s, t)
                    if elliptic_rhs(s, a) != square_prefactor(s, t)**2 * quartic(s, t):
                        factorization_failures += 1

                    q_num = (u*u*n*n-m*m*v*v)*(u*u*m*m-v*v*n*n)
                    q_rat = quartic(s, t)
                    if q_rat != Fraction(q_num, (v*n)**4):
                        homogeneous_failures += 1

                    U = s*t
                    V = s/t
                    lhs_factor = V*V*q_rat
                    rhs_factor = U*(U*U-1)*V*(V*V-1)
                    if lhs_factor != rhs_factor:
                        kummer_failures += 1

                    if q_num > 0:
                        r = math.isqrt(q_num)
                        if r*r == q_num:
                            positive_square_cases += 1

    return {
        "H_parameter_max": hmax,
        "reduced_positive_parameter_pairs": cases,
        "exact_factorization_failures": factorization_failures,
        "homogeneous_quartic_failures": homogeneous_failures,
        "kummer_identity_failures": kummer_failures,
        "positive_integral_square_cases": positive_square_cases,
    }


def build_report() -> dict:
    checks = audit()
    if any(checks[k] for k in (
        "exact_factorization_failures",
        "homogeneous_quartic_failures",
        "kummer_identity_failures",
    )):
        raise ArithmeticError(checks)

    return {
        "metadata": {
            "stage": "13-7je",
            "scope": (
                "exact coupled square-condition and Kummer/twist reduction; "
                "no overlap lower-order theorem is claimed"
            ),
        },
        "yoshida_elimination": {
            "elliptic_family": "beta^2=alpha(alpha-4s^2)(alpha+(s^2-1)^2)",
            "alpha": "2s(s^2-1)(1+st)/(s-t)",
            "exact_factorization": (
                "beta^2=[2s(s^2-1)(s^2+1)/(s-t)^2]^2 "
                "*(s^2-t^2)(s^2t^2-1)"
            ),
            "square_condition": "w^2=(s^2-t^2)(s^2t^2-1)",
            "degenerate_exclusions": "s,t in {0,+-1} and s=t are excluded by the nondegenerate face-cuboid construction",
        },
        "homogeneous_integer_form": {
            "parameters": "s=u/v, t=m/n with gcd(u,v)=gcd(m,n)=1",
            "condition": (
                "W^2=(u^2 n^2-m^2 v^2)(u^2 m^2-v^2 n^2)"
            ),
            "linear_factorization": (
                "W^2=(un-mv)(un+mv)(um-vn)(um+vn)"
            ),
            "denominator_note": "the rational denominator (vn)^4 is already a square, so the rational and integer square conditions are equivalent",
        },
        "kummer_transform": {
            "change": "U=st, V=s/t, Z=Vw",
            "equation": "Z^2=U(U^2-1)V(V^2-1)=(U^3-U)(V^3-V)",
            "geometry": "birational Kummer surface attached to E x E with E: y^2=x^3-x",
        },
        "quadratic_twist_interpretation": {
            "statement": (
                "For every nondegenerate rational solution there is a squarefree "
                "squareclass D such that U^3-U=D*y1^2 and V^3-V=D*y2^2."
            ),
            "twist": "E_D: Y^2=X^3-D^2 X",
            "coordinate_map": "if U^3-U=D*y^2, then (X,Y)=(DU,D^2 y) lies on E_D",
            "meaning": "face cuboids become pairs of rational points on one common congruent-number twist",
        },
        "literature_boundary": {
            "heath_brown_1993": (
                "For squarefree D in each odd residue class mod 8, the average of "
                "2^{Selmer-rank} is 3 plus a logarithmically saving error; hence "
                "the average 2^{rank} is bounded. This controls descent complexity, "
                "not the required rational-point denominator heights by itself."
            ),
            "chan_2024": (
                "The total number of non-torsion integral points on E_D for squarefree "
                "D<N is O(N(log N)^(-1/4+eps)). Our Kummer points generally have "
                "rational x-coordinates with square denominators, so an additional "
                "denominator/discriminant-lowering step is required before this theorem "
                "can close the face-cuboid count."
            ),
            "bonolis_browning_2021": (
                "Their square-sieve framework gives uniform rational-point bounds on "
                "hyperelliptic fibrations, but no direct specialization has been "
                "verified that respects the primitive coupled height below with the "
                "needed o(B(log B)^3) strength."
            ),
        },
        "remaining_problem": {
            "form": (
                "count coprime u,v,m,n satisfying the displayed four-linear-factor "
                "square condition together with the primitive coupled height from "
                "face_cuboid_primitive_height_report.json"
            ),
            "target": "F(B)=o(B(log B)^3)",
            "promising_route": (
                "average the common-twist rational points using 2-descent while "
                "retaining denominator height, or apply a square-sieve directly to "
                "the four linear factors in dyadic coupled-height boxes"
            ),
        },
        "finite_exact_checks": checks,
        "status": {
            "coupled_square_condition_exact": True,
            "kummer_self_product_identified": True,
            "congruent_number_twist_reduction_exact": True,
            "pair_overlap_lower_order_proved": False,
            "exact_one_directional_limit_identified": False,
            "next": "Stage13-7jf",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
