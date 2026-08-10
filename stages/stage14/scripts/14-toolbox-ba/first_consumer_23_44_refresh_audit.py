#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-s7-37/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34",
    "stages/stage14/14-X12/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128",
    "stages/stage14/14-s7-38/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112",
    "stages/stage14/14-s7-39/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=17/32",
    "stages/stage14/14-4cx/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
    "stages/stage14/14-s7-40/result.md": "TWENTYTHREE_44_SATURATION_POINT_UNIQUE=true",
    "stages/stage14/14-4cy/result.md": "TWENTYTHREE_44_SATURATION_SEGMENT_COLLAPSED_TO_POINT=true",
    "stages/stage14/14-t76/result.md": "Stage14-t76",
    "stages/stage14/14-tH21/result.md": "PROJECTIVE_ROOTLINE_KERNEL_RETAINED=true",
    "stages/stage14/14-t77/result.md": "ARITHMETIC_PROJECTIVE_KERNEL_SEPARATED=true",
    "stages/stage14/14-t78/result.md": "RAY_MODULUS_EXTERNAL_FORMULA=M=K_ext/gcd(K_ext,g)",
    "stages/stage14/14-t79/result.md": "PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy",
}

for rel, needle in required.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

chain = [Fraction(19, 34), Fraction(71, 128), Fraction(61, 112),
         Fraction(17, 32), Fraction(23, 44)]
assert all(b < a for a, b in zip(chain, chain[1:]))
assert Fraction(23, 44) - Fraction(1, 2) == Fraction(1, 44)
assert not (ROOT / "stages/stage14/14-tH22/result.md").exists()

print(json.dumps({
    "stage": "14-toolbox-ba",
    "sources": len(required),
    "supersession_chain_strict": True,
    "current_exponent": "23/44",
    "gap_to_sqrt": "1/44",
    "saturation_point_unique": True,
    "th22_merged_input_imported": False,
    "t79_merged_input_imported": True,
    "new_ba_saving": False,
}, sort_keys=True))
