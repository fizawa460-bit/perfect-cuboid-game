# Stage32 32-01-178 N361 — one exact canonical-rank selected64 sidecar sample

Status: `RESEARCH_GENERATION_NO_MAIN_CREDIT`.

## Goal

Exercise the N360 bridge on one real retained 32-01 boundary terminal without changing
Stage32 authority. The sample is the retained N342 terminal

`g0-d176, e=48, filtered_rank/x4=3`.

N342 already records this terminal inside its 21 exact Picard-SAT boundary terminals and
records that all 21 possess exact old-rank locators. N361 does not promote the N342 leaf
set to current MAIN coverage; it uses one member only as a deterministic integration test.

## Canonical terminal identity

The route-independent N104 identity is the old compressed-terminal rank in stratum
`(row_id,e)`. N361 reconstructs the exact 11-coordinate compressed terminal using the
locked production indexer and requires rank/unrank roundtrip before emitting

`terminal_identity = "{row_id}|e={e}|rank={terminal_rank}"`.

The filtered N220 rank is retained only as historical provenance and is not the final
coverage identity.

## Picard witness generation

The generator source-locks, before execution, the retained compressed terminal family and
indexer, pairing-prefix engine, Hperp integral adapter, Picard64 bundle, Stage32 marking,
and N342 retained result. It then solves one exact integer linear Picard feasibility
problem for the sample:

- all 48 exceptional labelled pairings equal `1`;
- all 92 normal pairings are nonnegative;
- normal pairing mass is `3104`;
- label 49 pairing is `3`;
- canonical degree is `176`.

A SAT model is replayed entry-for-entry against the retained 140x64 pairing matrix. The
emitted sidecar contains the full `picard64_coordinates[64]` and the full
`selected64_pairings[64]`, and independently checks

`Psel * picard64_coordinates = selected64_pairings`.

This generation step is not required to select a canonical Picard witness; after one exact
witness is frozen, the retained verifier will replay that fixed vector rather than trust
future solver model choices.

## Credit ceiling

This is one sample sidecar only. It creates no N104 coverage, no pruning, no N350
registration, no FULL178 completion, no 32-02 effectivity-final credit, no
integral/irreducible/member/genus claim, no receiver/theorem/endpoint/Stage32/Perfect
Cuboid credit, no heavy-compute authorization, and no merge authorization.

## Next gate

After exact-head CI emits the sample JSON, freeze that exact record as `RESULT.json`, add
a solver-independent replay verifier for the retained vector, replace the generation gate
with the retained replay gate, and then route the frozen N361 sample to independent hostile
audit if it is to be used as an interface authority.