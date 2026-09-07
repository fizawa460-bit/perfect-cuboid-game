#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "stages" / "stage32-ex6" / "post1697-rank4-degree113-one-unit-budget-contract.json"


def main() -> None:
    x = json.loads(PATH.read_text())
    assert x["schema"] == "STAGE32_EX6_RANK4_DEGREE113_ONE_UNIT_BUDGET_WALL_V1"
    assert x["status"] == "EXPLORATORY_EXACT_BOUNDED_WALL_NO_MAIN_CREDIT"

    i = x["inputs"]
    assert i["degree"] == 113
    assert i["normalization_genus"] == 1
    assert i["riemann_hurwitz_total_ramification"] == 2 * i["degree"] == 226
    assert i["O"] == 266
    assert i["all_O_contacts_unit_multiplicity"] is True
    assert i["split_exceptional_contact_mass"] == 140
    assert i["split_exceptional_contacts_locally_zero_ramification_realizable"] == 140

    b = x["budget"]
    assert b["remaining_O_contacts"] == i["O"] - i["split_exceptional_contact_mass"] == 126
    assert b["one_unit_per_remaining_contact_max"] == b["remaining_O_contacts"] == 126
    assert b["contradiction_threshold"] == i["riemann_hurwitz_total_ramification"] + 1 == 227
    assert b["additional_forced_ramification_needed"] == b["contradiction_threshold"] - b["one_unit_per_remaining_contact_max"] == 101
    required = Fraction(
        b["required_average_from_remaining_contacts_numerator"],
        b["required_average_from_remaining_contacts_denominator"],
    )
    assert required == Fraction(227, 126)
    assert required > Fraction(9, 5)

    r = x["bounded_route"]
    assert r["allows_zero_credit_on_140_split_exceptional_contacts"] is True
    assert r["no_independent_ramification_lower_bound"] is True
    assert r["at_most_one_forced_unit_per_remaining_contact"] is True
    assert r["numerically_sufficient_for_RH_contradiction"] is False
    assert r["decision"] == "NUMERICALLY_INSUFFICIENT"
    assert b["one_unit_per_remaining_contact_max"] < i["riemann_hurwitz_total_ramification"]

    f = x["firewalls"]
    assert f["global_v6_carrier_constructed"] is False
    assert f["degree113_route_globally_impossible_claimed"] is False
    assert f["O266_endpoint_excluded"] is False
    assert f["O266_endpoint_not_closed"] is True
    assert f["stage32_main_changed"] is False
    assert f["Q602_survivors_changed"] is False
    assert f["O264_descent_authorized"] is False
    assert f["receiver_credit"] is False
    assert f["theorem_credit"] is False
    assert f["perfect_cuboid_credit"] is False

    print("PASS: Stage32 EX6 degree113 one-unit budget contract")


if __name__ == "__main__":
    main()
