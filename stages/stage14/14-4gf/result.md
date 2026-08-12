# Stage14-4gf — explicit homogeneous reciprocal-seed construction test

## Status

`COMPLETE_Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST_WITH_SEEDED_SEEDLESS_SPLIT`

Consumes merged `Stage14-4ge`, merged `Stage14-Work-bzX38`, merged `Stage14-q17`, and latest batch-start main

```text
007ff032d7f757035029a04d6065b605c8a65ef0
```

Only merged artifacts are theorem sources. The auto-pilot commits after the mathematical X/q merge are operational only and do not alter the Stage14 arithmetic receiver.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the exact reciprocal selector

On one fixed-`E=E0`, fixed-ray, fixed-agreement principal rectangle, merged 4ge gives

```text
R_prim={(u,v):u in D,v in V,gcd(u,v)=1},
#R_prim=B^(kappa+o(1)),
```

and the reciprocal support

```text
T_rec={(u,v) in R_prim: Omega_rec(u,v) nonempty}.
```

Write

```text
m=u*v,
A_x:=H0*x,
A_y:=H0*y,
C0:=4*r*s*epsilon_k.
```

The bare reciprocal equations are

```text
p*c=A_x*m,
q*d=A_y*m,
F_-*F_+=C0*p*q,
F_+ + F_- == 0 (mod 2U),
F_+ - F_- == 0 (mod 2V),
```

plus the already-frozen positivity, parity, quotient-cell and endpoint-small divisibility filters.

## 2. The natural homogeneous seed

A **scale-compatible homogeneous reciprocal seed** is fixed packet data

```text
(P,Q,G_-,G_+)
```

such that

```text
P | A_x,
Q | A_y,
0<G_-<G_+,
G_-*G_+=C0*P*Q,
G_+ + G_- == 0 (mod 2U),
G_+ - G_- == 0 (mod 2V),
```

and the scaled tuple below obeys the inherited endpoint/parity/quotient-cell filters on one of the finitely many already-charged physical subcells.

For every `(u,v)` in that subcell set

```text
m=u*v,
p=P*m,
q=Q*m,
c=A_x/P,
d=A_y/Q,
F_-=G_-*m,
F_+=G_+*m,
a=((G_++G_-)/(2U))*m,
b=((G_+-G_-)/(2V))*m.
```

Then identically

```text
p*c=A_x*m,
q*d=A_y*m,
F_-*F_+=C0*p*q,
```

and both CRT congruences hold because their fixed coefficient versions hold before multiplication by `m`. Positivity is inherited from `0<G_-<G_+`. The endpoint-small divisibility and finite two-primary restrictions are part of the scale-compatible seed predicate and are not dropped.

Therefore every pair in the seed-compatible physical subcell has an explicit member of `Omega_rec(u,v)`.

```text
HOMOGENEOUS_RECIPROCAL_SEED_CONSTRUCTION_EXACT=true
Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST=COMPLETE
```

## 3. Seeded packets have zero reciprocal support deficit

The number of possible fixed seeds is subpolynomial:

```text
#P choices <= tau(A_x)=B^o(1),
#Q choices <= tau(A_y)=B^o(1),
#(G_-,G_+) choices <= tau(C0*P*Q)=B^o(1).
```

Finite parity/chart refinement is also `B^o(1)`. Hence if a principal packet has a scale-compatible seed whose compatible subcell carries exponent `kappa`, then

```text
#T_rec=B^(kappa+o(1)),
delta_rec=0
```

at fixed-power scale.

This is an unconditional branch-local no-go for extracting a reciprocal-CRT saving on a seeded packet.

```text
SEEDED_RECIPROCAL_PACKET_FULL_EXPONENT=true
SEEDED_RECIPROCAL_DEFICIT_FIXED_POWER=0
```

## 4. Absence of this seed is not a sparsity theorem

The seed above is a sufficient construction, not an exhaustive parameterization of `Omega_rec`. A valid witness may allocate the moving prime powers of `m` nontrivially among

```text
p versus c,
q versus d,
F_- versus F_+.
```

Consequently

```text
no homogeneous seed
```

does **not** imply `Omega_rec(u,v)=empty`, and it does not imply any fixed-power upper bound for `T_rec`.

This point is essential: q17's literature radar found no theorem allowing us to convert failure of a preferred explicit construction into support sparsity.

```text
SEEDLESS_IMPLIES_RECIPROCAL_SPARSITY=false
EXPLICIT_CONSTRUCTION_FAILURE_RECHARGED_AS_SAVING=false
```

## 5. Exact next obligation

The seed test cleanly discharges one possible direct full-density mechanism. On a seedless survivor the only honest next internal step is to normalize arbitrary witnesses by removing every prime supported on the frozen packet coefficients. This isolates which moving prime-power allocations of `m` actually enter the two divisor layers and the fixed `(U,V)` CRT congruences.

No new heavy H is opened yet because this normalization is elementary and must precede an external divisor-correlation audit.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4gg
```

## Boundary

```text
STAGE14_4GF=COMPLETE_Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST_WITH_SEEDED_SEEDLESS_SPLIT
HOMOGENEOUS_RECIPROCAL_SEED_CONSTRUCTION_EXACT=true
SEEDED_RECIPROCAL_PACKET_FULL_EXPONENT=true
SEEDED_RECIPROCAL_DEFICIT_FIXED_POWER=0
SEEDLESS_IMPLIES_RECIPROCAL_SPARSITY=false
Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST=COMPLETE
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gg
```