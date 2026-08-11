#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
required = {
    "stages/stage14/14-4dj/result.md": "SQRT_SATURATION_REQUIRES_NEAR_MAXIMAL_CONDITIONAL_OCCUPANCY=true",
    "stages/stage14/14-s7-52/result.md": "SQRT_THREE_PROJECTION_SATURATION_REQUIRES_ALL_MARGINALS_INTERIOR=true",
    "stages/stage14/14-X15/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "stages/stage14/14-Work-bdX16/result.md": "COMMON_PRINCIPAL_CENTERED_ORIENTATION_INTERFACE_PROVED=true",
}
for rel, needle in required.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

result = (ROOT / "stages/stage14/14-4dk/result.md").read_text()
locks = [
    "STAGE14_4DK=COMPLETE_NEAR_MAXIMAL_CELL_INTERIOR_VARIANCE_REDUCTION",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "SQRT_THREE_PROJECTION_SATURATION_REQUIRES_OMEGA=Bo0=true",
    "SQRT_THREE_PROJECTION_SATURATION_REQUIRES_ALL_MARGINALS_INTERIOR=true",
    "NEXT_H_NEEDED=false",
]
for needle in locks:
    assert needle in result, needle

print(json.dumps({
    "stage": "14-4dk",
    "near_maximal_occupancy": True,
    "all_marginals_interior": True,
    "current_exponent": "1/2",
    "strict_subsqrt_saving": False,
    "next_h_needed": False,
    "next": "Stage14-4dl",
}, sort_keys=True))
