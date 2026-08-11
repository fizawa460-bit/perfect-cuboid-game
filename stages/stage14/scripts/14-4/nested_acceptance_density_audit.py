#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-4dy/result.md': [
        'GLOBAL_ACCEPTANCE_PRINCIPAL_DENSITY_RECEIVER=true',
        'GLOBAL_ACCEPTANCE_DENSITY_EXPONENT_ZERO_ON_SATURATING_SEQUENCE=true',
        'PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1',
    ],
    'stages/stage14/14-s7-64/result.md': [
        'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
        'TRANSPORTED_PHYSICAL_ACCEPTANCE_FIXED_POWER_DEFICIT_PROVED=false',
    ],
    'stages/stage14/14-Work-bkX23/result.md': [
        'GLOBAL_BOOLEAN_ACCEPTANCE_PRINCIPAL_CENTERED_SPLIT_EXACT=true',
        'GLOBAL_FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Exact chain rule on nested finite events.
# comp subset alloc subset bal subset omega.
examples = [
    (100, 80, 40, 20),
    (81, 54, 27, 9),
    (64, 64, 32, 16),
    (125, 100, 75, 60),
]
for n0, n1, n2, n3 in examples:
    assert 0 < n3 <= n2 <= n1 <= n0
    mu_bal = Fraction(n1, n0)
    mu_alloc = Fraction(n2, n1)
    mu_comp = Fraction(n3, n2)
    mu_full = Fraction(n3, n0)
    assert mu_full == mu_bal * mu_alloc * mu_comp

# If a product of [0,1] factors is large, every individual factor is at least the product.
for a_num in range(1, 11):
    for b_num in range(1, 11):
        for c_num in range(1, 11):
            a = Fraction(a_num, 10)
            b = Fraction(b_num, 10)
            c = Fraction(c_num, 10)
            p = a * b * c
            assert a >= p and b >= p and c >= p

res = (ROOT / 'stages/stage14/14-4dz/result.md').read_text()
for needle in [
    'STAGE14_4DZ=COMPLETE_PRIMITIVE_SLOPE_ACCEPTANCE_TO_NESTED_CONDITIONAL_DENSITIES',
    'GLOBAL_ACCEPTANCE_DENSITY_CHAIN_RULE_EXACT=true',
    'SATURATION_FORCES_BALANCED_DENSITY_EXPONENT_ZERO=true',
    'SATURATION_FORCES_CONDITIONAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true',
    'SATURATION_FORCES_CONDITIONAL_COMPLETION_DENSITY_EXPONENT_ZERO=true',
    'ANY_ONE_FIXED_POWER_FACTOR_DEFICIT_CLOSES_ARITHMETIC_BRANCH=true',
    'SQRT_OBSTRUCTION_REDUCED_TO_NESTED_PRIMITIVE_SLOPE_ACCEPTANCE_DENSITIES=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle

print({'stage': '14-4dz', 'current_exponent': '1/2', 'next': 'Stage14-4ea'})
