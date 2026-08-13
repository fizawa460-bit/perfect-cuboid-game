# Stage14-s7-154 — common-core / coprime-side split of the moving p,q factors

## Status

`COMPLETE_PQ_COMMON_CORE_COPRIME_SIDE_SPLIT`

Consumes Stage14-s7-153.

For one retained first-layer witness write the exact reconstruction as

```text
c*p = H*C_+,
d*q = H*C_-,
gcd(C_+,C_-)=1.
```

Define the `H`-supported parts of the moving reciprocal factors by

```text
p_H := product over ell|H of ell^v_ell(p),
q_H := product over ell|H of ell^v_ell(q),
p_+ := p/p_H,
q_- := q/q_H.
```

Then, exactly,

```text
p = p_H*p_+,
q = q_H*q_-,
prime_support(p_H*q_H) subset prime_support(H),
gcd(p_+,H)=gcd(q_-,H)=1.
```

Since `p | H*C_+` and `q | H*C_-`, removing every prime supported on `H` gives

```text
p_+ | C_+,
q_- | C_-.
```

Because `gcd(C_+,C_-)=1`,

```text
gcd(p_+,q_-)=1.
```

Therefore the witness-dependent second reciprocal product has the exact split

```text
W1(lambda)
 = 4*r_ep*s_ep*epsilon_k * p_H*q_H * p_+*q_-,
```

with all cross-side common prime support confined to the moving common core `H`; the remaining two side movers are coprime and hosted separately by `C_+` and `C_-`.

The values `H,p_H,q_H` still move with the retained first-layer witness. They are not frozen coefficients and cannot be discarded or charged as a sparse set. For each fixed witness, the possible divisor allocations are already within the previously consumed `B^o(1)` reverse-witness multiplicity; that multiplicity is not recharged here.

The polynomial outer-pair branch continues to use `(E,m)` as its charged measure. No host projection to `z=Em` is introduced.

```text
PQ_COMMON_PRIME_SUPPORT_LOCALIZED_TO_H=true
PQ_COPRIME_SIDE_MOVERS_PROVED=true
P_PLUS_DIVIDES_C_PLUS=true
Q_MINUS_DIVIDES_C_MINUS=true
PQ_SIDE_COPRIMALITY_PROVED=true
COMMON_CORE_IS_MOVING_NOT_FIXED=true
REVERSE_WITNESS_MULTIPLICITY_RECHARGED=false
PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S_ROUTE_H_NEEDED=false
NEXT=Stage14-s7-155
```