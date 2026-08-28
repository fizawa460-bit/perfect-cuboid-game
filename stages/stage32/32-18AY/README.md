# Stage32-18AY — B16 172-monster algorithm tournament

Status: READY_TO_ARM

The six cut39 walls have completed equal-budget tier3 measurement at 262144 nodes. Exactly 172 resource-capped parent-frontier states remain:

- p436/s5: 36
- p436/s362: 34
- p503/s118: 31
- p503/s665: 30
- p922/s13: 22
- p922/s38: 19

These are resource-capped frontier parents, not mathematical survivors.

## Decision order

1. Re-select the exact algorithm on monster states only.
2. If a clearly superior exact variant appears, apply it to all 172 monsters.
3. If no clear winner appears, selectively split only the 172 monster parents into child subfrontiers.
4. Resolve the light child branches first and isolate the residual pathological tail.

Blind whole-wall reruns and automatic B18 remain forbidden.

## Tournament scout

The current baseline is already known: every one of the 172 monsters failed to finish within 262144 planner nodes. Therefore baseline is not recomputed.

Take four deterministic representative monsters from each wall (24 total), chosen from the ordered monster-id list at approximately 0%, 33%, 67%, and 100% positions. Test two previously exact-safe variants at the same 262144-node per-state budget:

- `lower48`: the semantics-preserving lower-48 coordinate activity order from 32-18AG.
- `pairwise`: the exact rational pairwise Gram/KKT symmetry propagation from 32-18AH.

Run 12 heavy jobs total (2 algorithms x 6 walls), with `max-parallel: 6`. Each job processes only four explicit monster IDs. Raw planner CSV remains runner-local; persist only a compact result certificate. Expected artifact footprint is far below 1 MB total.

## Winner rule

A variant is a **clear winner** only if it materially improves the monster completion count over the known baseline zero and does not produce a severe runtime/node regression on the unresolved remainder. Prefer a variant that succeeds across multiple walls rather than a one-wall anomaly.

If neither variant completes a meaningful fraction of the 24-sample monster set, stop algorithm search and proceed directly to selective monster splitting. If one variant is clearly superior, run that variant over all 172 monster IDs before splitting. A combined lower48+pairwise variant is considered only if at least one single variant shows signal; do not multiply experimental branches without evidence.

## Firewalls

- No resolved cut39 parent is rerun.
- No whole-wall cut31 or blind tier4 is authorized by this scout.
- No B18 or higher is authorized.
- Resource-capped states are not promoted to mathematical survivors.
- Numerical/global/theorem/receiver/endpoint credit remain false.

## Next state

- clear winner: `32-18AZ_D16_B16_172_MONSTER_WINNER_FULL_RUN`
- no winner: `32-18AZ_D16_B16_172_MONSTER_SELECTIVE_SPLIT`
