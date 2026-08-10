#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
P = ROOT / "stages/stage14/data/14-t79/ray_character_support_frozen.json"
D = json.loads(P.read_text())

assert D["stage"] == "14-t79"
assert D["reciprocal_states"] == 560
assert D["invisible_states"] == 419
assert D["support_partition_checks"] == 419
assert D["principal_density_checks"] == 419
assert D["support_deficit_checks"] == 4992
assert D["ray_order_phi_lower_checks"] == 4992
assert D["total_physical_support_strata"] == 4992
assert D["max_support_strata_per_state"] == 64
assert D["max_omega_M"] == 6
assert D["independent_squarefree_moduli"] == 486
assert D["independent_support_checks"] == 1783

B = D["boundary"]
assert B["STAGE14_T79"] == "COMPLETE_PRINCIPAL_RAY_DENSITY_AND_ACTIVE_SUPPORT_DEFICIT_STRATIFICATION"
assert B["PROJECTIVE_CHARACTER_ACTIVE_SUPPORT_DECOMPOSITION_PROVED"] is True
assert B["PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY"] is True
assert B["PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE"] is False
assert B["FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED"] is True
assert B["HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT"] is True
assert B["TH23_NEEDED"] is False
assert B["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "23/44"
assert B["NEXT"] == "Stage14-t80"
print("Stage14-t79 frozen boundary OK")
