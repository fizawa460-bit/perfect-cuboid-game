# Stage14-t143 — consume tH32 and discharge the Kai/Mitsui near-full safe endpoint

## Status

`COMPLETE_TH32_NEAR_FULL_SAFE_ENDPOINT_DISCHARGE_AND_INTERMEDIATE_SHORT_RANGE_LOCALIZATION`

Consumes completed independent `Stage14-tH32`, merged `Stage14-t140..t142`, completed positive `Stage14-tH31`, and merged `Stage14-Work-bwX35`.

The entering fixed-U receiver is

```text
(A) SafeMitsuiModulusQuarterScaleEndpointFixedGaussianResiduePrimeOccupancy
OR
(B) QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias
OR
(C) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

## 1. tH32 gives a partial positive theorem range on branch A

Put

```text
x=L_B=2*sqrt(B).
```

Completed tH32 certifies that Kai/Mitsui with the possible Siegel secondary term retained gives a fixed-residue lower occupancy once the endpoint width satisfies

```text
H >= H_Kai(B),
H_Kai(B)
 := B^(1/2)*exp(-c_short*sqrt(log B))
 = B^(1/2-o(1)),
```

for a sufficiently small fixed `c_short>0` compatible with the already-fixed safe modulus constant.

On that range

```text
T_safe,nearfull >= B^(-o(1)) M_safe,nearfull.
```

Therefore no fixed-power depletion can occur there.

```text
TH32_CONSUMED=true
SAFE_NEAR_FULL_ENDPOINT_BRANCH_DISCHARGED=true
SAFE_NEAR_FULL_ENDPOINT_FIXED_POWER_DEPLETION_POSSIBLE=false
```

## 2. Quarter scale itself is not covered

Stage14-t141 already discharged every fixed-power subquarter width by absolute capacity. The only safe-modulus endpoint widths that can still matter now lie between that capacity threshold and the Kai/Mitsui subtraction threshold:

```text
B^(1/4-o(1)) <= H < H_Kai(B).
```

This is a genuine short-interval zone. It includes every fixed exponent

```text
1/4 <= lambda < 1/2
```

at theorem level.

Stucky's conductor-one Gaussian-sector theorem provides a useful benchmark at

```text
H >= B^(7/20+epsilon),
```

but tH32 correctly does not import it into the exact target because it does not retain the growing ordinary residue modulo `d`.

Thus the safe-modulus endpoint obstruction is strictly narrower than at t142 but remains live.

```text
SAFE_ENDPOINT_SUBQUARTER_ALREADY_DISCHARGED=true
SAFE_ENDPOINT_KAI_NEARFULL_ALREADY_DISCHARGED=true
SAFE_ENDPOINT_INTERMEDIATE_SHORT_RANGE_LIVE=true
SAFE_ENDPOINT_INTERMEDIATE_SHORT_RANGE=B^(1/4-o(1))_TO_B^(1/2)*exp(-c*sqrt(logB))
```

## 3. Beyond-Mitsui branches are unchanged

The tH32 target intentionally freezes

```text
d <= exp(c_safe*sqrt(log B)).
```

Hence it says nothing about the two large-subpolynomial modulus branches:

```text
(B) quarter-scale endpoint with
    exp(c_safe*sqrt(log B)) < d=B^o(1),

(C) long-headroom with the same beyond-Mitsui modulus range.
```

They remain unchanged and still require internal provenance/capacity analysis before another theorem audit.

## 4. New minimal receiver

The safe endpoint is no longer the full quarter-scale-to-endpoint branch. Its near-full part is closed. The exact surviving fixed-U obstruction is now

```text
(A') SafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancy
     with
     B^(1/4-o(1)) <= H
       < B^(1/2)*exp(-c_short*sqrt(log B))

OR

(B) QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias

OR

(C) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This is a material receiver change. Under the shared batch contract the batch stops here even though only two substantive work units (`tH32`, `t143`) were needed.

The next internal task should inspect the provenance of the selector divisor `d` on the two beyond-Mitsui branches and determine whether the condition

```text
exp(c_safe*sqrt(log B)) < d=B^o(1)
```

itself forces a charged absolute-capacity loss from the original fixed-U packet structure. No new tH should be opened before that internal audit.

```text
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
PREFERRED_RECEIVER=SharedUSafeMitsuiModulusIntermediateShortEndpointFixedGaussianResiduePrimeOccupancyOrQuarterEndpointBeyondMitsuiModulusBiasOrLongHeadroomBeyondMitsuiModulusBias
NEXT_INTERNAL_TARGET=BeyondMitsuiSelectorDivisorProvenanceAndAbsoluteModulusCapacityAudit
NEXT=Stage14-t144
```
