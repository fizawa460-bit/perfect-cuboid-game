# Stage32 RESIDUAL_32_01 post-audit production release decision

Status: **RELEASE FULL178 PREFLIGHT / DO NOT RELEASE FULL178 HEAVY SWEEP**.

## Locked input

- merged representative-calibration PR: `#1456`
- merge commit: `a4027b54ff57c556f9a2d1cb9448bb5c8c1affbb`
- hostile audit review: `5056772158`
- hostile audit verdict: `PASS_RESIDUAL32_01_REPRESENTATIVE_COST_FEASIBILITY_SCOPE_LOCKED`
- locked representative completion nodes:
  - `m=1`: `14,526,419`
  - `m=2`: `6,194,539`
  - `m=4`: `10,360,479`
  - `m=8`: `8,277,509`

The four audited representatives establish that the exact pairing-prefix engine can complete one locked row in every `m in {1,2,4,8}` class below the tested 16M-node ceiling. They do **not** establish a worst-case bound over the 178 residual `(g,d)` rows.

## Decision

The next Stage32 MAIN item is released narrowly as:

`RESIDUAL32_01_FULL178_PRODUCTION_PREFLIGHT_AND_SHARD_POLICY`

This release authorizes repository-local planning and implementation needed to turn the representative engine into a safe 178-row production campaign. It does **not** authorize the all-178 heavy sweep.

The preflight must, before any heavy production arming:

1. materialize and hash-lock the exact 178-row manifest obtained from the audited 183-row receiver window after removing the audited degree-`<=6` catalogue rows;
2. assign every residual row to its exact `m` class and preserve `(g,d)` semantics;
3. define deterministic row/work-unit IDs and a bounded wave/shard policy;
4. project compute from the audited representative completion curves without treating them as worst-case bounds;
5. define a fail-closed per-row node/time ceiling and escalation path for rows exceeding the representative envelope;
6. preflight effective Stage32 heavy concurrency `<=18` and preserve headroom for other stages;
7. preflight Actions artifact storage under the repository 500 MB operating budget, using compact post-verification certificates and no requirement that raw exhaustive shards coexist in artifact storage;
8. add or revise a dedicated run key whose commit-range authorization gate is required before any heavy job;
9. keep the production workflow cold until the manifest, shard policy, storage projection, concurrency projection, and evidence contract are reviewable together.

## Why the full sweep is not released yet

Representative completion removes the previous feasibility blocker but does not certify the maximum cost among all 178 rows. Launching all 178 now would silently promote representative evidence into a population-wide cost claim and would violate the repository promotion firewall.

Therefore:

```text
FULL178_PREFLIGHT_RELEASED=true
FULL178_HEAVY_SWEEP_AUTHORIZED=false
B18_RELEASE_AUTHORIZED=false
HEAVY_COMPUTE_ARMED=false
PRODUCTION_COST_READY=false
```

`PRODUCTION_COST_READY` may become true only after the preflight supplies a bounded production policy that can fail closed on unexpectedly expensive rows; it does not require pretending that the four representatives prove a worst-case theorem.

## Mathematical firewalls

This is an operational downstream release only. It changes no mathematical credit.

```text
D16_B16_NUMERICAL_CREDIT=true
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ROUTE_COLOR_CHANGE_AUTHORIZED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Next MAIN target

Implement the cold full178 manifest + production preflight package. Do not launch the heavy sweep in the same step unless a later controller state explicitly authorizes it after the required Actions safety preflight.