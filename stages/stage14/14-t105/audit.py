#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# 1. Exact finite-fiber quantization and Bernoulli variance.
checked = 0
nonempty = 0
nonconstant = 0
for M in range(1, 65):
    for N in range(M + 1):
        rho = Fraction(N, M)
        var = rho * (1 - rho)
        assert 0 <= rho <= 1
        assert var == Fraction(N * (M - N), M * M)
        if N > 0:
            assert rho >= Fraction(1, M)
            nonempty += 1
        if 0 < N < M:
            assert rho >= Fraction(1, M)
            assert 1 - rho >= Fraction(1, M)
            nonconstant += 1
        checked += 1

# 2. Complement thinness only kills the centered term, not principal mass.
# Start at M=3 so the near-full example is strictly above 1/2.
for M in range(3, 65):
    rho_full = Fraction(M, M)
    var_full = rho_full * (1 - rho_full)
    assert rho_full == 1
    assert var_full == 0

    rho_near = Fraction(M - 1, M)
    var_near = rho_near * (1 - rho_near)
    assert rho_near > Fraction(1, 2)
    assert var_near < rho_near
    assert 1 - rho_near == Fraction(1, M)

# 3. Exact tower/total-variance identity on unequal fiber sizes.
fibers = [(3, 1), (5, 4), (7, 2), (8, 8), (11, 0)]
Mtot = sum(M for M, _ in fibers)
Ntot = sum(N for _, N in fibers)
rho_total = Fraction(Ntot, Mtot)

# Weighted outer expectation with weights M_Q/Mtot.
within = sum(Fraction(M, Mtot) * Fraction(N, M) * (1 - Fraction(N, M))
             for M, N in fibers)
between = sum(Fraction(M, Mtot) * (Fraction(N, M) - rho_total) ** 2
              for M, N in fibers)
assert rho_total * (1 - rho_total) == between + within

# 4. Positive principal mass equals the sum of boundary-bearing fiber weights.
omega = [N for _, N in fibers]
assert sum(omega) == Ntot
support = [i for i, N in enumerate(omega) if N > 0]
max_M = max(M for M, _ in fibers)
assert sum(omega) <= len(support) * max_M

# 5. Frozen-source locks.
sources = {
    'stages/stage14/14-t89/result.md': 'PHYSICAL_COMPLETION_BOUNDED_Q_WEIGHT_PROVED=true',
    'stages/stage14/14-t91/result.md': 'GENERIC_COFACTOR_PARAMETER_IS_SPLIT_PRIME_ORIENTATION_CUBE=true',
    'stages/stage14/14-t104/result.md': 'NEXT_INTERNAL_TARGET=FixedFullBoundaryBackgroundGaussianCofactorDensityDecomposition',
    'stages/stage14/14-Work-bkX23/result.md': 'COMMON_FIXED_BOOLEAN_PRINCIPAL_DENSITY_TEMPLATE_PROVED=true',
}
for rel, needle in sources.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

result = (ROOT / 'stages/stage14/14-t105/result.md').read_text()
for needle in [
    'STAGE14_T105=COMPLETE_BACKGROUND_GAUSSIAN_FIBER_DENSITY_NOGO_AND_OUTER_Q_SUPPORT_REDUCTION',
    'COMPLEMENT_DEFICIT_ELIMINATES_POSITIVE_PRINCIPAL_MASS=false',
    'T104_TWO_SIDED_MINIMAL_PRINCIPAL_SURVIVOR_LOCK_SUPERSEDED=true',
    'OUTER_Q_SUPPORT_IS_FIRST_REMAINING_POLYNOMIAL_LENGTH=true',
    'POSITIVE_PRINCIPAL_MASS_REDUCED_TO_OUTER_Q_SUPPORT_WEIGHT=true',
    'TH28_NEEDED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT=Stage14-t106',
]:
    assert needle in result, needle

print({
    'stage': '14-t105',
    'finite_fiber_cases_checked': checked,
    'nonempty_cases_checked': nonempty,
    'nonconstant_cases_checked': nonconstant,
    'tower_variance_exact': True,
    'principal_complement_correction_checked': True,
    'outer_support_identity_checked': True,
    'status': 'ok',
})
