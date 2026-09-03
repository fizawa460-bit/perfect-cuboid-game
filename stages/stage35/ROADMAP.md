# Stage35 — moving-fiber arithmetic

```text
STAGE=35
ROOT_KERNEL=K16-C3-MOVING-FIBER-ARITHMETIC
SOURCE_RECEIVER=R29-FIB2
PARENT_ROUTE=J12-PARAMETRIC
SOURCE_EXECUTION_CLASS=3
INITIAL_STATUS=ROADMAP_ONLY_NO_NEW_THEOREM_CREDIT
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Stage35 is the dedicated post-Stage29 attack on `K16-C3-MOVING-FIBER-ARITHMETIC`. It does not reopen Stage29 and it does not count isolated fiber computations as progress toward a uniform theorem.

## Audited source frontier

Stage29 compresses the target to one child receiver:

```text
R29-FIB2 = ArithmeticRankSpecializationAndEndpointResidualSpaceSquareLiftPerFibration
```

The missing result is exactly one of:

```text
A. a uniform arithmetic/specialization theorem over the moving genus-3/genus-5 family;
B. a globally exhaustive reduction to finitely many fibers, followed by exact lift reconstruction.
```

The source firewall is binding:

```text
INDIVIDUAL_FIBER_CHABAUTY_OR_MW_NE_UNIFORM_MOVING_BASE_CONTROL=true
GEOMETRIC_FIBRATION_NE_RATIONAL_POINT_COVERAGE=true
MARGINAL_FIBER_POINT_NE_ENDPOINT_POINT_WITHOUT_RESIDUAL_SPACE_LIFT=true
BOUNDED_MW_ENUMERATION_NE_EXHAUSTIVE=true
FIELD_OF_DEFINITION_MUST_BE_CERTIFIED_BEFORE_Q_ARITHMETIC=true
```

Source-locked context entering Stage35:

- the Euler K3 quotient has `15` geometric elliptic fibrations, but not all 15 are certified individually over `Q`;
- the full endpoint surface has `28` geometric genus-5 fibrations, but not all 28 are certified individually over `Q`;
- rank-4 rulings may require splitting fields;
- `R29-FIB1` remains the field/physical-class ledger dependency;
- the residual space-square condition remains after marginal elliptic arithmetic.

## Operating objective

Stage35 succeeds only by shrinking or closing the uniform moving-family wall. A valid outcome may still be `CLASS3_RETAINED` if the exact minimum theorem is isolated more sharply. A route may drop to Class 2 only when special structure converts the global theorem wall into a bounded exact computation with a reproducible certificate.

No theorem credit is granted for numerical rank samples, finite fiber searches, heuristic specialization behavior, unsourced CAS output, or a finite list of failed endpoint lifts.

## Planned sequence

```text
35-01 SOURCE_LOCK_AND_MODEL_INVENTORY
35-02 Q_FIELD_PHYSICAL_FIBRATION_LEDGER
35-03 RESIDUAL_SPACE_LIFT_INTERFACE
35-04 MINIMAL_UNIFORM_THEOREM_STATEMENT
35-05 BAD_FIBER_AND_EXCEPTIONAL_LOCUS
35-06 UNIFORM_ARITHMETIC_ATTACK_BRANCHES
35-07 FINITE_EXHAUSTIVE_REDUCTION_FALLBACK
35-08 PROOF_EXPERIMENTS_AND_COUNTEREXAMPLE_SEARCH
35-09 DECISION_CERTIFICATE_OR_PARK
35-close
```

### 35-01 — SOURCE_LOCK_AND_MODEL_INVENTORY

Import only the exact Stage29 interfaces needed by this kernel. Freeze the source blobs, named fibrations/families, base fields, parameter bases, generic fiber genera, physical coordinates, quotient direction, and endpoint-lift predicates. Do not replay Stage29 literature scans or all 46 historical receivers.

Required source interfaces:

```text
stages/stage29/29-16/active-kernel-ledger.json
stages/stage29/29-08/fibration-crosswalk.md
stages/stage29/29-14/theorem-dependency-ledger.json
```

Exit only when Stage35 has a compact source-lock certificate whose statements are independently checkable against those exact blobs.

### 35-02 — Q_FIELD_PHYSICAL_FIBRATION_LEDGER

Resolve the arithmetic domain before attempting uniform point arguments. For each fibration class actually used, record:

```text
FIBRATION_ID
SOURCE_MODEL
BASE_FIELD
BASE_PARAMETER_SPACE
GENERIC_FIBER_GENUS
Q_DEFINED=true/false
SPLITTING_FIELD_IF_NEEDED
PHYSICAL_CLASS_ADAPTER
ENDPOINT_PUSHFORWARD_SCOPE
EXCEPTIONAL_OR_DEGENERATE_LOCUS
```

`15 geometric` and `28 geometric` are not permission to run `Q`-arithmetic on every pencil. If the field ledger needed for the chosen attack is unresolved, Stage35 stops here rather than silently treating geometric rulings as `Q`-defined.

### 35-03 — RESIDUAL_SPACE_LIFT_INTERFACE

For each retained marginal/fiber model, materialize the exact condition that turns a rational point on the marginal fiber or quotient into a physical endpoint candidate. Record the residual square/torsor condition, positivity/primitivity conditions where relevant, exceptional points, and the inverse reconstruction map.

The target is a verifier-friendly interface:

```text
FIBER_POINT
  -> physical marginal data
  -> residual space-square predicate
  -> exact endpoint reconstruction or certified rejection.
```

Without this adapter, arithmetic on a quotient or marginal elliptic curve cannot close `R29-FIB2`.

### 35-04 — MINIMAL_UNIFORM_THEOREM_STATEMENT

State the smallest theorem that would actually close the selected moving-family route. The record must contain:

```text
MINIMAL_THEOREM_STATEMENT
QUANTIFIED_PARAMETER_BASE
EXCLUDED_BAD_LOCUS
NEAREST_KNOWN_THEOREM_OR_METHOD
HYPOTHESIS_MISMATCH
CUBOID_SPECIFIC_STRUCTURE
EXACT_RECEIVER_CONSEQUENCE
ENDPOINT_DECISION_CONDITION
```

Do not request a theorem broader than necessary. Conversely, do not weaken the quantifiers until only finitely many tested fibers remain.

### 35-05 — BAD_FIBER_AND_EXCEPTIONAL_LOCUS

Separate generic arithmetic from bad/singular/special fibers. Determine exactly which parameter values must be removed for the generic theorem and whether the removed locus is finite, thin, positive-dimensional, or itself moving. Every excluded locus needs its own exhaustive disposition before a global conclusion.

A statement valid for generic fibers is not global until all exceptional parameter classes are certified.

### 35-06 — UNIFORM_ARITHMETIC_ATTACK_BRANCHES

Run theorem-forge branches only after 35-01 through 35-05 define the exact target. Candidate branches may include specialization/rank control, uniform descent/Selmer control, uniform height bounds, family-level Chabauty-type reductions, or another exact arithmetic mechanism. These are research branches, not assumed available theorems.

Every branch must end in one of:

```text
UNIFORM_THEOREM_PROVED
HYPOTHESIS_MISMATCH_CERTIFIED
COUNTEREXAMPLE_TO_PROPOSED_UNIFORM_STATEMENT
REDUCED_TO_CLASS2_FINITE_CERTIFICATION
CLASS3_WALL_RETAINED_SHARPER
```

Do not accumulate repeated finite fiber computations once the missing uniform quantifier is known.

### 35-07 — FINITE_EXHAUSTIVE_REDUCTION_FALLBACK

This branch is legal only if Stage35 first proves that every relevant endpoint candidate lands in a certified finite set of fibers/classes. The reduction must include exact coverage and inverse/lift reconstruction, not an empirical bound.

Only then may per-fiber exact tools such as Mordell--Weil determination, descent, Chabauty, integral-point computation, or finite rational-point certification be composed into global credit.

```text
FINITE_FIBER_LIST_WITHOUT_GLOBAL_EXHAUSTIVENESS=false
FINITE_EXHAUSTIVE_REDUCTION_PLUS_EXACT_FIBER_CERTIFICATES=potentially_sufficient
```

### 35-08 — PROOF_EXPERIMENTS_AND_COUNTEREXAMPLE_SEARCH

Use finite computation only to test candidate lemmas, identify exceptional fibers, falsify overstrong uniform statements, or discover special structure that could lower the kernel from Class 3 to Class 2. Preserve exact inputs and compact deterministic certificates when computation becomes load-bearing.

Finite experiments alone do not advance receiver status.

### 35-09 — DECISION_CERTIFICATE_OR_PARK

Stage35 ends with exactly one audited classification:

```text
CLOSED_UNIFORM_OBSTRUCTION
CLOSED_BY_GLOBAL_FINITE_REDUCTION
PARTIAL_THEOREM_RECEIVER_STILL_OPEN
RECLASSIFIED_TO_CLASS2_WITH_EXACT_EXECUTION_DAG
CLASS3_RETAINED_WITH_SHARPER_MINIMAL_THEOREM
PARKED_NO_NEW_MATERIAL_INPUT
```

Closure requires all of:

1. exact source/model/field ledger;
2. quantified global coverage for the moving parameter base actually used;
3. a uniform arithmetic theorem or a proved globally exhaustive finite reduction;
4. exact residual-space lift/rejection reconstruction;
5. complete exceptional-locus discharge;
6. hostile audit of the implication back to `R29-FIB2`.

The Stage29 kernel is decision-capable only if the resulting obstructive output genuinely covers the endpoint candidates through the audited adapters. Receiver progress does not automatically imply parent-route closure or perfect-cuboid nonexistence.

## Stop / anti-loop conditions

Stop rather than broaden when any of the following occurs:

```text
ONLY_INDIVIDUAL_FIBER_RESULTS_AVAILABLE
Q_FIELD_LEDGER_REQUIRED_BUT_UNRESOLVED
RESIDUAL_ENDPOINT_LIFT_NOT_EXACT
GENERIC_THEOREM_LEAVES_UNCONTROLLED_EXCEPTIONAL_LOCUS
EXTERNAL_THEOREM_HYPOTHESES_DO_NOT_MATCH
BOUNDED_SEARCH_IS_BEING_USED_AS_GLOBAL_COVERAGE
NO_NEW_MATERIAL_INPUT_AFTER_CLASS3_WALL_IS_EXPLICIT
```

Reopen a stopped branch only for a new theorem/preprint, a new exact structural reduction, an audited contradiction, or a newly certified finite-exhaustive adapter. Renaming the same uniformity wall is not progress.