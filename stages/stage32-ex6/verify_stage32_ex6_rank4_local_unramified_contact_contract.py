#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-rank4-local-unramified-contact-contract.json"


def main() -> None:
    x = json.loads(PATH.read_text())
    assert x["schema"] == "STAGE32_EX6_RANK4_LOCAL_UNRAMIFIED_CONTACT_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_WALL_NO_MAIN_CREDIT"

    s = x["source_locks"]
    assert s["stoll_testa_cuboids_magma_blob"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
    assert s["stoll_testa_section5_fibrations_log_blob"] == "9cfef75aa58335655d6ae3e78597f5924b6c2433"
    assert s["v6_canonical_sha256"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
    assert s["v6_all140_pairings_sha256"] == "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
    assert s["hperp_adapter_canonical_sha256"] == "fc695b9405ec4becfbcf19866c0c70fceed9372186a5aa4974879f302ee8ffe9"
    assert s["post1648an_blob_sha1"] == "512fcc70afb1acf16956fd4b7a2b9b935a052150"

    g = x["degree113_split_geometry"]
    assert g["split_fiber_count"] == 6
    assert g["g3_components_per_split_fiber"] == 2
    assert g["exceptional_components_per_split_fiber"] == 4
    assert g["split_exceptional_curve_count"] == g["split_fiber_count"] * g["exceptional_components_per_split_fiber"] == 24
    assert g["attachment_points_per_split_exceptional"] == 2
    assert g["split_attachment_point_count"] == g["split_exceptional_curve_count"] * g["attachment_points_per_split_exceptional"] == 48
    assert g["v6_split_exceptional_mass"] == 140
    assert g["split_fiber_components_used_with_coefficient_one"] is True
    assert g["g3_components_disjoint_on_resolution"] is True
    assert g["each_split_exceptional_meets_each_g3_once"] is True

    e = x["endpoint_local_model"]
    assert e["O"] == 266
    assert e["all_exceptional_contacts_have_multiplicity_one"] is True
    assert e["landing_parameters_pairwise_distinct_per_exceptional"] is True
    assert e["finite_attachment_set_can_be_avoided_locally"] is True
    assert e["all_140_split_exceptional_contacts_locally_unramified_realizable"] is True
    assert e["global_v6_carrier_constructed"] is False

    d = x["decision"]
    assert d["naive_every_O_contact_rank4_ramification_adapter"] == "LOCALLY_FALSE"
    assert d["O266_implies_rank4_ramification_ge_266"] is False
    assert d["O266_endpoint_excluded"] is False
    assert d["O266_endpoint_not_closed"] is True
    assert d["stage32_main_changed"] is False
    assert d["Q602_survivors_changed"] is False
    assert d["O264_descent_authorized"] is False

    scope = x["scope"]
    assert scope["bounded_local_countermodel_only"] is True
    assert scope["member_level_global_landing_forcing_still_missing"] is True
    assert scope["receiver_credit"] is False
    assert scope["theorem_credit"] is False
    assert scope["perfect_cuboid_credit"] is False

    print("PASS: Stage32 EX6 rank4 local-unramified contact contract")


if __name__ == "__main__":
    main()
