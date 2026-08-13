# Stage14-4ee — canonical allocation type localization

## Status

`COMPLETE_CANONICAL_ALLOCATION_TYPE_FREEZE_AND_EXPLICIT_THREE_DIVISOR_INCIDENCE`

Consumes batch-local `Stage14-4ed`, merged `Stage14-4ea`, merged `Stage14-s7-65`, merged s-batch `Stage14-s7-66..68`, and merged `Stage14-s7-47`. Reciprocal-root information is not used as a saving; that sub-route is delegated to sH71.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Switch to the surviving allocation factor

Merged 4ea gives

```text
mu_G = mu_can * mu_root.
```

Stage14-4ed freezes the `mu_root` branch as the parallel sH71 target but leaves the mainline free to attack

```text
mu_can.
```

Use primitive slope coordinates

```text
gcd(a,b)=1,
0<a<b,
H=max(a,b)=B^(1/4+o(1)),
F_-(a,b)=oddpart(ab),
F_+(a,b)=oddpart(a^2+b^2).
```

Merged s7-65 proves

```text
gcd(F_-,F_+)=1.
```

## 2. Canonical allocation variables

Merged s7-66 gives the exact minus-side normalization: after the charged endpoint/common-scale decoration, every physical minus divisor allocation decomposes into divisors supported separately on the coprime primitive coordinates. Write representative divisor variables

```text
d_a | a,
d_b | b.
```

Their placement into the frozen minus physical cells is determined by the already-frozen chart/type label.

Merged s7-67 gives the plus-side normalization: every odd prime of `F_+` is `1 mod 4`, its Gaussian conjugate is fixed by the primitive slope, and the remaining physical plus allocation is a rational split-prime subset/divisor problem. Write one representative plus divisor

```text
d_+ | F_+(a,b)
```

with its complement `F_+/d_+`; both must satisfy the physical balanced windows and support masks.

Thus a canonical allocation witness can be represented, up to `B^o(1)` decoration, by

```text
(d_a,d_b,d_+)
```

together with its fixed finite allocation type.

```text
CANONICAL_MINUS_DIVISORS_LIVE_ON_A_AND_B=true
CANONICAL_PLUS_DIVISOR_LIVES_ON_A2_PLUS_B2=true
CANONICAL_ALLOCATION_REPRESENTED_BY_THREE_DIVISOR_INCIDENCE=true
```

## 3. Freeze one allocation type without exponent loss

The non-value labels in a canonical physical allocation consist of the already bounded chart/orientation choice, dyadic balanced window labels, smooth/rough side labels, endpoint/2-primary decorations and which canonical divisor feeds which frozen physical cell. Their total dictionary is `B^o(1)`.

On a square-root-saturating sequence, merged 4ea forces

```text
mu_can=B^(-o(1)).
```

Therefore one complete allocation type carries exponent-zero conditional mass and may be frozen by pigeonhole without fixed-power loss.

The actual divisor **values** `d_a,d_b,d_+` remain live polynomial arithmetic variables and are not frozen.

```text
CANONICAL_ALLOCATION_TYPE_DICTIONARY_SIZE=Bo1
ONE_CANONICAL_ALLOCATION_TYPE_CAN_BE_FROZEN=true
ACTUAL_DIVISOR_VALUES_REMAIN_POLYNOMIAL=true
```

## 4. Explicit fixed-type Boolean event

After freezing one type, define

```text
A_can(a,b)=1
```

iff there exist divisor values

```text
d_a|a,
d_b|b,
d_+|a^2+b^2
```

such that all fixed-type conditions hold:

```text
prescribed positive-width dyadic/balanced size windows,
squarefree/coprime cell masks,
smooth/rough support classes,
required complementary quotient windows,
all frozen chart/orientation/endpoint masks.
```

Because `gcd(a^2+b^2,ab)=1`, the plus divisor is automatically coprime to every minus divisor at fixed-power scale; this separation is already charged and supplies no additional density loss.

The canonical allocation density is now the density of this fixed-type three-divisor incidence, up to the `B^o(1)` type union.

```text
CANONICAL_ALLOCATION_DENSITY_REDUCED_TO_FIXED_TYPE_THREE_DIVISOR_INCIDENCE=true
CROSS_SIGN_COPRIMALITY_RECHARGE_ALLOWED=false
```

## 5. Next

Stage14-4ef should perform the elementary forward ledgers for the minus divisors and the plus Gaussian divisor/root line. If each side separately remains exponent-neutral, the only possible fixed-power saving will be their simultaneous correlation on the same primitive pair `(a,b)`.

## Boundary

```text
STAGE14_4EE=COMPLETE_CANONICAL_ALLOCATION_TYPE_FREEZE_AND_EXPLICIT_THREE_DIVISOR_INCIDENCE
CANONICAL_MINUS_DIVISORS_LIVE_ON_A_AND_B=true
CANONICAL_PLUS_DIVISOR_LIVES_ON_A2_PLUS_B2=true
CANONICAL_ALLOCATION_REPRESENTED_BY_THREE_DIVISOR_INCIDENCE=true
CANONICAL_ALLOCATION_TYPE_DICTIONARY_SIZE=Bo1
ONE_CANONICAL_ALLOCATION_TYPE_CAN_BE_FROZEN=true
CANONICAL_ALLOCATION_DENSITY_REDUCED_TO_FIXED_TYPE_THREE_DIVISOR_INCIDENCE=true
CANONICAL_ALLOCATION_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ef
```
