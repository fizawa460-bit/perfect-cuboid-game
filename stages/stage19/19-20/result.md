# Stage19-20 — finite-data baseline

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 counts the literal Stage15 numerator population
\[
\mathcal A_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly two integral face diagonals},\ R\in\mathbf Z\},
\]
with count \(N_2(B)\).

## 1. Exact census transfer

Stage19-10 established a literal population/cutoff/multiplicity match with Stage15 `A_2(B)`. Therefore the exact Stage15-3 matched numerical baseline transfers without an adapter.

Frozen exact counts:

| B | N_2(B) |
|---:|---:|
| 1,000 | 2 |
| 2,000 | 5 |
| 5,000 | 15 |
| 10,000 | 25 |
| 20,000 | 42 |
| 50,000 | 62 |
| 100,000 | 89 |

The Stage15 source additionally records `M_2(100000)=796698` and survival ratio `89/796698 = 0.00011171108751371284`, but Stage19-20 freezes only the numerator census as its own finite baseline.

## 2. Provenance

Canonical source:

- `stages/stage15/15-3/result.md`
- `stages/stage15/evidence/stage15_3_baseline.json`
- `stages/stage15/scripts/stage15_3_compare.py`
- `stages/stage15/replay/verify_stage15_3.py`

The source JSON explicitly marks `counts_exact_on_grid=true`, `finite_data_only=true`, and `survival_asymptotic_inferred=false`.

Stage19 CSV:

- `stages/stage19/19-20/counts.csv`
- SHA-256: `d9535d89dcd84b432150eda798fa42506e8412220abd4e3f425bf8a804448873`

No new enumerator is introduced because duplicating the already validated literal-match Stage15 enumerator would create a second implementation for the same population without adding evidence.

## 3. Interpretation discipline

The survivor count is only 89 even at `B=100000`. The predeclared Stage15-3 gate for global survivor-slope interpretation was `N_2>=200`, so it remains failed.

Consequently this checkpoint does **not** infer:

- an asymptotic for `N_2(B)`;
- a true polynomial exponent;
- sharpness of the known `B^(1/2+epsilon)` upper bound;
- directional survival rates;
- an independence law for the space-diagonal condition.

The frozen Stage14/15 theorems remain separate theorem-level provenance for later checkpoints.

```text
EVIDENCE_LEVEL=COMPUTED
PARENT_STAGE=Stage19
PARENT_CLASS=population_state
TARGET_POPULATION=A_2(B)
COUNT=N_2(B)
FINITE_BASELINE_SOURCE=Stage15-3 exact matched census
POPULATION_ADAPTER_REQUIRED=false
CUTOFF_ADAPTER_REQUIRED=false
MULTIPLICITY_ADAPTER_REQUIRED=false
THRESHOLDS=1000,2000,5000,10000,20000,50000,100000
COUNTS_N2=2,5,15,25,42,62,89
CSV_SHA256=d9535d89dcd84b432150eda798fa42506e8412220abd4e3f425bf8a804448873
FINITE_DATA_USED_AS_PROOF=false
SURVIVOR_SLOPE_GATE=N2>=200
SURVIVOR_SLOPE_GATE_STATUS=FAIL
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=30
CODEX_REQUIRED=false
CODEX_REASON=Literal transfer of an already validated exact matched census; no new implementation is needed.
```
