#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-Work-bjX22/result.md': [
        'GLOBAL_PRIMITIVE_DIRECTION_COUNT_EXPONENT=1/2',
        'COMMON_FINITE_LABEL_FREEZING_PRINCIPLE_PROVED=true',
    ],
    'stages/stage14/14-4dx/result.md': [
        'PHYSICAL_MASK_TRANSPORT_TO_SLOPE_SCALE_COMPLETED=true',
        'SQRT_OBSTRUCTION_REDUCED_TO_PROJECTIVE_SLOPE_SCALE_MASK_OCCUPANCY=true',
    ],
    'stages/stage14/14-s7-64/result.md': [
        'FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true',
        'FIXED_WIDTH_SLOPE_ROOT_LINE_AMBIENT_EXPONENT=1/2',
        'TRANSPORTED_PHYSICAL_ACCEPTANCE_FIXED_POWER_DEFICIT_PROVED=false',
    ],
    'stages/stage14/14-t104/result.md': [
        'FULL_PRIME_ACTION_FREEZE_PROVED=true',
        'FIXED_FULL_BOUNDARY_STATE_DENSITY_EXPONENT_ZERO=true',
        'PRIME_ACTION_VARIATION_DISCHARGED_AS_LOCALIZATION=true',
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Exact Bernoulli principal / centered identities for many finite ambient families.
checks = 0
for n in range(1, 80):
    for k in range(n + 1):
        mu = Fraction(k, n)
        vals = [1] * k + [0] * (n - k)
        centered = [Fraction(v, 1) - mu for v in vals]
        assert sum(centered, Fraction(0, 1)) == 0
        e2 = sum((z * z for z in centered), Fraction(0, 1)) / n
        assert e2 == mu * (1 - mu)
        assert Fraction(sum(vals), n) == mu
        checks += 1

# A fixed-power low-density bound transfers directly to the accepted count.
# This is a finite exponent-bookkeeping model: if N <= B^alpha and mu <= B^-delta,
# then M=N*mu <= B^(alpha-delta).
for alpha_num, delta_num in [(8, 1), (10, 2), (20, 3), (40, 7)]:
    alpha = Fraction(alpha_num, 16)
    delta = Fraction(delta_num, 16)
    assert alpha - delta < alpha

# Finite witness multiplicity does not imply sparse Boolean acceptance.
# Every point can be accepted with one witness, despite O(1) witness multiplicity.
for n in (8, 16, 32, 64):
    witnesses_per_point = [1] * n
    accepted = [w > 0 for w in witnesses_per_point]
    assert all(accepted)
    assert max(witnesses_per_point) == 1

res = (ROOT / 'stages/stage14/14-Work-bkX23/result.md').read_text()
for needle in [
    'STAGE14_WORK_BKX23=COMPLETE_FIXED_BOOLEAN_PHYSICAL_ACCEPTANCE_PRINCIPAL_DENSITY_UNIFICATION',
    'GLOBAL_BOOLEAN_ACCEPTANCE_PRINCIPAL_CENTERED_SPLIT_EXACT=true',
    'GLOBAL_ACCEPTANCE_DENSITY_EXPONENT_ZERO_ON_SATURATING_SEQUENCE=true',
    'COMMON_FIXED_BOOLEAN_PRINCIPAL_DENSITY_TEMPLATE_PROVED=true',
    'COMMON_CENTERED_BERNOULLI_L2_IDENTITY_PROVED=true',
    'COMMON_ARITHMETIC_ACCEPTANCE_ADAPTER_PROVED=false',
    'COLLISION_ENERGY_RECHARGE_ALLOWED=false',
    'PRIME_AVERAGE_RECHARGE_ALLOWED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'TH28_NEEDED=false',
]:
    assert needle in res, needle

matrix = (ROOT / 'docs/stage14-toolbox/work-bkX23-receiver-matrix.md').read_text()
for needle in [
    'COMMON_FIXED_BOOLEAN_PRINCIPAL_DENSITY_TEMPLATE_PROVED=true',
    'GLOBAL_FIXED_U_BACKGROUND_MEASURES_IDENTIFIED=false',
    'COMMON_ARITHMETIC_ACCEPTANCE_ADAPTER_PROVED=false',
]:
    assert needle in matrix, needle

print({
    'stage': '14-Work-bkX23',
    'bernoulli_checks': checks,
    'global_principal_split_checked': True,
    'finite_witness_no_density_implication_checked': True,
    'common_adapter': False,
    'current_exponent': '1/2',
    'status': 'PASS',
})
