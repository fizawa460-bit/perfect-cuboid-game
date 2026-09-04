#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-u1-fiber-cardinality-v55.json"


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


def det2_mod2(c1, c2):
    return (c1[0] * c2[1] - c2[0] * c1[1]) & 1


def main() -> None:
    d = load(CERT)
    assert d["schema"] == "stage33.e3.mask20_u1_fiber_cardinality.v55"
    assert d["parent_head"] == "1c3cc9c77ed0ef64bfd900a3738ad24209b79f28"

    v53 = assert_lock(d["source_locks"]["v53_candidate"])
    v54 = assert_lock(d["source_locks"]["v54_semantic_label"])

    ex53 = v53["exact_computation"]
    assert ex53["input_proper14_mask_decimal"] == 20
    assert ex53["input_support_one_based"] == [3, 5]
    c3 = ex53["axis_3"]["source_T_mod_2_coordinate_f2"]
    c5 = ex53["axis_5"]["source_T_mod_2_coordinate_f2"]
    assert c3 == [0, 1]
    assert c5 == [1, 1]
    assert ex53["combined"]["source_T_mod_2_coordinate_f2"] == [1, 0]

    bind54 = v54["exact_binding"]
    assert bind54["e3_proper14_mask_decimal"] == 20
    assert bind54["semantic_half_lattice_label"] == "u1"
    assert bind54["semantic_coordinate_f2"] == [1, 0]
    assert bind54["exact_vector_match"] is True

    la = d["exact_linear_algebra"]
    assert la["proper14_source_dimension_f2"] == 14
    assert la["semantic_target_dimension_f2"] == 2
    assert la["independent_source_axes_one_based"] == [3, 5]
    assert la["axis_3_semantic_column_f2"] == c3
    assert la["axis_5_semantic_column_f2"] == c5
    assert la["witness_matrix_columns_axis3_axis5"] == [c3, c5]
    det = det2_mod2(c3, c5)
    assert det == 1 == la["determinant_mod_2"]

    rank = 2
    kernel_dim = la["proper14_source_dimension_f2"] - rank
    fiber_size = 1 << kernel_dim
    assert la["semantic_projection_rank_f2"] == rank
    assert la["semantic_projection_kernel_dimension_f2"] == kernel_dim == 12
    assert la["every_semantic_fiber_cardinality"] == fiber_size == 4096
    assert la["u1_fiber_cardinality"] == fiber_size

    pos = d["e3_position"]
    assert pos["proper14_mask_decimal"] == 20
    assert pos["proper14_support_one_based"] == [3, 5]
    assert pos["semantic_label"] == "u1"
    assert pos["semantic_coordinate_f2"] == [1, 0]
    assert pos["marked_source_point_count_in_u1_fiber"] == fiber_size
    assert pos["other_source_points_with_same_semantic_label_count"] == fiber_size - 1 == 4095
    assert pos["e3_identified_by_semantic_label_alone"] is False

    g = d["geometric_realization_boundary"]
    assert g["literal_function_divisor_transition_data_for_e3_materialized"] is False
    assert g["source_specific_full_surface_cech_h2_mu2_preimage_materialized"] is False
    assert g["exact_brauer_image_binding_to_mask20_from_literal_geometry"] is False
    assert g["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert g["e3_kummer_column_materialized"] is False

    blocker = d["exact_blocker"]
    assert blocker["name"] == "SOURCE_SPECIFIC_GEOMETRIC_BINDING_TO_ONE_MARKED_POINT_OF_THE_4096_POINT_U1_FIBER"
    assert "treat semantic u1 as injective" in blocker["forbidden_shortcuts"]

    f = d["credit_firewall"]
    assert f["j2_adapted_columns_materialized"] == "1/10"
    assert f["standard_columns_materialized"] == "0/10"
    assert f["stage33_progress"] == "6/11"
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False
    assert f["receiver_credit"] is False
    assert f["endpoint_credit"] is False
    assert f["theorem_credit"] is False

    assert d["status"] == "PASS_EXACT_U1_FIBER_SIZE_4096_MASK20_REMAINS_SOURCE_SPECIFIC_GEOMETRIC_TARGET"
    assert d["next_exact_leaf"] == "E3_V25_S1B1B_CONSTRUCT_LITERAL_GEOMETRIC_CECH_DATUM_BINDING_EXACTLY_TO_MASK20_INSIDE_THE_4096_POINT_U1_FIBER"
    print("PASS: V55 semantic u1 fiber has 4096 proper14 source points; exact mask20 geometry remains open")


if __name__ == "__main__":
    main()
