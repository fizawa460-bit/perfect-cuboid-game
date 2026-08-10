# Stage14-tH22 — canonical Gaussian-prime projective ray-character balanced-cover large-sieve applicability audit

## Status

```text
STAGE14_TH22=COMPLETE_T78_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT
```

Audit target:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

This audit consumes merged t77 and the required t74--t76, tH20, tH21, and t71--t73 boundaries. It also consumes merged Stage14-t78, including

```text
stages/stage14/14-t78/th22-refinement.md
```

as the canonical refinement requested during this audit.

```text
MERGED_T78_IMPORTED=true
T78_REFINEMENT_CONSUMED=true
T78_REFINEMENT_SOURCE_PR=567
T78_REFINEMENT_MERGED_PREDECESSOR=true
```

No closed branch is reopened: Pell/class number/regulator, canonical-LPF detection, t74 fixed `(ell,c)`, t75 large-`g`, t75 high-imbalance Type-I, t76 large-`K_clean` root-line spacing, and the tH21 pre-ray DFI/Kuznetsov verdict remain closed.

---

## 1. Exact t77 ray kernel retained

Fix

```text
(U,epsilon,k,h,kappa,beta).
```

With

```text
Q=K_clean,
Q_rad=gcd(Q,k)=gcd(Q,m),
M=Q_ray=Q/Q_rad,
```

t77 proves on `M`

```text
G(M)=(Z[i]/MZ[i])^x/(Z/MZ)^x,
|G(M)|=prod_{p|M}(p-chi_4(p))=M*B^o(1),
```

and after fixed beta and reciprocal orientation

```text
[pi]_M=[U]^-1*I_beta*sigma([V]_M).
```

Hence exactly

```text
1_{class equality}
=
1/|G(M)| sum_{chi in dual G(M)}
 C_chi(U,beta)*chi(pi)*conjugate((chi o sigma)(V)).
```

The principal character contributes the natural

```text
M^-1*B^o(1)
```

projective density. This audit concerns only the nonprincipal contribution.

```text
T77_PROJECTIVE_RAY_KERNEL_RETAINED=true
T77_RADIAL_SELECTOR_REOPENED=false
RADIAL_SELECTOR_ARTIFICIAL_DENSITY_CHARGED=false
```

---

## 2. Merged t78 refinement imported exactly

Merged t78 gives

```text
K_ext=K/gcd(K,k),
M=K/gcd(K,g*k)=K_ext/gcd(K_ext,g).
```

Therefore

```text
M=1 <=> K_ext|g.
```

A radial-only block with fixed-power `K_ext` is already contained in t75's large-angular-`g` mechanism. tH22 audits only `M>1` ray-active packets; it does not reopen fixed-power radial-only external support.

```text
T78_RAY_MODULUS_EXTERNAL_FORMULA_RETAINED=true
T78_FIXED_POWER_RADIAL_ONLY_BRANCH_REOPENED=false
```

The angular gcd is decomposed into four pairwise-coprime cells

```text
d_AR=gcd(odd(A),odd(r)),
d_AT=gcd(odd(A),odd(t)),
d_BR=gcd(odd(Bdir),odd(r)),
d_BT=gcd(odd(Bdir),odd(t)),
g=d_AR*d_AT*d_BR*d_BT.
```

Only the `K`-supported parts of these cells affect `M`; the `K`-coprime parts leave the ray-character family unchanged. Exact Möbius inversion gives a separated direction/cover divisor tensor with only `B^o(1)` pointwise multiplicity.

```text
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
K_COPRIME_ANGULAR_GCD_DOES_NOT_CHANGE_RAY_CHARACTER_FAMILY=true
K_SUPPORTED_FOUR_CELL_ORIENTATION_MULTIPLICITY=Bo1
```

Thus the pre-t78 question “can the angular gcd be Möbius/divisor-switched?” is no longer an obstruction.

The exact t78 cofactor identities are

```text
c/odd(h)=R1*T1,
g*c=odd(h)*odd(r)*odd(t),
```

so the strongest t74 hyperbola becomes

```text
ell*odd(h)*odd(r)*odd(t)<2B.
```

Since `ell^2>4B`,

```text
odd(h)*odd(r)*odd(t)<sqrt(B).
```

```text
SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD=true
SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true
ODD_COVER_PRODUCT_IS_SQRT_B_SHORT=true
```

---

## 3. Complete physical masks retained

After t78 the theorem adapter must still retain

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
M>1 ray-active and t76-deficient,
small angular g through the four-cell conditioned coefficients,
balanced primitive V=p+i*q,
r=q-p,
t=q+p,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
c/odd(h)=R1*T1,
gcd(R1,T1)=1,
ell*odd(h)*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
delta=(r^2+t^2)/(2k),
fixed beta sign rule,
fixed reciprocal/inversion orientation.
```

Dyadic/Mellin localization costs only `B^o(1)` bookkeeping and preserves ray characters, but the coefficient `L2` norms after the four-cell divisor decomposition still have to be controlled uniformly.

```text
FULL_PHYSICAL_MASKS_RETAINED=true
APPLICABLE_THEOREM_ADAPTER_RETAINS_FULL_MASKS=false
```

---

## 4. Projective characters embed in standard Hecke-character language

Inflate

```text
chi in dual G(M)
```

to a finite residue character on `(Z[i]/MZ[i])^x`, trivial on rational scalars. Then `chi(-1)=1` and `chi(i)=+/-1`.

Split into two unit parities.

- If `chi(i)=+1`, the finite character is trivial on Gaussian units and yields a finite-order ray-class/Hecke character.
- If `chi(i)=-1`, multiply by the fixed infinity type `(z/|z|)^2`; this cancels the unit sign and changes analytic conductor only by an `O(1)` archimedean factor.

Therefore

```text
PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true
PROJECTIVE_CHARACTER_UNIT_PARITY_SPLIT_COUNT=2
PROJECTIVE_ODD_I_PARITY_REQUIRES_FIXED_INFINITY_TYPE=true
PROJECTIVE_INFINITY_TYPE_COST=O1
```

This is an exact representation statement, not a saving theorem.

---

## 5. Actual finite conductor

For one projective character set

```text
d_chi=product_{p|M, chi_p nonprincipal} p.
```

### Inert `p == 3 mod 4`

`(p)` is prime in `Z[i]`, with residue field `F_{p^2}`. A nontrivial projective local character lives on `F_{p^2}^x/F_p^x`, so its finite conductor is `(p)` and has ideal norm `p^2`.

### Split `p == 1 mod 4`

Write `(p)=mathfrak p*conjugate(mathfrak p)`. The projective quotient is the ratio of the two `F_p^x` factors. A nontrivial local character has form `psi(x/y)` and depends on both components. A conductor using only one split prime would depend on only one coordinate; triviality on diagonal rational scalars would then force triviality. Hence the nontrivial projective local conductor is again the full rational ideal `(p)`, norm `p^2`.

Thus exactly

```text
PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_IDEAL=(d_chi)
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2
MAX_PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=M^2
PROJECTIVE_GROUP_SIZE_USED_AS_CONDUCTOR_NORM=false
```

The distinction

```text
|G(M)|=M*B^o(1)
```

versus

```text
N f_fin(chi)<=M^2
```

is the central conductor issue.

---

## 6. Range and quantifier audit

The order is

```text
fix (U,epsilon,k,h,kappa,beta),
fix the K-supported four-cell orientation and dyadic packet,
then M=K_ext/gcd(K_ext,g) is fixed up to B^o(1) divisor choices,
then sum moving canonical Gaussian primes pi and balanced covers V,
then use projective characters chi in dual G(M).
```

So there is no long independent `M`-average in one fixed packet.

The deficient range gives

```text
M < R*T*B^o(1),
N(V)=(r^2+t^2)/2=R*T*B^o(1)
```

on balanced blocks. This makes the raw cover length favorable relative to `M`, but the actual Hecke conductor norm can still be as large as `M^2`. No t77/t78 identity forces the whole deficient range into a Gaussian-prime BV/BDH conductor level.

```text
DEFICIENT_M_GIVES_BROAD_MODULUS_AVERAGING=false
DEFICIENT_M_CONTROLS_PROJECTIVE_GROUP_SIZE=true
DEFICIENT_M_CONTROLS_HECKE_CONDUCTOR_NORM_TO_LINEAR_SCALE=false
```

---

## 7. Candidate theorem audit

### 7.1 Hecke/ray-class large sieve

Ambient number-field large sieves use modulus/conductor ideals. Here the ambient finite conductor norm is up to `M^2`, while the projective dual has only `M*B^o(1)` characters. No located theorem gives the required conductor-compressed projective-subfamily moment of schematic size

```text
(M + sequence length)*B^o(1)
```

with the t78 divisor-decomposed coefficients and all physical masks retained.

```text
GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false
PROJECTIVE_SUBFAMILY_CONDUCTOR_COMPRESSION_LARGE_SIEVE_LOCATED=false
```

### 7.2 Gaussian BV / BDH

Known Gaussian/number-field BV mechanisms average primes over modulus/conductor families inside a level-of-distribution range. Here `M` is packet-conditioned, the standard conductor norm can be `M^2`, and the moving prime is simultaneously restricted by the canonical-ell and short-cover hyperbolas. There is no uniform full-range adapter.

```text
GAUSSIAN_BV_BDH_APPLICABLE=false
GAUSSIAN_BV_BDH_SMALL_CONDUCTOR_SUBRANGE_PLAUSIBLE=true
```

### 7.3 Hybrid `pi`--`V` character large sieve

The arithmetic kernel is exactly separated:

```text
chi(pi)*conjugate((chi o sigma)(V)).
```

Cauchy/duality is therefore legal. After t78, the gcd arithmetic itself is also tensorized. What remains is a uniform moment bound for the two coefficient sequences, with projective conductor compression and the dyadic short-cover cutoffs preserved.

No located theorem supplies this exact hybrid estimate.

```text
PROJECTIVE_CHARACTER_CAUCHY_DUALITY_FORMALLY_VALID=true
HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false
```

### 7.4 Cover sequence

The raw conductor/length comparison is promising, but the cover sequence remains

```text
primitive,
balanced,
gcd(r,t) in {1,2},
K-supported cell conditioned,
divisor-decomposed,
R*T short,
short-ellipse localized,
ell*H*R*T localized,
ell*delta localized.
```

The algebraic tensorization is proved; the required uniform coefficient `L2` and character moment bound is not.

```text
COVER_RAW_CONDUCTOR_LENGTH_RANGE_PROMISING=true
COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false
DIVISOR_DECOMPOSED_COEFFICIENT_L2_BOUND_THEOREM_READY=false
```

---

## 8. Strict power-saving verdict

The t78 refinement improves the adapter state but does not change the off-the-shelf conclusion.

```text
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
```

No positive exponent is certified because no theorem adapter simultaneously proves:

1. the `M`-sized projective-family compression against conductor norm up to `M^2`;
2. uniform moments for the t78 four-cell divisor-decomposed prime and cover coefficients;
3. preservation of the canonical Gaussian-prime condition and short ellipse / `ell*H*R*T` / `ell*delta` masks.

The refined minimal obstruction is

```text
MINIMAL_REMAINING_OBSTRUCTION=ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve
```

and the current physical receiver is

```text
PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagBalancedExternalKappaRayCharacterFourCellMobiusTypeIIEnergy
```

This matches merged t78's narrowing rather than retaining the older opaque angular-gcd receiver.

---

## 9. Supervisor decision

`tH23` is not needed now. The next internal route stage is t79: consume the endpoint-small radial residue/principal-character packet and, on the ray-active side, quantify the divisor-decomposed coefficient norms before requesting another external theorem audit.

```text
TH23_NEEDED=false
NEXT=Stage14-t79
```

---

## 10. Current shared exponent

Latest merged main remains at

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
```

(the merged 4cy/s7-40 work refines saturation but does not lower the exponent). tH22 proves no new whole-family saving.

```text
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

---

## Locked boundary

```text
STAGE14_TH22=COMPLETE_T78_REFINED_CANONICAL_GAUSSIAN_PRIME_PROJECTIVE_RAY_CHARACTER_BALANCED_COVER_LARGE_SIEVE_APPLICABILITY_AUDIT
MERGED_T78_IMPORTED=true
T77_PROJECTIVE_RAY_KERNEL_RETAINED=true
T77_RADIAL_SELECTOR_REOPENED=false
T78_REFINEMENT_CONSUMED=true
T78_REFINEMENT_SOURCE_PR=567
T78_REFINEMENT_MERGED_PREDECESSOR=true
T78_FIXED_POWER_RADIAL_ONLY_BRANCH_REOPENED=false
T78_RAY_MODULUS_EXTERNAL_FORMULA_RETAINED=true
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD=true
SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true
PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=true
PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=true
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_IDEAL=(d_chi)
PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=d_chi^2
MAX_PROJECTIVE_CHARACTER_FINITE_CONDUCTOR_NORM=M^2
PROJECTIVE_GROUP_SIZE_USED_AS_CONDUCTOR_NORM=false
GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=false
GAUSSIAN_BV_BDH_APPLICABLE=false
HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=false
COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=false
FULL_PHYSICAL_MASKS_RETAINED=true
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
MINIMAL_REMAINING_OBSTRUCTION=ProjectiveConductorCompressedGaussianPrimeExternalKappaFourCellMobiusCoverHybridLargeSieve
PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagBalancedExternalKappaRayCharacterFourCellMobiusTypeIIEnergy
TH23_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-t79
```
