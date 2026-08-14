# Stage22-20 — matched finite baseline for the one-face / two-face strata

EVIDENCE_LEVEL=COMPUTED
CHECKPOINT=20
STATUS=COMPUTED_CANDIDATE_PENDING_FRESH_AUDIT

Stage22 reuses the audited finite censuses from Stage16 and Stage18 under the identical primitive/canonical cutoff `R<=B`.

| B | M1(B) | M2(B) | M2/M1 |
|---:|---:|---:|---:|
| 50 | 490 | 16 | 0.0326530612 |
| 100 | 2620 | 56 | 0.0213740458 |
| 200 | 12664 | 172 | 0.0135818067 |
| 400 | 59574 | 494 | 0.0082922073 |
| 800 | 273901 | 1347 | 0.0049178353 |
| 1200 | 662207 | 2350 | 0.0035487426 |
| 1600 | 1234822 | 3536 | 0.0028392751 |
| 2000 | 1997863 | 4812 | 0.0024085735 |

The ratio decreases monotonically across these shared thresholds. This is a finite diagnostic only and is not used to infer a power or logarithmic exponent.

## Reused assets

```text
SOURCE_COUNTS=stages/stage16/16-20/counts.csv
TARGET_COUNTS=stages/stage18/18-20/counts.csv
SOURCE_CENSUS_STATUS=AUDITED_COMPUTED
TARGET_CENSUS_STATUS=AUDITED_COMPUTED
COMMON_THRESHOLDS=50,100,200,400,800,1200,1600,2000
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=Stage16-20,Stage18-20
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=COMPUTED
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

## Interpretation boundary

Exactly-one and exactly-two are disjoint strata. Therefore `M2/M1` is not the empirical probability that a Stage16 object survives an added predicate. It is a matched population-size ratio between adjacent face-integrality strata under the same ambient universe and cutoff.

The finite trend is compatible with substantial thinning, but checkpoint20 does not promote it to any asymptotic law. Checkpoint30 must derive the strongest theorem-level ratio from audited asymptotic interfaces after the repository-wide stronger-result search.

```text
FINITE_DATA_USED_AS_PROOF=false
MONOTONE_DECREASE_ON_SHARED_THRESHOLDS=true
ASYMPTOTIC_EXPONENT_CLAIMED=false
NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
