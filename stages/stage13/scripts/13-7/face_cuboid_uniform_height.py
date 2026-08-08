#!/usr/bin/env python3
"""Stage13-7jd: unconditional uniform-height bound for primitive face cuboids.

Stage13-7jc reduced the exactly-one transfer to

    F(B) = o(B (log B)^3),

where F(B) counts primitive canonical integer face cuboids with space diagonal
d<=B.  This stage asks what follows unconditionally from the Yoshida elliptic
fibration plus a uniform bounded-height theorem for elliptic curves with
rational 2-torsion.

The result is a genuine global bound

    F(B) << B * exp(C log B / log log B) = B^(1+o(1)),

with an effective absolute C after harmless changes of constants.  This does
NOT imply the required o(B(log B)^3) bound, because exp(C L/log L) eventually
dominates every fixed power of L.

External theorem used:
  Marta Dujella, Uniform bounds for the number of rational points of bounded
  height on certain elliptic curves, Acta Arith. 217 (2025), 309-332,
  DOI 10.4064/aa231221-9-10; arXiv:2312.03655.

Structural bridge used:
  Takumi Yoshida, The relationship between face cuboids and elliptic curves,
  arXiv:2407.09825.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

IN_7JC = Path("stages/stage13/data/13-7/overlap_face_cuboid_reduction_report.json")
OUT = Path("stages/stage13/data/13-7/face_cuboid_uniform_height_report.json")


def build_report() -> dict:
    prev = json.loads(IN_7JC.read_text())
    assert prev["single_scalar_reduction"]["sufficient_bound"] == "F(B)=o(B(log B)^3)"

    return {
        "metadata": {
            "stage": "13-7jd",
            "scope": (
                "unconditional global face-cuboid height bound obtained from the "
                "Yoshida elliptic fibration and a uniform rational-point theorem; "
                "the exactly-one lower-order bound remains open"
            ),
        },
        "canonical_yoshida_parameters": {
            "geometry": (
                "Choose deterministically two integral faces of a primitive face cuboid. "
                "Yoshida's t is the Euclid parameter of one integral face triangle; "
                "s is the Euclid parameter of the Pythagorean triangle formed by the "
                "shared complementary edge, the second integral face diagonal, and d."
            ),
            "pythagorean_height": (
                "If d<=B and s=u/v is reduced from the primitive base of that outer "
                "Pythagorean triangle, then u^2+v^2<=B, hence H(s)<=sqrt(B). "
                "The same argument gives H(t)<=sqrt(B)."
            ),
            "number_of_possible_s": (
                "The four sign/inversion choices for s come from coprime integer pairs "
                "u,v with u^2+v^2<=B; crudely #s<=4B."
            ),
        },
        "explicit_x_height_transfer": {
            "yoshida_formula": (
                "t=(s*alpha-2*s*(s^2-1))/(alpha+2*s^2*(s^2-1))"
            ),
            "solved_formula": "alpha=2*s*(s^2-1)*(1+s*t)/(s-t)",
            "homogeneous_formula": (
                "For s=u/v, t=m/n reduced, alpha="
                "2u(u^2-v^2)(vn+um)/(v^3(un-vm))."
            ),
            "height_bound": "H(alpha)<=4 H(s)^4 H(t)<=4 B^(5/2)",
            "nonvanishing": (
                "s=t is impossible for a valid nondegenerate Yoshida point with "
                "s not in {0,+-1}; otherwise the defining relation forces "
                "2s(s^2-1)(1+s^2)=0."
            ),
        },
        "curve_height_transfer": {
            "model": (
                "E_{1,s}: y^2=x^3+(s^4-6s^2+1)x^2-4s^2(s^2-1)^2 x"
            ),
            "projective_integral_coordinates": (
                "For s=u/v, a common projective coefficient tuple is "
                "[v^6, v^2(u^4-6u^2v^2+v^4), -4u^2(u^2-v^2)^2, 0]."
            ),
            "height_bound": "H(E_{1,s})<=8 H(s)^6<=8 B^3",
            "rational_2_torsion": (
                "(0,0) is a rational point of exact order 2; in fact the cubic "
                "splits with roots 0, 4s^2, -(s^2-1)^2."
            ),
        },
        "uniform_elliptic_point_input": {
            "reference": (
                "Marta Dujella, Acta Arith. 217 (2025), 309-332, "
                "arXiv:2312.03655"
            ),
            "theorem_used": (
                "For elliptic curves over Q with a rational point of exact order 2, "
                "the number of rational points of exponential height <=X is at most "
                "exp(C log X/log log X), uniformly in the curve, once X dominates "
                "the curve height."
            ),
            "safe_height_parameter": (
                "Take X=8 B^3. This dominates both H(E_{1,s}) and H(alpha) for B>=1."
            ),
            "per_fiber_consequence": (
                "# relevant non-torsion P on E_{1,s} is <= "
                "exp(C1 log B/log log B), uniformly in eligible s."
            ),
        },
        "global_face_cuboid_bound": {
            "injection": (
                "Choose the first canonical integral-face pair and the positive outer "
                "Euclid parameter s. The resulting (s,P) determines one rational "
                "face-cuboid similarity class, so distinct primitive canonical cuboids "
                "cannot choose the same pair."
            ),
            "bound": "F(B) << B * exp(C1 log B/log log B)",
            "equivalent_form": "F(B)=B^(1+o(1))",
            "effective_constant_note": (
                "C1 is effective and absolute here because the number field is Q and "
                "the torsion prime is fixed at 2; no numerical optimization is claimed."
            ),
        },
        "comparison_with_required_overlap_bound": {
            "required": "F(B)=o(B(log B)^3)",
            "available": "F(B)<<B*exp(C1 log B/log log B)",
            "gap": (
                "For every fixed C1>0, exp(C1 L/log L)/(L^3) -> infinity. "
                "Thus the uniform worst-fiber theorem is too weak to transfer the "
                "raw asymptotic to exactly-one."
            ),
            "what_would_close": (
                "An average-over-s bound o((log B)^3) for the number of relevant "
                "points per eligible s, or a direct square-sieve/determinant estimate "
                "for the coupled (s,t) surface giving F(B)=O(B(log B)^(3-delta))."
            ),
        },
        "conditional_exact_one": prev["raw_limit_waiting_for_transfer"],
        "status": {
            "unconditional_global_face_cuboid_bound": True,
            "face_cuboid_bound": "B*exp(C log B/loglog B)",
            "face_cuboid_exponent_limsup_at_most_one": True,
            "pair_overlap_lower_order_proved": False,
            "exact_one_directional_limit_identified": False,
            "worst_fiber_uniform_height_route_sufficient": False,
            "next": "Stage13-7je",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
