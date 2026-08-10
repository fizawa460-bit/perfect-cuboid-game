#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t77/projective_ray_character_frozen.json"
RESULT = ROOT / "stages/stage14/14-t77/result.md"
TH21 = ROOT / "stages/stage14/14-tH21/result.md"
S738 = ROOT / "stages/stage14/14-s7-38/result.md"


def main():
    d = json.loads(DATA.read_text())
    b = d["boundary"]
    assert d["reciprocal_states"] == 560
    assert d["invisible_states"] == 419
    assert d["radial_identity_checks"] == 419
    assert d["radial_isotropic_prime_checks"] == 7
    assert d["ray_unit_prime_checks"] == 1370
    assert d["ray_projective_prime_checks"] == 1370
    assert d["ray_group_order_checks"] == 419
    assert d["diagnostic_balanced_states"] == 293
    assert d["diagnostic_balanced_deficient_states"] == 2
    assert d["diagnostic_balanced_deficient_ray_active_states"] == 2
    assert d["diagnostic_balanced_deficient_radial_only_states"] == 0
    assert d["ray_active_states"] == 419
    assert d["radial_nontrivial_states"] == 7
    assert d["ray_trivial_states"] == 0
    assert d["max_Q_rad"] == 5
    assert d["max_Q_ray"] == 56039519
    assert d["chosen_component_prime_histogram"] == [[1,250],[2,339],[3,417],[4,364]]
    assert b["STAGE14_T77"].startswith("COMPLETE_")
    assert b["RADIAL_SUPPORT_MOVING_PI_PHASE"] is False
    assert b["PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT"] is True
    assert b["RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY"] is True
    assert b["FULL_PHYSICAL_WEIGHT_TENSOR_FACTORIZATION_PROVED"] is False
    assert b["RAY_ACTIVE_TYPEII_ENERGY_PROVED"] is False
    assert b["TH22_NEEDED"] is True
    assert b["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "61/112"
    assert b["NEXT"] == "Stage14-t78"
    text = RESULT.read_text()
    assert "CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve" in text
    assert "TH22_NEEDED=true" in text
    assert "OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false" in TH21.read_text()
    assert "V(B) << B^(61/112+o(1))" in S738.read_text()
    print("Stage14-t77 frozen boundary: OK")

if __name__ == "__main__": main()
