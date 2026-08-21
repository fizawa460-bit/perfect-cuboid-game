# Stage29-02b — dense-open function-field adapter

```text
ROLE=GLOBAL_ENDPOINT_TO_JOINT_COVER_FUNCTION_FIELD_ADAPTER
STATUS=AUDIT_REPAIRED
```

## Field-of-definition split

Keep the arithmetic and geometric function fields distinct:

```text
K_Q   = Q(Y)
K_bar = Qbar(Y)
```

The two radicands are defined over `Q`, so all three quadratic quotients and the joint `V4` cover descend to `Q`. Stage28 proves that the two marginal squareclasses remain distinct after geometric base change to `K_bar`; therefore they are already distinct over `K_Q`.

The geometric `K_bar` layer is used for branch components, genera, singularity types, and divisor classes. The arithmetic `K_Q` layer is used for rational endpoint semantics. Over an extension field `F/Q`, an `F`-rational joint lift of an `F`-rational base point away from branch/pole loci exists iff both radicands are squares in `F`. Geometric lifting over `Qbar` alone is not an arithmetic perfect-cuboid criterion.

```text
ARITHMETIC_FIELD=Q(Y)
GEOMETRIC_FIELD=Qbar(Y)
COVERS_DESCEND_TO_Q=true
RATIONAL_LIFT_QUANTIFIER=F_RATIONAL
```

## Input from the audited Stage18/20/28 interface

On the labeled two-face host, choose the unique shared edge `e` and the other two edges `x,y`. On the dense chart `e!=0`, write

```text
t1=x/e,
t2=y/e.
```

The Stage18 toric base `Y=Bl_4(P1xP1)` already parametrizes the two Pythagorean conditions involving the shared edge; the two corresponding face diagonals are rational functions on the toric parameter chart. Stage28 records the remaining two square predicates as

```text
f_face=t1^2+t2^2,
f_sp=1+t1^2+t2^2.
```

Adjoining `sqrt(f_face)` gives the third face diagonal and adjoining `sqrt(f_sp)` gives the long/space diagonal.

## Full endpoint function field

On the positive physical chart,

```text
third_face_diagonal = e*sqrt(f_face)
space_diagonal      = e*sqrt(f_sp).
```

Thus the labeled full perfect-cuboid endpoint has arithmetic dense-open function field

```text
K_endpoint = Q(Y)(sqrt(f_face),sqrt(f_sp)).
```

The two quadratic extensions are distinct, so

```text
K_endpoint = K_joint
[K_joint:Q(Y)] = 4
Gal(K_joint/Q(Y)) = (Z/2)^2 generically.
```

After geometric base change the same quotient diamond is obtained over `Qbar(Y)`.

Conversely, an `F`-rational point of the joint cover provides the two missing square roots in `F` and hence reconstructs all three face diagonals and the long diagonal on the dense nondegenerate two-face chart. The physical chamber then chooses the positive signs and canonical edge ordering.

## Adapter verdict

At the function-field / dense-open level, the Stage29 global endpoint surface and the Stage28-derived joint cover are the same birational surface over `Q`.

```text
R29_G1_FUNCTION_FIELD_LEVEL=PASS
GLOBAL_ENDPOINT_BIRATIONAL_TO_JOINT_V4_COVER=true
DENSE_OPEN_RECONSTRUCTION_LOSS=0
PHYSICAL_HEIGHT_ON_ENDPOINT=space_diagonal=R
SIGN_CHAMBER_ADAPTER_REQUIRED=true
BOUNDARY_EXCEPTIONAL_LOCUS_ADAPTER_REQUIRED=true
GLOBAL_PROJECTIVE_MODEL_ISOMORPHISM_CLAIMED=false
```

## Multiplicity firewall

The algebraic cover records sign choices of the two newly adjoined square roots. The primitive/canonical physical population counts only the positive long diagonal and positive face diagonal after fixed edge ordering. Hence the degree-four algebraic cover must not be interpreted as four physical cuboids per base point.

```text
ALGEBRAIC_COVER_DEGREE=4
PHYSICAL_MULTIPLICITY_FACTOR=NOT_4
SIGN_CHOICES_ARE_NOT_DISTINCT_PHYSICAL_OBJECTS=true
```

## Remaining global adapter

The dense-open function field identification does not yet identify every exceptional divisor or resolved-surface boundary contraction. The remaining refinement is

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger
```

This is strictly smaller than the original `GlobalEndpointSurfaceToToricJointCoverAdapter` receiver.
