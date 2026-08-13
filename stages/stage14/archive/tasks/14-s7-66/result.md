# Stage14-s7-66 — primitive signed-factor allocation normalization

## Status

`COMPLETE_PRIMITIVE_SIGNED_FACTOR_ALLOCATION_NORMALIZATION`

Consumes only merged sources on batch-start main `9613e691496a1184435e5ecce6700880a9f87cc6`: merged `Stage14-s7-65`, `Stage14-4dz`, `Stage14-s7-46`, and `Stage14-s7-60`. Unmerged work is advisory only.

The canonical theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Exact primitive signed factors

Merged s7-65 writes

```text
r=g a,
s=g b,
gcd(a,b)=1,
0<a<b,
g=B^o(1),
D=(r+s)/2,
A=(s-r)/2.
```

Therefore exactly

```text
D-A = r = g a,
D+A = s = g b.
```

So the two real linear factors of the minus norm are already the primitive coordinates, up to the subpolynomial common scale.

```text
PRIMITIVE_SIGNED_FACTORS_EQUAL_GA_AND_GB=true
```

## 2. Minus allocation separates onto a and b

In merged s7-46 the agreement allocation is reconstructed from coprime factors placed in `D+A` and `D-A`. After peeling the allowed common-scale/endpoint support, every fixed-power minus-cell divisor therefore lies on exactly one primitive coordinate:

```text
U_b | b,
V_a | a,
gcd(U_b,V_a)=1.
```

Conversely any physical minus allocation determines such a pair, with only `B^o(1)` ambiguity from the already-frozen scale and 2-primary decorations. This is the signed version of the divisor factorization `d|ab => d=d_a d_b` from s7-65.

```text
MINUS_ALLOCATION_LOCALIZES_TO_DIVISORS_OF_A_AND_B=true
MINUS_CROSS_COORDINATE_GCD_ONE=true
MINUS_ALLOCATION_EXTRA_SCALE_MULTIPLICITY=Bo1
```

This is a coordinate normalization, not a density saving.

## 3. Reciprocal reconstruction does not create a new support length

Once the minus allocation pair and the plus allocation are fixed, merged s7-46 reconstructs the signed quotient pair and the remaining reciprocal/post-column variables with `B^o(1)` multiplicity. Merged s7-60 forbids charging reciprocal completion as an independent polynomial coordinate.

Thus the primitive signed-factor normalization removes an artificial mixed divisor coordinate but does not reduce the principal-density exponent.

```text
SIGNED_QUOTIENT_RECONSTRUCTION_AFTER_ALLOCATION=Bo1
RECIPROCAL_COMPLETION_INDEPENDENT_SUPPORT=false
```

## 4. Receiver

The s7-65 receiver is retained, now with an exact canonical minus-coordinate model:

```text
F_-(a,b)=oddpart(ab)
```

is allocated through divisors of coprime `a` and `b`, while the plus norm allocation and coupled reciprocal acceptance remain unresolved.

```text
CURRENT_S_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChartCoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity
RECEIVER_MATERIALLY_CHANGED=false
```

## 5. H decision

No new sH is needed. The next internal step is to normalize the plus norm allocation on `a^2+b^2` using primitive sum-of-two-squares arithmetic.

```text
S7_66_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_66=COMPLETE_PRIMITIVE_SIGNED_FACTOR_ALLOCATION_NORMALIZATION
PRIMITIVE_SIGNED_FACTORS_EQUAL_GA_AND_GB=true
MINUS_ALLOCATION_LOCALIZES_TO_DIVISORS_OF_A_AND_B=true
MINUS_CROSS_COORDINATE_GCD_ONE=true
SIGNED_QUOTIENT_RECONSTRUCTION_AFTER_ALLOCATION=Bo1
RECEIVER_MATERIALLY_CHANGED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_66_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-67
```