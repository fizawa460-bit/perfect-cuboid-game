#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
POLICY = HERE / "e3-search-routing-supersession-v58.json"
V57 = HERE / "e3-mask20-b1-gysin-image-gate-v57.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    d = load(POLICY)
    v57 = load(V57)

    assert d["schema"] == "stage33.search_routing_supersession.v58"
    assert d["role"] == "OPERATIONAL_ROUTING_ONLY_NO_MATHEMATICAL_CHANGE"
    assert d["parent_head"] == "0a83fbeac9e3fef63a01f11580a821ade063c751"

    sup = d["supersedes_operationally"]
    assert "one_automatic_bounded_repository_search" in sup["current_main_v41_field"]
    assert sup["current_main_v41_budget_field"].endswith("=1")
    assert sup["v57_historical_search_state"] == "CONSUMED_NO_HIT"
    assert sup["mathematical_content_of_v57"] == "UNCHANGED"
    assert v57["arsenal_routing"]["bounded_repository_search_for_this_missing_object"] == "CONSUMED_NO_HIT"

    r = d["routing_contract"]
    assert r["identify_exact_missing_object_first"] is True
    assert r["arsenal_first"] is True
    assert r["fixed_per_object_search_count_cap"] is None
    assert r["repeated_bounded_repository_search_allowed"] is True
    assert len(r["each_search_requires"]) >= 3
    assert len(r["stop_conditions"]) >= 4
    assert "unlimited or open-ended repository search" in r["forbidden"]
    assert "recursive repository-wide enumeration as ordinary discovery" in r["forbidden"]
    assert r["search_miss_proves_repository_absence"] is False
    assert r["search_miss_proves_mathematical_nonexistence"] is False

    leaf = d["current_leaf"]
    assert leaf["stage33_microgoal"] == "A2.4"
    assert leaf["exact_object"] == "B1_BRANCH_H1_TO_PROPER14_BRAUER_IMAGE_MATRIX"
    assert leaf["matrix_shape"] == [14, 4]
    assert leaf["target_membership_equation"] == "M*x=mask20"
    assert leaf["v57_mathematical_gate_unchanged"] is True
    assert v57["smallest_next_exact_object"]["matrix_shape"] == [14, 4]

    f = d["credit_firewall"]
    for key in (
        "new_mathematical_column_materialized",
        "genuine_full_surface_h2_mu2_lift_for_e3",
        "e3_kummer_column_materialized",
        "stage33_12_closed",
        "stage33_13_released",
        "receiver_credit",
        "endpoint_credit",
        "theorem_credit",
        "merge_allowed",
    ):
        assert f[key] is False, key

    assert d["status"] == "PASS_OPERATIONAL_FIXED_ONE_SEARCH_CAP_REVOKED_BOUNDED_REPEAT_SEARCH_ALLOWED"
    print("PASS V58: fixed one-search cap revoked; repeated bounded search allowed under explicit scope/stop conditions")


if __name__ == "__main__":
    main()
