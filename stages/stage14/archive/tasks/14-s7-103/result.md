# Stage14-s7-103 — fixed-E endpoint: exhaust the bare unitary shadow and isolate physical completion

## Status

`COMPLETE_FIXED_E_ENDPOINT_BARE_UNITARY_SHADOW_EXHAUSTION`

Consumes batch-local `Stage14-s7-102`, merged `Stage14-s7-101`, merged `Stage14-s7-94`, and merged mainline `Stage14-4fs`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Exact endpoint parameterization

Freeze one exact subpolynomial complementary dilation and one exact subpolynomial primitive side

```text
E=E0,
r=r0=B^o(1).
```

Let the opposite primitive side be `s`, with

```text
gcd(r0,s)=1.
```

Up to the already-frozen orientation (`u=r0,v=s` or the swapped case), the normalized coordinates are

```text
m=r0*s,
n=E0*r0*s,
h=d0*E0*r0*s.
```

For the orientation `u=r0,v=s`,

```text
|Xr|=alpha*E0*r0^2,
|Yr|=beta*E0*s^2.
```

The swapped orientation is identical after exchanging the two frozen root roles.

Because `gcd(r0,s)=1`, the factorization `m=r0*s` is automatically a unitary partition: `r0||m` and `s||m`.

```text
FIXED_E_ENDPOINT_UNITARY_CONDITION_REDUCES_TO_COPRIMALITY=true
FIXED_E_ENDPOINT_UNITARY_ORIENTATION_ENTROPY_EXHAUSTED=true
```

## 2. Bare archimedean scalar cell

After the inherited sign/chamber/dyadic packet is frozen, all bare root/radial size restrictions above are monotone interval restrictions on the single scalar `s`:

- `n=E0*r0*s` gives a linear interval;
- `h=d0*E0*r0*s` gives a linear interval;
- the moving root `beta*E0*s^2` (or its swapped analogue) gives a square-root interval;
- the fixed root is either already admissible on the cell or the cell is empty.

Let one nonempty resulting scalar cell be

```text
I_s=(S_-,S_+]
```

with integer length

```text
H_s=#(I_s cap Z)=B^(lambda+o(1)).
```

A branch carrying polynomial mass has `lambda>0`.

The bare endpoint support is therefore exactly

```text
B_end(s)=1{s in I_s and gcd(s,r0)=1}
```

up to only the already-frozen `B^o(1)` packet labels.

## 3. Coprimality with subpolynomial r0 costs no fixed power

By Möbius inversion, for any integer interval of length `H_s`,

```text
#{s in I_s : gcd(s,r0)=1}
 = H_s*phi(r0)/r0 + O(tau(r0)).
```

Since `r0=B^o(1)`, standard divisor/Euler-product bounds give

```text
phi(r0)/r0 = B^(-o(1)),
tau(r0)=B^o(1).
```

Hence whenever `H_s=B^(lambda+o(1))` with `lambda>0`,

```text
#supp(B_end)=B^(lambda+o(1)).
```

Thus the endpoint bare-unitary shadow has the full scalar-capacity exponent. It cannot provide an additional fixed-power saving.

```text
FIXED_E_ENDPOINT_BARE_SHADOW_EXPONENT=lambda
FIXED_E_ENDPOINT_COPRIMALITY_COST=Bo1
FIXED_E_ENDPOINT_BARE_UNITARY_FIXED_POWER_SAVING=false
```

This does not close the branch: the exact physical completion Boolean

```text
C_end(s)
```

can still be sparse.

## 4. Endpoint survival becomes a pure conditional-completion budget

Write

```text
# {s in I_s : gcd(s,r0)=1 and C_end(s)=1}
 = B^(tau_end+o(1)),

delta_end=lambda-tau_end >= 0.
```

A heavy endpoint survivor therefore requires exactly

```text
lambda-delta_end >= mu.
```

The polynomial obstruction on this branch is no longer short-unitary existence. It is the conditional canonical/reverse physical-completion support along one scalar line.

```text
FIXED_E_ENDPOINT_POLYNOMIAL_OBSTRUCTION_IS_PHYSICAL_COMPLETION_ONLY=true
FIXED_E_ENDPOINT_SURVIVAL_BUDGET=lambda_minus_delta_end_ge_mu
RADIAL_ENDPOINT_SAVING_RECHARGED=false
RATIO_ENDPOINT_GEOMETRY_SAVING_RECHARGED=false
```

Merged s7-94 is respected: the endpoint is not discarded geometrically; instead its bare arithmetic shadow is evaluated exactly.

## 5. H decision

No sH yet. `C_end(s)` is still an internal Stage14 physical-completion predicate and has not been opened to a theorem-ready arithmetic sequence.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_103_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
```

## Boundary

```text
STAGE14_S7_103=COMPLETE_FIXED_E_ENDPOINT_BARE_UNITARY_SHADOW_EXHAUSTION
FIXED_E_ENDPOINT_UNITARY_CONDITION_REDUCES_TO_COPRIMALITY=true
FIXED_E_ENDPOINT_BARE_SHADOW_EXPONENT=lambda
FIXED_E_ENDPOINT_BARE_UNITARY_FIXED_POWER_SAVING=false
FIXED_E_ENDPOINT_POLYNOMIAL_OBSTRUCTION_IS_PHYSICAL_COMPLETION_ONLY=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_103_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-104
```
