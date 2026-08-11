#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
result=(ROOT/'stages/stage14/14-t92/result.md').read_text()
frozen=json.loads((ROOT/'stages/stage14/data/14-t92/walsh_orientation_frozen.json').read_text())
locks=[
'STAGE14_T92=COMPLETE_GENERIC_ORIENTATION_WALSH_CENTERING_AND_HIGH_DEGREE_BARRIER',
'GENERIC_ORIENTATION_WALSH_EXPANSION_EXACT=true',
'PRINCIPAL_CUBE_MEAN_ISOLATED=true',
'CENTERED_ORIENTATION_COEFFICIENT_MEAN_ZERO=true',
'BOUNDED_WALSH_DEGREE_PROVED=false',
'FIXED_DEGREE_TAIL_POWER_SAVING_PROVED=false',
'FINITE_CHARACTER_DECOMPOSITION_READY=false',
'PRINCIPAL_REPRESENTATION_DENSITY_OBSTRUCTION_RETAINED=true',
'TH26_COMPLETE_CONSUMED=true',
'TH26_TARGET_REOPENED=false',
'TH27_NEEDED=false',
'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
'NEXT=Stage14-t93']
for x in locks: assert x in result,x
b=frozen['boundary']
assert b['TH27_NEEDED'] is False
assert b['CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT']=='1/2'
assert b['NEXT']=='Stage14-t93'
# Immutable predecessor/H locks.
t91=(ROOT/'stages/stage14/14-t91/result.md').read_text()
th26=(ROOT/'stages/stage14/14-tH26/result.md').read_text()
assert 'PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED=true' in t91
assert 'OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false' in th26
assert 'PrincipalGaussianRepresentationDensityAndNonmultiplicativeCenteredCofactorCoefficient' in th26
print('Stage14-t92 frozen boundary validated')
