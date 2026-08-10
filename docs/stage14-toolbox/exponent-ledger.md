# Stage14 main/s exponent and saving ledger

This ledger is the human-readable entry point for exponent arithmetic shared by Stage14 `14-4` and `s`.

The central rule is:

> Never compare or combine two exponents until both their **scale** and **quantifier scope** match.

A second rule is now necessary:

> Keep the **closed local baseline** distinct from the **current whole-family main-track bound** after post-local improvements.

## 1. Closed local baseline

The closed Stage14-s5 local method gives

```text
N_local(M) << M^(2-1/21+epsilon)
```

and physical conversion `M<=sqrt(B)` gives the local/base-class baseline

```text
#Q_B^phys << B^(41/42+epsilon).
```

Therefore:

```text
current closed local physical baseline = 41/42
local physical saving vs B^1         = 1/42
```

This remains the correct current statement about the closed s5 local theorem itself.

## 2. Local supersession chain

All three rows below refer to the same normalized local-count use case and therefore may be ordered by strength.

| Stage | M-scale saving | M exponent | physical B exponent | status |
|---|---:|---:|---:|---|
| s5s | `1/200` | `399/200` | `399/400` | SUPERSEDED |
| s5t | `1/41` | `81/41` | `81/82` | SUPERSEDED |
| s5u | `1/21` | `41/21` | `41/42` | CURRENT LOCAL BASELINE |

Exact conversion rule:

```text
M^(2-delta_M), M<=B^(1/2)
 -> B^(1-delta_M/2).
```

## 3. Current whole-family main-track bound

Merged Stage14-4bq recombines the exhaustive sectors

```text
small partner leg : B^(20/21+o(1))
cross branch      : B^(61/63+o(1))
good-cell residual: B^(13/14+o(1))
```

so

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/63
V(B) << B^(61/63+o(1)).
```

Relative to the previous whole-family checkpoint `41/42`, the proved direct post-local improvement is

```text
41/42 - 61/63 = 1/126.
```

Thus

```text
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=1/126
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true.
```

## 4. Current square-root budget

Target:

```text
B^(1/2+epsilon).
```

Current whole-family exponent:

```text
61/63.
```

Current remaining saving required:

```text
61/63 - 1/2 = 59/126.
```

Therefore

```text
CURRENT_REMAINING_GAP_TO_SQRT=59/126.
```

### Historical 41/42 checkpoint

Before the 4bq improvement, the gap was

```text
41/42 - 1/2 = 10/21.
```

This `10/21` remains valid as a historical threshold inside merged stages that explicitly chose parameters relative to the then-current `41/42` checkpoint. It is no longer the current whole-family remaining gap.

## 5. Specialized exponents that must not be promoted incorrectly

### 5.1 Stage14-4bl small-partner-leg sector

```text
X2 <= B^(20/21)
 -> count << B^(20/21+o(1)).
```

This is one sector in the later exhaustive recombination. It is not itself the whole-family exponent.

### 5.2 Stage14-s6-07 forced incidence scale

After the relevant five-factor decomposition, one factor is forced above

```text
B^(41/420),
```

because

```text
(41/84)/5 = 41/420.
```

This is a structural variable/incidence threshold, not a count saving.

### 5.3 Stage14-4bq good-cell residual

The diagonal-pair genus-one transfer gives

```text
E_good-res(B) << B^(13/14+o(1)).
```

This is a genuine moving-family sector bound because the reduced-slope recovery and family summation are controlled. It is still not the overall maximum; the current bottleneck is `61/63`.

## 6. Method ceilings and hypothetical bounds

The closed s5 source records a single-edge module ceiling near

```text
1/20 on M-scale.
```

This is not a whole-system theorem. Likewise planning diagnostics or fixed-curve point estimates do not become whole-family exponents without a merged transfer theorem.

## 7. Canonical current facts

Local baseline:

```text
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_M_EXPONENT=41/21
CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42
```

Whole-family main track:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/63
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=1/126
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=59/126
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
```

Historical checkpoint:

```text
HISTORICAL_PRE_4BQ_WHOLE_FAMILY_EXPONENT=41/42
HISTORICAL_PRE_4BQ_REQUIRED_POST_LOCAL_SAVING=10/21
```

Specialized facts:

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
4BQ_GOOD_CELL_RESIDUAL_EXPONENT=13/14
```

## 8. Safe arithmetic recipes

### Convert an M-scale local saving

If a merged theorem proves

```text
N(M) << M^(2-delta_M+epsilon)
```

and the same interface allows `M<=sqrt(B)`, then

```text
physical exponent = 1-delta_M/2.
```

### Compute remaining saving to a target

If the current whole-family exponent is `alpha` and target is `beta<alpha`, then

```text
remaining saving = alpha-beta.
```

Use the latest CURRENT whole-family ledger, not a historical threshold card.

### Promote a sector to a whole-family bound

Only after the sectors form an exhaustive partition may one take

```text
whole-family exponent = max(sector exponents).
```

A per-fixed-curve point bound must first be transferred through the moving family with controlled multiplicity.

## 9. Common forbidden substitutions

Do not perform any of these silently:

```text
M-scale saving <-> B-scale saving
local baseline exponent -> current post-local whole-family exponent
historical remaining gap -> current remaining gap
sector exponent -> whole-family exponent without exhaustive recombination
forced variable size -> count saving
coordinate-density saving -> packet/base-count saving
fixed genus-one point bound -> moving-family count without transfer
single-module ceiling -> whole-system theorem
local soluble -> global soluble
```

## 10. Canonical card map

```text
TB-BOUND-local-descent-s5s
  -> TB-BOUND-local-descent-s5t
  -> TB-BOUND-local-descent-current

TB-LEDGER-post-local-sqrt-gap [SUPERSEDED AS CURRENT GLOBAL GAP]
  -> TB-LEDGER-current-main-after-4bq [CURRENT]

TB-BOUND-dual-half-angle-small-leg-sector
TB-LEDGER-s6-07-forced-incidence-scale
TB-BOUND-diagonal-pair-genus-one-count
TB-WARNING-exponent-scope-and-transfer
TB-WARNING-genus-one-quantifier-and-model-boundary
```
