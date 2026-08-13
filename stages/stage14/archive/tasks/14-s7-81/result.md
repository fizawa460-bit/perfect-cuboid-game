# Stage14-s7-81 — fixed-kernel square-value incidence to exact four-factor squareclass relation

## Status

`COMPLETE_FIXED_KERNEL_SQUARE_VALUE_TO_FOUR_FACTOR_SQUARECLASS_RELATION`

Consumes merged `Stage14-s7-78..80`, merged mainline through `Stage14-4ex`, merged `Stage14-Work-boX27`, and latest main at batch start

```text
826205ff8aee31a80612583248af81421000e39c.
```

The current batch contract integrates any newly exposed `sH` audit into the same branch as a substantive work unit. No new `sH` is exposed here.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Import the merged radial square-kernel receiver

Merged `4ev..4ex` supersedes the earlier opaque radial-support description. On one fixed heavy primitive reciprocal ray,

```text
T := 4*Xr*Yr*epsilon_x*U*V
   = (x^2-y^2) h^2
   = K*(t0*h)^2,
```

where

```text
K=sqf(|x^2-y^2|)
```

and `K,t0` are fixed by the primitive ray. Merged `4ex` also proves that `h -> T` is injective and merged `4eq` gives only `B^o(1)` physical completion above each exact `T`.

Thus the live heavy-ray receiver is

```text
FixedPrimitiveRayCanonicalReciprocalProductFixedKernelSquareValueIncidence.
```

```text
MERGED_4EV_4EX_CONSUMED=true
FIXED_RAY_KERNEL_K_FIXED=true
RADIAL_H_TO_T_INJECTIVE=true
```

## 2. Remove the harmless square and frozen sign

Freeze the finite sign/orientation label `epsilon_x`. Since `4` is a square, the positive squareclass of the moving product is governed by

```text
F1:=|Xr|,
F2:=|Yr|,
F3:=|U|,
F4:=|V|.
```

For a positive integer `n`, write

```text
sqf(n)
```

for its squarefree kernel, equivalently its class in `Q_{>0}^*/(Q_{>0}^*)^2` represented by a squarefree integer.

From

```text
4*F1*F2*F3*F4 = K*z^2
```

with `z=t0*h`, one gets exactly

```text
sqf(F1*F2*F3*F4)=K.
```

```text
FOUR_FACTOR_PRODUCT_SQUARECLASS_EQUALS_FIXED_K=true
SQUARE_FACTOR_4_RECHARGE_ALLOWED=false
FINITE_SIGN_LABEL_COST=O1
```

## 3. Primewise parity form

For every prime `ell`, the preceding identity is equivalent to

```text
v_ell(F1)+v_ell(F2)+v_ell(F3)+v_ell(F4)
  == v_ell(K) (mod 2).
```

Since `K` is squarefree,

```text
v_ell(K) in {0,1}.
```

Thus primes outside `K` must occur with even total valuation parity across the four physical factors, while primes in `K` must occur with odd total parity.

Equivalently, if `kappa_j=sqf(Fj)`, then their prime supports satisfy the exact symmetric-difference relation

```text
supp(kappa_1) XOR supp(kappa_2) XOR supp(kappa_3) XOR supp(kappa_4)
  = supp(K).
```

No pairwise coprimality or squarefreeness of the four factors is assumed; valuation parity makes the identity valid with arbitrary overlaps.

```text
FIXED_KERNEL_CONDITION_IS_EXACT_VALUATION_PARITY_RELATION=true
FACTOR_PAIRWISE_COPRIMALITY_ASSUMED=false
FACTOR_SQUAREFREE_ASSUMED=false
```

## 4. Why this is not yet a density saving

The four factors are reconstructed from the same canonical physical background. Their squareclasses are therefore correlated. Treating each prime-parity condition as an independent factor `1/2`, or treating the four factor kernels as independent random squareclasses, would double-charge structure not proved by any merged stage.

Generic sparsity of square values is also unavailable: merged `4ex` already records that the moving canonical product can itself be biased toward the fixed squareclass.

```text
INDEPENDENT_FACTOR_SQUARECLASS_MODEL_ASSUMED=false
PER_PRIME_PARITY_DENSITY_RECHARGE_ALLOWED=false
GENERIC_SQUARE_DENSITY_RECHARGE_ALLOWED=false
FRESH_FIXED_POWER_SAVING_PROVED=false
```

## 5. Receiver and next

This stage exposes the exact squareclass equation inside the same fixed-kernel receiver. The next internal step is to use polynomial radial support plus the fact that there are only four physical factors to prove that at least one factor must itself have polynomial outer mobility.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_81_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_81=COMPLETE_FIXED_KERNEL_SQUARE_VALUE_TO_FOUR_FACTOR_SQUARECLASS_RELATION
MERGED_4EV_4EX_CONSUMED=true
FOUR_FACTOR_PRODUCT_SQUARECLASS_EQUALS_FIXED_K=true
FIXED_KERNEL_CONDITION_IS_EXACT_VALUATION_PARITY_RELATION=true
INDEPENDENT_FACTOR_SQUARECLASS_MODEL_ASSUMED=false
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_81_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-82
```
