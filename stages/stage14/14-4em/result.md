# Stage14-4em — determinant-scale stratification on the genuine-mover subbranch

## Status

`COMPLETE_GENUINE_MOVER_DETERMINANT_QUOTIENT_SCALE_STRATIFICATION`

Consumes corrected batch-local `Stage14-4el`, merged `Stage14-s7-75..77`, and merged `Stage14-4ek`. This stage acts only on

```text
ConcentratedExactCommonCoreGenuineProjectiveDeterminantMoverEnergy.
```

The parallel heavy-ray receiver from merged s7-77 remains unchanged.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
HEAVY_RAY_BRANCH_UNCHANGED=true
```

## 1. Freeze one archimedean mover-vector cell

Freeze one `B^o(1)` dyadic/range cell

```text
|X_j| ~ R,
|Y_j| ~ S,
j=1,2.
```

Every genuine mover pair satisfies

```text
Delta = X1*Y2-X2*Y1 != 0,
C | Delta.
```

Write uniquely

```text
Delta=qC,
q in Z\{0}.
```

The dyadic bounds give

```text
|Delta| <= O(RS),
|q| <= B^o(1) RS/C.
```

```text
NONZERO_DETERMINANT_QUOTIENT_Q_DEFINED=true
DETERMINANT_QUOTIENT_RANGE_BOUND=RS_over_C_times_Bo1
```

## 2. Super-determinant modulus range is empty for movers

If

```text
C > RS B^o(1),
```

then eventually `0<|Delta|<C`, contradicting `C|Delta`. Thus every saturating genuine-mover cell satisfies

```text
C <= RS B^o(1).
```

```text
SUPER_DETERMINANT_MODULUS_MOVER_BRANCH_EMPTY=true
GENUINE_MOVER_SATURATION_REQUIRES_C_AT_MOST_DETERMINANT_SCALE=true
```

## 3. Near-maximal versus polynomial quotient range

Two mover regimes remain.

### Near-maximal mover modulus

```text
RS/C=B^o(1)
```

gives

```text
|q|=B^o(1),
```

so one nonzero `q` may be frozen at subpolynomial cost.

```text
NEAR_MAXIMAL_MOVER_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true
```

### Polynomially separated mover modulus

For some fixed `eta>0`,

```text
RS/C >= B^(eta+o(1)),
```

and `q` has a genuinely polynomial admissible range; it cannot be frozen at `B^o(1)` cost.

```text
SEPARATED_MOVER_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true
```

Thus the genuine-mover receiver splits into

```text
A. NearMaximalCommonCoreFixedQuotientDeterminantMoverIncidence
or
B. PolynomialDeterminantQuotientFixedCommonCoreProjectiveMoverEnergy.
```

The heavy-ray branch is not touched by this split.

## Boundary

```text
STAGE14_4EM=COMPLETE_GENUINE_MOVER_DETERMINANT_QUOTIENT_SCALE_STRATIFICATION
NONZERO_DETERMINANT_QUOTIENT_Q_DEFINED=true
SUPER_DETERMINANT_MODULUS_MOVER_BRANCH_EMPTY=true
GENUINE_MOVER_SATURATION_REQUIRES_C_AT_MOST_DETERMINANT_SCALE=true
NEAR_MAXIMAL_MOVER_MODULUS_HAS_SUBPOLYNOMIAL_Q_DICTIONARY=true
SEPARATED_MOVER_MODULUS_HAS_POLYNOMIAL_Q_RANGE=true
HEAVY_RAY_BRANCH_UNCHANGED=true
FRESH_FIXED_POWER_SAVING_PROVED=false
NEW_RECIPROCAL_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4en
```
