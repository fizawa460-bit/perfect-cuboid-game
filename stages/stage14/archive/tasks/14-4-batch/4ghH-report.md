# Stage14-main-batch report — integrated 4ghH audit

```text
STAGE14_MAIN_BATCH=STOPPED_EARLY
BATCH_START_MAIN_SHA=72e747a7680d01f490ce549b4a8acbf38c368912
BATCH_PUBLICATION_MAIN_SHA=72e747a7680d01f490ce549b4a8acbf38c368912
BATCH_FIRST_STAGE=Stage14-4ghH
BATCH_LAST_STAGE=Stage14-4ghH
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=1
BATCH_SUBSTANTIVE_STAGE_COUNT=1
BATCH_INTEGRATED_H_UNITS=Stage14-4ghH
BATCH_STOP_REASON=unresolved_external_gate
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
MAIN_ROUTE_H_NEEDED=true
MAIN_ROUTE_H_REQUEST=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
MAIN_ROUTE_H_TARGET=stages/stage14/14-4gh/h-target.md
MAIN_ROUTE_H_BLOCKING=true
NEXT=UNRESOLVED_EXTERNAL_GATE:UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```

This batch starts from latest merged `main` and consumes the frozen heavy H
decision in merged `Stage14-4gh` before ordinary `Stage14-4gi`.

The audit derives the exact theorem species.  For

```text
N=t_p*t_q,
f=f_-,
f_+=N/f,
```

the two retained CRT congruences are equivalently

```text
G_-*f^2 == -G_+*N (mod 2U),
G_-*f^2 ==  G_+*N (mod 2V),
```

because the moving factor `f` is coprime to `2UV`.  Hence the target is a
nested quadratic divisor-root first moment over two divisors of the one
primitive product `(uv)^circ`.

The primary-source audit finds no unconditional theorem that supplies the
required estimate uniformly for every principal cell while retaining this
coupling.  Ordinary divisor-AP, almost-all-moduli, binary-form, fixed linear
correlation and single-divisor support theorems do not directly cover the
frozen object.  No saving is inferred from non-applicability.

The early count of one work unit is permitted by the common contract because
the integrated H audit leaves an unresolved external gate.  The batch therefore
does not execute `Stage14-4gi`.

```text
EXACT_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM_DERIVED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=false
DIRECT_TRANSFER_PROVED=false
FIRST_MOMENT_FULL_EXPONENT_PROVED=false
FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false
PARAMETER_DICHOTOMY_PROVED=false
STAGE14_4GI_EXECUTED=false
PUBLICATION_MAIN_RECHECK_COMPLETE=true
NEW_MERGED_CONSUMER_AFTER_BATCH_START=false
```
