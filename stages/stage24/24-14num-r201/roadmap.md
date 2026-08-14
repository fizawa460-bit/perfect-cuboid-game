# 24-14num-r201 — matched ambient M2 numerical lane

STATUS=BOOTSTRAP
PARENT_STAGE=Stage24
TRACK_ROLE=ADDITIONAL_NUMERICAL_RESEARCH
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false

## Why this lane exists

Stage24 studies the literal survivor transition

`Stage18 M2(B) -> Stage19 N2(B) = M2(B) intersect {R integral}`.

The Stage14 numerical observatory already gives a very deep exact numerator census N2 through B=500,000,000, but it does not enumerate the ambient Stage18 denominator M2. Stage24 therefore needs a matched ambient numerical lane instead of repeatedly relying on tiny Stage18 frozen windows.

## Exact population contract

For each cutoff B, enumerate primitive canonical triples satisfying

- `0 < a < b < c`,
- `gcd(a,b,c)=1`,
- `R^2=a^2+b^2+c^2 <= B^2`,
- exactly two of `a^2+b^2`, `a^2+c^2`, `b^2+c^2` are integer squares.

Define

- `M2(B)` = all such triples, with no space-diagonal integrality requirement;
- `N2(B)` = the same triples with `R^2` an integer square.

This is a literal same-object survivor classification. No population, cutoff, multiplicity, or measure adapter is allowed inside this lane.

## Existing exact engine

Do not rewrite the mathematics. Reuse `stages/stage15/scripts/paired_enumerator.py`.

That engine already performs

`two Pythagorean faces sharing one edge -> primitive/canonical exactly-two object -> final space_integral classification`.

Its validator already proves brute-force equality at small B and Stage14 N2 regression. Therefore r201 is a bootstrap/reuse proof, not a new mathematical enumerator.

## r201 gates

1. Revalidate the existing paired enumerator.
2. Reproduce `M2(2000)=4812` from frozen Stage18.
3. Reproduce `N2(2000)=5` and `N2(100000)=89` from frozen Stage19/Stage14 numerical data.
4. Compute the matched same-run `M2(100000), N2(100000), N2/M2` pair.
5. Freeze workload diagnostics from the same run.
6. Do not infer an asymptotic rate from these finite data.

## Planned continuation

`24-14num-r202` is the engineering/scaling step:

- streaming/chunked shared-edge enumeration;
- exact disjoint-union/dedup protocol;
- regression against r201 and the existing paired enumerator;
- staged bounds `200k -> 500k -> 1m -> 2m -> 5m -> 10m` as resources permit.

This is the natural Codex-oriented implementation task. Optimization may change indexing, chunking, streaming, parallelism and serialization, but may not change the population contract or the final `space_integral` predicate.

## Numerical reuse preflight

NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03 plus Stage15 paired enumerator
NUM_POPULATION_MATCH=ADAPTER_PROVED_FOR_N2_AND_EXACT_FOR_STAGE24_INTERSECTION
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS+EXACT_REGRESSION_ORACLE
NUM_NEW_COMPUTATION_JUSTIFIED=AMBIENT_M2_DENOMINATOR_IS_NOT_PRESENT_IN_STAGE14_NUM

## Safety

- Stage14 integral-space N2 is not ambient M2.
- Do not use alpha diagonal-first pruning that presupposes integral space diagonal to generate M2.
- Finite fits are not asymptotic theorems.
- Finite T=0 is not perfect-cuboid nonexistence.

NEXT=24-14num-r201-bootstrap-CI
