# StructureRadar parallel batch 35B — SR-STR-170 weighted square-dilate unfolding

BATCH_ID=SR-BATCH-PARALLEL-35B-170-R01
PHASE=EXTERNAL_GATE_CLOSURE
PARALLEL_LANE=B
STRUCTURE=SR-STR-170
MODE=PARALLEL_DEEP_ATTACK
BASE_MAIN=4d87d7f5461ee019229b31cd5f8c0947e13dbc0c
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE

This lane resumes from audited/merged 33B. There the reciprocal squareclass condition was reduced exactly to `a^2 | M/J` with `a` in the square-root physical window, while the complementary cofactor/canonical data remained attached to the chosen witness.

## 1. Exact nonnegative incidence unfolding with witness-dependent weights

Let `mu(M)>=0` denote the nonnegative base packet mass after the data independent of the square-divisor witness are frozen. Let `A(M,a)` denote the exact remaining admissibility/physical-mask factor for witness `a`; for a Boolean packet it is an indicator, and more generally it is the retained nonnegative witness weight. Let `I_A` be the exact allowed interval for `a` obtained from `L=J a^2`.

Pointwise,

```text
1_{exists a in I_A : J a^2 | M and A(M,a)>0}
 <= sum_{a in I_A} 1_{J a^2 | M} A(M,a)
```

in the indicator case, with the analogous union/first-moment domination for nonnegative witness weights. Multiplying by `mu(M)` and summing gives

```text
sum_M mu(M) * physical_squareclass_event(M)
 <= sum_{a in I_A} sum_{k>=1}
      mu(J a^2 k) A(J a^2 k,a).
```

Define the exact witness-indexed dilate weight

```text
w_a(k) = mu(J a^2 k) A(J a^2 k,a).
```

Then the right-hand side is `sum_a sum_k w_a(k)`. The complementary cofactor is exactly `k=M/(J a^2)`, so all cofactor/canonical/reverse masks remain attached to the same witness rather than being silently absorbed into a single function of `M` independent of `a`.

No ordinary-divisor comparison, Ford theorem, density equivalence, or change of measure is needed for this reduction.

## 2. Consequence for the theorem target

The old restart point `PhysicalSquareDivisorWindowOrdinaryShadowMeasureCompatibility` is sufficient but stronger than necessary. For the upper lane it is enough to prove a fixed-power deficit for the actual witness-weighted square-dilate incidence.

Thus the smaller missing lemma is

```text
FIRST_MISSING_LEMMA=PhysicalSquareDilateWitnessWeightedMassDeficit
```

A sufficient form is:

> Uniformly on every retained packet, prove
> `sum_{a in I_A} sum_k w_a(k) <= B^{-delta+o(1)} H_packet`
> for some fixed `delta>0`, where `H_packet` is the original charged packet mass, with the actual physical `a`-window, endpoint headroom, witness-dependent cofactor/canonical masks, and packet quantifiers preserved. Packet summation may lose only `B^o(1)`.

Any published divisor-window theorem that implies this bound on the exact witness-indexed physical weight remains usable, but an ordinary-divisor support theorem is no longer logically required as an intermediate target.

## 3. Why this is narrower

The right-hand side is a concrete square-dilation first moment on the exact physical witness weight. It asks only for mass on square dilates `J a^2 k`, not for a theorem about all ordinary divisors of `M`. The audit repair is important: witness-dependent masks are not replaced by a fictitious single `w(M)`.

No fixed-power saving is claimed here; the inequality is only a normalization of the unresolved weighted mass estimate.

## 4. Firewalls

```text
SQUARECLASS_TO_SQUARE_DIVISOR_PARAMETERIZATION_REUSED=true
WEIGHTED_SQUARE_DILATE_UNFOLDING=PROVED
WITNESS_DEPENDENT_MASKS_RETAINED=true
ORDINARY_DIVISOR_SHADOW_THEOREM_REQUIRED=false
PHYSICAL_SQUARE_DILATE_DEFICIT_PROVED=false
FIRST_MISSING_LEMMA=PhysicalSquareDilateWitnessWeightedMassDeficit
SR_STR_170_STATUS=EXTERNAL_GATE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PERFECT_CUBOID_EXISTENCE_NONEXISTENCE_CLAIM=false
PROGRESS_LEDGER_DEFERRED_TO_PARALLEL_INTEGRATION=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
