# Stage14-main-batch report — 4fe through 4fg

## Boundary

```text
STAGE14_MAIN_BATCH=COMPLETE
BATCH_START_MAIN_SHA=c5c84d2727caad0afdc08dec69f6696716f21b38
BATCH_PUBLICATION_MAIN_SHA=c5c84d2727caad0afdc08dec69f6696716f21b38
BATCH_FIRST_STAGE=Stage14-4fe
BATCH_LAST_STAGE=Stage14-4fg
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_MAIN_RECEIVER=FixedPrimitiveRayFixedAgreementPairNormalizedRadialSquareclassDivisorWindowPhysicalOccupancyWithMassExponentMuAtMostOneQuarterMinusPhi_OR_CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fh
```

## Result

This batch follows merged `Stage14-4fd` from latest merged main and consumes merged `Stage14-s7-86` plus merged `Stage14-Work-bqX29` on the identical global heavy-ray packet.

### 4fe — denominator peel and factorization no-go

The exact root/radial identity

```text
d0*J*a*b=c0*h,
gcd(c0,d0)=1
```

forces `d0|h`. If `d0=B^(delta+o(1))` and `rho=1/4-phi`, then

```text
|H_*| <= B^(rho-delta+o(1)).
```

A surviving heavy ray of mass exponent `mu` therefore requires

```text
delta<=rho-mu.
```

After writing `h=d0*n`, the bare equation is `Jab=c0*n`. The algebra itself is support-dense: `(J,a,b)=(1,1,c0*n)` is a valid squareclass-factorization tuple for every `n` before the remaining physical root windows are imposed. Hence no second power saving may be charged from the factorization equality itself.

### 4ff — mass transfers to normalized radial support

Define

```text
N_*={n:d0*n in H_*}.
```

Then exactly `|N_*|=|H_*|`, and

```text
B^(mu-o(1)) <= |N_*| <= B^(rho-delta+o(1)).
```

For fixed `n`, both the root-factor tuple count and the full physical reverse fiber are `B^o(1)`. Heavy mass is therefore genuinely carried by polynomially many distinct normalized integers, not anomalously large atomic weights.

### 4fg — one squareclass divisor coordinate controls both root factors

With fixed `A*B=K_Z`, set

```text
L=J*a^2.
```

Then exactly

```text
|Xr|=A*L,
|Yr|=B*c0^2*n^2/L,
```

while admissibility is

```text
sqrt(sqf(L)*L) | c0*n,
gcd(sqf(L),K_Z)=1,
```

plus the transported physical masks. The two root size conditions become reciprocal windows for the same `L`.

Thus normalized radial acceptance is precisely

```text
A_rad(n)=1
<=>
there exists an admissible squareclass divisor L
in the intersection of the two physical reciprocal L-windows.
```

This is a material receiver change. The next internal step is to freeze the exact dyadic geometry of those two windows and determine whether their intersection is a genuinely short divisor interval, an ordinary balanced divisor window, or can remain dense on a saturating packet.

## Other branches and H boundary

The existing low-C three-divisor, genuine-mover and diffuse complementary-Gaussian-factor H gates are unchanged. They are not consumed or cross-promoted here. The heavy branch itself still has an internal successor, so no new integrated main-line H unit is opened and the whole mainline is not blocked waiting for H.

```text
NEW_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## Publication recheck

Latest merged main remained

```text
c5c84d2727caad0afdc08dec69f6696716f21b38
```

through publication recheck. No unmerged concurrent route result is used as a theorem source.
