#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-Work-blX24/result.md': [
        'COMMON_PRINCIPAL_SCALE_RELOCATION_PRINCIPLE_PROVED=true',
        'COMMON_ADAPTER_PROVED=false',
    ],
    'stages/stage14/14-4ea/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
        'MAINLINE_H_NEEDED=false',
    ],
    'stages/stage14/14-s7-71/result.md': [
        'SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true',
        'S7_71_NEW_AUXILIARY_H_NEEDED=true',
        'S7_71_AUXILIARY_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity',
        'NEXT=Stage14-sH71',
    ],
    'stages/stage14/14-t108/result.md': [
        'Q_SUPPORT_IS_PROJECTED_PRIMITIVE_SUM_OF_TWO_SQUARES_INCIDENCE=true',
        'T_ROUTE_H_NEEDED=true',
        'T_ROUTE_H_BLOCKING=true',
        'NEXT=Stage14-tH28',
    ],
    'stages/stage14/14-t108/th28-target.md': [
        'CanonicalLPFPrimitiveSumOfTwoSquaresProjectedPhysicalSupportSieveOrDispersion',
        'Q=ell*(u^2+v^2)',
    ],
}

for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Exact s-route lift: C | X^2+Y^2 iff there is an integral quotient m.
cases = [
    (5, 1, 2),
    (5, 2, 1),
    (13, 2, 3),
    (17, 1, 4),
    (25, 3, 4),
    (29, 2, 5),
    (37, 1, 6),
]
checked = 0
for C, X, Y in cases:
    n = X * X + Y * Y
    divides = (n % C == 0)
    if divides:
        m = n // C
        assert m > 0
        assert X * X + Y * Y == C * m
    checked += 1

# Non-divisible examples must not admit an integral quotient.
for C, X, Y in [(5, 1, 1), (13, 1, 2), (17, 2, 3), (29, 1, 3)]:
    n = X * X + Y * Y
    assert n % C != 0

res = (ROOT / 'stages/stage14/14-Work-bmX25/result.md').read_text()
for needle in [
    'STAGE14_WORK_BMX25=COMPLETE_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_COMMON_LANGUAGE_WITH_SEPARATE_H_CONTRACTS',
    'S_ROUTE_ROOT_DIVISIBILITY_LIFTS_TO_NORM_FACTOR_EQUATION=true',
    'S_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true',
    'T_ROUTE_PROJECTED_PRIMITIVE_NORM_FORM_INCIDENCE=true',
    'COMMON_PROJECTED_PRIMITIVE_GAUSSIAN_NORM_FORM_LANGUAGE_PROVED=true',
    'COMMON_ARITHMETIC_NORM_FORM_ADAPTER_PROVED=false',
    'MAINLINE_H_NEEDED=false',
    'S_ROUTE_H_NEEDED=true',
    'S_ROUTE_H_REQUEST=Stage14-sH71',
    'FIXED_U_H_NEEDED=true',
    'TH28_NEEDED=true',
    'COMMON_H_AUDIT_MERGE_ALLOWED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'STRICT_SUBSQRT_POWER_SAVING_PROVED=false',
]:
    assert needle in res, needle

print({
    'stage': '14-Work-bmX25',
    's_norm_factor_lift_cases_checked': checked,
    'common_projected_norm_form_language': True,
    'arithmetic_adapter': False,
    'sH71_needed': True,
    'tH28_needed': True,
    'status': 'ok',
})
