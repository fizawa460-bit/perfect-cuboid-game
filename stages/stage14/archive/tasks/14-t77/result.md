# Stage14-t77 — radial-degenerate split and Gaussian projective ray-character kernel

## Purpose

Merged Stage14-t76 reduces the fixed-`U`, fixed-tag hard block to a deficient clean-squareclass projective line

```text
Q = K_clean,
gcd(Q,A*B*r*t)=1,
t == rho*r (mod Q),
Q < R*T*B^o(1),
```

inside the balanced small-angular-gcd physical packet. Merged Stage14-tH21 then proves that no DFI/Kuznetsov/spectral theorem can be imported directly: the modulus `Q` is fixed after packet conditioning, while the moving prime is the separate canonical Gaussian prime `ell`.

Stage14-t77 performs the exact reduction requested by tH21. It has two parts.

1. It removes the primes of `Q` on which the Gaussian direction and cover are nonunits. Those primes are exactly a fixed radial/isotropic selector coming from `k` (equivalently from `m=N(U)`).
2. On the remaining modulus the t76 projective line is exactly one class equality in

```text
G_Q = (Z[i]/Q Z[i])^x / (Z/QZ)^x,
```

and character orthogonality converts it to a separated bilinear kernel

```text
projective ray character on the canonical Gaussian prime
  x
projective ray character on the primitive cover.
```

This is a genuine theorem-ready multiplicative kernel. Stage14-t77 does **not** prove the required ray-character large-sieve/dispersion estimate, and proves no new whole-family exponent saving.

The current strongest merged whole-family theorem is

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112
```

from merged Stage14-s7-38 / the compatible 4cw certificate.

---

## 1. Imported post-t76 packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
beta=gcd(kappa,v),
alpha=kappa/beta.
```

Write

```text
z=a+i*b=pi*U,
N(pi)=ell,
N(U)=m,
V=p+i*q,
N(V)=k*delta,

A=b-a,
Bdir=b+a,
r=q-p,
t=q+p.
```

Put

```text
K=odd(kappa),
g=gcd(odd(A*Bdir),odd(r*t)),
Q=K_clean=K/gcd(K,g).
```

Merged t76 gives

```text
gcd(Q,A*Bdir*r*t)=1
```

and, after a `B^o(1)` reciprocal-orientation choice,

```text
t == rho*r (mod Q).
```

The Kummer components are

```text
L1=A*t-Bdir*r,
L2=Bdir*t-A*r,
L3=A*t+Bdir*r,
L4=Bdir*t+A*r,
```

with the Gaussian identities

```text
2*conj(z)*V =  L4-i*L1,
2*z*V       = -L3+i*L2.
```

For primes in `alpha`, the chosen local root is on `L1` or `L2`; for primes in `beta`, it is on `L3` or `L4`.

---

## 2. The radial nonunit support

Merged t69--t74 give

```text
gcd(Pplus*Pminus,kappa)=1,
odd(Pplus)=odd(delta)*R_pi,
odd(Pminus/ell)=odd(h)*R_V.
```

Hence every odd prime `s|K` satisfies

```text
s∤ell,
s∤delta,
s∤h.
```

Since

```text
h*k=epsilon*m
```

and `s` is odd, one has

```text
v_s(m)=v_s(k).
```

Therefore for the t76 clean modulus `Q`, define

```text
Q_rad = gcd(Q,k).
```

Then exactly

```text
boxed:
Q_rad = gcd(Q,m).
```

Put

```text
Q_ray = Q/Q_rad.
```

For every prime `s|Q_ray`, all of

```text
pi, U, z=pi*U, V
```

are units modulo `s Z[i]`, because

```text
s∤ell*m*k*delta.
```

Thus `Q_ray` is precisely the part of the t76 modulus on which Gaussian multiplication acts invertibly on projective classes.

```text
RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_K=true
RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_M=true
RAY_MODULUS_GAUSSIAN_DIRECTION_AND_COVER_ARE_UNITS=true
```

---

## 3. Radial primes are isotropic local selectors, not moving-prime phases

Let `s|Q_rad`. Since `s|m` and `s|k`, while `s∤ell*delta`,

```text
A^2+Bdir^2 = 2*ell*m == 0 (mod s),
r^2+t^2    = 2*k*delta == 0 (mod s).
```

Merged t76 gives `s∤A*Bdir*r*t`. Therefore `-1` is a square modulo `s`, so

```text
s == 1 (mod 4).
```

Both projective slopes are isotropic:

```text
(Bdir/A)^2 == -1 (mod s),
(t/r)^2     == -1 (mod s).
```

The two reciprocal t76 roots are therefore just the two isotropic slopes `+sqrt(-1)` and `-sqrt(-1)`, independently of the numerator/denominator sign. After the already-allowed local orientation conditioning this costs at most `2^omega(Q_rad)=B^o(1)` and produces no moving `pi` phase.

Equivalently, at such a split prime the fixed Gaussian factor of `U` selects one of the two primes above `s`, and the cover `V` must select the compatible local factor. Multiplication by the moving unit `pi` cannot change which split component of `U` is zero.

Thus `Q_rad` is a **radial Gaussian divisor tag**, not part of the analytic projective-ray modulus.

```text
RADIAL_SUPPORT_PRIMES_SPLIT_MOD4=true
RADIAL_SUPPORT_PROJECTIVE_ROOT_IS_ISOTROPIC=true
RADIAL_SUPPORT_MOVING_PI_PHASE=false
RADIAL_SUPPORT_LOCAL_SELECTOR_COST=Bo1
```

No fixed-power saving is claimed from the radial selector alone.

---

## 4. Four chosen Kummer components on the ray modulus

Restrict now to

```text
M=Q_ray.
```

Let

```text
alpha_ray=gcd(odd(alpha),M),
beta_ray=gcd(odd(beta),M).
```

Then

```text
alpha_ray*beta_ray=M,
gcd(alpha_ray,beta_ray)=1.
```

Fix one of the at most `2^omega(M)` reciprocal root choices. It partitions `M` into pairwise-coprime squarefree component moduli

```text
M1*M2=alpha_ray,
M3*M4=beta_ray,
M1*M2*M3*M4=M,
```

such that

```text
M1 | L1,
M2 | L2,
M3 | L3,
M4 | L4.
```

If a prime happens to satisfy both reciprocal roots, assign it to either admissible component; this only reduces the number of choices and remains `B^o(1)`.

```text
RAY_MODULUS_FOUR_KUMMER_COMPONENT_ORIENTATION_EXISTS=true
RAY_MODULUS_ORIENTATION_MULTIPLICITY=Bo1
```

---

## 5. Projective Gaussian ray-class group

For odd squarefree `M`, define

```text
G(M)=(Z[i]/M Z[i])^x / (Z/MZ)^x.
```

Write `[w]_M` for the class of a Gaussian unit `w`; two units have the same class exactly when they differ by a rational unit modulo `M`.

By CRT,

```text
G(M) = product_{s|M} G(s).
```

For an odd prime `s`,

```text
|G(s)| = s-1,  s==1 (mod4),
|G(s)| = s+1,  s==3 (mod4).
```

Hence

```text
boxed:
|G(M)| = product_{s|M} (s-chi_4(s))
       = M*B^o(1).
```

The principal projective density is therefore

```text
|G(M)|^-1 = M^-1*B^o(1),
```

matching the natural root-line density up to divisor-size factors.

```text
PROJECTIVE_GAUSSIAN_RAY_GROUP_EXHIBITED=true
PROJECTIVE_GAUSSIAN_RAY_GROUP_ORDER_FORMULA_PROVED=true
PROJECTIVE_RAY_PRINCIPAL_DENSITY=M^-1*Bo1
```

---

## 6. Each Kummer component is one projective ray-class equality

Because `z` and `V` are units modulo every prime of `M`, the Gaussian component identities can be projectivized.

The four local conditions become

```text
L1==0: [z]=[V],
L2==0: [z]=[conj(V)]=[V]^-1,
L3==0: [z]=[i*conj(V)]=[i]*[V]^-1,
L4==0: [z]=[i*V]=[i]*[V].
```

Here `[conj(V)]=[V]^-1` because `V*conj(V)=N(V)` is a rational unit on `M`.

Since `z=pi*U`, the chosen four-component orientation combines by CRT into the single global identity

```text
boxed:
[pi]_M = [U]^-1 * I_beta * sigma([V]_M).
```

Definitions:

- `I_beta` is componentwise `[i]` on `beta_ray` and `1` on `alpha_ray`;
- `sigma` is the product-group automorphism that is the identity on `M1,M4` and inversion on `M2,M3`.

Thus the t76 additive-looking root line is exactly a **projective Gaussian ray-class incidence** on its dynamically nondegenerate support.

```text
CLEAN_PROJECTIVE_ROOTLINE_EQUALS_GAUSSIAN_RAY_CLASS_INCIDENCE=true
FIXED_BETA_BECOMES_FIXED_I_RAY_CLASS=true
RECIPROCAL_ROOT_CHOICE_BECOMES_LOCAL_INVERSION_AUTOMORPHISM=true
```

---

## 7. Character orthogonality gives a separated bilinear kernel

Let `G=G(M)` and `G^` be its character group. The exact class indicator is

```text
1_{[pi]=[U]^-1 I_beta sigma([V])}
=
1/|G| * sum_{chi in G^}
  chi([pi]*[U]*I_beta^-1*sigma([V])^-1).
```

Let

```text
chi_sigma = chi o sigma.
```

Since `sigma` is an automorphism, `chi_sigma` is again a projective ray character. Therefore every nonprincipal term factors exactly as

```text
C_chi(U,beta)
  * chi([pi])
  * conjugate(chi_sigma([V])),
```

where `C_chi(U,beta)` has modulus one and is fixed on the packet/orientation.

So after t77 the discrepancy kernel is no longer an unspecified inverse-fraction phase. It is a standard multiplicative character correlation between

```text
canonical Gaussian prime pi
```

and

```text
primitive Gaussian cover V.
```

All canonical-prime, balanced-cover, short-ellipse, `ell*c`, `ell*g*c`, and `ell*delta` masks remain as weights; t77 does not discard them.

```text
PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT=true
RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY=true
PRINCIPAL_CHARACTER_REPRODUCES_PROJECTIVE_DENSITY=true
NONPRINCIPAL_KERNEL=GaussianPrimeRayCharacter_x_CoverRayCharacter
```

---

## 8. What t77 does and does not separate

The **arithmetic congruence kernel** is now separated. The complete physical weight is not declared to be a tensor product.

In particular, the exact angular gcd allocation and reconstructed cofactor still impose coupled local/sieve weights, while

```text
ell*c<2B,
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U
```

remain sharp multiplicative cutoffs.

Dyadic localization preserves the ray-character kernel at `B^o(1)` bookkeeping cost, but a uniform theorem must still prove cancellation with these weights present. Hence t77 does not silently import a Gaussian prime theorem with the masks removed.

```text
ARITHMETIC_PROJECTIVE_KERNEL_SEPARATED=true
FULL_PHYSICAL_WEIGHT_TENSOR_FACTORIZATION_PROVED=false
DYADIC_LOCALIZATION_PRESERVES_RAY_CHARACTER_KERNEL=true
```

---

## 9. Minimal post-t77 receiver

The ray-active branch is now

```text
SharedUSmallOddKappaFixedTagSmallAngularGcdBalancedRayActiveCanonicalGaussianPrimeProjectiveCharacterTypeIIEnergy
```

with exact analytic contract

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

uniformly for squarefree growing `M=Q_ray`, including the deficient range inherited from t76.

The complementary `M=1` / radial-only branch contains no moving-prime ray character. It remains an exact local Gaussian-divisor-tagged physical block and must not be falsely charged with `1/Q_rad` character density.

```text
RAY_ACTIVE_TYPEII_ENERGY_PROVED=false
RADIAL_ONLY_BRANCH_PROJECTIVE_CHARACTER_SAVING_AVAILABLE=false
```

---

## 10. tH22 decision

Merged tH21 explicitly said not to open another auxiliary audit until t77 produced a genuine standard Kloosterman/inverse-fraction or Gaussian-prime progression kernel.

Stage14-t77 has now produced the latter, more precisely a **Gaussian projective ray-character kernel**. Therefore a new independent applicability audit is justified.

```text
TH22_NEEDED=true
TH22_REQUESTED_OBJECT=CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

The t route is not blocked. Stage14-t78 should continue internally by studying the radial-only `Q_ray=1` block and by testing whether the exact small-`g` column allocation can be Möbius-separated without losing the sharp hyperbolas.

---

## 11. Shared exponent

Latest merged main carries

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112
```

Stage14-t77 proves no additional whole-family saving.

---

## Locked boundary

```text
STAGE14_T77=COMPLETE_RADIAL_DEGENERATE_SPLIT_AND_GAUSSIAN_PROJECTIVE_RAY_CHARACTER_KERNEL
MERGED_T76_IMPORTED=true
MERGED_TH21_IMPORTED=true
RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_K=true
RADIAL_NONUNIT_SUPPORT_EQUALS_GCD_Q_M=true
RADIAL_SUPPORT_PRIMES_SPLIT_MOD4=true
RADIAL_SUPPORT_PROJECTIVE_ROOT_IS_ISOTROPIC=true
RADIAL_SUPPORT_MOVING_PI_PHASE=false
RAY_MODULUS_GAUSSIAN_DIRECTION_AND_COVER_ARE_UNITS=true
PROJECTIVE_GAUSSIAN_RAY_GROUP_EXHIBITED=true
PROJECTIVE_GAUSSIAN_RAY_GROUP_ORDER_FORMULA_PROVED=true
CLEAN_PROJECTIVE_ROOTLINE_EQUALS_GAUSSIAN_RAY_CLASS_INCIDENCE=true
FIXED_BETA_BECOMES_FIXED_I_RAY_CLASS=true
RECIPROCAL_ROOT_CHOICE_BECOMES_LOCAL_INVERSION_AUTOMORPHISM=true
PROJECTIVE_ROOTLINE_CHARACTER_ORTHOGONALITY_EXACT=true
RAY_CHARACTER_KERNEL_SEPARATES_PI_AND_V_ARITHMETICALLY=true
FULL_PHYSICAL_WEIGHT_TENSOR_FACTORIZATION_PROVED=false
RAY_ACTIVE_TYPEII_ENERGY_PROVED=false
TH22_NEEDED=true
TH22_REQUESTED_OBJECT=CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH22=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=61/112
T77_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t78
```
