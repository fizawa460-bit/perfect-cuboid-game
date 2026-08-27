#!/usr/bin/env python3
"""Freeze the exact construction contract for the 26 mixed-order global Gersten lifts.

The boundary first-residue packages are already exact for all 26 source directions:
17 have raw order two and 9 require raw order four.  This does *not* by itself
produce classes in the geometric function field.  This leaf records, source by
source, the evidence that a future constructor must provide before any Galois
difference or 14x26 L-squareclass entry can receive credit.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST = HERE / "order2-first-residue-function-liftability.json"
NORMAL = HERE / "order2-raw-extension-normal-form.json"
GLCONTRACT = HERE / "order2-gl-restriction-squareclass-contract.json"
OUT = HERE / "mixed-order-global-gersten-lift-contract.json"

EXPECTED = {
    FIRST.name: "85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312",
    NORMAL.name: "3d5467d5af707780747134af734f53263eebb8aae1ac3f3ae33f55239a6241cd",
}


def canonical_sha256(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected=None):
    x = json.loads(path.read_text(encoding="utf-8"))
    claimed = x.get("canonical_sha256")
    if not claimed:
        raise SystemExit(f"missing canonical hash: {path.name}")
    body = dict(x)
    body.pop("canonical_sha256")
    actual = canonical_sha256(body)
    if claimed != actual:
        raise SystemExit(f"canonical hash mismatch: {path.name}: {claimed} != {actual}")
    if expected is not None and claimed != expected:
        raise SystemExit(f"source lock moved: {path.name}: {claimed} != {expected}")
    return x


first = load_locked(FIRST, EXPECTED[FIRST.name])
normal = load_locked(NORMAL, EXPECTED[NORMAL.name])
glc = load_locked(GLCONTRACT)

if first["source_order2_dimension_f2"] != 26:
    raise SystemExit("source dimension regression")
if normal["dimensions"]["quotient_A2_dimension_f2"] != 26:
    raise SystemExit("normal-form source dimension regression")
if normal["constructive_progress"]["global_geometric_Gersten_lifts_materialized_count"] != 0:
    raise SystemExit("a global Gersten lift is now claimed; this contract must be regenerated")
if normal["constructive_progress"]["global_geometric_Gersten_lifts_required_count"] != 26:
    raise SystemExit("global Gersten lift requirement regression")
if glc["source"]["dimension_f2"] != 26 or glc["coefficient"]["dimension_f2"] != 14:
    raise SystemExit("GL restriction contract shape regression")
if glc["extension_classification_over_GL"]["project_data_shape"] != [14, 26]:
    raise SystemExit("14x26 project tensor contract regression")

source_records = first["source_basis"]
if len(source_records) != 26:
    raise SystemExit("first-residue source record count regression")
source_names = [r["source_basis_name"] for r in source_records]
if len(set(source_names)) != 26:
    raise SystemExit("duplicate source names")
if glc["source"]["basis_names"] != source_names:
    raise SystemExit("GL contract source basis order moved")

order4_pairs = {p["order4_source"]: p for p in normal["nine_order4_normal_form_pairs"]}
if len(order4_pairs) != 9:
    raise SystemExit("order4 normal-form pair count regression")

raw2_names = []
raw4_names = []
obligations = []
required_fields = [
    "global_geometric_Gersten_lift_representation",
    "function_field_model_source_lock",
    "boundary_residue_equality_on_all_72_components",
    "off_boundary_codimension1_residue_inventory",
    "off_boundary_residue_zero_or_explicit_cancellation_certificate",
    "cc_transformed_lift_representation",
    "ct_transformed_lift_representation",
    "cc_difference_in_proper_Br2_F2_14_coordinates",
    "ct_difference_in_proper_Br2_F2_14_coordinates",
]

for r in source_records:
    name = r["source_basis_name"]
    raw2 = bool(r["raw_order2_first_residue_function_liftable"])
    if raw2:
        raw2_names.append(name)
        package = {
            "order": 2,
            "boundary_function_package_sha256": r["full_72_component_function_model_sha256"],
            "nontrivial_boundary_component_count": r["nontrivial_component_function_count"],
            "crossing_vector_f2_144_hex_le": r["crossing_vector_f2_144_hex_le"],
            "bockstein_double_basis_name": None,
        }
    else:
        raw4_names.append(name)
        if name not in order4_pairs:
            raise SystemExit(f"missing order4 normal-form pair for {name}")
        p = order4_pairs[name]
        package = {
            "order": 4,
            "boundary_function_package_sha256": p["raw_order4_function_package_sha256"],
            "nontrivial_boundary_component_count": None,
            "crossing_vector_f2_144_hex_le": None,
            "bockstein_double_basis_name": p["new_u44_double_basis_name"],
            "double_relation": p["double_relation"],
            "complex_conjugation_relation": p["complex_conjugation_relation"],
        }
    obligations.append({
        "source_basis_name": name,
        "mixed_order_boundary_package": package,
        "boundary_first_residue_package_materialized": True,
        "global_geometric_Gersten_lift_materialized": False,
        "required_exact_evidence_before_lift_credit": required_fields + (
            ["order4_lift_double_matches_named_U44_Bockstein_basis_vector"]
            if not raw2 else []
        ),
        "cc_difference_computed": False,
        "ct_difference_computed": False,
        "proper_Br2_difference_coordinates_computed": False,
        "GL_squareclass_column_computed": False,
    })

if len(raw2_names) != 17 or len(raw4_names) != 9:
    raise SystemExit(f"mixed-order partition regression {len(raw2_names)}+{len(raw4_names)}")
if set(raw4_names) != set(order4_pairs):
    raise SystemExit("order4 source names disagree with normal form")

cert = {
    "schema": "STAGE33_07_MIXED_ORDER_GLOBAL_GERSTEN_LIFT_CONTRACT_V1",
    "source_locks": {
        "first_residue_liftability_sha256": first["canonical_sha256"],
        "raw_extension_normal_form_sha256": normal["canonical_sha256"],
        "gl_restriction_squareclass_contract_sha256": glc["canonical_sha256"],
    },
    "field": "L=Q(i,sqrt(2))",
    "galois_generators": ["cc", "ct"],
    "boundary_geometry": {
        "component_count": 72,
        "crossing_count": 144,
        "mixed_order_source_count": 26,
        "raw_order2_source_count": 17,
        "raw_order4_source_count": 9,
        "all_26_boundary_first_residue_packages_materialized": True,
    },
    "global_Gersten_lift_contract": {
        "required_count": 26,
        "materialized_count": 0,
        "credit_rule": "boundary first-residue data alone never promotes a source to a global geometric Gersten/Brauer lift",
        "off_boundary_rule": "every codimension-one divisor outside the frozen 72-component boundary must have zero residue or be included in an explicit exact cancellation certificate",
        "galois_difference_rule": "cc(lift)-lift and ct(lift)-lift must be certified unramified and expressed in the frozen 14-dimensional proper Br(Sbar)[2] basis",
        "source_obligations": obligations,
    },
    "downstream_assembly_contract": {
        "proper_Br2_dimension_f2": 14,
        "source_dimension_f2": 26,
        "GL_project_tensor_shape": [14, 26],
        "GL_project_squareclass_entry_count": 364,
        "assemble_14x26_tensor_before_global_lift_completion": False,
        "consumer_after_squareclasses": "materialize_order2_gl_restriction_kernel_from_span.py",
    },
    "exact_checks": {
        "source_basis_has_26_unique_ordered_names": True,
        "mixed_order_partition_is_17_plus_9": True,
        "nine_order4_sources_match_raw_extension_normal_form": True,
        "all_26_boundary_packages_have_locked_evidence": True,
        "global_Gersten_lift_materialized_count_is_zero": True,
        "all_26_lift_obligations_explicitly_require_boundary_and_off_boundary_residue_checks": True,
        "all_26_lift_obligations_explicitly_require_cc_ct_proper_Br2_difference_coordinates": True,
        "14x26_tensor_firewall_preserved": True,
    },
    "constructive_progress": {
        "quotient_to_raw_Bockstein_extension_normal_form_closed": True,
        "global_Gersten_lift_input_contract_closed": True,
        "global_geometric_Gersten_lifts_materialized_count": 0,
        "global_geometric_Gersten_lifts_required_count": 26,
        "project_14x26_L_squareclass_tensor_materialized": False,
        "absolute_delta_loc_computed": False,
        "arithmetic_HS_closed": False,
    },
    "new_smallest_exact_kernel": "R33-BR2A-26-MIXED-ORDER-FIRST-RESIDUE-GLOBAL-GERSTEN-LIFT-GALOIS-DIFFERENCE-COCYCLE",
    "next_exact_leaf": "L33-07-CONSTRUCT-26-GLOBAL-GEOMETRIC-GERSTEN-LIFTS-WITH-FULL-CODIM1-RESIDUE-CERTIFICATES",
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False,
}
cert["canonical_sha256"] = canonical_sha256(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "mixed_order_partition": "17+9",
    "boundary_first_residue_packages": "26/26",
    "global_Gersten_lifts": "0/26",
    "lift_obligations_frozen": 26,
    "GL_tensor_shape": [14, 26],
    "certificate_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
