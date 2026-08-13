# Stage14-s7-101 — fixed-E physical-existence support splits into primitive endpoint or two-sided unitary partition

## Status

`COMPLETE_FIXED_E_OUTER_EXISTENCE_SUPPORT_TO_PRIMITIVE_ENDPOINT_OR_TWO_SIDED_UNITARY_PARTITION_RECEIVERS`

Consumes batch-local `Stage14-s7-99/100`, merged `Stage14-4fl`, merged mainline `Stage14-4fn..4fp`, merged `Stage14-s7-94..98`, and merged `Stage14-Work-buX33`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the fixed-E outer-support receiver

Freeze one exact surviving complementary dilation

```text
E=E0.
```

Merged 4fn/4fp and Work-buX33 reduce this branch to the outer support

```text
A_E0(m)=1
```

iff there exists

```text
m=u*v,
gcd(u,v)=1,
u||m,
u/v in R_phys(E0*m),
```

with the retained physical canonical/root-origin/reverse completion predicate true.

A surviving fixed-E heavy cell requires

```text
#{m : A_E0(m)=1} >= B^(mu-o(1)).
```

The number of unitary witnesses at fixed `m` is already exhausted as `B^o(1)` and is not charged again.

## 2. Freeze primitive-factor exponent cells

Localize the two primitive factors by exponent cells

```text
u=B^(a+o(1)),
v=B^(b+o(1)),
a,b>=0.
```

Only exponent-zero versus positive exponent matters for the present split.  After the finite choice of which side is smaller/moving orientation, there are two exhaustive alternatives:

```text
(A) min(a,b)=0;
(B) a>0 and b>0.
```

This is the same projective-scale distinction already permitted by merged 4fl, now applied after the stronger outer-support compression.  It is not a new endpoint-density saving.

```text
FIXED_E_PRIMITIVE_FACTOR_SCALE_SPLIT_EXPLICIT=true
RATIO_ENDPOINT_GEOMETRY_RECHARGED=false
```

## 3. Endpoint primitive-factor branch is one-dimensional after freezing the small side

On branch (A), suppose first

```text
u=B^o(1).
```

There are only `B^o(1)` exact values, so freeze

```text
u=r0.
```

Then

```text
v=s,
m=r0*s,
gcd(r0,s)=1.
```

The exact normalized formulas become

```text
n=E0*r0*s,
|Xr|=alpha*E0*r0^2,
|Yr|=beta*E0*s^2,
h=d0*E0*r0*s.
```

Thus one root factor is fixed, the opposite root factor is a fixed coefficient times `s^2`, and the radial coordinate is linear in `s`.  The unitary witness choice has disappeared: for fixed `r0`, the candidate is determined by the single moving integer `s`, subject to the retained gcd, size and physical completion conditions.

If instead `v=B^o(1)`, the symmetric statement holds with the root sides interchanged.  Freeze the finite side label and define the exact endpoint completion Boolean

```text
C_end(s) in {0,1}.
```

The endpoint branch is therefore a one-dimensional support problem

```text
#{s : gcd(r0,s)=1,
      s in the transported physical interval,
      C_end(s)=1}.
```

Merged s7-94 proved that such inner-ratio endpoint configurations cannot be discarded by geometry alone, so this is a genuine retained arithmetic receiver.

```text
FIXED_E_SUBPOLYNOMIAL_PRIMITIVE_FACTOR_FREEZABLE=Bo1
FIXED_E_ENDPOINT_UNITARY_CHOICE_EXHAUSTED=true
FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true
FIXED_E_ENDPOINT_GEOMETRY_ALONE_CLOSES_BRANCH=false
```

## 4. Two-sided polynomial branch retains a genuine unitary partition event

On branch (B), both primitive factors have positive polynomial scale.  Neither side can be frozen at `B^o(1)` cost.  For fixed outer `m`, admissibility asks for a prime-power partition

```text
m=u*v,
gcd(u,v)=1
```

whose ratio lies in the physical short window and whose canonical/reverse completion predicate holds.

The fixed-`m` witness multiplicity is still only `B^o(1)`, but the event

```text
there exists a two-sided polynomial unitary partition with physical completion
```

is not shown to have fixed-power deficit.  This is the genuinely balanced/two-sided unitary-existence receiver.

```text
FIXED_E_TWO_SIDED_POLYNOMIAL_UNITARY_PARTITION_RETAINS=true
FIXED_E_TWO_SIDED_PHYSICAL_EXISTENCE_AUTOMATIC=false
Q14_FORD_BOUNDED_DISTORTION_TRANSFER_PROVED=false
```

## 5. Material receiver change

Combining s7-100 with the present split, the s heavy packet now has the following explicit realizations:

```text
1. FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalPhysicalCompletionSupport;
2. FixedComplementaryDilationTwoSidedPolynomialShortUnitaryPartitionPhysicalExistenceSupport;
3. PolynomialComplementaryDilationFixedPrimitiveProductOneDimensionalPhysicalCompletionSupport;
4. PolynomialComplementaryDilationPolynomialPrimitiveProductOuterPairPhysicalUnitaryExistenceSupport.
```

This is a material receiver change: the former opaque canonical/reverse outer support has been separated into two one-dimensional completion-support mechanisms and two genuinely unitary-existence mechanisms.

No new sH is opened.  The one-dimensional completion Booleans still need internal arithmetic opening before a theorem target is stable, while the two-sided/polynomial-pair branches still lack a physical-measure-preserving transfer to an unrestricted divisor theorem.  Work-buX33's normal revisit condition explicitly included `s7-101`; the integrated Work route should be revisited after this batch merges.

```text
CURRENT_S_HEAVY_RECEIVER=FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPolynomialShortUnitaryPartitionPhysicalExistenceSupport_OR_PolynomialComplementaryDilationFixedPrimitiveProductOneDimensionalPhysicalCompletionSupport_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductOuterPairPhysicalUnitaryExistenceSupport
RECEIVER_MATERIALLY_CHANGED=true
S7_101_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
WORK_BUX33_REVISIT_TRIGGER_S7_101_REACHED=true
```

## Boundary

```text
STAGE14_S7_101=COMPLETE_FIXED_E_OUTER_EXISTENCE_SUPPORT_TO_PRIMITIVE_ENDPOINT_OR_TWO_SIDED_UNITARY_PARTITION_RECEIVERS
FIXED_E_ENDPOINT_ONE_DIMENSIONAL_SUPPORT=true
FIXED_E_TWO_SIDED_POLYNOMIAL_UNITARY_PARTITION_RETAINS=true
WORK_BUX33_REVISIT_TRIGGER_S7_101_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_101_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-102
```
