from pathlib import Path

root = Path(__file__).resolve().parents[3]
result = (Path(__file__).with_name('result.md')).read_text(encoding='utf-8')
progress = (Path(__file__).with_name('progress.md')).read_text(encoding='utf-8')

required_result = [
    'STAGE27_20_R302M_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT',
    'STRUCTURE_RADAR_REDUCTION_IMPORTED=true',
    'SAME_MEASURE_QUADRATIC_FORM_RECEIVER_DERIVED=true',
    'PUBLISHED_LARGE_SIEVE_APPLICABILITY_PROVED=false',
    'STRICT_SUB_SQRT_UPPER_PROVED=false',
    'ADVANCE_TO_CHECKPOINT50=false',
    'NEXT_DERIVED_ROUTE=27-20-r302n',
]
required_progress = [
    'ADVANCEMENT_POLICY=CONTINUE_THROUGH_EXTERNAL_GATE_REDUCTIONS',
    'FREEZE_FOR_STRUCTURE_RADAR=false',
    'UNRESOLVED_EXTERNAL_GATE_MAY_ADVANCE_BY_RECEIVER_REDUCTION=true',
]
for token in required_result:
    assert token in result, token
for token in required_progress:
    assert token in progress, token
print('Stage27-20-r302m verifier: PASS')
