#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-toolbox-bc/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "stages/stage14/14-X15/result.md": "THREE_COMPLETE_COORDINATE_COUNTS_MULTIPLICABLE=false",
    "stages/stage14/14-4di/result.md": "FULL_CONDUCTOR_ENDPOINT_PROVED=true",
    "stages/stage14/14-4diH/result.md": "CERTIFIED_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-s7-50/result.md": "EFFECTIVE_MODULUS_EQUALS_C_STAR_AT_FIXED_POWER=true",
    "stages/stage14/14-sH50/result.md": "CERTIFIED_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-s7-51/result.md": "SQRT_PRINCIPAL_SATURATION_FORCES_PRODUCT_MEAN=Bo1",
    "stages/stage14/14-t90/result.md": "Q_WEIGHT_REDUCED_TO_GAUSSIAN_ORIENTATION_SUM=true",
    "stages/stage14/14-t91/result.md": "GENERIC_COFACTOR_PARAMETER_IS_SPLIT_PRIME_ORIENTATION_CUBE=true",
    "stages/stage14/14-tH26/result.md": "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
}

for rel, needle in required.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

result = (ROOT / "stages/stage14/14-Work-bdX16/result.md").read_text()
locks = [
    "TOOLBOX_BD_COMPONENT_COMPLETE=true",
    "X16_COMPONENT_COMPLETE=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "COMMON_PRINCIPAL_CENTERED_ORIENTATION_INTERFACE_PROVED=true",
    "GLOBAL_AND_FIXED_U_RECEIVERS_EQUIVALENT=false",
    "FIXED_U_SAVING_CROSS_PROMOTABLE=false",
    "X15_COMPLETE_COORDINATE_COUNTS_MULTIPLICABLE=false",
    "NEW_BDX16_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]
for needle in locks:
    assert needle in result, needle

print(json.dumps({
    "stage": "14-Work-bdX16",
    "sources": len(required),
    "toolbox_bd_complete": True,
    "x16_complete": True,
    "current_exponent": "1/2",
    "strict_subsqrt_saving": False,
    "common_interface": "principal-density-plus-centered-orientation",
    "global_fixed_u_equivalent": False,
    "cross_promotion": False,
    "additional_h_needed": False,
    "new_bdx16_saving": False,
}, sort_keys=True))
