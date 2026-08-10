# Stage14-t53 — post-residue Kummer principal stratification

## Purpose

Stage14-t52 showed that after t51/tH14 local residue cleanup, the principal squareclass problem is not a generic selector-completion problem: it returns to the LD2-transverse Kummer incidence isolated in t42–t44.

The frozen reciprocal quotient leaves

```text
post-residue principal blocks          14
distinct-ell cross-good LD2             12
same-ell LD2                              2
```

Stage14-t53 asks whether the 12 generic distinct-ell blocks are genuinely two-sided Kummer incidences, or whether a large part shares one Gaussian cofactor and therefore belongs to a narrower moving-canonical-prime family.

No global principal-collision power saving is assumed or claimed.

## 1. Exact Gaussian labels retained

For each reciprocal-quotient physical state retain

\[
(R,U,V,\ell,\text{branch},\varepsilon,\delta,h),
\]

where

\[
N(U)=m,\qquad N(V)=n,
\]

and `R=(eps,delta,h,branch)` is the common-refinement packet from t37/tH12.

Two Gaussian coordinates are compared up to the four units `mu_4`; this is the same unit convention used by tH14.

The two exact-unit principal blocks already absorbed by t51/tH14 are removed before the t53 stratification.

## 2. Frozen post-residue stratification

For the 12 distinct-canonical-prime cross-good LD2 blocks:

```text
same U unit-orbit                         6
same V unit-orbit                         1
same U or V union                         7
genuinely U/V transverse                  5
same branch                              10
same common-refinement packet             0
same unordered cover                      1
same m                                    6
same n                                    2
```

The six shared-U blocks are exactly a half of the generic distinct-ell model.  In every shared-U block, `N(U)=m` is also identical, as it must be.

The one shared-V block is also the unique same-cover block in the frozen generic family.

Thus the generic principal incidence decomposes exactly as

\[
\boxed{
I_{\rm gen}
=I_{U\text{-shared}}+I_{V\text{-shared}}+I_{UV\text{-transverse}}.
}
\]

Frozen cardinalities are

\[
\boxed{12=6+1+5.}
\]

This is a partition, not an upper-bound argument.

## 3. Shared-U canonical-prime stratum

For a shared-U pair, up to Gaussian units,

\[
A_c=\pi U,\qquad A'_c=\pi' U,
\]

with distinct canonical Gaussian primes `pi,pi'` above distinct rational primes `ell,ell'`.

Therefore the direction cofactor itself is fixed while the canonical prime and the cover-side data move.  This is strictly more structured than an arbitrary pair of LD2-transverse Kummer fibers.

We name the remaining incidence problem on this stratum

```text
SharedUCanonicalPrimePrincipalIncidence
```

and its target is a near-linear aggregate bound over fixed primitive `U` fibers, with all physical hyperbola/canonical/branch selectors retained.

Important guard: fixing `U` is **not** the same as fixing the t37 common-refinement packet.  Frozen data already show `same_common_packet=0` after residue cleanup.  Therefore t37/tH12 fixed-packet estimates cannot simply be quoted to close this stratum.

## 4. Shared-V stratum

Exactly one frozen generic block shares the Gaussian cover cofactor `V`; it also shares the unordered physical cover `(p,q)`.

This motivates the separate receiver

```text
SharedVCanonicalPrimePrincipalIncidence
```

which is the cover-dual analogue of the shared-U family.  The frozen multiplicity is small, but no asymptotic boundedness claim is inferred from one block.

## 5. Genuine two-sided Kummer stratum

Only five of the twelve frozen distinct-ell cross-good principal blocks have neither `U` nor `V` in a common unit orbit.

These are the genuinely two-sided objects for which the t42 twisted-Kummer surface remains the correct primitive geometric model:

```text
UVTransverseCrossGoodLD2KummerPrincipalIncidence
```

They also have no common-refinement packet coincidence.  Consequently neither tH14 residue cleanup nor a one-cofactor freeze explains them.

## 6. Same-ell exceptional slice

The two post-residue same-ell blocks satisfy:

```text
same U orbit               0
same V orbit               0
same common packet         0
same branch                2
```

They remain a separate exceptional slice.  t53 does not combine them with the distinct-ell canonical-prime problem.

## 7. What t53 proves and does not prove

Proved / exact:

1. t52 post-residue model is reproduced from the physical state construction;
2. the 12 distinct-ell cross-good LD2 blocks split exactly `6 + 1 + 5` by shared `U`, shared `V`, and genuine `U/V` transversality;
3. no post-residue principal block shares the full common-refinement packet;
4. the same-ell two-block slice is disjoint from the shared-U/shared-V generic strata.

Not proved:

- a near-linear bound for the shared-U canonical-prime incidence;
- a near-linear bound for the shared-V incidence;
- a generic Kummer incidence theorem for the five U/V-transverse blocks;
- any global `A1`, `A_11`, critical-strip, or `T=o(sqrt(B))` power saving.

## 8. Next target

The largest newly isolated stratum is shared-U.  Stage14-t54 should attack

\[
\boxed{\text{SharedUCanonicalPrimePrincipalIncidence}}
\]

first, using the exact representation `A_c=pi U` with fixed primitive `U`, while allowing the common packet and cover variables to move.  The main question is whether the equal-squareclass condition becomes a one-moving-canonical-prime character/curve problem after the cover-side divisor coupling is retained.

The five genuinely U/V-transverse blocks remain the fallback Kummer core if the shared-U stratum can be closed.

## tH decision

**No additional tH stage is needed.  Do not start tH15.**

The new split is an arithmetic stratification of a live object already represented by t42–t44, not a missing adapter.  Reopen support only if t54 produces a concrete fixed-U/moving-prime theorem shape not covered by existing canonical-prime receivers.

## Boundary

```text
STAGE14_T53=COMPLETE_POST_RESIDUE_KUMMER_PRINCIPAL_STRATIFICATION
TH14_CONSUMED=true
TH15_NEEDED=false
POST_RESIDUE_PRINCIPAL_BLOCKS=14
DISTINCT_ELL_CROSS_GOOD_LD2_BLOCKS=12
SAME_ELL_LD2_BLOCKS=2
FROZEN_SHARED_U_GENERIC_BLOCKS=6
FROZEN_SHARED_V_GENERIC_BLOCKS=1
FROZEN_UV_TRANSVERSE_GENERIC_BLOCKS=5
POST_RESIDUE_COMMON_PACKET_COLLISIONS=0
SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_REQUIRED=true
SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false
SHARED_V_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false
UV_TRANSVERSE_CROSS_GOOD_LD2_KUMMER_INCIDENCE_PROVED=false
GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t54 attack SharedUCanonicalPrimePrincipalIncidence with fixed primitive U and moving canonical prime, retaining the moving common-packet and cover-side divisor coupling
```
