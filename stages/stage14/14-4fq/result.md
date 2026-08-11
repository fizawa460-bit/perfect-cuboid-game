# Stage14-4fq — fixed complementary dilation: physical outer support to bare-unitary shadow and conditional completion ledger

## Status

`COMPLETE_FIXED_E_PHYSICAL_SUPPORT_TO_BARE_UNITARY_SHADOW_AND_COMPLETION_LEDGER`

Consumes only merged theorem sources from batch-start main

```text
3af02c764300db002cce3e3bdf7da1236548ecbd
```

namely merged `Stage14-4fn..4fp`, merged `Stage14-s7-96..98`, and merged `Stage14-Work-buX33`.  Only merged artifacts are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed-E outer support receiver

Merged 4fn/4fp leaves, after freezing one exact admissible subpolynomial complementary dilation

```text
E=E0,
```

the outer acceptance predicate

```text
A_E0(m)=1
```

iff there exists a unitary divisor witness

```text
u || m,
u in U_E0(m),
```

satisfying the exact retained canonical/root-origin/reverse/post-column completion Boolean

```text
k_E0(m,u)=1.
```

A surviving heavy packet forces

```text
S_phys(E0):=#{m:A_E0(m)=1} >= B^(mu-o(1)).
```

The inner unitary multiplicity is already exhausted at `B^o(1)` and is not recharged here.

## 2. Define the bare unitary shadow

Remove **only** the canonical/reverse completion predicate, retaining the same outer cell, transported reciprocal interval, unitary condition, primitive orientation convention, and every condition already built into the fixed packet. Define

```text
B_E0(m)
 := 1{exists u || m with u in U_E0(m)}.
```

Then pointwise

```text
A_E0(m) <= B_E0(m).
```

Let

```text
S_bare(E0):=sum_m B_E0(m).
```

Therefore any heavy survivor necessarily has

```text
S_bare(E0) >= S_phys(E0) >= B^(mu-o(1)).
```

This is the exact legal place where a divisor-in-an-interval theorem could act: on the **bare** support.  No Ford/q14 estimate is imported here.

```text
FIXED_E_BARE_UNITARY_SHADOW_DEFINED=true
FIXED_E_PHYSICAL_SUPPORT_SUBSET_BARE_SHADOW=true
FIXED_E_BARE_SHADOW_REQUIRED_EXPONENT_AT_LEAST_MU=true
FORD_SAVING_IMPORTED=false
```

## 3. Exact conditional-completion exponent ledger

On one exponent cell write

```text
S_bare(E0)=B^(sigma+o(1)),
S_phys(E0)=B^(tau+o(1)),
```

with

```text
0 <= tau <= sigma,
tau >= mu
```

on a surviving physical packet.

Define the conditional completion deficit exponent

```text
delta_c := sigma-tau >= 0.
```

Equivalently,

```text
S_phys(E0)/S_bare(E0)=B^(-delta_c+o(1)).
```

No assertion is made that `delta_c=0`.  The exact survival budget is only

```text
sigma-delta_c=tau >= mu.               (1)
```

Thus there are two logically separate ways to close this fixed-E branch:

```text
(A) bare-shadow sparsity: sigma < mu;
(B) conditional physical-completion deficit: delta_c > sigma-mu.
```

Neither is currently proved uniformly.  In particular, if `sigma>mu`, a genuine fixed-power completion deficit can coexist with survival, so one may not demand exponent-zero conditional density without first controlling the bare-shadow exponent.

```text
FIXED_E_BARE_SUPPORT_EXPONENT=sigma
FIXED_E_PHYSICAL_SUPPORT_EXPONENT=tau
FIXED_E_CONDITIONAL_COMPLETION_DEFICIT_EXPONENT=delta_c
FIXED_E_SURVIVAL_BUDGET=sigma_minus_delta_c_ge_mu
EXPONENT_ZERO_COMPLETION_DENSITY_FORCED=false
```

## 4. Charged-once locks

The split

```text
physical support
 -> bare unitary shadow
 + conditional completion density
```

does not create two independent counts.  It is a nested support comparison on the same outer integers `m`.

The following remain forbidden:

```text
recharging unitary-divisor multiplicity,
recharging radial endpoint removal,
assuming independence of completion and divisor geometry,
identifying the bare shadow with the unrestricted ordinary-divisor ensemble,
using a Ford estimate without a proved exponent comparison.
```

```text
FIXED_E_BARE_AND_PHYSICAL_COUNTS_MULTIPLICABLE=false
UNITARY_INNER_FIBER_RECHARGED=false
CANONICAL_REVERSE_INDEPENDENCE_ASSUMED=false
```

## 5. H decision

The fixed-E receiver is sharper, but this single-branch ledger is not yet a stable new main-line H target because the polynomial-`E` branch must be put into the same bare-shadow/conditional-completion language before the main receiver can be frozen.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fr
```

## Boundary

```text
STAGE14_4FQ=COMPLETE_FIXED_E_PHYSICAL_SUPPORT_TO_BARE_UNITARY_SHADOW_AND_COMPLETION_LEDGER
FIXED_E_BARE_UNITARY_SHADOW_DEFINED=true
FIXED_E_PHYSICAL_SUPPORT_SUBSET_BARE_SHADOW=true
FIXED_E_SURVIVAL_BUDGET=sigma_minus_delta_c_ge_mu
EXPONENT_ZERO_COMPLETION_DENSITY_FORCED=false
FORD_SAVING_IMPORTED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-4fr
```
