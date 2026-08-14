# Stage24-20 — matched finite baseline

EVIDENCE_LEVEL=COMPUTED
CHECKPOINT=20
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Objective

Stage24 studies the literal survivor transition

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\},
\]

where `M2(B)=#B_2(B)` is the primitive canonical exactly-two-face source and `N2(B)=#A_2(B)` adds only integral space diagonal, under the same physical cutoff `R<=B`.

Checkpoint20 establishes a genuinely matched finite baseline. It does not infer the asymptotic transition law.

## 2. Frozen finite inputs and bounded replay

Stage19-20 freezes

```text
B:   1000  2000  5000  10000  20000  50000  100000
N2:     2     5    15     25     42     62      89
```

Stage18-20 publishes source counts only through B=2000. To avoid comparing unmatched thresholds, Stage24 reuses the audited Stage18 enumerator unchanged and evaluates it at the Stage19 thresholds. The overlap check reproduces the frozen Stage18 value

\[
M_2(2000)=4812.
\]

The replay code is `stages/stage24/24-20/replay.py`; the frozen Stage24 table is `matched-counts.csv`.

## 3. Matched exact table

| B | M2(B) | N2(B) | N2/M2 |
|---:|---:|---:|---:|
| 1,000 | 1,838 | 2 | 0.0010881393 |
| 2,000 | 4,812 | 5 | 0.0010390690 |
| 5,000 | 16,710 | 15 | 0.0008976661 |
| 10,000 | 41,666 | 25 | 0.0006000096 |
| 20,000 | 102,522 | 42 | 0.0004096682 |
| 50,000 | 331,731 | 62 | 0.0001868984 |
| 100,000 | 796,698 | 89 | 0.0001117111 |

Every row passes the literal-subset sanity check `N2<=M2`.

The survivor ratio decreases by a factor about 9.74 from B=1000 to B=100000 while B increases by a factor 100. The endpoint log-log effective slope is approximately `-0.494`. This finite resemblance to a half-power decay is diagnostic only.

## 4. Why checkpoint20 does not identify the exponent

There are three independent reasons not to promote this table to a power law:

1. the target sample is only `N2=89` at the largest matched replay threshold;
2. Stage19 explicitly froze the half-power exponent as an upper exponent, not a proven asymptotic exponent;
3. Stage19's much larger exact numerical endpoint `N2(500,000,000)=3495` failed its predeclared terminal stability gate for `N2(B)/sqrt(B)`.

Therefore checkpoint20 records only

```text
FINITE_RATIO_TREND=STRONGLY_DECREASING_ON_MATCHED_WINDOW
FINITE_EFFECTIVE_ENDPOINT_SLOPE_APPROX=-0.494
HALF_POWER_FINITE_RESEMBLANCE=DIAGNOSTIC_ONLY
TRUE_RATIO_EXPONENT_IDENTIFIED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
```

## 5. B=500,000,000 boundary

The exact Stage19 endpoint

\[
N_2(500,000,000)=3495
\]

is retained as target-side finite evidence and as the source of the certified constant lower floor. It is not included in the checkpoint20 matched ratio table because there is no frozen exact Stage18 source census at that threshold. Stage24 does not launch a 500-million-scale Stage18 enumeration merely to extend a diagnostic table.

## 6. Discovery and computation classification

The checkpoint20 discovery pass is materialized at `discovery-ledger.md`.

No new Stage19 enumerator was written. The only new computation is a bounded replay of the already-audited Stage18 enumerator at the seven existing Stage19 thresholds. That computation directly answers the missing matched-data question and reproduces the existing B=2000 source value.

```text
SOURCE_FINITE_ASSET_REUSED=true
TARGET_FINITE_ASSET_REUSED=true
NEW_COMPUTATION_JUSTIFIED=YES_BOUNDED_MATCHED_REPLAY
NEW_COMPUTATION_MAX_B=100000
NEW_STAGE19_ENUMERATOR=false
REPLAY_REPRODUCES_FROZEN_STAGE18_OVERLAP=true
FINITE_DATA_USED_AS_PROOF=false
```

## 7. Exit

Checkpoint20 has now supplied a reproducible matched finite baseline. The theorem-level survivor ratio belongs to checkpoint30, where the source asymptotic, target upper theorem, local zero-density route, leading-constant availability, directional refinements, and independent proof routes must be searched again under the Stage24 exploration policy.

```text
DISCOVERY_CHECKPOINT=20
DISCOVERY_LEDGER_STATUS=COMPLETE
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
UPSTREAM_PREMISE_CHECK=PASS
RETURN_TO_SOURCE_REQUIRED=false
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
