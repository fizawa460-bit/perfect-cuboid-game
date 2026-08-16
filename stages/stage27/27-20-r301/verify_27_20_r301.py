#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
r=(ROOT/'stages/stage27/27-20-r301/result.md').read_text()
required=[
'M3_SUBSET_N2=false','N2_SUBSET_M3=false','STAGE20_UPPER_DIRECTLY_BOUNDS_N2=false',
'COMMON_HOST=SHARED_EDGE_TWO_FACE_TORIC_HOST','E8_RAW_TRANSPLANT_STRICT_SUBHALF=false',
'STAGE20_THIRD_FACE_LOCAL_FACTORS_TRANSFER_TO_SPACE=false','SPACE_DIAGONAL_THIN_COVER_FIXED_POWER_THEOREM_PROVED=false',
'STRICT_SUB_SQRT_UPPER_PROVED=false','NEXT_DERIVED_ROUTE=27-20-r301a']
for x in required: assert x in r, x
ctl=json.loads((ROOT/'stages/stage27/27-controller.json').read_text())
route=ctl['derived_routes']['Stage27-20-r301']
assert route['status']=='PARALLEL_PREFLIGHT_SUBMITTED_PENDING_FRESH_AUDIT'
assert route['route_kind']=='UPPER_REENTRY_PREFLIGHT'
assert route['trigger_checkpoint']==30
assert route['source_stage']=='Stage20'
assert route['strict_sub_sqrt_upper_proved'] is False
assert ctl['state']['CURRENT_CHECKPOINT']==40
print('Stage27-20-r301 verifier: PASS')
