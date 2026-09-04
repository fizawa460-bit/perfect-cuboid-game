#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v25-method-rewire-v51.json"
V50 = HERE / "e3-a1-1-type-correction-v50.json"
V41 = HERE / "e3-independent-proper14-source-v41.json"
V25 = HERE / "j2-genuine-h2-mu2-kummer-adapter-v25.json"
CECH = HERE / "j2-corrected-explicit-cech-mu2-lift.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    d = load(CERT)
    v50 = load(V50)
    v41 = load(V41)
    v25 = load(V25)
    cech = load(CECH)

    assert d["schema"] == "stage33.e3.v25_method_rewire.v51"
    assert d["parent_head"] == "ab0a86527e76e955a951bd90d5db37283bc5a303"

    assert v50["status"] == "PASS_EXACT_A1_1_14X14_P_W_ROUTE_RETIRED_BY_TYPE_CHECK"
    assert v50["retired_assumption"]["v47_14_column_construction_contract_superseded"] is True
    assert v50["retired_assumption"]["arbitrary_equivariant_intertwiner_forbidden"] is True

    e3 = v41["e3_source"]
    assert e3["proper14_mask_decimal"] == 20
    assert e3["proper14_coordinate_f2"] == [0,0,1,0,1,0,0,0,0,0,0,0,0,0]
    assert e3["retained10_standard_mask_decimal"] == 4
    assert e3["derived_from_j2_xor_split"] is False
    assert v41["construction_boundary"]["genuine_full_surface_h2_mu2_lift_materialized"] is False

    j2src = v25["current_named_source"]
    assert j2src["proper14_mask_decimal"] == 25
    assert j2src["marked_brauer_coordinate_f2"] == [1,0]
    assert v25["genuine_h2_mu2_adapter"]["explicit_cech_preimage_e_D_materialized"] is True
    assert v25["genuine_h2_mu2_adapter"]["named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate"] is True
    assert v25["genuine_h2_mu2_adapter"]["revoked_c2_plus_c3_relation_used"] is False

    assert cech["explicit_cech_preimage"]["concrete_Cech_preimage_e_D_materialized"] is True
    assert cech["explicit_cech_preimage"]["class"] == "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)"
    assert cech["surface_mu2_lift"]["brauer_image"] == "corrected nonzero J2=(f2,1)"
    assert cech["surface_mu2_lift"]["genuine_surface_H2_mu2_lift_materialized"] is True

    r = d["exact_rewire"]
    assert r["retired_route_remains_forbidden"] is True
    assert r["e3_source"]["proper14_mask_decimal"] == 20
    assert r["e3_source"]["retained10_standard_mask_decimal"] == 4
    assert r["j2_specific_data_not_reusable_for_e3"]["proper14_mask_decimal"] == 25
    assert r["j2_specific_data_not_reusable_for_e3"]["marked_brauer_coordinate_f2"] == [1,0]
    assert r["e3_minimal_missing_object"]["materialized"] is False
    assert r["e3_minimal_missing_object"]["required_brauer_image_proper14_mask_decimal"] == 20

    a = d["arsenal_routing"]
    assert a["primary"].startswith("S33-PW07:")
    assert a["source_binding"].startswith("S33-PW04:")
    assert a["credit_firewall"].startswith("S30-WF03:")
    assert a["pw05_direct_14d_bridge_route"] is False

    f = d["credit_firewall"]
    assert f["e3_cech_h2_mu2_lift_materialized"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["j2_specific_v25_lift_relabelled_as_e3"] is False
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False
    assert f["stage33_progress"] == "6/11"

    assert d["status"] == "PASS_EXACT_E3_V25_METHOD_REWIRED_SOURCE_BOUND_CECH_LIFT_STILL_OPEN"
    assert d["next_exact_leaf"] == "E3_V25_S1_MATERIALIZE_EXPLICIT_CECH_H2_MU2_PREIMAGE_WITH_EXACT_BRAUER_IMAGE_PROPER14_MASK20"
    print("PASS: V51 e3 V25-method source-bound Cech route rewire")


if __name__ == "__main__":
    main()
