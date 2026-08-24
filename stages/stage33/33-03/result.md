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

## Absolute two-primary filtration

CI run `32690584148` materializes the total-degree-two hypercohomology filtration

```text
0 -> H^2(Q,U_D)/im(d2_01)
   -> H^2(Q,UPic(Ubar))
   -> ker(d2_11: H^1(Q,Pic(Ubar)) -> H^3(Q,U_D))
   -> 0.
```

Because `U_D ~= Z^14` is a trivial absolute-Galois lattice,

```text
H^2(Q,U_D)[2^infinity]
 ~= Hom_cont(G_Q,Q/Z)[2^infinity]^14.
```

The source of `d2_01` is exactly the fixed torsion subgroup

```text
Pic(Ubar)^G = (Z/2)^2,
```

so its image has exponent two and F2-rank at most two.  Hence the left two-primary filtration is necessarily an infinite character family:

```text
Hom_cont(G_Q,Q/Z)[2^infinity]^14 / im(d2_01).
```

In particular, the finite `(Z/2)^33` V4 computation is not the full absolute two-primary answer.

Evidence:

```text
workflow_run = 32690584148
workflow_conclusion = success
absolute_two_primary_shape_sha256 = 0446956d573d3071389432a20789814b62d4e74b72b733ed31f805e6ad14730c
finite_v4_hypercohomology_sha256 = 82eabfe80fce8407198a8b2dd5277de352280866e73a38d272f160bc0a41ac2d
artifact_id = 9507155144
artifact_zip_sha256 = 58932763f8a4cb10f7ac75b8b6c9e161bbb037566cda5a2c2d3fe555b95b7e01
```

## Remaining exact wall

The remaining all-primary ambiguity is now isolated in the right filtration and its absolute inflation/restriction data:

```text
RESIDUAL_KERNEL=R33-BR0B-ABSOLUTE-2PRIMARY-PICU-H1-TO-UNIT-H3-TRANSGRESSION
LEAF_ID=L33-03-ABSOLUTE-PICU-H1-INFLATION-RESTRICTION-AND-d2_11
CLASS=2
NEW_THEOREM_REQUIRED=false
```

No finite V4 result is promoted to a complete Q-defined Brauer inventory before this map is computed.

```text
UNRESOLVED_UNKNOWN_IN_SCOPE>0
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
