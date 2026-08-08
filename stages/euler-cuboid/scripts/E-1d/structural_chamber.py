#!/usr/bin/env python3
"""E-1d: structural explanation of the Euler-side directional profile.

This audit records the leading raw-incidence mechanism under the locked Euler
counting convention

    0 < a < b < c,
    gcd(a,b,c)=1,
    a^2+b^2+c^2 <= B^2,

without requiring the space diagonal to be integral.

For a distinguished integral face q, introduce its face hypotenuse p and the
single quadratic equation

    F_q = x_i^2+x_j^2-p^2 = 0.

Eliminating p at the real place gives the Gelfand--Leray factor 1/(2p).
Writing (a,b,c)=r*omega on the positive sphere turns this into

    (r / (2 s_q(omega))) dr d_sigma,
    s_q(omega)=sqrt(omega_i^2+omega_j^2).

Thus the angular factor is exactly the same

    w_q(omega)=1/s_q(omega)

that appears in the Stage13 space-diagonal-side chamber calculation.

The standard primitive-Pythagorean / totient summation then gives the Euler
raw scale B^2 log B and common arithmetic coefficient 6/pi^4:

    A_q(B) ~ [6 I_q/pi^4] B^2 log B.

This script numerically recomputes the chamber integrals, checks the constant
ledger, and compares the E-1c finite exact-one profile to the resulting chamber
vector.  It does NOT prove the lower-order pair-overlap estimate needed to
transfer the raw theorem to exactly-one; that is left for E-1e.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

STAGE13_GEOM = Path("stages/stage13/data/13-3/geometric_chamber_report.json")
E1C = Path("stages/euler-cuboid/data/E-1c/scaling_report.json")
OUT = Path("stages/euler-cuboid/data/E-1d/structural_chamber_report.json")
Q = ("ab", "ac", "bc")


def simpson(f, a: float, b: float, n: int) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return total * h / 3.0


def theta_max(phi: float) -> float:
    # y<z on the canonical sphere chamber gives tan(theta)<csc(phi).
    return math.atan(1.0 / math.sin(phi))


def chamber_integrals(n_phi: int = 320, n_theta: int = 320) -> dict[str, float]:
    lo = math.pi / 4.0
    hi = math.pi / 2.0

    # For ab, w_ab=1/sin(theta) and d_sigma=sin(theta)dtheta dphi,
    # so the theta integrand is exactly 1.
    I_ab = simpson(theta_max, lo, hi, n_phi)

    def inner(phi: float, q: str) -> float:
        tmax = theta_max(phi)

        def f(theta: float) -> float:
            st = math.sin(theta)
            ct = math.cos(theta)
            cp = math.cos(phi)
            sp = math.sin(phi)
            x = st * cp
            y = st * sp
            z = ct
            if q == "ac":
                s = math.sqrt(x * x + z * z)
            elif q == "bc":
                s = math.sqrt(y * y + z * z)
            else:
                raise ValueError(q)
            return st / s

        return simpson(f, 0.0, tmax, n_theta)

    I_ac = simpson(lambda p: inner(p, "ac"), lo, hi, n_phi)
    I_bc = simpson(lambda p: inner(p, "bc"), lo, hi, n_phi)
    return {"ab": I_ab, "ac": I_ac, "bc": I_bc}


def build_report() -> dict:
    stage13 = json.loads(STAGE13_GEOM.read_text())
    e1c = json.loads(E1C.read_text())

    I_num = chamber_integrals()
    I_ref = {
        "ab": float(stage13["numerical_chamber_integrals"]["I_ab"]),
        "ac": float(stage13["numerical_chamber_integrals"]["I_ac"]),
        "bc": float(stage13["numerical_chamber_integrals"]["I_bc"]),
    }
    for q in Q:
        assert abs(I_num[q] - I_ref[q]) < 2e-9

    I_sum = sum(I_ref.values())
    assert abs(I_sum - math.pi**2 / 8.0) < 1e-13

    directional_constants = {q: 6.0 * I_ref[q] / math.pi**4 for q in Q}
    total_constant = 3.0 / (4.0 * math.pi**2)
    assert abs(sum(directional_constants.values()) - total_constant) < 1e-14

    proportion = {q: I_ref[q] / I_sum for q in Q}
    ratio = {q: proportion[q] / proportion["bc"] for q in Q}

    stage13_prop = stage13["numerical_chamber_integrals"]["proportion"]
    for q in Q:
        assert abs(proportion[q] - float(stage13_prop[q])) < 2e-15

    finite = []
    for row in e1c["rows"]:
        exact = row["exact_one"]
        total = sum(int(exact[q]) for q in Q)
        p = {q: int(exact[q]) / total for q in Q}
        scaled = {
            q: int(exact[q]) / (row["B"] ** 2 * math.log(row["B"])) for q in Q
        }
        finite.append(
            {
                "B": int(row["B"]),
                "exact_one_proportion": p,
                "distance_to_predicted_chamber": {
                    "l1": sum(abs(p[q] - proportion[q]) for q in Q),
                    "linf": max(abs(p[q] - proportion[q]) for q in Q),
                },
                "scaled_exact_one_over_predicted_raw_constant": {
                    q: scaled[q] / directional_constants[q] for q in Q
                },
                "total_scaled_over_predicted_raw_total_constant": (
                    total / (row["B"] ** 2 * math.log(row["B"])) / total_constant
                ),
            }
        )

    l1s = [row["distance_to_predicted_chamber"]["l1"] for row in finite]
    strictly_decreasing = all(b < a for a, b in zip(l1s, l1s[1:]))

    return {
        "metadata": {
            "stage": "E-1d",
            "scope": "Euler-side raw directional structural asymptotic and chamber mechanism",
            "counting": "primitive canonical 0<a<b<c with a^2+b^2+c^2<=B^2",
            "space_diagonal_integrality_required": False,
        },
        "real_place_gelfand_leray": {
            "one_face_equation": "F_q=x_i^2+x_j^2-p^2=0",
            "eliminate_positive_p": "delta(F_q) dp gives factor 1/(2p)",
            "spherical_change": "(a,b,c)=r*omega, p=r*s_q(omega), da db dc=r^2 dr d_sigma",
            "measure": "dmu_q = [r/(2 s_q(omega))] dr d_sigma",
            "radial_integral_0_to_B": "B^2/[4 s_q(omega)]",
            "angular_weight": "w_q(omega)=1/s_q(omega)",
            "canonical_chamber": "R={omega in S^2:0<x<y<z}",
            "same_angular_weight_as_stage13": True,
        },
        "arithmetic_scale_ledger": {
            "primitive_face": "(u,v,h) primitive Pythagorean; every integral face is k(u,v,h)",
            "third_edge_primitivity": "gcd(ku,kv,z)=1 iff gcd(k,z)=1",
            "coprime_third_edge_density": "phi(k)/k",
            "totient_mean": "sum_{k<=X} phi(k)/k ~ (6/pi^2) X",
            "semicircle_radial_integral": "integral_0^1 sqrt(1-t^2) dt = pi/4",
            "primitive_pythagorean_count": "P(H) ~ H/(2pi)",
            "harmonic_primitive_sum": "sum_{primitive h<=B} 1/h ~ (1/(2pi)) log B",
            "full_positive_octant_ordered_face_count": "~ [3/(2 pi^2)] B^2 log B",
            "canonical_projection": "full ordered distinguished-face count = 2*(A_ab+A_ac+A_bc)",
            "canonical_raw_total": "A_total(B) ~ [3/(4 pi^2)] B^2 log B",
        },
        "chamber_integrals": {
            "numerical_recompute": I_num,
            "stage13_reference": I_ref,
            "sum": I_sum,
            "sum_identity": "pi^2/8",
            "full_positive_octant_identity": "2*(I_ab+I_ac+I_bc)=pi^2/4",
        },
        "raw_directional_theorem": {
            "scale": "B^2 log B",
            "categorywise": {
                q: f"A_{q}(B) ~ [6 I_{q}/pi^4] B^2 log B" for q in Q
            },
            "numeric_constants": directional_constants,
            "total": "A_total(B) ~ [3/(4 pi^2)] B^2 log B",
            "total_numeric_constant": total_constant,
            "normalized_limit": proportion,
            "bc_normalized_ratio": ratio,
        },
        "space_diagonal_comparison": {
            "euler_side": "A_q^E(B) ~ [6 I_q/pi^4] B^2 log B",
            "stage13_side": "A_q^S(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3",
            "shared_directional_factor": "I_q",
            "different_common_scale_and_arithmetic_factor": True,
            "interpretation": (
                "Imposing integral space diagonal changes the common radial/arithmetic "
                "density and growth scale, but the leading canonical real-place "
                "directional weight remains 1/s_q and hence the normalized chamber vector."
            ),
        },
        "finite_exact_one_diagnostic": {
            "rows": finite,
            "l1_distance_to_chamber_strictly_decreases_over_E1c_cutoffs": strictly_decreasing,
            "warning": (
                "These rows are exactly-one counts while the proved E-1d leading formula "
                "is for raw one-face incidences.  Pair-overlap lower order is not proved "
                "in E-1d, so the finite comparison is diagnostic only."
            ),
        },
        "remaining_gap": {
            "pair_overlap_lower_order_needed": "O_qr(B)=o(B^2 log B)",
            "triple_overlap_then_lower_order": True,
            "exact_one_transfer_proved_in_E1d": False,
            "suggested_route": (
                "fixed-prime quadratic-residue sieve inside the Euler raw incidence "
                "population, analogous in architecture to Stage13-7jf but with the "
                "simpler one-face raw parameterization"
            ),
        },
        "status": {
            "E_1D_complete": True,
            "completion_level": "RAW_DIRECTIONAL_STRUCTURAL_ASYMPTOTIC",
            "raw_scale_identified": True,
            "raw_directional_constants_identified": True,
            "raw_normalized_limit_equals_stage13_chamber": True,
            "space_diagonal_integrality_changes_absolute_scale_not_Iq_factor": True,
            "pair_overlap_lower_order_proved": False,
            "exact_one_directional_limit_proved": False,
            "next": "E-1e fixed-prime overlap sieve and exact-one synthesis",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
