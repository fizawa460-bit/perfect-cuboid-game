# Stage14-q24 — moving common-core / two-coprime-side literature radar

## Status

`COMPLETE_MOVING_COMMON_CORE_TWO_COPRIME_SIDE_LITERATURE_RADAR`

Triggered by merged Stage14-s7-155 after q23's generic witness-coupled target was sharpened to

```text
W1(lambda)=C1*p_H*q_H*p_+*q_-,
prime_support(p_H*q_H) subset prime_support(H(lambda)),
p_+|C_+(lambda),
q_-|C_-(lambda),
gcd(C_+,C_-)=1,
```

together with the q17 reciprocal-CRT witness

```text
f*n=W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V).
```

The requested theorem must give a uniform positive first-moment lower bound on every frozen principal cell, preserve all retained filtered-tau3 / q17 predicates, and preserve the scalar versus polynomial `(E,m)` charged theorem measures.

## Direct-theorem audit

```text
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
MOVING_COMMON_CORE_TWO_COPRIME_SIDE_DIRECT_THEOREM_FOUND=false
```

### Near architecture A — shifted divisor convolution

Topacogullari, *The Shifted Convolution of Divisor Functions* (arXiv:1506.02608), proves uniform asymptotics with power-saving error for `d_3(n)d(n+h)`-type shifted convolutions. This remains relevant only after an exact reduction to a fixed/uniform shift. Stage14-s7-150..152 proves that such a reduction is not presently available for the full charged witness family.

```text
SHIFTED_D3_D_DIRECT_TRANSFER_PROVED=false
```

### Near architecture B — additive divisor lower bounds

Ng--Thom, *Bounds and Conjectures for additive divisor sums* (arXiv:1609.01411), gives lower bounds of the expected order for classical additive divisor sums, uniform in the shift. It does not preserve the moving common core `H(lambda)`, the two side-host allocations, or the reciprocal-CRT filter as frozen Stage14 predicates.

```text
ADDITIVE_DIVISOR_LOWER_BOUND_DIRECT_TRANSFER_PROVED=false
```

### Near architecture C — binary-form divisor sums

Frei--Sofos, *Generalised divisor sums of binary forms over number fields* (arXiv:1609.04002), supplies asymptotics and lower bounds for broad divisor sums over binary-form values. The present Stage14 object has a witness-dependent common core plus two coprime side-divisor channels and no exact bounded-complexity binary-form encoding preserving the charged measure.

```text
BINARY_FORM_DIVISOR_SUM_DIRECT_TRANSFER_PROVED=false
```

### Near architecture D — generalized divisor functions in AP

Nguyen, *Generalized divisor functions in arithmetic progressions: II* (arXiv:2302.12815), gives second-moment estimates for modified shifted convolutions of the generalized 3-fold divisor function. The Stage14 target is a positive individual-cell first moment with moving host and exact reciprocal-CRT filters; no direct adapter is known.

```text
GENERALIZED_DIVISOR_AP_DIRECT_TRANSFER_PROVED=false
```

## q24 no-go / next adapter tests

The coprime-side split is materially stronger than q23, but it is not yet a standard theorem input. The next internal tests should exploit the split rather than rerun generic shifted-convolution searches:

```text
Q24_COMMON_CORE_CONDITIONING_TEST=Stage14-s7-156
Q24_COPRIME_SIDE_EULER_PRODUCT_OR_SIEVE_FACTOR_TEST=Stage14-s7-157+
```

Test 1: condition on a localized common core `H` and determine whether its total charged cost is `B^o(1)` on a principal cell or whether a polynomial family of `H` must remain averaged.

Test 2: after freezing/conditioning `H`, test whether the mutually coprime side movers `p_+|C_+`, `q_-|C_-` permit an exact multiplicative/Euler-product, local-density, or lower-bound sieve factorization compatible with the reciprocal-CRT congruences. A mere upper-bound factorization is insufficient.

```text
COMMON_CORE_CONDITIONING_ADAPTER_PROVED=false
COPRIME_SIDE_POSITIVE_DENSITY_FACTORIZATION_PROVED=false
RECIPROCAL_CRT_PRESERVING_EULER_PRODUCT_ADAPTER_PROVED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
POST_MASK_REMAINS_SEPARATELY_CHARGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
