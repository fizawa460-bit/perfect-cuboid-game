# Stage14-s7-97 — fixed complementary dilation to weighted unitary-divisor completion incidence

## Status

`COMPLETE_FIXED_E_LOCAL_MASK_EXHAUSTION_AND_CANONICAL_REVERSE_WEIGHT_ISOLATION`

Consumes batch-local `Stage14-s7-96`, merged `Stage14-4fm`, merged `Stage14-4eq`, and merged `Stage14-Work-btX32`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze the subpolynomial complementary dilation

On the `E=B^o(1)` branch from s7-96 / merged 4fm, freeze one exact surviving value

```text
E=E0.
```

The number of possible exact values is `B^o(1)`. Since the cell survives,

```text
m_E(E0)=1.
```

Therefore the local complementary mask is exhausted on this cell and cannot be charged as an additional density loss.

Put

```text
m:=n/E0=q.
```

Then exactly

```text
m=u*v,
gcd(u,v)=1,
u||m,
v=m/u.
```

The short primitive-ratio condition is

```text
u^2/m in R_int(E0*m),
```

or equivalently

```text
u in sqrt(m*R_int(E0*m)).
```

## 2. The remaining weight is genuinely inner-dependent

Define

```text
c_E0(m,u)
 := m_cpl(E0*m,u,m/u,E0).
```

Then the fixed-`E` physical incidence is exactly

```text
I_E0
 = sum_m
   sum_{
      u||m,
      u in sqrt(m*R_int(E0*m))
   }
      c_E0(m,u).
```

No merged result proves that `c_E0(m,u)` is constant in `u`, multiplicative, or a function of `m` alone. Work-btX32 explicitly records this inner dependence as the current global/s obstruction.

```text
FIXED_E_LOCAL_MASK_EXHAUSTED=true
FIXED_E_CANONICAL_REVERSE_WEIGHT=c_E0_of_m_u
FIXED_E_CANONICAL_REVERSE_WEIGHT_OUTER_ONLY_PROVED=false
FIXED_E_CANONICAL_REVERSE_WEIGHT_MULTIPLICATIVE_PROVED=false
```

## 3. Completion multiplicity is only B^o(1), but existence is not automatic

For fixed `(E0,m,u)` the values

```text
n=E0*m,
v=m/u,
L=E0*u^2
```

are fixed. Hence the corresponding root pair and radial coordinate are fixed up to the already-frozen packet coefficients.

Merged 4eq gives only `B^o(1)` full physical reverse completions over fixed exact radial/reciprocal data. Therefore the completion multiplicity over one `(E0,m,u)` is `B^o(1)`.

This does **not** imply `c_E0(m,u)=1`. It only proves that a successful inner candidate cannot hide polynomial multiplicity in its reverse fiber.

```text
FIXED_E_M_U_FULL_PHYSICAL_COMPLETION_MULTIPLICITY=Bo1
FIXED_E_COMPLETION_EXISTENCE_AUTOMATIC=false
FIXED_E_REVERSE_FIBER_RECHARGE_ALLOWED=false
```

For fixed `m`, the number of unitary divisors is

```text
2^omega(m)=B^o(1)
```

on the polynomial Stage14 range. Thus accepted `m` support and the weighted incidence have the same fixed-power exponent, but this finite fiber is already charged and supplies no extra saving.

## 4. q14 / H decision

The fixed-`E` branch is now theorem-shaped as a short unitary-divisor interval with a Boolean inner weight, but q14's required bounded-distortion transfer is still unproved precisely because `c_E0(m,u)` may select a highly biased subset of unitary divisors.

A new sH target is therefore still premature. The next stage treats the polynomial-`E` branch and separates whether the primitive product `m=uv` is subpolynomial or polynomial.

```text
Q14_FIXED_E_PHYSICAL_MEASURE_BOUNDED_DISTORTION_PROVED=false
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false
RECEIVER_MATERIALLY_CHANGED=false
S7_97_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
```

## Boundary

```text
STAGE14_S7_97=COMPLETE_FIXED_E_LOCAL_MASK_EXHAUSTION_AND_CANONICAL_REVERSE_WEIGHT_ISOLATION
FIXED_E_LOCAL_MASK_EXHAUSTED=true
FIXED_E_CANONICAL_REVERSE_WEIGHT_OUTER_ONLY_PROVED=false
FIXED_E_M_U_FULL_PHYSICAL_COMPLETION_MULTIPLICITY=Bo1
FIXED_E_COMPLETION_EXISTENCE_AUTOMATIC=false
Q14_FIXED_E_PHYSICAL_MEASURE_BOUNDED_DISTORTION_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_97_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-98
```