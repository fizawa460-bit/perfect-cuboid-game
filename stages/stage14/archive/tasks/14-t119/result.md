# Stage14-t119 — exceptional multiplier family is subpolynomial and may be frozen

## Status

`COMPLETE_EXCEPTIONAL_MULTIPLIER_SUBPOLYNOMIAL_COMPLEXITY_AND_FREEZING`

Consumes Stage14-t118 on the same batch branch and the merged fixed-U packet size bounds.

The t118 exceptional multiplier satisfies

```text
p|m_E => p|E_U,
rad(E_U)<=B^C,
m_E<=B^A
```

for fixed absolute packet-range constants `A,C=O(1)`. The finite two-primary factor is absorbed into the exceptional label and costs only `B^o(1)`.

We now prove uniformly that the number of possible `E_U`-smooth multipliers in the physical range is subpolynomial.

Let `P` be the odd prime support of `E_U`, let `X=B^A`, and put

```text
s=1/log log B.
```

Rankin's bound gives

```text
#{m<=X: p|m => p in P}
 <= X^s * product_{p in P}(1-p^(-s))^(-1).
```

The first factor is

```text
X^s=exp(O(log B/log log B))=B^o(1).
```

For the Euler product split the packet primes at `Y=log B`.

For `p<=Y`, `s log p<=1`, hence

```text
1-p^(-s)=1-exp(-s log p) >> s log p,
```

so each logarithmic Euler factor is at most `O(log log log B)`. The elementary Chebyshev prime-counting bound

```text
pi(Y)=O(Y/log Y)
```

therefore gives total small-prime logarithmic cost

```text
O((log B/log log B)*log log log B)=o(log B).
```

For `p>Y`, one has `p^(-s)<=e^(-1)`, so each logarithmic Euler factor is `O(1)`. Since

```text
sum_{p in P} log p = log rad(E_U) <= C log B,
```

the number of such large packet primes is at most

```text
O(log B/log log B),
```

again giving total logarithmic cost `o(log B)`.

Consequently

```text
product_{p in P}(1-p^(-s))^(-1)=B^o(1)
```

uniformly in every live fixed-U packet, and hence

```text
#M_U(B)=B^o(1).
```

The admissible exceptional multiplier set is a subset of this family, so it also has `B^o(1)` size.

Therefore the exact t118 cylinder union may be expanded and one multiplier `m` frozen at only `B^o(1)` charged-once cost. After this freeze the outer scalar norm is

```text
n=m*n_G,
```

where

```text
gcd(n_G,E_U)=1,
every odd p|n_G satisfies p==1 mod 4.
```

All exceptional-local labels above the fixed `m` are also only `B^o(1)` and may be frozen without creating a new polynomial length. The remaining polynomial mobility is the generic scalar norm `n_G` together with its primitive split-prime orientation existence predicate.

This does **not** assert that choosing a particular `m` is density-neutral under the prime weight `A(m*n_G)`. Any fixed-power effect caused by the physical choice of `m` is henceforth represented honestly as a weighted outer-support effect in the resulting `n_G` family, not as an independent exceptional-label density factor.

```text
EXCEPTIONAL_MULTIPLIER_FAMILY_SIZE=Bo1
EXCEPTIONAL_MULTIPLIER_RANKIN_BOUND_PROVED=true
EXCEPTIONAL_MULTIPLIER_MAY_BE_FROZEN_AT_BO1_COST=true
EXCEPTIONAL_LABELS_MAY_BE_FROZEN_AT_BO1_COST=true
GENERIC_SCALAR_NORM_IS_ONLY_REMAINING_POLYNOMIAL_COFACTOR_COORDINATE=true
EXCEPTIONAL_MULTIPLIER_DENSITY_RECHARGE_ALLOWED=false
WEIGHTED_EFFECT_OF_FROZEN_MULTIPLIER_RETAINED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportOrSelectedProjectiveClassNearTotalDepletion
NEXT_INTERNAL_TARGET=GenericNormSupportRelocationAndSavingDichotomy
NEXT=Stage14-t120
```
