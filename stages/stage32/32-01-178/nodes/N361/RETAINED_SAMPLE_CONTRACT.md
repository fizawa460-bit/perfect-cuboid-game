# Stage32 32-01-178 N361 — retained canonical-rank selected64 sidecar sample

Status: `AUDIT_REQUIRED_RETAINED_SAMPLE_NO_MAIN_CREDIT`.

## Retained sample

The exact-head generation run `34669281836` at commit
`7a8a99877ef3bbf4e5a3fcd15ad1e3d8cfaf92a0` produced one exact sidecar for
the retained N342 boundary terminal

`g0-d176, e=48, filtered_rank/x4=3`.

Its route-independent N104 terminal identity is

`g0-d176|e=48|rank=37830303724188`.

The retained record contains the complete `picard64_coordinates[64]` and
`selected64_pairings[64]`.  The retained replay independently reconstructs the
source-locked Picard/Hperp data and checks

`Psel * picard64_coordinates = selected64_pairings`.

It also replays the all-140 pairing vector, `[1]^48` exceptional pairings,
normal mass `3104`, degree `176`, `C^2=-1784`, and the scalar

`N = (16/gcd(d,16))^2 * (d^2/16 - C^2) = 3720`.

## Identity semantics

The authoritative inner identity is the old compressed-terminal rank required
by N104.  The N220 filtered rank is historical provenance only and is not used
as final coverage identity.

This sample is an interface proof-of-composition only.  It is not evidence
that all current N358 survivors have sidecars and it creates no N104 coverage.

## Replay boundary

The normal CI gate executes only the solver-independent retained replay.
The one-shot QF_LIA generator remains retained as provenance but is not run by
ordinary PR synchronization.

## Credit ceiling

`N361_SAMPLE_SIDECAR_RETAINED=true`

`N361_SAMPLE_COUNT=1`

`N361_MAIN_PRUNING_CREDIT=false`

`N104_COVERAGE_CREDIT=false`

`FULL178_COMPLETE=false`

`N350_REGISTERED=false`

`EFFECTIVITY_FINAL=false`

`INTEGRAL_IRREDUCIBLE_MEMBER_CLAIM=false`

`RECEIVER_CREDIT=false`

`THEOREM_CREDIT=false`

`ENDPOINT_CREDIT=false`

`STAGE32_CLOSED=false`

`PERFECT_CUBOID_EXISTENCE_CLAIM=false`

`PERFECT_CUBOID_NONEXISTENCE_CLAIM=false`

`HEAVY_COMPUTE_AUTHORIZED=false`

`MERGE_AUTHORIZED=false`
