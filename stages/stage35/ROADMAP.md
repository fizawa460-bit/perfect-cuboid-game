# Stage35 — moving-fiber arithmetic

```text
STAGE=35
ROOT_KERNEL=K16-C3-MOVING-FIBER-ARITHMETIC
SOURCE_RECEIVER=R29-FIB2
PARENT_ROUTE=J12-PARAMETRIC
SOURCE_EXECUTION_CLASS=3
CURRENT_BATCH_STATUS=35_09_SUBMITTED_FOR_HOSTILE_AUDIT
CURRENT_CLASSIFICATION=CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage35 is the dedicated post-Stage29 attack on `K16-C3-MOVING-FIBER-ARITHMETIC`. It does not reopen Stage29 and it does not count isolated fiber computations as progress toward a uniform theorem.

## Audited source frontier

Stage29 compresses the target to one child receiver:

```text
R29-FIB2 = ArithmeticRankSpecializationAndEndpointResidualSpaceSquareLiftPerFibration
```

The original missing result was one of:

```text
A. a uniform arithmetic/specialization theorem over the moving genus-3/genus-5 family;
B. an exact receiver-matched replacement theorem with the same R29-FIB2 quantifiers;
C. a globally exhaustive reduction to finitely many fibers, followed by exact lift reconstruction.
```

The source firewall remains binding:

```text
INDIVIDUAL_FIBER_CHABAUTY_OR_MW_NE_UNIFORM_MOVING_BASE_CONTROL=true
GEOMETRIC_FIBRATION_NE_RATIONAL_POINT_COVERAGE=true
BOUNDED_MW_ENUMERATION_NE_EXHAUSTIVE=true
FIELD_OF_DEFINITION_MUST_BE_CERTIFIED_BEFORE_Q_ARITHMETIC=true
```

## Formal Stage34 Arsenal routing

Stage35 does not preload Stage34 or the full Arsenal. Once an active leaf identifies an exact missing weapon type, it consults `docs/arsenal/index.json` before new route invention.

```text
S34-WF01 CLASS3_RECEIVER_REPLACEMENT_THEOREM_PIPELINE
  role: permit an exact replacement theorem matching the receiver quantifiers
  Stage35 outcome: USED

S34-W01 SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT
  role: exhaustive finite squareclass reduction when an exact factored receiver square appears
  Stage35 outcome: NOT APPLIED; selected direct route has no residual squareclass condition forcing finite t

S34-W03 RECEIVER_RESTRICTED_INTERSECTION_EXCLUSION
  role: close only branch/fiber intersect receiver condition when a uniform exact witness exists
  Stage35 outcome: retained as a future candidate; no uniform witness found

S34-W02 GLOBAL_MORDELL_WEIL_CONGRUENCE_EXCLUSION
  role: global exclusion on a fixed certified MW group after exhaustive finite reduction
  Stage35 outcome: LOCKED; no global finite-fiber reduction proved
```

## Executed sequence

```text
35-01 SOURCE_LOCK_AND_MODEL_INVENTORY                 PASS
35-02 Q_FIELD_PHYSICAL_FIBRATION_LEDGER              PASS_SELECTED_ROUTE
35-03 RESIDUAL_SPACE_LIFT_INTERFACE                  PASS_DIRECT_FULL_ENDPOINT_RECONSTRUCTION
35-04 MINIMAL_UNIFORM_THEOREM_STATEMENT              PASS_TARGET_LOCKED_NOT_PROVED
35-05 BAD_FIBER_AND_EXCEPTIONAL_LOCUS                PASS
35-06 UNIFORM_ARITHMETIC_ATTACK_BRANCHES             CLASS3_WALL_RETAINED_SHARPER
35-07 FINITE_EXHAUSTIVE_REDUCTION_FALLBACK           NO_CERTIFIED_GLOBAL_FINITE_REDUCTION
35-08 PROOF_EXPERIMENTS_AND_COUNTEREXAMPLE_SEARCH    NEW_EXACT_STRUCTURE_NO_CLOSURE
35-09 DECISION_CERTIFICATE_OR_PARK                   CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM
35-close                                              NOT AUTHORIZED; hostile audit required
```

## Selected exact route

Stage35 selects one direct rank-3 genus-5 fibration of the full endpoint surface rather than attempting to classify all 28 geometric fibrations.

With Stage29 coordinates `[e:x:y:p:q:z:d]` and Testa--Stoll coordinates `[a1:a2:a3:b1:b2:b3:c]`, use

```text
[a1:a2:a3:b1:b2:b3:c]=[e:x:y:z:q:p:d].
```

The selected rank-3 quadric is

```text
e^2+z^2=d^2,
```

with rational parameter

```text
t=(e+d)/z.
```

For a nondegenerate positive physical endpoint, `t in Q` and `t>1`. The rank-3 conic parameterization is over `Q`, its singular base points are outside the physical open, and every physical endpoint enters this selected fibration.

Thus the historical all-15/all-28 field ledger remains open, but it is not required for this selected Stage35 attack.

## Exact direct endpoint family

The selected fiber can be written in `[x:y:p:q:d]` as

```text
(t^2+1)^2*x^2+(t^2-1)^2*d^2=(t^2+1)^2*p^2
(t^2+1)^2*y^2+(t^2-1)^2*d^2=(t^2+1)^2*q^2
(t^2+1)^2*(x^2+y^2)=4*t^2*d^2.
```

The inverse reconstruction is

```text
e=((t^2-1)/(t^2+1))*d
z=(2*t/(t^2+1))*d.
```

This reconstructs all four endpoint equations exactly. Therefore the selected route is already on the full endpoint surface: the historical K3-marginal residual space-square predicate is not an additional condition here.

## Minimal receiver-matched theorem

`S34-WF01` allows the original broad theorem species to be replaced by the exact receiver obligation. Stage35 freezes

```text
T35-R3-PHYS-EMPTY:
for every t in Q with t>1,
the physical open U_t(Q) of the exact genus-5 fiber C_t is empty.
```

This theorem is **not proved**.

## Bad-fiber disposition

The exact squarefree bad-parameter divisor for the selected family is

```text
T*U*(T^2-U^2)*(T^2+U^2)*(T^4+U^4)=0.
```

It has 10 geometric bad fibers, matching the source count for a rank-3 fibration. Its intersection with the physical rational parameter base `Q_{>1}` is empty. Hence every physical rational parameter gives a smooth genus-5 fiber and no exceptional rational bad-fiber subproblem remains.

## Exact diagonal genus-5 structure

Writing

```text
alpha=((t^2-1)/(t^2+1))^2
beta=4*t^2/(t^2+1)^2=1-alpha,
```

the family is the diagonal genus-5 model

```text
alpha*d^2+x^2=p^2
beta*d^2-x^2=y^2
d^2-x^2=q^2.
```

Its five elliptic quotient Jacobians are explicit over `Q(t)` and have full rational 2-torsion. Fixed-fiber covering/elliptic-Chabauty methods and generic `Q(t)` Mordell--Weil/section methods are structurally applicable, but neither excludes rational points that appear only after specialization.

## Current Class-3 wall

Stage35 shrinks the original wall to:

```text
uniformly exclude specialization-new rational points in the physical open of
TS-S-R3-Q1 for every rational t>1,
or prove a receiver-restricted obstruction with exactly the same quantifier.
```

No applicable existing uniform closure theorem was source-locked. No globally exhaustive reduction to finitely many fibers was proved. No bounded fiber search is permitted to stand in for this quantifier.

## Current decision / anti-loop

```text
CLASSIFICATION=CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
NEW_THEOREM_CREDIT=false
```

Reopen only for a material input:

```text
- a theorem controlling specialization-new points for this exact family/quotient system;
- a uniform receiver-intersection obstruction valid for every rational t>1;
- an exact globally exhaustive finite reduction;
- an audited contradiction to the current model/coverage/reconstruction/bad-locus certificates.
```

Do not run additional individual fibers, expand all 28/15 field ledgers, or repeat the broad literature search without one of those triggers.
