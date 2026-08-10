# Stage14 main/s exponent and saving ledger

This ledger is the human-readable entry point for exponent arithmetic shared by Stage14 `14-4` and `s`.

Two rules are mandatory:

> Never compare or combine exponents until both their **scale** and **quantifier scope** match.

> Keep the **closed local baseline** distinct from the **current whole-family bound** after post-local improvements.

## 1. Closed local baseline

The closed Stage14-s5 local method gives

```text
N_local(M) << M^(2-1/21+epsilon)
```

and `M<=sqrt(B)` gives

```text
#Q_B^phys << B^(41/42+epsilon).
```

Therefore

```text
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_M_EXPONENT=41/21
CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42
```

This remains current **for the closed s5 local theorem itself**.

## 2. Local supersession chain

| Stage | M-scale saving | M exponent | physical B exponent | status |
|---|---:|---:|---:|---|
| s5s | `1/200` | `399/200` | `399/400` | SUPERSEDED |
| s5t | `1/41` | `81/41` | `81/82` | SUPERSEDED |
| s5u | `1/21` | `41/21` | `41/42` | CURRENT LOCAL BASELINE |

Conversion:

```text
M^(2-delta_M), M<=B^(1/2)
 -> B^(1-delta_M/2).
```

## 3. Whole-family post-local checkpoints

### 3.1 Stage14-4bq

Merged 4bq obtained

```text
V(B) << B^(61/63+o(1)).
```

with

```text
41/42 - 61/63 = 1/126,
61/63 - 1/2   = 59/126.
```

This was the first positive whole-family direct post-local saving.

### 3.2 Stage14-4br

Merged 4br recombined the then-exhaustive sectors at

```text
V(B) << B^(20/21+o(1)).
```

so at that checkpoint

```text
41/42 - 20/21 = 1/42,
20/21 - 1/2   = 19/42.
```

`20/21` is now **SUPERSEDED AS THE CURRENT WHOLE-FAMILY EXPONENT**, but remains a valid historical and sector-level checkpoint.

### 3.3 Current Stage14-s7-08 checkpoint

Merged s7-08 combines the s7-07 reduced fixed-quartic receiver, the merged 4bv thick-packet square sieve, and the shared-`xi` cell switch.

The exact optimized thresholds are

```text
lambda = 9/19,
tau    = 2/19,
theta  = 8/19.
```

The active terms are bounded by

```text
2lambda,
1-tau/2,
1+theta-lambda,
1-(theta-2tau)/4,
```

and all optimize to

```text
18/19.
```

Therefore the current whole-family theorem is

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
V(B) << B^(18/19+o(1)).
```

The strict improvement over the previous current checkpoint is

```text
20/21 - 18/19 = 2/399.
```

Relative to the closed local `41/42` baseline, cumulative direct post-local saving is

```text
41/42 - 18/19 = 11/798.
```

Thus

```text
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=11/798
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true.
```

## 4. Current square-root budget

Target:

```text
B^(1/2+epsilon).
```

Current whole-family exponent:

```text
18/19.
```

Current remaining gap:

```text
18/19 - 1/2 = 17/38.
```

Therefore

```text
CURRENT_REMAINING_GAP_TO_SQRT=17/38.
SQRT_B_UPPER_BOUND_PROVED=false.
```

Historical remaining gaps remain valid only in context:

```text
pre-4bq: 41/42 - 1/2 = 10/21
4bq:     61/63 - 1/2 = 59/126
4br:     20/21 - 1/2 = 19/42
current: 18/19 - 1/2 = 17/38
```

## 5. Specialized exponents and receiver thresholds

### 5.1 Stage14-4bl small-partner-leg sector

```text
count << B^(20/21+o(1)).
```

This remains a valid sector theorem but is now weaker than the current `18/19` whole-family theorem and must not be called current.

### 5.2 Stage14-s6-07 forced incidence scale

```text
B^(41/420)
```

is a forced structural variable/incidence scale, not a count saving.

### 5.3 Stage14-4bq good-cell residual

```text
E_good-res(B) << B^(13/14+o(1)).
```

This remains a genuine moving-family sector bound below the current whole-family maximum.

### 5.4 Stage14-4bv thick square-part receiver

For a fixed product-square packet,

```text
N_packet << M*H^(-1/2)*B^o(1).
```

If `H>=B^tau`, this is a sector exponent

```text
1-tau/2.
```

At the s7-08 optimum `tau=2/19`, it contributes exactly `18/19`.

### 5.5 Stage14-s7-08 shared-xi cell receiver

A selected cell `q~T` receives

```text
#solutions << T^(1/2)B^o(1),
```

or relative saving `T^(-1/2)`.

At the optimized thin-coefficient thresholds this closes the complementary hard branch at exponent `18/19`.

## 6. Canonical current facts

```text
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_PHYSICAL_BASELINE_EXPONENT=41/42

CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
WHOLE_FAMILY_POST_LOCAL_SAVING_PROVED=11/798
SQRT_TARGET_EXPONENT=1/2
CURRENT_REMAINING_GAP_TO_SQRT=17/38
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```

Historical checkpoints:

```text
HISTORICAL_PRE_4BQ_WHOLE_FAMILY_EXPONENT=41/42
HISTORICAL_4BQ_WHOLE_FAMILY_EXPONENT=61/63
HISTORICAL_4BR_WHOLE_FAMILY_EXPONENT=20/21
HISTORICAL_4BR_REMAINING_GAP_TO_SQRT=19/42
```

Current s7-08 optimization:

```text
S7_08_OPTIMAL_LAMBDA=9/19
S7_08_OPTIMAL_TAU=2/19
S7_08_OPTIMAL_THETA=8/19
S7_08_ADAPTIVE_ARCHITECTURE_EXPONENT=18/19
S7_08_IMPROVEMENT_OVER_20_21=2/399
```

## 7. Safe arithmetic recipes

### Convert an M-scale local saving

```text
N(M) << M^(2-delta_M+epsilon), M<=sqrt(B)
 -> physical exponent = 1-delta_M/2.
```

### Compute remaining saving

For current exponent `alpha` and target `beta<alpha`:

```text
remaining saving = alpha-beta.
```

Always follow the CURRENT ledger card through any `SUPERSEDED_BY` chain first.

### Promote sector bounds to a whole-family bound

Only after an exhaustive partition:

```text
whole-family exponent = max(sector exponents).
```

A fixed-curve/fiber bound must first pass a moving-family or active-base transfer.

## 8. Forbidden substitutions

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

## 9. Canonical card map

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
