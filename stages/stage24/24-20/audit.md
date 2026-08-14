# Stage24-20 fresh audit

AUDIT_VERDICT=FAIL
CHECKPOINT=20
PR=973

## Accepted

The checkpoint20 million-scale matched finite census is accepted as exact finite evidence under the Stage24 literal population contract.

- `M2(B)` and `N2(B)` are counted on the same primitive canonical exactly-two-face population under `R<=B`.
- `N2` is imposed only by the final exact-square predicate on `R^2`; no space-integral source pruning contaminates `M2`.
- The merged r202 source-level overlap at `B=200000` checks legacy Stage15, one-shard streaming and multi-shard streaming equality.
- The exact shared-edge shard cover, exactly-two unique common-edge multiplicity, and triple multiplicity-three gates are accepted.
- Target-side `N2` cross-oracles at `B=200000,500000,1000000` agree.
- The frozen matched panel through `B=1000000` is accepted.
- The repaired r202 displayed ratio is correct:
  `116/1896505 = 0.000061165143250347...`.
- The finite slopes and directional rates are used only diagnostically; no asymptotic exponent or directional limit is promoted.

## FAIL reason

The history-backflow repair is incomplete.

PR #973 correctly repairs the stale displayed `B=200000` ratio in merged `24-14num-r202/result.md`, but merged `24-14num-r203/result.md` still contains the copied stale value

`0.0000611651567`

for the same exact counts `M2=1896505`, `N2=116`.

The correct value is

`0.000061165143250347...`.

This is a derived-display typo only. It does not change any count, finite slope conclusion, population contract, or checkpoint20 mathematics. However the Stage24 controller requires `HISTORY_SUPERSESSION_BACKFLOW_REQUIRED=true`, so correcting the origin while leaving a dependent merged interpretation artifact stale is not a fully synchronized repair.

## Minimal repair

Update only `stages/stage24/24-14num-r203/result.md` so its 200k displayed ratio matches the corrected exact division. Add a short note that counts and conclusions are unchanged.

No recomputation is required. Do not reopen r201/r202 enumeration, checkpoint20 census, Stage19 target theory, or checkpoint30+ work.

```text
CHECKPOINT20_FINITE_CENSUS_ACCEPTED=true
R202_COUNT_CORRECTNESS_ACCEPTED=true
R202_RATIO_REPAIR_ACCEPTED=true
R203_STALE_RATIO_BACKFLOW_FOUND=true
REPAIR_SCOPE=R203_DERIVED_RATIO_DISPLAY_SYNC_ONLY
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=20
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```
