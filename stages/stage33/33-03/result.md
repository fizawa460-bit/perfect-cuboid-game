# Stage33-03 — BR0B UPic absolute-Galois production state

```text
STAGE33_UNIT=33-03
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0B=OPEN
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=false
UPIC_V4_INTEGRAL_ACTION_EXACT=true
UNIT_LATTICE_V4_ACTION_EXACT=true
PICU_INTEGRAL_V4_ACTION_EXACT=true
ODD_PRIMARY_BR0B_PARAMETRICALLY_COMPLETE=true
FINITE_V4_HYPERCOHOMOLOGY_EXACT=true
FINITE_V4_H2=(Z/2)^33
FINITE_V4_H1_UPIC=0
FINITE_D2_01_RANK=2
FINITE_D2_11_RANK=2
FINITE_TRANSGRESSION_AMBIGUITY=0
ABSOLUTE_TWO_PRIMARY_LEFT_FILTRATION_SHAPE_EXACT=true
ABSOLUTE_TWO_PRIMARY_LEFT_FILTRATION_INFINITE=true
ABSOLUTE_TWO_PRIMARY_RIGHT_TRANSGRESSION_COMPLETE=false
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact finite and odd-primary inputs

The hostile-audited compactification complex has unit lattice

```text
U_D = ker(Div_D -> Pic(Sbar)) ~= Z^14,
```

and both generators of `Gal(Q(i,sqrt(2))/Q) ~= V4` act trivially on it.  The free rank-six part of

```text
Pic(Ubar) ~= Z^6 + (Z/2)^2
```

has V4 character multiplicities

```text
(+,+)=0, (+,-)=3, (-,+)=2, (-,-)=1,
```

while the full `(Z/2)^2` torsion subgroup is jointly fixed.  The Stage32 primitive Picard basis and Testa--Stoll Picard basis are connected by a unimodular matrix of determinant `-1`.

For odd primary torsion,

```text
H^2(Q,UPic(Ubar))_odd
 ~= Hom_cont(G_Q,Q/Z)_odd^14.
```

The actual two-term complex `[Div_D -> Pic(Sbar)]` has exact finite-quotient hypercohomology

```text
H^2(V4,UPic(Ubar)) ~= (Z/2)^33.
```

## Exact finite V4 transgression ranks

The same integral total complex now also computes

```text
H^1(V4,UPic(Ubar)) = 0.
```

Since `H^1(V4,U_D)=0` and the V4-fixed torsion in `Pic(Ubar)` has F2-dimension two, the edge differential

```text
d2_01 : Pic(Ubar)^V4 -> H^2(V4,U_D)
```

is injective and therefore

```text
rank_F2(d2_01)=2.
```

The independently certified values

```text
H^1(V4,Pic(Ubar)) = (Z/2)^9,
H^2(V4,UPic(Ubar)) = (Z/2)^33
```

then force the finite-quotient right transgression rank to be

```text
rank_F2(d2_11)=2.
```

Thus the former finite ambiguity

```text
(rank d2_01, rank d2_11) in {(0,4),(1,3),(2,2)}
```

is completely removed:

```text
FINITE_TRANSGRESSION_RANK_PAIR=(2,2)
```

Evidence:

```text
workflow_run = 32693463647
workflow_conclusion = success
finite_transgression_ranks_sha256 = 5ab8f03d9c9612f0733ed63676231a5813f8bb4eb75f477244a81023c4d0d29f
artifact_id = 9508117881
artifact_zip_sha256 = 4e012978f1b385d7f4c60b681f4b96578a6ece81cff314c43fd650a0abf77d34
```

## Absolute two-primary filtration

Because `U_D ~= Z^14` is a trivial absolute-Galois lattice,

```text
H^2(Q,U_D)[2^infinity]
 ~= Hom_cont(G_Q,Q/Z)[2^infinity]^14.
```

The now-exact finite `d2_01` has two-dimensional exponent-two image.  Hence the left two-primary filtration remains an infinite character family, but its finite V4 correction is no longer ambiguous:

```text
Hom_cont(G_Q,Q/Z)[2^infinity]^14 / im(d2_01),
rank_F2 im(d2_01)=2.
```

The finite `(Z/2)^33` V4 computation is still not the full absolute two-primary answer.

## Remaining exact wall

All finite V4 extension data required by this leaf are now exact.  The remaining all-primary ambiguity is isolated strictly beyond the finite quotient, in the absolute inflation/restriction contribution from

```text
N = Gal(Qbar / Q(i,sqrt(2)))
```

and the resulting right-hand transgression into `H^3(Q,U_D)`.

```text
RESIDUAL_KERNEL=R33-BR0B-ABSOLUTE-2PRIMARY-N-CHARACTER-TRANSGRESSION
LEAF_ID=L33-03-ABSOLUTE-N-CHARACTER-INFLATION-RESTRICTION-AND-d2_11
CLASS=2
NEW_THEOREM_REQUIRED=false
FINITE_V4_SUBPROBLEM_CLOSED=true
```

No finite V4 result is promoted to a complete Q-defined Brauer inventory before the absolute character/transgression term is accounted exactly.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
