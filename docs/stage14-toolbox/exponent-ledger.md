# Stage14 main/s exponent and saving ledger

Rule: compare exponents only after matching both scale and quantifier scope. Keep reusable receiver theorems separate from the terminal whole-family ledger.

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
s7-10 / 4by: 13/14 [SUPERSEDED AS GLOBAL, REUSABLE TWO-CELL THEOREM]
s7-13: 7/8 [CURRENT]
```

Exact current arithmetic:

```text
13/14 - 7/8 = 3/56
41/42 - 7/8 = 17/168
7/8 - 1/2   = 3/8
```

Canonical current facts:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=17/168
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```

## Reusable two-cell theorem from s7-10 / 4by

The imported external-theorem contracts prove

```text
|T_p(h,k)| << p
N_2cell(R,S) << (RS)^(2/3) B^o(1)
TWO_CELL_COEFFICIENT_RELATIVE_SAVING=(RS)^(-1/3)
```

The resulting `13/14` whole-family checkpoint is historical, but the two-cell theorem remains a live input.

## Current full-coordinate refinement

Merged s7-13 writes

```text
P=a*x^2
Q=b*y^2
alpha=p-2s
beta=q-2t
m=max(alpha,beta)
```

and obtains two valid upper bounds on the same common-refinement block:

```text
coordinate support <= 1/2+m
two-cell receiver  <= 1-m/3
```

The estimates are not multiplied. Taking their minimum gives

```text
min(1/2+m, 1-m/3).
```

The exact worst point is `m=3/8`, hence

```text
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
```

Critical geometry:

```text
P,Q ~ B^(1/2)
a,b ~ B^(3/8)
x,y ~ B^(1/16)
xi=ab ~ B^(3/4)
```

## Historical architecture markers

```text
SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER_AT_4BZ=13/14
HISTORICAL_4BX_WHOLE_FAMILY_EXPONENT=15/16
HISTORICAL_S7_10_WHOLE_FAMILY_EXPONENT=13/14
S7_13_IMPROVEMENT_OVER_13_14=3/56
S7_13_IMPROVEMENT_OVER_10_11=3/88
```

## Specialized reusable results

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
4BQ_GOOD_CELL_RESIDUAL_EXPONENT=13/14
S7_08_CELL_SWITCH_RELATIVE_SAVING=T^(-1/2)
4BX_THICK_PACKET_RELATIVE_SAVING=H^(-4/5)
S7_10_4BY_TWO_CELL_RELATIVE_SAVING=(RS)^(-1/3)
S7_13_FULL_COORDINATE_BARRIER=7/8
```

These are not interchangeable whole-family bounds; retain their scale and conditioning.

## Safe recipes

```text
remaining saving = current exponent - target exponent
whole-family exponent = max(exhaustive sector exponents)
common-refinement alternative bounds -> take min when both bound the same block
```

Always follow the terminal ledger through `SUPERSEDED_BY` before using a gap or threshold.

## Forbidden substitutions

```text
M-scale saving <-> B-scale saving
local baseline -> current whole-family exponent
historical gap -> current gap
sector exponent -> whole-family exponent without exhaustive recombination
coordinate density -> packet/base-count saving
fixed-fiber B^o(1) -> active-direction sparsity
external complete-sum theorem -> whole-family bound without transfer
finite regression -> uniform theorem
rejected theorem shortcut -> imported theorem without new hypothesis proof
two valid bounds on same refinement -> multiply instead of take a justified min
```

## Canonical card chain

```text
TB-LEDGER-post-local-sqrt-gap [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4bq [SUPERSEDED]
 -> TB-LEDGER-current-main-after-4br [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-08 [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-4bx [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-10 [SUPERSEDED]
 -> TB-LEDGER-current-whole-family-after-s7-13 [CURRENT]

TB-RECIPE-cookbook-two-cell-conditional-gate [SUPERSEDED]
 -> TB-RECIPE-cookbook-two-cell-proved-13-14 [CURRENT REUSABLE RECEIVER]
 -> TB-LEDGER-current-whole-family-after-s7-13
```
