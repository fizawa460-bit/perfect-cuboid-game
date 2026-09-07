#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

V6_PATH = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"
AH_PATH = HERE / "post1648ah-fsm-unibranch-v6-exclusion.json"
SOURCE_NOTE = HERE / "post1648ai-fsm-nodewise-unibranch-source-note.md"
OUT = HERE / "post1648ai-fsm-nodewise-unibranch-v6-exclusion.json"

EXPECTED_V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
EXPECTED_ALL140_SHA = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
EXPECTED_PARENT_AH_CANONICAL = "6ee4ebdf266deec5d7aa865d5b088211f8fffadc99be1119b8cc779c4be9f043"
EXPECTED_SOURCE_NOTE_SHA256 = "406be5b1e97dc8048daa74dff01034743eb548f3da88a5cd32c753f19d68de8a"


def csha(value: object) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    if sha256_bytes(SOURCE_NOTE.read_bytes()) != EXPECTED_SOURCE_NOTE_SHA256:
        raise ValueError("AI FSM source note moved")
    source_text = SOURCE_NOTE.read_text(encoding="utf-8")
    required_source_fragments = [
        "T` is holomorphic away from the 48 exceptional curves",
        "the proof invokes global bijectivity at the pole-count sentence",
        "for every box-surface node s, card(nu^{-1}(s)) <= 1",
        "Smooth-ambient-locus singularities may still coexist",
    ]
    for fragment in required_source_fragments:
        if fragment not in source_text:
            raise ValueError(f"source-note semantic lock moved: {fragment}")

    ah = json.loads(AH_PATH.read_text(encoding="utf-8"))
    if ah.get("canonical_sha256_without_this_field") != EXPECTED_PARENT_AH_CANONICAL:
        raise ValueError("parent AH canonical moved")
    if csha(ah) != EXPECTED_PARENT_AH_CANONICAL:
        raise ValueError("parent AH canonical recomputation moved")
    if ah["fsm_refinement"]["hypothesis"] != "normalization_map_is_globally_bijective":
        raise ValueError("parent AH published hypothesis moved")
    if not ah["firewalls"]["smooth_ambient_locus_curve_singularity_branch_open"]:
        raise ValueError("parent AH smooth-locus branch was not open")

    v6 = json.loads(V6_PATH.read_text(encoding="utf-8"))
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
    zero_labels = [i + 1 for i, x in enumerate(exceptional) if x == 0]
    if (row_id, d, e, support, zero_labels) != ("g1-d186", 186, 266, 47, [6]):
        raise ValueError("V6 exact target/support regression")
    if sum(exceptional) != e:
        raise ValueError("V6 exceptional mass regression")

    genus = 1
    zeros_lower_per_k = 2 * d
    poles_all_minimal_per_k = 8 * support
    poles_one_nonminimal_per_k = 8 * (support - 1)

    if (zeros_lower_per_k, poles_all_minimal_per_k, poles_one_nonminimal_per_k) != (372, 376, 368):
        raise ValueError("FSM V6 budget arithmetic moved")
    if not (poles_one_nonminimal_per_k < zeros_lower_per_k <= poles_all_minimal_per_k):
        raise ValueError("V6 no longer lies in one-nonminimal contradiction window")

    admissible_below_16 = [
        [a1, a2]
        for a1 in range(4, 16, 4)
        for a2 in range(4, 16, 4)
        if (a1 + a2) % 8 == 0 and a1 + a2 < 16
    ]
    if admissible_below_16 != [[4, 4]]:
        raise ValueError("FSM translation-lattice minimal type moved")

    forced_exceptional_mass = support
    contradiction = forced_exceptional_mass == 47 and e == 266 and forced_exceptional_mass != e
    if not contradiction:
        raise ValueError("nodewise-unibranch V6 contradiction failed")

    cert = {
        "schema": "STAGE32_POST1648AI_FSM_NODEWISE_UNIBRANCH_V6_EXCLUSION_V1",
        "stage": 32,
        "leaf": "POST1648AI_FSM_NODEWISE_UNIBRANCH_V6_EXCLUSION",
        "status": "EXACT_BOUNDED_EXCLUSION_UNDER_NODEWISE_UNIBRANCH_AT_BOX_SURFACE_NODES",
        "audited_parent": {
            "pr": 1648,
            "hostile_review": 5127517046,
            "audited_exact_head": "673e5cdb6ace160f2bc6be00688ad6084cef97ad",
            "merged_main_commit": "24215fa27a631cd3cb370c0dfd76866dd2e916f1",
            "parent_ah_canonical_sha256": EXPECTED_PARENT_AH_CANONICAL,
        },
        "source_locks": {
            "primary_reference": "Freitag--Salvati Manni, Michigan Math. J. 65 (2016), Theorem 3.1 and proof, DOI 10.1307/mmj/1480734014",
            "fsm_source_note_path": str(SOURCE_NOTE.relative_to(ROOT)),
            "fsm_source_note_sha256": EXPECTED_SOURCE_NOTE_SHA256,
            "parent_ah_path": str(AH_PATH.relative_to(ROOT)),
            "parent_ah_canonical_sha256": EXPECTED_PARENT_AH_CANONICAL,
            "v6_witness_path": str(V6_PATH.relative_to(ROOT)),
            "v6_witness_canonical_sha256": EXPECTED_V6_CANONICAL,
            "v6_all140_pairings_sha256": EXPECTED_ALL140_SHA,
        },
        "proof_adapter": {
            "published_hypothesis": "normalization_map_is_globally_bijective",
            "weaker_sufficient_hypothesis": "for_every_box_surface_node_s_cardinality_of_normalization_fiber_nu_inverse_s_is_at_most_1",
            "smooth_ambient_locus_noninjectivity_allowed": True,
            "tensor_holomorphic_away_from_exceptional_curves": True,
            "poles_only_over_exceptional_divisor": True,
            "nodewise_unibranch_suffices_for_at_most_one_pole_point_per_exceptional_curve": True,
            "smooth_locus_noninjectivity_adds_no_tensor_poles": True,
            "adapter_is_proof_extraction_not_separately_published_theorem": True,
        },
        "v6_exact_data": {
            "row_id": row_id,
            "geometric_genus": genus,
            "degree_d": d,
            "positive_exceptional_support_N": support,
            "zero_exceptional_labels_1based": zero_labels,
            "exceptional_mass_e": e,
        },
        "fsm_budget": {
            "zeros_lower_per_k": zeros_lower_per_k,
            "poles_upper_if_all_47_minimal_per_k": poles_all_minimal_per_k,
            "poles_upper_if_at_least_one_nonminimal_per_k": poles_one_nonminimal_per_k,
            "genus1_divisor_degree_identity": "zeros_minus_poles=0",
            "translation_lattice_unique_positive_type_with_sum_lt_16": [4, 4],
            "all_47_met_node_branches_forced_to_type": [4, 4],
        },
        "local_A1_resolution": {
            "node_model": "Spec C[x,y,z]/(xz-y^2)=C^2/{+-1}; x=p^2,y=pq,z=q^2",
            "minimal_type_invariant_orders": [1, 1, 1],
            "minimal_type_exceptional_intersection": 1,
            "forced_exceptional_mass_under_nodewise_unibranch": forced_exceptional_mass,
            "observed_exceptional_mass": e,
            "contradiction": True,
        },
        "decision": {
            "bounded_negative": "NO_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_UNIBRANCH_OVER_ALL_BOX_SURFACE_NODES",
            "remaining_open_case": "ANY_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_MUST_BE_MULTIBRANCH_OVER_AT_LEAST_ONE_MET_BOX_SURFACE_NODE",
            "smooth_ambient_locus_singularities_may_coexist": True,
            "does_not_claim_all_noninjectivity_is_at_surface_nodes": True,
            "pure_smooth_locus_noninjectivity_with_all_surface_nodes_unibranch_excluded": True,
            "next_exact_route": "QUANTIFY_SURFACE_NODE_MULTIBRANCH_LOCAL_TYPES_USING_EXCEPTIONAL_PAIRINGS_AND_FSM_POLE_BUDGET",
        },
        "firewalls": {
            "integral_genus1_member_materialized": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "controller_promotion_granted": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1648AI_FSM_NODEWISE_UNIBRANCH_V6_EXCLUSION",
        "degree": d,
        "genus": genus,
        "node_support": support,
        "zeros_lower_per_k": zeros_lower_per_k,
        "poles_all_minimal_per_k": poles_all_minimal_per_k,
        "poles_one_nonminimal_per_k": poles_one_nonminimal_per_k,
        "forced_exceptional_mass": forced_exceptional_mass,
        "observed_exceptional_mass": e,
        "remaining_open_case": cert["decision"]["remaining_open_case"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
