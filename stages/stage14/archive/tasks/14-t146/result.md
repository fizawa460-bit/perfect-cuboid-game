# Stage14-t146 — host-normalized endpoint width floor and sparse-near-full alternative

## Status

`COMPLETE_HOST_NORMALIZED_ENDPOINT_CAPACITY_DICHOTOMY_AND_RECEIVER_CHANGE`

Consumes Stage14-t144/t145 on this batch branch, merged Stage14-t143/tH32, and merged Stage14-Work-bxX36.

The entering endpoint receiver still contains the safe intermediate short interval and the beyond-Mitsui quarter-scale endpoint.  Stage14-t145 gives for a dyadic width layer

```text
Y=B^(lambda+o(1)),
h*k0=B^(rho+o(1)),
```

the exact exponent envelope

```text
M_Y
 <= B^(max(2*lambda-rho,lambda)+o(1)).              (1.1)
```

A whole-exponent-obstructing layer must be capable of carrying

```text
M_Y >= B^(1/2-o(1)).                               (1.2)
```

## 1. Exact principal-capacity dichotomy

Combining (1.1) and (1.2), at least one of the following is necessary:

```text
(A) lambda >= 1/2-o(1),
```

or

```text
(B) 2*lambda-rho >= 1/2-o(1).                     (1.3)
```

Branch (A) is the **sparse-cofactor near-full** alternative: even `O(B^o(1))` cofactors may carry principal-scale mass because each associated prime interval itself has width `B^(1/2-o(1))`.

Branch (B) is the **host-normalized many-cofactor** alternative.  It is equivalently

```text
lambda >= 1/4 + rho/2 - o(1),
```

or in scale form

```text
Y >= B^(1/4-o(1))*sqrt(h*k0).                      (1.4)
```

This is the correct refinement of the universal quarter floor from t141.

```text
ENDPOINT_PRINCIPAL_CAPACITY_DICHOTOMY_PROVED=true
SPARSE_COFACTOR_NEAR_FULL_ALTERNATIVE_DEFINED=true
HOST_NORMALIZED_MANY_COFACTOR_ALTERNATIVE_DEFINED=true
HOST_NORMALIZED_WIDTH_FLOOR=BsQuarterTimesSqrtHK0
```

## 2. Relation to positive tH32

Completed tH32 and merged t143 already discharge, on the safe modulus range,

```text
H >= H_Kai(B)
 := B^(1/2)*exp(-c_short*sqrt(log B)).
```

Therefore the safe-modulus sparse-near-full alternative can survive only in the sub-Kai strip

```text
B^(1/2-o(1)) <= H < H_Kai(B),                     (2.1)
```

where the first inequality is exponent notation rather than a new fixed constant threshold.

The safe host-normalized many-cofactor alternative survives only if

```text
B^(1/4-o(1))*sqrt(h*k0)
 <= H < H_Kai(B).                                  (2.2)
```

When `h*k0=B^rho` with fixed `rho>0`, (2.2) raises the lower fixed-power width exponent from `1/4` to `1/4+rho/2`.

```text
SAFE_NEAR_FULL_ABOVE_KAI_ALREADY_DISCHARGED=true
SAFE_SUB_KAI_NEAR_FULL_STRIP_REMAINS=true
SAFE_HOST_NORMALIZED_WIDTH_FLOOR_PROVED=true
```

## 3. Beyond-Mitsui endpoint receives a forced pseudopolynomial width gain

Stage14-t144 proves on every beyond-Mitsui endpoint packet

```text
h*k0 >= C*d,
d>exp(c_safe*sqrt(log B)).
```

Thus the many-cofactor width floor (1.4) implies

```text
H
 >= B^(1/4-o(1))*sqrt(d)
 >  B^(1/4-o(1))
    * exp((c_safe/2)*sqrt(log B)).                 (3.1)
```

up to fixed packet constants.

This improves the quarter-scale boundary by a genuine pseudopolynomial factor.  Because that factor is still `B^o(1)`, it does not create a fixed positive exponent saving.

The sparse-near-full alternative is also still possible for beyond-Mitsui moduli; tH32 does not apply there.

```text
BEYOND_MITSUI_ENDPOINT_PSEUDOPOLYNOMIAL_WIDTH_GAIN_PROVED=true
BEYOND_MITSUI_ENDPOINT_FIXED_POWER_WIDTH_GAIN_PROVED=false
BEYOND_MITSUI_SPARSE_NEAR_FULL_ALTERNATIVE_REMAINS=true
```

## 4. Long-headroom beyond-Mitsui branch is unchanged

The t145 endpoint annulus argument uses the top cofactor norm relation and does not discharge the long-headroom branch.  Its modulus remains fixed-U hosted, but no polynomial capacity loss has been proved there.

```text
LONG_HEADROOM_BEYOND_MITSUI_BRANCH_UNCHANGED=true
```

## 5. New minimal fixed-U receiver

The old endpoint labels treated every `H>=B^(1/4-o(1))` layer alike.  They are now superseded by the exact capacity dichotomy:

```text
(A) SafeMitsuiModulusSubKaiSparseNearFullFixedGaussianResiduePrimeOccupancy
OR
(B) SafeMitsuiModulusHostNormalizedIntermediateEndpointFixedGaussianResiduePrimeOccupancy
OR
(C) BeyondMitsuiHostedSelectorSparseNearFullFixedGaussianResiduePrimeOccupancyBias
OR
(D) BeyondMitsuiHostedSelectorHostNormalizedEndpointFixedGaussianResiduePrimeOccupancyBias
OR
(E) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

For (B),(D), the mandatory lower width is

```text
H >= B^(1/4-o(1))*sqrt(h*k0).
```

For (D), additionally `h*k0 >= C*d > exp(c_safe*sqrt(log B))`.

This is a material receiver change and reaches the `t146` normal Work-bxX36 revisit trigger.

No new tH is opened.  tH32 already audited the safe fixed-residue short-interval theorem boundary; the new information is internal host-capacity localization, not a materially new external theorem target.  The next useful step is to analyze the sparse-near-full alternative separately from the many-cofactor alternative and determine whether cumulative subtraction or exact cofactor multiplicity closes either sub-Kai strip.

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
PREFERRED_RECEIVER=SharedUSparseNearFullOrHostNormalizedEndpointOccupancyPlusBeyondMitsuiLongBias
NEXT_INTERNAL_TARGET=SparseNearFullCofactorMultiplicityVersusHostNormalizedEndpointPrimeOccupancy
NEXT=Stage14-t147
```
