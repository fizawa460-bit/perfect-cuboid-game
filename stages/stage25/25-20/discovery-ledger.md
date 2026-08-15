# Stage25-20 discovery / reuse ledger

CHECKPOINT=20
STATUS=COMPLETE_PENDING_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
STRONGEST_KNOWN_CHECK=PASS
DISCOVERY_CHECKPOINT=Stage25-20
```

## SEARCHED_PATHS

- `stages/stage16/16-20/counts.csv` — audited finite `M1` source grid.
- `stages/stage16/16-20/enumerate.py` — audited source enumerator; inspected but not rerun for new larger cutoffs.
- `stages/stage19/19-20/counts.csv` — frozen finite `N2` target oracle.
- `stages/stage21/21-20/result.md` — confirms the same Stage16 finite source grid and cross-population conventions.
- `stages/stage22/22-20/result.md` — confirms exact Stage16/Stage18 matched finite conventions.
- `stages/stage24/24-20/matched-counts.csv` — current `M2,N2` target-side finite panel.
- `docs/stage14-num-reuse-index.md` — mandatory Stage14 numerical routing interface.
- `stages/stage14/data/14-num-alpha11/b500m_manifest.json` — terminal NUM-R01 exact manifest.
- `stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64` — exact physical object ledger used for projection.
- PR #980 — audited Stage25 checkpoint10 contract and reuse handoff.
- PR #981 — current checkpoint20 deterministic replay.

## SEARCH_TERMS

```text
M1 finite counts
N2 finite counts
Stage16 Stage19 common cutoff
matched endpoint grid
NUM-R01 exact object ledger
exactly two faces integral space d<=B
Stage24 matched counts
```

## STRUCTURAL_SIGNATURES

```text
PRIMITIVE_CANONICAL_OBJECTS
EXACTLY_ONE_FACE_SOURCE
EXACTLY_TWO_FACE_PLUS_SPACE_TARGET
COMMON_R_CUTOFF
INTEGRAL_SPACE_DIAGONAL
EXACT_FINITE_LEDGER_PROJECTION
NON_SUBSET_POPULATION_RATIO
```

## DEPENDENCY_NEIGHBORS

```text
Stage16-20
Stage19-20
Stage21-20
Stage22-20
Stage24-20
Stage14 NUM-R01/NUM-R02
Stage25-10
```

## CANDIDATES_FOUND

### C25-20-A — Stage16-20 frozen source table

`M1` exists at `50,100,200,400,800,1200,1600,2000` under the exact Stage25 source contract.

Verdict: `ACCEPT_EXACT_SOURCE_COUNTS`.

### C25-20-B — Stage19-20 frozen target table

`N2` exists at `1000,2000,5000,...,100000` under the exact Stage25 target contract.

Verdict: `ACCEPT_AS_TARGET_CROSS_ORACLE`, but the direct source/target grid intersection is only `B=2000`.

### C25-20-C — NUM-R01 500m physical-object ledger

The manifest freezes 3495 primitive canonical integral-space objects with at least two integral faces and `triple=0` through `B=500,000,000`. Therefore every ledger row in this finite dataset has exactly two integral faces. Filtering by `d<=B` is an exact Stage19 `N2(B)` projection.

Verdict: `ACCEPT_WITH_EXACT_POPULATION_ADAPTER`.

### C25-20-D — Stage24-20 `M2,N2` panel

Contains high-quality `N2` values through `1,000,000`, but its denominator is `M2`, not Stage25's `M1`.

Verdict: `REJECT_AS_DIRECT_STAGE25_DENOMINATOR`; retain as target-side cross-check only.

### C25-20-E — Stage21-20 `M1,N1,S_all` panel

Provides the same `M1` grid and confirms conventions, but `N1`/`S_all` are not the Stage25 target.

Verdict: `ACCEPT_M1_CONVENTION_CROSSCHECK`; reject `N1,S_all` as endpoint counts.

### C25-20-F — Stage22-20 `M1,M2` panel

Provides the exact same `M1` source counts and population-size ratio semantics for disjoint face masks.

Verdict: `ACCEPT_SOURCE_REGRESSION_AND_SEMANTICS_CROSSCHECK`; `M2` is not Stage25 target.

### C25-20-G — rerun Stage16 source census on Stage19's large grid

Would require substantially more work and is unnecessary once the exact target ledger can instead be projected onto the already audited Stage16 grid.

Verdict: `REJECT_UNNECESSARY_NEW_CENSUS`.

## CANDIDATES_ACCEPTED

```text
Stage16-20/counts.csv -> exact M1 source counts
NUM-R01 b500m object ledger -> exact finite N2 projection after adapter
Stage19-20/counts.csv -> exact N2 cross-oracle
Stage21-20 -> source convention regression
Stage22-20 -> source count/ratio semantics regression
Stage24-20 -> target-side N2 regression
NUM-R02 -> independent finite regression provenance
```

## CANDIDATES_REJECTED_WITH_REASON

```text
Stage24-20 M2 denominator -> wrong Stage25 denominator population
Stage21-20 N1 and S_all -> wrong Stage25 target population
Stage22-20 M2 -> intermediate population only
new Stage16 large-grid census -> unnecessary; exact ledger projection supplies an 8-row matched grid without new enumeration
finite power-law fit -> forbidden because sparse step-function numerator and nonmonotone finite ratio
```

## POPULATION_ADAPTERS_PROVED

### A25-20-NUM-R01-to-N2

```text
SOURCE=NUM-R01 b500m object ledger
SOURCE_CANONICAL=0<a<b<c
SOURCE_PRIMITIVE=gcd(a,b,c)=1
SOURCE_SPACE=d integral and d^2=a^2+b^2+c^2
SOURCE_FACE_MASK=at least two integral faces
MANIFEST_TRIPLE_COUNT=0 through B=500000000
TARGET=Stage19 exactly-two + integral space
CUTOFF_MAP=d<=B iff R<=B on target
MULTIPLICITY=one physical canonical object per row
ADAPTER_STATUS=PROVED_EXACT_FINITE
```

The replay verifies canonical order, primitivity and the exact space identity row-by-row, verifies the 3495-row terminal manifest count, and reproduces all frozen Stage19-20 `N2` counts before materializing the Stage25 grid.

### A25-20-Stage16-to-M1

No adapter is required: `stages/stage16/16-20/counts.csv` is literally the Stage25 source population under the same `R<=B` convention.

## Computation decision

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_LEDGER_PLUS_AUDITED_SOURCE_COUNTS
NUM_NEW_COMPUTATION_JUSTIFIED=NO_NEW_ENUMERATION_LEDGER_FILTER_ONLY
NEW_RESEARCH_JUSTIFIED=EXACT_LEDGER_PROJECTION_ONLY_BECAUSE_FROZEN_ENDPOINT_GRIDS_SHARED_ONLY_B_2000
```

The operation performed at checkpoint20 is deterministic filtering/replay of a frozen exact dataset, not a new population search.

## New finite deductions

1. The Stage25 endpoint numerator is zero at the first four Stage16 sample cutoffs and first becomes nonzero on this **sample grid** at `B=800`.
2. The ratio is nonmonotone because `N2` is sparse and stepwise: it rises from `800` to `1200`, then falls while the numerator remains five.
3. This nonmonotonicity is a finite-data warning against fitting a single power exponent from the small window.
4. The exact Stage19 cross-oracle equality shows the NUM-R01 adapter is not merely population-plausible; it reproduces the frozen target counts on an independent threshold panel.

No asymptotic inference is made.

```text
DISCOVERY_LEDGER_STATUS=COMPLETE
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PENDING
FINITE_DATA_USED_AS_PROOF=false
```
