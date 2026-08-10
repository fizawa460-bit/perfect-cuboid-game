# Stage14-tH21 — balanced clean-kappa canonical-prime primitive-cover Type-II dispersion applicability audit

## Purpose

Independent audit target:

```text
SmallAngularGcdBalancedCleanKappaCanonicalPrimePrimitiveCoverTypeIIDispersion
```

This audit starts from latest main with merged Stage14-t76. It consumes only the live boundaries of merged t74, t75, tH20, and the fixed-tag/squareclass facts of t71--t73 needed by t76.

It does **not** reopen:

```text
Pell / class number / regulator,
canonical-largest-prime detection,
t74 fixed (ell,c) physical fibers,
t75 large-g branch,
t75 highly-unbalanced Type-I branch,
t76 large-clean-kappa root-line spacing.
```

The strict applicability criterion used here is the one requested by the user: a theorem is marked `APPLICABLE=true` only if its quantifier order, modulus, variable lengths, coefficient dependence, moving canonical prime, clean-kappa range, short ellipse, sharp hyperbolas, and fixed-beta sign orientation can all be retained through an explicit adapter. Similarity of vocabulary or dyadic ranges is not enough.

The conclusion is negative for every off-the-shelf Type-II theorem audited. The post-t76 packet is now precise enough to explain why: after the fixed packet is conditioned, the root-line modulus `K_clean` is essentially fixed, whereas the moving prime `ell` is a separate Gaussian-direction variable. Opening the projective congruence produces additive phases modulo `K_clean`; it does not automatically produce the modulus-average Kloosterman family required by DFI/Kuznetsov/spectral large-sieve theorems. A genuinely new weighted Gaussian-prime projective-root-line discrepancy estimate is still needed unless Stage14-t77 finds another exact reduction.

---

## 1. Exact imported t76 kernel

Fix the packet

```text
(U, epsilon, k, h, kappa, beta),
beta=gcd(kappa,v).
```

Write

```text
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p,
K=odd(kappa),
K_bad=gcd(K,g),
K_clean=K/K_bad.
```

(`Bdir` denotes the direction coordinate `b+a`; the global height parameter remains `B`.)

Merged t76 proves exactly

```text
K_bad=gcd(K,g),
gcd(K_clean,A*Bdir*r*t)=1,
K_clean < R*T*B^o(1),
t == rho*r (mod K_clean),
```

where `R,T` are the dyadic cover lengths and fixed `beta` determines the primewise sign of `rho`. The only remaining local direction choice is reciprocal:

```text
rho mod p in { signed Bdir/A, signed A/Bdir }
```

for each `p|K_clean`, hence

```text
# rho choices <= 2^omega(K_clean)=B^o(1).
```

The large branch

```text
K_clean >= R*T*B^(-o(1))
```

is already closed by elementary primitive projective root-line spacing and is not reconsidered.

```text
T76_LARGE_CLEAN_KAPPA_BRANCH_REOPENED=false
PROJECTIVE_ROOTLINE_KERNEL_RETAINED=true
FIXED_BETA_ROOT_SIGN_RETAINED=true
RECIPROCAL_DIRECTION_MULTIPLICITY=Bo1
```

---

## 2. Mandatory physical masks

The live block also retains simultaneously

```text
g small on its dyadic scale,
r,t balanced,
gcd(r,t) in {1,2},
r,t < sqrt(ell),
ell^2 > 4B,
ell*c < 2B,
ell*g*c < 2B,
h*ell*(r^2+t^2) <= 4B,
ell*delta <= Y_U,
c/odd(h)=R0*T0,
gcd(R0,T0)=1,
ell is the canonical Gaussian direction prime.
```

These are not optional weights. In particular `c`, `delta`, `g`, `r`, `t`, and the Gaussian direction are reconstructed from the same physical state, so savings from their hyperbolas cannot be multiplied as independent events.

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

## 3. Quantifier order after all legal conditioning

The order matters.

1. Fix `(U,epsilon,k,h,kappa,beta)`.
2. Dyadically localize `g,ell,r,t,c,delta`; this costs `B^o(1)`.
3. Since `K` is fixed and `K_bad=gcd(K,g)` is a divisor of `K`, condition on `K_bad` and therefore on `K_clean`; this costs at most `tau(K)=B^o(1)`.
4. Fix one of the `B^o(1)` reciprocal root orientations.
5. Sum the moving canonical Gaussian direction prime `ell` / Gaussian prime `pi`, which determines `(A,Bdir)` for fixed `U`.
6. Sum balanced primitive covers `(r,t)` satisfying the projective line and all reconstructed physical masks.

Thus within one analytic packet the root modulus `K_clean` is **fixed**, not averaged over a long modulus interval. The moving prime `ell` is not the modulus in

```text
t == rho*r (mod K_clean).
```

This is the first decisive adapter constraint.

```text
KCLEAN_EFFECTIVELY_FIXED_AFTER_PACKET_CONDITIONING=true
CANONICAL_ELL_IS_PROJECTIVE_ROOT_MODULUS=false
KCLEAN_DEFICIENCY_CREATES_MODULUS_AVERAGING=false
```

---

## 4. Opening the projective root line

For fixed `Q=K_clean`, additive orthogonality gives the exact identity

```text
1_{t == rho*r (mod Q)}
 = (1/Q) * sum_{a mod Q} e_Q(a*(t-rho*r)).
```

The zero frequency gives the expected density term. The nonzero frequencies are initially only **linear additive phases** modulo `Q`.

If `rho` were fixed independently of the Gaussian direction, the `r,t` sums would be ordinary incomplete additive sums, not Kloosterman sums. Here `rho` moves with the direction through

```text
rho = signed Bdir * inverse(A) (mod Q)
```

or its reciprocal. Therefore averaging over the direction can expose a Kloosterman-*fraction-like* phase such as

```text
e_Q(a*r*Bdir*inverse(A)).
```

But this observation is not yet a Kuznetsov adapter: `(A,Bdir)` are the two coordinates of one Gaussian-prime direction with

```text
A^2+Bdir^2=2*ell*m,
```

and they remain coupled to `ell`, `c`, `delta`, the short ellipse, and the sharp hyperbolas. No independent complete sum over `A mod Q` or over moduli `Q` has been produced.

```text
PROJECTIVE_LINE_ADDITIVE_OPENING_EXACT=true
KLOOSTERMAN_SUM_KERNEL_AUTOMATIC_AFTER_OPENING=false
MOVING_INVERSE_DIRECTION_PHASE_PRESENT=true
```

---

## 5. DFI-style quadratic-root / prime-modulus dispersion

The Duke--Friedlander--Iwaniec prime-modulus root theorem concerns roots of a fixed quadratic congruence as the **prime modulus varies**. That is not the t76 quantifier order.

Here:

```text
root modulus = K_clean | odd(kappa),
K_clean fixed after fixed-kappa conditioning,
canonical moving prime = ell,
ell is not the root modulus,
rho depends on the moving Gaussian direction (A,Bdir).
```

Attempting to use the prime divisors `p|K_clean` as DFI moduli also fails to create the required average: those primes are fixed divisors of the fixed squareclass packet. Attempting to use `ell` as the varying prime fails because the congruence is not modulo `ell`.

Averaging over `kappa` before applying DFI would reverse the fixed-squareclass energy quantifier and would also move the beta sign rule and the physical coefficient system. No theorem adapter justifying that interchange is available.

Therefore

```text
DFI_STYLE_DISPERSION_APPLICABLE=false
DFI_FAILURE_REASON=PRIME_MODULUS_AND_MOVING_PRIME_ARE_DIFFERENT_VARIABLES
```

---

## 6. Kuznetsov / Kloosterman bilinear forms

Classical Deshouillers--Iwaniec/Kuznetsov estimates apply after a problem has been transformed into weighted sums of Kloosterman sums

```text
S(m,n;c)
```

with an admissible modulus/level family and coefficient sequences whose dependence on the level variables is controlled.

The t76 opening in Section 4 does not give this. Its denominator is the fixed `Q=K_clean`, and the inverse appears in the **moving Gaussian direction coefficient** `Bdir/A`, not as the complete Kloosterman variable summed modulo a varying `c`.

To create a standard Kloosterman sum one would need an additional completion/dispersion step that simultaneously:

```text
- completes the Gaussian-prime direction modulo Q,
- separates the cover coefficients from the direction coefficients,
- preserves ell canonical-prime support,
- preserves r,t balance and gcd(r,t)<=2,
- preserves odd(r*t)=g*c/H and (R0,T0)=1,
- preserves h*ell*(r^2+t^2)<=4B,
- preserves ell*g*c<2B and ell*delta<=Y_U.
```

No such exact adapter is currently proved.

The recent Blomer--Pascadi bilinear Kloosterman theorem gives a genuine power saving in its own critical Kloosterman range, but range similarity is insufficient: t76 has not produced the required Kloosterman bilinear form.

```text
KUZNETSOV_KLOOSTERMAN_APPLICABLE=false
STANDARD_KLOOSTERMAN_MODULUS_FAMILY_EXHIBITED=false
BLOMER_PASCADI_CRITICAL_RANGE_SAVING_TRANSFERRED_TO_STAGE14=false
```

---

## 7. Spectral large sieve / exceptional Maass estimates

Pascadi's large-sieve results are designed for automorphic Fourier coefficients at a level `q` and, in applications, for coefficient sequences with special sparse Fourier-transform structure arising after a successful dispersion/Kuznetsov reduction.

No such spectral sequence has yet been identified here. Setting the automorphic level equal to `K_clean` is not enough: after packet conditioning that level is fixed, while the coefficients still contain moving Gaussian-prime direction data and the coupled short-cover/hyperbola masks. Conversely making a level out of `ell`, `g`, or `c` does not preserve the actual projective congruence modulus.

Hence the exceptional-spectrum technology cannot be invoked before a valid Kuznetsov adapter exists.

```text
SPECTRAL_LARGE_SIEVE_APPLICABLE=false
EXCEPTIONAL_MAASS_SPARSE_FOURIER_SEQUENCE_VERIFIED=false
SPECTRAL_LEVEL_MATCHES_PROJECTIVE_MODULUS=false
```

---

## 8. Divisor switching + Cauchy / Poisson on one cover column

This route is algebraically legitimate as a **preprocessing method**, but it does not presently constitute a uniform power-saving theorem adapter.

For example parameterizing the projective line by

```text
t = rho*r + j*K_clean
```

leaves a `j`-interval of length roughly `T/K_clean` on the deficient branch. One may smooth the short ellipse and apply Cauchy/Poisson to `j` or to one cover column.

However:

1. the zero frequency reproduces the large density term `R*T/K_clean` that caused the deficient branch;
2. to beat that term one must average nonzero frequencies over moving directions/`ell`;
3. the phase coefficient `rho` depends on `(A,Bdir)`;
4. `c/H=R0*T0`, the coprimality of `R0,T0`, and `delta=(r^2+t^2)/(2k)` couple the two cover columns to the same `ell`;
5. the sharp `ell*g*c` and `ell*delta` cutoffs therefore remain coefficient-dependent after Cauchy.

No Poisson transform has been shown to convert these weights into a standard independent bilinear coefficient system with a fixed power saving.

Under the strict `APPLICABLE` convention of this audit:

```text
DIVISOR_SWITCHING_CAUCHY_POISSON_FORMALLY_AVAILABLE=true
DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_FIXED_POWER_SAVING_PROVED=false
```

---

## 9. Moving Gaussian-prime direction coefficient

The direction is not an arbitrary primitive pair. For fixed `U`,

```text
a+i*b = pi*U,
N(pi)=ell,
A=b-a,
Bdir=b+a,
```

so `(A,Bdir)` is a fixed integral linear transform of the Gaussian-prime coordinates of `pi`.

This structure is potentially useful. Fouvry--Iwaniec-type Gaussian-prime bilinear technology is therefore relevant in spirit. But the present coefficient is a rational projective function modulo the growing composite `K_clean`, while the same `ell` is simultaneously constrained by

```text
ell*c<2B,
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U.
```

No located Gaussian-prime theorem supplies a uniform estimate for this weighted rational-direction phase for every deficient `K_clean` range. In particular, t76 only gives

```text
K_clean < R*T*B^o(1),
```

not a level-of-distribution bound such as `K_clean <= ell^(1/2-epsilon)` that would place every packet in a classical prime-distribution range.

Therefore

```text
MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false
GAUSSIAN_PRIME_DIRECTION_STRUCTURE_RELEVANT=true
UNIFORM_KCLEAN_LEVEL_OF_DISTRIBUTION_RANGE_PROVED=false
```

---

## 10. Does K_clean-deficiency itself create enough averaging?

No.

`K_clean < R*T*B^o(1)` is a statement that elementary spacing is insufficient. It supplies **more points per residue line**, not more moduli. Since `K_clean` is fixed after conditioning on the fixed `kappa` packet and `K_bad`, the deficient condition cannot be converted into a Deshouillers--Iwaniec style modulus average.

Across different squareclasses there are many possible `K_clean`, but summing them before controlling one fixed-squareclass energy changes the quantifier order and moves the beta sign orientation and coefficients. There is no legal cross-kappa averaging theorem presently available.

```text
KCLEAN_DEFICIENCY_ALONE_GIVES_TYPEII_POWER_SAVING=false
KCLEAN_DEFICIENCY_ALONE_GIVES_MODULUS_AVERAGING=false
CROSS_KAPPA_MODULUS_AVERAGING_JUSTIFIED=false
```

---

## 11. Can canonical ell and ell*g*c<2B create a complementary modulus?

The inequality

```text
ell*g*c<2B
```

is a sharp size hyperbola. It does not imply a divisibility relation of the form

```text
K_clean * Q | determinant
```

or an exact conductor factorization linking `ell` to the projective root modulus. Merged t68 already guards against transferring a state-local canonical prime into an unrelated cross determinant; t74--t76 do not introduce a new such divisibility.

One may define numerical complementary *lengths* such as `B/(ell*g*c)`, but they are not arithmetic moduli and cannot be fed to a Kloosterman/spectral theorem as conductors.

```text
ELL_G_C_HYPERBOLA_CREATES_COMPLEMENTARY_ARITHMETIC_MODULUS=false
CANONICAL_ELL_TRANSFERS_INTO_KCLEAN_ROOT_MODULUS=false
```

---

## 12. Full-mask survival under a hypothetical dispersion step

The fixed-beta sign rule is favorable: after conditioning it removes sign entropy at `B^o(1)` cost and can be carried as a fixed root orientation.

Dyadic versions of the size inequalities are also harmless *as localizations*. The real problem is variable dependence, not smoothness:

```text
rho depends on moving Gaussian direction,
c depends on both cover columns after angular cancellation,
delta depends on r^2+t^2,
ell couples to both c and delta through distinct hyperbolas.
```

Thus a theorem that accepts arbitrary bounded coefficients in `r` and `t` separately is still insufficient unless the physical weight factors into admissible one-variable coefficients or its coupled part is controlled after Cauchy. No such factorization has been proved.

```text
FIXED_BETA_SIGN_SURVIVES_DISPERSION_PREPROCESSING=true
DYADIC_SHORT_ELLIPSE_LOCALIZATION_COST=Bo1
DYADIC_HYPERBOLA_LOCALIZATION_COST=Bo1
FULL_PHYSICAL_WEIGHT_SEPARATES_INTO_STANDARD_BILINEAR_COEFFICIENTS=false
```

---

## 13. Candidate theorem ledger

| Candidate | Quantifier/modulus match | Full masks preserved by proved adapter | Uniform fixed `B`-power saving |
|---|---:|---:|---:|
| DFI quadratic-root / prime-modulus dispersion | no | no | no |
| Kuznetsov / Kloosterman bilinear forms | no Kloosterman family yet | no | no |
| spectral large sieve / exceptional Maass | no spectral level/sequence adapter | no | no |
| divisor switch + Cauchy / Poisson | preprocessing only | masks can be retained before transform | no proved post-transform adapter |
| moving Gaussian-prime bilinear technology | structurally relevant | no | no |
| K_clean-deficiency averaging | no modulus average | yes as a condition | no |
| complementary modulus from `ell*g*c` | no arithmetic modulus | yes as size mask | no |

Therefore

```text
DFI_STYLE_DISPERSION_APPLICABLE=false
KUZNETSOV_KLOOSTERMAN_APPLICABLE=false
SPECTRAL_LARGE_SIEVE_APPLICABLE=false
DIVISOR_SWITCHING_CAUCHY_POISSON_APPLICABLE=false
MOVING_GAUSSIAN_PRIME_BILINEAR_APPLICABLE=false

OFF_THE_SHELF_TYPEII_POWER_SAVING_PROVED=false
CERTIFIED_TYPEII_B_POWER_SAVING_EXPONENT=0
```

No positive exponent from an external Type-II theorem is promoted into the Stage14 ledger.

---

## 14. Minimal remaining analytic obstruction

The exact missing statement is not simply "a Kloosterman bound". Before any spectral theorem can be invoked, one needs a weighted discrepancy theorem for the **fixed clean-kappa projective modulus with moving Gaussian-prime direction coefficient**.

A natural contract is:

```text
CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy
```

schematically controlling, on every legal dyadic packet,

```text
sum_{canonical Gaussian pi, N(pi)=ell~L}
  sum_{r~R,t~T, physical masks}
  w(pi,r,t)
  * ( 1_{t=rho(pi)r mod K_clean} - expected_density )
```

with a fixed power saving uniformly for

```text
K_clean < R*T*B^o(1)
```

and with the exact t76 fixed-beta orientation and all t74/t75 masks retained.

If an exact Cauchy/Poisson reduction in t77 turns this discrepancy into a standard Kloosterman family, then the preferred theorem can be renamed at that later boundary. At tH21 that conversion is not proved.

```text
MINIMAL_REMAINING_OBSTRUCTION=CanonicalGaussianPrimeWeightedCleanKappaProjectiveRootLineDiscrepancy
PREFERRED_RECEIVER=SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedCleanKappaDeficientCanonicalGaussianPrimePrimitiveCoverTypeIIDispersionEnergy
```

---

## 15. tH22 decision

No tH22 should be opened yet.

The external-theorem audit has reached the point where the missing object is a bespoke discrepancy kernel, but Stage14-t77 is specifically tasked to continue exact reduction of the deficient-modulus branch. A further auxiliary audit would be premature until t77 either

```text
- produces a genuine Kloosterman/Kuznetsov kernel,
- produces a Gaussian-prime progression theorem with a verified modulus range,
- or isolates another standard bilinear form with separated coefficients.
```

```text
TH22_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH21=false
T_ROUTE_BLOCKED_AFTER_TH21=false
NEXT=Stage14-t77
```

---

## 16. Current shared exponent

Latest main also contains merged Stage14-X12, which improves the whole-family theorem to

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128
```

from the previous `19/34`. tH21 is only an applicability audit and proves no new global exponent.

```text
MERGED_X12_GLOBAL_71_128_LEDGER_IMPORTED=true
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
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-t77
```
