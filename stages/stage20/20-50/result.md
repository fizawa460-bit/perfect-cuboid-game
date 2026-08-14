# Stage20-50 — lower-bound / construction ledger

EVIDENCE_LEVEL=PROVED
CHECKPOINT=50
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
SUBLANE=20-50a_SAUNDERSON_CONSTRUCTION

## Main result
An explicit one-parameter subfamily of the classical Saunderson Euler-brick construction can be adapted completely to the audited Stage20 population.

For every even integer `m>=10`, take the primitive Pythagorean triple

```text
u=m^2-1,
v=2m,
w=m^2+1
```

and the Euler-brick edges

```text
A=u|4v^2-w^2|,
B=v|4u^2-w^2|,
C=4uvw.
```

The companion proof `construction-proof.md` verifies internally that:

```text
ALL_THREE_FACE_DIAGONALS_INTEGRAL=true
PRIMITIVE=true
CANONICAL_ORDER_AFTER_SORT=B<C<A
DISTINCT_PARAMETER_VALUES_GIVE_DISTINCT_CANONICAL_OBJECTS=true
R<31m^6
```

Therefore every even `m>=10` with `m<=(B/31)^(1/6)` contributes one distinct Stage20 object, giving

```text
M_3(B) >= floor((B/31)^(1/6)/2)-4
```

for all sufficiently large `B`. In particular,

```text
M_3(B) >> B^(1/6).
```

## Ledger consequence

```text
STAGE20_POPULATION_INFINITE=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CERTIFIED_LOWER_EXPONENT=1/6
MATCHING_LOWER_BOUND_PROVED=false
TRUE_EXPONENT_IDENTIFIED=false
ASYMPTOTIC_FORMULA_PROVED=false
```

Combined with the audited repaired checkpoint40 bound from Stage14-e8,

```text
B^(1/6) << M_3(B) <<_epsilon B^(1+epsilon)
```

for every fixed epsilon>0.

The exponent gap is real project knowledge, not filled by finite fitting.

## Reinterpretation of checkpoint30 OPEN_GATE
Checkpoint30 recorded `STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED`. That remains correct: checkpoint50 proves unboundedness and a positive-power floor, but does not identify the true growth law.

The checkpoint40 OPEN_GATE is now `SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED`, not absence of a nontrivial upper bound.

## Numerical reuse preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NONE
NUM_POPULATION_MATCH=NO_MATCH
NUM_EVIDENCE_LEVEL=NOT_APPLICABLE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

No new finite census is needed for the construction proof.

## Boundary
The Stage18->Stage20 conditional survival law remains Stage26. No integrality condition is placed on the space diagonal, and no perfect-cuboid existence/nonexistence statement follows.

NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage20-audit
CODEX_REQUIRED=false
