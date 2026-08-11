from pathlib import Path

root = Path(__file__).resolve().parents[4]
checks = {
    'stages/stage14/14-4ev/result.md': [
        'HEAVY_RAY_ONLY_POLYNOMIAL_COORDINATE_IS_H=true',
        'FIXED_H_FULL_PHYSICAL_FIBER=Bo1',
    ],
    'stages/stage14/14-4ew/result.md': [
        'RADIAL_SCALE_ENTERS_AS_EXACT_SQUARE_FACTOR=true',
        'FRESH_DIVISOR_SAVING_CLAIMED=false',
    ],
    'stages/stage14/14-4ex/result.md': [
        'FIXED_RAY_SQUAREFREE_KERNEL_K_FIXED=true',
        'RADIAL_H_TO_MOVING_PRODUCT_T_INJECTIVE=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
    ],
    'stages/stage14/14-4-batch/4ev-4ex-report.md': [
        'BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3',
        'BATCH_STOP_REASON=receiver_change',
        'NEXT=Stage14-4ey',
    ],
}
for rel, needles in checks.items():
    text = (root / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)
print('stage14-4 4ev-4ex audit: OK')
