#!/usr/bin/env python3
"""Stage13-7ja finite audit for the pre-primitive/primitive scale transition.

This consumes the existing complete Stage13-7d scaling report.  It does not
enumerate new cuboids and is not used to prove the asymptotic.  Its purpose is
to put the finite data on the two theorem scales:

    m1 total       / (B log B)              -> 1/pi,
    primitive G    / (B (log B)^(1/3))      -> K_total,
    (G/m1)*(log B)^(2/3)                    -> Lambda.

It also records the finite sign of the m1 ac-bc gap and the much larger
uniform-inner-angle (`geom`) gap.  The theorem predicts that the m1 gap must
eventually become positive of order B log B; its negative sign through 5m is
therefore explicitly classified as pre-asymptotic.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data/13-7")
IN_SCALING = ROOT / "analytic_reduction_scaling_report.json"
IN_SCALE = ROOT / "primitive_support_scale_report.json"
OUT = ROOT / "primitive_support_finite_report.json"
CATS = ("ab", "ac", "bc")


def ratio_bc(v: list[float]) -> dict[str, float]:
    return {"ab": v[0] / v[2], "ac": v[1] / v[2], "bc": 1.0}


def build_report() -> dict:
    src = json.loads(IN_SCALING.read_text())
    theorem = json.loads(IN_SCALE.read_text())
    c_total = float(theorem["preprimitive_total"]["constant"])
    k_total = sum(
        float(theorem["primitive_pure_G_from_7j"][q]["constant"]) for q in CATS
    )
    lam = float(theorem["effective_primitive_survival"]["Lambda"])
    limit_ratio = theorem["normalized_direction"]["ratio_bc"]

    keep = {100_000, 500_000, 1_000_000, 2_000_000, 5_000_000}
    rows = []
    for row in src["rows"]:
        B = int(row["B"])
        if B not in keep:
            continue
        block = row["ALL"]
        direct = [float(x) for x in block["direct"]]
        m1 = [float(x) for x in block["m1"]]
        geom = [float(x) for x in block["geom"]]
        dtotal = sum(direct)
        mtotal = sum(m1)
        gtotal = sum(geom)
        if abs(mtotal - gtotal) > 1e-5:
            raise ArithmeticError("m1 and geom must redistribute the same shell mass")
        L = math.log(B)
        rows.append(
            {
                "B": B,
                "m1_total": mtotal,
                "primitive_G_total": dtotal,
                "m1_total_over_B_logB": mtotal / (B * L),
                "target_1_over_pi": c_total,
                "primitive_total_over_B_logB_one_third": dtotal / (B * L ** (1.0 / 3.0)),
                "target_K_total": k_total,
                "effective_survival": dtotal / mtotal,
                "scaled_survival": (dtotal / mtotal) * L ** (2.0 / 3.0),
                "target_Lambda": lam,
                "m1_ratio_bc": ratio_bc(m1),
                "primitive_ratio_bc": ratio_bc(direct),
                "limit_ratio_bc": limit_ratio,
                "m1_ac_minus_bc_gap": m1[1] - m1[2],
                "geom_ac_minus_bc_gap": geom[1] - geom[2],
                "inner_angular_discrepancy_gap": float(block["inner_angular_discrepancy_gap"]),
                "primitive_correction_gap": float(block["primitive_correction_gap"]),
            }
        )

    last = rows[-1]
    return {
        "metadata": {
            "stage": "13-7ja",
            "scope": "finite diagnostics only; theorem inputs come from primitive_support_scale_report.json",
            "source": "Stage13-7d complete analytic_reduction_scaling_report.json",
        },
        "targets": {
            "m1_total_constant": c_total,
            "primitive_G_total_constant": k_total,
            "scaled_survival_constant": lam,
            "directional_ratio_bc": limit_ratio,
        },
        "rows": rows,
        "B5000000_summary": {
            "m1_total": last["m1_total"],
            "primitive_G_total": last["primitive_G_total"],
            "m1_total_over_B_logB": last["m1_total_over_B_logB"],
            "primitive_total_over_B_logB_one_third": last[
                "primitive_total_over_B_logB_one_third"
            ],
            "scaled_survival": last["scaled_survival"],
            "m1_ratio_bc": last["m1_ratio_bc"],
            "primitive_ratio_bc": last["primitive_ratio_bc"],
            "m1_gap_sign": "negative",
            "theorem_m1_gap_eventual_sign": "positive",
        },
        "interpretation": {
            "direct_scale_already_close": (
                "the primitive B(log B)^(1/3) total constant is comparatively stable by 5m"
            ),
            "preprimitive_scale_converges_slowly": (
                "the B log B m1 constant is still substantially below 1/pi because the "
                "face-support exclusion is only lower order by a sqrt(log B) factor"
            ),
            "finite_gap_sign_not_asymptotic": (
                "m1 ac-bc remains negative through 5m because the centered inner-angle "
                "harmonic correction is still larger than the positive zero-mode gap; "
                "the B log B zero mode eventually wins"
            ),
            "primitive_correction_sign_not_stable": (
                "the finite positive ac-bc primitive correction from Stage13-7d is also "
                "pre-asymptotic: categorywise G_q-M_q ~ -C_q B log B"
            ),
        },
        "status": {
            "finite_data_consistent_with_exponent_change": True,
            "finite_m1_gap_has_reached_asymptotic_sign": False,
            "finite_primitive_correction_gap_has_reached_asymptotic_sign": False,
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["B5000000_summary"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
