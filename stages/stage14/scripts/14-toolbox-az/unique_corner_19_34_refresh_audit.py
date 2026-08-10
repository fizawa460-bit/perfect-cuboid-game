#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-4cu/result.md": "Stage14-4cu",
    "stages/stage14/14-s7-33/result.md": "Stage14-s7-33",
    "stages/stage14/14-s7-36/result.md": "Stage14-s7-36",
    "stages/stage14/14-X11/result.md": "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34",
    "stages/stage14/14-s7-37/result.md": "REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence",
    "stages/stage14/14-t73/result.md": "Stage14-t73",
    "stages/stage14/14-t74/result.md": "Stage14-t74",
    "stages/stage14/14-tH20/result.md": "TH21_NEEDED=false",
    "stages/stage14/14-t75/result.md": "POST_T75_GENUINE_TWO_VARIABLE_BLOCK_IS_BALANCED_SMALL_G=true",
}

for rel, needle in required.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

chain = [Fraction(5, 8), Fraction(19, 32), Fraction(47, 80),
         Fraction(7, 12), Fraction(4, 7), Fraction(9, 16), Fraction(19, 34)]
assert all(b < a for a, b in zip(chain, chain[1:]))
assert Fraction(13, 24) < Fraction(19, 34)
assert Fraction(7, 16) < Fraction(13, 24)
assert Fraction(19, 34) - Fraction(1, 2) == Fraction(1, 17)

print(json.dumps({
    "stage": "14-toolbox-az",
    "sources": len(required),
    "supersession_chain_strict": True,
    "current_exponent": "19/34",
    "proportional_exponent": "7/16",
    "gap_to_sqrt": "1/17",
    "th21_needed": False,
    "new_az_saving": False,
}, sort_keys=True))
