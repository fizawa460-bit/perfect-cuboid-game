#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-adjoint-u1-label-v54.json"


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
    assert d["schema"] == "stage33.e3.mask20_adjoint_u1_label.v54"
    assert d["parent_head"] == "ba085a30e9fd251bd33d6b7739c6288d02c28dc6"

    locks = d["source_locks"]
    v53 = assert_lock(locks["v53_candidate"])
    target = assert_lock(locks["semantic_discriminant_target"])
    orient = assert_lock(locks["j2_semantic_orientation"])

    candidate = v53["exact_computation"]["combined"]["source_half_lattice_numerator_mod2"]
    coord = v53["exact_computation"]["combined"]["source_T_mod_2_coordinate_f2"]
    u1 = next(x for x in target["semantic_half_lattice_basis"] if x["label"] == "u1")

    b = d["exact_binding"]
    assert b["e3_proper14_mask_decimal"] == 20
    assert candidate == b["v53_half_lattice_numerator_mod2"] == u1["numerator_mod2"]
    assert coord == b["semantic_coordinate_f2"] == [1,0]
    assert b["semantic_half_lattice_label"] == "u1"
    assert b["exact_vector_match"] is True
    assert b["target_scope"] == "KC_DISCRIMINANT_2TORSION_SEMANTIC_TARGET_ONLY"

    s = d["source_specificity_firewall"]
    assert orient["retained_named_j2_geometric_credit"]["marked_brauer_coordinate_beta_basis_f2"] == [1,0]
    assert orient["anti_isometry_check"]["matches_semantic_half_lattice_label"] == "u1"
    assert s["j2_named_semantic_label"] == "u1"
    assert s["j2_named_coordinate_f2"] == [1,0]
    assert s["same_semantic_target_label"] is True
    assert s["e3_identified_with_j2"] is False
    assert s["j2_literal_cech_representative_reused_as_e3"] is False

    g = d["geometric_realization_boundary"]
    assert g["e3_literal_function_divisor_transition_data_materialized"] is False
    assert g["source_specific_full_surface_cech_h2_mu2_preimage_materialized"] is False
    assert g["exact_brauer_image_binding_to_mask20_from_literal_geometry"] is False
    assert g["e3_kummer_column_materialized"] is False

    blocker = d["exact_blocker"]
    assert blocker["name"] == "SOURCE_SPECIFIC_GEOMETRIC_REALIZATION_IN_THE_U1_FIBER_FOR_E3_PROPER14_MASK20"
    assert "identify e3 with J2 from the common u1 label" in blocker["forbidden_shortcuts"]

    f = d["credit_firewall"]
    assert f["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["j2_adapted_columns_materialized"] == "1/10"
    assert f["stage33_progress"] == "6/11"
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False

    assert d["status"] == "PASS_EXACT_MASK20_ADJOINT_CANDIDATE_EQUALS_SEMANTIC_U1_SOURCE_SPECIFIC_GEOMETRIC_LIFT_STILL_OPEN"
    assert d["next_exact_leaf"] == "E3_V25_S1B1_CONSTRUCT_SOURCE_SPECIFIC_GEOMETRIC_CECH_REALIZATION_FOR_MASK20_WITHIN_SEMANTIC_U1_FIBER"
    print("PASS: V54 mask20 adjoint candidate is exactly semantic u1; source-specific geometric lift remains open")


if __name__ == "__main__":
    main()
