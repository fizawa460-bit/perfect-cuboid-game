# Stage32 RESIDUAL_32_01 full178 heavy production release

Status: **RELEASE BOUNDED FULL178 HEAVY PRODUCTION CAMPAIGN / WAVE 1 ONLY**.

## Audited prerequisites

- full178 static preflight PR: `#1461`
- merge commit: `f9317affbeafd81af4f537667de8be2d3c64ae90`
- failed provenance audit: review `5057147138`
- repaired provenance hostile re-audit: review `5057163230`
- verdict: `PASS_SOURCE_PROVENANCE_REPAIR_SCOPE_LOCKED`
- exact residual manifest: 178 rows, m-class counts `23/23/44/88`
- exact coarse exceptional-mass strata count: `64111`
- first-pass node ceiling: `16,000,000`
- effective Stage32 heavy concurrency: `8 <= 18`
- projected compact-artifact peak from audited preflight: `7.78125 MB < 500 MB`

## MAIN release decision

The audited preflight is sufficient to release heavy production under the bounded fail-closed policy. This is authorization for the production **campaign**, not a claim that all 178 rows or 64111 strata complete in one run.

Generation 1 starts with eight lexicographic genus-0 residual rows:

```text
g0-d008
g0-d010
g0-d012
g0-d014
g0-d016
g0-d018
g0-d020
g0-d022
```

Each job receives at most 16M prefix-search nodes. A node ceiling is a resource wall only. Any incomplete stratum is discarded as a partial result and replaced by deterministic disjoint exact child work units. Remaining exceptional-mass strata in the row are emitted as a separate exact tail work unit. Therefore `UNKNOWN != UNSAT` is preserved mechanically.

The current production engine stage is explicitly the exact pairing-prefix layer. A completed prefix partition records a deterministic terminal-prefix stream commitment; it does **not** by itself complete the numerical Picard row. Later production phases must regenerate/consume these deterministic terminal streams and finish the exact leaf/Picard/orbit checks before numerical row credit is possible.

## Actions authorization

The production workflow is cold on PR open. Heavy compute may run only after a distinct synchronization changes **only**:

`stages/stage32/runkeys/residual32-01-full178-production.json`

and advances generation `0 -> 1` with `armed=true`, the audited manifest hash, review `5057163230`, eight locked wave-1 work units, concurrency 8, and all mathematical firewalls intact.

## Credit firewalls

```text
FULL178_HEAVY_PRODUCTION_AUTHORIZED=true
FULL_178_ROW_SWEEP_AUTHORIZED=true
B18_RELEASE_AUTHORIZED=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ROUTE_COLOR_CHANGE_AUTHORIZED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

`FULL_178_ROW_SWEEP_AUTHORIZED=true` means the bounded resumable production campaign is released. It does not mean the sweep has completed and it grants no mathematical credit by itself.

## Next gate

After generation 1 finishes, MAIN must ingest the compact wave manifest, verify exact child-work-unit coverage and any completed prefix partitions, then either arm the next bounded wave or expose a precise smaller execution wall. No row or receiver closure is allowed from prefix-wave completion alone.
