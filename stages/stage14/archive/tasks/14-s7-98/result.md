# Stage14-s7-98 — polynomial complementary dilation to fixed-product outer occupancy or two-scale unitary correlation

## Status

`COMPLETE_POLYNOMIAL_E_PRIMITIVE_PRODUCT_SCALE_SPLIT_TO_OUTER_OCCUPANCY_OR_TWO_SCALE_UNITARY_CORRELATION`

Consumes batch-local `Stage14-s7-96/97`, merged `Stage14-4fm`, and merged `Stage14-Work-btX32`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Enter the polynomial-E branch

Merged 4fm and s7-96 leave

```text
n=E*m,
m=u*v,
gcd(u,v)=1,
u||m,
E=B^(epsilon+o(1)), epsilon>0,
```

with physical weight

```text
m_E(E) * m_cpl(E*m,u,m/u,E).
```

Freeze one exponent cell

```text
m=B^(kappa+o(1)),
nu=epsilon+kappa.
```

There are two possibilities:

```text
(P0) kappa=0: m=B^o(1),
(P1) kappa>0: m has polynomial scale.
```

This split costs only exponent-zero dyadic bookkeeping.

```text
POLYNOMIAL_E_PRIMITIVE_PRODUCT_SCALE_SPLIT_EXPLICIT=true
```

## 2. P0: subpolynomial primitive product freezes the whole inner selector

If `m=B^o(1)`, the number of exact values of `m` is `B^o(1)`. For fixed `m`, the number of unitary divisors `u||m` is also `B^o(1)`. Hence one surviving pair

```text
(m,u)=(m0,u0)
```

may be frozen at total `B^o(1)` cost.

Set

```text
v0=m0/u0,
r0=u0/v0=u0^2/m0.
```

The branch becomes a one-dimensional polynomial complementary-dilation occupancy

```text
I_P0
 = sum_E
     1_{r0 in R_int(E*m0)}
     m_E(E)
     m_cpl(E*m0,u0,v0,E).
```

Thus the unitary-divisor selector itself no longer carries polynomial entropy. All remaining polynomial mass lies in the outer complementary dilation `E` and its canonical/reverse completion predicate.

```text
SUBPOLYNOMIAL_M_EXACT_VALUE_FREEZABLE=Bo1
SUBPOLYNOMIAL_M_UNITARY_ORIENTATION_FREEZABLE=Bo1
P0_POLYNOMIAL_ENTROPY_ONLY_IN_E=true
```

This branch is not closed: the Boolean in `E` may still accept polynomially many values, and no merged theorem controls it.

## 3. P1: both E and the primitive product are polynomial

If `kappa>0`, neither `E` nor `m` can be frozen at exponent-zero cost. The exact incidence is

```text
I_P1
 = sum_E
   sum_m
   sum_{
      u||m,
      u^2/m in R_int(E*m)
   }
      m_E(E)
      m_cpl(E*m,u,m/u,E).
```

with

```text
E=B^(epsilon+o(1)), epsilon>0,
m=B^(kappa+o(1)), kappa>0.
```

The fixed-`m` unitary fiber remains `B^o(1)`, so any polynomial mass must come from polynomial support in the outer pair `(E,m)`. But the physical Boolean remains coupled to the chosen unitary orientation `u`, so one may not factor the count into an `E` density times an `m` divisor-window density.

```text
P1_BOTH_E_AND_M_POLYNOMIAL=true
P1_FIXED_M_UNITARY_FIBER=Bo1
P1_OUTER_PAIR_SUPPORT_MUST_BE_POLYNOMIAL=true
P1_E_M_WEIGHT_INDEPENDENCE_ASSUMED=false
```

## 4. Material receiver change

The polynomial-E receiver from merged 4fm has now separated into two genuinely different arithmetic mechanisms:

```text
(A) fixed/subpolynomial E:
    FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence;

(B0) polynomial E, subpolynomial primitive product:
    PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy;

(B1) polynomial E, polynomial primitive product:
    PolynomialComplementaryDilationPolynomialPrimitiveProductInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation.
```

The B0 branch has no polynomial inner selector left; B1 has a genuine two-scale outer correlation. This is a material receiver change.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new sH is frozen at this boundary.

- branch A still needs the exact dependence of `c_E0(m,u)` opened before any Ford/unitary theorem audit;
- branch B0 needs the resulting one-variable `E` Boolean opened internally;
- branch B1 needs an outer/inner weight factorization or a theorem-ready bilinear coefficient sequence before an external audit.

This is exactly the weight-factorization issue anticipated by merged Work-btX32. A new Work revisit is now justified when the companion mainline/fixed-U descendants reach their corresponding triggers.

```text
S7_98_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_98=COMPLETE_POLYNOMIAL_E_PRIMITIVE_PRODUCT_SCALE_SPLIT_TO_OUTER_OCCUPANCY_OR_TWO_SCALE_UNITARY_CORRELATION
POLYNOMIAL_E_PRIMITIVE_PRODUCT_SCALE_SPLIT_EXPLICIT=true
SUBPOLYNOMIAL_M_UNITARY_ORIENTATION_FREEZABLE=Bo1
P0_POLYNOMIAL_ENTROPY_ONLY_IN_E=true
P1_BOTH_E_AND_M_POLYNOMIAL=true
P1_OUTER_PAIR_SUPPORT_MUST_BE_POLYNOMIAL=true
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence_OR_PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_98_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-99
```