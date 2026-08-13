# Stage14-4fz — rectangular multiplication map has only divisor-many fibers

## Status

`COMPLETE_PRINCIPAL_RECTANGLE_MULTIPLICATION_COLLISION_COMPRESSION_EXHAUSTION`

Consumes merged `Stage14-4fw..4fy`, merged `Stage14-s7-105..107`, merged `Stage14-Work-bxX36`, and latest merged main

```text
f9c3116fc82cacbcb494a055b40bb0daa825e19e.
```

Only merged artifacts are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter one principal fixed-E rectangle

Merged 4fy leaves fixed positive-integer factor windows `D,V` with

```text
Q:=#D #V = B^(kappa+o(1)),
kappa=kappa_D+kappa_V>=mu-o(1),
```

and the ordinary product support

```text
P(D,V):={d*v:d in D,v in V}.
```

Write

```text
#P(D,V)=B^(pi+o(1)).
```

The previous receiver allowed a possible fixed-power gap `kappa-pi` caused by collisions of the multiplication map.

## 2. Uniform product-fiber bound

For each product value `m` define

```text
r(m):=#{(d,v) in D x V : d*v=m}.
```

Every ordered pair `(d,v)` counted by `r(m)` is determined by an ordinary positive divisor `d|m`, so

```text
r(m)<=tau(m).
```

All Stage14 variables in the present packet are polynomially bounded in `B`. Hence the standard divisor bound gives uniformly

```text
tau(m)=B^o(1).
```

Therefore

```text
Q=sum_m r(m)
 <= #P(D,V) * B^o(1),
```

while trivially `#P(D,V)<=Q`. Consequently

```text
#P(D,V)=Q*B^o(1)=B^(kappa+o(1)),
pi=kappa.                                            (1)
```

Thus the rectangular multiplication image is fixed-power near-injective automatically. No multiplication-table theorem or Ford-type divisor theorem is needed.

```text
RECTANGULAR_PRODUCT_FIBER_BOUND=Bo1
RECTANGULAR_DISTINCT_PRODUCT_EXPONENT_EQUALS_PAIR_CAPACITY=true
DISTINCT_PRODUCT_FIXED_POWER_COMPRESSION_EXPONENT=0
```

## 3. Collision energy is forced to diagonal exponent

Define multiplicative collision energy

```text
E_x(D,V)
 := #{(d1,v1,d2,v2) in (D x V)^2 : d1*v1=d2*v2}
 = sum_m r(m)^2.
```

Using `max_m r(m)=B^o(1)` and `sum_m r(m)=Q`,

```text
Q <= E_x(D,V) <= Q*B^o(1).
```

Hence

```text
E_x(D,V)=B^(kappa+o(1)).                             (2)
```

There is no separate polynomial high-collision branch. In the exponent ledger, off-diagonal multiplicative coincidences cannot create a positive fixed-power compression of `P(D,V)`.

```text
MULTIPLICATIVE_COLLISION_ENERGY_EXPONENT=kappa
POLYNOMIAL_COLLISION_EXCESS_BRANCH_EXISTS=false
NEAR_INJECTIVE_PRODUCT_SUPPORT_FORCED=true
```

## 4. Consequence for the 4fy survival budget

Merged 4fy wrote

```text
pi-delta_lift>=mu.
```

By (1), this is now exactly

```text
kappa-delta_lift>=mu.                               (3)
```

Thus mechanism P from 4fy — fixed-power distinct-product compression — is exhausted. Any remaining fixed-power loss from the ordinary rectangular envelope to the physical support lies in `delta_lift`.

At this stage `delta_lift` still bundles the unitary/coprime-complement restriction together with canonical/reverse completion. The next stage must determine whether the unitary restriction itself can contribute a fixed-power deficit on a principal rectangle.

```text
DISTINCT_PRODUCT_CAPACITY_MECHANISM_EXHAUSTED=true
PHYSICAL_LIFT_DEFICIT_RETAINS=true
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4ga
```

## Boundary

```text
STAGE14_4FZ=COMPLETE_PRINCIPAL_RECTANGLE_MULTIPLICATION_COLLISION_COMPRESSION_EXHAUSTION
RECTANGULAR_PRODUCT_FIBER_BOUND=Bo1
RECTANGULAR_DISTINCT_PRODUCT_EXPONENT_EQUALS_PAIR_CAPACITY=true
MULTIPLICATIVE_COLLISION_ENERGY_EXPONENT=kappa
POLYNOMIAL_COLLISION_EXCESS_BRANCH_EXISTS=false
DISTINCT_PRODUCT_CAPACITY_MECHANISM_EXHAUSTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4ga
```
