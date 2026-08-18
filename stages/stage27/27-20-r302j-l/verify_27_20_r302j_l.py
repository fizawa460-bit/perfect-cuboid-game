#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / 'stages' / 'stage27'
def read(p): return p.read_text(encoding='utf-8')
def req(t,s): assert s in t, f'missing marker: {s}'

parent = read(S27/'27-20-r302g-i'/'audit.md')
for s in ('AUDIT_VERDICT=PASS','AUDIT_PR=1073','NEXT_DERIVED_ROUTE=27-20-r302j'):
    req(parent,s)

for route, tokens in {
 '27-20-r302j': ('DIVISOR_FIBER_MULTIPLICITY_ALONE_IMPLIES_HIGH_OCCUPANCY_TAIL=false','UNIFORM_POLYNOMIAL_LOWER_BOUND_FOR_MAIN_HOST_FIBER_PROVED=false','NEXT_DERIVED_ROUTE=27-20-r302k'),
 '27-20-r302k': ('SAME_MEASURE_MAIN_ARITHMETIC_HOST_CORRELATION_TARGET_DERIVED=true','UNWEIGHTED_CLASS_COUNT_SUFFICIENT=false','NEXT_DERIVED_ROUTE=27-20-r302l'),
 '27-20-r302l': ('NEXT_THEOREM=UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit','MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false','NEXT_DERIVED_ROUTE=27-20-r302m')
}.items():
    t=read(S27/route/'result.md')
    for s in tokens: req(t,s)
    for s in ('STRICT_SUB_SQRT_UPPER_PROVED=false','NEW_MU_LT_HALF_PROVED=false','TRUE_N2_EXPONENT_IDENTIFIED=false','ADVANCE_TO_CHECKPOINT50=false'): req(t,s)

audit = read(S27/'27-20-r302j-l'/'audit.md')
for s in (
    'AUDIT_VERDICT=PASS',
    'MATHEMATICAL_AUDIT=PASS',
    'CI_AUDIT=PASS',
    'INTEGRATION_AUDIT=PASS_PREMERGE',
    'AUDIT_PR=1078',
    'AUDITED_CONTENT_COMMIT=227070f914058fc962baa28154c9c5abaf401857',
    'DEDICATED_CI_RUN=32020722384',
    'MERGE_ALLOWED=true',
    'ADVANCE_ALLOWED=false',
    'ADVANCE_TO_CHECKPOINT50=false',
    'NEXT_DERIVED_ROUTE=27-20-r302m',
): req(audit,s)

reg=json.loads(read(S27/'27-20-r302j-l'/'batch-registry.json'))
assert reg['status']=='AUDITED_PASS_PENDING_MERGE'
assert reg['audit_status']=='PASS'
assert reg['merge_allowed'] is True
assert reg['advance_allowed'] is False
assert reg['fresh_reaudit_required'] is False
assert reg['audit_pr']==1078
assert reg['audited_content_commit']=='227070f914058fc962baa28154c9c5abaf401857'
assert reg['claims']['main_arithmetic_host_correlation_power_deficit_proved'] is False
assert reg['claims']['wall_slab_aggregate_deficit_theorem_proved'] is False
assert reg['claims']['strict_sub_sqrt_upper_proved'] is False
assert reg['claims']['new_mu_lt_half_proved'] is False
assert reg['claims']['true_N2_exponent_identified'] is False
assert reg['advance_to_checkpoint50'] is False
assert reg['next_derived_route']=='27-20-r302m'
print('Stage27-20-r302j-l audited pre-merge verification: PASS')
