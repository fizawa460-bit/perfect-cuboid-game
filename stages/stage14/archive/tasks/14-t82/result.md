# Stage14-t82 — fixed-U selector divisor modulus and hard affine-support compression

## Status

`COMPLETE_AFFINE_DEGENERATE_RAY_MODULUS_TO_FIXED_U_COORDINATE_DIVISOR_HOST`

Stage14-t82 consumes Stage14-t81 as its direct predecessor. At the time this branch is opened, t81 PR #585 is Ready/mergeable but not yet merged, so t82 is stacked on the t81 head and must be cleaned onto main after #585 merges.

The current canonical whole-family theorem is still

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent saving is claimed here.

## 1. Entering t81 hard branch

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
N(U)=m=R^2+S^2,
gcd(R,S)=1.
```

Write

```text
K=oddpart(kappa),
K_ext=K/gcd(K,k),
M=K_ext/gcd(K_ext,g),
d=M/B^o(1).
```

Merged t72 gives the exact denominator tag

```text
alpha=kappa/beta,
beta=gcd(kappa,v),
alpha*beta=kappa,
gcd(alpha,beta)=1.
```

Stage14-t81 reduces the unsaved character/Fourier support to

```text
d_frac=B^o(1),
d_mis=B^o(1),
d_diag=d/B^o(1),
b_freq=s_d*a_freq mod d_diag,
s_d^2=1 mod d_diag,
```

and every prime of `d_diag` is affine-degenerate:

```text
[U]=I_beta,p.
```

## 2. Affine degeneration is an exact coordinate-divisor condition

For `p|M`, t77 guarantees that `U` is a Gaussian unit modulo `p`. In the projective quotient

```text
G(p)=(Z[i]/pZ[i])^x/(Z/pZ)^x,
```

the identities are elementary:

```text
[U]=[1]  <=> S==0 mod p,
[U]=[i]  <=> R==0 mod p.
```

Indeed `[R+iS]=[1]` means `R+iS` differs from `1` by a nonzero rational scalar, hence `S=0`; similarly `[U]=[i]` means `R=0`. The converse is immediate because `p` does not divide `m` on the ray modulus.

The t77 beta tag is

```text
I_beta,p=[1]  on alpha-ray primes,
I_beta,p=[i]  on beta-ray primes.
```

Therefore, exactly,

```text
p affine-degenerate
<=>
  (p|alpha and p|S)
  or
  (p|beta and p|R).
```

This is not an analytic exceptional set. It is a divisor selector on the two fixed coordinates of `U`.

## 3. Canonical selector divisor

Split the ray modulus by the alpha/beta tag:

```text
M_alpha=gcd(M,oddpart(alpha)),
M_beta =gcd(M,oddpart(beta)),
M_alpha*M_beta=M.
```

Define the fixed-U selector divisor

```text
D_Ubeta
 := gcd(M_alpha,abs(S)) * gcd(M_beta,abs(R)).
```

The factors are coprime. Section 2 gives

```text
boxed:
d_diag | D_Ubeta.
```

Moreover

```text
D_Ubeta | abs(R*S).
```

Since `U` is primitive,

```text
gcd(R,S)=1,
2*abs(R*S)<=R^2+S^2=m.
```

Hence

```text
boxed:
D_Ubeta <= m/2.
```

Merged t65 gives `ell>2m`, so on the hard affine branch

```text
boxed:
d_diag <= m/2 < ell/4.
```

The inequalities are exact up to the already-declared `B^o(1)` support deficits when replacing `d_diag` by `M`.

## 4. Every nonselector ray prime is already t81-saved

Let

```text
M_sel=D_Ubeta,
M_nsel=M/gcd(M,D_Ubeta).
```

For every prime `p|M_nsel`, one of two things happens:

1. `p` is inactive in the t79 support, hence `p|(M/d)`;
2. `p|d`, in which case `C_p!=identity`, hence `p|d_frac`.

Therefore squarefreely and exactly,

```text
boxed:
M_nsel | (M/d)*d_frac.
```

On the t79/t81 hard branch both factors on the right are `B^o(1)`. Consequently

```text
boxed:
M_nsel=B^o(1),
M=D_Ubeta*B^o(1).
```

Thus almost the entire ray modulus is hosted by the fixed coordinate divisor `R*S`.

## 5. Modulus averaging disappears at fixed U

For fixed `U`, every hard `d_diag` is a divisor of `D_Ubeta`, hence of `R*S`. Therefore

```text
# { admissible hard d_diag for fixed U }
 <= tau(abs(R*S))
 = B^o(1).
```

The remaining analytic problem must not pay an independent moving-modulus family length. The modulus is a divisor-hosted fixed coefficient.

Equivalently the post-t82 hard object is a single-frequency incomplete inverse-fraction sum with

```text
d_diag | R*S,
d_diag <= m/2,
d_diag < ell/4,
#d_diag=B^o(1) for fixed U.
```

This is a stronger range/quantifier statement than t81.

## 6. Pure pi/V projective relation on the selector modulus

On `d_diag`, the fixed class cancels:

```text
[U]^-1 I_beta = 1.
```

Hence the t77 incidence becomes simply

```text
[pi]=sigma([V]) mod d_diag.
```

Thus, primewise, the surviving congruence is a pure canonical-prime/primitive-cover projective relation. In ordinary coordinates `pi=c+i*d0`, `V=p+i*q`, it is one of

```text
d0*p-c*q == 0 mod p_ray,

d0*p+c*q == 0 mod p_ray,
```

according to the fixed identity/inversion orientation. CRT gives only `B^o(1)` sign patterns.

This does not by itself give enough determinant spacing in the t76-deficient range; it identifies the exact remaining phase without a moving fixed-U coefficient.

## 7. Refined receiver

The live receiver is

```text
SharedUBalancedFixedUSelectorDivisorModulusAlmostDiagonalSinglePrimitiveFrequencyCanonicalPrimeShortCoverInverseFractionEnergy
```

with mandatory contract

```text
fixed U=R+iS,
d_diag|R*S,
#d_diag=B^o(1),
d_diag<=m/2<ell/4,
[pi]=sigma([V]) mod d_diag,
single primitive frequency,
canonical ell,
balanced primitive cover,
short ellipse,
sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
ell*delta hyperbola.
```

## 8. tH decision

`tH23` remains useful because the analytic object is still an incomplete canonical-prime/short-cover inverse-fraction sum. However its target is refined again: modulus averaging and the fixed-U projective coefficient are no longer part of the obstruction.

```text
TH23_NEEDED=true
TH23_TARGET_REFINED_BY_T82=true
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
```

The complete handoff is in

```text
stages/stage14/14-t82/th23-refinement.md
```

## 9. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T82_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t83
```

## Locked boundary

```text
STAGE14_T82=COMPLETE_AFFINE_DEGENERATE_RAY_MODULUS_TO_FIXED_U_COORDINATE_DIVISOR_HOST
T81_PREDECESSOR_CONSUMED=true
AFFINE_ALPHA_TAG_EQUIVALENT_TO_P_DIVIDES_S=true
AFFINE_BETA_TAG_EQUIVALENT_TO_P_DIVIDES_R=true
FIXED_U_SELECTOR_DIVISOR_DEFINED=true
HARD_DIAGONAL_MODULUS_DIVIDES_FIXED_U_SELECTOR=true
FIXED_U_SELECTOR_DIVIDES_R_TIMES_S=true
FIXED_U_SELECTOR_MAX=m/2
HARD_DIAGONAL_MODULUS_LT_ELL_OVER_4_UP_TO_BO1=true
NONSEL_RAY_SUPPORT_DIVIDES_INACTIVE_TIMES_FRACTIONAL_SUPPORT=true
HARD_NONSEL_RAY_SUPPORT=Bo1
HARD_RAY_MODULUS_HOSTED_BY_FIXED_U_COORDINATES=true
FIXED_U_HARD_MODULUS_MULTIPLICITY=Bo1
MOVING_MODULUS_FAMILY_LENGTH_REOPENED=false
PURE_PI_V_PROJECTIVE_RELATION_ON_DIAGONAL_MODULUS=true
SINGLE_FREQUENCY_PHYSICAL_INVERSE_FRACTION_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T82_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH23_NEEDED=true
TH23_TARGET_REFINED_BY_T82=true
TH24_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
NEXT=Stage14-t83
```
