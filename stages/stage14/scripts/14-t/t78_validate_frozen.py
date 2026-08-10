#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t78/external_kappa_gcd_tensor_frozen.json"

obj = json.loads(DATA.read_text())
assert obj["stage"] == "14-t78"
assert obj["reciprocal_states"] == 560
assert obj["invisible_states"] == 419
assert obj["ray_modulus_formula_checks"] == 419
assert obj["radial_only_equivalence_checks"] == 419
assert obj["four_cell_checks"] == 419
assert obj["cofactor_residual_product_checks"] == 419
assert obj["sharp_hyperbola_cancellation_checks"] == 419
assert obj["k_supported_cell_checks"] == 419
assert obj["mobius_indicator_regressions"] == 2520
assert obj["four_cell_independent_regressions"] == 13689
assert obj["diagnostic_radial_only_states"] == 0
assert obj["diagnostic_ray_active_states"] == 419
assert obj["max_g"] == 21
assert obj["max_k_supported_four_cell_orientation_bound"] == 16
b = obj["boundary"]
assert b["STAGE14_T78"] == "COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION"
assert b["RAY_MODULUS_EQUALS_EXTERNAL_KAPPA_OUTSIDE_GK"] is True
assert b["RADIAL_ONLY_IFF_EXTERNAL_KAPPA_DIVIDES_ANGULAR_GCD"] is True
assert b["ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED"] is True
assert b["SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD"] is True
assert b["TH22_NEEDED"] is True
assert b["TH23_NEEDED"] is False
assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "23/44"
assert b["NEXT"] == "Stage14-t79"
print("Stage14-t78 frozen boundary: OK")
