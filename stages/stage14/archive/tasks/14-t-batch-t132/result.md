# Stage14-t-batch — t132 fixed projective class localization

## Status

`STOPPED_EARLY_ON_RECEIVER_CHANGE`

The batch starts from and publication-rechecks latest merged main

```text
1cce848e748d6b02d7e878c6bd1b326e953bc98c
```

and consumes merged `Stage14-t131` plus merged `Stage14-Work-bsX31`.

`Stage14-t132` performs the requested scalar-norm physical-weight common decomposition directly in the nonnegative cofactor projective classes. For

```text
W_c(n)=#{gamma : N(gamma)=n, [gamma]=c}
```

it obtains

```text
T=sum_c sum_n W_c(n) K_n(c^(-1)[a]^(-1)),
M=sum_c 1/|G| sum_n W_c(n)|P_n|.
```

Because `|G(d)|=B^o(1)`, any fixed-power depletion

```text
T<=B^(-delta)M
```

localizes to one exact class `c_*` satisfying

```text
M_{c_*}=B^(-o(1))M,
T_{c_*}<=B^(-delta/2)M_{c_*}.
```

Thus the moving selected class and the t128--t131 real/nonreal **cofactor-side** split are no longer the minimal receiver. They remain useful only when analyzing the prime progression theorem side. The new minimal receiver is

```text
FixedProjectiveCofactorClassScalarNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion.
```

This is a material receiver change at the first substantive work unit, so the common contract requires early stopping. Completed `tH29` remains the applicable negative theorem boundary; no new `tH` is justified before opening the scalar fixed-class weight `W_{c_*}(n)`.

```text
STAGE14_T_BATCH=STOPPED_EARLY
BATCH_START_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_PUBLICATION_MAIN_SHA=1cce848e748d6b02d7e878c6bd1b326e953bc98c
BATCH_FIRST_STAGE=Stage14-t132
BATCH_LAST_STAGE=Stage14-t132
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=1
BATCH_SUBSTANTIVE_STAGE_COUNT=1
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUFixedProjectiveCofactorClassScalarNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t133
```
