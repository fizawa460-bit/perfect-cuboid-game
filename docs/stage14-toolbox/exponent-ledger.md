# Stage14 main/s exponent and saving ledger

Rule: compare exponents only after matching both scale and quantifier scope. Keep the closed local baseline separate from the current whole-family theorem.

## Local baseline

```text
N_local(M) << M^(2-1/21+epsilon), M<=B^(1/2)
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42
```

Historical local chain:

```text
s5s: 1/200 -> 399/400 physical [SUPERSEDED]
s5t: 1/41  -> 81/82 physical  [SUPERSEDED]
s5u: 1/21  -> 41/42 physical  [CURRENT LOCAL BASELINE]
```

## Whole-family checkpoints

```text
4bq:  61/63 [SUPERSEDED]
4br:  20/21 [SUPERSEDED]
s7-08 / 4bw: 18/19 [SUPERSEDED]
4bx:  15/16 [SUPERSEDED]
s7-10 / 4by: 13/14 [CURRENT]
```

Exact current arithmetic:

```text
15/16 - 13/14 = 1/112
41/42 - 13/14 = 1/21
13/14 - 1/2   = 3/7
```

Canonical current facts:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=1/21
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=3/7
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```

## Current two-cell architecture

Merged s7-10 and 4by prove the formerly conditional adjacent two-cell mixed Fourier receiver:

```text
|T_p(h,k)| << p
N_2cell(R,S) << (RS)^(2/3) B^o(1)
ADJACENT_TWO_CELL_RELATIVE_SAVING=(RS)^(-1/3)
```

Combined with the merged 4bx thick theorem

```text
THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
```

and exact thresholds

```text
lambda=13/28
nu=11/28
tau=5/56
```

gives `13/14` exhaustively.

Merged 4bz and s7-11 then show that naive threshold retuning or higher-cell enlargement within the same square-root square-sieve architecture does not improve the ceiling:

```text
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
THRESHOLD_RETUNING_BEATS_13_14=false
NAIVE_MULTICELL_ENLARGEMENT_BEATS_TWO_CELL=false
```

## Historical conditional chain

```text
s7-09: conditional 16/17
4bx:   updated conditional 13/14
s7-10 / 4by: theorem gate CLOSED; 13/14 becomes proved CURRENT
```

The conditional status is historical. Do not keep describing the two-cell Fourier bound as open after merged s7-10/4by.

## Specialized reusable results

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
4BQ_GOOD_CELL_RESIDUAL_EXPONENT=13/14
S7_08_CELL_SWITCH_RELATIVE_SAVING=T^(-1/2)
4BX_THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
S7_10_4BY_TWO_CELL_RELATIVE_SAVING=(RS)^(-1/3)
4BZ_DENOMINATOR_THIN_EXPONENT=19/21
4BZ_DENOMINATOR_THIN_SLACK_BELOW_CURRENT_CEILING=1/42
```

These are not interchangeable whole-family bounds; retain their scale and conditioning.

## Safe recipes

```text
M^(2-delta_M), M<=B^(1/2)
 -> physical exponent 1-delta_M/2

remaining saving = current exponent - target exponent

whole-family exponent = max(exhaustive sector exponents)
```

Always follow the CURRENT ledger through `SUPERSEDED_BY` before using a gap or threshold.

## Forbidden substitutions

```text
M-scale saving <-> B-scale saving
local baseline -> current whole-family exponent
historical gap -> current gap
sector exponent -> whole-family exponent without exhaustive recombination
forced variable size -> count saving
coordinate density -> packet/base-count saving
fixed genus-one point bound -> moving-family count without transfer
fixed-fiber B^o(1) -> active-direction sparsity
external complete-sum theorem -> whole-family bound without CRT/completion/sieve/transfer
finite regression -> uniform theorem
rejected theorem shortcut -> imported theorem without new hypothesis proof
```

## Canonical card chain

```text
TB-BOUND-local-descent-s5s
 -> TB-BOUND-local-descent-s5t
 -> TB-BOUND-local-descent-current

TB-LEDGER-post-local-sqrt-gap [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4bq [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4br [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-08 [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-4bx [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-10 [CURRENT]

TB-RECIPE-cookbook-two-cell-conditional-gate [SUPERSEDED]
 -> TB-RECIPE-cookbook-two-cell-proved-13-14 [CURRENT]
 -> TB-LEDGER-current-whole-family-after-s7-10
```
