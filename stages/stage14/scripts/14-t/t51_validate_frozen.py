#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t51/exact_pair_diagonal.json"
FROZEN = ROOT / "stages/stage14/data/14-t51/exact_pair_diagonal_frozen.json"

live = json.loads(LIVE.read_text())
frozen = json.loads(FROZEN.read_text())

assert live["stage"] == frozen["stage"] == "14-t51"
assert live["decision"]["STAGE14_T51"] == frozen["boundary"]
assert live["critical_strip_no_alias"]["algebra_checks"] == frozen["critical_strip"]["algebra_checks"]
fa = live["frozen_alias_audit"]
ff = frozen["frozen_alias_audit"]
for key in (
    "states", "external_split_primes", "prime_pair_checks", "min_prime", "max_prime",
    "min_product_modulus", "max_abs_gaussian_coordinate", "exact_pair_collision_energy",
    "exact_pair_max_multiplicity", "residue_pair_collision_energy", "alias_failures",
):
    assert fa[key] == ff[key], (key, fa[key], ff[key])

assert live["diagonal_receiver"]["target_scale_met"] is True
assert live["decision"]["TWO_AUXILIARY_RESIDUE_DIAGONAL_NEAR_LINEAR"] is True
assert live["decision"]["OFFDIAGONAL_TWO_AUXILIARY_RESIDUE_DISPERSION_PROVED"] is False
assert live["decision"]["GLOBAL_EXTERNAL_TWO_PRIME_MEAN_SQUARE_BOUND_PROVED"] is False
assert live["decision"]["A_11_POWER_SAVING_PROVED"] is False
assert live["decision"]["T_O_SQRT_B_PROVED"] is False
assert live["decision"]["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
assert live["decision"]["TH14_STILL_NEEDED"] == frozen["TH14_STILL_NEEDED"] is True
assert live["decision"]["TH15_NEEDED"] == frozen["TH15_NEEDED"] is False
print("Stage14-t51 frozen ledger/boundary: PASS")
