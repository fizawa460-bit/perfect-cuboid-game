# Stage24-20 — million-scale matched finite baseline

EVIDENCE_LEVEL=COMPUTED
CHECKPOINT=20
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## Objective

Stage24 studies the literal survivor transition

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\},
\]

with one identical primitive/canonical physical cutoff `R<=B`. Thus `M2(B)` counts exactly-two-face objects with no space requirement and `N2(B)` is the same object population after the final exact-square test on `R^2`.

Checkpoint20 now uses merged `24-14num-r201/r202` rather than stopping at the old B=100000 replay.

## Exact matched census

| B | M2(B) | N2(B) | N2/M2 |
|---:|---:|---:|---:|
| 1,000 | 1,838 | 2 | 1.08813928183e-3 |
| 2,000 | 4,812 | 5 | 1.03906899418e-3 |
| 5,000 | 16,710 | 15 | 8.97666068223e-4 |
| 10,000 | 41,666 | 25 | 6.00009600154e-4 |
| 20,000 | 102,522 | 42 | 4.09668168783e-4 |
| 50,000 | 331,731 | 62 | 1.86898420708e-4 |
| 100,000 | 796,698 | 89 | 1.11711087514e-4 |
| 200,000 | 1,896,505 | 116 | 6.11651432503e-5 |
| 500,000 | 5,899,985 | 188 | 3.18644877911e-5 |
| 1,000,000 | 13,817,725 | 255 | 1.84545574615e-5 |

All rows are exact finite counts under the same population contract. `N2<=M2` holds identically.

## Main-lane revalidation

The detailed source-level audit is in `revalidation.md`. The main lane does not rely on r203 for correctness.

1. At B=200000, merged r202 explicitly compares the legacy Stage15 paired enumerator, one-shard streaming, and multi-shard streaming on totals, directions, M3/N3 and diagnostics. They are equal.
2. r202 partitions the complete shared-edge key set into an exact disjoint cover. For an exactly-two object the two integral faces have one unique common edge, and the implementation checks that the enumerating shared edge equals the mask-implied shared edge before counting.
3. Three-face objects are the only multi-source case; r202 aggregates their keys and rejects unless multiplicity is exactly three.
4. Space integrality remains only the final `isqrt(R2)^2==R2` predicate, so no integral-space pruning contaminates M2.
5. The r202 target counts independently agree with earlier Stage14-num frozen N2 oracles: B=200000 gives 116, B=500000 gives 188, and B=1000000 gives 255 with direction `(98,101,56)`.

Therefore checkpoint20 accepts the r202 rows as exact matched finite evidence.

## Finite scaling diagnostics

The million-scale data materially change the old visual picture. Between B=100000 and B=1000000:

```text
M2 growth factor = 17.3438...
N2 growth factor = 2.86517...
ratio drop factor = 6.05331...
finite effective slope M2 = 1.23914...
finite effective slope N2 = 0.457150...
finite effective slope N2/M2 = -0.781993...
```

The earlier B=1000 to B=100000 endpoint ratio slope was about `-0.494`. The shift from approximately `-0.494` to `-0.782` on a later window is itself a warning against promoting a finite power law.

At B=1000000:

```text
M2_DIRECTION_A_B_C=4592536,5816786,3408403
N2_DIRECTION_A_B_C=98,101,56
SURVIVOR_RATE_A=2.13389726286e-5
SURVIVOR_RATE_B=1.73635406219e-5
SURVIVOR_RATE_C=1.64299820180e-5
DIRECTIONAL_ORDER=a>b>c
MAX_MIN_RATE_RATIO=1.29878247...
```

This directional ordering is finite diagnostic evidence only; no directional limiting law is claimed.

## Boundary with the Stage14 B500m numerator census

Stage14-num still supplies exact target-side counts through B=500000000, including `N2(500000000)=3495`. It is not combined with the B=1m denominator into a fake matched ratio. The matched Stage24 panel stops exactly where r202 stops: B=1000000.

The known theorem boundaries are unchanged:

```text
TRUE_RATIO_EXPONENT_IDENTIFIED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
TARGET_UNBOUNDEDNESS_PROVED=false
TARGET_POSITIVE_POWER_LOWER_BOUND_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
```

## Numerical reuse preflight

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_MATCHED_CENSUS_WITH_SOURCE_LEVEL_REVALIDATION
NUM_NEW_COMPUTATION_JUSTIFIED=ALREADY_COMPLETED_IN_MERGED_R202
```

## Exit

Checkpoint20 now has a matched exact census through one million and an explicit independent main-lane revalidation. It remains audit-gated before checkpoint30.

```text
DISCOVERY_CHECKPOINT=20
DISCOVERY_LEDGER_STATUS=COMPLETE
R202_REVALIDATION_STATUS=PASS
R203_REQUIRED_FOR_MAIN_CORRECTNESS=false
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
UPSTREAM_PREMISE_CHECK=PASS
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
