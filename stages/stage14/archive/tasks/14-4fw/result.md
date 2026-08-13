# Stage14-4fw — fixed-E moving ordinary-divisor interval straightens to a rectangular product set

## Status

`COMPLETE_FIXED_E_MOVING_DIVISOR_INTERVAL_TO_RECTANGULAR_PRODUCT_SUPPORT`

Consumes merged `Stage14-4fv`, merged `Stage14-s7-102..104`, merged `Stage14-q15`, and merged `Stage14-Work-bwX35` from latest main

```text
5884e0ec4f9fc85589e00edafbdc6cda3c67bc2d.
```

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the fixed-E two-sided ordinary upper envelope

Freeze the already-charged exact complementary dilation

```text
E=E0,
```

and one two-sided positive primitive exponent cell. Merged 4fu gives the legal pointwise upper envelope

```text
A_2s(m) <= B_2s(m) <= O_2s(m),
```

where

```text
O_2s(m)=1
```

iff there exists an ordinary divisor `d|m` in the transported moving interval

```text
U_E0(m)=sqrt(m*R_int(E0*m))
```

with both `d` and `m/d` on the frozen positive primitive/root cells.

## 2. Recover the two fixed primitive-factor windows

On fixed `E0`, the exact primitive-ratio coordinates are

```text
n=E0*u*v,
m=u*v,
|Xr|=alpha*E0*u^2,
|Yr|=beta*E0*v^2,
```

for fixed positive packet coefficients `alpha,beta`. Freeze one physical root-size chart

```text
|Xr| in I_X=[X_-,X_+],
|Yr| in I_Y=[Y_-,Y_+].
```

After intersecting with the already-frozen positive exponent cells define the fixed integer sets

```text
D := Z_{>0} intersect sqrt(I_X/(alpha*E0)),
V := Z_{>0} intersect sqrt(I_Y/(beta*E0)).
```

All finite chart/orientation labels are already charged once.

For an arbitrary outer integer `m`, the condition that a candidate divisor `d` and its complementary factor lie in the two physical primitive windows is exactly

```text
d in D,
m/d in V.
```

Equivalently the moving divisor interval is merely

```text
D intersect (m/V).
```

Thus the dependence of the interval center on `m` is not a new arithmetic degree of freedom.

```text
FIXED_E_PRIMITIVE_FACTOR_WINDOWS_FIXED=true
MOVING_DIVISOR_INTERVAL_EQUALS_D_INTERSECT_m_OVER_V=true
```

## 3. Exact product-set straightening

Let

```text
P(D,V):={d*v : d in D, v in V}.
```

Then pointwise

```text
O_2s(m)=1  <=>  m in P(D,V).                    (1)
```

Indeed, `d|m`, `d in D`, and `m/d in V` are equivalent to `m=dv` with `(d,v) in D x V`.

Therefore

```text
sum_m O_2s(m)=#P(D,V),                           (2)
```

on the frozen outer exponent cell, up to only already-charged boundary labels. No Ford density theorem, multiplicity estimate, or physical independence is used in (1)--(2).

This resolves the q15/bwX35 **moving interval normalization** algebraically:

```text
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false
FIXED_E_ORDINARY_SHADOW_IS_RECTANGULAR_DISTINCT_PRODUCT_SET=true
```

It does **not** prove that the product set is fixed-power small.

## 4. What remains distinct from the physical support

The product set is only a legal ordinary upper envelope. The physical packet still requires the original unitary partition and canonical/reverse completion conditions. Hence

```text
A_2s(m) <= 1_{m in P(D,V)}
```

but no lower comparison or bounded distortion is claimed.

```text
ORDINARY_PRODUCT_SET_USED_AS_UPPER_ENVELOPE_ONLY=true
UNITARY_ORDINARY_BOUNDED_DISTORTION_PROVED=false
PHYSICAL_COMPLETION_DROPPED_ONLY_IN_UPPER_BOUND_DIRECTION=true
```

## 5. Receiver and H decision

The arithmetic content has been straightened, but the same absolute-capacity mechanism from 4fv remains: determine whether the distinct product set `P(D,V)` is too small to carry `B^(mu-o(1))` heavy mass.

The next stage must first compare the elementary rectangular pair capacity `#D #V` with the required heavy exponent `mu`; theorem machinery is unnecessary on subcritical rectangles.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fx
```

## Boundary

```text
STAGE14_4FW=COMPLETE_FIXED_E_MOVING_DIVISOR_INTERVAL_TO_RECTANGULAR_PRODUCT_SUPPORT
FIXED_E_ORDINARY_SHADOW_IS_RECTANGULAR_DISTINCT_PRODUCT_SET=true
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false
ORDINARY_PRODUCT_SET_USED_AS_UPPER_ENVELOPE_ONLY=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fx
```
