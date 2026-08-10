# Stage14-toolbox-ay — unique top-corner / fixed-U Pell receiver matrix

This matrix records only merged theorem sources on the toolbox-ay branch base.  Open or draft work is not promoted into the canonical ledger.

| Source | First merged consumer(s) | Proved refinement | Current disposition |
|---|---|---|---|
| `4cr` | `X9`, `4cs` | promotes `5/8`; retains exact `C_-/C_+` same/opposite Gaussian orientation | structural input; old `2/3` receiver is not current |
| `s7-31` | `X9`, `s7-32`, `4cs`, `t71` | `s7-32` collapses both apparent `5/8` barriers to `(theta,phi)=(5/16,1/4)` | current global geometry is one top corner |
| `t70` | `t71` | restores full Gaussian-component transfer of `kappa` inside small `J` | fixed-`U` only; followed by `t72` |
| `s7-32` | `4ct`, `X10` | one-host reconstruction fixes unique top-corner base receiver | both later filters apply to every possible `5/8` saturation packet |
| `4ct` | not yet audited beyond this stage | fixed-power residual-host gcd branches saved; `C_good` lifts to canonical Gaussian `Pi_C` | intersect with X10 filter, do not multiply savings |
| `X10` | not yet audited beyond this stage | large root-gcd branches saved; dominant Cayley Gaussian factor and short cofactor isolated | intersect with 4ct filter, do not identify `Pi_C` with `Pi_sigma` without proof |
| `t71` | `t72` | signed `kappa` split becomes one Cayley root-line modulus | large odd-`kappa` branch closed by t72 |
| `t72` | not yet audited beyond this stage | small-`kappa` real-quadratic norm/Pell-smooth receiver | `tH19` required; no global cross-promotion |

## Current whole-family certificate

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
CURRENT_GAP_TO_SQRT=1/8
FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=1
UNIQUE_FIVE_EIGHTHS_SATURATION_THETA=5/16
UNIQUE_FIVE_EIGHTHS_SATURATION_PHI=1/4
```

The old toolbox-ax global receiver

```text
FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence
```

is superseded as a current receiver by merged `s7-32` localization.

## Current global survivor

Merged `4ct` and merged `X10` prove complementary necessary filters on the same physical top-corner saturation packet.  The legal toolbox intersection is

```text
CURRENT_GLOBAL_TOOLBOX_RECEIVER=
TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence
```

with retained conditions including

```text
(theta,phi)=(5/16,1/4)
C=B^(3/8+o(1))
g=B^o(1)
N(Pi_C)=C_good=B^(3/8+o(1))
H<=B^(1/16+o(1))
C_sigma>=B^(1/8-o(1))
t_sigma<=B^(1/8+o(1))
q_xi=C*v_res
Z_S=lambda_S^2 W_S
primitive xi-agreement orientation
```

This is a survivor predicate, not a newly proved incidence bound.  In particular:

```text
FOUR_CT_AND_X10_FILTERS_SIMULTANEOUSLY_APPLICABLE_TO_SATURATING_PHYSICAL_PACKET=true
CURRENT_GLOBAL_TOOLBOX_RECEIVER_PROVED=false
```

No equality `Pi_C=Pi_sigma` is currently certified.

## Current fixed-U certificate

Merged `t72` leaves

```text
CURRENT_FIXED_U_RECEIVER=
SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy
```

and proves the large-odd-`kappa` root-line branch near-linear.  The complementary small-`kappa` object retains the real-quadratic norm equations together with the distinguished largest-prime and smooth-companion filters.

```text
TH19_NEEDED=true
TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
T72_CROSS_PROMOTED_TO_GLOBAL_TOP_CORNER=false
GLOBAL_AND_FIXED_U_RECEIVERS_EQUIVALENT=false
```

`tH19` is the correct independent theorem audit for the fixed-`U` line; it is not a toolbox-specific H continuation.

## Open-work guard

PR #531 (`Stage14-s7-33`) is an open draft exploratory branch.  Until merged:

```text
OPEN_S7_33_DRAFT_USED_AS_CANONICAL_SOURCE=false
```

The canonical global source chain remains merged `s7-32 -> 4ct/X10`.

## Next

```text
Stage14-toolbox-az:
audit first 4ct/X10/t72 consumers and the tH19 outcome against the unique-top-corner certificate.
```