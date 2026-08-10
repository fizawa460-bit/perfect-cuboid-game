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
```

## Whole-family checkpoints

```text
4bq: V(B) << B^(61/63+o(1))
      41/42-61/63=1/126
      61/63-1/2=59/126

4br: V(B) << B^(20/21+o(1))
      41/42-20/21=1/42
      20/21-1/2=19/42
      [SUPERSEDED AS CURRENT]

s7-08 CURRENT:
      V(B) << B^(18/19+o(1))
      20/21-18/19=2/399
      41/42-18/19=23/798
      18/19-1/2=17/38
```

Canonical current facts:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=23/798
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=17/38
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
```

## Current s7-08 optimization

```text
S7_08_OPTIMAL_LAMBDA=9/19
S7_08_OPTIMAL_TAU=2/19
S7_08_OPTIMAL_THETA=8/19
S7_08_ADAPTIVE_ARCHITECTURE_EXPONENT=18/19
S7_08_IMPROVEMENT_OVER_20_21=2/399
```

The active architecture terms are

```text
2lambda,
1-tau/2,
1+theta-lambda,
1-(theta-2tau)/4,
```

and optimize at `18/19`.

## Specialized results that are not automatically whole-family bounds

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
4BQ_GOOD_CELL_RESIDUAL_EXPONENT=13/14
4BV_FIXED_PACKET_RELATIVE_SAVING=H^(-1/2)
S7_08_CELL_SWITCH_RELATIVE_SAVING=T^(-1/2)
```

Interpretation:
- `B^(41/420)` is a structural variable/incidence scale, not a count saving.
- 4bv gives `N_packet << M*H^(-1/2)*B^o(1)` on a fixed product-square packet.
- s7-08 turns a selected shared-`xi` cell `q~T` into `O(T^(1/2)B^o(1))` solutions.
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
 -> TB-LEDGER-current-whole-family-after-s7-08 [CURRENT]

TB-RECIPE-dispatch-balanced-inert-square-sieve
 -> TB-RECIPE-dispatch-shared-xi-cell-switch
 -> TB-LEDGER-current-whole-family-after-s7-08
```
