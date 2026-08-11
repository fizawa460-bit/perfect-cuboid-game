#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
result=(ROOT/'stages/stage14/14-t91/result.md').read_text()
frozen=json.loads((ROOT/'stages/stage14/data/14-t91/orientation_hypercube_frozen.json').read_text())
for needle in [
'STAGE14_T91=COMPLETE_PRIMITIVE_GAUSSIAN_ORIENTATION_HYPERCUBE_AND_EXCEPTIONAL_SUPPORT_LOCALIZATION',
'PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED=true',
'PRIME_POWER_EXPONENT_SPLITTING_ALLOWED=false',
'PRIMITIVE_COVER_MASK_AUTOMATIC_ON_ORIENTATION_HYPERCUBE=true',
'FIXED_PACKET_EXCEPTIONAL_SUPPORT_DEFINED=true',
'FULL_GOOD_PRIME_COEFFICIENT_MULTIPLICATIVITY_PROVED=false',
'TH26_TARGET_REOPENED=false','TH27_NEEDED=false',
'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2','STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
'NEXT=Stage14-t92']:
    assert needle in result, needle
b=frozen['boundary']
assert b['PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED'] is True
assert b['PRIME_POWER_EXPONENT_SPLITTING_ALLOWED'] is False
assert b['TH26_TARGET_REOPENED'] is False
assert b['TH27_NEEDED'] is False
assert b['CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT']=='1/2'
assert b['STRICT_SUBSQRT_POWER_SAVING_PROVED'] is False
assert b['NEXT']=='Stage14-t92'
print('Stage14-t91 frozen boundary validated')
