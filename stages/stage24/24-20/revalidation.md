# Stage24-20 r202 main-lane revalidation

STATUS=PASS
SCOPE=MERGED_24-14num-r202_SOURCE_LEVEL_AND_CROSS_ORACLE_RECHECK
R203_DEPENDENCY=false

## Contract checked

The enumerated source is exactly

`0<a<b<c`, `gcd(a,b,c)=1`, `R^2=a^2+b^2+c^2<=B^2`, exactly two integral face diagonals.

`N2` is obtained on the same object at the final predicate `R^2` square. No space-integral condition is used in source generation.

## Gate R20-V1 — legacy overlap

`stages/stage24/24-14num-r202/validate.py` independently invokes the pre-r202 Stage15 `enumerate_paired` and compares it at B=200000 against both one-shard and multi-shard r202 enumeration.

Compared fields:

- M2 total and `(a,b,c)` direction totals;
- N2 total and `(a,b,c)` direction totals;
- M3 and N3;
- Pythagorean triangle count;
- glue count inside R;
- distinct primitive canonical >=2-face count;
- exact-two multiplicity-one gate;
- triple multiplicity-three gate.

The merged r202 CI records equality PASS.

## Gate R20-V2 — exact shard cover

`scaled_enumerator.py` constructs all shared edges from the same complete Pythagorean leg index and partitions that list by deterministic residue-in-list slices. Before scanning it checks both:

- no shared edge appears twice in the flattened shard union;
- the flattened shard union equals the complete original shared-edge set.

Thus the sharding layer itself neither drops nor duplicates a shared-edge bucket.

## Gate R20-V3 — exactly-two uniqueness

For each glued candidate the full face mask is recomputed after canonical sorting and primitivity filtering. If the mask has exactly two bits, the code derives the unique common edge from the mask/direction and raises unless the current enumerating shared edge is that edge.

Therefore each primitive canonical exactly-two object is counted once, with no global object dictionary required.

## Gate R20-V4 — triple multiplicity

A three-face object can be generated from all three shared edges. r202 therefore does not count such incidences as M2. It retains triple keys separately and rejects any triple whose accumulated source multiplicity is not exactly three.

`M3` is the number of distinct triple keys. `N3` is evaluated independently by the final space-square predicate.

## Gate R20-V5 — no space-biased source pruning

The source generator imported from Stage15 creates the full integer-Pythagorean leg index under hypotenuse <=B. The r202 scanner first applies physical R cutoff, canonical strict ordering, gcd primitivity and full face mask. Only after a mask is classified exactly-two does it test whether `R^2` is square for N2.

No Stage14 alpha diagonal-first or integral-space prerequisite is present in the M2 source path.

## Gate R20-V6 — independent target anchors

The r202 N2 values agree with previously frozen Stage14-num exact integral-space oracles produced by a different numerical history:

```text
B=200000   N2=116
B=500000   N2=188
B=1000000  N2=255
B=1000000  N2 direction=(98,101,56)
```

The 200k and 500k anchors occur in the Stage14 alpha equality matrix; the 1m total and direction vector occur in the Stage14 denominator-extension diagnostics. These are target-side cross-oracles, not substitutes for the ambient M2 calculation.

## Gate R20-V7 — arithmetic consistency

For every frozen row, directional M2 subtotals sum to M2 and directional N2 subtotals sum to N2. At B=1m:

```text
4592536+5816786+3408403=13817725
98+101+56=255
```

The exact survivor ratio is

`255/13817725 = 1.84545574615e-5`.

## Verdict

```text
R202_POPULATION_CONTRACT_RECHECK=PASS
R202_LEGACY_OVERLAP_RECHECK=PASS
R202_SHARD_COVER_RECHECK=PASS
R202_EXACT_TWO_MULTIPLICITY_RECHECK=PASS
R202_TRIPLE_MULTIPLICITY_RECHECK=PASS
R202_SPACE_PREDICATE_PLACEMENT_RECHECK=PASS
R202_STAGE14_N2_CROSS_ORACLE_RECHECK=PASS
R202_DIRECTION_SUM_RECHECK=PASS
MAIN_LANE_ACCEPTS_R202_EXACT_FINITE_COUNTS=true
R203_REQUIRED_FOR_THIS_VERDICT=false
```

This validates finite census correctness only. It does not promote any finite slope or directional ratio to an asymptotic theorem.
