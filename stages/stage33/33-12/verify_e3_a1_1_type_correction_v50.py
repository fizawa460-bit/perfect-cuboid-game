#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-a1-1-type-correction-v50.json"
S07 = HERE.parent / "33-07" / "result.md"
S11F = HERE.parent / "33-11f" / "stage33-11f-26-column-exact-closure-certificate.json"


def main() -> None:
    d = json.loads(CERT.read_text(encoding="utf-8"))
    assert d["schema"] == "stage33.e3.a1_1_type_correction.v50"
    assert d["parent_head"] == "1f124f014560b91d06e5a4a8993fc5165976b3e9"

    s07 = S07.read_text(encoding="utf-8")
    assert "Stage A: F2^26 -> ((L*/L*2) tensor_F2 Br(Sbar)[2])^V4" in s07
    assert "Stage B: ker(Stage A) -> H^1(V4,Br(Sbar)[2]) = F2^16." in s07
    assert "Stage A is exactly a `14 x 26` tensor of `L`-squareclasses" in s07

    c11 = json.loads(S11F.read_text(encoding="utf-8"))
    assert c11["canonical_sha256"] == "c7ba9a5a4a9475830e62276292abcdb89deb729a6aecab2c0b6f48a71a65f6e4"
    assert c11["absolute_receiver"]["coefficient_module"] == "K=Br(Sbar)[2], dim_F2=14"
    cols = c11["columns"]
    assert len(cols) == 26
    assert all(c["status"] == "ZERO_EXACT_MAIN" and c["unresolved"] is False for c in cols)

    t = d["exact_type_statement"]
    assert t["proper_geometric_coefficient_dimension_f2"] == 14
    assert t["stage_A_domain"] == "F2^26"
    assert t["stage_A_project_specific_data"] == "14x26 tensor of L-squareclasses"
    assert t["direct_boundary_source_to_K_linear_map_is_stage_A"] is False
    assert t["working_14_boundary_directions_are_proved_basis_of_K"] is False

    r = d["retired_assumption"]
    assert r["name"] == "P_W"
    assert r["old_shape"] == [14, 14]
    assert r["status"] == "RETIRED_WRONG_OBJECT_TYPE"
    assert r["v47_14_column_construction_contract_superseded"] is True
    assert r["positional_identification_forbidden"] is True
    assert r["arbitrary_equivariant_intertwiner_forbidden"] is True

    f = d["credit_firewall"]
    assert f["e3_boundary_coordinate_materialized"] is False
    assert f["e3_cech_h2_mu2_lift_materialized"] is False
    assert f["e3_kummer_column_materialized"] is False
    assert f["stage33_12_closed"] is False
    assert f["stage33_13_released"] is False
    assert f["merge_allowed"] is False
    assert f["stage33_progress"] == "6/11"
    assert d["status"] == "PASS_EXACT_A1_1_14X14_P_W_ROUTE_RETIRED_BY_TYPE_CHECK"
    print("PASS: V50 A1.1 type correction")


if __name__ == "__main__":
    main()
