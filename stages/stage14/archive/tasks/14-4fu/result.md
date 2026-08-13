# Stage14-4fu — exact upper-bound transfer from two-sided unitary shadow to ordinary divisor shadow

## Status

`COMPLETE_FIXED_E_TWO_SIDED_UNITARY_TO_ORDINARY_DIVISOR_SHADOW_DOMINATION`

Consumes batch-local `Stage14-4ft`, merged `Stage14-4fm`, merged `Stage14-q14`, and merged `Stage14-Work-bvX34`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Two-sided fixed-E bare shadow

On the live two-sided branch from 4ft, exact `E=E0` is frozen and

```text
m=u*v,
gcd(u,v)=1,
u||m,
u in U_E0(m)=sqrt(m*R_int(E0*m)),
```

with both `u` and `v=m/u` on fixed positive exponent cells.

Define

```text
B_2s(m)
 := 1{exists u||m in U_E0(m)
       with both primitive sides on the frozen positive exponent cells}.
```

The physical support `A_2s(m)` is a subset of `B_2s(m)`.

## 2. Drop only the unitary restriction in the legal upper-bound direction

Every unitary divisor is an ordinary divisor.  Define the ordinary-divisor ambient shadow

```text
O_2s(m)
 := 1{exists d|m,
       d in U_E0(m),
       d and m/d on the same frozen positive exponent cells}.
```

Then pointwise and without any probabilistic assumption,

```text
A_2s(m) <= B_2s(m) <= O_2s(m).                (1)
```

No multiplicity comparison is needed for this upper bound.  No physical completion predicate is used to prove (1), and no divisor density is charged.

```text
UNITARY_TO_ORDINARY_DIVISOR_SHADOW_POINTWISE_DOMINATION=true
UNITARY_RESTRICTION_REMOVAL_COST_FOR_UPPER_BOUND=ZERO
UNITARY_TO_ORDINARY_TRANSFER_USES_INDEPENDENCE=false
PHYSICAL_COMPLETION_DROPPED_ONLY_FOR_LEGAL_UPPER_BOUND=true
```

## 3. Consequence for the q14/Ford route

Merged q14 listed the unitary/squareclass restriction as one reason a direct unrestricted divisor theorem could not simply be cross-promoted.  At the present fixed-E two-sided bare-shadow level, the **unitary part of that issue is no longer an obstruction for an upper bound**: an ordinary divisor-window support estimate automatically dominates the Stage14 two-sided unitary shadow through (1).

This does not make Ford direct.  The ordinary ambient shadow still uses the transported moving interval

```text
U_E0(m)=sqrt(m*R_int(E0*m)),
```

on the charged Stage14 outer exponent cell, and no merged theorem gives the absolute support capacity needed at the heavy threshold `B^mu`.

```text
Q14_UNITARY_RESTRICTION_AS_UPPER_BOUND_OBSTRUCTION_EXHAUSTED=true
Q14_MOVING_DIVISOR_INTERVAL_RETAINS=true
Q14_BRANCH_EXACT_ABSOLUTE_CAPACITY_BOUND_PROVED=false
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
```

## 4. Exact closure criterion for mechanism U on this branch

Let

```text
S_ord:=sum_m O_2s(m).
```

A surviving physical branch has

```text
sum_m A_2s(m) >= B^(mu-o(1)).
```

By (1), any theorem proving for some fixed `eta>0`

```text
S_ord <= B^(mu-eta+o(1))                         (2)
```

would close the entire two-sided fixed-E branch, independently of the conditional completion deficit.

Conversely, an estimate stated only as a relative density inside a larger unrestricted integer ensemble is not enough unless it implies (2) on the exact Stage14 exponent cell.

```text
FIXED_E_TWO_SIDED_BARE_CLOSURE_CRITERION=ordinary_divisor_shadow_absolute_support_below_B_to_mu
CHARGED_BASELINE_DISTORTION_NOT_NEEDED_IF_ABSOLUTE_CAPACITY_BOUND_BEATS_MU=true
RELATIVE_AMBIENT_DENSITY_ALONE_SUFFICIENT=false
```

## 5. Receiver and H decision

The arithmetic object is now closer to a classical divisor-window support problem, but a stable external theorem target still requires the moving interval and outer exponent threshold to be normalized together.  Therefore no H is frozen yet.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fv
```

## Boundary

```text
STAGE14_4FU=COMPLETE_FIXED_E_TWO_SIDED_UNITARY_TO_ORDINARY_DIVISOR_SHADOW_DOMINATION
UNITARY_TO_ORDINARY_DIVISOR_SHADOW_POINTWISE_DOMINATION=true
UNITARY_RESTRICTION_REMOVAL_COST_FOR_UPPER_BOUND=ZERO
Q14_UNITARY_RESTRICTION_AS_UPPER_BOUND_OBSTRUCTION_EXHAUSTED=true
FIXED_E_TWO_SIDED_BARE_CLOSURE_CRITERION=ordinary_divisor_shadow_absolute_support_below_B_to_mu
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fv
```