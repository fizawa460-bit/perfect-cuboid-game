#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-s7-41/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
    "stages/stage14/14-4cz/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44",
    "stages/stage14/14-X13/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "stages/stage14/14-s7-42/result.md": "SQRT_B_UPPER_BOUND_PROVED=true",
    "stages/stage14/14-s7-43/result.md": "REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualPrimitiveRootLineIncidence",
    "stages/stage14/14-s7-44/result.md": "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "stages/stage14/14-sH44/result.md": "CERTIFIED_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-4da/result.md": "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2",
    "stages/stage14/14-4db/result.md": "REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullJointCoreSingleColumnIncidence",
    "stages/stage14/14-4dc/result.md": "REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy",
    "stages/stage14/14-4dH/result.md": "PREFERRED_RECEIVER=SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity",
    "stages/stage14/14-tH22/result.md": "CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-t80/result.md": "MERGED_TH22_IMPORTED=true",
    "stages/stage14/14-t81/result.md": "TWO_ADDITIVE_FREQUENCIES_COLLAPSE_TO_ONE=Bo1",
    "stages/stage14/14-t82/result.md": "HARD_DIAGONAL_MODULUS_DIVIDES_FIXED_U_SELECTOR=true",
    "stages/stage14/14-tH23/result.md": "CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0",
    "stages/stage14/14-t83/result.md": "PREFERRED_RECEIVER=SharedUBalancedFixedUSelectorDivisorShortDeterminantQuotientCanonicalPrimeCoverBinaryNormEnergy",
}

for rel, needle in required.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

assert Fraction(1, 2) < Fraction(23, 44)
assert Fraction(23, 44) - Fraction(1, 2) == Fraction(1, 44)

bb = (ROOT / "stages/stage14/14-toolbox-bb/result.md").read_text()
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in bb
assert "NEW_BB_WHOLE_FAMILY_POWER_SAVING_PROVED=false" in bb
assert "TH24_NEEDED=false" in bb

print(json.dumps({
    "stage": "14-toolbox-bb",
    "sources": len(required),
    "previous_exponent": "23/44",
    "current_exponent": "1/2",
    "improvement": "1/44",
    "sqrt_upper_bound": True,
    "strict_subsqrt_saving": False,
    "sh44_certified_delta": 0,
    "fourdh_certified_delta": 0,
    "th23_consumed_by_t83": True,
    "th24_needed": False,
    "new_bb_saving": False,
}, sort_keys=True))
