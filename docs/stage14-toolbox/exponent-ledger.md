# Stage14 main/s current exponent and saving ledger

This ledger is the human-readable entry point for exponent arithmetic shared by Stage14 `14-4` and `s`.

The central rule is:

> Never compare or combine two exponents until both their **scale** and **quantifier scope** match.

## 1. Current whole-family input

The closed Stage14-s5 local method currently gives

```text
N_local(M) << M^(2-1/21+epsilon)
```

and physical conversion `M<=sqrt(B)` gives

```text
#Q_B^phys << B^(41/42+epsilon).
```

Therefore:

```text
current whole-family physical exponent = 41/42
current whole-family physical saving vs B^1 = 1/42
```

This is an upper bound only, not an asymptotic.

## 2. Supersession chain for the same normalized local problem

All three rows below refer to the same basic local-count use case and therefore may be ordered by strength.

| Stage | M-scale saving | M exponent | physical B exponent | status |
|---|---:|---:|---:|---|
| s5s | `1/200` | `2-1/200=399/200` | `399/400` | SUPERSEDED |
| s5t | `1/41` | `2-1/41=81/41` | `81/82` | SUPERSEDED |
| s5u | `1/21` | `2-1/21=41/21` | `41/42` | CURRENT |

Exact conversion rule:

```text
M^(2-delta_M), M<=B^(1/2)
 -> B^(1-delta_M/2).
```

Hence the physical saving is `delta_M/2`.

## 3. Current square-root budget

Target:

```text
B^(1/2+epsilon).
```

Current whole-family input:

```text
B^(41/42+epsilon).
```

Required additional post-local saving:

```text
41/42 - 1/2 = 10/21.
```

So a theorem

```text
N_gs(B) << B^(41/42-delta_post+epsilon)
```

is genuine whole-family progress for every fixed `delta_post>0`, and reaches square-root scale if

```text
delta_post >= 10/21.
```

No merged main/s source used by this ledger proves that full `10/21` saving yet.

## 4. Current specialized exponents that must not be promoted

### 4.1 Stage14-4bl dual half-angle small-leg sector

On the sector

```text
X2 <= B^(20/21),
```

Stage14-4bl proves

```text
count << B^(20/21+o(1)).
```

Compared with the current whole-family `41/42`, this is an exact sector-only gain

```text
41/42 - 20/21 = 1/42.
```

The complementary sector forces one of the dual products to critical scale `B^(10/21)` up to constants, but no full-family post-local power saving is proved there yet.

### 4.2 Stage14-s6-07 five-factor forced incidence scale

Stage14-s6-07 has an exact five-factor decomposition of the relevant partner leg. After its small `X2` sector is removed, at least one factor is forced above

```text
B^(41/420),
```

because

```text
(41/84)/5 = 41/420.
```

This is a **structural variable/incidence threshold**, not a count saving.

## 5. Method ceilings and hypothetical bounds

The closed s5 source also records a single-edge module ceiling near

```text
1/20 on M-scale.
```

This is not the current whole-system saving. Replacing the proved `1/21` by `1/20` in a whole-family theorem is forbidden unless a later merged theorem actually closes the other sectors at that strength.

Similarly, architecture stress tests such as hypothetical Case-C removal are planning diagnostics rather than current bounds.

## 6. Canonical current facts

```text
CURRENT_LOCAL_M_SAVING=1/21
CURRENT_LOCAL_M_EXPONENT=41/21
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=41/42
CURRENT_PHYSICAL_WHOLE_FAMILY_SAVING_VS_B=1/42
SQRT_TARGET_EXPONENT=1/2
REQUIRED_POST_LOCAL_SAVING=10/21
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
```

Specialized facts:

```text
4BL_SMALL_PARTNER_LEG_SECTOR_EXPONENT=20/21
4BL_SMALL_PARTNER_LEG_SECTOR_GAIN_VS_41_42=1/42
S6_07_FORCED_LARGE_INCIDENCE_CELL_EXPONENT=41/420
```

## 7. Safe arithmetic recipes

### Convert an M-scale local saving

If a merged theorem proves

```text
N(M) << M^(2-delta_M+epsilon)
```

and the same theorem/interface allows `M<=sqrt(B)`, then

```text
physical exponent = 1-delta_M/2.
```

### Compute remaining saving to a target

If the current whole-family exponent is `alpha` and the target is `beta<alpha`, then the required saving is

```text
alpha-beta.
```

Only use a sectoral saving in this subtraction after the complementary sectors have also been bounded and a merged source states a whole-family theorem.

## 8. Common forbidden substitutions

Do not perform any of these silently:

```text
M-scale saving <-> B-scale saving
sector exponent -> whole-family exponent
forced variable size -> count saving
coordinate-density saving -> packet/base-count saving
single-module ceiling -> whole-system theorem
local soluble -> global soluble
```

## 9. Canonical card map

```text
TB-BOUND-local-descent-s5s
  -> TB-BOUND-local-descent-s5t
  -> TB-BOUND-local-descent-current

TB-LEDGER-post-local-sqrt-gap
TB-BOUND-dual-half-angle-small-leg-sector
TB-LEDGER-s6-07-forced-incidence-scale
TB-WARNING-exponent-scope-and-transfer
```
