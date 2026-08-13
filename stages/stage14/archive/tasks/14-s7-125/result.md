# Stage14-s7-125 — split first multiplicative-host deficit from second reverse-layer and post-mask deficits

## Status

`COMPLETE_MULTIPLICATIVE_HOST_SECOND_LAYER_POSTMASK_DEFICIT_LEDGER_AND_THEOREM_CONTRACT_REFINEMENT`

Consumes batch-local `Stage14-s7-123/124`, merged `Stage14-s7-120..122`, and merged `Stage14-Work-cbX40`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Nested support after allocation normalization

For each active nonaligned branch, start from the branch-specific precompletion support `S_pre` of s7-120. After freezing one exact squarefree allocation as in s7-124, define three further nested supports:

```text
S_mult := {outer candidates whose host z admits
           some (g,x,y) with g*x*y=c_C*z and R_mult=1};

S_rev2 := {outer candidates in S_mult for which some such
           first-layer triple extends through cp=c*p, dq=d*q
           and the second reverse factor-pair reconstruction};

S_phys := {outer candidates in S_rev2 for which at least one
           complete reverse witness also passes the residual
           root/canonical/post-column mask}.
```

Hence exactly

```text
S_phys subset S_rev2 subset S_mult subset S_pre.
```

No probabilistic independence is used.

## 2. Exponent ledger

On one principal exponent cell write

```text
#S_pre  = B^(sigma_pre+o(1)),
#S_mult = B^(sigma_mult+o(1)),
#S_rev2 = B^(sigma_rev2+o(1)),
#S_phys = B^(tau+o(1)).
```

Define nonnegative conditional deficits

```text
delta_mult := sigma_pre-sigma_mult,
delta_rev2 := sigma_mult-sigma_rev2,
delta_post := sigma_rev2-tau.
```

Then

```text
tau = sigma_pre-delta_mult-delta_rev2-delta_post.
```

A heavy survivor therefore requires

```text
sigma_pre-delta_mult-delta_rev2-delta_post >= mu.
```

This refines the s7-120 two-deficit ledger by opening the previously bundled square-class reverse deficit into first-layer multiplicative-host loss and second-layer reverse loss.

```text
S_MULTIPLICATIVE_REVERSE_POSTMASK_THREE_DEFICIT_LEDGER_PROVED=true
S_HEAVY_SURVIVAL_BUDGET=sigma_pre_minus_delta_mult_minus_delta_rev2_minus_delta_post_ge_mu
```

## 3. One-dimensional theorem contract

For the fixed-E endpoint and polynomial-E fixed-product branches, the charged outer variable is one scalar `z` (`t` or `E`). After freezing packet data and one squarefree allocation, the bare reverse problem has the common theorem species

```text
UniformOneDimensionalFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport
```

meaning uniform control, on every principal scalar cell, of the support loss caused by

```text
g*x*y=c_C*z,
R_mult(z;g,x,y)=1,
cp=c*p,
dq=d*q,
second reciprocal factor-pair existence,
```

before the branch-specific residual post-mask is charged.

The endpoint and fixed-product branches share the theorem species but not necessarily identical frozen coefficients or post-masks.

```text
S_ONE_DIMENSIONAL_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true
```

## 4. Polynomial outer-pair theorem contract

For the polynomial `(E,m)` branch, the charged outer measure remains the pair `(E,m)` while

```text
z=n=E*m
```

appears only as the internal reverse host. Therefore the correct theorem species is

```text
UniformPolynomialOuterPairFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupport.
```

Its support is counted on charged pairs `(E,m)`, with pair-dependent prefilters retained. The `B^o(1)` factorization fiber of a fixed `n` cannot replace this pair support by a scalar `n` indicator and cannot be used as a saving.

```text
S_POLYNOMIAL_PAIR_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true
S_FIXED_N_PAIR_FIBER_RECHARGED=false
```

## 5. Material receiver change

The three active nonaligned branches are no longer received as undifferentiated fixed-square-class two-level factor-pair support. Their bare reverse deficit now has two explicit arithmetic layers:

```text
first layer:
  fixed-allocation filtered triple-product host g*x*y=c_C*z;
second layer:
  cp,dq factorization plus reciprocal reconstruction;
then:
  residual post-mask.
```

The aligned fixed-E two-sided realization remains parked at the already completed main H boundary

```text
UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment.
```

Thus the current s receiver is

```text
FixedETwoSidedParkedUniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment
OR
OneDimensionalFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupportThenConditionalPostMask
OR
PolynomialOuterPairFiberedFixedSquarefreeAllocationTripleProductHostedTwoLevelReverseReciprocalSupportThenConditionalPostMask.
```

```text
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H / q decision

No new sH is opened here. The theorem targets are now sharper versions of the q18-ready contracts identified at s7-122, and merged Work-cbX40 assigns literature-target decisions to the integrated XQ/q pass rather than to a duplicate s-local H. The s route must not perform an independent literature search or infer theorem availability from the normalization alone.

```text
S_ROUTE_H_NEEDED=false
Q18_THEOREM_TARGETS_REFINED=true
WORK_CBX40_REVISIT_TRIGGER_S7_122_ALREADY_REACHED=true
```

## 7. Boundary

```text
STAGE14_S7_125=COMPLETE_MULTIPLICATIVE_HOST_SECOND_LAYER_POSTMASK_DEFICIT_LEDGER_AND_THEOREM_CONTRACT_REFINEMENT
S_MULTIPLICATIVE_REVERSE_POSTMASK_THREE_DEFICIT_LEDGER_PROVED=true
S_ONE_DIMENSIONAL_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true
S_POLYNOMIAL_PAIR_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-126
```
