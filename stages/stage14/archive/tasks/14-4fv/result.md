# Stage14-4fv — freeze fixed-E receiver as endpoint completion support or moving ordinary-divisor capacity versus completion deficit

## Status

`COMPLETE_FIXED_E_ENDPOINT_OR_MOVING_ORDINARY_DIVISOR_CAPACITY_COMPLETION_RECEIVER`

Consumes batch-local `Stage14-4ft/4fu`, merged `Stage14-4fs`, merged `Stage14-s7-101`, merged `Stage14-q14`, and merged `Stage14-Work-bvX34`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Endpoint and two-sided fixed-E branches now have different minimal mechanisms

Batch-local 4ft proves that on the primitive endpoint branch the unitary witness choice disappears after the exact subpolynomial primitive factor is frozen.  The remaining Stage14-specific receiver is one-dimensional conditional physical completion support.

Batch-local 4fu proves that on the two-sided branch

```text
A_2s(m) <= B_2s(m) <= O_2s(m),
```

where `O_2s` is the ordinary-divisor shadow in the same moving transported interval and exponent cells.

Thus there is no longer one uniform fixed-E "unitary-divisor obstruction".

```text
FIXED_E_ENDPOINT_AND_TWO_SIDED_MINIMAL_MECHANISMS_DIFFER=true
FIXED_E_UNITARY_DIVISOR_AS_UNIFIED_FINAL_RECEIVER_SUPERSEDED=true
```

## 2. Two-sided exponent ledger with an ordinary ambient capacity

Write on one two-sided exponent cell

```text
S_phys,2s = B^(tau_2s+o(1)),
S_unit,2s = B^(sigma_unit+o(1)),
S_ord,2s  = B^(sigma_ord+o(1)),
```

with

```text
tau_2s <= sigma_unit <= sigma_ord.
```

A heavy survivor requires

```text
tau_2s >= mu.
```

Define the conditional completion deficit relative to the unitary shadow by

```text
delta_c,2s := sigma_unit-tau_2s >= 0.
```

The branch can therefore be closed in either of two legal ways:

```text
(U-ambient capacity)
  sigma_ord < mu;

(C-physical completion)
  delta_c,2s > sigma_unit-mu.
```

The ordinary shadow is only an upper envelope.  No equality or bounded-distortion relation between `S_ord` and `S_unit` is asserted.

```text
ORDINARY_SHADOW_ONLY_UPPER_ENVELOPE=true
ORDINARY_UNITARY_BASELINES_IDENTIFIED=false
TWO_SIDED_CLOSURE_BY_ABSOLUTE_ORDINARY_CAPACITY_OR_CONDITIONAL_COMPLETION=true
```

## 3. q14 transfer question is sharpened

For the fixed-E two-sided mechanism U, the earlier q14 checklist can now be simplified.

Already discharged at the current level:

```text
- reciprocal geometry has been reduced to one transported divisor interval;
- fixed E has removed the moving squareclass dilation;
- unitary divisors can be enlarged to ordinary divisors at zero upper-bound cost.
```

A charged-measure bounded-distortion theorem is **not logically necessary** if one can prove the stronger absolute estimate

```text
#{m on the exact Stage14 outer cell : O_2s(m)=1}
 <= B^(mu-eta+o(1))                               (1)
```

for some fixed `eta>0`.

What remains before Ford-type technology can be audited against (1) is the exact theorem-compatible normalization of the moving interval

```text
U_E0(m)=sqrt(m*R_int(E0*m))
```

and its dependence on the outer exponent cell.  Merged q14 supplies no such branch-exact fixed-power theorem.

```text
Q14_BOUNDED_DISTORTION_IS_SUFFICIENT_NOT_NECESSARY_FOR_ABSOLUTE_CAPACITY_CLOSURE=true
Q14_UNITARY_UPPER_BOUND_ADAPTER_COMPLETE=true
Q14_MOVING_INTERVAL_NORMALIZATION_RETAINS=true
Q14_ABSOLUTE_CAPACITY_BELOW_HEAVY_THRESHOLD_PROVED=false
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
```

## 4. Material receiver change

The fixed-E component of the heavy main receiver is now exactly

```text
FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport
OR
FixedComplementaryDilationTwoSidedMovingOrdinaryDivisorShadowAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit.
```

This is materially sharper than the 4fs fixed-E nested bare-unitary budget:

- endpoint cells no longer carry a divisor-existence receiver at all;
- two-sided cells admit a classical ordinary-divisor ambient upper bound;
- the remaining Ford-side question is an absolute moving-window capacity theorem, not a generic unitary-divisor transfer or an obligatory relative-measure adapter.

The polynomial-E branches from 4fs remain unchanged and are not multiplied with this fixed-E refinement.

```text
CURRENT_FIXED_E_HEAVY_RECEIVER=FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedMovingOrdinaryDivisorShadowAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit
CURRENT_HEAVY_RECEIVER=CurrentFixedEHeavyReceiver_OR_PolynomialComplementaryDilationBareShortUnitaryShadowExponentVersusConditionalCanonicalReverseCompletionDeficitBudget
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new heavy main H is opened at this boundary.  The theorem target is not yet frozen tightly enough: `O_2s(m)` still has an `m`-dependent transported interval, while Ford's standard `H(x,y,z)` formulation uses theorem parameters that must be normalized uniformly across the charged outer cell.

The next internal stage must quantify the cost of straightening the moving center/width into theorem-compatible fixed interval parameters.  If that produces a stable fixed-power theorem contract, the following batch must integrate the corresponding main-line H audit under the common contract.

```text
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4fw
```

## Boundary

```text
STAGE14_4FV=COMPLETE_FIXED_E_ENDPOINT_OR_MOVING_ORDINARY_DIVISOR_CAPACITY_COMPLETION_RECEIVER
FIXED_E_UNITARY_DIVISOR_AS_UNIFIED_FINAL_RECEIVER_SUPERSEDED=true
Q14_UNITARY_UPPER_BOUND_ADAPTER_COMPLETE=true
Q14_MOVING_INTERVAL_NORMALIZATION_RETAINS=true
Q14_ABSOLUTE_CAPACITY_BELOW_HEAVY_THRESHOLD_PROVED=false
CURRENT_FIXED_E_HEAVY_RECEIVER=FixedComplementaryDilationPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedMovingOrdinaryDivisorShadowAbsoluteCapacityVersusConditionalPhysicalCompletionDeficit
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fw
```