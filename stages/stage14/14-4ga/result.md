# Stage14-4ga — principal rectangle unitary/coprime restriction has zero fixed-power support deficit

## Status

`COMPLETE_PRINCIPAL_RECTANGLE_UNITARY_COPRIME_SUPPORT_DEFICIT_EXHAUSTION`

Consumes batch-local `Stage14-4fz`, merged `Stage14-4fw..4fy`, merged `Stage14-s7-105..107`, and merged `Stage14-Work-bxX36`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Restore the actual unitary shadow inside the ordinary rectangle

On the fixed `E=E0` two-sided rectangle let

```text
D,V subset Z_{>0}
```

be the fixed primitive-factor integer windows from merged 4fw. After the already-charged finite boundary splitting, each is an integer interval on its frozen exponent cell.

Put

```text
Q:=#D #V=B^(kappa+o(1)),
kappa=kappa_D+kappa_V>=mu-o(1).
```

The actual bare unitary shadow is the product support

```text
P_prim(D,V)
 := {u*v : u in D, v in V, gcd(u,v)=1}.            (1)
```

Indeed for `m=uv`,

```text
u || m  <=>  u|m and gcd(u,m/u)=1
          <=>  gcd(u,v)=1.
```

Thus (1) is exactly the fixed-E two-sided bare unitary support before the canonical/reverse completion Boolean is imposed.

```text
FIXED_E_TWO_SIDED_UNITARY_SHADOW_EQUALS_COPRIME_RECTANGULAR_PRODUCT_SUPPORT=true
```

## 2. Coprime pairs retain the full pair-capacity exponent

Since `kappa>=mu>0`, at least one of `kappa_D,kappa_V` is positive on a principal surviving cell.

Suppose first

```text
kappa_V>0.
```

For each fixed `u in D`, elementary Möbius inversion on the integer interval `V` gives

```text
#{v in V:gcd(u,v)=1}
 = #V * phi(u)/u + O(tau(u)).                       (2)
```

All packet variables are polynomially bounded in `B`, so uniformly

```text
phi(u)/u = B^(-o(1)),
tau(u)=B^o(1).
```

Because `#V=B^(kappa_V+o(1))` with fixed positive exponent, the main term in (2) dominates the divisor-error at fixed-power scale. Hence uniformly after exponent localization,

```text
#{v in V:gcd(u,v)=1} >= #V * B^(-o(1)).
```

Summing over `u in D`,

```text
#{(u,v) in D x V:gcd(u,v)=1}
 >= Q * B^(-o(1)).                                  (3)
```

If `kappa_V=0`, principal capacity forces `kappa_D>0`; interchange `D` and `V` and apply the same argument. Therefore (3) holds on every principal rectangle.

```text
COPRIME_RECTANGULAR_PAIR_COUNT=Q_times_B_minus_o1
COPRIMALITY_FIXED_POWER_PAIR_DEFICIT=0
```

## 3. Pass from coprime pairs to distinct unitary products

For a fixed product `m`, the number of coprime representations `(u,v)` with `uv=m` is at most the total divisor count

```text
tau(m)=B^o(1).
```

Combining this with (3),

```text
#P_prim(D,V)
 >= Q * B^(-o(1)).                                  (4)
```

The reverse inequality `#P_prim(D,V)<=Q` is trivial. Hence

```text
#P_prim(D,V)=B^(kappa+o(1)).                         (5)
```

Batch-local 4fz also gives

```text
#P(D,V)=B^(kappa+o(1)).
```

Therefore the ordinary rectangular envelope and the actual unitary/coprime bare shadow have the same fixed-power support exponent on every principal fixed-E two-sided rectangle.

This is only a fixed-power support comparison on this exact rectangular Stage14 packet. It is not promoted to a global bounded-distortion theorem for arbitrary localized unitary-divisor ensembles.

```text
FIXED_E_RECTANGULAR_UNITARY_SUPPORT_EXPONENT=kappa
FIXED_E_RECTANGULAR_ORDINARY_SUPPORT_EXPONENT=kappa
UNITARY_TO_ORDINARY_FIXED_POWER_SUPPORT_DISTORTION=0
Q15_UNITARY_BOUNDED_DISTORTION_GLOBAL_CLAIMED=false
```

## 4. Physical lift now means canonical/reverse completion only at fixed-power level

Merged 4fy defined `delta_lift` from the ordinary product support to the physical support and allowed it to contain both

```text
unitary/coprime recovery
and
canonical/reverse physical completion.
```

Equation (5) proves that unitary/coprime recovery contributes zero fixed-power exponent on the principal rectangle. Thus any positive fixed-power `delta_lift` must come from the residual physical completion mechanism, up to exponent-zero finite/divisor fibers already charged once.

The next stage freezes the corrected survival ledger and minimal receiver.

```text
UNITARY_COPRIME_COMPONENT_OF_DELTA_LIFT_FIXED_POWER_EXPONENT=0
RESIDUAL_FIXED_POWER_LIFT_DEFICIT_IS_PHYSICAL_COMPLETION=true
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4gb
```

## Boundary

```text
STAGE14_4GA=COMPLETE_PRINCIPAL_RECTANGLE_UNITARY_COPRIME_SUPPORT_DEFICIT_EXHAUSTION
FIXED_E_TWO_SIDED_UNITARY_SHADOW_EQUALS_COPRIME_RECTANGULAR_PRODUCT_SUPPORT=true
COPRIME_RECTANGULAR_PAIR_COUNT=Q_times_B_minus_o1
UNITARY_TO_ORDINARY_FIXED_POWER_SUPPORT_DISTORTION=0
UNITARY_COPRIME_COMPONENT_OF_DELTA_LIFT_FIXED_POWER_EXPONENT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gb
```
