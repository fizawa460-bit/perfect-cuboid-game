# Stage14-t144 — beyond-Mitsui selector modulus provenance and fixed-U host coupling

## Status

`COMPLETE_BEYOND_MITSUI_SELECTOR_MODULUS_FIXED_U_HOST_COUPLING`

Consumes merged Stage14-t143, Stage14-t82/t84/t86/t125, Stage14-t65, and merged Stage14-Work-bxX36.

The entering fixed-U receiver is

```text
(A) SafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancy
OR
(B) QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias
OR
(C) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The purpose is to inspect the provenance of the modulus on (B),(C) before opening another theorem audit.

## 1. The selector modulus is hosted by fixed U

Write

```text
U=R+iS,
m=N(U)=R^2+S^2,
gcd(R,S)=1.
```

Merged t82 proves for every hard selector divisor

```text
d | D_Ubeta | |R*S|,
D_Ubeta <= m/2,
# {d for fixed U}=B^o(1).
```

Thus

```text
d <= m/2.
```

The surviving modulus is not an independent moving conductor family.  It is a divisor of a fixed coordinate product of the already-fixed U packet.

```text
SELECTOR_MODULUS_HOSTED_BY_FIXED_U=true
SELECTOR_MODULUS_DIVIDES_R_TIMES_S=true
SELECTOR_MODULUS_LE_M_OVER_2=true
SELECTOR_MODULUS_MULTIPLICITY_AT_FIXED_U=Bo1
```

## 2. Fixed packet scale hk0 is exactly proportional to m

Merged t65 gives

```text
h*k = epsilon*m.
```

The later 2-primary normalization writes

```text
k0=eta*k,
eta in {1,2}.
```

Hence exactly

```text
h*k0 = eta*epsilon*m.                              (2.1)
```

Therefore the prime hyperbola scale

```text
X_U=2B/(h*k0)
```

is equivalently

```text
X_U=2B/(eta*epsilon*m).
```

No independent polynomial entropy is hidden in `h*k0` once U and the O(1) eta branch are fixed.

```text
HK0_EQUALS_ETA_EPSILON_M=true
FIXED_U_HYPERBOLA_SCALE_DETERMINED_BY_M=true
```

## 3. Endpoint selector inequality reproduces the same host coupling

Merged t86 retains

```text
2*epsilon*eta*d*N(gamma) < sqrt(B).                (3.1)
```

For an endpoint cofactor put

```text
n=N(gamma),
L_B=2*sqrt(B),
H=X_U/n-L_B,
```

so exactly

```text
n=X_U/(L_B+H).
```

Substitute this into (3.1):

```text
d < sqrt(B)*(L_B+H)/(2*epsilon*eta*X_U)
  = h*k0/(2*epsilon*eta) * (1+H/(2*sqrt(B))).      (3.2)
```

Using (2.1),

```text
d < m/2 * (1+H/(2*sqrt(B))).                       (3.3)
```

On every endpoint width with `H=o(sqrt(B))` this is asymptotically the same fixed-U host bound already exposed by t82.  Thus the late reciprocal endpoint geometry is consistent with, and does not create, a new independent modulus scale.

```text
ENDPOINT_SELECTOR_HEIGHT_COUPLING_EXACT=true
ENDPOINT_SELECTOR_HOST_BOUND_CONSISTENT_WITH_T82=true
INDEPENDENT_BEYOND_MITSUI_MODULUS_ENTROPY=false
```

## 4. Consequence for beyond-Mitsui endpoint packets

On branch (B),

```text
d > exp(c_safe*sqrt(log B)).
```

Since `d<=m/2` and `h*k0=eta*epsilon*m`, necessarily

```text
m > 2*exp(c_safe*sqrt(log B)),
h*k0 > 2*eta*epsilon*exp(c_safe*sqrt(log B)).
```

Thus a beyond-Mitsui endpoint packet requires a simultaneously large fixed-U norm / hyperbola denominator scale.

This is only a subpolynomial lower bound.  It does not by itself yield a fixed positive B-power saving and therefore does not discharge branch (B).

```text
BEYOND_MITSUI_ENDPOINT_FORCES_LARGE_FIXED_U_NORM=true
BEYOND_MITSUI_ENDPOINT_FORCES_LARGE_HK0=true
HOST_LOWER_BOUND_ONLY_SUBPOLYNOMIAL=true
BEYOND_MITSUI_ENDPOINT_DISCHARGED=false
```

## 5. Long-headroom branch

For branch (C), the same fixed-U hosting

```text
d|D_Ubeta|R*S,
d<=m/2
```

remains exact.  However the endpoint substitution leading to a near-equality with `m/2` is unavailable because the cofactor may lie polynomially below the top norm.  No additional fixed-power capacity loss follows from provenance alone.

```text
BEYOND_MITSUI_LONG_MODULUS_FIXED_U_HOSTED=true
BEYOND_MITSUI_LONG_HOSTING_GIVES_FIXED_POWER_SAVING=false
```

## 6. Receiver decision and next step

This stage identifies the origin of both beyond-Mitsui moduli but does not yet change the minimal receiver: the host scale is only subpolynomial at the current boundary.

The next internal step is to keep the previously dropped host denominator in the endpoint annulus capacity estimate.  Because the endpoint cofactor norm annulus has thickness proportional to `H/(h*k0)`, branch (B) should receive an explicit `1/(h*k0)` capacity factor before deciding whether the width floor moves.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
NEXT_INTERNAL_TARGET=HostedEndpointAnnulusCapacityWithFixedUNormDenominator
NEXT=Stage14-t145
```
