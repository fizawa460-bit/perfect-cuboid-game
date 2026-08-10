#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
doc = (root / "docs/stage14-toolbox/minimal-common-theorem-envelope.md").read_text()
result = (root / "stages/stage14/14-toolbox-aq/result.md").read_text()

required_doc = [
    "CommonPhysicalCenteredPrimePairKernel",
    "PositiveXiKCollision",
    "SignedGaussianDispersion",
    "SharedUBipartiteSquareclassEnergy",
    "PrimePairProjectiveSlopeDispersion",
    "exact subtraction of `z=z'` once",
    "do not bound it",
    "does not improve the unconditional physical whole-family exponent",
]
required_result = [
    "STAGE14_TOOLBOX_AQ=COMPLETE_MINIMAL_COMMON_THEOREM_ENVELOPE_AND_RECEIVER_SEPARATION",
    "COMMON_ENVELOPE_IS_ESTIMATE=false",
    "SIGNED_GAUSSIAN_IMPLIES_POSITIVE_COLLISION=false",
    "RAW_HP2_IMPLIES_CENTERED_H2P=false",
    "DIVISOR_FAN_IMPLIES_BIPARTITE_ENERGY=false",
    "ROW_COLUMN_GLOBALIZATION_ALLOWED=false",
    "RECEIVER_CROSS_PROMOTION_ALLOWED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
    "TOOLBOX_H_CONTINUATION_NEEDED=false",
]

for token in required_doc:
    assert token in doc, f"missing document guard: {token}"
for token in required_result:
    assert token in result, f"missing result guard: {token}"

assert "COMMON_ENVELOPE_IS_ESTIMATE=true" not in result
assert "RECEIVER_CROSS_PROMOTION_ALLOWED=true" not in result
print("stage14-toolbox-aq envelope audit: PASS")
