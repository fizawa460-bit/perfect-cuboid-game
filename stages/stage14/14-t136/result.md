# Stage14-t136 — consume tH30 and reduce fixed-U to endpoint or individual-modulus fixed-residue prime occupancy

## Status

`COMPLETE_TH30_ENDPOINT_VERSUS_INDIVIDUAL_SUBPOLYNOMIAL_MODULUS_REDUCTION`

Consumes completed independent `Stage14-tH30` and the exact fixed-residue hyperbola from Stage14-t135.

The t135/tH30 target is

```text
T
 = # {(z,pi_ell):
      z in one explicit primitive Gaussian sector/residue family,
      pi_ell in one fixed ordinary Gaussian residue beta_* mod d,
      ell>2*sqrt(B),
      N(z)*ell<=X_U},
```

against its ordinary-residue principal baseline `M`, with

```text
d=B^o(1).
```

tH30 proves that the previous opaque cofactor/Type-I--II obstruction is gone.  It leaves only prime-side endpoint and individual-modulus issues.

## 1. Exact endpoint/long-headroom split on the explicit cofactor set

For each live cofactor `z`, put

```text
R(z)
 := (X_U/N(z))/(2*sqrt(B))
 = sqrt(B)/(h*k0*N(z))
 >1.
```

Fix a small constant `theta>0` and split the explicit cofactor set into

```text
Z_edge(theta)={z: 1<R(z)<B^theta},
Z_long(theta)={z: R(z)>=B^theta}.
```

Let

```text
T=T_edge+T_long,
M=M_edge+M_long
```

be the corresponding nonnegative physical and principal ordinary-residue masses.

If for some fixed `delta>0`

```text
T<=B^(-delta)M,
```

then at least one nonzero branch satisfies the same fixed-power depletion at exponent level.  Thus every bad packet localizes to an endpoint branch or a long-headroom branch.

## 2. Endpoint branch

On `Z_edge(theta)` the prime interval is

```text
(2*sqrt(B), 2*sqrt(B)*R(z)]
```

with no lower bound on `R(z)-1`.  tH30 certifies that no audited unconditional theorem gives the required lower occupancy in one fixed Gaussian residue for every such moving interval.

The first live receiver is therefore

```text
EndpointShortFixedGaussianResiduePrimeOccupancyDeficit.
```

This is now a pure prime-side obstruction: the cofactor set itself is explicit.

## 3. Long-headroom branch

On `Z_long(theta)`, every interval has fixed-power multiplicative headroom.  The short-endpoint obstruction is absent, but tH30 still finds no theorem uniform for every allowed individual modulus

```text
d=B^o(1)
```

and one fixed ordinary Gaussian residue, because the hypotheses do not place `d` in a fixed/polylogarithmic conductor range and do not uniformly exclude real exceptional-character bias.

The second live receiver is therefore

```text
LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This label intentionally contains both the modulus-uniformity and possible exceptional-real-character mechanisms.  They should not be split again by Fourier cofactor characters: t132--t135 have removed that cofactor-side distinction.

## 4. New minimal fixed-U receiver

The t128 three-way receiver and the t132 arbitrary scalar-weight receiver are superseded.  After tH30 the minimal fixed-U obstruction is exactly

```text
(A) EndpointShortFixedGaussianResiduePrimeOccupancyDeficit
OR
(B) LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

The old physical-cofactor Type-I/II adapter is no longer live.

This is a material receiver change.  The next internal task is to open the actual scale/conductor structure of `d` on the long branch and determine whether a polylogarithmic safe range can be separated from the genuinely larger `B^o(1)` range before any further theorem audit.

No new tH is opened here: tH30 explicitly recommends that internal modulus-scale split first.

```text
TH30_CONSUMED=true
TH29_COFACTOR_ADAPTER_OBSTRUCTION_REMOVED=true
FIXED_RESIDUE_ENDPOINT_LONG_SPLIT_EXACT=true
ENDPOINT_SHORT_FIXED_RESIDUE_BRANCH_LIVE=true
LONG_HEADROOM_INDIVIDUAL_SUBPOLYNOMIAL_MODULUS_BRANCH_LIVE=true
REAL_NONREAL_COFACTOR_SPLIT_REOPENED=false
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH31_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficitOrLongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias
NEXT_INTERNAL_TARGET=LongHeadroomProjectiveModulusScaleAndExceptionalCharacterStructureAudit
NEXT=Stage14-t137
```
