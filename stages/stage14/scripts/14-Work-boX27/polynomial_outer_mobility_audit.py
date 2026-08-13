#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[4]

locks = {
    "stages/stage14/14-Work-bnX26/result.md": [
        "COMMON_CORRELATION_ONLY_OBSTRUCTION_LANGUAGE_PROVED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    ],
    "stages/stage14/14-s7-80/result.md": [
        "FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=UNPROVED",
        "HEAVY_RAY_SPLIT_INTO_FIXED_DATA_BACKGROUND_FIBER_OR_DIFFUSE_RADIAL_SUPPORT=true",
    ],
    "stages/stage14/14-4eq/result.md": [
        "FIXED_RECIPROCAL_DATA_TO_CANONICAL_BACKGROUND_FIBER_BOUND=Bo1",
        "HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true",
        "HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true",
    ],
    "stages/stage14/14-4eu/result.md": [
        "DIFFUSE_SMALL_QUOTIENT_BRANCH_CLOSED=true",
        "HEAVY_RAY_RADIAL_DIFFUSION_BRANCH_RETAINED=true",
        "WHOLE_MAINLINE_BLOCKED_BY_H=false",
    ],
    "stages/stage14/14-t117/result.md": [
        "WEIGHTED_CORE_DENSITY_FACTORIZATION_EXACT=true",
        "FIXED_U_THREE_MECHANISM_SAVING_TRICHOTOMY_PROVED=true",
        "T_ROUTE_H_NEEDED=false",
    ],
    "stages/stage14/archive/docs/q-research/stage14-q13-summary.md": [
        "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
        "STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false",
    ],
}

for rel, needles in locks.items():
    path = ROOT / rel
    assert path.exists(), rel
    text = path.read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# Finite exact check of the support-relocation inequality.
# For nonnegative weights w_y, inner fiber sizes L_y and accepted counts a_y,
# M=sum w_y*a_y dominates the weighted outer support S=sum_{a_y>0} w_y,
# while H=sum w_y*L_y is at most Lmax*sum w_y.
examples = [
    ([1, 2, 3], [1, 2, 4], [0, 1, 0]),
    ([3, 5, 7, 11], [2, 3, 5, 7], [1, 0, 2, 0]),
    ([2, 4, 8], [8, 4, 2], [0, 0, 1]),
]
for weights, fibers, accepted in examples:
    assert all(0 <= a <= L for a, L in zip(accepted, fibers))
    H = sum(w * L for w, L in zip(weights, fibers))
    M = sum(w * a for w, a in zip(weights, accepted))
    S = sum(w for w, a in zip(weights, accepted) if a > 0)
    W = sum(weights)
    Lmax = max(fibers)
    assert M >= S
    assert H <= Lmax * W
    if H:
        # Exact normalized consequence: S/W <= Lmax*(M/H).
        assert Fraction(S, W) <= Fraction(Lmax * M, H)

res = (ROOT / "stages/stage14/14-Work-boX27/result.md").read_text()
for needle in [
    "STAGE14_WORK_BOX27=COMPLETE_SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_AND_POLYNOMIAL_OUTER_MOBILITY",
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "SUBPOLYNOMIAL_FIBER_SUPPORT_RELOCATION_LEMMA_PROVED=true",
    "COMMON_SUBPOLYNOMIAL_FIBER_EXHAUSTION_PROVED=true",
    "COMMON_FIXED_POWER_SAVING_REQUIRES_POLYNOMIAL_OUTER_MOBILITY=true",
    "HEAVY_RAY_RADIAL_CONCENTRATION_BRANCH_CLOSED=true",
    "FIXED_U_LOCAL_AND_ORIENTATION_DEFICITS_RELOCATE_TO_WEIGHTED_NORM_SUPPORT=true",
    "COMMON_ADAPTER_PROVED=false",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "MAINLINE_H_NEEDED=true",
    "S_ROUTE_H_NEEDED=false",
    "FIXED_U_H_NEEDED=false",
]:
    assert needle in res, needle

print({
    "stage": "14-Work-boX27",
    "support_relocation": True,
    "heavy_fixed_h_closed": True,
    "current_exponent": "1/2",
    "strict_subsqrt": False,
})
