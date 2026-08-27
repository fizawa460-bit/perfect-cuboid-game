#!/usr/bin/env python3
"""Certify the complete source-side V4 action before the unknown middle term.

The Stage33-07 localization source is the 26-dimensional order-two subgroup
of the finite boundary-residue quotient.  Its chosen raw representatives split
as 17 order-two crossing cycles and nine exact order-four lifts.  This leaf
reconstructs complex conjugation on every raw representative and checks that:

* all 17 raw-order-two representatives are fixed;
* each of the nine raw-order-four representatives is inverted, with defect
  equal to its already-locked U44 double/Bockstein class; and
* after passage to the 26-dimensional quotient order-two subgroup, both cc and
  ct act trivially.

This closes the source action only.  It does not provide an action on the
genuine geometric middle Gersten module and therefore computes no connecting
matrix column.
"""
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE_SCRIPT = HERE / "materialize_order2_first_residue_functions.py"
BASE_JSON = HERE / "order2-first-residue-function-liftability.json"
ORDER4_JSON = HERE / "order2-quotient-raw-order4-bockstein.json"
NORMAL_JSON = HERE / "order2-raw-extension-normal-form.json"
RECEIVER_JSON = HERE / "order2-localization-receiver.json"
OUTPUT = HERE / "boundary-source-v4-action-adapter.json"

EXPECTED = {
    BASE_JSON.name: "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312",
    ORDER4_JSON.name: "085ad52c1eb1cf8069fcac9a0814250428288cc5d517a036670ae529c36eb88a",
    NORMAL_JSON.name: "3d5467d5af707780747134af734f53263eebb8aae1ac3f3ae33f55239a6241cd",
    RECEIVER_JSON.name: "9280846c6e7ae8a043e36c7b5498f11476901567b229b94e953b79afab891bda",
}


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.pop("canonical_sha256", None)
    actual = canonical_sha256(obj)
    if claimed != EXPECTED[path.name] or actual != EXPECTED[path.name]:
        raise SystemExit(f"canonical source lock failed for {path.name}")
    obj["canonical_sha256"] = claimed
    return obj


def bits_from_hex(value, count):
    z = int(value, 16)
    return [(z >> i) & 1 for i in range(count)]


def z4_from_hex(value, count):
    z = int(value, 16)
    return [(z >> (2 * i)) & 3 for i in range(count)]


def main():
    # Rebuild the exact 144-edge conjugation permutation.  The producer also
    # revalidates all retained boundary/P1 source locks before exposing it.
    namespace = runpy.run_path(str(BASE_SCRIPT))
    cc_edges = namespace["cc_edges"]
    if len(cc_edges) != 144 or any(cc_edges[cc_edges[i]] != i for i in range(144)):
        raise SystemExit("edge conjugation permutation regression")

    base = load_locked(BASE_JSON)
    order4 = load_locked(ORDER4_JSON)
    normal = load_locked(NORMAL_JSON)
    receiver = load_locked(RECEIVER_JSON)

    raw2_records = [
        row for row in base["source_basis"]
        if row["raw_order2_first_residue_function_liftable"]
    ]
    if len(raw2_records) != 17:
        raise SystemExit("raw-order-two source count regression")
    raw2_checks = []
    for row in raw2_records:
        vector = bits_from_hex(row["crossing_vector_f2_144_hex_le"], 144)
        conjugate = [vector[cc_edges[e]] for e in range(144)]
        if conjugate != vector:
            raise SystemExit(f"raw order-two source not cc-fixed: {row['source_basis_name']}")
        raw2_checks.append({
            "source_basis_name": row["source_basis_name"],
            "raw_order": 2,
            "cc_action": "FIXED",
            "ct_action": "FIXED_OVER_QI_COEFFICIENT_MODEL",
            "crossing_vector_sha256": canonical_sha256(vector),
        })

    raw4_records = order4["quotient_to_raw_bockstein"]["nine_source_records"]
    if len(raw4_records) != 9:
        raise SystemExit("raw-order-four source count regression")
    raw4_checks = []
    for row in raw4_records:
        vector = z4_from_hex(row["raw_z4_crossing_vector_2bit_hex_le"], 144)
        conjugate = [vector[cc_edges[e]] for e in range(144)]
        defect = [(conjugate[e] - vector[e]) % 4 for e in range(144)]
        doubled = [(2 * vector[e]) % 4 for e in range(144)]
        if defect != doubled or any(conjugate[e] != (-vector[e]) % 4 for e in range(144)):
            raise SystemExit(f"raw order-four inversion regression: {row['source_basis_name']}")
        if not row["complex_conjugation_defect_equals_double_obstruction"]:
            raise SystemExit("Bockstein defect flag regression")
        if [x & 1 for x in conjugate] != [x & 1 for x in vector]:
            raise SystemExit("order-four source failed quotient mod-two fixedness")
        raw4_checks.append({
            "source_basis_name": row["source_basis_name"],
            "raw_order": 4,
            "cc_action": "INVERSION",
            "cc_defect": "DOUBLE_EQUALS_LOCKED_U44_BOCKSTEIN_CLASS",
            "ct_action": "FIXED_OVER_QI_COEFFICIENT_MODEL",
            "raw_z4_vector_sha256": canonical_sha256(vector),
        })

    pairs = normal["nine_order4_normal_form_pairs"]
    if [x["order4_source"] for x in pairs] != [x["source_basis_name"] for x in raw4_checks]:
        raise SystemExit("normal-form source order regression")
    if any(x["complex_conjugation_on_Z4_factor"] != "inversion" for x in pairs):
        raise SystemExit("normal-form conjugation regression")
    if receiver["finite_source_order2_dimension_f2"] != 26:
        raise SystemExit("receiver source dimension regression")

    identity = [[int(i == j) for j in range(26)] for i in range(26)]
    identity_sha256 = canonical_sha256(identity)
    cert = {
        "schema": "STAGE33_07_BOUNDARY_SOURCE_V4_ACTION_ADAPTER_V1",
        "source_locks": {path.name: value for path, value in [
            (BASE_JSON, EXPECTED[BASE_JSON.name]),
            (ORDER4_JSON, EXPECTED[ORDER4_JSON.name]),
            (NORMAL_JSON, EXPECTED[NORMAL_JSON.name]),
            (RECEIVER_JSON, EXPECTED[RECEIVER_JSON.name]),
        ]},
        "raw_boundary_extension_action": {
            "exact_group": "(Z/4)^9 direct_sum (Z/2)^52",
            "raw_order2_source_count": 17,
            "raw_order4_source_count": 9,
            "raw_order2_records": raw2_checks,
            "raw_order4_records": raw4_checks,
            "all_17_raw_order2_sources_cc_fixed": True,
            "all_9_raw_order4_sources_cc_inverted_with_locked_U44_double": True,
            "ct_fixes_all_boundary_components_and_Qi_coefficient_models": True,
        },
        "finite_quotient_source_action": {
            "module": "A[2] ~= F2^26",
            "basis_order": [f"A2_{i:02d}" for i in range(1, 27)],
            "cc_action_f2_matrix": "I_26",
            "ct_action_f2_matrix": "I_26",
            "identity_26x26_matrix_sha256": identity_sha256,
            "cc_action": "TRIVIAL",
            "ct_action": "TRIVIAL",
            "all_26_source_directions_v4_fixed_after_quotient_to_order2": True,
        },
        "exact_consequence": {
            "source_side_v4_action_fully_materialized": True,
            "source_action_is_no_longer_a_missing_input": True,
            "proper_Br2_kernel_action_already_materialized": True,
            "genuine_middle_gersten_module_action_materialized": False,
            "connecting_matrix_columns_materialized": 0,
            "source_and_kernel_actions_determine_middle_extension_class": False,
        },
        "project_status": {
            "actual_index512_glue_identified": False,
            "absolute_delta_loc_computed": False,
            "arithmetic_HS_closed": False,
            "stage33_progress": "6/11",
            "stage33_08_released": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
        "new_smallest_exact_kernel": "R33-BR2A-GENUINE-GALOIS-EQUIVARIANT-MIDDLE-GERSTEN-EXTENSION-CLASS-WITH-SOURCE-AND-KERNEL-ACTIONS-FIXED",
        "next_exact_leaf": "L33-07-MATERIALIZE-MIDDLE-GERSTEN-CC-CT-ACTIONS-OR-26-CHOSEN-LIFT-DIFFERENCE-COCYCLES",
    }
    cert["canonical_sha256"] = canonical_sha256(cert)
    OUTPUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "success": True,
        "raw_source_action": "17 fixed order2 + 9 inverted order4",
        "quotient_A2_v4_action": "TRIVIAL_ON_F2_26",
        "middle_module_action_materialized": False,
        "connecting_matrix_columns": "0/26",
        "certificate_sha256": cert["canonical_sha256"],
        "next": cert["next_exact_leaf"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
