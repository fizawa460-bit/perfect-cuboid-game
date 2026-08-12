# Stage14-main-batch report — 4gf through 4gh

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=007ff032d7f757035029a04d6065b605c8a65ef0
BATCH_PUBLICATION_MAIN_SHA=007ff032d7f757035029a04d6065b605c8a65ef0
BATCH_FIRST_STAGE=Stage14-4gf
BATCH_LAST_STAGE=Stage14-4gh
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
MAIN_ROUTE_H_NEEDED=true
MAIN_ROUTE_H_REQUEST=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
MAIN_ROUTE_H_TARGET=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
MAIN_ROUTE_H_BLOCKING=false
NEW_HEAVY_MAIN_H_NEEDED=true
NEXT=Stage14-4gi
```

This batch starts from merged `Stage14-4ge` and consumes merged `Stage14-Work-bzX38/q17`, merged `s7-111..113`, merged `t147..149` only for no-cross-promotion boundaries, plus the latest operational auto-pilot commits. The latter do not change the mathematical Stage14 receiver.

## Stage14-4gf — direct construction test

The q17 explicit construction handoff is executed first.

On the reciprocal system

```text
p*c=A_x*m,
q*d=A_y*m,
F_-*F_+=C0*p*q,
F_+ + F_- == 0 (mod 2U),
F_+ - F_- == 0 (mod 2V),
```

one scale-compatible homogeneous seed `(P,Q,G_-,G_+)` produces for every pair in the compatible principal subcell

```text
p=P*m,
q=Q*m,
F_-=G_-*m,
F_+=G_+*m.
```

Hence a seeded packet has full reciprocal-support exponent and

```text
delta_rec=0.
```

The number of candidate fixed seeds is `B^o(1)`. Failure of this sufficient construction is **not** reinterpreted as a saving; seedless witnesses may allocate moving prime powers nontrivially.

```text
Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST=COMPLETE
SEEDED_RECIPROCAL_DEFICIT_FIXED_POWER=0
SEEDLESS_IMPLIES_RECIPROCAL_SPARSITY=false
```

## Stage14-4gg — exact moving-prime normal form

Let `K_*` contain every prime appearing in the frozen reciprocal coefficients. Removing those primes from a seedless witness gives exactly

```text
t_p | m^circ,
t_q | m^circ,
f_-*f_+=t_p*t_q,
```

while all fixed-prime/core valuations remain inside already-bounded witness labels. The CRT conditions stay exact:

```text
G_+*f_+ + G_-*f_- == 0 (mod 2U),
G_+*f_+ - G_-*f_- == 0 (mod 2V).
```

Thus the only genuinely moving reciprocal arithmetic is a K-free divisor-allocation CRT incidence. The homogeneous seed is its diagonal full-density subcase.

```text
FIRST_LAYER_KFREE_MOVING_DIVISORS_EXACT=true
SECOND_LAYER_KFREE_FACTOR_ALLOCATION_EXACT=true
FIXED_UV_CRT_PRESERVED_EXACTLY=true
```

## Stage14-4gh — one first moment is enough

For

```text
N_rec(u,v)=#Omega_rec(u,v),
```

merged 4gd gives `N_rec<=B^o(1)`. Therefore

```text
#T_rec <= sum N_rec <= B^o(1)*#T_rec.
```

The reciprocal support and its first moment have the same fixed-power exponent. Hence q17's proposed second moment is unnecessary for support transfer:

```text
Q17_SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false
Q17_FIRST_MOMENT_ALONE_CONTROLS_SUPPORT_AT_B_POWER_SCALE=true.
```

The seedless reciprocal target is now theorem-shaped as one nonnegative K-free divisor-allocation CRT first moment. A full-exponent first-moment lower bound proves reciprocal deficit zero; a fixed-power first-moment upper bound proves a reciprocal support saving of the same exponent.

This changes the fixed-E two-sided receiver materially to

```text
FixedComplementaryDilationTwoSidedPrincipalRectangular
KFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficit
VersusConditionalRootCanonicalPostColumnCompletionDeficit
WithCapacityHeadroomKappaMinusMu.
```

## New heavy H boundary

The stable clean-room theorem target is frozen as

```text
FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit.
```

It must retain the primitive rectangle, the exact two CRT congruences, bare parity/positivity/endpoint filters, K-free divisor allocations and charged-once quantifier order. It must not absorb the residual `R_post` mask or fixed-U Gaussian-prime occupancy.

The q17 literature leads are advisory only. No direct theorem is claimed in this batch.

The batch stops after three substantive stages because 4gh materially changes the theorem interface. Under the common batch contract, the next batch should consume this frozen H decision before ordinary `Stage14-4gi`; an integrated H that leaves an unresolved external gate is then a legal stop condition.

Existing non-heavy mainline H targets remain pending and are not consumed or multiplied with this heavy target.

```text
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
PUBLICATION_MAIN_RECHECK_COMPLETE=false
```