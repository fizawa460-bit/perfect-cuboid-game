# Stage19 post-Stage25 supersession — current receiver

STATUS=SUBMITTED_BACKFLOW_R008A_PENDING_FRESH_AUDIT
HISTORICAL_STAGE19_PASS_REVOKED=false
ORIGINAL_SOURCE_STAGE=Stage25
ORIGINAL_SOURCE_CHECKPOINT=50
ORIGINAL_SOURCE_PR=984
LATEST_SOURCE_ROUTE=Stage25-um-r008a
LATEST_PARENT_TASK=Stage25-u24-r002a
LATEST_SOURCE_PR=1003
LATEST_SOURCE_MERGE_COMMIT=1d88e8e3254a383620e221df8a1a1039ebeabcd4
LATEST_SOURCE_AUDIT=stages/stage25/25-reentry-20/audit.md

Stage19's historical final bundle, the Stage24 logarithmic supersession, and the Stage25 checkpoint50 quarter-power backflow remain valid historical records. Phase20 of Stage25-reentry has now proved a stronger **directional** current interface without changing the global exponent.

## Current global lower

The audited Meskhishvili-family adapter still gives

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

Together with the existing whole-family upper,

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

No global exponent upgrade occurs in r008a.

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
GLOBAL_N2_EXPONENT_UPGRADED=false
```

## Current directional backflow

The hostile phase20 audit accepted three canonical shared-edge quarter-power families:

- R501 on `9/2<t<5` has raw shared edge `C` as the strict smallest edge, hence canonical shared edge `a`;
- audited R501 on `7/2<t<4` gives canonical shared edge `b`;
- audited R502 on `7/2<t<4` gives canonical shared edge `c`.

Therefore

\[
\boxed{N_{2,a}(B)\gg_a B^{1/4}},\qquad
\boxed{N_{2,b}(B)\gg_b B^{1/4}},\qquad
\boxed{N_{2,c}(B)\gg_c B^{1/4}}.
\]

The implied constants may depend on the fixed direction. These are physical Stage19 directional target-channel statements under the same primitive/canonical `R<=B` contract.

```text
N2,a(B)>>B^(1/4)
N2,b(B)>>B^(1/4)
N2,c(B)>>B^(1/4)
ALL_DIRECTIONAL_QUARTER_POWER_LOWER_PROVED=true
DIRECTIONAL_A_SOURCE=R501_CONE_9/2<t<5
DIRECTIONAL_B_SOURCE=R501_CONE_7/2<t<4
DIRECTIONAL_C_SOURCE=R502_CONE_7/2<t<4
GLOBAL_N2_EXPONENT_UPGRADED=false
```

## Open gate after directional supersession

Positive power is proved globally and in every canonical shared-edge chamber. Remaining quantitative gates include any exponent strictly above `1/4`, a matching half-power lower, a strict whole-family sub-square-root upper, moving-family/growing-modulus uniformity, and identification of the true exponent.

```text
HISTORICAL_STAGE19_CLOSEOUT_STILL_VALID=true
POST_STAGE24_LOG_LOWER_SUPERSEDED=true
CURRENT_OPEN_GATE=LOWER_EXPONENT_ABOVE_ONE_QUARTER_OR_MATCHING_HALF_POWER_AND_TRUE_EXPONENT
BACKFLOW_ROUTE=Stage25-um-r008a
BACKFLOW_AUDIT_STATUS=PENDING
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
