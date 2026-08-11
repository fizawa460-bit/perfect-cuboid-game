# Stage14-4es — fixed-power overlap between the two diffuse norm factors is strictly sub-square-root

## Status

`COMPLETE_DIFFUSE_COMMON_CORE_QUOTIENT_GCD_SQUARE_DIVISOR_SAVING`

Consumes batch-local `Stage14-4er`, merged `Stage14-4ep`, and the charged-once primitive norm projection.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering two-polynomial-factor packet

Stage14-4er gives

```text
N=C*m=B^(1/2+o(1)),
C=B^(kappa+o(1)),
1/6<=kappa<=1/4,
m=B^(1/2-kappa+o(1)).
```

The full physical candidate projects to `N` with `B^o(1)` fiber by merged 4ep.

Define

```text
G:=gcd(C,m),
G=B^(gamma+o(1)).
```

Then exactly

```text
G^2 | N.
```

## 2. Count one fixed-power overlap stratum through the norm value

Fix a dyadic `G`-stratum with `gamma>0`.  The number of possible integers

```text
G~B^gamma
```

is at most `B^(gamma+o(1))`.

For each such `G`, write

```text
N=G^2 n.
```

Since `N=B^(1/2+o(1))`, the quotient satisfies

```text
n<=B^(1/2-2gamma+o(1)).
```

Therefore the total number of possible norm values on this stratum is bounded by

```text
B^(gamma+o(1)) * B^(1/2-2gamma+o(1))
 = B^(1/2-gamma+o(1)).
```

For fixed `N`, the possible factor pairs `(C,m)` with `Cm=N` are divisor-many, and the physical reverse fiber over `N` is `B^o(1)`.  Hence the complete physical count on the fixed-`gamma` overlap stratum satisfies

```text
V_G(B) << B^(1/2-gamma+o(1)).
```

```text
FIXED_POWER_COMMON_CORE_QUOTIENT_OVERLAP_SAVING=gamma
```

This count charges the derived overlap `G` once and does not reuse Gaussian root-line spacing or divisor density.

## 3. Consequence for square-root saturation

Every fixed `gamma>0` is strictly sub-square-root.  Thus any diffuse branch capable of saturating the global `1/2` envelope must satisfy

```text
G=B^o(1).
```

After the standard finite 2-primary/endpoint peel, the two polynomial factors are coprime at fixed-power scale:

```text
gcd(C,m)=B^o(1).
```

```text
DIFFUSE_SATURATION_REQUIRES_CORE_QUOTIENT_GCD=Bo1
FIXED_POWER_CORE_QUOTIENT_OVERLAP_BRANCH_CLOSED=true
```

## 4. Updated diffuse receiver

The live diffuse packet now has

```text
N=C*m=X0^2+Y0^2,
gcd(X0,Y0)=1,
N=B^(1/2+o(1)),
C=B^(kappa+o(1)),
1/6<=kappa<=1/4,
m=B^(1/2-kappa+o(1)),
gcd(C,m)=B^o(1).
```

The remaining issue is no longer repeated rational prime support between `C` and `m`; it is the correlated allocation of two essentially coprime polynomial Gaussian norm factors inside one primitive norm value.

Call this receiver

```text
DiffuseCoprimeTwoPolynomialFactorCanonicalAllocationPrimitiveGaussianNormCorrelation.
```

## Boundary

```text
STAGE14_4ES=COMPLETE_DIFFUSE_COMMON_CORE_QUOTIENT_GCD_SQUARE_DIVISOR_SAVING
FIXED_POWER_COMMON_CORE_QUOTIENT_OVERLAP_SAVING=gamma
DIFFUSE_SATURATION_REQUIRES_CORE_QUOTIENT_GCD=Bo1
FIXED_POWER_CORE_QUOTIENT_OVERLAP_BRANCH_CLOSED=true
CURRENT_DIFFUSE_RECEIVER=DiffuseCoprimeTwoPolynomialFactorCanonicalAllocationPrimitiveGaussianNormCorrelation
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=true
NEXT=Stage14-4et
```
