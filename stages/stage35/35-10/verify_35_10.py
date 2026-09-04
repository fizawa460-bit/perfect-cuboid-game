#!/usr/bin/env python3
"""Verify Stage35 35-10 material-input routing and credit firewalls."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def load(rel: str):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


routing = load("stages/stage35/35-10/material-reopen-routing.json")
state = load("stages/stage35/MAIN-STATE.json")
kernels = load("stages/stage29/29-16/active-kernel-ledger.json")

assert routing["status"] == "MATERIAL_INPUT_ASSESSED_ROUTE_TO_SIBLING_NO_STAGE35_REOPEN"
assert routing["exact_stage35_target"]["kernel"] == "K16-C3-MOVING-FIBER-ARITHMETIC"
assert routing["exact_stage35_target"]["receiver"] == "R29-FIB2"
assert routing["exact_stage35_target"]["target"] == "T35-R3-PHYS-EMPTY"
assert routing["exact_stage35_target"]["proved"] is False

by_id = {entry["kernel"]: entry for entry in kernels["class3_kernels"]}
assert by_id["K16-C3-MOVING-FIBER-ARITHMETIC"]["children"] == ["R29-FIB2"]
assert by_id["K16-C3-PESCH-EXPONENT-ONE"]["children"] == ["R29-PESCH-E1"]
assert by_id["K16-C3-PESCH-EXPONENT-ONE"]["endpoint_decision_capable"] is True

sibling = routing["sibling_kernel_route"]
assert sibling["kernel"] == "K16-C3-PESCH-EXPONENT-ONE"
assert sibling["receiver"] == "R29-PESCH-E1"
assert sibling["newly_surfaced_replacement_target"]["proved"] is False
assert sibling["newly_surfaced_replacement_target"]["primary_owner"] == "K16-C3-PESCH-EXPONENT-ONE"

adapter = routing["stage35_adapter_assessment"]
for key in [
    "direct_theorem_about_TS_S_R3_Q1_all_t",
    "uniform_specialization_new_point_control",
    "uniform_receiver_intersection_obstruction",
    "globally_exhaustive_finite_fiber_reduction",
    "material_input_warrants_stage35_research_reopen",
]:
    assert adapter[key] is False, key

fixed = routing["fixed_fiber_method"]
assert fixed["proof_capable_on_certified_individual_fiber"] is True
assert fixed["globally_exhaustive_parameter_reduction"] is False

for key in ["new_theorem_credit", "R29_FIB2_closed", "R29_PESCH_E1_closed", "J12_PARAMETRIC_closed", "stage35_closed", "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim"]:
    assert routing["decision"][key] is False, key

assert state["decision"]["classification"] == "CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM"
assert state["promotion_gates"]["R29_FIB2_closed"] is False
assert state["promotion_gates"]["stage35_closed"] is False
assert state["claims"]["perfect_cuboid_nonexistence_claim"] is False

print("PASS STAGE35_35_10_MATERIAL_ROUTING_V1")
