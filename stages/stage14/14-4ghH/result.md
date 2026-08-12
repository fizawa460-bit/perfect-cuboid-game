# Stage14-4ghH — K-free two-level CRT first-moment theorem audit

## Frozen source and verdict

```text
H_STAGE=Stage14-4ghH
AUDITED_THROUGH=Stage14-4gh
SOURCE_SNAPSHOT_SHA=79393f83b1110b7e66b41a23c51596a10bc6c7ef
TARGET_FILE=stages/stage14/14-4gh/h-target.md
REQUESTED_OBJECT=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
TARGET_FROZEN=true
SOURCE_SNAPSHOT_FROZEN=true
```

This clean-room audit retains the exact bare reciprocal selector and does not
use the residual `R_post` mask or any later `Stage14-4gi` conclusion.

No audited unconditional theorem directly proves a full-exponent asymptotic, a
fixed-power upper deficit, or a uniform parameter dichotomy for the frozen first
moment on every principal cell.

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
DIRECT_TRANSFER_PROVED=false
FIRST_MOMENT_FULL_EXPONENT_PROVED=false
FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false
PARAMETER_DICHOTOMY_PROVED=false
```

This is an applicability certificate.  It is not a theorem that the requested
first-moment result is false.

## 1. Exact quadratic divisor-root normal form

For one fixed `K_*`-supported core label, put

```text
N=t_p*t_q,
f=f_-,
f_+=N/f.
```

Merged 4gg gives

```text
t_p|m^circ,
t_q|m^circ,
f|N,
gcd(f*N/f,2UV)=1.
```

Since `f` is a unit modulo `2UV`, multiplying the two exact CRT congruences by
`f` is reversible.  They are equivalent to

```text
G_-*f^2 == -G_+*N (mod 2U),
G_-*f^2 ==  G_+*N (mod 2V).                       (1)
```

Thus the moving first moment is an iterated nonnegative divisor sum

```text
sum_{(u,v) in R_prim}
  sum_{t_p|m^circ}
  sum_{t_q|m^circ}
  sum_{f|t_p*t_q} 1_{the two quadratic root congruences (1)}
```

with the frozen core, parity, positivity and endpoint filters.  It is not one
ordinary divisor function in one fixed residue class.  The residue target in
(1) moves with `N=t_p*t_q`, and the same `N` is assembled from two divisors of
the single product `m^circ=(uv)^circ`.

```text
EXACT_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM_DERIVED=true
QUADRATIC_ROOT_RESIDUE_MOVES_WITH_N=true
NESTED_TWO_DIVISORS_OF_ONE_PRIMITIVE_PRODUCT_RETAINED=true
EXACT_TWO_CRT_CONGRUENCES_RETAINED=true
```

## 2. Divisor functions in arithmetic progressions

Grimmelt--Merikoski prove equidistribution for the ordinary divisor function in
arithmetic progressions to moduli with two small factors, including an almost-all
moduli application.  Irving treats the ordinary divisor function for suitably
factorable smooth moduli.  Nguyen treats generalized divisor functions in
progressions with modulus averaging, and a separate modified shifted-convolution
second moment.

None of these statements counts the nested tuple `(t_p,t_q,f)` above while
preserving both quadratic root conditions, the primitive `(u,v)` rectangle and
uniformity for every charged principal cell.  In particular, almost-all-moduli
or averaged-modulus conclusions cannot be substituted for the frozen uniform
quantifier.

The 2025 Zhong--Zhang prime-power-modulus result is also a one-progression
ordinary-divisor asymptotic.  The frozen modulus is not restricted to one prime
power, and the moving two-level allocation is unchanged.

```text
GRIMMELT_MERIKOSKI_DIRECTLY_APPLICABLE=false
IRVING_DIRECTLY_APPLICABLE=false
NGUYEN_I_II_DIRECTLY_APPLICABLE=false
ZHONG_ZHANG_PRIME_POWER_DIRECTLY_APPLICABLE=false
EVERY_PRINCIPAL_CELL_UNIFORMITY_SUPPLIED=false
```

## 3. Binary-form and linear-correlation routes

Frei--Sofos give asymptotics and lower bounds for specified generalized divisor
sums over binary-form values.  Bettin treats products of divisor functions under
a fixed nontrivial linear relation.  The exact Stage14 weight has neither been
identified with a covered binary-form convolution nor converted into a finite
sum of Bettin-type fixed linear correlations.  Its active relation remains
multiplicative through `N=t_p*t_q` and quadratic through (1).

```text
FREI_SOFOS_COVERED_BINARY_FORM_WEIGHT_DERIVED=false
BETTIN_FIXED_LINEAR_CORRELATION_ENCODING_DERIVED=false
BINARY_FORM_OR_LINEAR_CORRELATION_DIRECT_TRANSFER_PROVED=false
```

## 4. Support templates do not settle the first moment

Ford's divisor-in-an-interval theorem is a genuine support theorem, but the
frozen event is not the existence of one divisor in an interval.  It requires
two divisors of `m^circ`, a divisor of their product, and the simultaneous
quadratic root conditions (1).  Dropping that coupling would enlarge the set and
would not prove either requested direction for `S_1`.

The first moment already has the same fixed-power exponent as reciprocal support
by merged 4gh.  A new second moment is therefore not the missing logical step.

```text
FORD_SINGLE_DIVISOR_SUPPORT_DIRECTLY_APPLICABLE=false
SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false
```

## 5. Minimal unresolved external gate

The clean-room H audit is complete, but its requested theorem remains external.
The exact missing object is

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```

meaning an unconditional every-principal-cell estimate for the iterated sum in
Section 1, with all frozen filters and core labels uniform.  A future positive
input must give either the exponent-full lower bound, a fixed-power upper deficit,
or a genuine parameter dichotomy.  A one-AP divisor asymptotic, an almost-all
moduli result, or failure to find a theorem is insufficient.

Because merged 4gh explicitly requires this H decision to be consumed before
ordinary `Stage14-4gi`, and the audit leaves the external theorem unresolved,
the common contract requires the batch to stop here.

```text
MINIMAL_UNRESOLVED_EXTERNAL_GATE=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
MAINLINE_H_COMPLETED=true
MAINLINE_H_RESULT=NO_DIRECT_THEOREM_OR_COMPLETE_TRANSFER_CERTIFIED
MAINLINE_BLOCKED_BY_H=true
NEXT_H_NEEDED=false
STAGE14_4GI_EXECUTED=false
```

## Whole-family boundary

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## H boundary

```text
STAGE14_4GHH=COMPLETE_UNRESOLVED_EXTERNAL_FIRST_MOMENT_GATE
H_STAGE=Stage14-4ghH
AUDITED_THROUGH=Stage14-4gh
SOURCE_SNAPSHOT_SHA=79393f83b1110b7e66b41a23c51596a10bc6c7ef
TARGET_FILE=stages/stage14/14-4gh/h-target.md
TARGET_FROZEN=true
SOURCE_SNAPSHOT_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
EXACT_TWO_CRT_CONGRUENCES_RETAINED=true
EXACT_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM_DERIVED=true
OFF_THE_SHELF_THEOREM_APPLICABLE=false
DIRECT_TRANSFER_PROVED=false
FIRST_MOMENT_FULL_EXPONENT_PROVED=false
FIRST_MOMENT_FIXED_POWER_DEFICIT_PROVED=false
PARAMETER_DICHOTOMY_PROVED=false
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=UNRESOLVED_EXTERNAL_GATE:UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
```
