# Stage14-Work-clX50 — moving common core / two coprime side integration

## Status

`COMPLETE_MOVING_COMMON_CORE_TWO_COPRIME_SIDE_RECEIVER_INTEGRATION`

Consumes merged Work-ckX49/q23 and merged Stage14-s7-150..155.

Stage14-s7-150..152 proves that the moving `W1(lambda)` dependence cannot be replaced by a fixed shift, ordinary divisor-AP modulus, or bounded-complexity binary form without losing the charged filtered-tau3 witness measure. Stage14-s7-153..155 then exposes a strictly sharper exact factorization.

For every retained first-layer witness `lambda`, write

```text
W1(lambda)=C1*p_H*q_H*p_+*q_-,
C1=4*r_ep*s_ep*epsilon_k,
prime_support(p_H*q_H) subset prime_support(H(lambda)),
p_+ | C_+(lambda),
q_- | C_-(lambda),
gcd(C_+,C_-)=1,
gcd(p_+,q_-)=1.
```

The q17 reciprocal witness remains

```text
f*n=W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V),
```

with all frozen q17 kernel predicates retained.

## X50 integration lemma

The new split separates the moving arithmetic into exactly two kinds of dependence:

1. a common-prime-support channel carried entirely by the moving core `H(lambda)`;
2. two mutually coprime side-divisor channels carried by `C_+(lambda)` and `C_-(lambda)`.

Hence any future theorem may condition on or decompose over `H(lambda)` without recharging the already-proved common-gcd localization, but it must still preserve the charged filtered-tau3 witness measure and the reciprocal-CRT constraints. Coprimality of the side movers does not by itself yield a positive first-moment lower bound.

```text
FIRST_REVERSE_EXACT_COMMON_GCD_CONSUMED=true
PQ_COMMON_PRIME_SUPPORT_LOCALIZATION_CONSUMED=true
PQ_COPRIME_SIDE_MOVERS_CONSUMED=true
COMMON_CORE_SIDE_COPRIME_DECOMPOSITION_RECHARGE_FORBIDDEN=true
COPRIME_SIDE_STRUCTURE_ALONE_IMPLIES_POSITIVE_DENSITY=false
```

## Active s theorem species

Scalar:

```text
UniformScalarFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound
```

Polynomial outer pair:

```text
UniformPolynomialOuterPairFilteredTau3MovingCommonCoreTwoCoprimeSideReciprocalCRTJointIncidenceFirstMomentLowerBound
```

The polynomial `(E,m)` measure remains charged as a pair. No `Em` scalarization is allowed.

```text
S_COMMON_CORE_COPRIME_SIDE_THEOREM_SPECIES_COUNT=2
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
```

## q24 gate

Merged Stage14-s7-155 explicitly freezes

```text
Q24_THEOREM_TARGET_NOW_STABLE=true
Q24_NEEDED=true
```

so the XQ q-component is triggered. q24 searches only the sharpened common-core / two-coprime-side first-moment target; it does not rerun q23's generic witness-coupled search.

```text
Q_COMPONENT=COMPLETE
Q_TRIGGER_STAGE=Stage14-s7-155
Q_LEDGER_BASELINE=Stage14-q23
Q24_NEEDED=true
```

## H / exponent ledger

```text
MAINLINE_H_NEEDED=true
MAINLINE_H_COMPLETED=true
MAINLINE_BLOCKED_BY_H=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
FIXED_U_H_COMPLETED=true
FIXED_U_BLOCKED_BY_H=true
TH33_COMPLETE_CONSUMED=true
TH34_NEEDED=false
WHOLE_STAGE14_BLOCKED_BY_EXTERNAL_GATES=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

## Next

Primary s handoffs from q24:

```text
Stage14-s7-156
Stage14-s7-157+
```

Normal Work/XQ revisit: approximately `s7-158`, or earlier on a successful common-core conditioning/side-factor separation adapter, a material post-mask receiver change, parked-gate resolution, or exponent change.
