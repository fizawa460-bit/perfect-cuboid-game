# Stage14-4em — determinant-scale stratification of genuine projective collisions

## Status

`COMPLETE_NONZERO_PROJECTIVE_COLLISION_DETERMINANT_QUOTIENT_SCALE_STRATIFICATION`

Consumes batch-local `Stage14-4el` and merged `Stage14-4ek`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze one archimedean vector cell

The reciprocal candidate coordinates already live in a `B^o(1)` dyadic/range dictionary. Freeze one cell

```text
|X_j| ~ R,
|Y_j| ~ S,
j=1,2,
```

with the frozen signs/units retained. This costs only `B^o(1)`.

For every genuine collision from 4el,

```text
Delta = X1*Y2-X2*Y1 != 0,
C | Delta.
```

Write uniquely

```text
Delta = q C,
q in Z\{0}.
```

The dyadic bounds give

```text
|Delta| <= O(RS),
|q| <= B^o(1) * RS/C.
```

```text
NONZERO_DETERMINANT_QUOTIENT_Q_DEFINED=true
DETERMINANT_QUOTIENT_RANGE_BOUND=RS_over_C_times_Bo1
```

## 2. Super-determinant modulus range is impossible

If on a fixed exponent cell

```text
C > RS * B^o(1),
```

then `0<|Delta|<C` for all sufficiently large `B`, contradicting `C|Delta`.

Hence every saturating concentrated collision cell must satisfy

```text
C <= RS * B^o(1).
```

```text
SUPER_DETERMINANT_MODULUS_COLLISION_BRANCH_EMPTY=true
CONCENTRATED_SATURATION_REQUIRES_C_AT_MOST_DETERMINANT_SCALE=true
```

This is a genuine range exclusion, but by itself it does not change the whole-family exponent because the surviving cells may still have full polynomial mass.

## 3. Near-maximal versus separated determinant scale

There are two remaining exponent regimes.

### Near-maximal modulus

```text
RS/C = B^o(1).
```

Then

```text
|q| = B^o(1),
```

so one nonzero integer quotient `q` may be frozen with only `B^o(1)` loss.

```text
NEAR_MAXIMAL_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true
```

### Polynomially separated modulus

For some fixed `eta>0`,

```text
RS/C >= B^(eta+o(1)).
```

Then the determinant quotient has a genuinely polynomial admissible range. It cannot be frozen by a subpolynomial pigeonhole.

```text
SEPARATED_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true
```

Thus the genuine concentrated collision receiver splits into

```text
A. NearMaximalCommonCoreFixedQuotientDeterminantIncidence
or
B. PolynomialDeterminantQuotientFixedCommonCoreProjectiveCollisionEnergy.
```

## Boundary

```text
STAGE14_4EM=COMPLETE_NONZERO_PROJECTIVE_COLLISION_DETERMINANT_QUOTIENT_SCALE_STRATIFICATION
NONZERO_DETERMINANT_QUOTIENT_Q_DEFINED=true
SUPER_DETERMINANT_MODULUS_COLLISION_BRANCH_EMPTY=true
CONCENTRATED_SATURATION_REQUIRES_C_AT_MOST_DETERMINANT_SCALE=true
NEAR_MAXIMAL_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true
SEPARATED_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true
FRESH_FIXED_POWER_SAVING_PROVED=false
NEW_RECIPROCAL_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4en
```
