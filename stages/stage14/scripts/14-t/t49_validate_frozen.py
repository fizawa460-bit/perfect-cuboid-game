#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t49/external_frobenius_amplifier.json"
FROZEN = ROOT / "stages/stage14/data/14-t49/frobenius_amplifier_frozen.json"

live = json.loads(LIVE.read_text())
frozen = json.loads(FROZEN.read_text())

assert live["stage"] == frozen["stage"] == "14-t49"
assert live["external_split_prime_amplifier"]["external_physical_character_checks"] == frozen["external_physical_character_checks"]

for side, live_key in (("endogenous", "frozen_endogenous"), ("external", "frozen_external_amplifier")):
    a = frozen[side]
    b = live[live_key]
    assert b["H"] == a["H"]
    assert b["P"] == a["P"]
    assert b["A1"] == a["A1"]
    assert b["max_bad_test_primes_per_squareclass"] == a["max_bad"]
    assert b["full_frobenius"] == a["full_frobenius"]
    assert b["diagonal_frobenius"] == a["diagonal_frobenius"]
    assert b["offdiagonal_frobenius"] == a["offdiagonal_frobenius"]
    assert b["max_offdiagonal_row_l2"] == a["max_row_l2"]
    assert abs(b["offdiag_to_random_scale_H_P_Pminus1"] - a["offdiag_random_scale_ratio"]) < 1e-15

assert live["frozen_external_amplifier"]["min_test_prime"] == frozen["external"]["min_prime"]
assert live["frozen_external_amplifier"]["max_test_prime"] == frozen["external"]["max_prime"]

pk = live["product_kernel_order_of_operations"]
fpk = frozen["product_kernel"]
assert pk["cross_kernel_support"] == fpk["support"]
assert pk["refinement_groups"] == fpk["refinement_groups"]
assert pk["total_pair_mass_sum_c"] == fpk["total_pair_mass"]
assert pk["principal_cross_kernel_mass"] == fpk["principal_mass"]
assert pk["max_nonprincipal_cross_kernel_multiplicity"] == fpk["max_nonprincipal_multiplicity"]
assert pk["pair_mass_with_nonempty_shared_test_prime_support"] == fpk["shared_test_prime_pair_mass"]
assert pk["naive_pair_coefficient_energy_sum_c_squared"] == fpk["E4"]
assert pk["naive_nonprincipal_pair_coefficient_energy"] == fpk["nonprincipal_E4"]

D = live["decision"]
assert D["STAGE14_T49"] == frozen["boundary"]
assert D["EXTERNAL_SPLIT_PRIME_AMPLIFIER_VALID"] is True
assert D["PRINCIPAL_COLLISION_FROBENIUS_LOWER_BOUND"] is True
assert D["UNIFORM_WORST_ROW_BOUND_REQUIRED"] is False
assert D["AVERAGED_TWO_PRIME_MEAN_SQUARE_SUFFICIENT_FOR_A1_NEAR_LINEAR"] is True
assert D["PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_IS_CIRCULAR"] is True
assert D["GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED"] is False
assert D["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
assert D["A_11_POWER_SAVING_PROVED"] is False
assert D["T_O_SQRT_B_PROVED"] is False
assert D["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
assert D["TH14_NEEDED"] is False

print("Stage14-t49 frozen ledger and boundary: PASS")
