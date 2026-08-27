#!/usr/bin/env python3
"""Freeze the exact missing input for the Stage33-07 order-two delta_loc leaf.

The retained stack now gives both ends of the finite diagnostic problem:

  source A[2] = (Z/2)^26
  receiver H^1(V4, Br(Sbar)[2]) = (Z/2)^16.

That does *not* determine the connecting map.  The map is the extension class
of the geometric residue-lift torsor.  To compute a column for a source basis
vector r, one must choose a geometric lift b and compute

    (cc(b)-b, ct(b)-b)

in the exact proper Br(Sbar)[2] coordinates.  The pair is then reduced modulo
coboundaries to the certified H^1(V4,Br[2]) quotient coordinates.

The hostile audit proves existence of compatible geometric lifts over Qbar but
provides no chosen lift section or Galois action on such lifts.  It also does
not prove that the full arithmetic extension action factors through the V4
used for the proper Br2 diagnostic.  This certificate records that precise
input gap and forbids synthesizing a 16x26 matrix from endpoint dimensions.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent

EXPECTED = {
    "two-primary-residue-invariant-basis.json": (
        "STAGE33_07_TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_V1",
        "f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939",
    ),
    "proper-brauer2-from-discriminant.json": (
        "STAGE33_07_PROPER_BRAUER2_FROM_DISCRIMINANT_V1",
        "c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf",
    ),
    "order2-localization-receiver.json": (
        "STAGE33_07_ORDER2_LOCALIZATION_RECEIVER_V1",
        "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda",
    ),
}


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(name):
    schema, expected = EXPECTED[name]
    x = json.loads((HERE / name).read_text(encoding="utf-8"))
    claimed = x["canonical_sha256"]
    body = dict(x)
    body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if claimed != expected or actual != expected:
        raise SystemExit(
            f"source lock moved for {name}: claimed={claimed} actual={actual}"
        )
    if x["schema"] != schema:
        raise SystemExit(f"schema regression for {name}")
    return x


ib = load_locked("two-primary-residue-invariant-basis.json")
br2 = load_locked("proper-brauer2-from-discriminant.json")
recv = load_locked("order2-localization-receiver.json")
hs = json.loads((HERE / "arithmetic-hs-descent-problem.json").read_text(encoding="utf-8"))
a08 = json.loads((S33 / "33-08" / "audit-state.json").read_text(encoding="utf-8"))

if hs["schema"] != "STAGE33_07_ARITHMETIC_HS_DESCENT_PROBLEM_V1":
    raise SystemExit("HS problem schema regression")
if hs["boundary_candidates_not_yet_promoted_to_global_q_classes"]["finite_ramified_after_u44"]["exact_unknown_quotient"] != "(Z/2)^23 direct_sum (Z/4)^3":
    raise SystemExit("finite HS quotient regression")
if not hs["geometric_lift_fiber"]["compatible_boundary_tuples_lift_over_Qbar"]:
    raise SystemExit("geometric Qbar lift existence regression")
if hs["arithmetic_hs_obstruction_package"]["blanket_global_gersten_surjectivity_used"]:
    raise SystemExit("global Gersten firewall regression")
if not a08["theorem_scope_regression"]["geometric_global_residue_lift_over_qbar_repaired"]:
    raise SystemExit("Stage33-08 geometric lift repair regression")
if a08["theorem_scope_regression"]["arithmetic_q_descent_certified"]:
    raise SystemExit("Stage33-08 arithmetic descent firewall regression")

if recv["finite_source_order2_dimension_f2"] != 26:
    raise SystemExit("source A[2] dimension regression")
if recv["finite_receiver_module_dimension_f2"] != 14:
    raise SystemExit("proper Br2 module dimension regression")
if recv["finite_receiver_Z1_dimension_f2"] != 20:
    raise SystemExit("finite receiver Z1 dimension regression")
if recv["finite_receiver_B1_dimension_f2"] != 4:
    raise SystemExit("finite receiver B1 dimension regression")
if recv["finite_receiver_H1_dimension_f2"] != 16:
    raise SystemExit("finite receiver H1 dimension regression")
if br2["finite_v4_H1_proper_Br2"]["absolute_H1_identified_with_finite_H1"]:
    raise SystemExit("absolute H1 identification firewall regression")
if recv["localization_extension_class_computed"]:
    raise SystemExit("receiver unexpectedly claims extension-class computation")

# Exact source basis names are frozen so a later extension certificate must
# provide one lift/cocycle record for every source coordinate, without loss or
# duplication.
source_names = [x["name"] for x in recv["finite_source_basis"]]
if source_names != [f"A2_{i:02d}" for i in range(1, 27)]:
    raise SystemExit("source basis naming/order regression")

required_per_source_record = {
    "source_basis_name": "A2_01 ... A2_26",
    "chosen_geometric_lift_id": "required",
    "chosen_lift_residue_rehash_matches_source": "required true",
    "cc_lift_difference_proper_Br2_f2_14": "required 14-bit vector",
    "ct_lift_difference_proper_Br2_f2_14": "required 14-bit vector",
    "pair_satisfies_certified_V4_cocycle_equations": "required true",
    "finite_V4_H1_coordinates_f2_16": "required 16-bit quotient coordinate",
}

cert = {
    "schema": "STAGE33_07_ORDER2_LOCALIZATION_EXTENSION_INPUT_GAP_V1",
    "source_locks": {
        "two_primary_residue_invariant_basis_sha256": EXPECTED["two-primary-residue-invariant-basis.json"][1],
        "proper_brauer2_from_discriminant_sha256": EXPECTED["proper-brauer2-from-discriminant.json"][1],
        "order2_localization_receiver_sha256": EXPECTED["order2-localization-receiver.json"][1],
        "arithmetic_hs_descent_problem_sha256": hs["canonical_sha256"],
        "stage33_08_audit_state": "stages/stage33/33-08/audit-state.json",
    },
    "exact_known_endpoints": {
        "source_order2_group": "(Z/2)^26",
        "source_order2_dimension_f2": 26,
        "proper_geometric_Br2_dimension_f2": 14,
        "finite_V4_Z1_dimension_f2": 20,
        "finite_V4_B1_dimension_f2": 4,
        "finite_V4_H1_dimension_f2": 16,
        "geometric_compatible_residue_lifts_over_Qbar_exist": True,
    },
    "connecting_map_contract": {
        "finite_diagnostic_map": "delta_loc,V4: (Z/2)^26 -> H^1(V4,Br(Sbar)[2]) ~= (Z/2)^16",
        "column_formula": "A2_i |-> class of (cc(lift_i)-lift_i, ct(lift_i)-lift_i) modulo B1",
        "matrix_shape_when_computable": [16, 26],
        "source_basis_order": source_names,
        "receiver_coordinate_source": "order2-localization-receiver.json finite_receiver_H1_quotient_representatives_f2_28",
        "required_per_source_record": required_per_source_record,
    },
    "missing_exact_inputs": {
        "chosen_geometric_lift_for_each_A2_source": False,
        "residue_rehash_for_each_chosen_geometric_lift": False,
        "cc_action_on_each_chosen_geometric_lift": False,
        "ct_action_on_each_chosen_geometric_lift": False,
        "lift_differences_identified_in_proper_Br2_f2_14_coordinates": False,
        "geometric_residue_lift_extension_presented_as_exact_V4_module": False,
        "full_arithmetic_extension_action_proved_to_factor_through_this_V4": False,
    },
    "why_dimensions_do_not_determine_delta_loc": (
        "The 26-dimensional invariant residue source and the 16-dimensional finite V4 H1 receiver determine only the domain and codomain. "
        "The connecting homomorphism is the extension class of the geometric residue-lift torsor and requires the Galois action on chosen lifts (or an equivalent exact extension-module presentation)."
    ),
    "prohibited_shortcuts": [
        "do not infer delta_loc=0 from Galois-invariant residue tuples",
        "do not infer delta_loc from source/receiver dimensions or ranks alone",
        "do not identify finite H^1(V4,Br[2]) with absolute H^1(G_Q,Br[2]) without a separate proof",
        "do not promote geometric Qbar lift existence to Q-defined global Brauer lifts",
        "do not synthesize a 16x26 matrix without lift-difference or equivalent extension data",
    ],
    "finite_V4_delta_loc_matrix_computed": False,
    "absolute_delta_loc_computed": False,
    "absolute_H1_identified_with_finite_V4_H1": False,
    "boundary_residual_promoted_to_global_q_classes": False,
    "constant_cokernel_HS_d2_computed": False,
    "actual_index512_k3_glue_identified": False,
    "arithmetic_HS_closed": False,
    "new_smallest_exact_kernel": "R33-BR2A-ORDER2-GEOMETRIC-LIFT-EXTENSION-COCYCLE",
    "next_exact_leaf": (
        "L33-07-MATERIALIZE-26-CHOSEN-QBAR-ORDER2-RESIDUE-LIFTS-AND-"
        "CC-CT-DIFFERENCE-COCYCLES-IN-PROPER-BR2-COORDINATES"
    ),
    "unit_status": "RUNNING_REPAIR",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
(HERE / "order2-localization-extension-input-gap.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "source_A2_dimension_f2": 26,
    "finite_V4_H1_dimension_f2": 16,
    "finite_V4_delta_loc_matrix_computed": False,
    "new_smallest_exact_kernel": cert["new_smallest_exact_kernel"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "stage33_progress": "6/11",
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
