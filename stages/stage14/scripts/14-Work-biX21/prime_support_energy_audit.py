#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path

# Exact finite-support concentration inequalities.
checks = 0
for masses in (
    [1, 2, 3],
    [0, 5, 0, 7],
    [4, 4, 4, 4],
    [1, 0, 0, 0, 9],
):
    I = sum(masses)
    K = len(masses)
    E = sum(m*m for m in masses)
    assert max(masses) * K >= I
    assert I*I <= K*E
    checks += 1

# Normalized fixed-U version: mean-square dominates square of the mean.
for vals in (
    [Fraction(1,4), Fraction(1,2), Fraction(3,4)],
    [Fraction(0,1), Fraction(1,1)],
    [Fraction(1,3)] * 5,
):
    n = len(vals)
    mean = sum(vals, Fraction(0,1)) / n
    energy = sum(v*v for v in vals) / n
    assert energy >= mean*mean
    assert max(vals) >= mean
    checks += 1

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4du/result.md': 'CANDIDATE_FIRST_SECOND_MOMENT_DICHOTOMY_PROVED=true',
    'stages/stage14/14-s7-62/result.md': 'RANGE_STABLE_CANDIDATE_PRIME_IMAGE_SIZE=Bo1',
    'stages/stage14/14-t102/result.md': 'FIXED_U_PRIME_MOVER_DENSITY_ENERGY_LEMMA_PROVED=true',
    'stages/stage14/14-Work-bhX20/result.md': 'COMMON_STABILIZER_MOVER_DICHOTOMY_PROVED=true',
}
for rel, needle in locks.items():
    text = (ROOT / rel).read_text()
    assert needle in text, (rel, needle)

res = (ROOT / 'stages/stage14/14-Work-biX21/result.md').read_text()
for needle in (
    'STAGE14_WORK_BIX21=COMPLETE_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_ENERGY_UNIFICATION',
    'COMMON_SUBPOLYNOMIAL_PRIME_SUPPORT_CONCENTRATION_LEMMA_PROVED=true',
    'GLOBAL_RANGE_STABLE_HEAVY_MOVER_PRIME_PROVED=true',
    'GLOBAL_COLLISION_PRIME_CAN_BE_FROZEN_ON_SATURATING_ARITHMETIC_SUBFAMILY=true',
    'HEAVY_PRIME_AND_ENERGY_DOUBLE_CHARGE_FORBIDDEN=true',
    'COMMON_ARITHMETIC_COLLISION_ADAPTER_PROVED=false',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'TH28_NEEDED=false',
):
    assert needle in res, needle

print({'stage':'14-Work-biX21','checks':checks,'status':'PASS','current_exponent':'1/2'})
