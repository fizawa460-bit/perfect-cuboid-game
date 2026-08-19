# StructureRadar parallel batch 37A — SR-STR-169 quadratic-form reduction

BATCH_ID=SR-BATCH-PARALLEL-37A-169-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=A
STRUCTURE=SR-STR-169
MODE=ONE_PR_FOUR_LANES_DEEP_ATTACK
BASE_MAIN=9f70ff9c37c12981e197f0c213795fc7a906fc35
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 36A. There the primitive completed inverse-frequency operator was converted exactly to its same-`H_phys^MAIN` Gram matrix `G_d(b,b')`, and Schur supplied the sufficient absolute row-sum target.

## 1. The absolute Gram-row target is stronger than necessary

For the same operator `T_d` and the same original batch34/35A coefficient vector, exact Hilbert-space duality gives

```text
||T_d||_{2->2}^2
 = ||T_d^*T_d||_{2->2}
 = sup_{||c||_2=1}
     sum_{b,b': d|b,d|b'} c_b conj(c_{b'}) G_d(b,b').
```

Because `G_d=T_d^*T_d` is positive semidefinite, this quadratic-form identity is exact. The 36A Schur bound

```text
sup_b sum_{b'} |G_d(b,b')|
```

is only one sufficient way to control the operator norm; it is not a mandatory theorem target. In particular, a spectral large-sieve or Kuznetsov inequality may control the full quadratic form without supplying pairwise absolute Gram-row decay.

No new coefficient normalization is introduced. The admissible `c_b` remain supported on the original `d|b` stratum and are charged to the original-q Fourier `L2` energy from batches34/35A.

## 2. Smaller live theorem target

The required analytic input can therefore be weakened to

```text
FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencySameMeasureLargeSieveQuadraticFormDeficit
```

A sufficient form is: uniformly on every retained MAIN wall packet and gcd stratum, for every coefficient vector `c` supported on `d|b`, prove

```text
sum_{b,b'} c_b conj(c_{b'}) G_d(b,b')
 <= B^{-2 delta+o(1)} E_packet ||c||_2^2
```

for one fixed `delta>0`, with `E_packet` the exact batch34/35A kernel-energy scale. The correlated modulus, common-parent allocation, gcd-descent factor, primitive/chamber/parity masks, and frozen/summed quantifier order must remain unchanged.

This formulation does not assume the Gram diagonal is separately small and does not require absolute off-diagonal decay. Any successful quadratic-form theorem must of course control the positive diagonal contribution implicitly at the target scale.

## 3. Consequence for external search

Dong--Robles--Zeindler/Wright/Kuznetsov/large-sieve inputs should now be tested against this quadratic-form receiver rather than the stronger Schur row-sum receiver. Average-modulus or different-measure estimates remain unusable without an exact transfer back to `H_phys^MAIN`.

No published theorem applicability is claimed in this batch.

## 4. Firewalls

```text
TTSTAR_GRAM_REDUCTION_REUSED=true
SCHUR_ABSOLUTE_ROW_BOUND_MANDATORY=false
EXACT_GRAM_QUADRATIC_FORM_RECEIVER=PROVED
FRESH_DESCENDED_PARSEVAL_IDENTITY_CLAIMED=false
GCD_DESCENT_FACTOR_RETAINED=true
GRAM_DIAGONAL_AUTOMATICALLY_SMALL=false
PUBLISHED_LARGE_SIEVE_APPLICABILITY_PROVED=false
FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencySameMeasureLargeSieveQuadraticFormDeficit
SR_STR_169_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
NOVELTY_BY_SEARCH_ABSENCE=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```

WORK_DELEGATION_RECOMMENDED=true
WORK_TARGET=SR-STR-169 / MAINWallPrimitiveInverseFrequencySameMeasureLargeSieveQuadraticFormDeficit
