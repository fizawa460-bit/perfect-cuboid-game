#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-marked-picard-to-literal-geometry-bridge-gap-v56.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def assert_lock(entry: dict) -> dict:
    path = ROOT / entry["path"]
    assert path.exists(), entry["path"]
    assert git_blob_sha1(path) == entry["git_blob_sha1"], entry["path"]
    return load(path)


def main() -> None:
    d = load(CERT)
    assert d["schema"] == "stage33.e3.mask20_marked_picard_to_literal_geometry_bridge_gap.v56"
    assert d["parent_head"] == "38b37b7ac847993f96d7fae92dd3bbd731444248"

    v52 = assert_lock(d["source_locks"]["v52_literal_cech_gap"])
    v53 = assert_lock(d["source_locks"]["v53_picard_adjoint_candidate"])
    v54 = assert_lock(d["source_locks"]["v54_semantic_u1_binding"])
    v55 = assert_lock(d["source_locks"]["v55_u1_fiber_cardinality"])

    # V52 already bounded the literal-Cech miss without making global absence claims.
    bi52 = v52["bounded_inspection"]
    assert bi52["e3_source"]["proper14_mask_decimal"] == 20
    assert bi52["available_marked_picard_data"]["exact_picard_adjoint_present"] is True
    assert bi52["available_marked_picard_data"]["exact_marked_picard_bridge_present"] is True
    assert bi52["available_marked_picard_data"]["literal_function_divisor_transition_preimage_for_mask20_materialized"] is False
    assert bi52["mask20_literal_preimage_materialized"] is False
    assert bi52["repo_absence_claim"] is False
    assert bi52["mathematical_nonexistence_claim"] is False

    # V53 supplies the exact marked candidate but explicitly not its geometric realization.
    ex53 = v53["exact_computation"]
    assert ex53["input_proper14_mask_decimal"] == 20
    assert ex53["input_support_one_based"] == [3, 5]
    assert ex53["combined"]["source_T_mod_2_coordinate_f2"] == [1, 0]
    assert len(ex53["combined"]["source_half_lattice_numerator_mod2"]) == 20
    g53 = v53["geometric_realization_boundary"]
    assert g53["picard_adjoint_candidate_materialized"] is True
    assert g53["literal_function_divisor_transition_data_for_mask20_materialized"] is False
    assert g53["source_specific_cech_h2_mu2_preimage_materialized"] is False
    assert g53["brauer_image_binding_to_v41_e3_certified_from_literal_geometry"] is False

    # V54 identifies only the semantic quotient label.
    b54 = v54["exact_binding"]
    assert b54["e3_proper14_mask_decimal"] == 20
    assert b54["semantic_half_lattice_label"] == "u1"
    assert b54["semantic_coordinate_f2"] == [1, 0]
    assert b54["exact_vector_match"] is True
    assert v54["source_specificity_firewall"]["e3_identified_with_j2"] is False
    assert v54["geometric_realization_boundary"]["source_specific_full_surface_cech_h2_mu2_preimage_materialized"] is False

    # V55 quantifies why the semantic quotient cannot identify the source point.
    la55 = v55["exact_linear_algebra"]
    pos55 = v55["e3_position"]
    assert la55["u1_fiber_cardinality"] == 4096
    assert pos55["proper14_mask_decimal"] == 20
    assert pos55["other_source_points_with_same_semantic_label_count"] == 4095
    assert pos55["e3_identified_by_semantic_label_alone"] is False
    assert v55["geometric_realization_boundary"]["exact_brauer_image_binding_to_mask20_from_literal_geometry"] is False
    assert v55["geometric_realization_boundary"]["genuine_full_surface_h2_mu2_lift_for_e3"] is False

    chain = d["exact_chain_localization"]
    src = chain["source_object"]
    assert src["proper14_mask_decimal"] == ex53["input_proper14_mask_decimal"] == 20
    assert src["proper14_support_one_based"] == ex53["input_support_one_based"] == [3, 5]
    assert src["marked_picard_adjoint_candidate_materialized"] is True
    assert src["combined_source_T_mod_2_coordinate_f2"] == ex53["combined"]["source_T_mod_2_coordinate_f2"] == [1, 0]
    assert src["combined_source_half_lattice_numerator_mod2"] == ex53["combined"]["source_half_lattice_numerator_mod2"]

    sem = chain["semantic_quotient"]
    assert sem["label"] == b54["semantic_half_lattice_label"] == "u1"
    assert sem["coordinate_f2"] == b54["semantic_coordinate_f2"] == [1, 0]
    assert sem["fiber_cardinality"] == la55["u1_fiber_cardinality"] == 4096
    assert sem["other_marked_source_points_in_same_fiber"] == pos55["other_source_points_with_same_semantic_label_count"] == 4095
    assert sem["injective_for_source_identification"] is False

    out = chain["required_geometry_output"]
    assert out["literal_function_divisor_transition_datum"] is True
    assert out["full_surface_cech_h2_mu2_scope"] is True
    assert out["exact_marked_brauer_image_proper14_mask_decimal"] == 20
    assert out["source_specific_binding_to_v41_e3"] is True
    assert chain["locked_chain_materializes_required_geometry_output"] is False
    assert chain["locked_chain_materializes_marked_picard_to_literal_geometry_adapter"] is False
    assert chain["repo_wide_absence_claim"] is False
    assert chain["mathematical_nonexistence_claim"] is False

    gap = d["interface_gap"]
    assert gap["name"] == "MASK20_MARKED_PICARD_ADJOINT_TO_LITERAL_FULL_SURFACE_CECH_GEOMETRY"
    assert "mask20" in gap["required_postcondition"]
    assert "literal" in gap["smallest_next_datum"]

    forbidden = d["forbidden_shortcuts"]
    assert "treat semantic u1 as injective" in forbidden
    assert "identify e3 with J2 from the common u1 label" in forbidden
    assert "reuse J2 {f2,g22} as e3 without exact mask20 binding" in forbidden
    assert "claim repository-wide absence or mathematical nonexistence from the bounded locked-chain gap" in forbidden

    f = d["credit_firewall"]
    assert f["e3_literal_cech_preimage_materialized"] is False
    assert f["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["j2_adapted_columns_materialized"] == "1/10"
    assert f["standard_columns_materialized"] == "0/10"
    assert f["stage33_progress"] == "6/11"
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False
    assert f["receiver_credit"] is False
    assert f["endpoint_credit"] is False
    assert f["theorem_credit"] is False

    assert d["status"] == "PASS_EXACT_GAP_LOCALIZED_TO_MASK20_MARKED_PICARD_TO_LITERAL_GEOMETRY_BRIDGE"
    assert d["next_exact_leaf"] == "E3_V25_S1B1C_CONSTRUCT_ONE_SOURCE_LOCKED_LITERAL_GEOMETRIC_DATUM_WITH_EXACT_MARKED_BRAUER_IMAGE_MASK20"
    print("PASS: V56 localizes the remaining e3 gap to an exact mask20 marked-Picard-to-literal-geometry bridge")


if __name__ == "__main__":
    main()
