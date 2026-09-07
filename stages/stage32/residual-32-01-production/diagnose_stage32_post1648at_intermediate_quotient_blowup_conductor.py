#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AP = HERE / "post1648ap-factor-pair-birational-conductor-demand.json"
AQ = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"
AS = HERE / "post1648as-residual-inertia-tangent-preflight.json"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def main() -> None:
    ap = json.loads(AP.read_text())
    aq = json.loads(AQ.read_text())
    ass = json.loads(AS.read_text())
    v6 = json.loads(V6.read_text())

    assert ap["canonical_sha256_without_this_field"] == "35c1f8ff265250ccda9bd44f0ce815022e7fde1f30120ba18722a6cf12bb8b3d"
    assert aq["canonical_sha256_without_this_field"] == "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e"
    assert ass["canonical_sha256_without_this_field"] == "3211e758e5b4ec4e96e91b8844a0de429f08fb031e1fd99ba01ac0f9ccea5907"
    assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"

    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    boundary = pairings[32:44]
    exceptional = pairings[92:]
    assert boundary == [11,26,31,22,16,26,25,11,28,40,34,22]
    assert sum(boundary) == 292
    assert sum(exceptional) == 266

    inertia_boundary_sums = []
    inertia_pairwise = []
    inertia_conductor = []
    for row in ass["node_inertia"]:
        labels = [int(x) for x in row["boundary_inertia_labels_1based"]]
        bsum = sum(pairings[i-1] for i in labels)
        cdot = int(row["C_dot_gC"])
        assert (cdot - bsum) % 2 == 0
        inertia_boundary_sums.append(bsum)
        inertia_pairwise.append(cdot)
        inertia_conductor.append((cdot-bsum)//2)
    assert inertia_boundary_sums == [90,78,124]
    assert inertia_pairwise == [1360,1286,1498]
    assert inertia_conductor == [635,604,687]

    nonnode = [int(r["C_dot_gC"]) for r in ass["non_node_elements"]]
    assert nonnode == [1112,1266,1284,1480]
    assert sum(nonnode) == 5142
    nonnode_conductor = sum(nonnode)//2
    assert nonnode_conductor == 2571

    S2 = int(aq["v6_orbit"]["S_square"])
    H_order = int(aq["residual_group"]["pointwise_stabilizer_order"])
    assert (S2,H_order) == (80352,8)
    assert S2 % H_order == 0
    CY2 = S2//H_order
    assert CY2 == 10044

    KS_C = int(ap["v6_strict_transform"]["canonical_intersection"])
    pa_C = int(ap["v6_strict_transform"]["arithmetic_genus"])
    delta_C = int(ap["v6_strict_transform"]["intrinsic_delta_defect"])
    assert (KS_C,pa_C,delta_C) == (186,473,472)

    ramification_boundary_C = sum(boundary)
    KY_CY = KS_C - ramification_boundary_C
    assert KY_CY == -106
    pa_CY = 1 + (CY2 + KY_CY)//2
    delta_CY = pa_CY - 1
    assert pa_CY == 4970 and delta_CY == 4969

    quotient_conductor = delta_CY - delta_C
    pairwise_sum = int(ass["residual_group"]["total_nontrivial_C_dot_gC_sum"])
    assert pairwise_sum == 9286
    assert quotient_conductor == (pairwise_sum-ramification_boundary_C)//2 == 4497
    assert sum(inertia_conductor) + nonnode_conductor == quotient_conductor

    m = [int(x) for x in aq["target_cusp_grid"]["image_multiplicities"]]
    assert m == [35,24,18,19,28,21,25,34,20,5,5,32]
    m_sum = sum(m)
    m_sq = sum(x*x for x in m)
    blowdown_delta = sum(x*(x-1)//2 for x in m)
    assert (m_sum,m_sq,blowdown_delta) == (266,6966,3350)

    D2 = int(aq["factor_pullback"]["D_square"])
    assert D2 == 17010 and D2-CY2 == m_sq
    D_bidegree = [int(x) for x in aq["factor_pullback"]["D_bidegree"]]
    assert D_bidegree == [81,105]
    KP1_D = -2*sum(D_bidegree)
    assert KP1_D == -372
    assert KP1_D + m_sum == KY_CY

    pa_D = int(ap["image_curve"]["arithmetic_genus"])
    delta_D = int(ap["image_curve"]["total_delta_defect"])
    assert (pa_D,delta_D) == (8320,8319)
    assert pa_CY + blowdown_delta == pa_D
    assert delta_CY + blowdown_delta == delta_D

    total_conductor = int(ap["conductor_demand"]["required_additional_conductor_length"])
    assert total_conductor == 7847 == quotient_conductor + blowdown_delta
    composite_canonical_difference = ramification_boundary_C + m_sum
    assert composite_canonical_difference == 558
    assert int(aq["conductor"]["canonical_difference"]) == composite_canonical_difference

    out = {
        "mode": "SCRATCH_POST1648AT_INTERMEDIATE_QUOTIENT_BLOWUP_CONDUCTOR",
        "parents": {
            "AP_canonical": ap["canonical_sha256_without_this_field"],
            "AQ_canonical": aq["canonical_sha256_without_this_field"],
            "AS_canonical": ass["canonical_sha256_without_this_field"],
            "V6_canonical": v6["canonical_sha256_without_this_field"],
        },
        "ramification_scope_correction": {
            "boundary_intersection_total": ramification_boundary_C,
            "exceptional_mass_not_divisorial_ramification": m_sum,
            "composite_canonical_difference": composite_canonical_difference,
            "identity": "558=292+266",
            "wrong_interpretation_rejected": "558=3*(K_S.C)",
        },
        "intermediate_quotient_curve": {
            "surface": "Y=S/H, locally blowup of P1xP1 at 12 target cusps",
            "H_order": H_order,
            "C_Y_square": CY2,
            "K_Y_dot_C_Y": KY_CY,
            "arithmetic_genus": pa_CY,
            "normalization_genus": 1,
            "delta": delta_CY,
            "additional_conductor_from_finite_H_quotient": quotient_conductor,
            "pairwise_formula": "(9286-292)/2=4497",
        },
        "finite_H_conductor_split": {
            "node_inertia_boundary_sums": inertia_boundary_sums,
            "node_inertia_pairwise_C_dot_gC": inertia_pairwise,
            "node_inertia_contributions": inertia_conductor,
            "node_inertia_total": sum(inertia_conductor),
            "non_node_pairwise_C_dot_gC": nonnode,
            "non_node_total": nonnode_conductor,
            "total": quotient_conductor,
        },
        "blowdown_to_P1xP1": {
            "target_cusp_multiplicities": m,
            "sum_m": m_sum,
            "sum_m_squared": m_sq,
            "C_Y_square": CY2,
            "D_square": D2,
            "K_P1xP1_dot_D": KP1_D,
            "K_Y_dot_C_Y": KY_CY,
            "arithmetic_genus_jump": blowdown_delta,
            "delta_jump": blowdown_delta,
            "formula": "sum binom(m_i,2)=(6966-266)/2=3350",
        },
        "total_conductor": {
            "AP_required": total_conductor,
            "finite_H_quotient": quotient_conductor,
            "twelve_blowdowns": blowdown_delta,
            "identity": "7847=4497+3350",
        },
        "decision": {
            "bounded_positive": "AP_CONDUCTOR_DEMAND_FACTORS_EXACTLY_THROUGH_SMOOTH_INTERMEDIATE_RESIDUAL_QUOTIENT_AND_12_BLOWDOWNS",
            "v6_carrier_excluded": False,
            "next_exact_route": "USE_EXACT_12_CUSP_INCIDENCE_GRAPH_AND_LOW_BIDEGREE_DIVISORS_OR_PROVE_MEMBER_LEVEL_JET_CONSTRAINTS; DO_NOT REUSE_FALSE_3K_RAMIFICATION_INTERPRETATION",
        },
        "firewalls": {
            "scratch_only": True,
            "shared_MAIN_STATE_unchanged": True,
            "shared_authority_unchanged": True,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
