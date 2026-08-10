# Stage14 main/s exponent and saving ledger

Rule: compare exponents only after matching both scale and quantifier scope. Keep the closed local baseline separate from the current whole-family theorem.

## Local baseline

```text
N_local(M) << M^(2-1/21+epsilon), M<=B^(1/2)
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_M_EXPONENT=41/21
CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42
```

Local supersession:

```text
s5s: 1/200 -> 399/400 physical [SUPERSEDED]
s5t: 1/41  -> 81/82 physical  [SUPERSEDED]
s5u: 1/21  -> 41/42 physical  [CURRENT LOCAL BASELINE]
```

Historical pre-4bq square-root gap:

```text
41/42 - 1/2 = 10/21.
HISTORICAL_PRE_4BQ_REQUIRED_POST_LOCAL_SAVING=10/21
```

## Whole-family checkpoints

```text
4bq: V(B) << B^(61/63+o(1))
      41/42-61/63=1/126
      61/63-1/2=59/126

4br: V(B) << B^(20/21+o(1))
      41/42-20/21=1/42
      20/21-1/2=19/42
      [SUPERSEDED]

s7-08 / 4bw:
      V(B) << B^(18/19+o(1))
      20/21-18/19=2/399
      41/42-18/19=23/798
      18/19-1/2=17/38
      [SUPERSEDED AS CURRENT BY 4bx]

4bx CURRENT:
      V(B) << B^(15/16+o(1))
      18/19-15/16=3/304
      41/42-15/16=13/336
      15/16-1/2=7/16
```

Canonical current facts:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=13/336
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=7/16
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```

Historical facts:

```text
HISTORICAL_PRE_4BQ_WHOLE_FAMILY_EXPONENT=41/42
HISTORICAL_PRE_4BQ_REQUIRED_POST_LOCAL_SAVING=10/21
HISTORICAL_4BQ_WHOLE_FAMILY_EXPONENT=61/63
HISTORICAL_4BQ_REMAINING_GAP_TO_SQRT=59/126
HISTORICAL_4BR_WHOLE_FAMILY_EXPONENT=20/21
HISTORICAL_4BR_REMAINING_GAP_TO_SQRT=19/42
HISTORICAL_S7_08_WHOLE_FAMILY_EXPONENT=18/19
HISTORICAL_S7_08_REMAINING_GAP_TO_SQRT=17/38
```

## Current 4bx optimization

```text
OPTIMAL_THICK_AUXILIARY_PRIME_SCALE=H^(4/5)
THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
4BX_OPTIMAL_LAMBDA=15/32
4BX_OPTIMAL_NU=13/32
4BX_OPTIMAL_TAU=5/64
4BX_ADAPTIVE_ARCHITECTURE_EXPONENT=15/16
4BX_IMPROVEMENT_OVER_18_19=3/304
```

The proved thick and one-cell-thin architecture closes exhaustively at `15/16`.

## Two-cell conditional ledger

Merged s7-09 leaves the adjacent two-cell mixed Fourier theorem open. Its historical conditional target was `16/17`. After importing the proved 4bx thick improvement, the conditional target improves to `13/14` without becoming a theorem.

```text
HISTORICAL_S7_09_CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17
UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14
S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false
CONDITIONAL_TARGET_IS_CURRENT_THEOREM=false
```

## Specialized results that are not automatically whole-family bounds

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
4BQ_GOOD_CELL_RESIDUAL_EXPONENT=13/14
4BV_FIXED_PACKET_RELATIVE_SAVING=H^(-1/2)
S7_08_CELL_SWITCH_RELATIVE_SAVING=T^(-1/2)
4BX_THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
```

Interpretation:
- `B^(41/420)` is a structural variable/incidence scale, not a count saving.
- s7-08 supplies the one-cell thin receiver reused by 4bx.
- 4bx strengthens the thick packet estimate but does not prove the missing two-cell mixed Fourier theorem.
- sector bounds become a whole-family bound only after exhaustive recombination.

## Safe recipes

```text
M^(2-delta_M), M<=B^(1/2)
 -> physical exponent 1-delta_M/2

remaining saving = current exponent - target exponent

whole-family exponent = max(exhaustive sector exponents)
```

Always follow the CURRENT ledger through its `SUPERSEDED_BY` chain before using a gap or threshold.

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
single CRT modulus -> required power saving without a large-sieve/second-moment transfer
conditional target -> current theorem without the missing theorem gate
```

In particular: `sector exponent -> whole-family exponent` and `forced variable size -> count saving` are forbidden without their explicit transfer theorem.

## Canonical card chain

```text
TB-BOUND-local-descent-s5s
 -> TB-BOUND-local-descent-s5t
 -> TB-BOUND-local-descent-current

TB-LEDGER-post-local-sqrt-gap [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4bq [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4br [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-08 [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-4bx [CURRENT]

TB-RECIPE-cookbook-one-cell-18-19
 -> TB-RECIPE-cookbook-thick-reoptimized-15-16
 -> TB-LEDGER-current-whole-family-after-4bx

TB-RECIPE-cookbook-two-cell-conditional-gate
 -> TB-LEDGER-updated-conditional-two-cell-after-4bx [CONDITIONAL TARGET ONLY]
```
