# Stage14-toolbox-am — external theorem hypothesis contract and import checklist

## Purpose

Freeze a reusable contract for importing literature theorems into Stage14, record valid and rejected live examples from the adjacent two-cell receiver, and keep the toolbox terminal exponent ledger synchronized with all merged main/s progress that landed during the stage.

Toolbox-am owns no new theorem. The external-theorem receiver comes from merged s7-10/4by; the current `7/8` whole-family theorem comes from merged s7-13.

## Deliverables

- `docs/stage14-toolbox/external-theorem-import-contract.md`
- `docs/stage14-toolbox/external-theorem-import-checklist-template.md`
- 11 new canonical cards
- external theorem state machine and mandatory hypothesis/transfer contract
- imported Katz--Laumon and Lei Fu examples
- rejected direct Katz 2007 shortcut example
- historical 4bx and s7-10 global ledgers superseded, not deleted
- historical s7-09 conditional cookbook superseded by the proved two-cell recipe
- current whole-family ledger advanced through `13/14` to merged s7-13 `7/8`
- toolbox-al forward-compatible regression
- dedicated theorem-import/current-ledger audit and CI

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

The imported routes prove the reusable adjacent two-cell all-frequency `O(p)` receiver. They are cross-checks, not multiplicative savings.

## Quantitative ledger

```text
historical 4bx whole-family exponent       = 15/16
historical s7-10 / 4by global checkpoint   = 13/14
current s7-13 whole-family exponent         = 7/8
13/14 -> 7/8 improvement                    = 3/56
post-local saving 41/42 -> 7/8              = 17/168
remaining gap 7/8 -> 1/2                    = 3/8
```

Merged s7-13 reaches `7/8` by using the proved two-cell theorem inside a finer common-coordinate refinement and taking the minimum of two valid block bounds, not by multiplying them.

## Boundary

```text
STAGE14_TOOLBOX_AM=COMPLETE_EXTERNAL_THEOREM_HYPOTHESIS_CONTRACT_AND_IMPORT_CHECKLIST
CANONICAL_NEW_CARD_COUNT=11
CANONICAL_TOTAL_CARD_COUNT=98
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
TWO_CELL_THEOREM_REMAINS_REUSABLE_AFTER_GLOBAL_SUPERSESSION=true
HISTORICAL_4BX_LEDGER_SUPERSEDED=true
HISTORICAL_TWO_CELL_CONDITIONAL_LEDGER_SUPERSEDED=true
HISTORICAL_TWO_CELL_CONDITIONAL_RECIPE_SUPERSEDED=true
HISTORICAL_S7_10_13_14_LEDGER_SUPERSEDED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
IMPROVEMENT_OVER_13_14=3/56
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=17/168
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
SQRT_B_UPPER_BOUND_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AM=false
OPEN_PR_USED_AS_CANONICAL_SOURCE=false
TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false
NEXT=Stage14-toolbox-an barrier and obstruction atlas / next-receiver selector
```
