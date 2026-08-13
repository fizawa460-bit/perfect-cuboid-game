# Stage14-tH20 — canonical-prime short angular-cofactor hyperbola sieve applicability audit

## Purpose

Independent audit target:

```text
SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
```

This consumes merged Stage14-t74 plus the necessary t65--t73/tH19 boundary. It does not reopen generic Pell counts, fixed-norm Pell orbits, class numbers, regulators, unit-orbit polynomial losses, denominator-tag orientation enumeration, `kappa=1` Pell theory, or fixed `(kappa,beta,Pminus)` fibers.

Main conclusion:

```text
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_DIRECT_EXTERNAL_SIEVE_B_POWER_SAVING_EXPONENT=0
```

After t74, largest-prime/friable norm-value sieve is no longer minimal. Canonical `ell` is already a physical prime coordinate, exponent one is structural, and the moving cofactor is an explicitly short angular product.

---

## 1. Exact post-t74 packet

Condition on

```text
U, epsilon, k, h,
small squarefree kappa band,
beta=gcd(kappa,v).
```

Write

```text
H=odd(h),
D=odd(delta),
D_pi=b^2-a^2,
D_V=q^2-p^2,
g=gcd(odd(D_pi),odd(D_V)),
R_pi=odd(D_pi)/g,
R_V=odd(D_V)/g.
```

Merged t74 gives

```text
c=odd(Pminus/ell)=H*R_V,
odd(Pplus)=D*R_pi,
ell=LPF_odd(Pplus*Pminus),
v_ell(Pminus)=1.
```

The live physical inequalities are

```text
ell prime,
ell^2>4B,
c<sqrt(B),
2c<ell,
ell*c<2B,
ell*g*c<2B,
ell*delta<=Y_U.
```

Set

```text
r=q-p,
t=q+p.
```

Then exactly

```text
D_V=r*t,
gcd(r,t)|2,
r,t<sqrt(ell),
h*ell*(r^2+t^2)<=4B,
odd(r*t)=g*c/H.
```

Also

```text
fixed (U,epsilon,k,h,ell,c) physical fiber = B^o(1),
fixed (U,epsilon,k,h,kappa,beta,ell,c) physical fiber = B^o(1).
```

Thus the minimal problem is the distribution/energy of admissible `(ell,c)` together with a short primitive cover factorization.

---

## 2. Largest-prime-factor sieve is nonminimal

Before t74, a Buchstab/Harman formulation of

```text
odd(Pminus)=ell*c,
2c<ell,
P+(odd(Pplus))<ell
```

was natural.

After t74:

- `ell` is already the canonical Gaussian direction prime;
- it has two local real-quadratic root/prime-ideal hosts, costing `O(1)`;
- exponent one is structural;
- fixed `(ell,c)` reconstructs `Pplus`, `delta`, and all remaining predicates at `B^o(1)` cost.

Hence detecting the largest prime factor of `Pminus` attacks a solved coordinate.

```text
CANONICAL_LPF_SIEVE_POST_T74_MINIMAL=false
EXPONENT_ONE_SIEVE_POST_T74_MINIMAL=false
PRIME_IDEAL_HOST_FIXING_COST=O1
```

---

## 3. Binary quadratic / norm-form sieve

The t73 identities

```text
eta*Pplus = beta*w^2+alpha*u^2,
eta*Pminus= beta*w^2-alpha*u^2,
alpha*beta=kappa
```

remain valid, so binary norm-form sieve language is formally available.

But t74 proves that moving norm values have no independent fixed-power entropy after `(ell,c)` is fixed. Replacing the live receiver by generic quadratic-value sieve discards the stronger angular data

```text
odd(r*t)=g*c/H,
r,t<sqrt(ell),
h*ell*(r^2+t^2)<=4B.
```

Therefore:

```text
BINARY_QUADRATIC_NORM_FORM_SIEVE_FORMALLY_AVAILABLE=true
BINARY_QUADRATIC_NORM_FORM_SIEVE_POST_T74_MINIMAL=false
BINARY_QUADRATIC_NORM_FORM_SIEVE_DIRECT_IMPORT_VALID=false
```

---

## 4. Buchstab / Harman / beta sieve

Buchstab and Harman decompositions remain formally compatible with reconstructed `Pplus*Pminus`, but they are not minimal coordinates post-t74.

A beta/linear sieve supplies prime-density/logarithmic thinning, but primality plus

```text
2c<ell,
ell*c<2B
```

does not itself force a positive fixed `B`-power saving.

```text
BUCHSTAB_POST_T74_FORMALLY_COMPATIBLE=true
HARMAN_POST_T74_FORMALLY_COMPATIBLE=true
BUCHSTAB_HARMAN_POST_T74_MINIMAL=false
BETA_SIEVE_POST_T74_FIXED_POWER_SAVING_PROVED=false
```

Greatest-prime-factor theorems for one-variable quadratic polynomials are analogues of the superseded pre-t74 formulation, not direct theorems for the current receiver.

---

## 5. Divisor switching is directly useful

The exact relation

```text
odd(r*t)=g*c/H,
gcd(r,t)|2
```

makes divisor switching natural after t74.

Fixing `g,c` fixes the odd part of `r*t`; fixing one short factor restricts the other by a divisor relation and by

```text
h*ell*(r^2+t^2)<=4B.
```

Therefore the t74 split is analytically correct:

```text
large g        -> exploit ell*g*c<2B
balanced r,t   -> exploit short ellipse + primitive factorization
unbalanced r,t -> divisor-switch on the shorter factor
```

This is stronger than divisor switching on `Pminus=ell*c`, because it retains the physical angular product.

```text
ANGULAR_SHORT_FACTOR_DIVISOR_SWITCHING_VALID=true
ANGULAR_DIVISOR_SWITCHING_POST_T74_PREFERRED=true
DIVISOR_SWITCHING_ALONE_UNIFORM_FIXED_POWER_SAVING_PROVED=false
```

---

## 6. Friable-value theory

Generic friable-value theory is no longer close to minimal.

`c` is not merely an `ell`-smooth number; it satisfies

```text
c=H*R_V,
odd(r*t)=g*c/H,
r,t<sqrt(ell),
```

and the positive companion has no independent fixed-power entropy after `(ell,c)`.

```text
FRIABLE_VALUE_THEORY_POST_T74_MINIMAL=false
FRIABLE_VALUE_THEORY_DIRECTLY_CLOSES_SHORT_COFACTOR_RECEIVER=false
```

Binary-form friability results remain useful only as a warning that smoothness alone is not a universal power-sparsity mechanism.

---

## 7. Primitive-divisor / Lucas-Pell input

This is decisively nonminimal after t74. t73 already closes fixed-norm unit-orbit multiplicity, and t74 removes the moving negative norm value as an independent variable.

```text
PRIMITIVE_DIVISOR_LUCAS_PELL_POST_T74_DIRECT_ROUTE_VALID=false
```

---

## 8. Prime-ideal host

The canonical root condition chooses one of two conjugate split-prime hosts in `Q(sqrt(kappa))`. Merged t74 proves exactly two local hosts and exponent one.

This is valid notation/bookkeeping at `O(1)` cost; it does not save a fixed power.

```text
CANONICAL_ELL_PRIME_IDEAL_HOST_VALID=true
CANONICAL_ELL_PRIME_IDEAL_HOST_COST=O1
CANONICAL_ELL_PRIME_IDEAL_HOST_FIXED_POWER_SAVING=false
```

---

## 9. Quadratic-root and represented-prime theorems

Theorems on equidistribution of quadratic roots to prime moduli, primes represented by binary quadratic forms, and prime values of binary forms with a thin variable each address one isolated component.

None of the located theorems simultaneously keeps

```text
odd(r*t)=g*c/H,
r,t<sqrt(ell),
h*ell*(r^2+t^2)<=4B,
ell*c<2B,
ell*g*c<2B,
ell*delta<=Y_U,
fixed kappa,beta reconstruction.
```

Hence

```text
DFI_QUADRATIC_ROOT_EQUIDISTRIBUTION_DIRECT_IMPORT_VALID=false
BINARY_QUADRATIC_REPRESENTED_PRIME_DIRECT_IMPORT_VALID=false
THIN_VARIABLE_BINARY_QUADRATIC_PRIME_DIRECT_IMPORT_VALID=false
```

---

## 10. Bilinear forms / dispersion

A bilinear or dispersion estimate remains a plausible future ingredient, but the post-t74 variables differ from the pre-t74 two-companion Type-II problem.

Natural future sums have canonical prime `ell` coupled to short primitive factors `(r,t)` and possibly `g`, under

```text
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
odd(r*t)=g*c/H.
```

No identity currently transforms this into a standard Kloosterman bilinear form, a standard primes-in-progressions dispersion sum, or a standard binary-form prime-value sequence.

Modern Kloosterman/exceptional-Maass large-sieve results therefore cannot be imported from range similarity alone.

A possible stronger future theorem is

```text
CanonicalPrimeShortPrimitiveCoverBilinearDispersion.
```

It is not yet certified as minimal, because t75 still has unused elementary `g` and balanced/unbalanced factor geometry.

```text
POST_T74_BILINEAR_DISPERSION_PLAUSIBLE=true
POST_T74_STANDARD_DISPERSION_DIRECT_IMPORT_VALID=false
POST_T74_KLOOSTERMAN_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
CANONICAL_PRIME_SHORT_PRIMITIVE_COVER_BILINEAR_DISPERSION_PROVED=false
```

---

## 11. Sharp hyperbolas must remain joint

Retain simultaneously

```text
ell*c<2B,
ell*g*c<2B,
ell*delta<=Y_U.
```

Dyadic localization of `ell,c,g,delta` costs only `B^o(1)`. It is not valid to replace them by independent marginal bounds and multiply separate savings, because all variables come from the same physical state.

```text
SHARP_ELL_C_HYPERBOLA_RETAINED=true
SHARP_ELL_G_C_HYPERBOLA_RETAINED=true
SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
JOINT_HYPERBOLA_DYADIC_COST=Bo1
INDEPENDENT_HYPERBOLA_SAVINGS_MULTIPLIABLE=false
```

---

## 12. Candidate-technique verdict

| Candidate | Post-t74 applicability | Direct fixed-power closure? |
|---|---|---:|
| binary quadratic / norm-form sieve | formally valid, nonminimal | no |
| largest-prime-factor sieve | superseded by canonical `ell` | no |
| Buchstab / Harman | formally valid, nonminimal | no |
| beta sieve | local/logarithmic | no |
| bilinear forms / dispersion | plausible after t75 splits | no direct theorem |
| divisor switching | **directly useful** on `r,t` | no alone |
| friable-value estimates | nonminimal | no |
| primitive-divisor / Lucas-Pell | superseded | no |
| prescribed-largest-prime quadratic values | wrong minimal coordinates | no direct import |
| prime-ideal canonical host | exact `O(1)` bookkeeping | no |
| sharp hyperbola averaging | mandatory | still coupled |
| simultaneous `P+`,`P-` norm sieve | superseded by fixed `(ell,c)` reconstruction | nonminimal |

---

## 13. Exponent audit

From external sieve/dispersion theorems that directly match the complete post-t74 receiver,

```text
CERTIFIED_DIRECT_EXTERNAL_SIEVE_B_POWER_SAVING_EXPONENT=0
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
```

This allows logarithmic thinning and does not rule out a power saving after further exact reduction.

The current strongest merged whole-family theorem is Stage14-s7-36:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16
```

This improves the previously merged `4/7`; tH20 itself proves no new global exponent.

```text
MERGED_S7_36_GLOBAL_9_16_LEDGER_IMPORTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16
TH20_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
```

---

## 14. Superseded pre-t74 target

For the pre-t74 t73 receiver, a natural sufficient theorem would have been

```text
FixedTagCanonicalLargestPrimeSharpHyperbolaTwoCompanionNormValueTypeIIDispersion.
```

Merged t74 proves it is not minimal because fixed `(ell,c)` reconstructs the physical state with `B^o(1)` multiplicity and restores the short angular factorization.

```text
PRE_T74_MOVING_NORM_VALUE_SIEVE_AUDITED=true
PRE_T74_TWO_COMPANION_TYPEII_FORMULATION_VALID_AS_SUFFICIENT=true
PRE_T74_TWO_COMPANION_TYPEII_IS_MINIMAL=false
TH20_CURRENT_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
```

---

## 15. Supervisor decision

No tH21 is needed now. The correct next step is Stage14-t75's elementary split on `g` and the balance of `(r,t)`. Only if a genuinely irreducible balanced prime/short-cover bilinear sum survives should a new auxiliary theorem audit be opened.

```text
TH21_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
T_ROUTE_BLOCKED_AFTER_TH20=false
NEXT=Stage14-t75
```

---

## Locked boundary

```text
STAGE14_TH20=COMPLETE_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_SIEVE_APPLICABILITY_AUDIT
MERGED_T74_IMPORTED=true
TH20_CURRENT_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
T65_T74_PHYSICAL_FILTERS_RETAINED=true
TH19_CONSUMED=true

GENERIC_PELL_SOLUTION_COUNT_REOPENED=false
FIXED_NORM_PELL_ORBIT_MULTIPLICITY_REOPENED=false
CLASS_NUMBER_REOPENED=false
REGULATOR_REOPENED=false
UNIT_ORBIT_POLYNOMIAL_LOSS_REOPENED=false
DENOMINATOR_TAG_ORIENTATION_ENUMERATION_REOPENED=false
KAPPA_ONE_PELL_THEORY_REOPENED=false
FIXED_KAPPA_BETA_PMINUS_FIBER_REOPENED=false

CANONICAL_LPF_SIEVE_POST_T74_MINIMAL=false
EXPONENT_ONE_SIEVE_POST_T74_MINIMAL=false
BINARY_QUADRATIC_NORM_FORM_SIEVE_POST_T74_MINIMAL=false
BUCHSTAB_HARMAN_POST_T74_MINIMAL=false
FRIABLE_VALUE_THEORY_POST_T74_MINIMAL=false
PRIMITIVE_DIVISOR_LUCAS_PELL_POST_T74_DIRECT_ROUTE_VALID=false

CANONICAL_ELL_PRIME_IDEAL_HOST_VALID=true
CANONICAL_ELL_PRIME_IDEAL_HOST_COST=O1
ANGULAR_SHORT_FACTOR_DIVISOR_SWITCHING_VALID=true
ANGULAR_DIVISOR_SWITCHING_POST_T74_PREFERRED=true

SHARP_ELL_C_HYPERBOLA_RETAINED=true
SHARP_ELL_G_C_HYPERBOLA_RETAINED=true
SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
JOINT_HYPERBOLA_DYADIC_COST=Bo1

POST_T74_BILINEAR_DISPERSION_PLAUSIBLE=true
POST_T74_STANDARD_DISPERSION_DIRECT_IMPORT_VALID=false
POST_T74_KLOOSTERMAN_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
CANONICAL_PRIME_SHORT_PRIMITIVE_COVER_BILINEAR_DISPERSION_PROVED=false

PRE_T74_TWO_COMPANION_TYPEII_IS_MINIMAL=false
CERTIFIED_DIRECT_EXTERNAL_SIEVE_B_POWER_SAVING_EXPONENT=0
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_ENERGY_PROVED=false

MERGED_S7_36_GLOBAL_9_16_LEDGER_IMPORTED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=9/16
TH20_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false

TH21_NEEDED=false
T_ROUTE_BLOCKED_AFTER_TH20=false
NEXT=Stage14-t75
```
