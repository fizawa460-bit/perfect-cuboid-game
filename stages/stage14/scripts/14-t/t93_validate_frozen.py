#!/usr/bin/env python3
import json
from pathlib import Path
p=Path('stages/stage14/data/14-t93/conjugation_pairing_frozen.json')
x=json.loads(p.read_text())
b=x['boundary']
assert b['CONJUGATION_IS_GLOBAL_ORIENTATION_ANTIPODE']
assert b['WALSH_PARITY_SPLIT_EXACT']
assert b['ODD_WALSH_SECTOR_ANTIPODALLY_CENTERED']
assert not b['PRINCIPAL_CUBE_MEAN_KILLED_BY_CONJUGATION']
assert not b['CENTERED_EVEN_SPECTRUM_ELIMINATED']
assert not b['TH27_NEEDED']
assert b['CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT']=='1/2'
assert not b['STRICT_SUBSQRT_POWER_SAVING_PROVED']
assert b['NEXT']=='Stage14-t94'
print('Stage14-t93 frozen boundary validated')
