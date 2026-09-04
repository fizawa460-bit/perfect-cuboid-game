#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-picard-adjoint-candidate-v53.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def assert_lock(entry: dict) -> dict:
    path = ROOT / entry["path"]
    assert path.exists(), entry["path"]
    assert git_blob_sha1(path) == entry["git_blob_sha1"], entry["path"]
    return load(path) if path.suffix == ".json" else {}


def xor_vec(a, b):
    assert len(a) == len(b)
    return [x ^ y for x, y in zip(a, b)]


def main() -> None:
    d = load(CERT)
    assert d["schema"] == "stage33.e3.mask20_picard_adjoint_candidate.v53"
    assert d["parent_head"] == "a3188ad5f5c1b722499dd95a6ab910102c7b2803"

    locks = d["source_locks"]
    v41 = assert_lock(locks["v41_e3_source"])
    v52 = assert_lock(locks["v52_gap"])
    adj = assert_lock(locks["proper14_picard_adjoint"])
    assert_lock(locks["proper14_picard_adjoint_verifier"])
    orient = assert_lock(locks["j2_semantic_orientation"])

    e3 = v41["e3_source"]
    assert e3["proper14_mask_decimal"] == 20
    assert e3["proper14_coordinate_f2"] == [0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    assert e3["retained10_standard_mask_decimal"] == 4
    assert e3["derived_from_j2_xor_split"] is False
    assert v52["status"] == "BLOCKED_EXACT_MASK20_LITERAL_CECH_PREIMAGE_REQUIRES_SOURCE_SPECIFIC_MARKED_GEOMETRIC_DATUM"

    cols = {c["target_basis_index_1based"]: c for c in adj["degree2_picard_adjoint"]["decoded_target_basis_columns"]}
    c3, c5 = cols[3], cols[5]
    calc_t = xor_vec(c3["source_T_mod_2_coordinate_f2"], c5["source_T_mod_2_coordinate_f2"])
    calc_h = xor_vec(c3["source_half_lattice_numerator_mod2"], c5["source_half_lattice_numerator_mod2"])

    ex = d["exact_computation"]
    assert ex["input_proper14_mask_decimal"] == 20
    assert ex["input_support_one_based"] == [3,5]
    assert ex["axis_3"]["source_T_mod_2_coordinate_f2"] == c3["source_T_mod_2_coordinate_f2"]
    assert ex["axis_3"]["source_half_lattice_numerator_mod2"] == c3["source_half_lattice_numerator_mod2"]
    assert ex["axis_5"]["source_T_mod_2_coordinate_f2"] == c5["source_T_mod_2_coordinate_f2"]
    assert ex["axis_5"]["source_half_lattice_numerator_mod2"] == c5["source_half_lattice_numerator_mod2"]
    assert ex["combined"]["source_T_mod_2_coordinate_f2"] == calc_t == [1,0]
    assert ex["combined"]["source_half_lattice_numerator_mod2"] == calc_h == [1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0]
    assert ex["candidate_scope"] == "DEGREE2_PICARD_ADJOINT_MARKED_CANDIDATE_ONLY"

    sem = d["semantic_projection_firewall"]
    assert orient["retained_named_j2_geometric_credit"]["marked_brauer_coordinate_beta_basis_f2"] == [1,0]
    assert sem["e3_mask20_projection_f2"] == calc_t
    assert sem["j2_named_orientation_f2"] == [1,0]
    assert sem["projection_coordinates_equal"] is True
    assert sem["e3_identified_with_j2"] is False

    g = d["geometric_realization_boundary"]
    assert g["picard_adjoint_candidate_materialized"] is True
    assert g["literal_function_divisor_transition_data_for_mask20_materialized"] is False
    assert g["source_specific_cech_h2_mu2_preimage_materialized"] is False
    assert g["full_surface_h2_mu2_scope_certified"] is False
    assert g["brauer_image_binding_to_v41_e3_certified_from_literal_geometry"] is False
    assert g["e3_kummer_column_materialized"] is False

    blocker = d["exact_blocker"]
    assert blocker["name"] == "SOURCE_SPECIFIC_GEOMETRIC_REALIZATION_OF_MASK20_PICARD_ADJOINT_CANDIDATE_AS_FULL_SURFACE_CECH_H2_MU2_CLASS"
    assert "identify e3 with J2 because both project to [1,0]" in blocker["forbidden_shortcuts"]

    f = d["credit_firewall"]
    assert f["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["j2_adapted_columns_materialized"] == "1/10"
    assert f["stage33_progress"] == "6/11"
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False

    assert d["status"] == "PASS_EXACT_MASK20_PICARD_ADJOINT_CANDIDATE_GEOMETRIC_REALIZATION_STILL_OPEN"
    assert d["next_exact_leaf"] == "E3_V25_S1B_REALIZE_MASK20_PICARD_ADJOINT_CANDIDATE_AS_SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_CLASS"
    print("PASS: V53 mask20 Picard-adjoint candidate is exact; geometric Cech realization remains open")


if __name__ == "__main__":
    main()
