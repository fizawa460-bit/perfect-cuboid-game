# Stage14-t129 — exact endpoint-headroom logarithmic wedge and charged principal-mass no-go

## Status

`COMPLETE_ENDPOINT_HEADROOM_LOG_WEDGE_AND_GEOMETRIC_THINNESS_NOGO`

Consumes merged `Stage14-t128`, merged `Stage14-t126/t127`, and merged `Stage14-Work-brX30` from latest merged main.

Keep the fixed-`U` packet and the exact hyperbola coordinates

```text
X_U=2B/(h*k0),
L_B=2*sqrt(B),
N_max=X_U/L_B=sqrt(B)/(h*k0),
N(gamma)*ell<=X_U,
ell>L_B.
```

For one fixed small constant `theta>0`, t128 defines the endpoint-headroom cofactor layer by

```text
1<R(n)<B^theta,
R(n)=N_max/n.
```

Equivalently

```text
N_max*B^(-theta)<n<N_max.
```

Let `Omega_edge(theta)` be the corresponding charged nonboundary physical cofactor family.

## 1. Exact transposed endpoint layer

For `gamma in Omega_edge(theta)` the accepted prime labels satisfy

```text
L_B<ell<=X_U/n=L_B*R(n)<L_B*B^theta.
```

Hence the endpoint principal mass is exactly

```text
M_edge(theta)
 = 1/|G(d)|
   * sum_{L_B<ell<L_B*B^theta}
       F_edge(X_U/ell),
```

where

```text
F_edge(y)
 := #{gamma in Omega_edge(theta): N(gamma)<=y}.
```

All primitive, exceptional, canonical and nonboundary masks remain inside `Omega_edge(theta)`; no replacement by an unweighted scalar norm count is made.

## 2. Logarithmic wedge coordinates

Write formally

```text
ell=L_B*B^u,
n=N_max*B^(-v).
```

On a contributing endpoint pair, the conditions become exactly

```text
0<u,
0<v<theta,
u<=v.
```

Thus the endpoint branch is the triangular reciprocal-hyperbola corner

```text
0<u<=v<theta.
```

The diagonal `u=v` is the hyperbola boundary `n*ell=X_U`; `u=0` is the prime endpoint `ell=L_B`; and `v=theta` is the chosen headroom cut.

This is the exact endpoint/interior decomposition requested by the fixed-U side of merged Work-brX30.

## 3. Why fixed `theta` gives no deterministic power loss

The wedge is narrow in logarithmic coordinates but is not power-small merely from geometry.

For every fixed `theta>0`, its scalar cofactor projection is

```text
N_max*B^(-theta)<n<N_max,
```

whose upper scale remains `B^(1/2+o(1))/(h*k0)`. Its prime projection is

```text
L_B<ell<L_B*B^theta,
```

whose upper scale is `B^(1/2+theta+o(1))`.

Neither projection has a charged fixed-power density deficit under the merged hypotheses. In particular:

- split-prime support is only logarithmically sparse at fixed-power scale;
- exact cofactor fibers are `B^o(1)` but the scalar norm support is polynomial;
- principal mass may concentrate arbitrarily near the hyperbola corner at theorem level;
- Work-brX30 proves no measure-preserving adapter from this prime-weighted wedge to the global/s divisor-window measure.

Therefore endpoint geometry alone cannot close branch (A) of t128.

```text
ENDPOINT_HEADROOM_LAYER_TRANSPOSED_EXACTLY=true
ENDPOINT_LOG_WEDGE_EXACT=true
ENDPOINT_LOG_WEDGE_REGION=0<u<=v<theta
ENDPOINT_COFACTOR_PROJECTION_POWER_SMALL=false
ENDPOINT_PRIME_PROJECTION_POWER_SMALL=false
ENDPOINT_GEOMETRY_ALONE_FIXED_POWER_SAVING=false
GLOBAL_S_ENDPOINT_MEASURE_ADAPTER_AVAILABLE=false
```

## 4. Receiver status and next step

The endpoint branch is sharpened from a generic short-prime-interval label to the charged corner-wedge mass problem

```text
EndpointReciprocalHyperbolaCornerWedgeProjectivePrimeDepletion.
```

This is an exact refinement of branch (A), not yet a material change of the full three-branch fixed-U receiver. The next internal priority is branch (B): determine whether real/order-two projective characters actually retain generic Gaussian orientation dependence.

No new tH is justified. `tH29` already audited the endpoint and long-headroom theorem boundary; t129 introduces no new theorem-ready coefficient.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH30_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointCornerWedgeProjectivePrimeDepletionOrLongHeadroomRealProjectiveHeckeBiasOrLongHeadroomNonrealProjectiveCofactorBilinearCorrelation
NEXT_INTERNAL_TARGET=RealProjectiveCharacterGenericOrientationBlindnessAudit
NEXT=Stage14-t130
