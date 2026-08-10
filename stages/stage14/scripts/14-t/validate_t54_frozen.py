#!/usr/bin/env python3

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t54/shared_u_canonical_prime.json"
FROZEN = ROOT / "stages/stage14/data/14-t54/shared_u_canonical_prime_frozen.json"

live = json.loads(LIVE.read_text())
frozen = json.loads(FROZEN.read_text())

assert live["stage"] == frozen["stage"] == "14-t54"
assert live["input"]["reciprocal_states"] == frozen["reciprocal_states"]
assert live["input"]["post_residue_principal_blocks"] == frozen["post_residue_principal_blocks"]
assert live["input"]["shared_U_principal_blocks"] == frozen["shared_U_principal_blocks"]

pc = live["frozen_shared_U_pair_counts"]
assert pc["same_eps"] == frozen["shared_U_same_eps"]
assert pc["same_branch"] == frozen["shared_U_same_branch"]
assert pc["same_k"] == frozen["shared_U_same_k"]
assert pc["same_h"] == frozen["shared_U_same_h"]
assert pc["same_delta"] == frozen["shared_U_same_delta"]
assert pc["same_V_unit"] == frozen["shared_U_same_V_unit"]

fd = live["full_U_fiber_diagnostics"]
for key in (
    "distinct_U_unit_fibers",
    "max_states_per_U_fiber",
    "max_distinct_V_per_U_fiber",
    "max_distinct_delta_per_U_fiber",
    "U_fibers_with_principal_excess",
    "max_principal_excess_in_U_fiber",
):
    assert fd[key] == frozen[key]

assert live["exact_fixed_U_divisor_fan"]["checks"] == frozen["divisor_fan_checks"]
assert live["exact_fixed_U_divisor_fan"]["identity_n_equals_k_delta"] is True
assert live["exact_fixed_U_divisor_fan"]["identity_k_divides_eps_m"] is True
assert live["exact_fixed_U_divisor_fan"]["identity_hk_equals_eps_m"] is True

D = live["decision"]
assert D["STAGE14_T54"] == frozen["boundary"]
for key in (
    "FIXED_U_DIVISOR_FAN_PROVED",
    "FIXED_U_REDUCES_TO_ONE_DIMENSIONAL_CANONICAL_PRIME_SUM",
    "ONE_VARIABLE_FIBER_BOUNDS_GLOBALIZE",
    "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_REQUIRED",
    "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED",
    "SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED",
    "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED",
    "T_O_SQRT_B_PROVED",
    "TH15_NEEDED",
):
    assert D[key] == frozen[key]

assert live["latin_square_quantifier_guard"]["failure_factor"] == 32
assert D["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
assert D["T_O_SQRT_B_PROVED"] is False
assert D["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
print("Stage14-t54 frozen ledger and boundary validated")
