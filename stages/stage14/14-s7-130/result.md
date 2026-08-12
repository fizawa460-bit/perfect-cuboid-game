# Stage14-s7-130 — conditioned second-reverse support versus joint first moment

## Status

`COMPLETE_SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE`

Consumes merged `Stage14-s7-128`, merged q19, and batch-local `Stage14-s7-129`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. First-layer witness measure

Let `Lambda_mult` be the exact charged first-layer witness set on one frozen principal cell. It retains the scalar outer variable on the two one-dimensional branches and the full `(E,m)` outer pair on the polynomial branch.

Define

```text
Lambda_rev2 := {lambda in Lambda_mult : N_rev2(lambda)>=1}.
```

The physical post-mask has not yet been applied.

## 2. Joint first moment

Define the nonnegative conditioned joint first moment

```text
J_rev2 := sum_{lambda in Lambda_mult} N_rev2(lambda).
```

Since every `lambda` in `Lambda_rev2` contributes at least one and s7-129 gives the pointwise `B^o(1)` multiplicity envelope,

```text
#Lambda_rev2
 <= J_rev2
 <= B^o(1) #Lambda_rev2.
```

Hence `J_rev2` and second-layer extendable first-witness support have the same fixed-power exponent.

```text
SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true
SECOND_REVERSE_SUPPORT_TO_MOMENT_LOSS=Bo1
```

This does not prove that `#Lambda_rev2` is large relative to `#Lambda_mult`; it only replaces the support question by an exactly equivalent nonnegative first-moment question at fixed-power precision.

## 3. Outer support versus witness support

A charged outer candidate may have `B^o(1)` first-layer witnesses by merged s7-128. Therefore projecting `Lambda_mult` or `Lambda_rev2` to charged outer candidates also changes counts by at most `B^o(1)`.

Thus, separately for the scalar species and the polynomial pair species, the fixed-power exponent of second-layer outer support equals the exponent of `J_rev2`.

No scalarization of `(E,m)` through `n=Em` occurs.

```text
SECOND_REVERSE_OUTER_SUPPORT_JOINT_MOMENT_EQUIVALENCE_PROVED=true
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
FIXED_N_PAIR_FIBER_RECHARGED=false
```

## 4. Updated deficit ledger

The first-layer deficit `delta_mult` is already represented by the merged filtered-tau3 first moment and may not be recharged. The second reverse deficit is now exactly the conditional loss measured by `J_rev2` relative to the charged first-layer witness mass.

The residual `delta_post` remains untouched.

```text
FIRST_LAYER_DEFICIT_RECHARGED=false
SECOND_LAYER_JOINT_MOMENT_RECEIVER_PROVED=true
POST_MASK_REMAINS_SEPARATE=true
RECEIVER_MATERIALLY_CHANGED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-131
```

## Boundary

```text
STAGE14_S7_130=COMPLETE_SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE
SECOND_REVERSE_SUPPORT_FIRST_MOMENT_EQUIVALENCE_PROVED=true
SECOND_REVERSE_OUTER_SUPPORT_JOINT_MOMENT_EQUIVALENCE_PROVED=true
SECOND_REVERSE_SUPPORT_TO_MOMENT_LOSS=Bo1
FIRST_LAYER_DEFICIT_RECHARGED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-131
```
