#!/usr/bin/env python3
"""Assemble the first exact Stage33-12 arithmetic-HS obstruction inventory.

This is a local deterministic adapter over audited repository certificates.  It
computes no new Brauer class and deliberately keeps the localization connecting
map (Stage A) separate from the Hochschild--Serre differential (Stage B).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
ROOT = STAGE33.parent.parent


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def canonical_sha256(obj: dict) -> str:
    payload = dict(obj)
    recorded = payload.pop("canonical_sha256", None)
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    if recorded is not None and recorded != digest:
        raise SystemExit(f"canonical SHA mismatch: recorded={recorded} computed={digest}")
    return digest


def require(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(message)


handoff09 = load("stages/stage33/33-09/handoff.json")
handoff10 = load("stages/stage33/33-10/handoff.json")
exit11 = load(
    "stages/stage33/33-11g/stage33-11g-hostile-audit-exact-exit-certificate.json"
)
hs_problem = load("stages/stage33/33-07/arithmetic-hs-descent-problem.json")
odd = load("stages/stage33/33-07/proper-brauer-odd-invariants-zero.json")
proper2 = load("stages/stage33/33-07/proper-brauer2-from-discriminant.json")
br0b = load("stages/stage33/33-07/br0b-boundary-raw-residue-map.json")
finite = load("stages/stage33/33-07/br0g-finite-ramified-residue-presentation.json")
explicit = load("stages/stage33/33-08/audit-state.json")
controller = load("stages/stage33/controller.json")

locks = {
    "stage33_09_handoff_sha256": canonical_sha256(handoff09),
    "stage33_10_handoff_sha256": canonical_sha256(handoff10),
    "stage33_11g_certificate_sha256": canonical_sha256(exit11),
    "arithmetic_hs_problem_sha256": canonical_sha256(hs_problem),
    "proper_brauer_odd_invariants_sha256": canonical_sha256(odd),
    "proper_brauer2_from_discriminant_sha256": canonical_sha256(proper2),
    "br0b_boundary_raw_residue_map_sha256": canonical_sha256(br0b),
    "finite_ramified_presentation_sha256": canonical_sha256(finite),
    "stage33_08_audit_state_content_sha256": canonical_sha256(explicit),
}

require(
    locks["stage33_10_handoff_sha256"]
    == "4dbbfa8d208026e8ccb47915e66eb4bedef327ccf5b6f8c6c9caa7e74a64028f",
    "Stage33-10 authoritative handoff changed",
)
require(
    locks["stage33_11g_certificate_sha256"]
    == "233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e",
    "Stage33-11g authoritative exit changed",
)
require(handoff09["status"] == "CLOSED_EXACT", "Stage33-09 is not closed exact")
require(
    handoff10["status"] == "CLOSED_EXACT",
    "Stage33-10 is not hostile-audited closed exact",
)
repair_children = {child["id"]: child for child in controller["repair_children"]}
require(
    repair_children["33-10"]["status"] == "CLOSED_EXACT_HOSTILE_AUDIT_PASS"
    and repair_children["33-10"]["audit_passed"] is True,
    "Stage33-10 controller hostile-audit state regressed",
)
require(
    exit11["exact_result"]["arithmetic_localization_connecting_map"]
    == "COMPUTED_EXACT_ZERO_MAP",
    "Stage33-11 connecting map is not the audited zero map",
)
require(
    exit11["exact_result"]["connecting_columns_exact_audited"] == "26/26",
    "Stage33-11 audited coverage regression",
)
require(odd["repair_reduced_to_two_primary"] is True, "odd-primary repair is open")
require(
    odd["constant_odd_boundary_cokernel_globally_liftable_part"] == "0",
    "unexpected odd-primary boundary cokernel lift",
)
require(
    proper2["proper_Br2_joint_v4_fixed_dimension_f2"] == 10,
    "proper geometric Br[2] invariant dimension regression",
)
require(
    br0b["induced_left_filtration_boundary_map_injective"] is True,
    "BR0B left-filtration injection regression",
)
require(
    explicit["accepted_exact_prefix"]["u44_explicit_q_defined_quaternion_representatives"]
    == 44,
    "U44 explicit representative regression",
)
require(
    explicit["accepted_exact_prefix"]["j2_q_defined_generic_corestriction_csa"] is True,
    "J2 exact representative regression",
)
require(
    finite["diagnostic_quotient_by_U44"] == "(Z/2)^23 direct_sum (Z/4)^3",
    "finite quotient regression",
)
require(
    controller["stage33_progress"] == "6/11"
    and controller["stage33_07"]["unit_closed"] is False
    and controller["stage33_08_released"] is False
    and controller["stage33_40_released"] is False,
    "Stage33 firewall regression",
)

constant_two_cokernel = odd["remaining_two_primary_constant_unknown"]
finite_two_group = odd["remaining_finite_two_primary_hs_unknown"]
finite_direction_ids = [f"A2_{i:02d}" for i in range(1, 27)]

certificate = {
    "schema": "STAGE33_12_EXACT_ARITHMETIC_HS_OBSTRUCTION_INVENTORY_V1",
    "stage": "33",
    "unit": "33-12",
    "pr": 1460,
    "source_locks": locks,
    "audited_interface_assembly": {
        "stage33_09_picard_equivariant_transport": "CLOSED_EXACT",
        "stage33_10_absolute_receiver": handoff10["exact_receiver"]["absolute_H1"],
        "stage33_10_E_L_splitting_claimed": False,
        "stage33_10_finite_v4_shortcut": "EXPLICITLY_REPLACED",
        "stage33_11_connecting_map": "COMPUTED_EXACT_ZERO_MAP",
        "stage33_11_connecting_columns_exact_audited": "26/26",
    },
    "two_stage_separation": {
        "stage_A_localization_connecting_map": "CLOSED_EXACT_ZERO_ON_ALL_26_FINITE_DIRECTIONS",
        "stage_B_hoch_schild_serre_d2": "NOT_YET_COMPUTED_ON_REMAINING_TWO_PRIMARY_BLOCKS",
        "connecting_zero_implies_hs_d2_zero_without_adapter": False,
        "connecting_zero_implies_global_q_lift_without_adapter": False,
    },
    "known_q_defined_blocks": {
        "br0b_all_primary": {
            "status": "Q_DEFINED_ACCOUNTED",
            "boundary_map_injective": True,
            "hs_d2": "ZERO_BECAUSE_THE_BLOCK_IS_ALREADY_IN_THE_IMAGE_OF_Br(U)",
        },
        "u44": {
            "status": "44_EXPLICIT_Q_DEFINED_QUATERNION_CLASSES",
            "hs_d2": "ZERO_BECAUSE_THE_BLOCK_IS_ALREADY_IN_THE_IMAGE_OF_Br(U)",
        },
        "j2": {
            "status": "Q_DEFINED_EXACT_ORDER_2_PROPER_CLASS",
            "hs_d2": "ZERO_BECAUSE_THE_CLASS_IS_ALREADY_IN_THE_IMAGE_OF_Br(U)",
        },
        "seven_line": {"group": "0", "hs_d2": "ZERO_VACUOUSLY"},
    },
    "odd_primary_completion": {
        "proper_geometric_brauer_odd_gq_invariants": "0",
        "constant_odd_boundary_cokernel_globally_liftable_part": "0",
        "constant_odd_global_image_equals_br0b_odd_image": True,
        "new_odd_primary_q_defined_residue_lifts_required": 0,
        "status": "EXACT_COMPLETE_NO_NEW_ODD_PRIMARY_BLOCK",
    },
    "remaining_two_primary_obstruction_blocks": [
        {
            "block_id": "C2_CONSTANT_COKERNEL",
            "group": constant_two_cokernel,
            "full_cokernel_claimed_globally_liftable": False,
            "liftable_subgroup_exact_reduction": {
                "proper_geometric_br2_gq_invariant_dimension_f2": 10,
                "known_q_defined_zero_boundary_subgroup": "<J2> ~= Z/2",
                "known_q_defined_zero_boundary_subgroup_dimension_f2": 1,
                "liftable_residue_classes_modulo_BR0B_inject_into": "Br(Sbar)[2]^G_Q / image(Q-defined zero-boundary proper classes)",
                "therefore_dimension_upper_bound_f2": 9,
                "therefore_cardinality_upper_bound": 512,
                "therefore_exponent": 2,
                "proof": "Two Q-defined lifts with the same constant residue differ by a Q-defined zero-boundary class. A lift whose geometric restriction is zero is algebraic and already lies in BR0B. Hence liftable constant-residue classes modulo BR0B inject into the proper invariant quotient; the nonzero Q-defined zero-boundary class J2 removes at least one of its ten dimensions.",
            },
            "localization_connecting_map_status": "NOT_CLAIMED_BY_THE_26_DIRECTION_CERTIFICATE",
            "hs_d2_status": "UNCOMPUTED_PARAMETRIC_MAP",
            "global_q_residue_lift_status": "UNRESOLVED",
        },
        {
            "block_id": "F26_FINITE_AFTER_U44",
            "group": finite_two_group,
            "invariant_factor_generator_count": 26,
            "order2_factors": 23,
            "order4_factors": 3,
            "named_direction_ids": finite_direction_ids,
            "localization_connecting_map_status": "ZERO_EXACT_AUDITED_26_OF_26",
            "hs_d2_status": "26_NAMED_VALUES_UNCOMPUTED",
            "global_q_residue_lift_status": "26_NAMED_LIFTS_UNRESOLVED",
        },
    ],
    "exact_remaining_work": {
        "unresolved_block_count": 2,
        "unresolved_parametric_blocks": ["C2_CONSTANT_COKERNEL"],
        "unresolved_finite_named_directions": finite_direction_ids,
        "unresolved_finite_named_direction_count": 26,
        "next_leaf": "COMPUTE_C2_CONSTANT_COKERNEL_HS_MAP_AND_F26_26_NAMED_HS_D2_VALUES_OR_EXPLICIT_Q_DEFINED_LIFTS",
    },
    "stage33_12_exit": {
        "arithmetic_hs_d2_computed": False,
        "global_q_br0g_residue_lifts_complete": False,
        "complete_relevant_q_defined_class_list_for_stage33_brauer_scope": False,
        "stage33_07_hostile_reaudit": "NOT_RUN",
        "stage33_12_closed": False,
    },
    "firewalls": {
        "stage33_progress": "6/11",
        "stage33_07_closed": False,
        "stage33_08_released": False,
        "stage33_40_released": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}

certificate["canonical_sha256"] = hashlib.sha256(
    json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()

stage12 = repair_children["33-12"]
require(
    stage12["exact_obstruction_inventory_materialized"] is True
    and stage12["exact_obstruction_inventory_sha256"] == certificate["canonical_sha256"],
    f"Stage33-12 controller inventory writeback is missing or stale; expected {certificate['canonical_sha256']}",
)
require(
    controller["stage33_07"]["stage33_12_exact_obstruction_inventory_sha256"]
    == certificate["canonical_sha256"]
    and controller["stage33_07"]["arithmetic_hs_d2_computed"] is False
    and controller["stage33_07"]["global_q_br0g_residue_lifts_complete"] is False,
    "Stage33-07 controller checkpoint is missing or over-promoted",
)

output = HERE / "stage33-12-exact-obstruction-inventory.json"
output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(
    json.dumps(
        {
            "success": True,
            "known_q_defined_hs_blocks_zero": 4,
            "odd_primary_new_lifts_required": 0,
            "remaining_two_primary_blocks": 2,
            "remaining_finite_named_hs_values": 26,
            "stage33_12_closed": False,
            "certificate_sha256": certificate["canonical_sha256"],
        },
        indent=2,
        sort_keys=True,
    )
)
