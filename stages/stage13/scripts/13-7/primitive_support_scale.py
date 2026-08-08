#!/usr/bin/env python3
"""Stage13-7ja: primitive support changes logarithmic scale, not limit vector.

M_q(B): Stage13-7d `m1`, i.e. the 1/R_all(p) face average before the global
primitive condition gcd(x,y,z)=1.
G_q(B): primitive pure-G mass proved in Stage13-7j.

Analytic inputs: elementary Euclid-parameter sector counting, the finite-order
Selberg--Delange level already accepted in Stage12 for the no-split semigroup,
and the same finite Vaaler/Gaussian-Hecke cancellation used in Stage13-7i/j.
Only o(B log B) is needed from the nonzero angular harmonics here.
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
    if abs(sum(I.values()) - math.pi**2 / 8.0) > 1e-12:
        raise ArithmeticError("Stage13-3b chamber sum mismatch")

    # Primitive oriented outer triples are uniform in outer angle psi.
    # After summing all integer dilates, the zero-mode coefficient is
    # (2/pi^2) int k_q(psi)dpsi = 8 I_q/pi^3.
    C = {q: 8.0 * I[q] / math.pi**3 for q in CATS}
    C_total = sum(C.values())
    if abs(C_total - 1.0 / math.pi) > 2e-15:
        raise ArithmeticError("pre-primitive constants do not sum to 1/pi")

    K = {
        q: float(r7j["individual_leading_constants"][q]["numeric_truncation"])
        for q in CATS
    }
    K_total = sum(K.values())
    K_star = float(r7j["common_arithmetic_factor"]["K_star"])
    survival = {q: K[q] / C[q] for q in CATS}
    Lambda = K_star * math.pi**2 / 4.0
    if max(abs(survival[q] - Lambda) for q in CATS) > 5e-14:
        raise ArithmeticError("primitive survival factor is not category-independent")
    if abs(Lambda - math.pi * K_total) > 5e-14:
        raise ArithmeticError("total survival identity failed")

    prop = {q: C[q] / C_total for q in CATS}
    gprop = r7j["normalized_limit"]["proportion"]
    if max(abs(prop[q] - float(gprop[q])) for q in CATS) > 2e-14:
        raise ArithmeticError("primitive filter changed leading normalized vector")

    return {
        "metadata": {
            "stage": "13-7ja",
            "scope": "primitive-support main-scale effect: pre-primitive m1 -> primitive pure-G",
        },
        "definitions": {
            "M_q": "pre-primitive G-neutral/m1 category mass before gcd(x,y,z)=1",
            "G_q": "primitive pure-G category mass from Stage13-7j",
            "shellwise_support_factor": (
                "R_prim(p,z)/R_all(p), R_prim=sum_{m|gcd(p,z)} mu(m) R_all(p/m)"
            ),
        },
        "preprimitive_outer_shell_count": {
            "primitive_oriented_sector_count": (
                "P_f(X)=(2/pi^2)*(int_0^(pi/2) f(psi)dpsi)*X + lower order"
            ),
            "all_dilates": (
                "S_f(B)=(2/pi^2)*(int f)*B log B + O_f(B) before face-support exclusion"
            ),
            "face_support_exclusion": (
                "G(p)=1 iff p has no q=1 mod 4 prime. The no-split semigroup has "
                "count O(X/sqrt(log X)), hence excluded shells O(B sqrt(log B))."
            ),
        },
        "inner_angle_remainder": {
            "decomposition": (
                "zero kernel k_q(t) plus centered Gaussian harmonics "
                "(H_l(p)-1)/(G(p)-1)"
            ),
            "bound": (
                "The Stage13-7i/j finite Vaaler truncation and nontrivial Gaussian-Hecke "
                "input give o(B log B), which is all 7ja requires."
            ),
            "role": "only the zero angular mode contributes to the B log B main term",
        },
        "preprimitive_asymptotic": {
            q: {
                "constant": C[q],
                "formula": f"C_{q}=8 I_{q}/pi^3",
                "theorem": f"M_{q}(B) ~ C_{q} B log B",
            }
            for q in CATS
        },
        "preprimitive_total": {
            "constant": C_total,
            "formula": "C_total=1/pi",
            "theorem": "M_ab+M_ac+M_bc ~ (1/pi) B log B",
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
                "G_q/M_q ~ Lambda (log B)^(-2/3), "
                "Lambda=K_q/C_q=(3*pi^2/8)c_h*C_odd=pi*K_total"
            ),
            "Lambda": Lambda,
            "categorywise_values": survival,
            "category_independent": True,
            "logarithmic_exponent_change": "1 -> 1/3",
        },
        "primitive_correction": {
            "definition": "P_q=G_q-M_q",
            "theorem": "P_q(B) ~ -C_q B log B for each q",
            "interpretation": (
                "primitive support cancels the entire pre-primitive B log B main scale; "
                "it is not a lower-order perturbation"
            ),
        },
        "normalized_direction": {
            "preprimitive_limit": prop,
            "primitive_pure_G_limit": {q: float(gprop[q]) for q in CATS},
            "same_limit": True,
            "ratio_bc": {"ab": C["ab"] / C["bc"], "ac": C["ac"] / C["bc"], "bc": 1.0},
            "conclusion": (
                "primitive support changes absolute logarithmic scale but not the leading "
                "normalized directional vector"
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
