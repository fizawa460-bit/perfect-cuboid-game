#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

# Theorem-source locks.
locks = {
    'stages/stage14/14-sH71/result.md': [
        'UNIFORM_FIXED_POWER_CONDITIONAL_DENSITY_SAVING_PROVED=false',
        'PREFERRED_NEXT_INTERNAL_REDUCTION=CommonCoreScaleStratifiedCanonicalAllocationRootLinePrincipalDensityPlusCenteredDiscrepancy',
    ],
    'stages/stage14/14-4ef/result.md': [
        'ONLY_SIMULTANEOUS_INTEGER_GAUSSIAN_DIVISOR_CORRELATION_CAN_SAVE=true',
        'CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)


def roots_minus_one(n):
    return [x for x in range(1, n) if gcd(x, n) == 1 and (x*x + 1) % n == 0]

# For one frozen oriented root i_C, the root line among unit pairs has density 1/phi(C0).
for C in (5, 13, 17, 65, 85):
    roots = roots_minus_one(C)
    assert roots
    units = [x for x in range(1, C) if gcd(x, C) == 1]
    phi = len(units)
    iC = roots[0]
    hit = 0
    for y in units:
        for x in units:
            if (x - iC*y) % C == 0:
                hit += 1
    assert hit == phi
    assert hit * phi == phi * phi

# Primitive sum-of-two-squares core remains coprime to ab.
for a in range(1, 40):
    for b in range(a+1, 50):
        if gcd(a, b) == 1:
            assert gcd(a*a+b*b, a*b) == 1

for stage, needles in {
    '14-s7-72': [
        'COMMON_CORE_SCALE_CELL_DEFINED=true',
        'POLYNOMIAL_C0_PRINCIPAL_POWER_SAVING_POTENTIALLY_AVAILABLE=true',
        'RECEIVER_MATERIALLY_CHANGED=false',
        'NEXT=Stage14-s7-73',
    ],
    '14-s7-73': [
        'PHYSICAL_ROOT_COUNT_PRINCIPAL_DISCREPANCY_IDENTITY_EXACT=true',
        'POLYNOMIAL_C0_PRINCIPAL_TERM_FIXED_POWER_SMALL=true',
        'CENTERED_DISCREPANCY_FIXED_POWER_BOUND_PROVED=false',
        'NEXT=Stage14-s7-74',
    ],
    '14-s7-74': [
        'POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true',
        'SMALL_C0_REVERTS_TO_CANONICAL_ALLOCATION_DENSITY_OBSTRUCTION=true',
        'RECEIVER_MATERIALLY_CHANGED=true',
        'NEXT=Stage14-s7-75',
    ],
}.items():
    text = (ROOT / f'stages/stage14/{stage}/result.md').read_text()
    for needle in needles:
        assert needle in text, (stage, needle)

print({
    'batch': 's7-72..74',
    'stop': 'receiver_change',
    'small_core_receiver': 'canonical_allocation_density',
    'polynomial_core_receiver': 'centered_root_discrepancy',
    'current_exponent': '1/2',
    'next': 'Stage14-s7-75',
})
