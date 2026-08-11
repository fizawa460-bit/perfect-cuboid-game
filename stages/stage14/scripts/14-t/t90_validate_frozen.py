#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
result = (ROOT / "stages/stage14/14-t90/result.md").read_text()
frozen = json.loads((ROOT / "stages/stage14/data/14-t90/open_q_weight_frozen.json").read_text())

locks = [
    "STAGE14_T90=COMPLETE_BOUNDED_Q_WEIGHT_OPENING_LOCAL_SELECTOR_PEEL_AND_GAUSSIAN_ORIENTATION_CORE",
    "PHYSICAL_Q_WEIGHT_EXACT_SELECTOR_EXPANSION_PROVED=true",
    "PRIMITIVE_COVER_MOBIUS_EXPANSION_EXACT=true",
    "FOUR_CELL_LABELS_DETERMINED_BY_GAUSSIAN_LABEL=true",
    "ENDPOINT_PROJECTIVE_SELECTOR_CHARACTER_EXPANSION_EXACT=true",
    "Q_WEIGHT_REDUCED_TO_GAUSSIAN_ORIENTATION_SUM=true",
    "FULL_REDUCED_WEIGHT_MULTIPLICATIVE_PROVED=false",
    "ONE_DIMENSIONAL_CANONICAL_LPF_GAUSSIAN_ORIENTATION_CORRELATION_PROVED=true",
    "TH26_NEEDED=true",
    "TH26_DISPATCHED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "NEXT=Stage14-t91",
]
for needle in locks:
    assert needle in result, needle

boundary = frozen["boundary"]
assert boundary["TH26_NEEDED"] is True
assert boundary["TH26_DISPATCHED"] is False
assert boundary["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "1/2"
assert boundary["STRICT_SUBSQRT_POWER_SAVING_PROVED"] is False
assert boundary["NEXT"] == "Stage14-t91"

target = (ROOT / "stages/stage14/14-t90/th26-target.md").read_text()
for needle in [
    "PARENT_STAGE=Stage14-t90",
    "PARENT_RECEIVER=SharedUCanonicalLPFPrimitiveGaussianCofactorRepresentationCharacterWeightedPhysicalSieve",
    "H_NUMBER=26",
    "H_TARGET_FROZEN_AT_PARENT_DISPATCH=true",
    "Sum_U,chi(delta0)",
    "OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=true|false",
]:
    assert needle in target, needle

print("Stage14-t90 frozen boundary validated")
