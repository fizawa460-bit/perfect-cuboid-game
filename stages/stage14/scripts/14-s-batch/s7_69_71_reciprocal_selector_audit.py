#!/usr/bin/env python3
from pathlib import Path
from math import gcd

ROOT = Path(__file__).resolve().parents[4]

locks = {
    'stages/stage14/14-s7-68/result.md': [
        'CANONICAL_ALLOCATION_RECIPROCAL_DENSITY_CHAIN_EXACT=true',
        'NEXT=Stage14-s7-69',
    ],
    'stages/stage14/14-Work-blX24/result.md': [
        'CURRENT_GLOBAL_RECEIVER=PrimitiveCoprimeBinaryFormsCanonicalBalancedIntegerGaussianAllocationDensity_x_ConditionalReciprocalPostColumnCompletionDensity',
        'SUBPOLYNOMIAL_INNER_FIBERS_NOT_INDEPENDENT_SAVING_LENGTHS=true',
    ],
    'stages/stage14/14-s7-46/result.md': [
        'MIXED_ROOT_TO_SECOND_RECIPROCAL_FIBER_MULTIPLICITY=Bo1',
    ],
}
for rel, needles in locks.items():
    text=(ROOT/rel).read_text()
    for needle in needles:
        assert needle in text, (rel, needle)

# First reciprocal identity: signed-square difference is 4DA.
for D,A in [(13,5),(25,7),(41,9),(61,11)]:
    assert (D+A)**2-(D-A)**2 == 4*D*A

# Primitive Gaussian norm divisibility forces -1 to be a square modulo odd primes.
for p in [5,13,17,29,37,41]:
    roots=[x for x in range(1,p) if (x*x+1)%p==0]
    assert len(roots)==2
    r=roots[0]
    for y in range(1,p):
        if gcd(y,p)!=1: continue
        x=(r*y)%p
        assert (x*x+y*y)%p==0

# Conversely no roots for representative 3 mod 4 primes.
for p in [3,7,11,19,23,31,43]:
    assert all((x*x+1)%p for x in range(1,p))

for stage, needles in {
    '69':[
        'FIRST_RECIPROCAL_EQUATION_TAUTOLOGICAL_AFTER_CANONICAL_ALLOCATION=true',
        'RECEIVER_MATERIALLY_CHANGED=false',
        'NEXT=Stage14-s7-70',
    ],
    '70':[
        'SECOND_RECIPROCAL_SELECTOR_IS_GAUSSIAN_NORM_DIVISIBILITY=true',
        'SECOND_RECIPROCAL_SELECTOR_TAUTOLOGICAL_AFTER_ALLOCATION=false',
        'NEXT=Stage14-s7-71',
    ],
    '71':[
        'PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false',
        'S7_71_NEW_AUXILIARY_H_NEEDED=true',
        'S7_71_AUXILIARY_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity',
        'NEXT=Stage14-sH71',
    ],
}.items():
    text=(ROOT/f'stages/stage14/14-s7-{stage}/result.md').read_text()
    for needle in needles:
        assert needle in text, (stage, needle)

print({
    'batch':'s7-69..71',
    'first_reciprocal_identity':'checked',
    'gaussian_root_examples':'checked',
    'stop_reason':'new_external_lemma_needed',
    'H':'Stage14-sH71',
    'current_exponent':'1/2',
})
