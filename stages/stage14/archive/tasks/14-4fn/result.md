# Stage14-4fn — fixed complementary dilation: weighted unitary incidence to outer physical-support Boolean

## Status

`COMPLETE_FIXED_E_WEIGHTED_UNITARY_INCIDENCE_TO_OUTER_PHYSICAL_SUPPORT_BOOLEAN`

Consumes merged `Stage14-4fm`, merged `Stage14-s7-95`, merged `Stage14-Work-btX32`, and latest main

```text
43c2beeda0c9c5af2154d6deca5912d5be9e3ab2.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Fixed-E unitary-divisor packet

On the `E=B^o(1)` branch of merged 4fm, freeze one exact admissible value

```text
E=E0
```

at `B^o(1)` cost and put

```text
m=n/E0.
```

Every inner candidate is then determined by a unitary divisor

```text
u || m,
v=m/u,
gcd(u,v)=1,
```

lying in the transported short physical interval

```text
u in U_E0(m).
```

All local complementary-E conditions are constant on the surviving fixed-E cell and cannot be recharged. Let

```text
k_E0(m,u) in {0,1}
```

be the exact remaining canonical/root-origin/reverse/post-column physical Boolean for that candidate. No independence is assumed.

The fixed-E heavy incidence is

```text
I_E0
 = sum_m sum_{u || m, u in U_E0(m)} k_E0(m,u).      (1)
```

## 2. Fixed outer value has only subpolynomially many unitary candidates

For every polynomial-height `m`,

```text
#{u : u || m} = 2^omega(m) <= tau(m) = B^o(1).
```

The transported short interval can only reduce this set. Hence

```text
D_E0(m)
 := #{u || m : u in U_E0(m)}
 <= B^o(1).                                        (2)
```

This is the same fixed-inner-fiber budget already charged in the global/s unitary coordinate; it is not a new divisor saving.

## 3. Compress the inner physical weight to one outer Boolean

Define the exact outer acceptance predicate

```text
A_E0(m)
 := 1{there exists u || m,
       u in U_E0(m),
       k_E0(m,u)=1}.
```

Since every summand in (1) is Boolean and (2) holds,

```text
A_E0(m)
 <= sum_{u || m, u in U_E0(m)} k_E0(m,u)
 <= B^o(1) A_E0(m).                                (3)
```

Summing (3) over `m` gives

```text
sum_m A_E0(m)
 <= I_E0
 <= B^o(1) sum_m A_E0(m).                          (4)
```

Therefore the weighted unitary-divisor incidence and the outer support of the physical-existence predicate `A_E0` are exponent-equivalent.

This does **not** say that `k_E0(m,u)` is independent of `u`, nor that it factors pointwise. It says only that a `B^o(1)` inner fiber permits exact exponent-level projection to the outer variable by existential acceptance.

```text
FIXED_E_INNER_UNITARY_FIBER=Bo1
FIXED_E_OUTER_ACCEPTANCE_BOOLEAN_DEFINED=true
FIXED_E_WEIGHTED_INCIDENCE_OUTER_SUPPORT_EXPONENT_EQUIVALENT=true
INNER_WEIGHT_POINTWISE_FACTORIZATION_PROVED=false
UNITARY_DIVISOR_DENSITY_RECHARGED=false
```

## 4. Consequence for a heavy survivor

If the fixed-E branch carries heavy mass

```text
I_E0 >= B^(mu-o(1)),
```

then (4) forces

```text
#{m : A_E0(m)=1} >= B^(mu-o(1)).                   (5)
```

Thus the polynomial obstruction on this branch is no longer multiplicity of accepted unitary divisors at fixed `m`; it is the outer density of normalized integers admitting at least one **physical** unitary divisor in the short interval.

The canonical/reverse arithmetic is retained inside `A_E0(m)` and has not been discarded.

## H decision

No new H is opened yet. Merged q14/Ford becomes structurally closer because the receiver is now an outer existential-divisor support count, but the accepted divisor is unitary and carries the Stage14 canonical/reverse condition. No bounded-distortion comparison with Ford's unrestricted divisor ensemble is proved.

```text
Q14_OUTER_EXISTENTIAL_SUPPORT_FORM_REACHED_ON_FIXED_E=true
Q14_PHYSICAL_UNITARY_TO_UNRESTRICTED_DIVISOR_TRANSFER_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT=Stage14-4fo
```
