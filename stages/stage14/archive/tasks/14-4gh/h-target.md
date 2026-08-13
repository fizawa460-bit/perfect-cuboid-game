# Stage14-4ghH immutable theorem target

```text
H_STAGE=Stage14-4ghH
SOURCE_STAGE=Stage14-4gh
SOURCE_SNAPSHOT_SHA=79393f83b1110b7e66b41a23c51596a10bc6c7ef
BATCH_START_MAIN_SHA=72e747a7680d01f490ce549b4a8acbf38c368912
TARGET_FREEZES_AT_DISPATCH=true
REQUESTED_OBJECT=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
```

The audit uses the merged `Stage14-4gh` receiver and no later main-line
conclusion.  On one fixed-`E` principal primitive rectangle retain

```text
R_prim={(u,v):u in D,v in V,gcd(u,v)=1},
#R_prim=B^(kappa+o(1)),
m^circ=(u*v)^circ,
t_p|m^circ,
t_q|m^circ,
f_-*f_+=t_p*t_q.
```

The frozen coefficient-prime support is `K_*`.  The moving factors are coprime
to `K_*`, while the subpolynomial core labels `G_-,G_+` retain all valuations at
coefficient primes.  Preserve exactly

```text
G_+*f_+ + G_-*f_- == 0 (mod 2U),
G_+*f_+ - G_-*f_- == 0 (mod 2V),
```

together with primitive-pair measure, positivity, parity, endpoint-small
filters and the charged-once quantifier order inside `Omega_rec`.

## Question

Audit whether an existing unconditional theorem, or a complete direct transfer
from such a theorem, proves uniformly on every relevant principal cell one of

```text
S_1=sum_{(u,v) in R_prim} #Omega_rec(u,v)
    = B^(kappa+o(1)),

S_1 <= B^(kappa-eta+o(1)) for some fixed eta>0,

or a rigorous parameter-dependent dichotomy between these outcomes.
```

The audit may use merged q17 only as a source list.  It must independently
check theorem hypotheses after the exact 4gg/4gh normalization.

```text
DO_NOT_USE_RESIDUAL_R_POST_MASK=true
DO_NOT_CROSS_PROMOTE_FIXED_U_PRIME_OCCUPANCY=true
DO_NOT_DROP_PRIMITIVE_GCD_OR_ENDPOINT_FILTERS=true
DO_NOT_REPLACE_EVERY_PRINCIPAL_CELL_BY_ALMOST_ALL_MODULI=true
DO_NOT_REPLACE_TWO_LEVEL_CRT_BY_ONE_UNCOUPLED_DIVISOR_AP=true
DO_NOT_INFER_SAVING_FROM_ABSENCE_OF_A_THEOREM=true
DO_NOT_REQUIRE_A_SECOND_MOMENT_FOR_SUPPORT_TRANSFER=true
```

Required output:

```text
STAGE14_4GHH=COMPLETE|INCOMPLETE
SOURCE_SNAPSHOT_SHA=<immutable 4gh merge>
TARGET_FILE=stages/stage14/14-4gh/h-target.md
TARGET_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
EXACT_TWO_CRT_CONGRUENCES_RETAINED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=true|false
DIRECT_TRANSFER_PROVED=true|false
FIRST_MOMENT_FULL_EXPONENT_PROVED=true|false
FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=true|false
PARAMETER_DICHOTOMY_PROVED=true|false
MAINLINE_BLOCKED_BY_H=true|false
NEXT=<Stage14-4gi or exact unresolved external gate>
```
