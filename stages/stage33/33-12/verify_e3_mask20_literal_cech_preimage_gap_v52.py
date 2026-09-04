#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-mask20-literal-cech-preimage-gap-v52.json"


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
    assert d["schema"] == "stage33.e3.mask20_literal_cech_preimage_gap.v52"
    assert d["parent_head"] == "b9465e28b429ce7b46d5e93021e90692a7d02f42"

    locks = d["source_locks"]
    v51 = assert_lock(locks["v51_route"])
    v41 = assert_lock(locks["v41_e3_source"])
    j2cech = assert_lock(locks["j2_literal_cech"])
    orient = assert_lock(locks["j2_semantic_orientation"])
    assert_lock(locks["proper14_picard_adjoint"])
    assert_lock(locks["marked_picard_bridge"])

    assert v51["status"] == "PASS_EXACT_E3_V25_METHOD_REWIRED_SOURCE_BOUND_CECH_LIFT_STILL_OPEN"
    assert v51["next_exact_leaf"] == "E3_V25_S1_MATERIALIZE_EXPLICIT_CECH_H2_MU2_PREIMAGE_WITH_EXACT_BRAUER_IMAGE_PROPER14_MASK20"

    e3 = v41["e3_source"]
    assert e3["proper14_mask_decimal"] == 20
    assert e3["proper14_coordinate_f2"] == [0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    assert e3["retained10_standard_mask_decimal"] == 4
    assert e3["derived_from_j2_xor_split"] is False
    assert v41["construction_boundary"]["genuine_full_surface_h2_mu2_lift_materialized"] is False

    assert j2cech["explicit_cech_preimage"]["concrete_Cech_preimage_e_D_materialized"] is True
    assert j2cech["explicit_cech_preimage"]["class"] == "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
    assert j2cech["surface_mu2_lift"]["brauer_image"] == "corrected nonzero J2=(f2,1)"
    assert j2cech["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True

    assert orient["retained_named_j2_geometric_credit"]["corrected_J2"] == "(f2,1)"
    assert orient["retained_named_j2_geometric_credit"]["marked_brauer_coordinate_beta_basis_f2"] == [1,0]
    assert orient["explicit_marked_adapter"]["canonical_identification_claimed"] is False
    assert orient["firewalls"]["proper_Br2_14D_coordinate_guessed"] is False

    b = d["bounded_inspection"]
    assert b["e3_source"]["proper14_mask_decimal"] == 20
    assert b["available_literal_cech_example"]["source"] == "corrected J2=(f2,1)"
    assert b["available_literal_cech_example"]["proper14_mask_decimal"] == 25
    assert b["available_literal_cech_example"]["reusable_as_e3_by_relabelling"] is False
    assert b["available_semantic_orientation"]["reusable_as_mask20_binding"] is False
    assert b["available_marked_picard_data"]["literal_function_divisor_transition_preimage_for_mask20_materialized"] is False
    assert b["mask20_literal_preimage_materialized"] is False
    assert b["repo_absence_claim"] is False
    assert b["mathematical_nonexistence_claim"] is False

    blocker = d["exact_blocker"]
    assert blocker["name"] == "SOURCE_SPECIFIC_MARKED_GEOMETRIC_CECH_PREIMAGE_FOR_E3_PROPER14_MASK20"
    assert "proper14 mask 20" in blocker["smallest_missing_datum"]
    assert "relabel J2 {f2,g22} as e3" in blocker["forbidden_shortcuts"]

    f = d["credit_firewall"]
    assert f["e3_literal_cech_preimage_materialized"] is False
    assert f["genuine_full_surface_h2_mu2_lift_for_e3"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["j2_adapted_columns_materialized"] == "1/10"
    assert f["stage33_progress"] == "6/11"
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False

    assert d["status"] == "BLOCKED_EXACT_MASK20_LITERAL_CECH_PREIMAGE_REQUIRES_SOURCE_SPECIFIC_MARKED_GEOMETRIC_DATUM"
    assert d["next_exact_leaf"] == "E3_V25_S1A_CONSTRUCT_SOURCE_SPECIFIC_MARKED_GEOMETRIC_CECH_PREIMAGE_FOR_PROPER14_MASK20"
    print("PASS: V52 bounded mask20 literal-Cech gap is exact and source-locked")


if __name__ == "__main__":
    main()
