# Stage14-tH31 — independent Mitsui-safe fixed-residue Gaussian-prime occupancy audit

## Status

`COMPLETE_POSITIVE_MITSUI_SAFE_LONG_HEADROOM_FIXED_RESIDUE_OCCUPANCY_AUDIT`

This is a clean-room audit of the frozen Stage14-t138 target only.

```text
AUDITED_THROUGH=Stage14-t138
SOURCE_SNAPSHOT_SHA=3916563a938dc5d1c8369bcd4d28ca02c3e2b64a
TARGET_FILE=stages/stage14/14-t138/th31-target.md
TARGET_FROZEN=true
REQUESTED_OBJECT=MitsuiSafeLongHeadroomFixedGaussianResiduePrimeOccupancyLowerBound
```

No later Stage14-t conclusion is used.

## 1. Frozen target

The target is the safe long-headroom count

```text
T_safe
 = sum_{z in Z_safe,long}
   #{canonical split Gaussian prime pi:
     pi==beta_* (mod d),
     L_B<N(pi)<=y_z},
```

against

```text
M_safe
 = 1/|(Z[i]/dZ[i])^x|
   * sum_z
     #{canonical split Gaussian prime pi:
       L_B<N(pi)<=y_z},
```

where

```text
L_B=2*sqrt(B),
y_z/L_B>=B^theta,
theta>0 fixed,
d<=exp(c_safe*sqrt(log B)),
q=(d),
N(q)=d^2.
```

The cofactor set is explicit and contributes only by selecting the upper endpoints `y_z`.

The required conclusion is only

```text
T_safe >= B^(-o(1)) M_safe.
```

## 2. Mitsui/Kai theorem matches the prime-element geometry

Mitsui's generalized prime number theorem counts prime elements of a fixed number field in archimedean regions and a prescribed congruence class.  Wataru Kai's refinement, arXiv:2209.11816, states the classical polylogarithmic-modulus prime-element theorem and then retains the possible Siegel secondary term in order to extend the modulus norm to a pseudopolynomial range

```text
N(q) <= exp(sqrt(log X)/O_K(1)).
```

Its prime-element formulation explicitly handles

- a fixed number field `K`;
- a residue `alpha mod q`;
- archimedean convex/thin-cone restrictions;
- a possible real Hecke/Siegel character and its secondary main term.

For `K=Q(i)`, the t138 canonical open D4 sector is an admissible fixed angular region/fundamental-sector piece.  Inert rational Gaussian primes lie on the real/imaginary axes, hence outside the strict open canonical sector; the prime elements counted in the physical sector are the desired split Gaussian prime elements up to the finitely many ramified/boundary exceptions.

Choosing `c_safe>0` sufficiently small makes

```text
N((d))=d^2 <= exp(sqrt(log X_z)/O(1))
```

uniformly for `X_z=sqrt(y_z)` throughout the long branch.

```text
MITSUI_KAI_PRIME_ELEMENT_GEOMETRY_MATCHES_TARGET=true
CANONICAL_OPEN_SECTOR_COMPATIBLE=true
ORDINARY_GAUSSIAN_RESIDUE_COMPATIBLE=true
MITSUI_PSEUDOPOLYNOMIAL_MODULUS_CONDITION_SATISFIED=true
```

## 3. Fixed-power headroom removes the interval issue

Kai's theorem is cumulative in a bounded region.  Apply it to the fixed sector/residue truncated at norm `y_z` and at norm `L_B`, then subtract.

Because

```text
y_z/L_B >= B^theta,
```

the lower endpoint cumulative principal mass is smaller by a fixed power than the upper endpoint mass.  Thus no genuinely short-interval prime theorem is required on this branch.

The same subtraction is valid with the possible Siegel secondary term retained, because its integrand is nonnegative after the sign is fixed and its scale changes monotonically with norm.

```text
LONG_HEADROOM_CUMULATIVE_SUBTRACTION_VALID=true
SHORT_INTERVAL_THEOREM_REQUIRED=false
```

## 4. A possible Siegel zero cannot create a fixed B-power depletion in the safe range

Kai's refined main term has the schematic local density

```text
1 - sigma_exc * N(pi)^(beta_exc-1),
```

where `sigma_exc in {+1,-1}` is the value of the possible real exceptional character on the frozen residue/sector class.

If

```text
sigma_exc=-1,
```

the secondary term increases the lower occupancy and is harmless.

If

```text
sigma_exc=+1,
```
write

```text
lambda=1-beta_exc>0.
```

The suppressing factor on the interval is bounded below by

```text
1-L_B^(-lambda).
```

The standard Siegel lower bound for a real Hecke zero over the fixed field `Q(i)` gives, for every fixed `epsilon>0`, ineffectively but uniformly,

```text
lambda >= N(q)^(-epsilon).
```

Since on the safe branch

```text
N(q) <= exp(O(sqrt(log B))),
```
we obtain

```text
lambda = B^(-o(1)),
1-L_B^(-lambda) >= B^(-o(1)).
```

Thus even the suppressing exceptional sign can reduce the principal fixed-residue density only by a subpolynomial factor, never by `B^-delta` for fixed `delta>0`.

The prime-element theorem error is

```text
X^2*exp(-sqrt(log X)/O(1))
```
for `Q(i)`.  By choosing `c_safe` strictly inside the theorem's pseudopolynomial modulus constant, the residue-class denominator `phi_K(q)=B^o(1)` and the worst exceptional suppression `B^{-o(1)}` are both dominated by the exponential-in-`sqrt(log B)` error margin.  Hence the lower main term remains positive at `B^{-o(1)}` relative scale.

```text
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SIEGEL_SECONDARY_TERM_FIXED_POWER_DEPLETION_POSSIBLE=false
SIEGEL_SUPPRESSING_FACTOR_LOWER_BOUND=BoMinusO1
MITSUI_SAFE_ERROR_ABSORBED_AFTER_RESIDUE_DENOMINATOR=true
```

## 5. From log-weighted prime elements to the t138 count

Mitsui/Kai is naturally stated with logarithmic prime weights.  On the interval

```text
L_B<N(pi)<=y_z
```
all logarithmic weights are `B^o(1)` at exponent level.  Partial summation, or simply bounding each weight between comparable logarithmic scales on the fixed-power long interval, transfers the `B^{-o(1)}` lower ratio to the unweighted prime-element count.

The unrestricted canonical split-prime denominator in `M_safe` is governed by the ordinary Gaussian prime number theorem and differs from its volume/main-term normalization by only `B^o(1)` at the precision needed here.

Therefore, uniformly on the frozen safe branch,

```text
T_safe >= B^(-o(1)) M_safe.
```

Consequently for every fixed `delta>0`, for sufficiently large `B`,

```text
T_safe <= B^(-delta) M_safe
```

is impossible whenever `M_safe>0`.

```text
SAFE_BRANCH_T_GE_BO_MINUS_O1_M_PROVED=true
SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT=true
```

## 6. Scope boundary

This positive audit does **not** cover either remaining region:

```text
endpoint-short:
  y_z/L_B -> 1 with no uniform headroom,

large-subpolynomial modulus:
  d > exp(c_safe*sqrt(log B)) but d=B^o(1).
```

The first still lacks an interval lower theorem; the second can lie beyond the modulus range of Kai's pseudopolynomial prime-element theorem.

No saving is cross-promoted to the whole family.  The theorem only rules out one possible fixed-U depletion mechanism.

## Certified verdict

```text
MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE=true
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SIEGEL_SECONDARY_TERM_FIXED_POWER_DEPLETION_POSSIBLE=false
SAFE_BRANCH_T_GE_BO_MINUS_O1_M_PROVED=true
SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT=true
DIRECT_THEOREM_APPLICABLE=true
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT_H_NEEDED=false
```

## Primary sources checked

```text
Wataru Kai, Notes on Mitsui's Prime Number Theorem with Siegel zeros,
  arXiv:2209.11816 (v2, 2023).

Takayoshi Mitsui, Generalized Prime Number Theorem,
  Japanese Journal of Mathematics 26 (1956), 1--42.
```

Kai's introduction explicitly records Mitsui's congruence-and-convex-region prime-element theorem, the Siegel secondary term, and the pseudopolynomial modulus extension.  Those are exactly the ingredients used here.

## Frozen boundary

```text
STAGE14_TH31=COMPLETE_POSITIVE_MITSUI_SAFE_LONG_HEADROOM_FIXED_RESIDUE_OCCUPANCY_AUDIT
AUDITED_THROUGH=Stage14-t138
SOURCE_SNAPSHOT_SHA=3916563a938dc5d1c8369bcd4d28ca02c3e2b64a
TARGET_FROZEN=true
MITSUI_SAFE_LONG_HEADROOM_THEOREM_APPLICABLE=true
SAFE_BRANCH_FIXED_POWER_DEPLETION_RULED_OUT=true
ENDPOINT_SHORT_BRANCH_UNCHANGED=true
LARGE_SUBPOLYNOMIAL_MODULUS_BRANCH_UNCHANGED=true
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
