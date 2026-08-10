# Stage14-toolbox-am — external theorem hypothesis contract and import checklist

## Purpose

Freeze a reusable contract for importing literature theorems into Stage14, record valid and rejected live examples from the newly merged adjacent two-cell receiver, and advance the toolbox current ledger from the historical 4bx `15/16` checkpoint to the proved `13/14` theorem.

Toolbox-am does not own the `13/14` theorem. It imports only merged s7-10 / 4by / 4bz results and reorganizes them for safe reuse.

## Deliverables

- `docs/stage14-toolbox/external-theorem-import-contract.md`
- `docs/stage14-toolbox/external-theorem-import-checklist-template.md`
- 10 new canonical cards
- current exponent ledger advanced to `13/14`
- historical 4bx current and conditional ledgers superseded, not deleted
- historical s7-09 conditional cookbook superseded by a proved two-cell recipe
- toolbox-al forward-compatible regression
- dedicated theorem-import audit and CI

## Import state machine

```text
CANDIDATE
 -> HYPOTHESIS_MAPPED
    -> IMPORTED
    -> REJECTED
```

`IMPORTED` requires exact theorem locator, Stage14 object map, every required hypothesis, uniformity, exceptional-stratum treatment, bad-prime treatment, output scale, and post-theorem transfer chain.

## Live imported/rejected examples

```text
Katz 2007 direct nonsingular-polynomial shortcut : REJECTED
Katz--Laumon stationary-phase route              : IMPORTED (s7-10)
Lei Fu Corollary 0.3 Newton-polyhedron route      : IMPORTED (4by)
```

The two imported routes independently prove the same adjacent two-cell all-frequency `O(p)` receiver. They are cross-checks, not multiplicative savings.

## Current quantitative ledger

```text
historical 4bx whole-family exponent = 15/16
current s7-10 / 4by exponent         = 13/14
improvement                           = 1/112
post-local saving from 41/42          = 1/21
remaining gap to 1/2                  = 3/7
```

Merged 4bz records `13/14` as the current square-root square-sieve architecture barrier; threshold retuning or naive multicell enlargement does not improve it.

## Boundary

```text
STAGE14_TOOLBOX_AM=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_CONTRACT_AND_IMPORT_CHECKLIST
CANONICAL_NEW_CARD_COUNT=10
CANONICAL_TOTAL_CARD_COUNT=97
EXTERNAL_THEOREM_IMPORT_STATE_COUNT=4
EXTERNAL_THEOREM_IMPORT_STATES=CANDIDATE,HYPOTHESIS_MAPPED,REJECTED,IMPORTED
EXACT_THEOREM_LOCATOR_REQUIRED=true
FULL_HYPOTHESIS_MAP_REQUIRED=true
EXCEPTIONAL_STRATA_MUST_BE_CLOSED=true
POST_THEOREM_TRANSFER_CHAIN_REQUIRED=true
FINITE_REGRESSION_COUNTS_AS_UNIFORM_THEOREM=false
DIRECT_KATZ_2007_DELIGNE_POLYNOMIAL_SHORTCUT_APPLICABLE=false
KATZ_LAUMON_STATIONARY_PHASE_ROUTE_IMPORTED=true
FU_COROLLARY_0_3_ROUTE_IMPORTED=true
MAIN_S_TWO_CELL_13_14_CONVERGENCE_RECORDED=true
HISTORICAL_4BX_LEDGER_SUPERSEDED=true
HISTORICAL_TWO_CELL_CONDITIONAL_LEDGER_SUPERSEDED=true
HISTORICAL_TWO_CELL_CONDITIONAL_RECIPE_SUPERSEDED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
IMPROVEMENT_OVER_15_16=1/112
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/21
CURRENT_REMAINING_GAP_TO_SQRT=3/7
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
SQRT_B_UPPER_BOUND_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AM=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-an barrier and obstruction atlas / next-receiver selector
```
