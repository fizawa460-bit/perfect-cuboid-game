# Stage14-t138 — freeze Mitsui-safe long-headroom fixed-residue prime occupancy target

## Status

`COMPLETE_MITSUI_SAFE_LONG_HEADROOM_FIXED_RESIDUE_TARGET_FREEZE`

Consumes Stage14-t137 on this batch branch together with merged `Stage14-t135/t136`, completed merged `Stage14-tH30`, and merged `Stage14-Work-buX33`.

The long-headroom branch has now been split into

```text
SAFE_MITSUI:
  d <= exp(c_safe*sqrt(log B)),

LARGE_SUBPOLY:
  exp(c_safe*sqrt(log B)) < d = B^o(1).
```

This stage freezes only the first branch for an independent theorem audit.

## 1. Exact safe-branch object

Fix the t135 ordinary cofactor residue `rho_*`, ordinary prime residue `beta_*`, one fixed open D4/canonical sector `S`, and the frozen exceptional cofactor packet.

For the actual long-headroom primitive cofactors `z`, define

```text
L_B=2*sqrt(B),
y_z=X_U/N(z),
y_z/L_B>=B^theta
```

for fixed `theta>0`.

The physical safe-branch count is exactly

```text
T_safe
 = sum_z
   #{canonical split Gaussian prime pi:
     pi==beta_* (mod d),
     L_B<N(pi)<=y_z}.
```

The ordinary-residue principal baseline is

```text
M_safe
 = 1/|R_d| * sum_z
   #{canonical split Gaussian prime pi:
     L_B<N(pi)<=y_z},

R_d=(Z[i]/dZ[i])^x.
```

The cofactor side remains explicit and unweighted.  No projective/Fourier coefficient remains.

## 2. Why a cumulative theorem suffices

The target does not require a genuinely short-interval theorem.  On every safe long cofactor

```text
y_z >= L_B*B^theta.
```

Thus a cumulative fixed-residue prime-element theorem at `y_z`, minus the same theorem at `L_B`, has a polynomial headroom gap.  The lower cumulative main term is smaller by at least `B^{-theta+o(1)}` relative to the upper one, provided the same possible Siegel secondary term is retained consistently.

Consequently the exact theorem target is only

```text
T_safe >= B^(-o(1)) M_safe,
```

not a unit-relative-error asymptotic for the interval itself.

## 3. Why the exceptional zero must remain in the target

The SAFE_MITSUI modulus range is deliberately wider than the classical polylogarithmic Siegel-Walfisz range.  A possible real Hecke/Siegel character may therefore contribute a second main term.

For one fixed residue/sector packet its sign is frozen, but t138 does not assume that the secondary term is favorable.  The audit must prove that even the suppressing sign cannot reduce the safe branch by a fixed power of `B` once the modulus lies in the chosen pseudopolynomial range.

This makes tH31 materially different from tH30: tH30 audited all `d=B^o(1)` and therefore stopped at the modulus obstruction; tH31 audits only the explicit pseudopolynomial conductor subrange and asks for the weaker `B^{-o(1)}` lower ratio needed by Stage14.

## 4. Immutable H request

The target is frozen at

```text
stages/stage14/14-t138/th31-target.md
```

with requested object

```text
MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyLowerBound.
```

The audit should prioritize Mitsui's prime-element theorem and modern versions retaining Siegel zeros, specialized to `K=Q(i)`, one fixed open sector and one ordinary residue class modulo `(d)`.

The large-subpolynomial branch and endpoint-short branch are outside this H target.

```text
MITSUI_SAFE_TARGET_FROZEN=true
FIXED_POWER_HEADROOM_REPLACES_SHORT_INTERVAL_THEOREM_NEED=true
POSSIBLE_SIEGEL_ZERO_MUST_BE_RETAINED=true
LARGE_SUBPOLYNOMIAL_MODULUS_BRANCH_EXCLUDED_FROM_TH31=true
ENDPOINT_SHORT_BRANCH_EXCLUDED_FROM_TH31=true
RECEIVER_MATERIALLY_CHANGED=false
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyLowerBound
T_ROUTE_H_TARGET=stages/stage14/14-t138/th31-target.md
T_ROUTE_H_BLOCKING=false
TH31_NEEDED=true
PREFERRED_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficitOrMitsuiSafeLongHeadroomFixedResiduePrimeOccupancyOrLongHeadroomLargeSubpolynomialModulusFixedResiduePrimeOccupancyBias
NEXT=Stage14-tH31
```