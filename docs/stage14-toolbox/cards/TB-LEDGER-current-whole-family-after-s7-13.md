# Historical whole-family ledger after s7-13

```yaml
ID: TB-LEDGER-current-whole-family-after-s7-13
TYPE: LEDGER
STATUS: SUPERSEDED
SUPERSEDED_BY: AR-006
TITLE: Historical whole-family exponent 7/8 after full-coordinate common refinement
SCOPE: BOTH
SOURCE_STAGE: Stage14-s7-13
SOURCE_PR: 434
SOURCE_MERGE_SHA: 079d053d1182e82a1924b37bba9ae33a3907f031
SOURCE_FILES:
  - stages/stage14/14-s7-13/result.md
```

## INPUT

Merged s7-13 keeps the proved s7-10/4by two-cell theorem and refines a short reduced coordinate simultaneously in numerator, denominator, and square-part variables.

## OUTPUT

```text
HISTORICAL_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
IMPROVEMENT_OVER_13_14=3/56
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
SQRT_B_UPPER_BOUND_PROVED_AT_THIS_STAGE=false
```

## VARIABLE DICTIONARY

For `P~B^p, Q~B^q, P=a*x^2, Q=b*y^2`, put `alpha=p-2s`, `beta=q-2t`, `m=max(alpha,beta)`. The common-refinement block has two valid upper envelopes

```text
1/2+m
1-m/3
```

and uses their minimum, not their product. The worst point is `m=3/8`, giving `7/8`.

## USED BY

- Historical reconstruction of the Stage14 main/s route after merged s7-13.
- Diagnosing which full-coordinate refinement barrier was later broken by AR-006.

## DO NOT USE FOR

- Do not multiply fixed-coordinate and two-cell savings; s7-13 explicitly takes the minimum on the common refinement.
- Do not use `7/8` as the current Stage14 whole-family exponent. AR-006 proves
  `N_2(B) << B^(1/2+o(1))` on the final physical Stage14 population.

## PROVENANCE NOTES

Merged s7-13 imports the proved two-cell theorem as an ingredient and improves the global count through a finer coordinate-support refinement rather than a new external character-sum theorem.
