#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-toolbox-bb/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "stages/stage14/14-X14/result.md": "REMAINING_RECEIVER=SquareRootThetaQuarterSwitchSupportedGaussianNormPhysicalAdmissibilityDensity",
    "stages/stage14/14-4dd/result.md": "FIRST_RESIDUAL_FIXED_POWER_DEFICIT_SAVING_PROVED=true",
    "stages/stage14/14-4de/result.md": "MIXED_FOURTH_ROOT_LINE_PROVED=true",
    "stages/stage14/14-s7-46/result.md": "MIXED_FOURTH_ROOT_TUPLE_PHYSICAL_PACKET_FINITE_FIBER_EQUIVALENCE=true",
    "stages/stage14/14-s7-47/result.md": "SQRT_SATURATION_FOUR_NORM_BLOCKS_PAIRWISE_SEPARATED=true",
    "stages/stage14/14-s7-48/result.md": "GAUSSIAN_NORM_ROTATED_COORDINATE_PRODUCT_REDUCTION_PROVED=true",
    "stages/stage14/14-sH48/result.md": "CERTIFIED_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-4df/result.md": "S7_47_AND_4DF_OVERLAP_SAVINGS_MULTIPLICABLE=false",
    "stages/stage14/14-t84/result.md": "CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF=true",
    "stages/stage14/14-tH24/result.md": "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-t85/result.md": "BINARY_NORM_SQUARE_ROOT_LIFT_MOD_D2=true",
    "stages/stage14/14-t86/result.md": "FORM_DISCRIMINANT=-4*d^2",
    "stages/stage14/14-tH25/result.md": "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-t87/result.md": "HARD_SELECTOR_CONDUCTOR_ENDPOINT=d=Bo1",
}

for rel, needle in required.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

bc = (ROOT / "stages/stage14/14-toolbox-bc/result.md").read_text()
locks = [
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "GLOBAL_AND_FIXED_U_RECEIVERS_EQUIVALENT=false",
    "SH48_CERTIFIED_DELTA=0",
    "TH25_CERTIFIED_DELTA=0",
    "NEW_BC_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]
for needle in locks:
    assert needle in bc, needle

print(json.dumps({
    "stage": "14-toolbox-bc",
    "sources": len(required),
    "current_exponent": "1/2",
    "strict_subsqrt_saving": False,
    "global_receiver_centered": True,
    "fixed_u_endpoint_selector": True,
    "sh48_certified_delta": 0,
    "th24_certified_delta": 0,
    "th25_certified_delta": 0,
    "additional_h_needed": False,
    "new_bc_saving": False,
}, sort_keys=True))
