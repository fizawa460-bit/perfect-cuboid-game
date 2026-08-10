#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
LIVE = ROOT / "stages/stage14/data/14-t52/ssgc_principal_resonance.json"
FROZEN = ROOT / "stages/stage14/data/14-t52/ssgc_principal_resonance_frozen.json"
RESULT = ROOT / "stages/stage14/14-t52/result.md"

live = json.loads(LIVE.read_text())
frozen = json.loads(FROZEN.read_text())
result = RESULT.read_text()

p = live["frozen_principal_audit"]
fp = frozen["principal"]
assert p["H"] == fp["H"] == 560
assert p["A1"] == fp["A1"] == 592
assert p["principal_offdiagonal_ordered_mass"] == fp["offdiagonal_ordered_mass"] == 32
assert p["principal_offdiagonal_unordered_blocks"] == fp["original_unordered_blocks"] == 16
assert p["same_exact_unit_pair_ordered_mass"] == fp["exact_unit_residue_absorbed_ordered_mass"] == 4
assert p["residue_offdiagonal_principal_ordered_mass"] == fp["post_residue_ordered_mass"] == 28
assert p["residue_absorbed_distinct_ell_blocks"] == fp["absorbed_distinct_ell_blocks"] == 2
assert p["residue_absorbed_same_ell_blocks"] == fp["absorbed_same_ell_blocks"] == 0
assert p["residual_principal_blocks"] == fp["post_residue_blocks"] == 14
assert p["residual_distinct_ell_blocks"] == fp["post_residue_distinct_ell_cross_good_blocks"] == 12
assert p["residual_same_ell_blocks"] == fp["post_residue_same_ell_blocks"] == 2

sg = live["synthetic_quantifier_guard"]
fg = frozen["synthetic_guard"]
for k in (
    "states",
    "auxiliary_primes",
    "exact_pair_energy",
    "residue_collision_energy",
    "two_auxiliary_offdiagonal_second_moment",
    "near_linear_target",
    "failure_factor",
):
    assert sg[k] == fg[k]

D = live["decision"]
assert D["STAGE14_T52"] == frozen["boundary"]
assert D["TH14_CONSUMED"] is True
assert D["SSGC_CONTAINS_GLOBAL_PRINCIPAL_COLLISION_SUBPROBLEM"] is True
assert D["RESIDUE_COLLISION_CONTROL_ALONE_IMPLIES_SSGC"] is False
assert D["FROZEN_POST_RESIDUE_PRINCIPAL_BLOCKS"] == 14
assert D["FROZEN_POST_RESIDUE_DISTINCT_ELL_CROSS_GOOD_BLOCKS"] == 12
assert D["FROZEN_POST_RESIDUE_SAME_ELL_BLOCKS"] == 2
assert D["GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED"] is False
assert D["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
assert D["T_O_SQRT_B_PROVED"] is False
assert D["PERFECT_CUBOID_NONEXISTENCE_PROVED"] is False
assert D["TH15_NEEDED"] is False

for token in (
    "STAGE14_T52=COMPLETE_SSGC_PRINCIPAL_RESONANCE_AUDIT_AND_KUMMER_REIDENTIFICATION",
    "FROZEN_POST_RESIDUE_PRINCIPAL_BLOCKS=14",
    "FROZEN_POST_RESIDUE_DISTINCT_ELL_CROSS_GOOD_BLOCKS=12",
    "FROZEN_POST_RESIDUE_SAME_ELL_BLOCKS=2",
    "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false",
    "TH15_NEEDED=false",
):
    assert token in result

print("Stage14-t52 frozen principal-resonance boundary: OK")
