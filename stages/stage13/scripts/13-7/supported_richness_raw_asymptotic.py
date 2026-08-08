#!/usr/bin/env python3
"""Stage13-7jb: restore supported-shell richness and identify raw directional limits.

Stage13-7j proved the primitive pure-G category asymptotics.  Multiplying the
shell contribution by R_all(p)=(G(p)-1)/2 removes the G-neutral denominator and
returns the primitive canonical raw face-incidence count.  In the fixed-channel
language of Stage13-7g/7h this is exactly the missing normalization channel j=0.

The j=0 zero mode has the same Stage12 (h,r,s) coefficient system as the frozen
primitive raw theorem, hence scale B(log B)^3.  Nonzero Gaussian harmonics have
no zeta pole in the free scale and are lower order after the same finite
Vaaler/Hecke closure used in 7i/j.  Therefore the raw leading directional
constants are the frozen Stage12 total constant times the Stage13-3b chamber
proportions.

This script validates the j=0 local identities and the resulting constants.
The numerical kappa value is the Stage12 prime-product diagnostic, not a
certified enclosure; the symbolic theorem constants are in terms of kappa.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_3B = ROOT / "13-3/geometric_chamber_report.json"
IN_7J = ROOT / "13-7/individual_category_asymptotic_report.json"
IN_12 = Path("stages/stage12/archive/data/2k/final_remainder_report.json")
OUT = ROOT / "13-7/supported_richness_raw_asymptotic_report.json"
CATS = ("ab", "ac", "bc")


def D(e: int, phase: float) -> float:
    return 1.0 + 2.0 * sum(math.cos(m * phase) for m in range(1, e + 1))


def local_j0(mode: str, phase: float, a: int, b: int) -> float:
    e = a + b
    if mode == "zero":
        return float(2 * b + 1) if a == 0 else 2.0
    return D(b, phase) if a == 0 else 2.0 * math.cos(e * phase)


def validate_j0() -> dict:
    phase = 0.731234567
    ez = eh = 0.0
    cases = 0
    for a in range(7):
        for b in range(7):
            e = a + b
            z_direct = float(2 * e + 1) if a == 0 else 2.0
            h_direct = D(e, phase) if a == 0 else D(e, phase) - D(e - 1, phase)
            ez = max(ez, abs(z_direct - local_j0("zero", phase, a, b)))
            eh = max(eh, abs(h_direct - local_j0("harmonic", phase, a, b)))
            cases += 1
    if ez > 1e-14 or eh > 1e-12:
        raise ArithmeticError((ez, eh))
    return {"cases": cases, "max_zero_error": ez, "max_harmonic_error": eh}


def build_report() -> dict:
    r3 = json.loads(IN_3B.read_text())
    r7 = json.loads(IN_7J.read_text())
    r12 = json.loads(IN_12.read_text())

    I = {q: float(r3["numerical_chamber_integrals"][f"I_{q}"]) for q in CATS}
    P = {q: 8.0 * I[q] / math.pi**2 for q in CATS}
    if abs(sum(P.values()) - 1.0) > 2e-15:
        raise ArithmeticError("chamber proportions do not sum to one")

    kappa_diag = float(r12["euler_product_diagnostic"]["stage12_kappa_partial"])
    raw_total_diag = kappa_diag / (24.0 * math.pi)
    raw_diag = {q: raw_total_diag * P[q] for q in CATS}

    K = {
        q: float(r7["individual_leading_constants"][q]["numeric_truncation"])
        for q in CATS
    }
    omega = {q: raw_diag[q] / K[q] for q in CATS}
    omega0 = omega["ab"]
    if max(abs(omega[q] - omega0) for q in CATS) > 2e-15:
        raise ArithmeticError("raw/pure-G leading amplification is category-dependent")

    return {
        "metadata": {
            "stage": "13-7jb",
            "scope": "supported-shell richness restoration from primitive pure-G to primitive raw incidence",
        },
        "exact_reweighting": {
            "R_all": "R_all(p)=(G(p)-1)/2",
            "identity": "A_q(B)=sum_shell R_all(p) * [n_q(shell)/R_all(p)] = sum_shell n_q(shell)",
            "fixed_channel_interpretation": "restoring R_all removes 1/(G-1); this is the j=0 member of the Stage13-7g/7h local kernel family, up to the universal factor 1/2 converting ordered to unordered face representations",
        },
        "j0_local_validation": validate_j0(),
        "j0_singularity_ledger": {
            "zero_scale": "A_{0,0}(s)=(zeta(s)L(s,chi4)) E_h(s)",
            "zero_base": "B_{0,0}(s)=zeta(s)^2 L(s,chi4) E_b(s)",
            "zero_bulk_after_primitive_region_transfer": "B(log B)^3",
            "zero_minimal_scale": "O(B(log B)^2)",
            "harmonic_scale": "A_{0,l}(s)=L(s,xi_{8l}) E_{h,l}(s), l>=1; no zeta pole",
            "harmonic_base": "B_{0,l}(s)=zeta(s)L(s,xi_{8l})E_{b,l}(s)",
            "harmonic_minimal_scale": "O(B) for fixed l",
            "infinite_family": "the Stage13-7i finite Vaaler truncation with the same polylog-uniform nontrivial Gaussian-Hecke input makes the retained nonzero harmonics o(B(log B)^3)",
        },
        "frozen_stage12_total": {
            "theorem": "A_ab(B)+A_ac(B)+A_bc(B) ~ [kappa/(24*pi)] B(log B)^3",
            "source": "Stage13-3d exact bridge plus frozen Stage12 C_prim(B)~[kappa/(12*pi)]B(log B)^3",
            "kappa_prime_product_diagnostic": kappa_diag,
            "numeric_total_constant_diagnostic": raw_total_diag,
        },
        "individual_raw_asymptotics": {
            q: {
                "symbolic_constant": f"D_{q}=kappa*I_{q}/(3*pi^3)",
                "numeric_prime_product_diagnostic": raw_diag[q],
                "theorem": f"A_{q}(B) ~ D_{q} B(log B)^3",
            }
            for q in CATS
        },
        "raw_normalized_limit": {
            "proportion": P,
            "bc_normalized_ratio": {
                "ab": P["ab"] / P["bc"],
                "ac": P["ac"] / P["bc"],
                "bc": 1.0,
            },
            "identity": "D_q/sum D = 8 I_q/pi^2; supported-shell richness changes the scale but not the leading normalized vector",
        },
        "richness_amplification_relative_to_pure_G": {
            "formula": "A_q(B)/G_q(B) ~ Omega (log B)^(8/3)",
            "numeric_Omega_using_stage12_kappa_diagnostic": omega0,
            "categorywise_numeric_values": omega,
            "category_independent_at_leading_order": True,
            "log_exponent_change": "1/3 -> 3, i.e. amplification (log B)^(8/3)",
        },
        "interpretation": {
            "finite_flattening": "The strong finite flattening seen in Stage13-3e is pre-asymptotic category dependence of shell richness.",
            "asymptotic_result": "At the leading B(log B)^3 scale, the richness factor is common across categories and the chamber vector is restored.",
        },
        "status": {
            "supported_shell_richness_changes_log_exponent": True,
            "supported_shell_richness_changes_leading_normalized_vector": False,
            "individual_raw_directional_asymptotics": True,
            "raw_directional_limit_identified": True,
            "exact_one_directional_limit_identified": False,
            "next": "Stage13-7jc",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
