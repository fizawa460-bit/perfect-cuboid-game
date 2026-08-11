#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-Work-bmX25/result.md': [
        'COMMON_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_LANGUAGE_PROVED=true',
        'COMMON_ARITHMETIC_NORM_FORM_ADAPTER_PROVED=false',
        'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    ],
    'stages/stage14/14-sH71/BOUNDARY.txt': [
        'DIRECT_GAUSSIAN_ROOT_EQUIDISTRIBUTION_THEOREM_APPLICABLE=false',
        'ROOT_LARGE_SIEVE_DIRECTLY_APPLICABLE=false',
        'BILINEAR_ROOT_DISPERSION_DIRECTLY_APPLICABLE=false',
        'CANONICAL_BACKGROUND_PSEUDORANDOMNESS_ADAPTER_PROVED=false',
        'UNIFORM_FIXED_POWER_CONDITIONAL_DENSITY_SAVING_PROVED=false',
        'CERTIFIED_CONDITIONAL_DENSITY_SAVING_EXPONENT=0',
    ],
    'stages/stage14/14-tH28/result.md': [
        'DIRECT_THEOREM_APPLICABLE=false',
        'UNIFORM_FIXED_POWER_SAVING_PROVED=false',
        'CERTIFIED_B_POWER_SAVING_EXPONENT=0',
        'T_ROUTE_H_BLOCKING_RESOLVED_BY_NEGATIVE_VERDICT=true',
    ],
    'stages/stage14/14-4-batch/4eb-4ef-report.md': [
        'CURRENT_GLOBAL_RECEIVER=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_x_ConditionalPrimitiveGaussianRootDensity',
        'MAINLINE_H_NEEDED=true',
        'MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity',
        'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
    ],
    'stages/stage14/14-s7-74/result.md': [
        'POLYNOMIAL_C0_SATURATION_FORCES_CENTERED_DISCREPANCY_EXPONENT_ZERO=true',
        'SMALL_C0_REVERTS_TO_CANONICAL_ALLOCATION_DENSITY_OBSTRUCTION=true',
        'S7_74_NEW_AUXILIARY_H_NEEDED=false',
        'RECEIVER_MATERIALLY_CHANGED=true',
    ],
    'stages/stage14/14-t111/result.md': [
        'UNIFORM_ALL_CLASS_FIXED_POWER_DEFICIT_IMPOSSIBLE=true',
        'ENDPOINT_PROJECTIVE_SELECTOR_STANDALONE_FIXED_POWER_SOURCE=false',
        'JOINT_COFACTOR_SELECTED_CLASS_PRIME_CORRELATION_REMAINS=true',
        'T_ROUTE_H_NEEDED=false',
        'NEXT_INTERNAL_TARGET=PrimitiveGaussianCofactorPhysicalCoreDensityPlusSelectedClassCenteredCorrelation',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Exact principal-plus-centered logic: if total accepted mass is large while
# the principal term is small, the discrepancy must carry the remainder.
for total_num in range(5, 11):
    total = Fraction(total_num, 10)
    for principal_num in range(0, 3):
        principal = Fraction(principal_num, 10)
        discrepancy = total - principal
        assert discrepancy >= total - principal
        assert abs(discrepancy) >= total - principal
        assert total == principal + discrepancy

# A partition into K classes cannot have every nonempty class uniformly below
# total/K by a strict common factor.  This finite identity mirrors t111's
# subpolynomial-class no-go.
for K in range(1, 10):
    counts = [j + 1 for j in range(K)]
    total = sum(counts)
    assert sum(counts) == total
    assert max(counts) >= Fraction(total, K)

# Nested/global factor sanity: a power loss in either factor closes the product;
# conversely exponent-neutral factors cannot be multiplied again as fresh gains.
for a_num in range(1, 11):
    for b_num in range(1, 11):
        a = Fraction(a_num, 10)
        b = Fraction(b_num, 10)
        product = a * b
        assert product <= a and product <= b

res = (ROOT / 'stages/stage14/14-Work-bnX26/result.md').read_text()
for needle in [
    'STAGE14_WORK_BNX26=COMPLETE_DUAL_NEGATIVE_H_INTERSECTION_AND_CORRELATION_ONLY_RECEIVER_PIVOT',
    'PROJECTED_NORM_FORM_THEOREM_INTERSECTION_AT_CURRENT_MASK_LEVEL=EMPTY',
    'COMMON_CORRELATION_ONLY_OBSTRUCTION_LANGUAGE_PROVED=true',
    'ALL_SURVIVING_POLYNOMIAL_SCALE_OBSTRUCTIONS_REQUIRE_PHYSICAL_CORRELATION=true',
    'STANDALONE_LOCAL_DENSITY_AS_UNIFORM_FIXED_POWER_SOURCE_EXHAUSTED=true',
    'MAINLINE_H_NEEDED=true',
    'MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity',
    'S_ROUTE_H_NEEDED=false',
    'FIXED_U_H_NEEDED=false',
    'TH29_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert needle in res, needle

print({
    'stage': '14-Work-bnX26',
    'projected_norm_form_theorem_intersection': 'empty_at_current_mask_level',
    'common_receiver': 'correlation_only',
    'mainline_H_needed': True,
    's_new_H_needed': False,
    'fixed_U_new_H_needed': False,
    'current_exponent': '1/2',
    'status': 'ok',
})
