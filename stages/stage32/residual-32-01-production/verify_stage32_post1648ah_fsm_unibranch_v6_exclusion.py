#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
SOURCE_NOTE = HERE / "post1648ah-fsm-unibranch-source-note.md"
OUT = HERE / "post1648ah-fsm-unibranch-v6-exclusion.json"

EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    v6 = json.loads(V6_PATH.read_text())
    if v6["canonical_sha256_without_this_field"] != EXPECTED_V6_CANONICAL:
        raise ValueError("V6 canonical source regression")
    if v6["witness"]["all140_pairings_sha256"] != EXPECTED_ALL140_SHA:
        raise ValueError("V6 all140 pairing source regression")

    d = int(v6["target"]["d"])
    e = int(v6["target"]["e"])
    row_id = str(v6["target"]["row_id"])
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    exceptional = pairings[92:]
    if len(pairings) != 140 or len(exceptional) != 48:
        raise ValueError("known140 ordering/count regression")
    support = sum(x > 0 for x in exceptional)
    zero_indices = [i + 1 for i, x in enumerate(exceptional) if x == 0]
    if (d, e, row_id) != (186, 266, "g1-d186"):
        raise ValueError("V6 target regression")
    if sum(exceptional) != e:
        raise ValueError("exceptional mass does not equal target e")
    if support != int(v6["witness"]["positive_exceptional_support"]) or support != 47:
        raise ValueError("V6 exceptional support regression")
    if zero_indices != [6]:
        # Stored zero_exceptional_indices is historical zero-based [5].
        raise ValueError(f"V6 zero exceptional label regression: {zero_indices}")

    # FSM §3 exact arithmetic under the bijective-normalization hypothesis.
    # For genus g=1 and N actual surface nodes met by C:
    #   0 = zeros-poles >= 2*k*d - 8*k*N,
    # hence d <= 4*N.
    genus = 1
    N = support
    fsm_actual_node_bound = 16 * genus - 16 + 4 * N
    if fsm_actual_node_bound != 188 or d > fsm_actual_node_bound:
        raise ValueError("unexpected refined FSM arithmetic")

    zeros_lower_per_k = 2 * d
    poles_max_all_minimal_per_k = 8 * N
    poles_max_if_one_nonminimal_per_k = 8 * (N - 1)
    if not (
        poles_max_if_one_nonminimal_per_k < zeros_lower_per_k <= poles_max_all_minimal_per_k
    ):
        raise ValueError("V6 is not in the claimed one-cusp-type slack window")

    # Translation-lattice constraints in FSM: ai positive, ai=0 mod 4,
    # a1+a2=0 mod 8. The unique pair with a1+a2<16 is (4,4).
    admissible_below_16 = [
        [a1, a2]
        for a1 in range(4, 16, 4)
        for a2 in range(4, 16, 4)
        if (a1 + a2) % 8 == 0 and a1 + a2 < 16
    ]
    if admissible_below_16 != [[4, 4]]:
        raise ValueError(f"FSM minimal cusp type regression: {admissible_below_16}")

    # If even one of the N cusp branches is nonminimal, its local pole upper
    # bound drops from 8k to <=0, making total poles <=8k(N-1)<2kd.
    # Therefore every one of the 47 branches must be the unique (4,4) type.
    all_nodes_forced_minimal = True

    # Local A1 quotient calculation from the source note:
    # x=p^2,y=pq,z=q^2 have Q-orders a1/4,(a1+a2)/8,a2/4.
    # At (4,4) these are [1,1,1], so after blowing up the node the
    # strict transform crosses the exceptional curve with multiplicity 1.
    local_invariant_orders_minimal = [1, 1, 1]
    forced_exceptional_pairing_per_met_node = 1
    forced_exceptional_mass = N * forced_exceptional_pairing_per_met_node
    observed_nonunit = [
        {"exceptional_label_1based": i + 1, "pairing": x}
        for i, x in enumerate(exceptional)
        if x > 1
    ]
    contradiction = (
        all_nodes_forced_minimal
        and forced_exceptional_mass == 47
        and e == 266
        and bool(observed_nonunit)
    )
    if not contradiction:
        raise ValueError("unibranch V6 contradiction failed")

    cert = {
        "schema": "STAGE32_POST1648AH_FSM_UNIBRANCH_V6_EXCLUSION_V1",
        "stage": 32,
        "leaf": "POST1648AH_FSM_UNIBRANCH_V6_EXCLUSION",
        "status": "EXACT_BOUNDED_EXCLUSION_UNDER_BIJECTIVE_NORMALIZATION",
        "source_locks": {
            "v6_witness_path": str(V6_PATH.relative_to(ROOT)),
            "v6_witness_canonical_sha256": EXPECTED_V6_CANONICAL,
            "v6_all140_pairings_sha256": EXPECTED_ALL140_SHA,
            "fsm_source_note_path": str(SOURCE_NOTE.relative_to(ROOT)),
            "fsm_source_note_sha256": sha256_bytes(SOURCE_NOTE.read_bytes()),
            "primary_reference": "Freitag--Salvati Manni, Michigan Math. J. 65 (2016), Theorem 3.1 and proof, DOI 10.1307/mmj/1480734014",
        },
        "v6_exact_data": {
            "row_id": row_id,
            "degree_d": d,
            "geometric_genus_under_test": genus,
            "exceptional_mass_e": e,
            "positive_exceptional_support": support,
            "zero_exceptional_labels_1based": zero_indices,
            "exceptional_pairings": exceptional,
            "exceptional_pairing_max": max(exceptional),
            "exceptional_nonunit_positive_count": len(observed_nonunit),
            "exceptional_nonunit_positive_entries": observed_nonunit,
        },
        "fsm_refinement": {
            "hypothesis": "normalization_map_is_bijective (unibranch over every surface node)",
            "actual_node_count_N": N,
            "refined_degree_bound_formula": "d <= 16*g - 16 + 4*N",
            "refined_degree_upper_bound": fsm_actual_node_bound,
            "degree_survives_crude_refined_bound": d <= fsm_actual_node_bound,
            "zeros_lower_order_per_k": zeros_lower_per_k,
            "poles_upper_order_per_k_if_all_N_minimal": poles_max_all_minimal_per_k,
            "poles_upper_order_per_k_if_at_least_one_nonminimal": poles_max_if_one_nonminimal_per_k,
            "translation_lattice_unique_cusp_type_below_sum16": admissible_below_16,
            "all_47_node_branches_forced_to_cusp_type": [4, 4],
        },
        "local_A1_resolution": {
            "node_model": "Spec C[x,y,z]/(xz-y^2) = C^2/{+-1}, x=p^2,y=pq,z=q^2",
            "minimal_cusp_invariant_orders": local_invariant_orders_minimal,
            "blowup_resolves_A1_node": True,
            "minimal_cusp_strict_transform_exceptional_intersection": forced_exceptional_pairing_per_met_node,
            "forced_total_exceptional_mass_under_unibranch_V6": forced_exceptional_mass,
            "observed_total_exceptional_mass": e,
            "contradiction": True,
        },
        "decision": {
            "bounded_negative": "NO_INTEGRAL_GEOMETRIC_GENUS1_CURVE_IN_THE_V6_CLASS_WITH_BIJECTIVE_NORMALIZATION_MAP_TO_ITS_IMAGE_ON_THE_NODAL_BOX_SURFACE",
            "remaining_open_case": "ANY_V6_GENUS1_CARRIER_MUST_BE_MULTIBRANCH_OVER_AT_LEAST_ONE_OF_THE_47_MET_SURFACE_NODES",
            "member_level_gap_closed": False,
            "next_exact_route": "QUANTIFY_MULTIBRANCH_LOCAL_TYPES_USING_EXCEPTIONAL_PAIRINGS_AND_FSM_CUSP_POLE_BUDGET",
        },
        "firewalls": {
            "does_not_exclude_multibranch_integral_genus1_carrier": True,
            "does_not_prove_all_low_genus_curves_are_known140": True,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_credit": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AH_FSM_UNIBRANCH_V6_EXCLUSION",
        "degree": d,
        "node_support": N,
        "exceptional_mass_observed": e,
        "exceptional_mass_forced_unibranch": forced_exceptional_mass,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
