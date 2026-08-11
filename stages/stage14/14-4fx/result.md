# Stage14-4fx — rectangular product-set pair capacity localization

## Status

`COMPLETE_FIXED_E_RECTANGULAR_PRODUCT_PAIR_CAPACITY_LOCALIZATION`

Consumes batch-local `Stage14-4fw` and merged `Stage14-Work-bwX35`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Product-set upper envelope

Stage14-4fw gives, on one frozen fixed-`E` two-sided cell,

```text
A_2s(m) <= 1_{m in P(D,V)},
P(D,V)={dv:d in D,v in V}.
```

Let the integer cardinalities of the two fixed factor windows be localized as

```text
#D = B^(kappa_D+o(1)),
#V = B^(kappa_V+o(1)),
kappa_D,kappa_V>=0.
```

This is a charged dyadic/exponent localization only.

## 2. Elementary pair-capacity envelope

The multiplication map

```text
D x V -> P(D,V),
(d,v) -> dv
```

is surjective. Therefore

```text
#P(D,V) <= #D #V
          = B^(kappa_D+kappa_V+o(1)).             (1)
```

No arithmetic theorem is required for (1).

If a heavy physical cell requires

```text
#supp(A_2s) >= B^(mu-o(1)),
```

then the upper-envelope absolute-capacity lemma from merged Work-bwX35 immediately closes every rectangle for which there is a fixed `eta>0` with

```text
kappa_D+kappa_V <= mu-eta.                         (2)
```

Hence every surviving two-sided rectangle must satisfy

```text
kappa_D+kappa_V >= mu-o(1).                        (3)
```

```text
RECTANGULAR_PAIR_CAPACITY_BOUND_PROVED=true
SUBCRITICAL_RECTANGLE_CAPACITY_BRANCH_CLOSED=true
SURVIVING_RECTANGLE_PAIR_CAPACITY_EXPONENT_AT_LEAST_MU=true
```

## 3. Why this does not close all two-sided cells

The fixed positive primitive exponent cells allow both factor windows to have polynomial cardinality. In a full-width dyadic cell, one can have

```text
#D = B^(a+o(1)),
#V = B^(b+o(1)),
a,b>0,
```

so the pair capacity exponent `a+b` may exceed the required heavy exponent `mu`.

Thus the deterministic product-pair envelope is powerful only for subcritical interval-capacity cells. It does not by itself prove a fixed-power deficit on every principal rectangle.

```text
ALL_TWO_SIDED_RECTANGLES_CLOSED_BY_PAIR_CAPACITY=false
PRINCIPAL_RECTANGLE_SURVIVOR_RETAINS=true
```

## 4. Distinct products are the next possible deterministic loss

On a principal rectangle satisfying (3), the only remaining bare-envelope reduction before physical completion is the collision compression of the multiplication map:

```text
#P(D,V) < #D #V.
```

Define the distinct-product exponent

```text
#P(D,V)=B^(pi+o(1)),
0<=pi<=kappa_D+kappa_V.
```

A physical survivor necessarily has

```text
pi >= mu-o(1),                                      (4)
```

because `A_2s` is pointwise contained in the product support.

Equation (4) is not a theorem about typical multiplication tables; it is merely the necessary capacity condition on a surviving Stage14 cell.

```text
DISTINCT_PRODUCT_EXPONENT_PI_DEFINED=true
HEAVY_SURVIVAL_FORCES_PI_AT_LEAST_MU=true
MULTIPLICATION_TABLE_SAVING_IMPORTED=false
```

## 5. Receiver and H decision

The receiver remains the fixed-E two-sided ordinary ambient-capacity branch, now localized to rectangles whose pair capacity is principal. Before any new H audit, the next stage should rewrite the physical survival ledger directly against the distinct-product exponent `pi` and separate product-set compression from the residual physical-lift deficit.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fy
```

## Boundary

```text
STAGE14_4FX=COMPLETE_FIXED_E_RECTANGULAR_PRODUCT_PAIR_CAPACITY_LOCALIZATION
RECTANGULAR_PAIR_CAPACITY_BOUND_PROVED=true
SUBCRITICAL_RECTANGLE_CAPACITY_BRANCH_CLOSED=true
SURVIVING_RECTANGLE_PAIR_CAPACITY_EXPONENT_AT_LEAST_MU=true
DISTINCT_PRODUCT_EXPONENT_PI_DEFINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fy
```
