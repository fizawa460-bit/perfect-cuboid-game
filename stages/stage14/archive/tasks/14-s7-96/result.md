# Stage14-s7-96 — synchronize weighted-unitary packet and factor physical weight by complementary dilation

## Status

`COMPLETE_WEIGHTED_UNITARY_PACKET_SYNCHRONIZATION_AND_E_LOCAL_WEIGHT_FACTORIZATION`

Consumes merged `Stage14-s7-93..95`, merged mainline `Stage14-4fk..4fm`, merged `Stage14-Work-btX32`, and latest main

```text
43c2beeda0c9c5af2154d6deca5912d5be9e3ab2.
```

Only merged artifacts are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering s-route incidence

Merged s7-95 gives exactly

```text
I_unit
 = sum_n
   sum_{q|n}
   sum_{u||q, u in U_phys(n,q)}
      W_unit(n,q,u),

E=n/q,
v=q/u,
```

where `u||q` means `u|q` and `gcd(u,q/u)=1` and a surviving heavy packet requires

```text
I_unit >= B^(mu-o(1)).
```

Merged 4fk and Work-btX32 prove that this is the same charged global heavy packet as the mainline physical incidence, not a second count.

```text
GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true
GLOBAL_S_WEIGHTED_UNITARY_COUNTS_MULTIPLICABLE=false
```

## 2. Exact location factorization of the Boolean weight

Merged 4fk opens the physical Boolean into

```text
W_unit(n,q,u)
 = m_E(E) * m_cpl(n,u,q/u,E),
E=n/q.
```

Here `m_E(E)` contains only predicates already proved to depend on the complementary dilation and frozen packet data. In particular the s7-93 condition

```text
gcd(sqf(E),K_Z)=1
```

belongs to `m_E`. Every canonical, root-origin, allocation, reverse/post-column completion predicate not proved to depend on `E` alone remains in `m_cpl`.

This is a factorization of a conjunction of named predicates. It is not an independence assertion.

```text
E_LOCAL_PHYSICAL_MASK=m_E
INNER_DEPENDENT_CANONICAL_REVERSE_MASK=m_cpl
PHYSICAL_WEIGHT_BOOLEAN_FACTORING_USES_INDEPENDENCE=false
PHYSICAL_MASK_DROPPED=false
```

## 3. Consume the merged E-scale split without recharging it

Merged 4fm applies to the identical s7-95 packet and splits

```text
(A) E=B^o(1),
(B) E=B^(epsilon+o(1)), epsilon>0.
```

This split is now imported into the s route as theorem source. It is not a new s saving and is not counted twice.

On (A), exact `E` has only `B^o(1)` possible values and one surviving `E=E0` may be frozen. On (B), `E` is a genuine polynomial outer coordinate and cannot be frozen at exponent-zero cost.

```text
MAINLINE_4FM_E_SCALE_SPLIT_CONSUMED_BY_S=true
E_SCALE_SPLIT_RECHARGED=false
SUBPOLYNOMIAL_E_EXACT_VALUE_FREEZABLE=Bo1
POLYNOMIAL_E_FREEZE_ALLOWED=false
```

## 4. Receiver and H decision

This stage synchronizes the s packet with the stronger merged mainline/Work description; it does not yet materially change the merged receiver. The next internal step isolates the fixed-`E` branch and determines exactly what the remaining canonical/reverse Boolean can and cannot contribute.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_96_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_96=COMPLETE_WEIGHTED_UNITARY_PACKET_SYNCHRONIZATION_AND_E_LOCAL_WEIGHT_FACTORIZATION
GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true
E_LOCAL_PHYSICAL_MASK=m_E
INNER_DEPENDENT_CANONICAL_REVERSE_MASK=m_cpl
MAINLINE_4FM_E_SCALE_SPLIT_CONSUMED_BY_S=true
E_SCALE_SPLIT_RECHARGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_96_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-97
```