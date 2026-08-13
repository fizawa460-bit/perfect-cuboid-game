# Stage14-s7-88 — peel the fixed numerator from the normalized radial root factorization

## Status

`COMPLETE_FIXED_NUMERATOR_PRIME_POWER_ALLOCATION_AND_COEFFICIENT_FREE_TRIPLE_PRODUCT_REDUCTION`

Consumes batch-local `Stage14-s7-87`, merged `Stage14-s7-85/86`, and the same frozen heavy-ray/agreement packet.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering normalized equation

Stage14-s7-87 gives exactly

```text
h=d0*n,
J*a*b=c0*n,
gcd(c0,d0)=1,
```

where `c0,d0` are fixed on the packet, `J` is squarefree, and the s7-85 root normal form remains

```text
|Xr|=J*A*a^2,
|Yr|=J*B*b^2,
A*B=K_Z,
gcd(A,B)=1,
gcd(J,K_Z)=1.
```

The accepted normalized support still has

```text
#N_* >= B^(mu-o(1)).
```

## 2. Prime-power allocation of c0 is divisor-many

For every accepted point,

```text
c0 | J*a*b.
```

For each prime power `p^e || c0`, allocate exactly `e` copies among the three factors according to the actual valuations of `(J,a,b)`.  Since `J` is squarefree, its allocated exponent is `0` or `1`; the remaining copies are allocated to `a` and `b`.

The number of possible ordered exponent allocations over all primes is bounded by

```text
d_3(c0)=B^o(1).
```

Hence on a polynomial-support subpacket one may freeze one exact coefficient allocation

```text
c0=c_J*c_a*c_b,
```

with

```text
c_J | J,
c_a | a,
c_b | b.
```

No independence is asserted; the allocation is chosen from the actual physical point and frozen by a divisor-many pigeonhole.

```text
FIXED_NUMERATOR_PRIME_POWER_ALLOCATION_COUNT=Bo1
FIXED_NUMERATOR_ALLOCATION_CAN_BE_FROZEN=true
NUMERATOR_ALLOCATION_RECHARGE_ALLOWED=false
```

## 3. Peel the fixed coefficients exactly

Write

```text
J=c_J*J1,
a=c_a*a1,
b=c_b*b1.
```

Then

```text
J*a*b
 = c_J*c_a*c_b * J1*a1*b1
 = c0*J1*a1*b1.
```

Comparing with `J*a*b=c0*n` gives the exact coefficient-free product equation

```text
boxed:
n=J1*a1*b1.
```

Because `c_J|J` and `J` is squarefree, `J1` remains squarefree.  Every inherited gcd/range/orientation condition is retained after substituting the fixed coefficient factors.

The radial coordinate is now

```text
boxed:
h=d0*J1*a1*b1.
```

Thus both fixed rational-square coefficients have been removed from the moving multiplicative structure: `d0` is a fixed outer dilation and `c0` has been absorbed into a divisor-many frozen coefficient packet.

```text
COEFFICIENT_FREE_NORMALIZED_PRODUCT=n_equals_J1_a1_b1
NORMALIZED_SHARED_FACTOR_J1_SQUAREFREE=true
RADIAL_SCALE=h_equals_d0_J1_a1_b1
FIXED_RATIONAL_SQUARE_COEFFICIENTS_FULLY_PEELED=true
```

## 4. Fibers over n remain divisor-many

For one exact normalized value `n`, ignoring all additional physical filters,

```text
# {(J1,a1,b1): J1*a1*b1=n}
 <= d_3(n)
 = B^o(1).
```

The squarefree restriction on `J1`, inherited gcd conditions and physical masks only reduce this number.

Therefore

```text
# physical normalized triples over one n = B^o(1).
```

Together with s7-87,

```text
B^(mu-o(1)) <= #N_* <= B^(sigma-lambda+o(1)).
```

So the polynomial heavy-ray mass is now carried by polynomially many exact values of the coefficient-free ternary product `J1*a1*b1`.

```text
FIXED_N_NORMALIZED_TRIPLE_FIBER=Bo1
POLYNOMIAL_RADIAL_MASS_REQUIRES_POLYNOMIAL_NORMALIZED_PRODUCT_SUPPORT=true
```

## 5. Receiver and H decision

The next internal step is to rewrite the two physical root factors in the peeled variables and freeze the exact coefficient system seen by `(J1,a1,b1)`.  A generic multiplication-table or divisor theorem is not yet applicable because the physical acceptance predicate is still correlated with both root factors and reverse completion.

```text
RECEIVER_MATERIALLY_CHANGED=false
S7_88_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_88=COMPLETE_FIXED_NUMERATOR_PRIME_POWER_ALLOCATION_AND_COEFFICIENT_FREE_TRIPLE_PRODUCT_REDUCTION
FIXED_NUMERATOR_PRIME_POWER_ALLOCATION_COUNT=Bo1
FIXED_NUMERATOR_ALLOCATION_CAN_BE_FROZEN=true
COEFFICIENT_FREE_NORMALIZED_PRODUCT=n_equals_J1_a1_b1
NORMALIZED_SHARED_FACTOR_J1_SQUAREFREE=true
FIXED_N_NORMALIZED_TRIPLE_FIBER=Bo1
POLYNOMIAL_RADIAL_MASS_REQUIRES_POLYNOMIAL_NORMALIZED_PRODUCT_SUPPORT=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_88_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-89
```
