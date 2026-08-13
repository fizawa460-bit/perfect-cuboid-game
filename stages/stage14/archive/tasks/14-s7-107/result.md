# Stage14-s7-107 — polynomial outer-pair unitary shadow to ordinary-divisor absolute upper envelope

## Status

`COMPLETE_POLYNOMIAL_OUTER_PAIR_ORDINARY_DIVISOR_ABSOLUTE_CAPACITY_ENVELOPE_AND_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-105/106`, merged `Stage14-s7-98/104`, merged `Stage14-4fu/4fv`, merged `Stage14-q15`, and merged `Stage14-Work-bwX35`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the polynomial-(E,m) realization

On the live polynomial outer-pair branch,

```text
E=B^(epsilon+o(1)), epsilon>0,
m=B^(kappa+o(1)), kappa>0,
n=E*m,
```

physical acceptance requires a primitive pair

```text
m=u*v,
gcd(u,v)=1,
u || m,
u in U_phys(E,m),
```

with the retained physical Boolean.  After the provenance correction of s7-106, keep the only named E-only factor explicit:

```text
m_K(E)=1_{gcd(sqf(E),K_Z)=1}.
```

Define the exact physical outer-pair selector

```text
A_pair(E,m)
 := m_K(E)
    * 1{exists u || m,
        u in U_phys(E,m),
        C_pair(E,m,u)=1},
```

where `C_pair` contains every remaining primitive/orientation/root-origin/parity/canonical/reverse-completion condition not already forced by the normalized coordinate identities.

## 2. Define unitary and ordinary outer-pair shadows

Remove only the residual physical completion predicate:

```text
B_unit,pair(E,m)
 := m_K(E)
    * 1{exists u || m with u in U_phys(E,m)}.
```

Now enlarge the unitary witness to an arbitrary divisor in the **same** moving interval:

```text
O_ord,pair(E,m)
 := m_K(E)
    * 1{exists d | m with d in U_phys(E,m)}.
```

Since every unitary divisor is an ordinary divisor, pointwise

```text
A_pair(E,m)
 <= B_unit,pair(E,m)
 <= O_ord,pair(E,m).
```

This inclusion is independent of whether E is fixed.  What failed to transfer from merged 4fu was only the already-packaged fixed-E theorem target; the elementary upper-envelope inclusion itself remains valid on every polynomial `(E,m)` cell.

```text
POLYNOMIAL_PAIR_UNITARY_TO_ORDINARY_POINTWISE_ENVELOPE_PROVED=true
POLYNOMIAL_PAIR_ORDINARY_ENVELOPE_RETAINS_SAME_MOVING_INTERVAL=true
POLYNOMIAL_PAIR_E_LOCAL_KERNEL_MASK_RETAINED=true
POLYNOMIAL_PAIR_PHYSICAL_MASK_DROPPED_FROM_TARGET=false
```

## 3. Absolute-capacity-first closure on the outer pair

Let

```text
S_phys,pair := #supp(A_pair),
S_unit,pair := #supp(B_unit,pair),
S_ord,pair  := #supp(O_ord,pair).
```

Then

```text
S_phys,pair <= S_unit,pair <= S_ord,pair.
```

A heavy realization requires

```text
S_phys,pair >= B^(mu-o(1)).
```

Therefore a fixed `eta>0` estimate

```text
S_ord,pair <= B^(mu-eta+o(1))
```

would close this complete branch without any relative unitary/ordinary comparison and without opening the conditional physical Boolean.

If such an absolute estimate is unavailable, the remaining Stage14-specific alternative is a conditional deficit of physical completion inside the actual unitary shadow.

```text
POLYNOMIAL_PAIR_ABSOLUTE_CAPACITY_FIRST_CLOSURE=true
POLYNOMIAL_PAIR_BOUNDED_DISTORTION_UNITARY_ORDINARY_REQUIRED=false
POLYNOMIAL_PAIR_ORDINARY_ABSOLUTE_CAPACITY_BELOW_MU_PROVED=false
POLYNOMIAL_PAIR_CONDITIONAL_PHYSICAL_COMPLETION_DEFICIT_RETAINS=true
```

## 4. Why no Ford/q15 theorem is charged here yet

The ordinary upper envelope is two-dimensional:

```text
(E,m) -> U_phys(E,m),
```

and the interval depends on both outer variables through the reciprocal root-window geometry.  Merged q15 only supplies near results for localized ordinary-divisor support and explicitly requires a Stage14-compatible width/normalization test before charging them.

Thus this stage proves the legal envelope but not a fixed-power capacity estimate.

```text
Q15_LOCALIZED_DIVISOR_WIDTH_COMPATIBILITY_REMAINS=true
POLYNOMIAL_PAIR_THEOREM_COMPATIBLE_NORMALIZATION_PROVED=false
FORD_DRAPPEAU_MOUNIER_DIRECTLY_CHARGED=false
```

## 5. Material receiver change

Combining s7-103, s7-105, s7-106 and the present outer-pair envelope, the four s realizations reduce to

```text
(A) fixed-E primitive endpoint:
    one-dimensional conditional physical-completion support;

(B) fixed-E two-sided polynomial:
    moving ordinary-divisor absolute capacity
    versus conditional physical-completion deficit;

(C) polynomial-E fixed primitive product:
    one-dimensional conditional physical-completion support;

(D) polynomial-E polynomial primitive product:
    moving ordinary-divisor outer-pair absolute capacity
    versus conditional physical-completion deficit.
```

The previous polynomial-pair unitary-shadow receiver is therefore superseded at the absolute-capacity level.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPolynomialMovingOrdinaryDivisorShadowAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit_OR_PolynomialComplementaryDilationFixedPrimitiveProductOneDimensionalConditionalPhysicalCompletionSupport_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductMovingOrdinaryDivisorOuterPairAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H and Work decisions

No new sH is opened.  Both ordinary-divisor envelopes still have moving Stage14-specific intervals that are not theorem-normalized, while both one-dimensional branches retain opaque physical-completion support.  The theorem target is therefore not yet stable enough for an independent sH audit.

This stage reaches the `s7-107` component of merged Work-bwX35's normal accumulation target.

```text
S7_107_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
WORK_BWX35_REVISIT_TRIGGER_S7_107_REACHED=true
```

## Boundary

```text
STAGE14_S7_107=COMPLETE_POLYNOMIAL_OUTER_PAIR_ORDINARY_DIVISOR_ABSOLUTE_CAPACITY_ENVELOPE_AND_RECEIVER_CHANGE
POLYNOMIAL_PAIR_UNITARY_TO_ORDINARY_POINTWISE_ENVELOPE_PROVED=true
POLYNOMIAL_PAIR_ABSOLUTE_CAPACITY_FIRST_CLOSURE=true
POLYNOMIAL_PAIR_ORDINARY_ABSOLUTE_CAPACITY_BELOW_MU_PROVED=false
Q15_LOCALIZED_DIVISOR_WIDTH_COMPATIBILITY_REMAINS=true
WORK_BWX35_REVISIT_TRIGGER_S7_107_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_107_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-108
```