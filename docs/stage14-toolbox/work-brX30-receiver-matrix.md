# Stage14-Work-brX30 receiver / supersession matrix

| Route | Merged input | Exact current coordinate | Polynomial obstruction | H status |
|---|---|---|---|---|
| main heavy | `4fg` | normalized radial `n` plus admissible squareclass divisor `L`; `|Xr|=A L`, `|Yr|=B c0^2 n^2/L` | physical reciprocal divisor-window occupancy across polynomially many `n` | internal `4fh`; no new heavy H |
| s heavy | `s7-89` | `n=J1 a1 b1`, `L_s=J1 a1^2`; `|Xr|=alpha L_s`, `|Yr|=beta n^2/L_s` | same reciprocal divisor-window occupancy after fixed coefficient peel | internal `s7-90`; no new sH |
| fixed-U | `t128` + `tH29` | `N(gamma) ell<=X_U`, selected projective class, exact headroom `R(N(gamma))` | endpoint prime depletion OR long-headroom real Hecke bias OR long-headroom nonreal physical cofactor bilinear correlation | `tH29` consumed negative; `tH30` premature |

## Proven identifications

```text
GLOBAL_S_RECIPROCAL_DIVISOR_WINDOW_COORDINATE_IDENTIFIED=true
GLOBAL_S_RECIPROCAL_COORDINATE_FINITE_FIBER_EQUIVALENT=true
COMMON_RECIPROCAL_WINDOW_GEOMETRY_LANGUAGE_PROVED=true
COMMON_RECIPROCAL_TWO_COORDINATE_MONOTONE_STRUCTURE_PROVED=true
```

The global and s descriptions are the same heavy-ray arithmetic after setting

```text
L_s=J1*a1^2,
n=J1*a1*b1,
n^2/L_s=J1*b1^2.
```

Fixed packet coefficients absorb the difference between `(A,B c0^2)` and `(alpha,beta)`.

## Non-identifications / double-charge locks

```text
GLOBAL_S_RECIPROCAL_COORDINATE_COUNTS_MULTIPLICABLE=false
COMMON_RECIPROCAL_WINDOW_ARITHMETIC_MEASURE_IDENTIFIED=false
COMMON_RECIPROCAL_WINDOW_QUANTIFIER_ORDER_IDENTIFIED=false
DIRECT_RADIAL_DIVISOR_TO_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ARITHMETIC_RECIPROCAL_WINDOW_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
TH29_CROSS_PROMOTABLE_TO_GLOBAL_DIVISOR_WINDOWS=false
```

Reasons:

- global/s uses an existential admissible squareclass divisor `L` at fixed `n`, with only `B^o(1)` candidates per `n`;
- fixed-U uses a weighted cofactor/prime sum on an inequality hyperbola and a selected projective class;
- the physical baselines, prime condition, projective character weights and quantifier order are not transported by any merged finite-fiber map.

## Receiver supersession

```text
bqX29 GLOBAL/S:
  PolynomialRadialOccupancy

brX30 GLOBAL/S:
  NormalizedRadialSquareclassDivisorWindowPhysicalOccupancy
```

The fixed-U receiver changes independently through merged t128:

```text
SelectedProjectiveClassNearTotalPrimeDepletion
  -> EndpointHeadroomProjectivePrimeDepletion
     OR LongHeadroomRealProjectiveHeckeCharacterPrincipalScaleBias
     OR LongHeadroomNonrealProjectiveCharacterPhysicalCofactorBilinearCorrelation
```

## Current theorem locks

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_NEEDED=false
NEXT_INTEGRATED_TARGET=ReciprocalWindowEndpointInteriorPhysicalWeightIntersectionOrNoGo
NEXT_REVISIT_CONDITION=4fj+s7-92+t131
```
