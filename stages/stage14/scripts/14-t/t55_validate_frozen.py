#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
FROZEN = ROOT / "stages/stage14/data/14-t55/shared_u_projective_trace_frozen.json"

d = json.loads(FROZEN.read_text())
assert d["stage"] == "14-t55"
assert d["reciprocal_states"] == 560
assert d["shared_U_principal_blocks"] == 6
assert d["shared_U_invisible_invisible_blocks"] == 5
assert d["shared_U_mixed_branch_blocks"] == 1
assert d["quartic_cross_ratio_checks"] == 560
assert d["split_prime_trace_checks"] == 11
assert d["inert_prime_trace_checks"] == 11
assert d["fixed_U_PGL2_checks"] == 22
assert d["two_split_prime_CRT_pair_checks"] == 55
assert d["boundary"] == "COMPLETE_SHARED_U_PROJECTIVE_TRACE_AND_CENTERED_SELECTOR_REDUCTION"
assert d["SHARED_U_INVISIBLE_COMPLETE_PROJECTIVE_TRACE_PROVED"] is True
assert d["SHARED_U_CONSTANT_DENSITY_MEAN_CLOSED"] is True
assert d["SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_REQUIRED"] is True
assert d["SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED"] is False
assert d["SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED"] is False
assert d["SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED"] is False
assert d["GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED"] is False
assert d["A_11_POWER_SAVING_PROVED"] is False
assert d["T_O_SQRT_B_PROVED"] is False
assert d["TH15_NEEDED"] is True
print("t55 frozen boundary valid")
