# Stage25-20 fresh audit

Status: **PASS**

## Audit scope

This audit checks the checkpoint20 matched finite baseline for the Stage25 endpoint comparison `Stage16 -> Stage19` under the frozen common physical cutoff `R<=B`.

## Accepted source panel

`stages/stage16/16-20/counts.csv` is the audited exact primitive/canonical exactly-one-face source census. The checkpoint20 panel reuses its eight frozen thresholds without changing the source population or cutoff:

```text
B=50,100,200,400,800,1200,1600,2000
M1=490,2620,12664,59574,273901,662207,1234822,1997863
```

No source adapter is required.

## Accepted target adapter

The Stage14 NUM-R01 ledger is a frozen exact primitive/canonical integral-space ledger with at least two integral faces. Its audited B500m manifest records `total=3495`, `distinct_physical_cuboids=3495`, and `triple=0`, so every ledger object in the finite range is exactly-two rather than three-face.

During this fresh audit, `replay_matched_grid.py` was strengthened without changing any count or conclusion. It now:

1. binds the reused base64, bz2, and decompressed CSV bytes to the frozen manifest SHA-256 values;
2. verifies the manifest row count and `triple=0` directly;
3. checks every one of the 3495 rows for strict canonical order, global primitivity, and integral space identity;
4. recomputes all three face-square predicates on every row and requires **exactly two** integral faces;
5. reproduces the frozen Stage19-20 target counts before accepting the Stage25 grid.

Thus the finite NUM-R01 -> Stage19 `N2` adapter is certified directly at checkpoint20, not merely inferred from matching row totals.

## Matched panel

The deterministic replay gives

| B | M1(B) | N2(B) | N2/M1 |
|---:|---:|---:|---:|
| 50 | 490 | 0 | 0 |
| 100 | 2620 | 0 | 0 |
| 200 | 12664 | 0 | 0 |
| 400 | 59574 | 0 | 0 |
| 800 | 273901 | 1 | 3.65095417687413e-6 |
| 1200 | 662207 | 5 | 7.55050913083069e-6 |
| 1600 | 1234822 | 5 | 4.04916660053028e-6 |
| 2000 | 1997863 | 5 | 2.50267410728363e-6 |

The committed `matched-counts.csv` agrees exactly.

## Finite interpretation

The submission keeps the evidence boundary correctly.

- The ratio is nonmonotone on this small sparse grid because the numerator jumps from 1 to 5 and then stays fixed.
- `B=800` is only the first nonzero **sample threshold**, not a claim about the globally first Stage19 object.
- No finite slope, power law, asymptotic exponent, independence claim, or theorem-level thinning law is inferred from this panel.
- Checkpoint30 must use the audited endpoint theorems for the combined ratio law and use the finite panel only as a regression/transcription diagnostic.

## Reuse/discovery audit

The checkpoint20 discovery ledger satisfies the required Stage21-28 evidence contract: searched paths, search terms, structural signatures, dependency neighbors, accepted/rejected candidates, and population adapters are all explicit. Reuse-first was followed; no unnecessary new large Stage16 or Stage19 census was launched.

`NUM-R01` is the actual finite target projection asset. `NUM-R02` is retained only as independent enumerator/regression provenance and is not used as a second mathematical count or multiplied into the evidence.

## Verifier state

`checkpoint20_submission_audit.py` was made audit-state aware so the same deterministic contract checks both the submitted PENDING state and this post-audit PASS state. This changes no mathematics or finite counts.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
CHECKPOINT20_FINITE_BASELINE_ACCEPTED=true
SOURCE_M1_COUNTS_ACCEPTED=true
NUM_R01_MANIFEST_BINDING_ACCEPTED=true
NUM_R01_EXACTLY_TWO_ROW_CHECK_ACCEPTED=true
STAGE19_CROSS_ORACLE_ACCEPTED=true
COMMITTED_MATCHED_GRID_ACCEPTED=true
FINITE_RATIO_NONMONOTONICITY_ACCEPTED=true
FINITE_POWER_FIT_PROMOTED=false
FINITE_DATA_USED_AS_PROOF=false
TRUE_RATIO_EXPONENT_IDENTIFIED=false
NEW_LARGE_CENSUS_REQUIRED=false
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=30
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #981; then Stage25-main-batch
```
