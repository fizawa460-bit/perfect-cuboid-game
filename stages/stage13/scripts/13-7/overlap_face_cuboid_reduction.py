#!/usr/bin/env python3
"""Stage13-7jc: reduce the exact-one obstruction to face-cuboid counting.

Stage13-7jb proves primitive raw directional asymptotics

    A_q(B) ~ D_q B (log B)^3.

To transfer these to the exactly-one counts N_q, it is enough to show that
cuboids carrying two or three integral face diagonals are lower order.  This
script records the exact inclusion-exclusion algebra and identifies the one
remaining scalar counting problem.

A cuboid with integer edges, integer space diagonal and at least two integer
face diagonals is a (rational/integer) face cuboid.  After division by the
space diagonal it gives a rational face-cuboid similarity class; conversely,
clearing denominators and dividing the common gcd recovers a primitive integer
representative.  Thus the overlap problem is a height-count problem on the
face-cuboid locus, not another local Euler-factor correction.

No lower-order theorem for that height count is claimed here.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path("stages/stage13/data")
IN_RAW = ROOT / "13-3/raw_incidence_report.json"
IN_7JB = ROOT / "13-7/supported_richness_raw_asymptotic_report.json"
OUT = ROOT / "13-7/overlap_face_cuboid_reduction_report.json"
CATS = ("ab", "ac", "bc")


def build_report() -> dict:
    raw = json.loads(IN_RAW.read_text())
    r7jb = json.loads(IN_7JB.read_text())

    finite_checks = []
    for row in raw["rows"]:
        A = row["raw_incidence"]
        N = row["exact_one"]
        ov = row["overlap"]
        o12 = int(ov["ab_ac"])
        o13 = int(ov["ab_bc"])
        o23 = int(ov["ac_bc"])
        t = int(ov["three_face"])
        reconstructed = {
            "ab": A["ab"] - o12 - o13 + t,
            "ac": A["ac"] - o12 - o23 + t,
            "bc": A["bc"] - o13 - o23 + t,
        }
        if reconstructed != N:
            raise ArithmeticError((row["B"], reconstructed, N))

        pair_sum = o12 + o13 + o23
        # If E2 is the number with exactly two integral faces and E3 the
        # number with exactly three, then pair_sum=E2+3E3 and
        # F=E2+E3.  Hence F=pair_sum-2E3 and F<=pair_sum<=3F.
        face_cuboids = pair_sum - 2 * t
        if not (face_cuboids <= pair_sum <= 3 * face_cuboids):
            raise ArithmeticError("face-cuboid/pair-overlap sandwich failed")

        raw_total = sum(int(A[q]) for q in CATS)
        exact_total = sum(int(N[q]) for q in CATS)
        if exact_total != raw_total - 2 * pair_sum + 3 * t:
            raise ArithmeticError("total inclusion-exclusion failed")

        finite_checks.append({
            "B": row["B"],
            "pair_overlap_sum": pair_sum,
            "face_cuboid_count": face_cuboids,
            "triple_overlap": t,
            "raw_total": raw_total,
            "exact_one_total": exact_total,
            "face_cuboid_fraction_of_raw_incidence": face_cuboids / raw_total,
        })

    prop = r7jb["raw_normalized_limit"]["proportion"]
    ratio = r7jb["raw_normalized_limit"]["bc_normalized_ratio"]

    return {
        "metadata": {
            "stage": "13-7jc",
            "scope": (
                "exact reduction of the exactly-one correction to a scalar "
                "primitive face-cuboid height count; no overlap asymptotic is proved"
            ),
        },
        "exact_inclusion_exclusion": {
            "notation": {
                "O_ab_ac": "primitive canonical cuboids with ab and ac face diagonals integral",
                "O_ab_bc": "primitive canonical cuboids with ab and bc face diagonals integral",
                "O_ac_bc": "primitive canonical cuboids with ac and bc face diagonals integral",
                "T": "primitive canonical cuboids with all three face diagonals integral (perfect-cuboid overlap locus)",
            },
            "category_identities": {
                "N_ab": "A_ab-O_ab_ac-O_ab_bc+T",
                "N_ac": "A_ac-O_ab_ac-O_ac_bc+T",
                "N_bc": "A_bc-O_ab_bc-O_ac_bc+T",
            },
            "total_identity": (
                "N1=A_total-2*(O_ab_ac+O_ab_bc+O_ac_bc)+3*T"
            ),
        },
        "single_scalar_reduction": {
            "F_definition": (
                "number of primitive canonical integer face cuboids with d<=B, "
                "i.e. integer edges and space diagonal and at least two integral face diagonals"
            ),
            "O_definition": "O=O_ab_ac+O_ab_bc+O_ac_bc",
            "histogram_identity": "if E2=exactly-two count and E3=triple count, then F=E2+E3 and O=E2+3E3",
            "sandwich": "F(B) <= O(B) <= 3 F(B)",
            "sufficient_bound": "F(B)=o(B(log B)^3)",
            "consequence": (
                "the sufficient bound implies every overlap correction is o(B(log B)^3), "
                "hence N_q(B)~A_q(B) categorywise"
            ),
            "triple_note": (
                "No separate bound for T is needed once F (or O) is lower order; "
                "T<=F.  In particular no assumption about nonexistence of perfect cuboids is used."
            ),
        },
        "projective_face_cuboid_bridge": {
            "normalization": (
                "divide a primitive integer overlap by d; this gives a rational face-cuboid "
                "similarity class with two rational face diagonals and rational space diagonal"
            ),
            "inverse": (
                "clear denominators of a rational face cuboid and divide the common gcd to "
                "recover a primitive integer representative"
            ),
            "interpretation": (
                "F(B) is therefore a rational-point height-count problem on the face-cuboid locus, "
                "not a local-density perturbation of the Stage12 Euler product"
            ),
        },
        "elliptic_surface_literature_bridge": {
            "reference": (
                "Takumi Yoshida, The relationship between face cuboids and elliptic curves, "
                "arXiv:2407.09825 (2024)"
            ),
            "family": "E_{1,s}: y^2=x(x-(2s)^2)(x+(s^2-1)^2)",
            "published_structural_result": (
                "a surjective 32:1 map from pairs (s,P), with P a non-torsion rational point "
                "on E_{1,s}, to rational face-cuboid equivalence classes"
            ),
            "use_here": (
                "this identifies the correct arithmetic-geometric object and shows the overlap "
                "locus is genuinely infinite; it does not supply the uniform height-count bound required here"
            ),
        },
        "required_new_theorem": {
            "minimal_form": "F(B)=o(B(log B)^3)",
            "stronger_convenient_form": "F(B)=O(B(log B)^(3-delta)) for some delta>0, or any O(B^(1-epsilon)) bound",
            "elliptic_form": (
                "obtain a height-uniform count for the relevant rational points across the family E_{1,s}, "
                "after translating elliptic height to the primitive cuboid space-diagonal height"
            ),
            "not_supplied_by_current_stage12_13_toolkit": True,
        },
        "raw_limit_waiting_for_transfer": {
            "scale": "B(log B)^3",
            "proportion": {q: float(prop[q]) for q in CATS},
            "bc_normalized_ratio": {q: float(ratio[q]) for q in CATS},
            "conditional_exact_one_statement": (
                "if F(B)=o(B(log B)^3), then the exact-one normalized limit equals the raw/Stage13-3b chamber limit"
            ),
        },
        "finite_legacy_checks": finite_checks,
        "status": {
            "pair_overlap_exactly_reduced_to_face_cuboid_count": True,
            "triple_overlap_requires_perfect_cuboid_nonexistence": False,
            "pair_overlap_lower_order_proved": False,
            "exact_one_directional_limit_identified": False,
            "new_external_height_count_needed": True,
            "next": "Stage13-7jd",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
