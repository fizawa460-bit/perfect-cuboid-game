# Stage14-4fk — open the interior physical incidence weight in primitive-ratio coordinates

## Status

`COMPLETE_INTERIOR_PHYSICAL_WEIGHT_PULLBACK_TO_COMPLEMENTARY_E_AND_COUPLED_COMPLETION_BOOLEAN`

Consumes only merged theorem sources from batch-start main

```text
1cce848e748d6b02d7e878c6bd1b326e953bc98c
```

namely merged `Stage14-4fh..4fj`, merged `Stage14-s7-90..92`, merged `Stage14-Work-bsX31`, and merged `Stage14-q14` as a literature-routing boundary.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering heavy receiver

Merged 4fj leaves, on one fixed primitive ray/agreement packet and one interior radial exponent cell,

```text
I_int
 = sum_n sum_{L in C(n)} w_phys(n,L),
I_int >= B^(mu-o(1)),
```

where fixed `n` has only `B^o(1)` admissible `L` candidates and all radial endpoint geometry has already been discharged.

Merged s7-90..92 and Work-bsX31 identify exactly, on the same charged global packet,

```text
n=E*u*v,
gcd(u,v)=1,
L=E*u^2,
L/n=u/v,
E=n/(uv).
```

This is a coordinate change on the same incidences, not a second count.

## 2. Exact pullback of the incidence sum

Let `R_int(n)` be the already-charged interior primitive-ratio window corresponding to the 4fj interior `L` window. Then

```text
I_int
 = sum_n
   sum_{gcd(u,v)=1, uv|n, u/v in R_int(n)}
      w_ratio(n,u,v,E=n/(uv)).                    (1)
```

up to only the frozen `B^o(1)` packet labels already present in the merged coordinate equivalence. No support exponent changes in (1).

```text
FOUR_FJ_INCIDENCE_PULLBACK_TO_RATIO_EXACT=true
GLOBAL_S_COORDINATE_CHANGE_RECHARGED=false
FIXED_N_INNER_RATIO_FIBER=Bo1
```

## 3. Open the residual Boolean without assuming independence

Merged s7-90/91 states that the inherited squareclass/gcd conditions are transported through

```text
J1=sqf(E).
```

Collect precisely those complementary-dilation conditions into the Boolean

```text
m_E(E) in {0,1}.
```

It includes only conditions already known to be functions of `E` (equivalently `sqf(E)`) and frozen packet data. Do **not** move any mask into `m_E` unless merged provenance shows that dependence.

Collect every remaining canonical, root-origin, allocation and reverse/post-column completion condition that has not already been frozen or discharged into

```text
m_cpl(n,u,v,E) in {0,1}.
```

Then, by definition of conjunction,

```text
w_ratio(n,u,v,E)
 = m_E(E) * m_cpl(n,u,v,E).                       (2)
```

Equation (2) is an exact Boolean factorization of named predicates, not a probabilistic factorization and not an independence statement.

The full heavy incidence is therefore

```text
I_int
 = sum_n
   sum_{gcd(u,v)=1, uv|n, u/v in R_int(n)}
      m_E(n/(uv))
      m_cpl(n,u,v,n/(uv)).                         (3)
```

All original physical information remains present in (3).

```text
COMPLEMENTARY_E_LOCAL_MASK_EXPLICIT=true
COUPLED_CANONICAL_REVERSE_MASK_EXPLICIT=true
PHYSICAL_WEIGHT_BOOLEAN_FACTORING_USES_INDEPENDENCE=false
PHYSICAL_MASK_DROPPED=false
```

## 4. What is now exhausted

The following are already charged and cannot be extracted again from (3):

```text
radial endpoint removal,
reciprocal-window geometry,
L <-> (E,u,v) coordinate change,
fixed-n divisor/ratio multiplicity,
primitive gcd(u,v)=1 bookkeeping,
finite packet/chart labels.
```

Thus any new heavy saving must come from the arithmetic distribution of the actual Boolean weight in (3), not from counting coordinates again.

## 5. H decision

The weight has now been opened one layer, but a theorem target is still premature because `m_cpl` remains a coupled physical completion Boolean. Merged q14 explicitly forbids importing Ford's unrestricted divisor-window estimate before this physical measure is exposed.

The next internal step should dyadically split the primitive ratio variables and determine whether projective endpoint rays can be discarded or must remain separate from genuinely polynomial `(u,v)`.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fl
```

## Boundary

```text
STAGE14_4FK=COMPLETE_INTERIOR_PHYSICAL_WEIGHT_PULLBACK_TO_COMPLEMENTARY_E_AND_COUPLED_COMPLETION_BOOLEAN
FOUR_FJ_INCIDENCE_PULLBACK_TO_RATIO_EXACT=true
COMPLEMENTARY_E_LOCAL_MASK_EXPLICIT=true
COUPLED_CANONICAL_REVERSE_MASK_EXPLICIT=true
PHYSICAL_WEIGHT_BOOLEAN_FACTORING_USES_INDEPENDENCE=false
GLOBAL_S_COORDINATE_CHANGE_RECHARGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4fl
```
