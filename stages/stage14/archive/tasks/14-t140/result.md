# Stage14-t140 — endpoint additive prime width and explicit cofactor-annulus principal capacity

## Status

`COMPLETE_ENDPOINT_ADDITIVE_WIDTH_COFACTOR_ANNULUS_CAPACITY`

Consumes merged `Stage14-t139`, positive `Stage14-tH31`, and merged `Stage14-Work-bvX34` on latest main.

Fix the explicit fixed-residue endpoint branch from t135/t139. Put

```text
L_B=2*sqrt(B),
N_0=sqrt(B)/(h*k0),
n=N(z)<N_0,
y_z=X_U/n=2B/(h*k0*n).
```

Define the additive prime width

```text
H(z):=y_z-L_B>0.
```

Since `y_z=L_B*N_0/n`, writing `s=N_0-n` gives the exact identities

```text
H(z)=2*sqrt(B)*s/n,
s=H(z)*N_0/(2*sqrt(B)+H(z))
 = H(z)/(h*k0*(2+H(z)/sqrt(B))).
```

Thus endpoint-short prime width and distance of the cofactor norm from its top endpoint are the same scalar variable. In particular, for `H(z)<=sqrt(B)`,

```text
H(z)/(3*h*k0) <= N_0-N(z) <= H(z)/(2*h*k0).
```

No asymptotic theorem is used.

## Dyadic additive-width layer

For `Y>=1`, let

```text
Z(Y):={z: Y<H(z)<=2Y}.
```

On `Y<=sqrt(B)`, the exact relation above places every scalar norm `n=N(z)` in an interval of length

```text
O(Y/(h*k0)+1).
```

For each integer norm, the primitive Gaussian representation fiber, after the already frozen sector/residue/local labels, has size at most `B^o(1)`. Hence

```text
#Z(Y) <= B^o(1)*(Y/(h*k0)+1).
```

For each `z in Z(Y)`, the unrestricted canonical split-prime interval has additive length at most `2Y`, so trivially

```text
|P_z| <= O(Y+1).
```

The ordinary-residue principal baseline on this layer is

```text
M_Y = 1/|(Z[i]/dZ[i])^x| * sum_{z in Z(Y)} |P_z|.
```

Since the residue denominator is at least one,

```text
M_Y <= B^o(1)*(Y/(h*k0)+1)*(Y+1)
    <= B^o(1)*(Y+1)^2.
```

Therefore a dyadic endpoint layer of additive width `Y=B^(lambda+o(1))` has the unconditional capacity bound

```text
M_Y <= B^(2*lambda+o(1)).
```

This is a charged principal-mass capacity bound; it does not assume prime equidistribution in the selected residue.

For `0<H<=1`, the same argument gives only `B^o(1)` principal capacity, which is already exponent-zero.

```text
ENDPOINT_ADDITIVE_WIDTH_DEFINED=true
ENDPOINT_COFACTOR_TOP_ANNULUS_IDENTITY_EXACT=true
ENDPOINT_WIDTH_LAYER_COFACTOR_COUNT_LE_BO1_TIMES_Y=true
ENDPOINT_WIDTH_LAYER_PRINCIPAL_CAPACITY_LE_B_POW_2LAMBDA=true
PRIME_DISTRIBUTION_USED_FOR_CAPACITY=false
```

The beyond-Mitsui long-headroom branch from t139 is unchanged.

This stage opens the endpoint geometry/capacity but does not yet localize a bad principal-scale sequence to one width exponent, so it is not declared a material receiver change.

```text
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH32_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointAdditiveWidthCapacityAgainstFixedGaussianResiduePrimeOccupancyOrLongHeadroomBeyondMitsuiModulusBias
NEXT_INTERNAL_TARGET=EndpointDyadicPrincipalMassLocalizationAndQuarterWidthFloor
NEXT=Stage14-t141
