#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / 'stages' / 'stage27'

def read(path):
    return path.read_text(encoding='utf-8')

def req(text, marker):
    assert marker in text, f'missing marker: {marker}'

m = read(S27/'27-20-r302m'/'result.md')
for marker in (
    'STRUCTURE_RADAR_REDUCTION_IMPORTED=true',
    'SAME_MEASURE_QUADRATIC_FORM_RECEIVER_DERIVED=true',
    'PUBLISHED_LARGE_SIEVE_APPLICABILITY_PROVED=false',
):
    req(m, marker)

n = read(S27/'27-20-r302n'/'result.md')
for marker in (
    'AUDIT_REPAIR_APPLIED=true',
    'BASIS_VECTOR_DIAGONAL_NECESSITY_PROVED=true',
    'PSD_NO_CANCELLATION_REASON_WITHDRAWN=true',
    'BASELINE_SUBTRACTION_ESCAPE_REMOVED=true',
):
    req(n, marker)

o = read(S27/'27-20-r302o'/'result.md')
for marker in (
    'AUDIT_REPAIR_APPLIED=true',
    'NEXT_THEOREM=MAINWallPrimitiveInverseFrequencyDiagonalAndRemainderOperatorDeficitTheorem',
    'BASELINE_SUBTRACTION_ADAPTER_PROVED=false',
):
    req(o, marker)

checks = {
    '27-20-r302p': (
        'INVERSE_PHASE_DIAGONAL_CANCELLATION_AVAILABLE=false',
        'FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencySingleFrequencyPhysicalEnergyDeficit',
    ),
    '27-20-r302q': (
        'ALL_C_OPERATOR_DEFICIT_REQUIRES_UNIFORM_DIAGONAL_POWER=true',
        'ACTUAL_COEFFICIENT_FALLBACK_LOGICALLY_AVAILABLE=true',
    ),
    '27-20-r302r': (
        'COEFFICIENT_SPECIFIC_DIAGONAL_RECEIVER_DERIVED=true',
        'PARSEVAL_ALONE_DISCHARGES_DIAGONAL_RECEIVER=false',
    ),
    '27-20-r302s': (
        'BAD_DIAGONAL_MODE_SET_DEFINED=true',
        'EXCEPTIONAL_MASS_SPLIT_IDENTITY_PROVED=true',
        'BAD_MODE_FOURIER_ENERGY_DEFICIT_PROVED=false',
    ),
    '27-20-r302t': (
        'ACTUAL_COEFFICIENT_OFFDIAGONAL_RECEIVER_DERIVED=true',
        'FULL_REMAINDER_OPERATOR_NORM_REQUIRED=false',
    ),
    '27-20-r302u': (
        'AUDIT_REPAIR_CHAIN_COMPLETE=true',
        'UNIFORM_OPERATOR_PACKAGE_DERIVED=true',
        'ACTUAL_FOURIER_VECTOR_PACKAGE_DERIVED=true',
        'FREEZE_FOR_STRUCTURE_RADAR=false',
        'NEXT_DERIVED_ROUTE=27-20-r302v',
    ),
}

for route, markers in checks.items():
    text = read(S27/route/'result.md')
    for marker in markers:
        req(text, marker)
    for marker in (
        'STRICT_SUB_SQRT_UPPER_PROVED=false',
        'NEW_MU_LT_HALF_PROVED=false',
        'TRUE_N2_EXPONENT_IDENTIFIED=false',
        'ADVANCE_TO_CHECKPOINT50=false',
    ):
        req(text, marker)

reg = json.loads(read(S27/'27-20-r302p-u'/'batch-registry.json'))
assert reg['status'] == 'BATCH_SUBMITTED_PENDING_FRESH_AUDIT'
assert reg['audit_status'] == 'PENDING'
assert reg['merge_allowed'] is False
assert reg['fresh_reaudit_required'] is True
assert reg['freeze_for_structure_radar'] is False
assert reg['advance_to_checkpoint50'] is False
assert reg['next_derived_route'] == '27-20-r302v'
assert reg['claims']['baseline_subtraction_escape_removed'] is True
assert reg['claims']['basis_vector_diagonal_necessity_proved'] is True
assert reg['claims']['bad_mode_fourier_energy_deficit_proved'] is False
assert reg['claims']['actual_coefficient_offdiagonal_deficit_proved'] is False

print('Stage27-20-r302p-u batch verification: PASS')
