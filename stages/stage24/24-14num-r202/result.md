# 24-14num-r202 — scalable exact matched census

STATUS=SUBMITTED_FOR_CI
PARENT_STAGE=Stage24
TRACK_ROLE=ADDITIONAL_NUMERICAL_RESEARCH
BASELINE=24-14num-r201 / PR #969

## Frozen scope

This lane preserves the r201 population exactly and changes only enumeration architecture. It computes the literal same-object transition

`M2(B) -> N2(B) = M2(B) intersect {R integral}`

for primitive canonical exactly-two-face cuboids under `R<=B`.

## One-dispatch ladder

The workflow has a hard-coded, dependency-gated ladder:

1. `B=200000`: legacy r201 enumerator = one-shard streaming = multi-shard streaming;
2. `B=500000`: exact sharded production census;
3. `B=1000000`: exact sharded production census;
4. stop.

The 500k job cannot start unless 200k validation passes, and the 1m job cannot start unless 500k succeeds. There is no workflow input or code path for a bound above one million.

## Exact sharding contract

- Every Pythagorean shared edge belongs to exactly one shard.
- An exactly-two object has one unique common edge, so it is counted exactly once.
- A three-face object is encountered at its three shared edges; the reducer retains only a small triple-key counter and requires multiplicity exactly three.
- Space integrality remains the final exact-square predicate on `R^2`.
- No Stage14 diagonal-first generator is used for ambient `M2`.

## Evidence boundary

All outputs are exact finite census data. They do not establish an asymptotic rate, an intrinsic exponent, or perfect-cuboid nonexistence.

```text
R202_POPULATION_CONTRACT_UNCHANGED=true
R202_LEGACY_OVERLAP_BOUND=200000
R202_STAGED_BOUNDS=200000,500000,1000000
R202_HARD_MAX_BOUND=1000000
R202_AUTO_EXPAND_ABOVE_1M=false
R202_ASYMPTOTIC_CLAIM=false
R202_PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
R202_CI_STATUS=PENDING
```
