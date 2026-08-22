# Stage29-14 — adversarial audit contract

Audit this submission from the exact endpoint equations, authoritative prior audits, and current low-degree source. Do not accept a slice closure or coverage label merely because the locus is visually natural.

## 1. F7 branch-avoidance theorem — highest-priority elementary check

Start from the exact endpoint equations and F7 map

```text
[x:y:z]=[a1^2:a2^2:a3^2]
D=V(xyz(x+y)(x+z)(y+z)(x+y+z)).
```

For a physical endpoint Q-point verify, projectively and without positivity handwaving, that none of the seven forms can vanish.

Check separately:

- side coordinates `x,y,z`;
- two-square sums `x+y,x+z,y+z` over Q;
- the three-square sum `x+y+z` over Q.

Confirm that the physical endpoint image lies in `P2\D`, and determine whether this indeed places every physical point in the unramified/etale locus of the F7 cover and every coordinate-sign quotient.

If correct, accept only the exact rational-point statement; do not infer a 64-fold physical counting multiplicity.

## 2. Q-liftable permutation-fixed slices

Independently verify that the relevant Q-defined coordinate permutation transpositions have base fixed lines

```text
x=y,
x=z,
y=z.
```

At `x=y`, use the original endpoint equations to verify that a nonzero physical Q-point would force a rational square equal to `2`; repeat cyclically.

Then check the stabilizer claim:

```text
S3_STABILIZER_ON_PHYSICAL_Q_ENDPOINT_TRIVIAL=true.
```

Do not extend this statement to the full geometric `S4` arrangement automorphism group without the already-open lift/cocycle adapter.

## 3. Low-degree carrier scope

Re-read the authoritative Testa--Stoll theorem/source lock and 29-02c-LG2 / 29-10.

Verify exactly what is meant by

```text
ALL_INTEGRAL_CURVES_OF_CANONICAL_DEGREE_LE_6_CLASSIFIED.
```

Check that the repo's statement `positive_physical_family_result=NONE_AT_DEGREE_LE_6` is supported. If the theorem merely lists curves without a complete physical-Q analysis, repair the disposition.

Preserve the firewall:

```text
isolated endpoint Q points not covered;
higher-degree carriers not covered;
R29-LG2, R29-LG2-EFF, R29-LG2-MB remain open.
```

## 4. Combined closed-slice union

Check that every locus included in the submitted closed-slice union is positive codimension and that only finitely many loci/classes are being unioned.

If so, the union is a proper geometric subset of the irreducible endpoint surface. Audit the language carefully:

```text
GEOMETRIC_GLOBAL_COVERAGE_BY_CURRENT_CLOSED_SLICES=false
GLOBAL_ENDPOINT_Q_POINT_COVERAGE_PROVED=false.
```

The first is an actual geometric noncoverage statement. The second says no rational-point coverage theorem is proved. Do not claim there exists a rational endpoint point outside the union, since no endpoint rational point is known at all.

Do not assign a numerical `coverage fraction`.

## 5. Coordinate-sign K3 quotient pushforward

Re-read 29-06/29-10 and verify:

- the seven coordinate sign involutions are defined over Q at the canonical model level;
- the quotient maps `Sbar -> Kbar_j` are degree two;
- a physical endpoint Q-point pushes to a Q-point of the quotient;
- because the physical point is in the free/unramified locus, determine whether its quotient image lies in the smooth locus and therefore gives a Q-point on the K3 minimal resolution as well.

Do not reverse the implication. A quotient Q-point does not automatically lift to an endpoint Q-point.

Check the `K_c` warning: the Stage20/Testa--Stoll Euler K3 has rational families, so a strategy requiring `K_c(Q)=empty` is impossible.

## 6. Global parametric coverage versus slice closure

Reconfirm the 29-08 proof that Peschmann/Master-Hit gives global primitive Euler-brick and endpoint-candidate coverage after gcd normalization.

Then verify that the currently closed families (1,072 fibers, Saunderson, StageA2, explicit B(q), bounded MW enumerations) do not exhaust the infinite globally covering atlas.

Recheck that

```text
R29-PESCH-E1
```

is still conjectural. If a theorem has appeared in the repo since 29-13, repair materially.

## 7. Fibration coverage semantics

Re-read 29-08 fibration crosswalk. Keep separate:

```text
28 endpoint genus-5 fibrations = geometric count;
15 Euler-K3 elliptic fibrations = geometric count;
all individual Q-definition = not certified;
known sections/multisections generate all Q-points = not proved.
```

If current source or repo data already determine more of the field-of-definition ledger, record that as a bounded positive repair, but do not equate a fibration of a surface with arithmetic generation of all rational points.

## 8. Search for a stronger natural-slice theorem already present

Search the current repo and the authoritative cuboid curve/fibration sources for any theorem stronger than the submitted slice list, especially:

- a theorem forcing every endpoint Q-point onto a proper closed exceptional locus;
- a complete rational-point classification on a Q-defined genus-5 fiber family;
- a finite closed-curve coverage theorem;
- a natural quotient whose Q-points are empty or whose relevant residual lift locus is empty;
- a slice/family closure already subsuming Saunderson, StageA2, or B(q).

If found, repair 29-14 rather than deferring automatically to 29-15.

## 9. Double-credit and route state

The following are imported inputs and must not receive new 29-14 attack credit:

```text
Saunderson closure and M3-P lower theorem -> 29-13
StageA2 -18 closure -> StageA2
B(q) closure -> 29-13
Peschmann global coverage -> 29-08
Testa--Stoll degree<=6 classification -> prior source lock
K3 quotient architecture -> 29-06/29-10.
```

New 29-14 credit, if it survives, is only for newly formalized exact branch/symmetry slice closure and coverage semantics.

Reconstruct the portfolio state independently. Expected submission state remains

```text
ATTACK_ROUTE_COUNT=11
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false.
```

## Required output

Create `stages/stage29/29-14/audit.md` and repair this same PR branch if needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
R29_SLICE_BRANCH=<audited disposition>
R29_SLICE_S3FIX=<audited disposition>
R29_SLICE_LD6=<audited disposition>
R29_COV_CLOSED_SLICES=<audited disposition>
R29_COV_K3_PUSH=<audited disposition>
GLOBAL_CLOSED_SLICE_ENDPOINT_Q_COVERAGE_PROVED=true|false
GLOBAL_ENDPOINT_QUOTIENT_PUSHFORWARD_COVERAGE_PROVED=true|false
GLOBAL_ENDPOINT_PARAMETRIC_CANDIDATE_COVERAGE_PROVED=true|false
ATTACK_ROUTE_COUNT=<integer>
GREEN_ROUTE_COUNT=<integer>
AMBER_ROUTE_COUNT=<integer>
P_OVER_M3_SCALE_KNOWN=true|false
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If the submitted routing survives, the next item is

```text
29-15_ENDPOINT_ARSENAL_REMATCH.
```
