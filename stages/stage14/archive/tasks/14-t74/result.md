# Stage14-t74 — canonical host orientation, ell-free cofactor balance, and short angular-cover reduction

## Purpose

Merged t73 proves that fixed `(U,kappa,beta,P_-)` norm fibers are uniformly `B^{o(1)}`.  Stage14-t74 removes the remaining moving norm value as an independent variable and returns it to the original physical angular variables.

For the dominant invisible packet

```text
N(U)=m,
N(V)=n=k*delta,
h*k=epsilon*m,
a^2+b^2=ell*m,
p^2+q^2=k*delta,
ell^2>4B,
epsilon*ell*m*delta<=2B.
```

Write

```text
D_pi=b^2-a^2,
D_V=q^2-p^2,
H=odd(h),
D=odd(delta),
g=gcd(odd(D_pi),odd(D_V)),
R_pi=odd(D_pi)/g,
R_V=odd(D_V)/g.
```

For the reduced Cayley pair

```text
P+=(v^2+kappa*u^2)/G,
P-=(v^2-kappa*u^2)/G,
s=kappa*(u/v)^2,
```

merged t69 gives

```text
odd(P+)=D*R_pi,
odd(P-)=ell*H*R_V,
ell=LPF_odd(P+*P-),
v_ell(P-)=1.
```

No new whole-family saving is claimed by t74.

---

## 1. Canonical `ell` has only two local hosts

Because `ell|P-` and `ell` is coprime to `kappa*u*v`,

```text
rho_ell = v/u (mod ell)
rho_ell^2 = kappa (mod ell).
```

Thus `ell` has exactly two local root orientations `±rho_ell`.  Equivalently the norm element lies on one of the two conjugate split-prime hosts in `Q(sqrt(kappa))`.  Since `v_ell(P-)=1`, the selected host occurs exactly once.

```text
CANONICAL_ELL_TWO_ROOT_HOST_ORIENTATIONS_PROVED=true
CANONICAL_ELL_HOST_ORIENTATION_COST=O1
CANONICAL_ELL_HOST_EXPONENT_ONE=true
```

No class-number or principality assertion is used.

---

## 2. Exact cancellation of `ell` from the Cayley balance

Merged t65 gives

```text
P+/P- = epsilon*delta*D_pi/(ell*h*D_V).
```

Put

```text
Q=P-/ell.
```

Since the exponent of `ell` is exactly one, cross multiplication and exact cancellation give

```text
boxed:
h*D_V*P+ = epsilon*delta*D_pi*Q.                 (74.1)
```

The residual balance contains no canonical prime.

On odd parts,

```text
boxed:
c:=odd(Q)=H*R_V.                                 (74.2)
```

Also

```text
odd(P+)=D*R_pi,
gcd(odd(P+),c)=1.
```

Therefore the post-t73 moving negative norm value is `ell` times a short physical angular cofactor; its canonical prime factor is not an additional moving smooth-value variable.

```text
CANONICAL_ELL_CANCELS_EXACTLY_FROM_CAYLEY_BALANCE=true
ELL_FREE_RESIDUAL_COFACTOR_BALANCE_PROVED=true
ODD_PMINUS_OVER_ELL_EQUALS_H_TIMES_RV=true
POSITIVE_NEGATIVE_ODD_COMPANIONS_COPRIME=true
```

---

## 3. New short-cofactor hyperbolas

Merged t65 gives

```text
c < epsilon*m*delta,
2c < ell.
```

Combining the first inequality with the physical budget gives

```text
boxed:
ell*c < 2B.                                      (74.3)
```

Since `ell>2*sqrt(B)`,

```text
boxed:
c < sqrt(B).                                     (74.4)
```

Retaining the angular cancellation is stronger.  Since

```text
odd(D_V)=g*R_V=g*c/H < k*delta,
```

we have

```text
g*c < H*k*delta <= h*k*delta=epsilon*m*delta,
```

hence

```text
boxed:
ell*g*c < 2B.                                    (74.5)
```

The old sharp `ell*delta<=Y_U` hyperbola remains simultaneously valid and is not replaced by (74.3) or (74.5).

```text
SHARP_ELL_C_HYPERBOLA_PROVED=true
SHARP_ELL_G_C_HYPERBOLA_PROVED=true
CANONICAL_ODD_COFACTOR_LT_SQRT_B=true
```

---

## 4. The cover deficit is a product of two `sqrt(ell)`-short linear factors

Put

```text
r=q-p,
t=q+p.
```

Then

```text
D_V=r*t,
r^2+t^2=2*(p^2+q^2)=2*k*delta,
gcd(r,t)|2.
```

Merged t65 gives `ell>2n=2k*delta`.  Therefore

```text
0<r<t,
t^2<2n<ell,
boxed: r,t<sqrt(ell).                              (74.6)
```

The physical budget becomes the exact short ellipse

```text
boxed:
h*ell*(r^2+t^2)<=4B.                              (74.7)
```

and (74.2) is equivalent to

```text
boxed:
odd(r*t)=g*c/H.                                    (74.8)
```

Thus the negative cofactor is, up to a direction divisor and a 2-adic factor, the product of two essentially coprime short linear factors on the physical ellipse.

```text
COVER_DEFICIT_LINEAR_FACTORIZATION_RESTORED=true
COVER_LINEAR_FACTORS_LT_SQRT_ELL=true
SHORT_COVER_ELLIPSE_PROVED=true
```

---

## 5. Fixed `(ell,c)` physical fiber is `B^{o(1)}`

Fix

```text
(U,epsilon,k,h,ell,c).
```

Optional fixed `(kappa,beta)` conditions only shrink the fiber.

1. `a+ib=pi*U`, `N(pi)=ell`; a rational split prime `ell` has only `O(1)` Gaussian prime associates/conjugates, hence only `O(1)` physical directions `(a,b)`.
2. Once `(a,b)` is fixed, `g|odd(D_pi)`, so possible `g` cost `tau(D_pi)=B^{o(1)}`.
3. `H=odd(h)` and `c` fix `R_V=c/H`, hence `odd(D_V)=g*R_V`.
4. The 2-adic valuation of `D_V` has only `O(log B)=B^{o(1)}` possibilities in the polynomial physical box.
5. For fixed `D_V`, the factorization `D_V=(q-p)(q+p)` has `tau(D_V)=B^{o(1)}` admissible factor pairs.  Each pair recovers `p,q`, then `delta=(p^2+q^2)/k`.

Therefore

```text
boxed:
# fixed (U,epsilon,k,h,ell,c) physical states = B^o(1).   (74.9)
```

The same is true after fixed `(kappa,beta)` conditioning.

After a state is reconstructed, `P+`, `delta`, `R_pi`, the 2-adic part of `P-`, and the sharp `ell*delta` test are determined.  They remain mandatory physical predicates but contribute no independent fixed-power summation entropy after `(ell,c)` is fixed.

```text
FIXED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1
FIXED_TAGGED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1
POSITIVE_COMPANION_FIXED_POWER_ENTROPY_AFTER_ELL_C=0
DELTA_FIXED_POWER_ENTROPY_AFTER_ELL_C=0
TWO_ADIC_PMINUS_FIXED_POWER_ENTROPY_AFTER_ELL_C=0
MOVING_NORM_VALUE_PARAMETER_REDUCED_TO_ELL_C=true
```

This strictly sharpens t73's fixed-`P-` fiber theorem: the 2-adic part of `P-` can now be forgotten at only `B^{o(1)}` cost.

---

## 6. Post-t74 receiver

The live fixed-`U` problem is now the energy of admissible pairs `(ell,c)`, with only divisor-many direction/cancellation/orientation data, subject to

```text
ell prime,
ell^2>4B,
c<sqrt(B),
2c<ell,
ell*c<2B,
ell*g*c<2B,
q-p,q+p<sqrt(ell),
h*ell*((q-p)^2+(q+p)^2)<=4B,
ell*delta<=Y_U,
fixed U,
fixed small odd kappa band,
fixed beta,
physical squareclass/tag and reconstructed positive-companion predicates.
```

The canonical largest-prime and exponent-one statements are structural consequences on this physical parameterization; they are not separate independent sieve coordinates.

```text
CURRENT_FIXED_U_RECEIVER=
SharedUSmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaEnergy

SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_ENERGY_PROVED=false
CANONICAL_LPF_FILTER_STRUCTURAL_ON_PHYSICAL_PACKET=true
EXPONENT_ONE_FILTER_STRUCTURAL_ON_PHYSICAL_PACKET=true
```

---

## 7. tH20 decision

`tH20` remains needed, but the pre-t74 target

```text
SmallOddKappaFixedTagMovingCanonicalLargestPrimeSmoothNormValueSieve
```

is no longer minimal.

Use instead

```text
TH20_REQUESTED_OBJECT=
SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
```

The useful independent theorem audit should count the `(ell,c)` / primitive-cover parameterization while retaining the two root hosts, both sharp hyperbolas, short factors, short ellipse, reconstructed positive companion, `ell*delta<=Y_U`, and fixed `(kappa,beta)` squareclass/tag data.

Do not reopen fixed-norm Pell orbits, class number, regulator, denominator-tag orientation, or generic smooth-value counting detached from `(q-p)(q+p)`.

```text
TH20_NEEDED=true
TH20_PRE_T74_TARGET_MINIMAL=false
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
```

---

## 8. Shared exponent and next step

Merged s7-34 improves the current whole-family theorem to

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=47/80
```

from the previous `19/32` certificate.  This improvement is imported; t74 itself proves no additional whole-family saving.

Stage14-t75 should split the live `(ell,c)` energy by angular cancellation `g` and by the balance of the short factors `(q-p,q+p)`:

- large `g`: exploit `ell*g*c<2B`;
- balanced short factors: exploit the ellipse and primitive factorization directly;
- highly unbalanced factors: divisor-switch on one short linear factor before requesting any further external theorem.

---

## Locked boundary

```text
STAGE14_T74=COMPLETE_CANONICAL_HOST_ELL_FREE_COFACTOR_BALANCE_AND_SHORT_ANGULAR_COVER_REDUCTION
MERGED_T73_IMPORTED=true
MERGED_S7_34_GLOBAL_47_80_LEDGER_IMPORTED=true
CANONICAL_ELL_TWO_ROOT_HOST_ORIENTATIONS_PROVED=true
CANONICAL_ELL_HOST_ORIENTATION_COST=O1
CANONICAL_ELL_CANCELS_EXACTLY_FROM_CAYLEY_BALANCE=true
ELL_FREE_RESIDUAL_COFACTOR_BALANCE_PROVED=true
ODD_PMINUS_OVER_ELL_EQUALS_H_TIMES_RV=true
SHARP_ELL_C_HYPERBOLA_PROVED=true
SHARP_ELL_G_C_HYPERBOLA_PROVED=true
CANONICAL_ODD_COFACTOR_LT_SQRT_B=true
COVER_DEFICIT_LINEAR_FACTORIZATION_RESTORED=true
COVER_LINEAR_FACTORS_LT_SQRT_ELL=true
SHORT_COVER_ELLIPSE_PROVED=true
FIXED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1
FIXED_TAGGED_PACKET_ELL_C_PHYSICAL_FIBER=Bo1
MOVING_NORM_VALUE_PARAMETER_REDUCED_TO_ELL_C=true
SHARED_U_SMALL_ODD_KAPPA_FIXED_TAG_CANONICAL_PRIME_SHORT_ANGULAR_COFACTOR_HYPERBOLA_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=47/80
T74_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH20_NEEDED=true
TH20_PRE_T74_TARGET_MINIMAL=false
TH20_REQUESTED_OBJECT=SmallOddKappaFixedTagCanonicalPrimeShortAngularCofactorHyperbolaSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH20=false
NEXT=Stage14-t75
```
