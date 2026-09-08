#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

OUT = Path(__file__).with_name("v6-galois-field-adapter-wall-20260909.json")
EXPECTED = "97a20f369f181404a062d3f7009860bac8f2e55445f5e52f3dade1a898e55c40"

def csha(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

x = json.loads(OUT.read_text())
stored = x.pop("canonical_sha256_without_this_field")
assert stored == EXPECTED == csha(x)
assert x["retained_galois_facts"]["V6_cc_invariant"] is False
assert x["retained_aut_orbit_facts"]["retained_full_aut_order"] == 1536
assert x["retained_aut_orbit_facts"]["aut_elements_sending_V6_to_ccV6"] == 0
assert x["exact_cross_lane_consequences"]["q_defined_divisor_class_V6_impossible"] is True
assert x["exact_cross_lane_consequences"]["aut_twisted_cc_repair_impossible"] is True
assert x["route_deduplication"]["AS_already_closes_pure_residual_inertia_tangent_action_as_nonpruning"] is True
assert x["route_deduplication"]["AU_closes_cusp_multiplicity_only_Bezout_route_as_nonpruning"] is True
assert x["ex1_live_status"]["new_hostile_reaudit_pass_present"] is False
assert x["firewalls"]["V6_geometric_carrier_excluded"] is False
assert x["firewalls"]["Q602_excluded"] is False
assert x["firewalls"]["O210_excluded"] is False
assert x["firewalls"]["MAIN_STATE_changed"] is False
print(json.dumps({
    "verdict":"PASS_STAGE32_MAIN_SCRATCH_V6_GALOIS_FIELD_ADAPTER_WALL",
    "q_defined_exact_V6_class_possible":False,
    "aut_twisted_cc_repair_available":False,
    "Q602_excluded":False,
    "O210_excluded":False,
    "canonical_sha256":EXPECTED
}, sort_keys=True))
