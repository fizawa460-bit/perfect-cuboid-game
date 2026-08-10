#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t50/selector_sensitive_two_modulus.json"
FROZEN = ROOT / "stages/stage14/data/14-t50/selector_sensitive_two_modulus_frozen.json"
RESULT = ROOT / "stages/stage14/14-t50/result.md"

live = json.loads(LIVE.read_text())
frozen = json.loads(FROZEN.read_text())
result = RESULT.read_text()

assert live["stage"] == frozen["stage"] == "14-t50"
assert live["t49_target"]["frozen_H"] == frozen["t49_frozen"]["H"] == 560
assert live["t49_target"]["frozen_P"] == frozen["t49_frozen"]["P"] == 128
assert live["t49_target"]["frozen_external_R_off"] == frozen["t49_frozen"]["R_off"] == 9007456
assert live["t49_target"]["frozen_external_ratio"] == frozen["t49_frozen"]["ratio"]
assert live["bad_auxiliary"]["frozen_external_max_bad"] == frozen["t49_frozen"]["external_max_bad"] == 0
assert live["bad_auxiliary"]["frozen_endogenous_max_bad"] == frozen["t49_frozen"]["endogenous_max_bad"] == 2

cm = live["t32_to_physical_selector_gap"]["countermodel"]
for key in ("prime", "complete_nonzero_sum", "selected_points", "selected_sum"):
    assert cm[key] == frozen["selector_countermodel"][key]

assert live["bad_auxiliary"]["aggregate_bound_proved"] is True
assert frozen["bad_auxiliary"]["aggregate_bound_proved"] is True
assert live["roadworks_contract"]["tH4_same_modulus_joint_second_moment_already_proved"] is False
assert live["roadworks_contract"]["tH5_same_modulus_residue_collision_energy_already_proved"] is False
assert live["roadworks_contract"]["tH5_exact_gaussian_pair_collision_energy_near_linear"] is True
assert live["decision"]["TH11_MULTI_MODULUS_REOPEN_TRIGGER_HIT"] is True

D = live["decision"]
assert D["STAGE14_T50"] == frozen["boundary"]
assert D["EXTERNAL_BAD_AUXILIARY_AGGREGATE_BOUND_PROVED"] is True
assert D["SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_REQUIRED"] is True
assert D["SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED"] is False
assert D["GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED"] is False
assert D["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
assert D["A_11_POWER_SAVING_PROVED"] is False
assert D["T_O_SQRT_B_PROVED"] is False
assert D["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
assert D["TH14_NEEDED"] is frozen["TH14_NEEDED"] is True

assert "STAGE14_T50=COMPLETE_BAD_AUXILIARY_BOUND_AND_SELECTOR_SENSITIVE_TWO_MODULUS_BOUNDARY" in result
assert "TH14_NEEDED=true" in result
assert "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false" in result

print("Stage14-t50 frozen boundary validation: PASS")
