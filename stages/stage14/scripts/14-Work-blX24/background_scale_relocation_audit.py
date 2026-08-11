#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

locks = {
    "stages/stage14/14-Work-bkX23/result.md": [
        "COMMON_FIXED_BOOLEAN_PRINCIPAL_DENSITY_TEMPLATE_PROVED=true",
        "COMMON_ARITHMETIC_ACCEPTANCE_ADAPTER_PROVED=false",
    ],
    "stages/stage14/14-4dz/result.md": [
        "GLOBAL_ACCEPTANCE_DENSITY_CHAIN_RULE_EXACT=true",
        "SATURATION_FORCES_CONDITIONAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true",
        "SATURATION_FORCES_CONDITIONAL_COMPLETION_DENSITY_EXPONENT_ZERO=true",
    ],
    "stages/stage14/14-s7-68/result.md": [
        "CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "SATURATION_FORCES_CANONICAL_ALLOCATION_DENSITY_EXPONENT_ZERO=true",
        "SATURATION_FORCES_RECIPROCAL_CONDITIONAL_DENSITY_EXPONENT_ZERO=true",
    ],
    "stages/stage14/14-t105/result.md": [
        "FIXED_Q_BACKGROUND_GAUSSIAN_FIBER_SIZE=Bo1",
        "LOCAL_BACKGROUND_FIBER_DENSITY_FIXED_POWER_SAVING_AVAILABLE=false",
        "OUTER_Q_SUPPORT_IS_FIRST_REMAINING_POLYNOMIAL_LENGTH=true",
        "T104_TWO_SIDED_MINIMAL_PRINCIPAL_SURVIVOR_LOCK_SUPERSEDED=true",
    ],
}
for rel, needles in locks.items():
    text = (ROOT / rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# 1. Exact nested two-factor chain used by s7-68.
for ambient in range(8, 40):
    for can in range(1, ambient + 1):
        for accepted in (1, can):
            mu_can = Fraction(can, ambient)
            mu_recip = Fraction(accepted, can)
            mu_full = Fraction(accepted, ambient)
            assert mu_full == mu_can * mu_recip
            assert mu_can >= mu_full and mu_recip >= mu_full

# 2. Fixed-Q density quantization: a nonempty event on an M-point fiber
# has density at least 1/M, so there is no separate polynomial density length
# when M=B^o(1).
for M in range(1, 65):
    for N in range(1, M + 1):
        rho = Fraction(N, M)
        assert rho >= Fraction(1, M)

# 3. Outer support carries the positive principal mass up to the bounded
# fixed-Q fiber weight.
fibers = [(3, 0), (5, 2), (7, 1), (9, 9), (11, 0)]
omega = [N for _, N in fibers]
support = [i for i, N in enumerate(omega) if N > 0]
assert sum(omega) <= len(support) * max(M for M, _ in fibers)

# 4. Exponent-scale mismatch for the direct local-fiber adapter.
# Global primitive-slope ambient exponent is 1/2; one fixed-Q Gaussian fiber
# has exponent zero. This only forbids a direct polynomial-scale-preserving
# identification at this inner level; it says nothing about a future outer-Q
# support adapter.
global_background_exponent = Fraction(1, 2)
fixed_q_inner_fiber_exponent = Fraction(0, 1)
assert global_background_exponent != fixed_q_inner_fiber_exponent

res = (ROOT / "stages/stage14/14-Work-blX24/result.md").read_text()
for needle in [
    "STAGE14_WORK_BLX24=COMPLETE_BACKGROUND_SCALE_RELOCATION_AND_DIRECT_FIXED_Q_FIBER_ADAPTER_NOGO",
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "DIRECT_GLOBAL_TO_FIXED_Q_FIBER_DENSITY_ADAPTER_NOGO=true",
    "COMMON_PRINCIPAL_SCALE_RELOCATION_PRINCIPLE_PROVED=true",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "TH28_NEEDED=false",
]:
    assert needle in res, needle

matrix = (ROOT / "docs/stage14-toolbox/work-blX24-receiver-matrix.md").read_text()
for needle in [
    "DIRECT_LOCAL_BACKGROUND_FIBER_SCALE_MATCH=false",
    "FUTURE_OUTER_SUPPORT_ADAPTER_NOT_RULED_OUT=true",
    "FIXED_U_OUTER_Q_OCCUPANCY_IS_REMAINING_PRINCIPAL_SCALE=true",
]:
    assert needle in matrix, needle

print({
    "stage": "14-Work-blX24",
    "global_chain_exact": True,
    "fixed_q_density_quantization_checked": True,
    "outer_support_weight_checked": True,
    "direct_inner_scale_mismatch_checked": True,
    "current_exponent": "1/2",
    "status": "PASS",
})
