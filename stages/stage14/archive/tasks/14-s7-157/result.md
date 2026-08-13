# Stage14-s7-157 — coprime-side Euler-product / sieve-factor test

## Status

`COMPLETE_COPRIME_SIDE_POSITIVE_FACTORIZATION_AUDIT`

Consumes batch-local Stage14-s7-156 and merged q24.

After retaining the common-core average, the exact arithmetic on each first-layer witness has

```text
W1(lambda)=C1*p_H*q_H*p_+*q_-,
p_+ | C_+(lambda),
q_- | C_-(lambda),
gcd(C_+,C_-)=gcd(p_+,q_-)=1,
```

and the q17 reciprocal witness

```text
f*n=W1(lambda),
n+f == 0 (mod 2U),
n-f == 0 (mod 2V).
```

The side-host coprimality separates prime support of `p_+` and `q_-`, but it does not separate reciprocal-CRT acceptance into a product of one predicate on the `+` host and one predicate on the `-` host. The divisor allocation `(f,n)` is performed after all factors of `W1` have been assembled, and the two congruences simultaneously see the complete allocated products.

Hence the merged identities do not supply an exact positive Euler product or lower-bound sieve factorization for the full charged incidence.

There is, however, an exact unit-stratum normal form. Put

```text
Q=2*U*V
```

with `gcd(U,V)=1` on the frozen agreement packet. On the stratum

```text
gcd(W1,Q)=1,
```

every divisor pair `f*n=W1` is a unit modulo `Q`. Writing

```text
r = n*f^{-1} (mod Q),
```

the reciprocal congruences are exactly equivalent to

```text
r == -1 (mod 2U),
r == +1 (mod 2V).
```

The two conditions define one unit residue class `r0 (mod Q)`. Therefore its indicator admits the exact Dirichlet-character expansion

```text
1_{r=r0 mod Q}
 = 1/phi(Q) * sum_{chi mod Q} chi(r*inv(r0)).
```

This expansion is algebraically exact on the unit stratum, but nonprincipal characters have signs/phases. It is not a nonnegative Euler product and does not itself prove a lower bound. In particular, side-host coprimality does not justify discarding or absolutely bounding the nonprincipal part at a power-saving level.

The complementary nonunit stratum `gcd(W1,Q)>1` is not removed by this argument and remains separately charged.

```text
Q24_COPRIME_SIDE_EULER_PRODUCT_OR_SIEVE_FACTOR_TEST=FAIL_NO_POSITIVE_FACTORIZATION
COPRIME_SIDE_POSITIVE_DENSITY_FACTORIZATION_PROVED=false
RECIPROCAL_CRT_PRESERVING_EULER_PRODUCT_ADAPTER_PROVED=false
UNIT_STRATUM_RECIPROCAL_CRT_RATIO_RESIDUE_NORMAL_FORM_PROVED=true
UNIT_STRATUM_DIRICHLET_CHARACTER_EXPANSION_PROVED=true
UNIT_STRATUM_CHARACTER_EXPANSION_IMPLIES_LOWER_BOUND=false
NONUNIT_Q_SUPPORTED_STRATUM_REMAINS=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-158
```
