# Stage14-Work-btX32 receiver / weight-location matrix

This matrix records only merged sources consumed by `Stage14-Work-btX32`.

| Route | Polynomial outer coordinate | Inner selector | Physical weight location | Current status |
|---|---|---|---|---|
| global/main heavy, fixed `E=E0` | `m=n/E0` | unitary divisor `u||m` in transported short interval | residual canonical/reverse Boolean depends on `(m,u,m/u,E0)` | live |
| global/main heavy, polynomial `E` | `(E,m)` with `n=Em` | unitary divisor `u||m` in transported short interval | `m_E(E) m_cpl(Em,u,m/u,E)` remains coupled | live |
| s heavy | same `(n,q,u,E=n/q)` weighted-unitary packet | `q|n`, `u||q` in `U_phys(n,q)` | `W_unit(n,q,u)` depends on inner candidate | same packet as global; do not multiply |
| fixed-U | scalar norm `n` | primes `ell<=X_U/n` in fixed projective class `q_*` | cofactor physical multiplicity is outer-only `W_{c_*}(n)` | live |

## Same-packet locks

```text
GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true
MAINLINE_4FM_E_SCALE_SPLIT_APPLIES_TO_SAME_S7_95_PACKET=true
GLOBAL_S_WEIGHTED_UNITARY_COUNTS_MULTIPLICABLE=false
```

The mainline `4fm` split is a refinement of the exact same global/s heavy incidence exposed by `s7-95`; it is not a second independent saving source.

## Common abstraction

Both routes admit a broad form

```text
sum_x sum_{y in S(x)} w(x,y)
```

with polynomial outer support and reciprocal dependence of `S(x)` on the outer variable.

```text
COMMON_NONNEGATIVE_WEIGHTED_RECIPROCAL_SELECTOR_TEMPLATE_PROVED=true
```

The abstraction stops there. On global/s the retained canonical/reverse physical Boolean remains inner-dependent. On fixed-U, after `t132`, the cofactor physical weight is a nonnegative outer function `W_{c_*}(n)` and the inner object is a fixed-projective-class prime count.

```text
PHYSICAL_WEIGHT_LOCATION_ASYMMETRY_PROVED=true
GLOBAL_S_INNER_DEPENDENT_PHYSICAL_WEIGHT_REMAINS=true
FIXED_U_PHYSICAL_COFACTOR_WEIGHT_OUTER_N_ONLY=true
```

## Adapter boundary

A direct adapter at the current level would need a measure-preserving identification of

```text
u||m or (q|n,u||q)
```

with

```text
prime ell in fixed projective class q_*
```

and would also need to preserve the different locations of the physical weights.

No such finite-fiber map, baseline comparison, or weight factorization is merged.

```text
DIRECT_WEIGHTED_UNITARY_TO_FIXED_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false
COMMON_ARITHMETIC_INNER_SELECTOR_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

This is a current-coordinate no-go only; later arithmetic opening may change the receiver.

## Literature/H routing

```text
Q14_GLOBAL_S_ONLY_ROUTING_RETAINED=true
TH29_FIXED_U_NEGATIVE_BOUNDARY_RETAINED=true
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_NEEDED=false
```

The broad mainline H flag refers to the pre-existing non-heavy H targets. No new H is opened for the present weighted-unitary or fixed-class prime receivers.

## Next

```text
NEXT_INTEGRATED_TARGET=OuterInnerPhysicalWeightFactorizationAdapterOrNoGo
NEXT_REVISIT_CONDITION=approximately merged 4fp plus s7-98 plus t135, or earlier material weight-factorization/adapter/H/exponent trigger
```