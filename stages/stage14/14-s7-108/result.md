# Stage14-s7-108 — polynomial outer-pair ordinary envelope to an exact fibered product image

## Status

`COMPLETE_POLYNOMIAL_OUTER_PAIR_MOVING_ORDINARY_ENVELOPE_TO_FIBERED_PRODUCT_IMAGE`

Consumes only merged theorem sources from batch-start main

```text
f9c3116fc82cacbcb494a055b40bb0daa825e19e
```

namely merged `Stage14-s7-105..107`, merged mainline `Stage14-4fw..4fy`, merged `Stage14-Work-bxX36`, and the already-merged q15 routing boundary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Synchronize the fixed-E realization without recharging it

Merged `4fw..4fy` and `Work-bxX36` supersede the fixed-E two-sided moving-divisor formulation.  On the same charged global/s packet, after freezing `E=E0`, the ordinary upper envelope is exactly

```text
P(D,V)={d*v:d in D,v in V},
```

and every subprincipal rectangle with

```text
#D#V <= B^(mu-eta+o(1))
```

is already discharged.  A surviving fixed-E two-sided cell is therefore the merged receiver

```text
FixedComplementaryDilationTwoSidedPrincipalRectangularDistinctProductCapacityVersusConditionalPhysicalLiftDeficit.
```

This stage merely consumes that theorem source.  It does not create a second count or recharge rectangular capacity.

```text
FIXED_E_MAINLINE_RECTANGULAR_RECEIVER_CONSUMED=true
FIXED_E_RECTANGULAR_CAPACITY_RECHARGED=false
```

## 2. Enter the polynomial-(E,m) realization

The remaining s-specific ordinary-envelope branch has

```text
E=B^(epsilon+o(1)), epsilon>0,
m=B^(kappa+o(1)), kappa>0,
n=E*m.
```

Merged s7-107 gives the pointwise upper envelope

```text
A_pair(E,m) <= O_ord,pair(E,m),
```

where the only separately named E-local factor is

```text
m_K(E)=1_{gcd(sqf(E),K_Z)=1}.
```

Freeze one already-charged root/exponent chart

```text
|Xr| in I_X,
|Yr| in I_Y,
```

with packet coefficients `alpha,beta` fixed on the heavy packet.  For each admissible integer `E` define

```text
D_E := Z_{>0} intersect sqrt(I_X/(alpha*E))
       intersect (the frozen first primitive exponent cell),

V_E := Z_{>0} intersect sqrt(I_Y/(beta*E))
       intersect (the frozen second primitive exponent cell).
```

The sets vary with `E`; no fixed-E identification is being made.

## 3. Exact fiberwise straightening

For an ordinary divisor candidate `d|m`, put

```text
v=m/d.
```

The transported root-window condition is exactly

```text
d in D_E,
v in V_E.
```

Equivalently, on the frozen chart,

```text
O_ord,pair(E,m)=1
```

iff

```text
m_K(E)=1
```

and there exist

```text
d in D_E,
v in V_E,
m=d*v.
```

Let

```text
E_K := {E on the frozen polynomial E-cell : m_K(E)=1}
```

and define the fibered multiplication image

```text
P_fib
 := {(E,d*v): E in E_K, d in D_E, v in V_E}.
```

Then pointwise and exactly

```text
O_ord,pair(E,m)=1  <=>  (E,m) in P_fib.          (1)
```

Consequently

```text
#supp(O_ord,pair)=#P_fib
 = sum_{E in E_K} #P(D_E,V_E),                    (2)
```

where

```text
P(D_E,V_E)={d*v:d in D_E,v in V_E}.
```

The equality in (2) uses the preserved first coordinate `E`: products from different E-fibers never collide as outer pairs `(E,m)`.

```text
POLYNOMIAL_PAIR_FIBERED_PRODUCT_IMAGE_EXACT=true
POLYNOMIAL_PAIR_SUPPORT_EQUALS_SUM_OF_FIBER_PRODUCT_SUPPORTS=true
CROSS_E_PRODUCT_COLLISIONS_EXIST=false
```

## 4. Why this is not the fixed-E rectangle

Merged Work-bxX36 correctly forbids silently importing the fixed-E rectangular straightening to the polynomial-E branch.  Here the correct object is a family

```text
E -> (D_E,V_E)
```

and not one fixed pair `(D,V)`.

What has been eliminated is only the apparently moving divisor interval: after retaining E as an outer coordinate, it is exactly a fibered multiplication image.  No Ford/Drappeau--Mounier theorem and no multiplication-table saving is charged.

```text
S_POLYNOMIAL_PAIR_RECTANGULAR_STRAIGHTENING_PROVED=false
S_POLYNOMIAL_PAIR_FIBERED_STRAIGHTENING_PROVED=true
LITERATURE_FIXED_POWER_SAVING_IMPORTED=false
```

## 5. H and next-step decision

The polynomial-pair arithmetic receiver is now exact enough for deterministic capacity localization, but not yet for an external theorem audit.  The next stage should compare

```text
sum_E #D_E#V_E
```

with the required heavy exponent `mu` and remove subcritical fibers before asking about multiplicative collisions.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_108_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-109
```

## Boundary

```text
STAGE14_S7_108=COMPLETE_POLYNOMIAL_OUTER_PAIR_MOVING_ORDINARY_ENVELOPE_TO_FIBERED_PRODUCT_IMAGE
FIXED_E_MAINLINE_RECTANGULAR_RECEIVER_CONSUMED=true
POLYNOMIAL_PAIR_FIBERED_PRODUCT_IMAGE_EXACT=true
POLYNOMIAL_PAIR_SUPPORT_EQUALS_SUM_OF_FIBER_PRODUCT_SUPPORTS=true
CROSS_E_PRODUCT_COLLISIONS_EXIST=false
S_POLYNOMIAL_PAIR_RECTANGULAR_STRAIGHTENING_PROVED=false
S_POLYNOMIAL_PAIR_FIBERED_STRAIGHTENING_PROVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_108_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-109
```
