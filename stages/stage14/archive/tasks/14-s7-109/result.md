# Stage14-s7-109 — polynomial fibered product: deterministic pair-capacity threshold localization

## Status

`COMPLETE_POLYNOMIAL_FIBERED_PRODUCT_PAIR_CAPACITY_THRESHOLD_LOCALIZATION`

Consumes batch-local `Stage14-s7-108` and merged `Stage14-Work-bxX36`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact ambient capacity from the fibered image

Stage14-s7-108 gives

```text
#P_fib
 = sum_{E in E_K} #P(D_E,V_E)
 <= sum_{E in E_K} #D_E #V_E.                    (1)
```

The inequality is only the surjectivity of

```text
D_E x V_E -> P(D_E,V_E),
(d,v) -> d*v
```

inside each fixed E-fiber.

No multiplication-table theorem, average divisor theorem, or physical-completion estimate is used in (1).

```text
FIBERED_PAIR_CAPACITY_BOUND_PROVED=true
FIBERED_PAIR_CAPACITY_USES_ONLY_SURJECTIVITY=true
```

## 2. Freeze one cardinality cell at B^o(1) cost

The integer cardinalities `#D_E` and `#V_E` vary with E.  Partition the admissible E-fibers into logarithmically many bins according to dyadic cardinality ranges.  There are only `B^o(1)` such bins.

On one bin `E_*` carrying principal support, write

```text
#E_* = B^(kappa_E+o(1)),
#D_E <= B^(kappa_D+o(1)),
#V_E <= B^(kappa_V+o(1))
```

uniformly for `E in E_*`, with `kappa_E,kappa_D,kappa_V>=0`.

The known kernel-gcd mask is already built into `E_*`; its zero fixed-power deficit from merged s7-104 is not recharged.

Equation (1) gives the absolute ambient capacity

```text
#P_fib(E_*)
 <= B^(kappa_E+kappa_D+kappa_V+o(1)).             (2)
```

```text
FIBER_CARDINALITY_LOCALIZATION_COST=Bo1
KNOWN_KERNEL_GCD_MASK_RECHARGED=false
FIBERED_AMBIENT_CAPACITY_EXPONENT=kappa_E_plus_kappa_D_plus_kappa_V
```

## 3. Discharge every subcritical fiber-cardinality cell

A surviving physical realization requires

```text
#supp(A_pair on E_*) >= B^(mu-o(1)).
```

Since

```text
supp(A_pair) subseteq P_fib(E_*),
```

Work-bxX36's ambient-capacity threshold principle closes every cell for which some fixed `eta>0` satisfies

```text
kappa_E+kappa_D+kappa_V <= mu-eta.                (3)
```

Hence every surviving polynomial-E outer-pair cell must satisfy

```text
kappa_E+kappa_D+kappa_V >= mu-o(1).               (4)
```

Call such a cell a **principal fibered product cell**.

```text
SUBCRITICAL_FIBERED_PAIR_CAPACITY_BRANCH_CLOSED=true
SURVIVING_FIBERED_PAIR_CAPACITY_EXPONENT_AT_LEAST_MU=true
PRINCIPAL_FIBERED_PRODUCT_CELL_DEFINED=true
```

## 4. This is a capacity threshold, not a density theorem

The inequality (2) may be far from sharp because the multiplication map can have many collisions inside individual E-fibers.  Conversely, on a near-injective fiber the distinct-product support may be comparable to `#D_E#V_E` up to only subpolynomial factors.

Therefore (4) is only a necessary condition for survival.  It does not imply that the actual distinct outer-pair support reaches exponent `mu`.

No saving is taken from:

```text
- typical multiplication-table compression;
- average divisor density;
- unitary versus ordinary distortion;
- cross-E collisions, which do not exist for outer pairs;
- physical completion.
```

```text
GENERIC_MULTIPLICATION_TABLE_SAVING_IMPORTED=false
GENERIC_DIVISOR_DENSITY_RECHARGED=false
CROSS_E_COLLISION_SAVING_RECHARGED=false
```

## 5. H and next-step decision

The next stage should place the physical support directly under the actual distinct fibered product image, define its exponent, and separate fiberwise multiplicative compression from conditional physical lift.  That is still an internal receiver normalization, not an external sH target.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_109_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-110
```

## Boundary

```text
STAGE14_S7_109=COMPLETE_POLYNOMIAL_FIBERED_PRODUCT_PAIR_CAPACITY_THRESHOLD_LOCALIZATION
FIBERED_PAIR_CAPACITY_BOUND_PROVED=true
FIBER_CARDINALITY_LOCALIZATION_COST=Bo1
SUBCRITICAL_FIBERED_PAIR_CAPACITY_BRANCH_CLOSED=true
SURVIVING_FIBERED_PAIR_CAPACITY_EXPONENT_AT_LEAST_MU=true
PRINCIPAL_FIBERED_PRODUCT_CELL_DEFINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_109_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-110
```
