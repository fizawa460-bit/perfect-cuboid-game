# Stage29-14 — natural slice, quotient, and coverage test

```text
STAGE=Stage29
ITEM=29-14_NATURAL_SLICE_QUOTIENT_AND_COVERAGE_TEST
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
BASE_MAIN_SHA=2433ad54322fa9a3f71b9bbcccf9a581ebe87f2a
ATTACK_ROUTE_COUNT_RETAINED=11
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Purpose

The roadmap requires exact closure on the most structurally natural surviving slices/quotients and, separately, an honest statement of their global coverage role.

The governing firewall is

```text
SLICE_CLOSURE_NE_GLOBAL_ENDPOINT_CLOSURE=true
GEOMETRIC_FIBRATION_NE_RATIONAL_SECTION_COVERAGE=true
GLOBAL_COVERAGE_REQUIRES_AN_EXACT_MAP_OR_THEOREM=true
COVERAGE_FRACTION_WITHOUT_MEASURE_THEOREM_FORBIDDEN=true
```

This stage consumes the audited endpoint map, 29-08 coverage atlas, 29-10 low-genus/K3 attack, 29-13 family closures, and the current Testa--Stoll low-degree classification. It does not replay those results as new attack credit.

## 2. Physical endpoint image avoids the entire F7 branch arrangement

The exact F7 map is

```text
pi_F7:Sbar -> P2,
[a1:a2:a3:...] -> [x:y:z]=[a1^2:a2^2:a3^2],
```

with branch divisor

```text
D: xyz(x+y)(x+z)(y+z)(x+y+z)=0.
```

A physical endpoint Q-point has nonzero rational sides and rational face/space diagonals. Hence its image has

```text
x=a1^2,
y=a2^2,
z=a3^2,
x+y=b3^2,
x+z=b2^2,
y+z=b1^2,
x+y+z=c^2.
```

For such a point none of the seven branch forms can vanish:

- `x=0`, `y=0`, or `z=0` makes a side zero;
- `x+y=0`, `x+z=0`, or `y+z=0` would make a sum of two rational squares zero, forcing both terms zero over Q;
- `x+y+z=0` would make a sum of three rational squares zero, again forcing all three zero.

Therefore

```text
R29-SLICE-BRANCH=DISCHARGED_PHYSICAL_Q_ENDPOINT_AVOIDS_FULL_F7_BRANCH_DIVISOR
PHYSICAL_Q_ENDPOINT_IMAGE_SUBSET=P2(Q)_MINUS_D
F7_RAMIFICATION_CONTAINS_PHYSICAL_Q_ENDPOINT=false
```

On the physical Q-endpoint locus the degree-64 sign cover is therefore in its unramified locus. This is a rational-point statement; it is not a population multiplicity theorem.

## 3. Natural Q-defined permutation-fixed slices are empty

The Q-liftable base permutation group contains the coordinate transpositions. Their codimension-one fixed loci are

```text
L_xy: x=y,
L_xz: x=z,
L_yz: y=z.
```

Suppose a physical endpoint Q-point mapped to `x=y`. Since `x=a1^2` is a nonzero rational square and `x+y=b3^2` is also a rational square,

```text
b3^2=2*a1^2,
```

so `(b3/a1)^2=2`, impossible in Q. The same argument applies to the other two lines.

Hence

```text
R29-SLICE-S3FIX=DISCHARGED_NO_PHYSICAL_Q_POINT_ON_COORDINATE_PERMUTATION_FIXED_LINES
S3_STABILIZER_ON_PHYSICAL_Q_ENDPOINT_TRIVIAL=true
```

The diagonal fixed point `x=y=z` is already contained in these empty fixed lines. No claim is made for fixed loci of geometric automorphisms that are not certified as Q-liftable in the physical model.

## 4. Low-degree curve carrier closure is exact but not point coverage

The audited Testa--Stoll theorem classifies every integral curve on the endpoint surface of canonical/projective degree at most six. The 29-08 atlas records

```text
TESTA_STOLL_LOW_DEGREE_COVERAGE=ALL_INTEGRAL_CURVES_DEGREE_LE_6
POSITIVE_PHYSICAL_FAMILY_RESULT=NONE_AT_DEGREE_LE_6.
```

Thus every positive-dimensional endpoint carrier of degree `<=6` is already accounted for and contributes no nondegenerate physical perfect-cuboid family.

```text
R29-SLICE-LD6=DISCHARGED_ALL_DEGREE_LE_6_INTEGRAL_CURVE_CARRIERS_CLASSIFIED_NO_POSITIVE_PHYSICAL_FAMILY
```

This does **not** cover isolated rational points, curves of higher degree, or the unresolved genus-0/genus-1 classes in the global 176/192 windows.

The surviving low-genus receivers remain

```text
R29-LG2
R29-LG2-EFF
R29-LG2-MB.
```

Even closing them would classify/exclude carriers, not automatically isolated endpoint points.

## 5. Audited closed thin families entering 29-14

The current certified closed families include at least:

```text
SAUNDERSON_ENDPOINT_LIFT
  canonical degree 12
  closed in 29-13

STAGEA2_MINUS18
  one exact source-locked family
  closed in StageA2

EXPLICIT_Bq_FAMILY
  B(q)=(4q,q^2-4,2(q^2-1))
  closed in 29-13 by Pell/Lucas

TESTA_STOLL_DEGREE_LE_6_CARRIERS
  complete low-degree carrier class
  no positive physical family

F7_BRANCH_PREIMAGE_ON_PHYSICAL_Q_LOCUS
  empty by section 2

S3_PERMUTATION_FIXED_SLICES
  empty by section 3.
```

Each is a proper positive-codimension locus or finite union of such loci. Their finite union is therefore a proper geometric subset of the irreducible endpoint surface.

```text
R29-COV-CLOSED-SLICES=DISCHARGED_CURRENT_CERTIFIED_CLOSED_SLICE_UNION_IS_GEOMETRICALLY_PROPER
GEOMETRIC_GLOBAL_COVERAGE_BY_CURRENT_CLOSED_SLICES=false
```

This is deliberately **not** upgraded to

```text
ALL_ENDPOINT_Q_POINTS_LIE_OUTSIDE_OR_INSIDE_CURRENT_SLICE_UNION
```

because no theorem presently determines the Zariski closure of the unknown endpoint rational set. If the endpoint rational set were empty, rational-point coverage by any set would be vacuous; if nonempty, a Lang-type concentration theorem would still require an explicit cuboid-specific exceptional locus.

## 6. Coordinate-sign K3 quotients have global pushforward coverage, not closure

Each Q-defined coordinate sign involution gives a finite degree-two normal quotient

```text
Sbar -> Kbar_j,
```

with K3 minimal resolution. The seven directions form the audited Q-orbit pattern

```text
3*K_a + 3*K_b + 1*K_c.
```

Every endpoint Q-point pushes forward to a Q-point on each corresponding Q-defined quotient. Thus the quotient mechanism has exact endpoint **pushforward coverage**.

```text
R29-COV-K3-PUSH=DISCHARGED_GLOBAL_ENDPOINT_PUSHFORWARD_TO_COORDINATE_SIGN_QUOTIENTS
```

But none of these quotient targets is certified Q-point-empty. In particular `K_c` is exactly the Stage20/Testa--Stoll Euler K3 and carries known rational families. A quotient rational point need not lift to a physical endpoint point without the residual square/torsor condition.

```text
K3_QUOTIENT_ENDPOINT_NONEXISTENCE=false
K3_QPOINT_IMPLIES_ENDPOINT_QPOINT=false
G10-K3-SIGN=AMBER
```

## 7. The only certified global parametrized coverage remains Peschmann/Master-Hit

29-08 independently proved that every primitive Euler brick, and hence every perfect-cuboid candidate, is represented after gcd normalization by the two-Euclid-pair Master-Hit atlas.

This is a genuine global endpoint candidate coverage theorem:

```text
R29-PESCH-COV=DISCHARGED
PESCHMANN_GLOBAL_ENDPOINT_COVERAGE_VIA_MASTER_HITS=true.
```

However the decisive universal exponent-one statement is still conjectural:

```text
R29-PESCH-E1=AMBER_CONJECTURAL_GLOBAL_ENDPOINT_BLOCKER.
```

The 1,072 closed fibers, Saunderson family, StageA2 family, explicit `B(q)` family and any bounded Mordell-Weil enumeration are strict subfamilies of the globally covering atlas and do not exhaust it.

Hence

```text
J12-PARAMETRIC=AMBER_GLOBAL_COVERAGE_WITH_CONJECTURAL_DECISIVE_BLOCKER
```

remains correct.

## 8. Fibration coverage firewall

The endpoint has 28 geometric genus-5 fibrations, and the Euler K3 quotient has 15 geometric elliptic fibrations. The audited field ledger is incomplete:

```text
ALL_28_ENDPOINT_FIBRATIONS_Q_DEFINED_CERTIFIED=false
ALL_15_EULER_K3_FIBRATIONS_Q_DEFINED_CERTIFIED=false.
```

Even a Q-defined fibration covers the surface by fibers geometrically; this does not mean rational points are generated by known sections or multisections. Rank-4 rulings may require splitting fields. Therefore 29-14 does not promote geometric fibration counts to arithmetic endpoint coverage.

```text
R29-FIB1=OPEN_PHYSICAL_CLASS_PLUS_FIELD_OF_DEFINITION_LEDGER
R29-FIB2=OPEN_ARITHMETIC_SPECIALIZATION_AND_RESIDUAL_SPACE_LIFT
```

## 9. Coverage verdict

The systematic test separates three notions that had previously appeared close in prose:

```text
CLOSED_SLICE_COVERAGE:
  several exact families/slices closed,
  union geometrically proper,
  global endpoint-Q coverage not proved.

GLOBAL_QUOTIENT_PUSHFORWARD_COVERAGE:
  coordinate-sign K3 quotients receive every endpoint point,
  quotient obstruction not closed.

GLOBAL_PARAMETRIC_CANDIDATE_COVERAGE:
  Peschmann/Master-Hit covers every primitive Euler/endpoint candidate,
  decisive exponent-one blocker remains conjectural.
```

Therefore no current natural closed slice/quotient package is a global nonexistence proof.

```text
GLOBAL_CLOSED_SLICE_ENDPOINT_COVERAGE_PROVED=false
GLOBAL_ENDPOINT_QUOTIENT_PUSHFORWARD_COVERAGE_PROVED=true
GLOBAL_ENDPOINT_PARAMETRIC_CANDIDATE_COVERAGE_PROVED=true
GLOBAL_ENDPOINT_NONEXISTENCE_PROVED=false
P_OVER_M3_SCALE_KNOWN=false
```

No coverage fraction is assigned.

## 10. Portfolio/routing state

29-14 creates no twelfth attack route and does not retire an existing parent route. The new branch/symmetry slice closures are supporting exact results. The important global frontier remains unchanged:

```text
P(B)/M3(B)=UNKNOWN.
```

Submitted state:

```text
R29-SLICE-BRANCH=DISCHARGED
R29-SLICE-S3FIX=DISCHARGED
R29-SLICE-LD6=DISCHARGED
R29-COV-CLOSED-SLICES=DISCHARGED_GEOMETRIC_NONCOVERAGE
R29-COV-K3-PUSH=DISCHARGED_GLOBAL_PUSHFORWARD
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
TARGETED_BACKFLOW_REQUIRED=false
ROADMAP_REWRITE_REQUIRED=false
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=29-15_ENDPOINT_ARSENAL_REMATCH
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
