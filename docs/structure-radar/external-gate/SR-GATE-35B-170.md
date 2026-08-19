# StructureRadar parallel batch 35B — SR-STR-170 weighted square-dilate unfolding

BATCH_ID=SR-BATCH-PARALLEL-35B-170-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=B
STRUCTURE=SR-STR-170
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=4d87d7f5461ee019229b31cd5f8c0947e13dbc0c
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 33B. There the reciprocal squareclass condition was reduced exactly to `a^2 | M/J` with `a` in the square-root physical window, and the ordinary-divisor shadow was retained only as a one-sided upper bound.

## 1. Exact nonnegative incidence unfolding

Let `w(M)>=0` be the exact charged physical packet weight after all frozen data and complementary cofactor/canonical masks are retained. Let `I_A` be the exact allowed interval for `a` obtained from `L=J a^2`.

Pointwise,

```text
1_{exists a in I_A : a^2 | M/J}
 <= sum_{a in I_A} 1_{J a^2 | M}.
```

Multiplying by `w(M)` and summing gives the exact one-sided first-moment bound

```text
sum_M w(M) 1_{exists a in I_A : a^2 | M/J}
 <= sum_{a in I_A} sum_{k>=1} w(J a^2 k).
```

No ordinary-divisor comparison, Ford theorem, density equivalence, or change of measure is needed for this reduction. The complementary cofactor is exactly `k=M/(J a^2)`, so the physical cofactor/canonical masks can be kept inside `w(J a^2 k)` rather than removed.

## 2. Consequence for the theorem target

The old restart point `PhysicalSquareDivisorWindowOrdinaryShadowMeasureCompatibility` is sufficient but stronger than necessary. For the upper lane it is enough to prove a fixed-power deficit for the actual weighted square-dilate incidence on the right-hand side.

Thus the smaller missing lemma is

```text
FIRST_MISSING_LEMMA=PhysicalSquareDilateWeightedMassDeficit
```

A sufficient form is:

> Uniformly on every retained fixed-E/fixed-ray packet, prove
> `sum_{a in I_A} sum_k w(J a^2 k) <= B^{-delta+o(1)} sum_M w(M)`
> for some fixed `delta>0`, with the actual physical `a`-window, endpoint headroom, cofactor masks and packet quantifiers preserved. Packet summation may lose only `B^o(1)`.

Any published divisor-window theorem that implies this bound on the same weight remains usable, but an ordinary-divisor support theorem is no longer logically required as an intermediate target.

## 3. Why this is narrower

The right-hand side is a concrete dilation operator on the exact physical weight. It asks only for mass on square dilates `J a^2 k`, not for a theorem about all ordinary divisors of `M`. This avoids paying for the much larger ordinary-divisor shadow and keeps the squareclass geometry visible.

No fixed-power saving is claimed here; the inequality is only a normalization of the unresolved weighted mass estimate.

## 4. Firewalls

```text
SQUARECLASS_TO_SQUARE_DIVISOR_PARAMETERIZATION_REUSED=true
WEIGHTED_SQUARE_DILATE_UNFOLDING=PROVED
ORDINARY_DIVISOR_SHADOW_THEOREM_REQUIRED=false
PHYSICAL_SQUARE_DILATE_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalSquareDilateWeightedMassDeficit
SR_STR_170_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
