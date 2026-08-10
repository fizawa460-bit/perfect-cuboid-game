# Stage14-tH22 — projective ray-character large-sieve applicability audit, through merged t79

## Status

```text
STAGE14_TH22=COMPLETE_T79_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT
```

Target:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

Canonical predecessors now include merged t77, merged t78 and merged t79, together with the required t74--t76, tH20, tH21 and t71--t73 boundaries.

```text
MERGED_T78_IMPORTED=true
MERGED_T79_IMPORTED=true
```

The closed Pell/orbit, canonical-LPF, t74 fixed `(ell,c)`, t75 large-`g`, t75 high-imbalance Type-I, t76 large-`K_clean`, t77 radial selector and tH21 pre-ray DFI/Kuznetsov branches are not reopened.

---

## 1. t77 exact projective ray kernel

On the ray-active modulus

```text
M=Q_ray,
G(M)=(Z[i]/MZ[i])^x/(Z/MZ)^x,
|G(M)|=prod_{p|M}(p-chi_4(p))=M*B^o(1),
```

fixed beta and reciprocal orientation give

```text
[pi]_M=[U]^-1*I_beta*sigma([V]_M),
```

and exact character orthogonality

```text
1_{class equality}
=
1/|G(M)| sum_chi
 C_chi(U,beta)*chi(pi)*conjugate((chi o sigma)(V)).
```

```text
T77_PROJECTIVE_RAY_KERNEL_RETAINED=true
T77_RADIAL_SELECTOR_REOPENED=false
```

The principal character is not part of the nonprincipal large-sieve contract.

---

## 2. Merged t78 exact coefficient refinement

Merged t78 gives

```text
K_ext=K/gcd(K,k),
M=K_ext/gcd(K_ext,g),
M=1 <=> K_ext|g.
```

Fixed-power radial-only external support is already subsumed by t75 large-`g`.

The angular gcd has the exact four-cell factorization

```text
d_AR=gcd(odd(A),odd(r)),
d_AT=gcd(odd(A),odd(t)),
d_BR=gcd(odd(Bdir),odd(r)),
d_BT=gcd(odd(Bdir),odd(t)),
g=d_AR*d_AT*d_BR*d_BT,
```

with pairwise-coprime cells.  The `K`-coprime cell portions leave the ray-character family unchanged and exact Möbius inversion tensorizes the arithmetic direction/cover weights.

```text
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
K_COPRIME_ANGULAR_GCD_DOES_NOT_CHANGE_RAY_CHARACTER_FAMILY=true
```

The strongest hyperbola is exactly

```text
g*c=H*R*T,
ell*H*R*T<2B.
```

```text
SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD=true
SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true
```

Thus angular-gcd tensorization is no longer part of the external obstruction.

---

## 3. Merged t79 support stratification

For `chi in dual G(M)`, define the active rational support

```text
d(chi)=product_{p|M, chi_p nonprincipal} p,
e=M/d(chi).
```

Merged t79 proves exactly

```text
N_M(d)/|G(M)| <= B^o(1)/e.
```

Hence every character missing a fixed-power fraction of `M` is automatically power-suppressed before estimating the Gaussian-prime or cover sums.

The hard nonprincipal family may therefore be restricted to

```text
d(chi)=M/B^o(1).
```

Also:

- the principal character is exactly the expected `1/|G(M)|=M^-1 B^o(1)` projective density and requires no large sieve;
- endpoint-small `K_ext` implies endpoint-small `M` and only `B^o(1)` ray characters, so no large sieve is required merely for character enumeration there.

```text
PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true
PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE=false
FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true
HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true
ENDPOINT_SMALL_RAY_GROUP_CHARACTER_ENUMERATION_COST=Bo1
```

The current t-route receiver is therefore

```text
SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy.
```

---

## 4. Complete physical masks retained

The remaining theorem adapter must retain simultaneously

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
M=B^(positive power+o(1)),
d(chi)=M/B^o(1),
small angular g through t78 four-cell coefficients,
balanced primitive V=p+i*q,
r=q-p,
t=q+p,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell*H*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
delta=(r^2+t^2)/(2k),
fixed beta sign rule,
fixed reciprocal/inversion orientation.
```

```text
FULL_PHYSICAL_MASKS_RETAINED=true
APPLICABLE_THEOREM_ADAPTER_RETAINS_FULL_MASKS=false
```

---

## 5. Projective characters embed into Hecke-character language

Inflate a projective character to `(Z[i]/MZ[i])^x`, trivial on rational scalars.  Since `chi(i)=+/-1`, split into two unit parities:

- `chi(i)=+1`: finite-order ray-class/Hecke character;
- `chi(i)=-1`: multiply by the fixed infinity type `(z/|z|)^2`, changing analytic conductor only by `O(1)`.

```text
PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true
PROJECTIVE_CHARACTER_UNIT_PARITY_SPLIT_COUNT=2
PROJECTIVE_ODD_I_PARITY_REQUIRES_FIXED_INFINITY_TYPE=true
```

---

## 6. Actual finite conductor

Let

```text
d_chi=d(chi).
```

At an inert rational prime `p=3 mod 4`, a nontrivial projective local character is nontrivial on `F_{p^2}^x/F_p^x`, hence has local finite conductor `(p)` of norm `p^2`.

At a split rational prime `p=1 mod 4`, a nontrivial projective character is a ratio character `psi(x/y)` on the two split residue factors.  Triviality on diagonal rational scalars prevents a one-prime conductor; both primes above `p` are required, again giving the full rational ideal `(p)` of norm `p^2`.

Therefore

```text
PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_IDEAL=(d_chi)
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2
```

For the t79 hard family,

```text
d_chi=M/B^o(1),
N f_fin(chi)=M^2 B^o(1).
```

Thus t79 removes small-conductor/support-deficient characters from the hard family: the external analytic problem is specifically the **near-maximal conductor** projective family.

```text
HARD_PROJECTIVE_CHARACTER_CONDUCTOR_NORM=M^2*Bo1
PROJECTIVE_GROUP_SIZE_USED_AS_CONDUCTOR_NORM=false
```

---

## 7. Theorem applicability audit

### Hecke / ray-class large sieve

Ambient number-field large sieves naturally see conductor ideals and hence the `M^2` scale.  The Stage14 projective family has only `M*B^o(1)` characters.  No located off-the-shelf theorem gives the required conductor-compressed projective-subfamily moment while retaining the t78 divisor coefficients and physical masks.

```text
GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false
PROJECTIVE_SUBFAMILY_CONDUCTOR_COMPRESSION_LARGE_SIEVE_LOCATED=false
```

### Gaussian BV / BDH

Known number-field/Gaussian Bombieri–Vinogradov mechanisms depend on averaging over modulus/conductor families in a level-of-distribution range.  Here `M` is packet-conditioned, the hard conductor norm is `M^2 B^o(1)`, and the prime variable remains coupled to the short cover hyperbolas.

```text
GAUSSIAN_BV_BDH_APPLICABLE=false
```

### Hybrid `pi`--`V` character large sieve

The separated kernel

```text
chi(pi)*conjugate((chi o sigma)(V))
```

allows Cauchy/duality exactly.  t78 has already tensorized the arithmetic gcd coefficients, and t79 has already removed support-deficient characters.  What remains is a near-full-support, near-maximal-conductor hybrid moment with uniform coefficient `L2` control and the short physical masks.

No located theorem supplies that exact estimate.

```text
PROJECTIVE_CHARACTER_CAUCHY_DUALITY_FORMALLY_VALID=true
HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false
COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false
DIVISOR_DECOMPOSED_COEFFICIENT_L2_BOUND_THEOREM_READY=false
```

---

## 8. Power-saving verdict

The t78/t79 reductions narrow the analytic contract substantially, but do not produce an off-the-shelf fixed `B`-power saving.

```text
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
```

The minimal remaining external obstruction is now

```text
MINIMAL_REMAINING_OBSTRUCTION=NearFullSupportProjectiveConductorCompressedGaussianPrimeFourCellMobiusCoverHybridLargeSieve
```

and the current physical receiver is

```text
PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy
```

---

## 9. tH decision and next stage

Merged t79 explicitly says not to open tH23 yet.  t80 should first exploit near-full support locally, e.g. conductor-exact dualization / primitive projective Gauss sums, and only request tH23 if that produces a new standard analytic object.

```text
TH23_NEEDED=false
NEXT=Stage14-t80
```

---

## 10. Whole-family ledger

Latest merged main remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
```

No new whole-family saving is proved by tH22.

```text
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

---

## Locked boundary

```text
STAGE14_TH22=COMPLETE_T79_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT
MERGED_T78_IMPORTED=true
MERGED_T79_IMPORTED=true
T77_PROJECTIVE_RAY_KERNEL_RETAINED=true
T77_RADIAL_SELECTOR_REOPENED=false
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
PRINCIPAL_RAY_CHARACTER_IS_EXPECTED_DENSITY=true
PRINCIPAL_RAY_CHARACTER_REQUIRES_LARGE_SIEVE=false
FIXED_POWER_INACTIVE_SUPPORT_AUTOMATICALLY_SAVED=true
HARD_PROJECTIVE_CHARACTERS_HAVE_NEAR_FULL_ACTIVE_SUPPORT=true
PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true
PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_IDEAL=(d_chi)
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2
HARD_PROJECTIVE_CHARACTER_CONDUCTOR_NORM=M^2*Bo1
GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false
GAUSSIAN_BV_BDH_APPLICABLE=false
HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false
COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false
FULL_PHYSICAL_MASKS_RETAINED=true
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
MINIMAL_REMAINING_OBSTRUCTION=NearFullSupportProjectiveConductorCompressedGaussianPrimeFourCellMobiusCoverHybridLargeSieve
PREFERRED_RECEIVER=SharedUBalancedRayActiveNearFullSupportCanonicalGaussianPrimeProjectiveCharacterHybridEnergy
TH23_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-t80
```
