# Stage23-60 old dead branch revalidation policy

Purpose: before Stage23 synthesis can treat the Stage19 lower-bound landscape as genuinely explored, re-open a targeted set of historically dead or exhausted branches whose original stopping argument may be weaker than the current Stage19 contract and geometry.

This is not a request to rerun all 824 Stage14/15 artifacts. The attack ledger remains the discovery index. The purpose is to challenge the *old death decisions* on the highest-value Stage19-relevant branches.

## Mandatory scope

Checkpoint60 must revalidate at least 8 high-value historical branches, selected from the Stage14/15 attack ledger, deep-review queue, and Stage23 history, with priority to branches satisfying one or more of:

1. the original dead/exhausted status relied materially on finite scan, numerical absence, heuristic sparsity, or incomplete computation;
2. the original obstruction used only a weak/local congruence and was never checked against the later Stage19 squareclass/Kummer/Jacobi formulations;
3. population, primitive normalization, canonical multiplicity, or physical cutoff `d<=B` was not matched exactly to the Stage19 population;
4. the branch was terminated before later Stage14/15 geometry or Stage19 exact interfaces became available;
5. the branch could plausibly contribute to Stage19 unboundedness, an explicit primitive family, or a positive-power lower bound if revived.

Ties should be broken in favor of lower-bound relevance and independent construction mechanisms rather than another rephrasing of the already-open Q06/Q11 upper-side bottlenecks.

## Revalidation contract for each selected branch

For every branch, checkpoint60 must record:

- source attack ID/path and original stop/dead/exhausted claim;
- the actual source-level argument supporting that claim, not only ledger metadata;
- whether the original claim was a proof, finite evidence, heuristic, population-mismatch conclusion, or conditional blocker;
- exact Stage19 population/cutoff/primitivity/multiplicity retest;
- retest under current Stage19 interfaces, including relevant squareclass/Kummer/Jacobi structure where applicable;
- verdict: `DEAD_CONFIRMED`, `DEAD_REASON_WEAKENED`, `REVIVED_LIVE`, `POPULATION_MISMATCH_ONLY`, or `NEEDS_NEW_INPUT`;
- if revived, immediate promotion ahead of synthesis and a concrete next attack;
- if dead remains confirmed, the strongest present proof of death and its exact scope.

A finite zero-hit search alone is not sufficient to keep a branch classified `DEAD_CONFIRMED`.

## History correction rule

If a historical branch was mathematically wrong, mark the actual false-claim origin and propagate corrections to dependent records. If it was merely underexplored or stopped on weaker evidence, do not revoke an otherwise correct historical PASS; instead materialize a supersession/addendum and update the attack ledger status.

## Stage19 lower-bound target

The certified current floor remains

\[
N_2(B)\ge3495\qquad(B\ge500{,}000{,}000),
\]

from the exact finite census and monotonicity. This revalidation is specifically looking for anything stronger: target unboundedness, an infinite primitive family, `N_2(B)\gg B^\delta`, or a route toward a matching half-power lower bound.

## Completion gate

Checkpoint60 cannot close with synthesis-only prose. It must materialize the selected-branch list and source-level revalidation ledger. If any branch revives, synthesis is deferred until that branch is attacked to its new boundary.

```text
OLD_DEAD_BRANCH_REVALIDATION_REQUIRED=true
REVALIDATE_BEFORE_SYNTHESIS=true
MIN_HIGH_VALUE_BRANCHES=8
SOURCE_LEVEL_OPEN_REQUIRED=true
ORIGINAL_DEATH_ARGUMENT_RECHECK_REQUIRED=true
CURRENT_STAGE19_CONTRACT_RETEST_REQUIRED=true
FINITE_ZERO_HIT_ALONE_CANNOT_CONFIRM_DEAD=true
REVIVED_BRANCH_PROMOTION_REQUIRED=true
LOWER_BOUND_RELEVANCE_PRIORITY=true
ALL_824_BLIND_RERUN_REQUIRED=false
```