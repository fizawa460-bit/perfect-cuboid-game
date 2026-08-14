# Stage24-20 discovery ledger r2

CHECKPOINT=20
STATUS=COMPLETE

## Search order actually used

1. Stage24 literal population contract from checkpoint10.
2. Stage14 numerical reuse index and AR-040/NUM-R01-R03.
3. Merged `24-14num-r201` bootstrap.
4. Merged `24-14num-r202` scalable exact census.
5. Pre-r202 Stage15 paired enumerator for independent overlap.
6. Earlier Stage14 exact N2 checkpoints as target-side cross-oracles.
7. r203 was inspected only as an in-progress audit lane and was not used as a correctness premise.

## Assets found

### D20-R01 — r201 matched bootstrap

Population match is exact. `M2` is generated without a space requirement and `N2` is the final space-square subset on the same objects.

### D20-R02 — r202 scalable matched census

Exact matched data extend to B=1,000,000. r202 changes architecture only: shared-edge sharding/streaming instead of a global object dictionary.

### D20-R03 — legacy Stage15 overlap

At B=200,000 the old exact paired enumerator is directly compared to one-shard and multi-shard r202 output over totals, directional counts, triples and workload diagnostics.

### D20-R04 — Stage14 target cross-oracles

Previously frozen integral-space N2 counts independently match the r202 target side at B=200k, 500k and 1m. They validate N2 transcription but are not used as an M2 denominator.

## New finding during main-lane revalidation

The merged r202 `result.md` displayed `N2/M2=0.0000611651567` at B=200000. Direct division of the frozen exact counts gives

`116/1896505 = 0.000061165143250347...`.

This is a derived-display typo only. The counts, directional totals, legacy equality and CI output are not changed. The replacement checkpoint20 branch repairs the displayed value.

```text
R202_COUNT_ERROR_FOUND=false
R202_DERIVED_RATIO_DISPLAY_TYPO_FOUND=true
R202_RATIO_TYPO_MATHEMATICALLY_MATERIAL=false
```

## Research interpretation

The enlarged matched panel makes the finite exponent look less stable, not more theorem-like. The old 1k→100k ratio endpoint slope was about -0.494; the 100k→1m slope is about -0.782. No single finite exponent is promoted.

The one-million directional survival rates are unequal on this finite window, but no directional asymptotic law is inferred.

## Reuse protocol

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_MATCHED_CENSUS
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_AFTER_MERGED_R202
```

## Boundary

No claim of exhaustive theorem search, no new upper/lower theorem, no unboundedness, no half-power sharpness, and no perfect-cuboid conclusion is made at checkpoint20.

NEXT=FRESH_STAGE24_AUDIT_CHECKPOINT20
