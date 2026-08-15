# Stage19 post-Stage25-50 supersession

STATUS=AUDITED_BACKFLOW_FROM_STAGE25_CHECKPOINT50
HISTORICAL_STAGE19_PASS_REVOKED=false
SOURCE_STAGE=Stage25
SOURCE_CHECKPOINT=50
SOURCE_PR=984
SOURCE_AUDIT=stages/stage25/25-50/audit.md

Stage19's historical final bundle and the later Stage24 logarithmic supersession remain valid historical records. Stage25 checkpoint50 now supplies a strictly stronger current lower interface.

## Current lower

The audited Meskhishvili-family adapter gives

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

Together with the existing whole-family upper,

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

Therefore Stage19 now has a proved positive-power lower bound.

```text
CURRENT_LOWER=N2(B)>>B^(1/4)
CURRENT_LOWER_CLASS=POSITIVE_POWER_ONE_QUARTER
UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_CONSTRUCTION_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_EXPONENT_PROVED=1/4
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
```

## Directional backflow

On the audited Stage25 physical cone the canonical assignment is

\[
(a,b,c)=(B/g,C/g,A/g),
\]

and the guaranteed faces are `ab` and `bc`. Hence

\[
\boxed{N_{2,b}(B)\gg B^{1/4}}.
\]

This is a target-channel statement only; it does not supply the missing Stage25 source-channel denominator adapter.

```text
DIRECTIONAL_B_LOWER=N2,b(B)>>B^(1/4)
GUARANTEED_FACES=ab,bc
SHARED_EDGE=b
```

## Open gate after supersession

The old Stage19 open gate `POSITIVE_POWER_OR_MATCHING_LOWER_BOUND_FOR_STAGE19` is partially closed: positive power is now proved. Remaining quantitative gates include any exponent strictly above `1/4`, a matching half-power lower, a strict whole-family sub-square-root upper, and identification of the true exponent.

```text
HISTORICAL_STAGE19_CLOSEOUT_STILL_VALID=true
POST_STAGE24_LOG_LOWER_SUPERSEDED=true
CURRENT_OPEN_GATE=LOWER_EXPONENT_ABOVE_ONE_QUARTER_OR_MATCHING_HALF_POWER_AND_TRUE_EXPONENT
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
