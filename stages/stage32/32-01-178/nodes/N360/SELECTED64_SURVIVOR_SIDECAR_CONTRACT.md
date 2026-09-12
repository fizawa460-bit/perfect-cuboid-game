# Stage32 32-01-178 N360 — selected64 survivor witness sidecar bridge

Status: `RESEARCH_PREFLIGHT_NO_MAIN_CREDIT`.

## Purpose

N359 hostile audit closes the N356/N357 optimistic transport-plus-support relaxation: further pruning must introduce information outside that relaxation. The next load-bearing interface is the per-survivor Picard witness required by the 32-02 exact scalar/Riemann--Roch route.

N104 already fixes the route-independent terminal identity as a canonical indexed terminal rank inside each coarse stratum `(row_id,e)`. Therefore N360 does **not** invent another terminal numbering. It defines a sidecar keyed by the N104 identity

`(row_id, e, terminal_rank)`.

The existing N357/N358 retained results are aggregate censuses and do not retain enough per-survivor data to reconstruct a Picard64 class. N360 is an interface/producer preflight only; it does not assert that the current 47,589,703,313,957,134,966,240 compressed terminals have been expanded or checked numerically.

## Source-locked Picard interface

The current tree retains the four files used by the independent 32-02 scalar-producer research:

- `pairing_prefix_engine.py` — blob `c8e87c6598fa1cd7ba1675fc35fa83bea983c94b`;
- `hperp_integral_adapter.py` — blob `fb1eb380ca786e42a6b00c5ef454b0e79fdba771`;
- `picard_base_rows_retained.py` — blob `82e4d450a1d852e34f6615440fb88a029c6e54eb`;
- `stage32_picard_marking_retained.py` — blob `5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7`.

The Picard bundle canonical SHA256 remains
`d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c`.

PR #1790 is a **non-authoritative compatibility reference only** at this checkpoint. Its draft protocol expects `row_id`, `terminal_identity`, `d`, an integral `picard64_coordinates` vector, exact `selected64_pairings`, matrix/Gram commitments, and source locks before deriving `C2` and `negative_hperp_square_N`. N360 deliberately stops one layer earlier: it defines the 32-01 witness sidecar needed to feed such a consumer after that external route is independently audited.

## Sidecar record

Every eventual survivor witness record must contain:

```text
schema = STAGE32_32_01_178_SELECTED64_SURVIVOR_SIDECAR_V1
row_id
e
terminal_rank
terminal_identity = "{row_id}|e={e}|rank={terminal_rank}"
d
selected64_pairings[64]        exact integers
picard64_coordinates[64]       exact integers
selected_pairing_matrix_sha256
gram64_sha256
picard64_coordinates_sha256
witness_source_locks
coverage_source
```

The producer must additionally prove, under the locked retained matrix data,

`Psel * picard64_coordinates = selected64_pairings`.

An asserted coordinate vector or asserted scalar without this replay is not creditable.

## Completeness integration

N104 remains authoritative for final coverage. A sidecar may only attach to a canonical N104 terminal rank. It cannot create coverage. For a terminal to be passed to 32-02, the final producer must provide both:

1. the normalized N104 coverage identity `(row_id,e,rank)`;
2. the source-locked selected64/Picard64 witness sidecar for that same identity.

No sidecar record may promote an aggregate stratum count into per-terminal evidence.

## Current exact gap

At this checkpoint:

```text
N359_ROUTE_EXHAUSTION_HOSTILE_AUDIT_PASS=true
N359_ADDITIONAL_PRUNING=0
CURRENT_AUTHORITATIVE_REMAINING_STRATA=17128
CURRENT_AUTHORITATIVE_REMAINING_TERMINALS=47589703313957134966240

SIDECAR_SCHEMA_DEFINED=true
ACTUAL_CURRENT_SURVIVOR_SIDECARS_EMITTED=0
RANK_TO_SELECTED64_WITNESS_PRODUCER_IMPLEMENTED=false
FULL178_NUMERICAL_PICARD_LEAF_CHECKS_COMPLETE=false
```

The next bounded implementation unit is a fail-closed **rank-to-selected64 witness producer** on a small deterministic sample, preserving the N104 canonical terminal identity. Only after that sample replays exactly should it be generalized/sharded.

## Firewalls

This node grants no pruning, no FULL178 completion, no 32-02 effectivity-final credit, no irreducible/member/genus claim, no N104 release, no N350 producer registration, no receiver/theorem/endpoint/Stage32/Perfect-Cuboid credit, no heavy authorization, and no merge authorization.
