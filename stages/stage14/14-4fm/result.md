# Stage14-4fm — complementary-dilation scale split and unitary-divisor physical receivers

## Status

`COMPLETE_COMPLEMENTARY_E_SCALE_SPLIT_TO_FIXED_E_UNITARY_DIVISOR_OR_POLYNOMIAL_E_COUPLED_INCIDENCE`

Consumes batch-local `Stage14-4fk/4fl`, merged `Stage14-s7-90..92`, merged `Stage14-Work-bsX31`, and merged `Stage14-q14` only as its already-recorded literature-routing boundary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze the complementary-dilation exponent

On one branch from 4fl write

```text
n=B^(nu+o(1)),
E=B^(epsilon+o(1)),
u=B^(alpha+o(1)),
v=B^(beta+o(1)),
nu=epsilon+alpha+beta,
```

with

```text
n=E*u*v,
gcd(u,v)=1.
```

There are two complementary-dilation alternatives:

```text
(A) epsilon=0: E=B^o(1),
(B) epsilon>0: E has polynomial scale.
```

A surviving heavy mass may be frozen to one of these two alternatives at finite/exponent-zero cost.

```text
COMPLEMENTARY_E_SCALE_SPLIT_EXPLICIT=true
HEAVY_MASS_CAN_BE_FROZEN_TO_ONE_E_SCALE_BRANCH=true
```

## 2. Subpolynomial E becomes a fixed unitary-divisor problem

On branch (A), exact `E` has only `B^o(1)` possibilities. Freeze one surviving value

```text
E=E0.
```

If the local complementary mask satisfies `m_E(E0)=0`, that frozen cell is empty; hence on a surviving cell it is the constant `1` and cannot be charged again.

Put

```text
m:=n/E0.
```

Then exactly

```text
m=u*v,
gcd(u,v)=1,
v=m/u.                                              (1)
```

Thus `u` is a **unitary divisor** of `m`. The primitive-ratio condition becomes

```text
u/v = u^2/m in R_int(E0*m).                         (2)
```

Equivalently, `u` lies in the transported short interval

```text
sqrt(m * R_int(E0*m)).                              (3)
```

while the residual physical weight is

```text
m_cpl(E0*m,u,m/u,E0).                               (4)
```

The fixed-`E` heavy branch is therefore an exact short **unitary-divisor** incidence problem with the original canonical/reverse-completion Boolean retained.

```text
SUBPOLYNOMIAL_E_EXACT_VALUE_FREEZABLE=Bo1
FIXED_E_LOCAL_MASK_RECHARGE_ALLOWED=false
FIXED_E_PRIMITIVE_RATIO_EQUALS_UNITARY_DIVISOR_SELECTOR=true
FIXED_E_UNITARY_DIVISOR_SHORT_WINDOW_EXPLICIT=true
```

## 3. Polynomial E remains a genuine complementary-dilation correlation

On branch (B), define again

```text
m:=u*v=n/E.
```

Then

```text
E=B^(epsilon+o(1)),
m=B^(nu-epsilon+o(1)),
epsilon>0,
```

and every incidence has

```text
n=E*m,
u|m,
gcd(u,m/u)=1,
u^2/m in R_int(E*m),
```

weighted by

```text
m_E(E) * m_cpl(E*m,u,m/u,E).                       (5)
```

Because `E` itself has polynomial support, it cannot be frozen at `B^o(1)` cost. The remaining object is consequently a two-level correlation between a polynomial complementary dilation and a short unitary-divisor selector on `m`, with the full physical completion weight in (5).

```text
POLYNOMIAL_E_FREEZE_ALLOWED=false
POLYNOMIAL_E_UNITARY_DIVISOR_COUPLED_CORRELATION_EXPLICIT=true
```

## 4. q14 Ford transfer status

Merged q14 identified Ford's divisor-in-an-interval architecture as the nearest unrestricted model but required four transfer checks.

At the present boundary:

```text
Q14_STEP1_RECIPROCAL_WINDOW_TO_ONE_DIVISOR_INTERVAL=PASS_AT_GEOMETRY_LEVEL
Q14_STEP2_SQUARECLASS_REMOVAL=PASS_ONLY_ON_FIXED_E_BRANCH_AFTER_FREEZE
Q14_STEP3_CHARGED_PHYSICAL_MEASURE_BOUNDED_DISTORTION=NOT_PROVED
Q14_STEP4_FIXED_POWER_RELATIVE_DEFICIT=NOT_PROVED
```

Even branch (A) is not a direct Ford application: its divisor is unitary and the Boolean (4) is the charged canonical/reverse physical weight. An unrestricted divisor-window count may upper-bound a larger ambient set, but no merged result compares that ambient baseline to the Stage14 heavy packet with the fixed-power precision needed to close the branch.

Branch (B) is farther from the unrestricted Ford ensemble because the polynomial `E`-correlation remains explicit.

```text
FORD_2008_DIRECT_ON_FIXED_E_PHYSICAL_UNITARY_DIVISOR_BRANCH=false
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
Q14_UNRESTRICTED_SAVING_CROSS_PROMOTED=false
```

## 5. Material receiver change and H decision

The opaque complementary physical weight from 4fk has now split into two concrete arithmetic receivers:

```text
(A)
FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence

OR

(B)
PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation.
```

This is a material receiver change and ends the batch.

A new heavy H audit is still premature. On (A), the exact canonical/reverse Boolean must be opened before a Ford/unitary-divisor theorem target can be frozen. On (B), the polynomial `E` weight must likewise be decomposed before an external bilinear target is stable.

The next internal mainline step should attack branch (A) first because the complementary dilation has already been frozen there.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation
RECEIVER_MATERIALLY_CHANGED=true
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4fn
```

## Boundary

```text
STAGE14_4FM=COMPLETE_COMPLEMENTARY_E_SCALE_SPLIT_TO_FIXED_E_UNITARY_DIVISOR_OR_POLYNOMIAL_E_COUPLED_INCIDENCE
COMPLEMENTARY_E_SCALE_SPLIT_EXPLICIT=true
FIXED_E_UNITARY_DIVISOR_SHORT_WINDOW_EXPLICIT=true
POLYNOMIAL_E_UNITARY_DIVISOR_COUPLED_CORRELATION_EXPLICIT=true
Q14_STEP3_CHARGED_PHYSICAL_MEASURE_BOUNDED_DISTORTION=NOT_PROVED
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fn
```
