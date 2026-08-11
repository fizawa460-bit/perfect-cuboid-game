#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
required = {
    "stages/stage14/14-4dk/result.md": "STAGE14_4DK=COMPLETE_NEAR_MAXIMAL_CELL_INTERIOR_VARIANCE_REDUCTION",
    "stages/stage14/14-s7-53/result.md": "EXACT_THREE_WEIGHT_CUMULANT_IDENTITY_PROVED=true",
    "stages/stage14/14-X15/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
}
for rel, needle in required.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

result = (ROOT / "stages/stage14/14-4dl/result.md").read_text()
for needle in [
    "STAGE14_4DL=COMPLETE_PAIRWISE_CORRELATION_COEFFICIENT_LOCALIZATION",
    "PAIRWISE_FIXED_POWER_CORRELATION_DEFICIT_STRICT_SUBSQRT=true",
    "PAIRWISE_SQRT_SATURATION_REQUIRES_RIJ=Bo0=true",
    "CONNECTED_TRIPLE_BRANCH_RETAINED=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT_H_NEEDED=false",
]:
    assert needle in result, needle

print(json.dumps({
    "stage": "14-4dl",
    "pairwise_correlation_localized": True,
    "pairwise_saturation_requires_near_cs": True,
    "connected_triple_retained": True,
    "current_exponent": "1/2",
    "strict_subsqrt_saving": False,
    "next_h_needed": False,
    "next": "Stage14-4dm",
}, sort_keys=True))
