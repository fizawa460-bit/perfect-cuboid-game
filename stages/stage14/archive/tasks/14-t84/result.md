# Stage14-t84 — primitive switched norm, unique super-square-root largest prime, and short cofactor reduction

## Status

`COMPLETE_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_AND_SHORT_COFACTOR_REDUCTION`

Stage14-t84 consumes merged Stage14-t83 and the already-merged Stage14-tH23 snapshot result. The H result is frozen under `stages/stage14/H-PROTOCOL.md`; this stage does not refine or reopen tH23.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

The purpose of t84 is to remove the remaining apparent bilinear choice of the canonical Gaussian prime `pi` and the primitive cover `V` from the post-t83 kernel. In the switched coordinates, the canonical prime is exactly the unique super-square-root largest rational prime factor of one primitive binary norm.

---

## 1. Entering t83 switched packet

Fix the t82/t83 packet

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
```

and a fixed reciprocal/inversion orientation `sigma in {+1,-1}`. Let

```text
pi=x+i*y,
ell=N(pi)=x^2+y^2,
V=p+i*q,
n=N(V)=p^2+q^2=k*delta.
```

The cover is primitive:

```text
gcd(p,q)=1.
```

Stage14-t83 defines

```text
T = x*p + sigma*y*q,
D = y*p - sigma*x*q,
```

so that

```text
T^2+D^2=ell*n.                                  (1.1)
```

On the hard t82 selector modulus,

```text
D=d*j,
d=d_diag,
d | D_Ubeta | |R*S|,
0<|D|<=sqrt(2B/h),
```

and t83 proves `D!=0` together with

```text
min(d,|j|) <= (2B/h)^(1/4).                       (1.2)
```

The physical inequalities retained throughout are

```text
ell>2*n,
h*ell*n<=2B,
ell*delta<=Y_U,
ell^2>4B,
```

where the last two are used only in the ranges in which they were already established upstream.

---

## 2. The switched binary norm is primitive

Let

```text
g0=gcd(T,D).
```

The inverse linear identities are exact:

```text
x*T+y*D = ell*p,
sigma*(y*T-x*D) = ell*q.                          (2.1)
```

Hence `g0` divides both `ell*p` and `ell*q`. Since `gcd(p,q)=1`,

```text
g0 | ell.                                         (2.2)
```

But from `ell>2n` and (1.1),

```text
T^2+D^2=ell*n<ell^2/2,
```

so `|T|,|D|<ell`. Because `D!=0`, `g0=ell` is impossible. Therefore

```text
boxed:
gcd(T,D)=1.                                      (2.3)
```

This strengthens the t83 statement `gcd(T,d)=1`:

```text
PRIMITIVE_SWITCHED_BINARY_NORM_PROVED=true
GCD_T_D=1
GCD_T_J=1
```

The final line follows because `D=d*j`.

A standard sum-of-two-squares consequence is now exact: no odd prime `r==3 mod 4` divides `T^2+D^2`, because such an `r` would divide both `T` and `D`. Thus

```text
ODD_BINARY_NORM_SUPPORT_ONLY_1_MOD_4=true.         (2.4)
```

The 2-adic valuation is at most one for a primitive pair.

---

## 3. Canonical ell is the unique largest prime factor of the norm

Put

```text
N:=T^2+D^2=ell*n.                                  (3.1)
```

The physical separation

```text
ell>2*n                                             (3.2)
```

has three immediate consequences.

First, every prime divisor of `n` is strictly less than `ell`, so

```text
boxed:
ell=LPF(N)=LPF_odd(N).                            (3.3)
```

Second, `ell` does not divide `n`, hence

```text
boxed:
v_ell(N)=1.                                       (3.4)
```

Third,

```text
ell^2 > 2*ell*n = 2N,                              (3.5)
```

so the canonical prime is not merely the largest prime: it is the unique prime factor above the super-square-root threshold `sqrt(2N)`.

Conversely, inside the primitive switched image, (3.3)--(3.5) recover the same short cofactor

```text
n=N/ell<ell/2.                                     (3.6)
```

Thus the canonical-prime variable is determined by the primitive binary norm itself.

```text
CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF=true
CANONICAL_ELL_EXPONENT_ONE_IN_BINARY_NORM=true
CANONICAL_ELL_SUPER_SQRT_GAP=ell^2>2N
CANONICAL_PRIME_INDEPENDENT_CHOICE_ELIMINATED=true
```

This is a mathematical uniqueness statement; it does not claim that factoring arbitrary integers is computationally free.

---

## 4. The cofactor is automatically square-root short

From `N=ell*n` and `ell>2n`,

```text
n^2 < N/2.                                         (4.1)
```

Combining `h*N<=2B` with (4.1) gives

```text
boxed:
n < sqrt(B/h).                                    (4.2)
```

Since `n=k*delta`,

```text
boxed:
delta < sqrt(B/h)/k.                              (4.3)
```

Thus the switched norm has the exact large-prime/small-cofactor shape

```text
N=ell*n,
ell=LPF(N),
v_ell(N)=1,
ell^2>2N,
n=k*delta<sqrt(B/h).                              (4.4)
```

The original `ell*delta` hyperbola is retained, but its canonical prime is now a function of `(T,D)`.

```text
SHORT_COVER_NORM_COFACTOR_PROVED=true
SHORT_COVER_NORM_BOUND=sqrt(B/h)
SHORT_DELTA_BOUND=sqrt(B/h)/k
ELL_DELTA_HYPERBOLA_RETAINED=true
```

---

## 5. pi and V reconstruct from one primitive norm point

For a rational prime `ell==1 mod 4`, its representation

```text
ell=x^2+y^2
```

is unique up to the usual Gaussian units and conjugation. The already-fixed canonical direction convention chooses one `pi=x+i*y`.

For fixed `sigma`, (2.1) gives the exact inverse map

```text
p = (x*T+y*D)/ell,
q = sigma*(y*T-x*D)/ell.                           (5.1)
```

Therefore every physical switched point `(T,D)` has exactly one `V` under the fixed canonical `pi` and fixed orientation. If orientations are temporarily forgotten, the ambiguity is only `O(1)`.

Hence the post-t84 count no longer has an independent canonical-prime side and cover side. It is a one-vector primitive binary-norm problem, with the original balanced-cover and four-cell masks checked after the deterministic reconstruction (5.1).

```text
FIXED_ORIENTATION_PI_V_RECONSTRUCTION_UNIQUE=true
BILINEAR_PI_V_MULTIPLICITY_ELIMINATED=true
PHYSICAL_MASKS_BECOME_FILTERS_ON_RECONSTRUCTED_BINARY_NORM_POINT=true
```

For a fixed norm value `N`, the standard representation bound gives

```text
# {(T,D): T^2+D^2=N, gcd(T,D)=1}
 <= r_2(N)
 <= 4*tau(N)
 = B^o(1).                                         (5.2)
```

Thus a fixed exact binary norm has only subpolynomial switched multiplicity.

```text
FIXED_BINARY_NORM_PRIMITIVE_REPRESENTATION_MULTIPLICITY=Bo1
```

---

## 6. Fixed-U divisor hosting survives the switch

Stage14-t82/t83 remains fully active:

```text
d | D_Ubeta | |R*S|,
# {d for fixed U}=B^o(1),
D=d*j,
```

with

```text
0<d*|j|=|D|<=sqrt(2B/h),
min(d,|j|)<=(2B/h)^(1/4).                           (6.1)
```

Because `(T,D)=1`, every such divisor satisfies

```text
gcd(T,d)=gcd(T,j)=1.                               (6.2)
```

No moving-modulus family is reintroduced. The fixed-U selector divisor is now a vertical divisor of one primitive binary norm coordinate.

```text
FIXED_U_SELECTOR_DIVISOR_RETAINED=true
MOVING_MODULUS_FAMILY_REOPENED=false
DETERMINANT_QUOTIENT_RETAINED=true
QUARTER_SCALE_D_OR_J_DICHOTOMY_RETAINED=true
```

---

## 7. New analytic receiver

After t84, the live object is no longer the tH23 inverse-fraction bilinear form. It is

```text
SharedUFixedSelectorDivisorPrimitiveBinaryNorm
SuperSqrtLargestPrimeShortCofactorPhysicalEnergy.
```

The mandatory arithmetic kernel is

```text
N=T^2+D^2,
gcd(T,D)=1,
D=d*j,
d|D_Ubeta|R*S,
#d=B^o(1) for fixed U,
ell=LPF(N),
v_ell(N)=1,
ell^2>2N,
n=N/ell=k*delta<sqrt(B/h),
h*N<=2B,
ell*delta<=Y_U.
```

The reconstructed `V` must still satisfy the pre-existing physical filters:

```text
balanced primitive cover,
small angular-g four-cell weights,
short ellipse,
sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
fixed beta tag,
fixed reciprocal/inversion orientation,
canonical Gaussian direction convention.
```

No asymptotic saving for this sieve is proved in t84.

```text
PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_PHYSICAL_ENERGY_PROVED=false
```

---

## 8. tH24 decision under the immutable snapshot protocol

This is now a genuinely different standard analytic kernel from tH23:

```text
inverse-fraction / fixed modulus
   -> primitive binary quadratic norm
      with one unique super-square-root largest prime
      and a square-root-short cofactor.
```

An external theorem audit is therefore justified.

```text
TH23_TARGET_REOPENED=false
TH23_RESULT_FROZEN_AND_CONSUMED=true
TH24_NEEDED=true
TH24_REQUESTED_OBJECT=FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve
TH24_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
```

The complete request is stored in

```text
stages/stage14/14-t84/th24-target.md
```

When tH24 is actually dispatched, this t84 target is the immutable source snapshot. Later t85+ work must not refine the running tH24 request; any materially new receiver uses tH25.

---

## 9. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T84_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t85
```

---

## Locked boundary

```text
STAGE14_T84=COMPLETE_PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_AND_SHORT_COFACTOR_REDUCTION
MERGED_T83_IMPORTED=true
MERGED_TH23_SNAPSHOT_CONSUMED=true
PRIMITIVE_SWITCHED_BINARY_NORM_PROVED=true
GCD_T_D=1
GCD_T_J=1
ODD_BINARY_NORM_SUPPORT_ONLY_1_MOD_4=true
CANONICAL_ELL_RECOVERED_AS_BINARY_NORM_LPF=true
CANONICAL_ELL_EXPONENT_ONE_IN_BINARY_NORM=true
CANONICAL_ELL_SUPER_SQRT_GAP=ell^2>2N
CANONICAL_PRIME_INDEPENDENT_CHOICE_ELIMINATED=true
SHORT_COVER_NORM_COFACTOR_PROVED=true
SHORT_COVER_NORM_BOUND=sqrt(B/h)
SHORT_DELTA_BOUND=sqrt(B/h)/k
FIXED_ORIENTATION_PI_V_RECONSTRUCTION_UNIQUE=true
BILINEAR_PI_V_MULTIPLICITY_ELIMINATED=true
FIXED_BINARY_NORM_PRIMITIVE_REPRESENTATION_MULTIPLICITY=Bo1
FIXED_U_SELECTOR_DIVISOR_RETAINED=true
MOVING_MODULUS_FAMILY_REOPENED=false
DETERMINANT_QUOTIENT_RETAINED=true
QUARTER_SCALE_D_OR_J_DICHOTOMY_RETAINED=true
PRIMITIVE_BINARY_NORM_SUPER_SQRT_LPF_PHYSICAL_ENERGY_PROVED=false
TH23_TARGET_REOPENED=false
TH23_RESULT_FROZEN_AND_CONSUMED=true
TH24_NEEDED=true
TH24_REQUESTED_OBJECT=FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve
TH24_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T84_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t85
```
