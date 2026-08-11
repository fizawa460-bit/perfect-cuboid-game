# Stage14-t142 — cross the quarter-width endpoint with the Mitsui modulus split and freeze the short-interval theorem target

## Status

`COMPLETE_ENDPOINT_WIDTH_MODULUS_CROSS_SPLIT_AND_TH32_FREEZE`

Consumes Stage14-t141 on this batch branch, merged t137--t139, positive tH31, and merged Work-bvX34.

A sequence capable of obstructing the whole `B^(1/2+o(1))` exponent has, after t141 dyadic localization,

```text
H(z) ~ Y=B^(lambda+o(1)),
lambda>=1/4-o(1),
```

on one principal-scale endpoint layer.

Independently, t137/t139 split the modulus at

```text
d_safe(B)=exp(c_safe*sqrt(log B)).
```

Cross these two exact conditions.

## 1. Safe-modulus endpoint branch

Define

```text
E_SAFE:
  d<=d_safe(B),
  H(z)~Y,
  Y>=B^(1/4-o(1)).
```

This branch is not covered by positive tH31 because tH31 used fixed-power multiplicative headroom and cumulative subtraction. Here

```text
y_z/L_B = 1 + H(z)/L_B
```

may tend to one.

However the branch is now theorem-ready: the prime variable is an ordinary Gaussian prime element in

- the fixed field `Q(i)`;
- one fixed broad canonical sector;
- one fixed ordinary invertible residue `beta_* mod d`;
- one norm interval `(L_B,L_B+H]` with `L_B=2*sqrt(B)` and additive width at least quarter-scale on an obstructing sequence;
- modulus norm `N((d))=d^2` inside the same pseudopolynomial safe range already certified by tH31.

The cofactor side only supplies `B^o(1)`-many moving upper endpoints inside one dyadic width layer and no opaque coefficient remains.

A fresh independent theorem audit is therefore materially different from tH30/tH31. It must determine the best unconditional short-norm-interval threshold available with the required fixed Gaussian residue and broad sector, retaining a possible exceptional real Hecke zero, and specifically answer whether the certified threshold reaches

```text
H>=B^(1/4-o(1))
```
(or equivalently norm-interval exponent `1/2+o(1)` relative to `L_B~B^(1/2)`).

The frozen request is

```text
SafeMitsuiModulusQuarterScaleFixedGaussianResidueShortIntervalPrimeOccupancy.
```

## 2. Beyond-Mitsui endpoint branch

Define

```text
E_LARGE:
  exp(c_safe*sqrt(log B))<d=B^o(1),
  H(z)~Y,
  Y>=B^(1/4-o(1)).
```

Even if a short-interval theorem existed at quarter scale for fixed/safe conductor, this branch would retain the separate individual large-subpolynomial modulus problem. It is therefore kept outside the tH32 target as

```text
QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias.
```

No modulus average is introduced.

## 3. Beyond-Mitsui long-headroom branch

The t139 survivor remains

```text
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

It is not mixed with the endpoint branch: the former has long intervals but excessive conductor; the latter has both short-interval and excessive-conductor issues.

## 4. Material receiver change

The old endpoint receiver allowed arbitrarily short prime intervals. That is no longer a possible principal-scale obstruction: t140/t141 remove all fixed-power-below-quarter widths by an elementary cofactor-annulus capacity argument.

The minimal fixed-U receiver is now

```text
(A) SafeMitsuiModulusQuarterScaleEndpointFixedGaussianResiduePrimeOccupancy
OR
(B) QuarterScaleEndpointBeyondMitsuiModulusFixedGaussianResiduePrimeOccupancyBias
OR
(C) LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

This is a material receiver change and reaches the `t142` revisit point named by merged Work-bvX34.

Under the shared batch contract the batch stops at this receiver change; tH32 is frozen but not consumed in this batch.

```text
ENDPOINT_SAFE_LARGE_MODULUS_CROSS_SPLIT_EXACT=true
ENDPOINT_OBSTRUCTING_WIDTH_GE_QUARTER_SCALE=true
SAFE_ENDPOINT_SHORT_INTERVAL_TARGET_THEOREM_READY=true
BEYOND_MITSUI_ENDPOINT_BRANCH_RETAINED=true
BEYOND_MITSUI_LONG_BRANCH_RETAINED=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=Audit the sharp unconditional short-norm-interval threshold for Gaussian prime elements in one fixed broad sector and one ordinary residue modulo d<=exp(c_safe*sqrt(log B)), with possible exceptional real Hecke zero retained; decide whether B^(1/4-o(1)) additive width suffices for T>=B^(-o(1))M.
T_ROUTE_H_TARGET=stages/stage14/14-t142/th32-target.md
T_ROUTE_H_BLOCKING=false
TH32_NEEDED=true
PREFERRED_RECEIVER=SharedUSafeMitsuiModulusQuarterScaleEndpointFixedGaussianResiduePrimeOccupancyOrBeyondMitsuiEndpointOrLongHeadroomResidueBias
NEXT=Stage14-tH32
