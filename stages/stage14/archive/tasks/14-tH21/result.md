# Stage14-tH21 — balanced clean-kappa canonical-prime primitive-cover Type-II dispersion applicability audit

## Purpose

Independent audit target:

```text
SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
```

This audit consumes latest-main merged t76, together with the live t74/t75/tH20 and fixed-tag t71--t73 boundaries. It does not reopen Pell/class-number/regulator issues, canonical-largest-prime detection, t74 fixed `(ell,c)` fibers, t75 large-`g`, t75 high-imbalance Type-I, or t76 large-`K_clean` root-line spacing.

Strict rule: `APPLICABLE=true` is allowed only if an explicit theorem adapter preserves the quantifier order, modulus and variable ranges, coefficient dependence, moving canonical `ell`, `K_clean`, fixed-beta sign, balanced primitive cover, short ellipse, and all sharp hyperbolas.

Result: no audited off-the-shelf Type-II theorem meets that standard. The missing object is a weighted discrepancy estimate for a **fixed clean-kappa projective modulus with a moving Gaussian-prime direction coefficient**.

---

## 1. Exact t76 kernel retained

Fix

```text
(U,epsilon,k,h,kappa,beta),
beta=gcd(kappa,v).
```

Use

```text
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p,
K=odd(kappa),
K_bad=gcd(K,g),
K_clean=K/K_bad.
```

Merged t76 gives

```text
gcd(K_clean,A*Bdir*r*t)=1,
K_clean < R*T*B^o(1),
t == rho*r (mod K_clean).
```

Fixed `beta` fixes the primewise sign. Only the reciprocal direction choice remains, with total multiplicity

```text
2^omega(K_clean)=B^o(1).
```

The already-closed branch

```text
K_clean >= R*T*B^(-o(1))
```

is not reconsidered.

```text
T76_LARGE_CLEAN_KAPPA_BRANCH_REOPENED=false
PROJECTIVE_ROOTLINE_KERNEL_RETAINED=true
FIXED_BETA_ROOT_SIGN_RETAINED=true
```

---

## 2. Physical masks retained

All of the following remain inside the receiver:

```text
g small on its dyadic scale,
r,t balanced,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell^2>4B,
ell*c<2B,
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
c/odd(h)=R0*T0,
gcd(R0,T0)=1,
ell canonical Gaussian direction prime.
```

They come from one physical state, so separate hyperbola savings are not multiplied.

```text
CANONICAL_ELL_MASK_RETAINED=true
SHORT_ELLIPSE_MASK_RETAINED=true
SHARP_ELL_G_C_HYPERBOLA_RETAINED=true
SHARP_ELL_C_HYPERBOLA_RETAINED=true
SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
BALANCED_PRIMITIVE_COVER_MASK_RETAINED=true
SMALL_ANGULAR_G_MASK_RETAINED=true
```

---

## 3. Quantifier order and the fixed-modulus obstruction

After fixing `(U,epsilon,k,h,kappa,beta)` and dyadic scales, condition on `K_bad=gcd(K,g)`. Since `K` is fixed, this costs only `tau(K)=B^o(1)` and fixes `K_clean`.

The analytic order is then

```text
fixed packet
-> fixed dyadic scales and K_clean
-> fixed reciprocal root orientation
-> moving canonical Gaussian prime pi, N(pi)=ell
-> moving balanced primitive cover (r,t)
```

Thus

```text
root modulus = K_clean is fixed,
moving prime = ell is separate,
ell is not the modulus of t==rho*r.
```

The deficient inequality gives more points on one residue line; it does not create a modulus average.

```text
KCLEAN_EFFECTIVELY_FIXED_AFTER_PACKET_CONDITIONING=true
CANONICAL_ELL_IS_PROJECTIVE_ROOT_MODULUS=false
KCLEAN_DEFICIENCY_CREATES_MODULUS_AVERAGING=false
CROSS_KAPPA_MODULUS_AVERAGING_JUSTIFIED=false
```

---

## 4. Exact additive opening

For `Q=K_clean`,

```text
1_{t==rho*r (mod Q)}
=(1/Q) sum_{a mod Q} e_Q(a*(t-rho*r)).
```

The zero mode reproduces the deficient density term. Nonzero modes are initially linear additive phases. Because

```text
rho = signed Bdir*inverse(A)
```

or the reciprocal, averaging over the Gaussian direction exposes inverse-fraction phases, but not automatically a complete Kloosterman sum.

`(A,Bdir)` are two coordinates of the same Gaussian-prime direction and satisfy

```text
A^2+Bdir^2=2*ell*m.
```

They remain coupled to all cover and hyperbola masks.

```text
PROJECTIVE_LINE_ADDITIVE_OPENING_EXACT=true
KLOOSTERMAN_SUM_KERNEL_AUTOMATIC_AFTER_OPENING=false
MOVING_INVERSE_DIRECTION_PHASE_PRESENT=true
```

---

## 5. DFI-style prime-modulus quadratic-root dispersion

DFI varies the **prime modulus** of a fixed quadratic congruence. Here the prime factors of `K_clean` are fixed divisors of fixed `kappa`, while the moving prime is `ell` and the projective congruence is not modulo `ell`.

Averaging over `kappa` first would reverse the fixed-squareclass energy quantifier and simultaneously move the beta sign rule and coefficients.

```text
DFI_STYLE_DISPERSION_APPLICABLE=false
DFI_FAILURE_REASON=PRIME_MODULUS_AND_MOVING_PRIME_ARE_DIFFERENT_VARIABLES
```

---

## 6. Kuznetsov / Kloosterman bilinear forms

A valid Kuznetsov adapter would first have to produce weighted complete sums `S(m,n;c)` with a controlled modulus/level family. t76 has not done this.

Opening the projective line gives denominator `K_clean` fixed and an inverse in the moving direction coefficient. To complete it, one must simultaneously preserve

```text
canonical ell,
balanced primitive (r,t),
odd(r*t)=g*c/odd(h),
(R0,T0)=1,
short ellipse,
ell*g*c<2B,
ell*delta<=Y_U.
```

No exact completion separating those coefficients is proved. Therefore even recent critical-range Kloosterman power savings cannot be transferred.

```text
KUZNETSOV_KLOOSTERMAN_APPLICABLE=false
STANDARD_KLOOSTERMAN_MODULUS_FAMILY_EXHIBITED=false
BLOMER_PASCADI_CRITICAL_RANGE_SAVING_TRANSFERRED_TO_STAGE14=false
```

---

## 7. Spectral large sieve / exceptional Maass

Pascadi-type large sieves require a verified automorphic level and coefficient sequence, often with specific sparse Fourier-transform structure after dispersion.

Using `K_clean` as a level leaves moving Gaussian-direction and physical weights coupled; using `ell` as a level loses the actual projective modulus. No admissible spectral sequence has been derived.

```text
SPECTRAL_LARGE_SIEVE_APPLICABLE=false
EXCEPTIONAL_MAASS_SPARSE_FOURIER_SEQUENCE_VERIFIED=false
SPECTRAL_LEVEL_MATCHES_PROJECTIVE_MODULUS=false
```

---

## 8. Divisor switching + Cauchy / Poisson

This is formally legal preprocessing. Parameterize

```text
t=rho*r+j*K_clean.
```

In the deficient branch the `j` interval is long enough to open. But Poisson zero frequency recreates the large `R*T/K_clean` density. Any saving must therefore come from nonzero frequencies averaged over moving Gaussian directions.

After Cauchy, the weights still couple through

```text
rho(A,Bdir),
c/odd(h)=R0*T0,
delta=(r^2+t^2)/(2k),
ell*g*c<2B,
ell*delta<=Y_U.
```

No proved transform puts them into separated standard bilinear coefficients with a uniform fixed power saving.

```text
DIVISOR_SWITCHING_CAUCHY_POISSON_FORMALLY_AVAILABLE=true
DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_FIXED_POWER_SAVING_PROVED=false
```

---

## 9. Moving Gaussian-prime direction bilinear form

For fixed `U`,

```text
a+i*b=pi*U,
N(pi)=ell,
```

so `(A,Bdir)` is a fixed integral linear transform of Gaussian-prime coordinates. This makes Fouvry--Iwaniec Gaussian-prime technology structurally relevant.

But Stage14 needs a rational projective phase modulo growing composite `K_clean` plus all short-cover/hyperbola masks. t76 gives only

```text
K_clean<R*T*B^o(1),
```

not a uniform level-of-distribution bound relative to `ell` that covers every deficient packet.

```text
MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false
GAUSSIAN_PRIME_DIRECTION_STRUCTURE_RELEVANT=true
UNIFORM_KCLEAN_LEVEL_OF_DISTRIBUTION_RANGE_PROVED=false
```

---

## 10. K_clean deficiency and complementary-modulus tests

Deficiency itself yields no modulus averaging:

```text
KCLEAN_DEFICIENCY_ALONE_GIVES_TYPEII_POWER_SAVING=false
KCLEAN_DEFICIENCY_ALONE_GIVES_MODULUS_AVERAGING=false
```

Likewise

```text
ell*g*c<2B
```

is a size hyperbola, not a divisibility/conductor identity. It does not create `Q` with `K_clean*Q` dividing a determinant or phase conductor.

```text
ELL_G_C_HYPERBOLA_CREATES_COMPLEMENTARY_ARITHMETIC_MODULUS=false
CANONICAL_ELL_TRANSFERS_INTO_KCLEAN_ROOT_MODULUS=false
```

---

## 11. Full-mask survival

The fixed-beta sign rule is favorable and survives as fixed local orientation. Dyadic short-ellipse and hyperbola localizations cost only `B^o(1)`.

The obstruction is coefficient dependence:

```text
rho depends on moving Gaussian direction,
c depends on both cover columns,
delta depends on r^2+t^2,
ell couples to c and delta through distinct hyperbolas.
```

No factorization into theorem-ready one-variable coefficient sequences is proved.

```text
FIXED_BETA_SIGN_SURVIVES_DISPERSION_PREPROCESSING=true
DYADIC_SHORT_ELLIPSE_LOCALIZATION_COST=Bo1
DYADIC_HYPERBOLA_LOCALIZATION_COST=Bo1
FULL_PHYSICAL_WEIGHT_SEPARATES_INTO_STANDARD_BILINEAR_COEFFICIENTS=false
```

---

## 12. Applicability ledger

```text
DFI_STYLE_DISPERSION_APPLICABLE=false
KUZNETSOV_KLOOSTERMAN_APPLICABLE=false
SPECTRAL_LARGE_SIEVE_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false
MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false

OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false
CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT=0
```

This does not say dispersion cannot work after another exact reduction. It says no existing theorem has been legally adapted to the complete t76 packet.

---

## 13. Minimal remaining obstruction and preferred receiver

The minimal external analytic contract is more precise than a generic "Kloosterman bound":

```text
CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy
```

It must control the discrepancy of

```text
sum_{canonical Gaussian pi, N(pi)=ell}
 sum_{balanced primitive (r,t), all physical masks}
 w(pi,r,t)
 (1_{t==rho(pi)r mod K_clean}-expected_density)
```

uniformly throughout the deficient range while keeping fixed beta and the exact reconstructed masks.

```text
MINIMAL_REMAINING_OBSTRUCTION=CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy
PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedCleanKappaDeficientCanonicalGaussianPrimePrimitiveCoverTypeIIDispersionEnergy
```

---

## 14. tH22 decision

Do not open tH22 yet. t77 should first determine whether the discrepancy can be transformed into an actual standard Kloosterman/inverse-fraction or Gaussian-prime progression kernel.

```text
TH22_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH21=false
T_ROUTE_BLOCKED_AFTER_TH21=false
NEXT=Stage14-t77
```

---

## 15. Current shared exponent

While tH21 was being prepared, merged Stage14-s7-38 improved the whole-family theorem from `71/128` to

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112
```

by combining the X12 lost-core column divisor with the full Cayley-row core. tH21 proves no additional whole-family power saving.

```text
MERGED_S7_38_GLOBAL_61_112_LEDGER_IMPORTED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

---

## Locked boundary

```text
STAGE14_TH21=COMPLETE_BALANCED_CLEAN_KAPPA_CANONICAL_PRIME_PRIMITIVE_COVER_TYPEII_DISPERSION_APPLICABILITY_AUDIT
MERGED_T76_IMPORTED=true
MERGED_T75_IMPORTED=true
MERGED_T74_IMPORTED=true
MERGED_TH20_IMPORTED=true

T76_LARGE_CLEAN_KAPPA_BRANCH_REOPENED=false
T75_HIGH_IMBALANCE_BRANCH_REOPENED=false
T75_LARGE_G_BRANCH_REOPENED=false

PROJECTIVE_ROOTLINE_KERNEL_RETAINED=true
CANONICAL_ELL_MASK_RETAINED=true
SHORT_ELLIPSE_MASK_RETAINED=true
SHARP_ELL_G_C_HYPERBOLA_RETAINED=true
FIXED_BETA_ROOT_SIGN_RETAINED=true

DFI_STYLE_DISPERSION_APPLICABLE=false
KUZNETSOV_KLOOSTERMAN_APPLICABLE=false
SPECTRAL_LARGE_SIEVE_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_FORMALLY_AVAILABLE=true
MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false

KCLEAN_DEFICIENCY_ALONE_GIVES_MODULUS_AVERAGING=false
ELL_G_C_HYPERBOLA_CREATES_COMPLEMENTARY_ARITHMETIC_MODULUS=false
FULL_PHYSICAL_WEIGHT_SEPARATES_INTO_STANDARD_BILINEAR_COEFFICIENTS=false

OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false
CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT=0

MINIMAL_REMAINING_OBSTRUCTION=CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy
PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedCleanKappaDeficientCanonicalGaussianPrimePrimitiveCoverTypeIIDispersionEnergy

TH22_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-t77
```
