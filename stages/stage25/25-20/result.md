# Stage25-20 — matched finite Stage16 / Stage19 endpoint baseline

EVIDENCE_LEVEL=COMPUTED_EXACT_REPLAY
CHECKPOINT=20
STATUS=COMPUTED_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Reuse-first computation decision

Checkpoint10 required a matched finite `M1(B),N2(B)` grid under the common physical cutoff `R<=B`.

The frozen endpoint tables did not already provide a useful shared panel:

- Stage16-20 has `M1` at `B=50,100,200,400,800,1200,1600,2000`;
- Stage19-20 has `N2` at `B=1000,2000,5000,...,100000`;
- their literal intersection is only `B=2000`.

Rather than launch a new cuboid census, Stage25 projects the audited Stage14 `NUM-R01` exact object ledger onto the already frozen Stage16 thresholds. The NUM-R01 ledger contains the primitive canonical integral-space population with at least two integral faces through `B=500,000,000`; its terminal manifest freezes `triple=0`, so every ledger row is exactly-two on this finite range. Thus selecting `d<=B` is an exact Stage19 `N2(B)` adapter.

```text
NEW_CUBOID_ENUMERATION_PERFORMED=false
EXACT_LEDGER_FILTER_ONLY=true
SOURCE_COUNTS=stages/stage16/16-20/counts.csv
TARGET_OBJECT_LEDGER=stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64
TARGET_MANIFEST=stages/stage14/data/14-num-alpha11/b500m_manifest.json
TARGET_CROSS_ORACLE=stages/stage19/19-20/counts.csv
```

## 2. Matched finite grid

| B | M1(B) | N2(B) | N2/M1 |
|---:|---:|---:|---:|
| 50 | 490 | 0 | 0 |
| 100 | 2,620 | 0 | 0 |
| 200 | 12,664 | 0 | 0 |
| 400 | 59,574 | 0 | 0 |
| 800 | 273,901 | 1 | 3.65095417687413e-6 |
| 1,200 | 662,207 | 5 | 7.55050913083069e-6 |
| 1,600 | 1,234,822 | 5 | 4.04916660053028e-6 |
| 2,000 | 1,997,863 | 5 | 2.50267410728363e-6 |

Frozen machine table: `stages/stage25/25-20/matched-counts.csv`.

The replay also reproduces every Stage19-20 frozen `N2` count (`B=1000` through `100000`) from the same NUM-R01 object ledger before accepting the Stage25 grid.

```text
STAGE19_CROSS_ORACLE=PASS
NUM_R01_ADAPTER=PASS
COMMITTED_MATCHED_GRID=PASS
```

## 3. Finite interpretation

The target is extremely sparse in this small window. On the chosen Stage16 grid the numerator is a step function

```text
N2=0,0,0,0,1,5,5,5.
```

Consequently `N2/M1` is **not monotone** on the frozen panel: it rises when four new target objects enter between the `800` and `1200` thresholds and then falls while `N2` remains fixed and `M1` grows.

This is useful negative evidence against naive finite power fitting. It is not evidence against the theorem-level zero-density result, nor does it identify the true Stage25 exponent. In particular:

- `N2=0` at finitely many small cutoffs is not nonexistence;
- the grid's first nonzero sample at `B=800` is not claimed to be the globally first Stage19 object;
- the local rise from `800` to `1200` is not asymptotic enhancement;
- the later decline is not an asymptotic exponent estimate.

Checkpoint30 must derive the combined ratio class from the audited endpoint theorems and then use this finite panel only as a transcription/regression diagnostic.

## 4. Reuse and evidence handoff

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=Stage16-20,Stage19-20,Stage21-20,Stage22-20,Stage24-20,NUM-R01
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=EXACT_LEDGER_PROJECTION_ONLY_BECAUSE_FROZEN_ENDPOINT_GRIDS_SHARED_ONLY_B_2000

NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_LEDGER_PLUS_AUDITED_SOURCE_COUNTS
NUM_NEW_COMPUTATION_JUSTIFIED=NO_NEW_ENUMERATION_LEDGER_FILTER_ONLY

FINITE_DATA_USED_AS_PROOF=false
FINITE_POWER_FIT_PROMOTED=false
FINITE_RATIO_MONOTONE=false
TRUE_RATIO_EXPONENT_IDENTIFIED=false
COUNTS_RECOMPUTE_REQUIRED=false
```

Concrete discovery evidence is recorded in `stages/stage25/25-20/discovery-ledger.md`.

## 5. Checkpoint20 exit

```text
CHECKPOINT20_STATUS=COMPUTED_SUBMITTED_FOR_FRESH_AUDIT
MATCHED_GRID_REQUIRED=true
MATCHED_GRID_MATERIALIZED=true
MATCHED_GRID_MAX_B=2000
MATCHED_GRID_ROWS=8
NEW_LARGE_CENSUS_PERFORMED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=20
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
