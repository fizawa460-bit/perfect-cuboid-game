#!/usr/bin/env python3
"""Stage13-7ja: primitive-support changes the logarithmic scale, not the limit vector.

Definitions.

M_q(B) is the Stage13-7d `m1` observable: for every oriented outer
Pythagorean shell (p,z,d), d<=B, with at least one face representation,
average the q-category indicator over *all* unordered face representations
of p, before imposing gcd(x,y,z)=1.

G_q(B) is the primitive pure-G observable proved in Stage13-7j.

The point of 7ja is to determine the size of the primitive-support filter.
The pre-primitive quantity has a B log B main term.  The primitive filter
cancels that whole scale and leaves the B (log B)^(1/3) scale from 7j.
Nevertheless the three leading constants are proportional category by
category, so the normalized directional vector is unchanged.

This file is a deterministic constant/identity validator.  The analytic
inputs are:
  * elementary Euclid-parameter lattice counting for primitive outer
    Pythagorean triples in angular sectors;
  * the finite-order Selberg--Delange level already accepted in Stage12,
    used to bound scales having no prime 1 mod 4;
  * the Gaussian-Hecke/Vaaler cancellation already used in Stage13-7i/j,
    now only needed to show the nonzero inner-angle harmonics are
    o(B log B).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_3B = ROOT / "13-3/geometric_chamber_report.json"
IN_7J = ROOT / "13-7/individual_category_asymptotic_report.json"
OUT = ROOT / "13-7/primitive_support_scale_report.json"
CATS = ("ab", "ac", "bc")


def build_report() -> dict:
    r3b = json.loads(IN_3B.read_text())
    r7j = json.loads(IN_7J.read_text())

    chamber = r3b["numerical_chamber_integrals"]
    I = {q: float(chamber[f"I_{q}"]) for q in CATS}
    isum = sum(I.values())
    if abs(isum - math.pi**2 / 8.0) > 1e-12:
        raise ArithmeticError("Stage13-3b chamber sum mismatch")

    # For oriented primitive outer triples, the outer angle psi is uniform:
    #   P_f(X) = (2/pi^2) int_0^(pi/2) f(psi)dpsi * X + lower order.
    # Summing all positive integer dilates supplies the harmonic factor log B.
    # Since int k_q dpsi = 4 I_q/pi, the m1 leading constant is 8 I_q/pi^3.
    C_m1 = {q: 8.0 * I[q] / math.pi**3 for q in CATS}
    C_total = sum(C_m1.values())
    if abs(C_total - 1.0 / math.pi) > 2e-15:
        raise ArithmeticError("pre-primitive constants do not sum to 1/pi")

    K = {
        q: float(r7j["individual_leading_constants"][q]["numeric_truncation"])
        for q in CATS
    }
    K_total = sum(K.values())
    common = float(r7j["common_arithmetic_factor"]["K_star"])

    survival = {q: K[q] / C_m1[q] for q in CATS}
    Lambda = common * math.pi**2 / 4.0
    if max(abs(survival[q] - Lambda) for q in CATS) > 5e-14:
        raise ArithmeticError("primitive-support factor is not category-independent")
    if abs(Lambda - math.pi * K_total) > 5e-14:
        raise ArithmeticError("total survival constant identity failed")

    prop_m1 = {q: C_m1[q] / C_total for q in CATS}
    prop_g = r7j["normalized_limit"]["proportion"]
    if max(abs(prop_m1[q] - float(prop_g[q])) for q in CATS) > 2e-14:
        raise ArithmeticError("primitive filter changed the leading normalized vector")

    return {
        "metadata": {
            "stage": "13-7ja",
            "scope": (
                "primitive-support main-scale effect between the pre-primitive m1 "
                "observable and the primitive pure-G observable"
            ),
        },
        "definitions": {
            "M_q": (
                "pre-primitive G-neutral/m1 category mass: average over all face "
                "representations on each face-supported outer shell before gcd(x,y,z)=1"
            ),
            "G_q": "primitive pure-G category mass from Stage13-7j",
            "primitive_support_factor_shellwise": (
                "R_prim(p,z)/R_all(p), with R_prim=sum_{m|gcd(p,z)} mu(m) R_all(p/m)"
            ),
        },
        "preprimitive_outer_shell_count": {
            "primitive_oriented_sector_count": (
                "P_f(X)=(2/pi^2)*(int_0^(pi/2) f(psi)dpsi)*X + lower order"
            ),
            "all_dilates": (
                "sum over primitive oriented shells of floor(B/d0) gives "
                "S_f(B)=(2/pi^2)*(int f)*B log B + O_f(B) before face-support exclusion"
            ),
            "face_support_exclusion": (
                "G(p)=1 iff p has no prime q=1 mod 4.  The no-split semigroup has "
                "count O(X/sqrt(log X)); partial summation gives harmonic mass "
                "O(sqrt(log X)), hence excluded outer shells O(B sqrt(log B))."
            ),
        },
        "inner_angle_remainder": {
            "decomposition": (
                "m1 category indicator = zero kernel k_q(t) + centered Gaussian "
                "nonzero harmonics (H_l(p)-1)/(G(p)-1)"
            ),
            "bound": (
                "The Stage13-7i finite Vaaler truncation plus the same nontrivial "
                "Gaussian-Hecke zero-free input gives o(B log B); a conservative "
                "combined ledger is O_eps(B (log B)^(1/2+eps))."
            ),
            "role": "therefore only the zero angular mode contributes to the B log B main term",
        },
        "preprimitive_asymptotic": {
            q: {
                "constant": C_m1[q],
                "formula": f"C_{q}=8 I_{q}/pi^3",
                "theorem": f"M_{q}(B) ~ C_{q} B log B",
            }
            for q in CATS
        },
        "preprimitive_total": {
            "constant": C_total,
            "formula": "C_total=1/pi",
            "theorem": "M_ab(B)+M_ac(B)+M_bc(B) ~ (1/pi) B log B",
        },
        "primitive_pure_G_from_7j": {
            q: {
                "constant": K[q],
                "theorem": f"G_{q}(B) ~ K_{q} B (log B)^(1/3)",
            }
            for q in CATS
        },
        "effective_primitive_survival": {
            "formula": (
                "G_q(B)/M_q(B) ~ Lambda (log B)^(-2/3), "
                "Lambda=K_q/C_q=(3*pi^2/8)c_h*C_odd=pi*K_total"
            ),
            "Lambda": Lambda,
            "categorywise_values": survival,
            "category_independent": True,
            "logarithmic_exponent_change": "1 -> 1/3, i.e. suppression (log B)^(-2/3)",
        },
        "primitive_correction": {
            "definition": "P_q(B)=G_q(B)-M_q(B)",
            "theorem": "P_q(B) ~ -C_q B log B for each q",
            "interpretation": (
                "the primitive filter is not a perturbative correction: it cancels the "
                "entire pre-primitive B log B main scale, leaving the smaller 7j scale"
            ),
        },
        "normalized_direction": {
            "preprimitive_limit": prop_m1,
            "primitive_pure_G_limit": {q: float(prop_g[q]) for q in CATS},
            "same_limit": True,
            "ratio_bc": {
                "ab": C_m1["ab"] / C_m1["bc"],
                "ac": C_m1["ac"] / C_m1["bc"],
                "bc": 1.0,
            },
            "conclusion": (
                "primitive support changes the absolute logarithmic scale but does not "
                "change the leading normalized directional vector"
            ),
        },
        "status": {
            "primitive_support_is_lower_order_perturbation": False,
            "primitive_support_changes_log_exponent": True,
            "primitive_support_changes_leading_normalized_vector": False,
            "preprimitive_m1_asymptotic_identified": True,
            "next": "Stage13-7jb",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
