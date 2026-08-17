#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]

def must(path, *needles):
    text=(ROOT/path).read_text(encoding='utf-8')
    for n in needles:
        assert n in text, (path,n)

must('stages/stage27/27-20-r301d/result.md',
     'SPACE_DIAGONAL_STATE_G_REDUCTION_PROVED=true',
     'SPACE_DIAGONAL_LOCAL_BLOCKER_MASS_FORMULA_PROVED=true',
     'SPACE_DIAGONAL_DELTA_2=2/9',
     'SPACE_DIAGONAL_DELTA_P=2(p-chi4(p))/(p^2+6p+1)',
     'ALL_STAGE20_LOCAL_FACTORS_TRANSFER=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')
must('stages/stage27/27-20-r301e/result.md',
     'SPACE_DIAGONAL_GROWING_PRIME_SIEVE_TRANSFER_PROVED=true',
     'SPACE_DIAGONAL_HOST_SIEVE_BOUND=B(log B)^5/(log log B)^2',
     'HOST_SIEVE_BOUND_BEATS_CURRENT_HALF_POWER=false',
     'SIEVE_FACTOR_MULTIPLIED_WITH_HALF_POWER=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')
must('stages/stage27/27-20-r301f/result.md',
     'SPACE_DIAGONAL_TORUS_FACTORIZATION_PROVED=true',
     'SPACE_DIAGONAL_SQUARECLASS_RECEIVER_DERIVED=true',
     'GAUSSIAN_NORM_FACTOR_STRUCTURE_IDENTIFIED=true',
     'SQUARECLASS_SUPPORT_FIXED_POWER_BOUND_PROVED=false',
     'STRICT_SUB_SQRT_UPPER_PROVED=false')

reg=json.loads((ROOT/'stages/stage27/27-20-r301d-f/batch-registry.json').read_text())
assert reg['routes']==['Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']
assert reg['claims']['host_sieve_beats_half_power'] is False
assert reg['claims']['strict_sub_sqrt_upper_proved'] is False

ctl=json.loads((ROOT/'stages/stage27/27-controller.json').read_text())
for key in ['Stage27-20-r301','Stage27-20-r301a','Stage27-20-r301b','Stage27-20-r301c','Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']:
    assert key in ctl['derived_routes'], key
assert ctl['derived_routes']['Stage27-20-r301']['audit_status']=='PASS'
assert ctl['derived_routes']['Stage27-20-r301a']['audit_status']=='PASS'
assert ctl['derived_routes']['Stage27-20-r301b']['audit_status']=='PASS'
assert ctl['derived_routes']['Stage27-20-r301c']['audit_status']=='PASS'
for key in ['Stage27-20-r301d','Stage27-20-r301e','Stage27-20-r301f']:
    r=ctl['derived_routes'][key]
    assert r['audit_status']=='PENDING'
    assert r['merge_allowed'] is False
    assert r['strict_sub_sqrt_upper_proved'] is False
assert ctl['state']['CURRENT_CHECKPOINT']==40
assert ctl['state']['NEXT_CHECKPOINT']==40
assert ctl['derived_routes']['Stage27-20-r301e']['host_sieve_beats_current_half_power'] is False
assert ctl['derived_routes']['Stage27-20-r301f']['next_derived_route']=='27-20-r301g'
print('Stage27-20-r301d-f verifier: PASS')
