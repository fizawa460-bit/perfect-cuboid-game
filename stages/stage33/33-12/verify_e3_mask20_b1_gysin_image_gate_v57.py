#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-b1-gysin-image-gate-v57.json"


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
    assert d["schema"] == "stage33.e3.mask20_b1_gysin_image_gate.v57"
    assert d["parent_head"] == "7f9c2d8ed3ca69ac631ff68d1051430be2d5caac"

    v41 = assert_lock(d["source_locks"]["v41_e3_source"])
    v50 = assert_lock(d["source_locks"]["v50_type_correction"])
    v52 = assert_lock(d["source_locks"]["v52_literal_cech_gap"])
    v56 = assert_lock(d["source_locks"]["v56_geometry_gap"])
    branch = assert_lock(d["source_locks"]["j2_branch_surface_adapter"])
    cech = assert_lock(d["source_locks"]["j2_literal_cech"])

    e3 = v41["e3_source"]
    assert e3["proper14_mask_decimal"] == 20
    assert e3["proper14_coordinate_f2"] == [0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    assert e3["derived_from_j2_xor_split"] is False

    types = v50["exact_type_statement"]
    assert types["proper_geometric_coefficient_module"] == "K=Br(Sbar)[2]"
    assert types["proper_geometric_coefficient_dimension_f2"] == 14
    assert types["direct_boundary_source_to_K_linear_map_is_stage_A"] is False

    gap56 = v56["interface_gap"]
    assert gap56["name"] == "MASK20_MARKED_PICARD_ADJOINT_TO_LITERAL_FULL_SURFACE_CECH_GEOMETRY"
    assert v56["exact_chain_localization"]["locked_chain_materializes_required_geometry_output"] is False

    geom = branch["double_cover_geometry"]
    kg = branch["kummer_gysin_adapter"]
    c22 = branch["corrected_pic0_2torsion"]
    assert c22["component_smooth_genus"] == 1
    assert geom["branch_over_Qi"] == ["C21: A3+i*A2=0", "C22: A3-i*A2=0"]
    assert kg["branch"] == "Cbar=C21_tilde disjoint_union C22_tilde"
    assert kg["brauer_image"] == "Phi(0,kappa_D)=corrected geometric J2=(f2,1)"

    # C21 and C22 are the i -> -i conjugate branch components, so both are genus one.
    expected_branch_h1_dim = 2 * c22["component_smooth_genus"] * len(geom["branch_over_Qi"])
    assert expected_branch_h1_dim == 4

    route = d["exact_b1_route_geometry"]
    assert route["C22_genus"] == 1
    assert route["C21_genus"] == 1
    assert route["branch_H1_total_dimension_f2"] == expected_branch_h1_dim == 4
    assert route["proper_geometric_Br2_dimension_f2"] == types["proper_geometric_coefficient_dimension_f2"] == 14
    assert route["required_marked_matrix_shape"] == [14, 4]
    assert route["image_rank_upper_bound_f2"] == 4
    assert route["route_surjective_onto_full_proper14"] is False

    lit52 = v52["bounded_inspection"]["available_literal_cech_example"]
    assert lit52["proper14_mask_decimal"] == 25
    assert lit52["explicit_symbol_materialized"] is True
    assert lit52["reusable_as_e3_by_relabelling"] is False
    assert cech["explicit_cech_preimage"]["class"] == "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
    assert cech["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True

    known = d["existing_exact_j2_point_in_route"]
    assert known["proper14_brauer_image_mask_decimal"] == lit52["proper14_mask_decimal"] == 25
    assert known["literal_symbol"] == "{f2,g22}"
    assert known["certifies_one_nonzero_route_image"] is True
    assert known["certifies_full_14x4_route_matrix"] is False

    gate = d["e3_membership_gate"]
    assert gate["proper14_mask_decimal"] == e3["proper14_mask_decimal"] == 20
    assert gate["proper14_coordinate_f2"] == e3["proper14_coordinate_f2"]
    assert gate["semantic_u1_label_is_membership_proof"] is False
    assert gate["membership_in_im_Phi_B1"] == "OPEN_NOT_COMPUTED"
    assert gate["j2_literal_symbol_reusable_without_membership_and_source_binding"] is False

    nxt = d["smallest_next_exact_object"]
    assert nxt["name"] == "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX"
    assert nxt["matrix_shape"] == [14,4]
    assert "M*x=e3_mask20" in nxt["required_replay"]

    ar = d["arsenal_routing"]
    assert ar["primary"].startswith("S33-PW07")
    assert ar["marked_source_binding"].startswith("S33-PW04")
    assert ar["bounded_repository_search_for_this_missing_object"] == "CONSUMED_NO_HIT"
    assert ar["broad_or_repeated_search_authorized"] is False

    f = d["credit_firewall"]
    assert f["b1_branch_to_proper14_matrix_materialized"] is False
    assert f["e3_b1_route_membership_computed"] is False
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

    assert d["status"] == "PASS_EXACT_B1_GYSIN_ROUTE_REDUCED_TO_FINITE_14X4_MEMBERSHIP_GATE"
    assert d["next_exact_leaf"] == "MATERIALIZE_EXACT_B1_BRANCH_H1_TO_PROPER14_PHI_MATRIX_AND_SOLVE_E3_MASK20_MEMBERSHIP"
    print("PASS: V57 reduces the e3 literal-geometry attempt to an exact finite 14x4 B1-Gysin membership gate")


if __name__ == "__main__":
    main()
