# Stage14-4fh — exact reciprocal divisor-window geometry and radial product window

## Status

`COMPLETE_RECIPROCAL_DIVISOR_WINDOW_GEOMETRY_TO_RADIAL_PRODUCT_WINDOW`

Consumes merged `Stage14-4fg`, merged `Stage14-s7-89`, merged `Stage14-Work-brX30`, and latest merged main at batch start

```text
d519dcccee5bedb4844dbcee5cb4b5171600c0bf.
```

Only merged results are theorem sources.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Entering heavy reciprocal-window selector

Merged 4fg fixes one heavy primitive ray, one agreement packet, fixed positive squareclass coefficients

```text
A,
B0,
c0,
```

and writes every root-factor candidate over normalized radial integer `n` as

```text
|Xr| = A*L,
|Yr| = beta0*n^2/L,
beta0 := B0*c0^2,
```

where `L` obeys the exact squareclass-divisor admissibility

```text
sqrt(sqf(L)*L) | c0*n,
gcd(sqf(L),K_Z)=1,
```

plus the already transported primitive/canonical/reverse-completion masks.

Freeze one allowed physical root-size chart

```text
I_X=[X_-,X_+],
I_Y=[Y_-,Y_+],
0<X_-<=X_+,
0<Y_-<=Y_+.
```

Finite chart/end-point splitting is charged once and changes no fixed-power exponent.

## 2. Exact L-window intersection

The two physical size masks are equivalent to

```text
L in W_X := [X_-/A, X_+/A],
L in W_Y(n) := [beta0*n^2/Y_+, beta0*n^2/Y_-].
```

Hence the exact geometric L-window is

```text
W(n)
 := W_X intersect W_Y(n)
 = [
     max(X_-/A, beta0*n^2/Y_+),
     min(X_+/A, beta0*n^2/Y_-)
   ].
```

No arithmetic assumption has been used.

```text
EXACT_RECIPROCAL_L_WINDOW_INTERSECTION_PROVED=true
```

## 3. Nonempty intersection is exactly one radial product window

The intersection is nonempty iff both cross inequalities hold:

```text
X_-/A <= beta0*n^2/Y_-,
beta0*n^2/Y_+ <= X_+/A.
```

Equivalently

```text
N_-^2 <= n^2 <= N_+^2,
```

with

```text
N_-^2 := X_-*Y_-/(A*beta0),
N_+^2 := X_+*Y_+/(A*beta0).
```

Thus the geometric support is exactly

```text
N_geom=[N_-,N_+].
```

Moreover

```text
N_+/N_-
 = sqrt((X_+/X_-)*(Y_+/Y_-)).
```

The frozen physical chart has only constant/subpolynomial multiplicative width, so `N_geom` is one ordinary dyadic/subpolynomial radial cell. Its existence does not supply an independent fixed-power saving relative to the already charged normalized radial ambient support.

```text
RECIPROCAL_WINDOW_NONEMPTY_IFF_RADIAL_PRODUCT_WINDOW=true
PURE_WINDOW_GEOMETRY_GIVES_NEW_FIXED_POWER_SAVING=false
```

## 4. Logarithmic overlap profile

Put

```text
t=log n,
u=log L.
```

Then `W_X` is a fixed interval in `u`, while `W_Y(n)` translates with slope `2` in `t`. The logarithmic overlap length

```text
omega(n):=log(sup W(n)/inf W(n))
```

on `N_geom` is a continuous piecewise-linear function of `log n` which vanishes at the two radial endpoints and grows linearly away from an active endpoint until capped by the narrower root window.

This exact profile is the relevant endpoint/interior geometry. It does not itself count admissible squareclass divisors.

```text
LOG_OVERLAP_PROFILE_PIECEWISE_LINEAR=true
OVERLAP_VANISHES_ONLY_AT_RADIAL_PRODUCT_ENDPOINTS=true
DIVISOR_OCCUPANCY_NOT_REPLACED_BY_GEOMETRY=true
```

## 5. Receiver and H decision

The minimal heavy receiver remains the 4fg squareclass-divisor occupancy selector, now with its geometric support made exact. The next internal stage must compare the endpoint strips, where `omega(n)` is small, with the required heavy support exponent `mu`.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fi
```
