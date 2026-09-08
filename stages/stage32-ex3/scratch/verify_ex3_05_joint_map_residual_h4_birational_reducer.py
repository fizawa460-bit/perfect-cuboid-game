#!/usr/bin/env python3
import json
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "ex3-05-joint-map-residual-h4-birational-reducer.json"

with ART.open("r", encoding="utf-8") as f:
    art = json.load(f)

# H4=(F2)^2.  For the residual quotient (H4 x H4)/diag(H4),
# every stabilizer/decomposition subgroup has order 1, 2, or 4.
ambient_allowed = {1, 2, 4}
projection_allowed = {d for d in range(1, gcd(105, 81) + 1) if 105 % d == 0 and 81 % d == 0}
assert gcd(105, 81) == 3
assert projection_allowed == {1, 3}
assert ambient_allowed & projection_allowed == {1}

jm = art["joint_map"]
assert set(jm["ambient_allowed_delta"]) == ambient_allowed
assert set(jm["projection_allowed_delta"]) == projection_allowed
assert jm["forced_delta"] == 1

cons = art["exact_consequences"]
assert cons["joint_map_birational_onto_image"] is True
assert cons["Y_is_normalization_of_Gamma"] is True
assert cons["degree3_common_factor_ruled_out"] is True
assert cons["residual_H4_stabilizer_of_lifted_curve"] == "trivial"
assert cons["rho_inverse_image_of_Gamma_generic_components"] == 4
assert cons["generic_component_degrees_over_Gamma"] == [1,1,1,1]

fw = art["firewalls"]
assert fw["arithmetic_genus_computed_from_only_two_fiber_degrees"] is False
assert fw["NS_C0xC0_reduced_to_rank2"] is False
assert fw["O210_excluded"] is False
assert fw["Q602_excluded"] is False
assert fw["stage32_main_credit"] is False
assert fw["claim_dag_sync_triggered_by_this_scratch"] is False
assert fw["merge_authorized"] is False

print(json.dumps({
    "status": "PASS",
    "gcd_105_81": gcd(105,81),
    "ambient_allowed_delta": sorted(ambient_allowed),
    "projection_allowed_delta": sorted(projection_allowed),
    "forced_joint_degree": 1,
    "degree3_common_factor_ruled_out": True,
    "EX3_05_exclusion_obtained": False
}, sort_keys=True))
