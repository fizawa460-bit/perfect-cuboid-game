import json
from pathlib import Path
p=Path('stages/stage14/data/14-t94/antipodal_quotient_frozen.json')
d=json.loads(p.read_text())
assert d['stage']=='14-t94'
b=d['boundary']
assert b['ANTIPODAL_QUOTIENT_REDUCTION_PROVED'] is True
assert b['ODD_WALSH_SECTOR_REOPENED'] is False
assert b['PAIR_OCCUPANCY_DEFICIT_FIXED_POWER_SAVING_PROVED'] is True
assert b['PRINCIPAL_PAIR_MEAN_ELIMINATED'] is False
assert b['TH27_NEEDED'] is False
assert b['CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT']=='1/2'
assert b['STRICT_SUBSQRT_POWER_SAVING_PROVED'] is False
print('Stage14-t94 frozen boundary validated')
