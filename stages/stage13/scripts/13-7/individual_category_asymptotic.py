#!/usr/bin/env python3
"""Stage13-7j: individual pure-G category asymptotics.

Stage13-7i proved the pure-G ac-bc gap by isolating the j=1 zero angular
mode.  The same arithmetic coefficient occurs for each category; only the
archimedean zero-mode kernel changes.  This script integrates the three
category kernels in the frozen Stage12 (r,s) polar angle, checks that they
recover the Stage13-3b chamber integrals, and multiplies them by the 7i
arithmetic constant.

The result is at the same external theorem level as Stage13-7i:
finite-order Selberg--Delange plus the polylog-uniform Gaussian Hecke
zero-free input used there.  This script is a deterministic constant/identity
validator, not a replacement for those external theorems.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_7I = ROOT / "13-7/curved_wedge_asymptotic_report.json"
IN_3B = ROOT / "13-3/geometric_chamber_report.json"
OUT = ROOT / "13-7/individual_category_asymptotic_report.json"


def t_of_phi(phi: float) -> float:
    c = math.cos(phi)
    s = math.sin(phi)
    return (s * s - c * c) / (2.0 * s * c)


def category_zero_kernel(phi: float) -> tuple[float, float, float]:
    """(P_ab,P_ac,P_bc) for uniform inner face angle at fixed outer phi."""
    t = t_of_phi(phi)
    z = 1.0 / math.sqrt(2.0)
    if t < z:
        ac = 4.0 * math.asin(t) / math.pi
        return 0.0, ac, 1.0 - ac
    if t < 1.0:
        ac = 4.0 * math.acos(t) / math.pi
        return 1.0 - ac, ac, 0.0
    return 1.0, 0.0, 0.0


def simpson_component(index: int, n: int = 200_000) -> float:
    if n % 2:
        n += 1
    a = math.pi / 4.0
    b = math.pi / 2.0
    h = (b - a) / n
    acc = category_zero_kernel(a)[index] + category_zero_kernel(b)[index]
    for i in range(1, n):
        acc += (4.0 if i % 2 else 2.0) * category_zero_kernel(a + i * h)[index]
    return acc * h / 3.0


def build_report() -> dict:
    r7i = json.loads(IN_7I.read_text())
    r3b = json.loads(IN_3B.read_text())

    J = [simpson_component(i) for i in range(3)]
    names = ("ab", "ac", "bc")

    chamber = r3b["numerical_chamber_integrals"]
    I = [float(chamber[f"I_{name}"]) for name in names]

    # psi=atan(z/p)=2*phi-pi/2.  The Stage13-3b I_q integral contains the
    # inner face-angle length, while the fixed-shell zero kernel is that
    # length divided by pi/4.  Therefore J_q=(2/pi)I_q.
    bridge_errors = [abs(J[i] - 2.0 * I[i] / math.pi) for i in range(3)]
    if max(bridge_errors) > 2e-9:
        raise ArithmeticError(f"Stage13-3b bridge mismatch: {bridge_errors}")
    if abs(sum(J) - math.pi / 4.0) > 3e-10:
        raise ArithmeticError("category zero kernels do not partition the outer angle")

    diag = max(r7i["euler_product_diagnostics"], key=lambda row: row["prime_cutoff"])
    c_h = float(diag["scale_summatory_constant_truncated"])
    c_odd = float(diag["C_odd_at_111_truncated"])
    common = 1.5 * c_h * c_odd
    K = [common * x for x in J]
    K_total = sum(K)

    gap_J = J[1] - J[2]
    gap_K = K[1] - K[2]
    i0 = float(r7i["archimedean_wedge"]["numeric_value"])
    k0 = float(r7i["leading_constant"]["numeric_truncation_at_prime_1e6"])
    if abs(gap_J - i0) > 3e-10:
        raise ArithmeticError("category gap angular constant does not reproduce Stage13-7i")
    if abs(gap_K - k0) > 3e-10:
        raise ArithmeticError("category constants do not reproduce Stage13-7i K0")

    proportions = [x / K_total for x in K]
    ratio_bc = [K[0] / K[2], K[1] / K[2], 1.0]

    return {
        "metadata": {
            "stage": "13-7j",
            "scope": (
                "individual pure-G category asymptotics and normalized pure-G limit; "
                "raw/shell/exact-one reweighting is not included"
            ),
        },
        "exact_category_zero_kernels": {
            "0<t<1/sqrt(2)": {
                "ab": "0",
                "ac": "4 asin(t)/pi",
                "bc": "1-4 asin(t)/pi",
            },
            "1/sqrt(2)<t<1": {
                "ab": "1-4 acos(t)/pi",
                "ac": "4 acos(t)/pi",
                "bc": "0",
            },
            "t>1": {"ab": "1", "ac": "0", "bc": "0"},
            "partition": "k_ab(t)+k_ac(t)+k_bc(t)=1 pointwise",
        },
        "stage13_3b_bridge": {
            "relation": "J_q=int_{pi/4}^{pi/2} k_q(t(phi)) dphi = (2/pi) I_q",
            "J": dict(zip(names, J)),
            "I_stage13_3b": dict(zip(names, I)),
            "max_abs_bridge_error": max(bridge_errors),
            "sum_J": sum(J),
            "expected_sum_J": math.pi / 4.0,
            "gap_J_ac_minus_bc": gap_J,
            "stage13_7i_I0": i0,
        },
        "common_arithmetic_factor": {
            "formula": "K_star=(3/2)*c_h*C_odd(1,1,1)",
            "prime_product_cutoff_for_numeric_diagnostic": int(diag["prime_cutoff"]),
            "c_h": c_h,
            "C_odd_at_111": c_odd,
            "K_star": common,
            "reason_category_independent": (
                "For j=1 zero mode the h,r,s multiplicative coefficient and parity/radial "
                "ledger are identical for ab, ac, bc; the category enters only through k_q(t)."
            ),
        },
        "individual_leading_constants": {
            name: {
                "formula": f"K_{name}=K_star*J_{name}",
                "numeric_truncation": K[i],
                "theorem": f"G_{name}(B) ~ K_{name} B(log B)^(1/3)",
            }
            for i, name in enumerate(names)
        },
        "total_and_gap_checks": {
            "K_total": K_total,
            "K_total_formula": "K_star*pi/4",
            "K_ac_minus_K_bc": gap_K,
            "stage13_7i_K0": k0,
            "gap_constant_match_abs_error": abs(gap_K - k0),
        },
        "remainder_transfer": {
            "nonzero_harmonics": (
                "Apply the Stage13-7i finite Vaaler/Selberg truncation separately to each "
                "category interval indicator; retained nonzero Gaussian harmonics are lower order."
            ),
            "normalization_tail": (
                "After j=1, each primitive category count is nonnegative and bounded by the "
                "total primitive face-count majorant, so the full j>=2 remainder is bounded by "
                "the same positive j=2 zero channel used in Stage13-7i."
            ),
            "minimal_scale_and_wings": (
                "The Stage13-7h O(B) minimal-scale and O(B(log B)^(1/4)) small-height/"
                "coordinate bounds are categorywise upper bounds and remain lower order."
            ),
        },
        "normalized_limit": {
            "proportion": dict(zip(names, proportions)),
            "bc_normalized_ratio": {
                "ab": ratio_bc[0],
                "ac": ratio_bc[1],
                "bc": ratio_bc[2],
            },
            "identity": (
                "Because the common arithmetic factor cancels, the pure-G normalized limit "
                "equals the Stage13-3b archimedean chamber proportion I_q/(pi^2/8)."
            ),
        },
        "status": {
            "individual_pure_G_category_asymptotics": True,
            "pure_G_normalized_directional_limit_identified": True,
            "raw_or_exact_one_directional_limit_identified": False,
            "next": "Stage13-7k",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
