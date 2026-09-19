# MB104 — shallow composition scan A/B after 100-commit review — 2026-09-19

Status: **PRE-AUDIT SHALLOW CROSS-ROUTE SCAN / NO DEEP ROUTE PROMOTED / NO CREDIT**

## Scope

Compare two cross-route compositions on the sole dangerous support 000707000f0f without duplicating
the active 32-01 fibration search.

A. six relative polars + conductor/Jacobian/Fitting globalization;
B. six projection orders + cuboid relations as a local branch conductor/contact bound.

## A. Piene conductor-Jacobian identity is source-valid for the local receiver

Let C be the hypothetical integral Cartier curve on the smooth cuboid resolution and
nu:E->C its normalization.

Because C is Cartier in a smooth surface, C is a local complete intersection curve and nu is finite.

Piene's theorem for a finite desingularization of a local complete intersection gives

```
J_C O_E = I_nu * c O_E,
```

where

```
J_C  = Jacobian ideal of C,
I_nu = ramification/Fitting ideal of the normalization,
c    = conductor ideal.
```

This is exactly the local ideal-theoretic shape needed by the retained conductor/polar discussion.

For a local equation f=0 on the smooth surface and a local fibration coordinate h_j, the relative
polar is

```
df wedge dh_j.
```

The six imported fibration differentials span the cotangent space at every smooth non-node point.
Therefore locally two of the dh_j form a basis, and the six relative polar generators generate the
same Jacobian ideal J_C.

Thus the earlier source gate can be sharpened to:

```
six polar ideal = J_C locally on the smooth-interior conductor support,
and
J_C O_E = conductor * normalization-ramification ideal.
```

The common normalization ramification divisor remains

```
A=gcd(R_0,...,R_5),
deg A<=80l.
```

So on E the common polar divisor is exactly of the expected form

```
Delta + A.
```

### Coefficient check

This is structurally exact, but it does not itself produce a finite-l inequality.

For either minimum-degree fibration on 000707,

```
deg R_j=80l,
deg(Delta+R_j)=336l^2+192l.
```

A pairwise ambient polar-intersection bound has leading quadratic coefficient 336, while
```
deg Delta=336l^2+112l.
```

Hence the leading coefficient ties rather than beats the conductor different.

No shallow two-polar Bezout/Chern count yields a contradiction.

Disposition:

```
A = SOURCE-VALID STRUCTURAL ADAPTER,
but NO SHALLOW COEFFICIENT CLOSER.
Do not launch a long Fitting/syzygy computation yet.
```

A future revival needs a genuinely stronger consequence of the six-generator Jacobian ideal,
such as an ambient syzygy/degeneracy theorem that uses all six cuboid relations simultaneously.

## B. Ramification-order-only branch bound is impossible

Differential spanning alone cannot bound branch delta by the sum of the ramification orders of a
fixed spanning family.

Local counterexample on a smooth surface:

```
x=t^2,
y=t^(2k+1).
```

This irreducible plane branch has

```
delta=k.
```

Take two local measuring functions

```
h1=x,
h2=x+y.
```

Their differentials

```
dh1=dx,
dh2=dx+dy
```

span the cotangent space.

But along the branch

```
ord(d h1)=1,
ord(d h2)=1
```

for every k, while delta=k is unbounded.

The same example can be padded by additional fixed functions whose linear parts are generic
combinations with nonzero x coefficient.  Hence no inequality of the form

```
delta_q <= C * sum_j ord_q(dg_j)
```

can follow from finite differential spanning alone.

This does not invalidate the cuboid six-map route.  It identifies the missing datum:

```
high delta is hidden in high-order cancellation between projection functions.
```

In the example,

```
h2-h1=y=t^(2k+1)
```

carries the missing characteristic exponent even though h1 and h2 separately have small
ramification.

Therefore the viable B-route must control **pairwise/multilinear jet cancellation**, not only the
individual ramification divisors.

Disposition:

```
B1 ramification-order inequality = CLOSED.
B2 simultaneous jet-cancellation / difference-resultant route = LIVE SHALLOW.
```

## Cross-route conclusion

Neither A nor B earns deep allocation yet.

The 100-commit reuse map is refined as follows:

```
KEEP:
  Piene local ideal adapter,
  six-polar generation of J_C,
  common residual A with deg<=80l.

CLOSE:
  two-polar coefficient-only Bezout,
  any branch-delta bound using only individual ramification orders.

NEXT SHALLOW TARGET:
  exploit bounded-degree algebraic relations among the six cuboid maps to control
  high-order cancellations such as h_i-h_j / cross-ratios / 2x2 minors.
```

This is distinct from the 32-01 fibration-classification search: it treats the existing six maps as
fixed analytic coordinates and studies their mutual jets on the hypothetical carrier.

## Firewalls

```
piene_local_adapter_source_valid=true
six_polars_generate_local_jacobian=true
two_polar_coefficient_closer=false
ramification_order_only_delta_bound=false
jet_cancellation_route_live=true
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
