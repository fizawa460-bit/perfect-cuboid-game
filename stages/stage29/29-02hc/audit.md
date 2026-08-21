# Stage29-02hc — extra-adversarial audit

```text
AUDITED_PR=1305
AUDITED_SUBMISSION_HEAD=138409e579a04bda4b01bc5450c600a98f25ac60
AUDIT_MODE=EXTRA_ADVERSARIAL
AUDIT_VERDICT=PASS_AFTER_MATERIAL_REPAIR
```

## Executive verdict

The non-Fano recognition is real and useful, but the submission over-promoted it in exactly the field-of-definition direction that Stage29 audits are required to attack.

Three repairs were necessary:

1. branch-arrangement `PGL3(Q)` equivalence was incorrectly promoted to equality of the **standard Kummer Q-covers**;
2. Suciu's central unbranched congruence-cover `b1(X_N)` was blurred with the endpoint's projective degree-64 arrangement-open cover;
3. `hc` was classified as a new independent global foundation although it is more accurately the named classical recognition/theorem-package adapter for the already-audited F7 / `29-02ha` sign cover.

No fatal defect remains after those repairs.

## Attack 1 — is it really the same map?

At the branch-arrangement level, yes.  The rational transformation

```text
x=X, y=-Y, z=Z-X
```

maps the seven cuboid branch lines exactly to Suciu's standard non-Fano line set, up to line scalars and permutation.

At the **Q-cover** level, no: the line scalars matter in the square-root extension.  Thus the submitted statement was too strong.

```text
SAME_BRANCH_MAP_AUDIT=PASS
SAME_STANDARD_Q_KUMMER_COVER_AUDIT=FAIL_AS_SUBMITTED
```

## Attack 2 — Q versus Q(i)

For a projectivity with

```text
phi^* L_i=lambda_i L_sigma(i),
```

a lift between the standard sign/Kummer covers over a field `F` requires all seven `lambda_i` to have one common class in `F*/F*^2`.

The displayed map has multiplier classes

```text
+,-,-,+,+,-,-
```

and relative six-coordinate twist

```text
-,+,+,-,-,+.
```

Fresh exact enumeration of every rational projective equivalence gives

```text
PGL3_Q_EQUIVALENCES_TOTAL=24
STANDARD_NF_Q_COVER_LIFTABLE_EQUIVALENCES=0
QI_COVER_LIFTABLE_EQUIVALENCES=24.
```

Hence

```text
STANDARD_NF_Q_COVER_IDENTIFICATION=false
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=true
CUBOID_Q_FORM_IS_EXPLICIT_CONSTANT_SIGN_TWIST=true
ABSTRACT_Q_SURFACE_ISOMORPHISM_TO_STANDARD_M2_PROVED=false
```

The final line prevents overclaiming: the audit disproves the submitted cover-over-`P2` Q-identification, not every conceivable abstract Q-isomorphism.

## Attack 3 — generic versus global

After adjoining `i`, the cuboid and standard non-Fano normal covers have the same Kummer function field over the same `P2`, so uniqueness of normalization promotes the identification globally.

For the projective seven-line `N=2` Hirzebruch construction:

```text
deck=(Z/2)^6
degree=64
triple fiber=8
six triples -> 48 A1 nodes.
```

Ordinary double branch intersections are smooth in the normal cover.  Minimal resolutions therefore agree over `Q(i)`.

```text
GENERIC_TO_GLOBAL_AUDIT=PASS_AFTER_FIELD_SCOPE_REPAIR
RESOLUTION_AUDIT=PASS_GEOMETRIC_OVER_QI
```

## Attack 4 — independent invariant recovery

Hirzebruch/Suciu formulas give at `N=2`

```text
K^2=16
c2=80
b1=0
q=0
chi(O)=8
pg=7
```

and the 48-node count above.  This is a strong independent consistency check, but invariant equality is not used to erase the Q-form twist.

```text
R29-NF2=DISCHARGED_GEOMETRIC
```

## Attack 5 — central versus projective topology

Suciu's Example 10.5 formula for the unbranched `X_N` is central-arrangement data.  The endpoint open cover is projective.  Using the central/projective product splitting,

```text
CENTRAL_OPEN_B1_N2=33
PROJECTIVE_ENDPOINT_OPEN_B1_N2=32.
```

The compact `M_2` value remains `b1=0`.

The seven-coordinate characteristic varieties must be intersected with the product-one projective character torus before being called endpoint data.  The special

```text
rho=(1,-1,-1,1,-1,-1,1)
```

has product one and does descend.

```text
CENTRAL_PROJECTIVE_SCOPE_AUDIT=PASS_AFTER_MATERIAL_REPAIR
R29-NF3=OPEN_DOWNSTREAM
R29-NF4=OPEN_DOWNSTREAM
R29-NF5=OPEN_DOWNSTREAM
```

## Attack 6 — physical/population overreach

The arrangement complement and Stage29-02f physical algebraic open differ over `Qbar`.  Nondegenerate rational endpoint points do lie in the arrangement complement, because no rational sum of nonzero squares can vanish.

That fact supplies no automatic transfer of

```text
M1,N1,M2,N2,M3,
R<=B,
primitivity,
canonical ordering,
face multiplicity,
asymptotics,
or Brauer residues.
```

```text
STAGE16_20_POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
CANONICAL_ORDER_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
BRAUER_TRANSFER_AUTOMATIC=false
BACKFLOW_TO_STAGE16_28=false
```

## Attack 7 — is this actually a new foundation?

Not independently.  `29-02ha` already discovered the exact seven-line degree-64 sign cover.  `29-02hc` recognizes that same geometric structure as the non-Fano `N=2` Hirzebruch construction and imports a substantial pre-existing theorem ecosystem.

This is high-value progress, but the correct classification is

```text
NOVELTY_IN_REPO=HIGH_VALUE_NAMED_RECOGNITION_ADAPTER_ON_F7
INDEPENDENT_FOUNDATION=false
NEW_THEOREM_ECOSYSTEM=true
```

This distinction prevents the project from counting literature recognition of an existing foundation as another independent viewpoint.

Internal continuation of the non-Fano receivers does not automatically earn a new suffix:

```text
HC_INTERNAL_RECEIVER_CONTINUATION_DOES_NOT_EARN_HD=true
NEXT_ITEM=29-02hd_BROAD_INDEPENDENT_SCREEN_ONLY
```

## Final state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02HC_AUDIT=PASS
BOUNDED_REPAIR=Q_FORM_TWIST_PLUS_CENTRAL_PROJECTIVE_SCOPE_PLUS_NOVELTY_ROUTING
SOURCE_LOCK_AUDIT=PASS_AFTER_SCOPE_REPAIR
SAME_BRANCH_MAP_AUDIT=PASS
STANDARD_NF_Q_COVER_IDENTIFICATION=false
QI_GEOMETRIC_HIRZEBRUCH_IDENTIFICATION=true
CUBOID_Q_FORM_IS_EXPLICIT_CONSTANT_SIGN_TWIST=true
PROJECTIVE_OPEN_B1_N2=32
INDEPENDENT_FOUNDATION=false
NEW_THEOREM_ECOSYSTEM=true
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
AUTO_ADVANCE_TO_29_03=false
STAGE29_02_MINING_STOP_CONDITION_SATISFIED=false
BACKFLOW_TO_STAGE16_28=false
NEXT_ITEM=29-02hd_BROAD_INDEPENDENT_SCREEN_ONLY
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
