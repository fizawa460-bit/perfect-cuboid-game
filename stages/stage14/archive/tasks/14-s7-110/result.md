# Stage14-s7-110 — principal polynomial fibered product capacity versus conditional physical-lift deficit

## Status

`COMPLETE_POLYNOMIAL_PRINCIPAL_FIBERED_DISTINCT_PRODUCT_CAPACITY_VERSUS_PHYSICAL_LIFT_RECEIVER`

Consumes batch-local `Stage14-s7-108/109`, merged mainline `Stage14-4fw..4fy`, and merged `Stage14-Work-bxX36`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Principal polynomial fibered product cell

After s7-109 every surviving polynomial `(E,m)` ordinary-envelope cell has one cardinality-localized E-set `E_*` with

```text
#E_* = B^(kappa_E+o(1)),
#D_E <= B^(kappa_D+o(1)),
#V_E <= B^(kappa_V+o(1)),
```

and necessarily

```text
kappa_E+kappa_D+kappa_V >= mu-o(1).
```

Its exact ordinary outer-pair support is

```text
P_fib(E_*)
 := {(E,d*v): E in E_*, d in D_E, v in V_E}.
```

Because E is retained as the first outer coordinate,

```text
#P_fib(E_*)
 = sum_{E in E_*} #P(D_E,V_E).
```

## 2. Distinct fibered-product exponent

Write

```text
#P_fib(E_*) = B^(pi_fib+o(1)),
0 <= pi_fib <= kappa_E+kappa_D+kappa_V.
```

The gap

```text
(kappa_E+kappa_D+kappa_V)-pi_fib
```

is precisely the aggregate loss caused by multiplicative collisions **inside** the E-fibers.  There are no collisions between different E-fibers in the outer-pair space.

```text
FIBERED_DISTINCT_PRODUCT_EXPONENT_PI_DEFINED=true
FIBERED_PRODUCT_COMPRESSION_IS_FIBERWISE=true
CROSS_E_PRODUCT_COMPRESSION=false
```

## 3. Put physical support directly under the distinct product image

Let

```text
S_phys,fib
 := #{(E,m) on E_* : A_pair(E,m)=1}
 = B^(tau_fib+o(1)).
```

The exact inclusions from s7-107/108 give

```text
supp(A_pair) subseteq P_fib(E_*),
```

so

```text
0 <= tau_fib <= pi_fib.
```

Define the total conditional physical-lift deficit from the ordinary fibered product envelope by

```text
delta_lift,fib := pi_fib-tau_fib >= 0.
```

This one deficit retains every condition removed in passing from a physical unitary witness to the ordinary fibered image, including

```text
- unitary/coprime-complement structure;
- primitive/orientation conditions not forced by the normalized coordinates;
- root-origin/parity/two-primary masks;
- canonical orientation;
- reverse/post-column completion.
```

It is a nested-support exponent and makes no independence assertion.

A heavy survivor requires exactly

```text
pi_fib-delta_lift,fib=tau_fib >= mu.              (1)
```

Therefore survival forces

```text
pi_fib >= mu-o(1),
delta_lift,fib <= pi_fib-mu+o(1).
```

```text
POLYNOMIAL_FIBER_PRODUCT_PHYSICAL_SUPPORT_NESTED=true
POLYNOMIAL_FIBER_SURVIVAL_BUDGET=pi_fib_minus_delta_lift_ge_mu
```

## 4. Two noninterchangeable remaining mechanisms

The polynomial-pair branch can now close only by one of the same abstract mechanisms as the fixed-E principal rectangle, but on a genuinely different arithmetic family.

### P_fib — fiberwise multiplicative compression

Prove that every relevant principal fibered cell satisfies

```text
pi_fib <= mu-eta
```

for some fixed `eta>0`.

### C_fib — conditional physical lift

When `pi_fib>=mu`, prove

```text
delta_lift,fib > pi_fib-mu
```

uniformly on the charged cell.

The mechanisms are not multiplied without a same-cell joint estimate.

```text
FIBERED_DISTINCT_PRODUCT_CAPACITY_MECHANISM_SEPARATED=true
FIBERED_CONDITIONAL_PHYSICAL_LIFT_MECHANISM_SEPARATED=true
FIBERED_PRODUCT_AND_LIFT_INDEPENDENCE_ASSUMED=false
```

## 5. Relation to the fixed-E mainline receiver

Merged 4fy has the fixed-E principal receiver

```text
FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit.
```

The present polynomial-E receiver is not that rectangle multiplied by an E-count.  It is the direct sum of E-indexed multiplication images

```text
sum_E #P(D_E,V_E),
```

with E-dependent factor sets.  Only the threshold/collision/lift language is shared.

```text
FIXED_E_AND_POLYNOMIAL_E_PRODUCT_COUNTS_MULTIPLICABLE=false
FIXED_E_RECTANGULAR_THEOREM_CROSS_PROMOTABLE=false
COMMON_PRODUCT_CAPACITY_LANGUAGE_ONLY=true
```

## 6. Material s receiver change

Combining merged mainline through 4fy with s7-106 and the present fibered reduction, the four s realizations are now

```text
(A) fixed-E primitive endpoint:
    one-dimensional conditional physical-completion support;

(B) fixed-E two-sided polynomial:
    principal rectangular distinct-product capacity
    versus conditional physical-lift deficit;

(C) polynomial-E fixed primitive product:
    one-dimensional conditional physical-completion support;

(D) polynomial-E polynomial primitive product:
    principal fibered distinct-product outer-pair capacity
    versus conditional physical-lift deficit.
```

Thus the former polynomial moving ordinary-divisor outer-pair receiver is superseded.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit_OR_PolynomialComplementaryDilationFixedPrimitiveProductOneDimensionalConditionalPhysicalCompletionSupport_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductPrincipalFiberedDistinctProductOuterPairCapacityVersusConditionalPhysicalLiftDeficit
RECEIVER_MATERIALLY_CHANGED=true
```

## 7. H and Work decisions

No new sH is opened at this boundary.  The fibered multiplication object is now stable, but the next internal step should split principal fibers by multiplicative collision energy / near-injective support before freezing an external theorem target.  An H request at s7-110 would otherwise ask for a stronger multiplication-table theorem than the Stage14 exponent ledger may require.

This stage reaches the explicit `s7-110` component of merged Work-bxX36's revisit condition.

```text
S7_110_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
WORK_BXX36_REVISIT_TRIGGER_S7_110_REACHED=true
NEXT=Stage14-s7-111
```

## Boundary

```text
STAGE14_S7_110=COMPLETE_POLYNOMIAL_PRINCIPAL_FIBERED_DISTINCT_PRODUCT_CAPACITY_VERSUS_PHYSICAL_LIFT_RECEIVER
FIBERED_DISTINCT_PRODUCT_EXPONENT_PI_DEFINED=true
POLYNOMIAL_FIBER_SURVIVAL_BUDGET=pi_fib_minus_delta_lift_ge_mu
FIBERED_DISTINCT_PRODUCT_CAPACITY_MECHANISM_SEPARATED=true
FIBERED_CONDITIONAL_PHYSICAL_LIFT_MECHANISM_SEPARATED=true
FIXED_E_AND_POLYNOMIAL_E_PRODUCT_COUNTS_MULTIPLICABLE=false
WORK_BXX36_REVISIT_TRIGGER_S7_110_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_110_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-111
```
