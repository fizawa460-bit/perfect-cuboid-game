# Stage14-s7-147 — exact q17-good witness expansion

## Status

`COMPLETE_GOOD_INDICATOR_TO_Q17_WITNESS_COUNT_FIXED_POWER_EQUIVALENCE`

Consumes merged Stage14-s7-144..146 and merged Work-cjX48/q22.

## 1. Frozen good-packet witness count

On one frozen active nonaligned principal cell retain the Stage14-s7-144 notation

```text
pi : Lambda -> Theta,
G subset Theta = q17-good reciprocal-CRT packet support.
```

For each complete q17 packet `theta`, let

```text
N_G(theta)
```

be the number of admissible q17 reciprocal-CRT kernel witnesses in the already-frozen q17 witness model whose existence defines membership in `G`.

By definition of the good support,

```text
theta in G  iff  N_G(theta) >= 1.
```

All labels used in this count are the already-frozen q17 packet labels; no residual root/canonical/post-column mask is inserted here.

## 2. Pointwise multiplicity bound is already available

The q17 / main reciprocal-divisor reconstruction gives divisor-many kernel witnesses on a polynomial-height cell. Hence uniformly

```text
0 <= N_G(theta) <= B^o(1).
```

This is a multiplicity statement only. It is consumed here solely to replace a Boolean support indicator by a nonnegative witness count at fixed-power exponent scale; it is not charged as a density saving.

Thus pointwise

```text
1_G(theta) <= N_G(theta) <= B^o(1) 1_G(theta).
```

## 3. Good-indicator first moment becomes a witness first moment

Define

```text
M1_G := sum_{lambda in Lambda} 1_G(pi(lambda)),
J1_G := sum_{lambda in Lambda} N_G(pi(lambda)).
```

Summing the pointwise sandwich gives

```text
M1_G <= J1_G <= B^o(1) M1_G.
```

Therefore `M1_G` and `J1_G` have the same fixed-power exponent.

This proves the q22 exact-witness-expansion handoff in the only sense needed for the Stage14 exponent ledger:

```text
Q22_GOOD_INDICATOR_EXACT_WITNESS_EXPANSION_TEST=PASS_NONNEGATIVE_Q17_WITNESS_COUNT
S_GOOD_INDICATOR_TO_Q17_WITNESS_FIRST_MOMENT_ADAPTER_PROVED=true
Q17_WITNESS_MULTIPLICITY_RECHARGED_AS_SAVING=false
```

## 4. Charged measures remain distinct

For scalar branches A/C, `Lambda` is the retained scalar filtered-tau3 witness family. For branch D, `Lambda` remains indexed over the charged polynomial `(E,m)` outer measure and its retained first-layer witnesses.

No map `(E,m) -> Em` is used to change the theorem measure.

```text
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
S_FIXED_N_PAIR_FIBER_RECHARGED=false
```

The residual post-mask remains outside `N_G` and is still separately charged.

```text
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-148
```