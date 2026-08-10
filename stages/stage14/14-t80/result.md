# Stage14-t80 — primitive projective Gauss dualization and additive conductor compression

## Status

`COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL`

Stage14-t80 consumes merged t77, t78, and t79. The independent tH22 audit is retained only as an advisory literature/conductor check because its PR was closed without merge; no theorem in this stage depends on tH22 being merged.

The current strongest merged whole-family theorem remains

```text
V(B) << B^(23/44+o(1)).
```

No additional whole-family power saving is claimed here.

## 1. Entering packet

Fix

```text
(U,epsilon,k,h,kappa,beta)
```

and the t78/t79 ray-active data

```text
K=oddpart(kappa),
K_ext=K/gcd(K,k),
M=K/gcd(K,g*k)=K_ext/gcd(K_ext,g),
M>1.
```

Merged t79 decomposes a projective character by active support

```text
d=d(chi)|M,
e=M/d,
```

and proves that all fixed-power inactive support `e` is automatically suppressed. Hence the only analytic character family which can remain hard has

```text
d=M/B^o(1).
```

At every `p|d` the local projective character is nonprincipal. The t76 unit statement gives

```text
gcd(d,A*Bdir*r*t)=1,
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p.
```

Moreover `A+iBdir` and `r+it` are Gaussian units modulo every `p|d`, because they are fixed-unit/conjugate transforms of `pi*U` and `V` on the ray-active support. Thus the corresponding projective Cayley slopes are finite admissible points.

## 2. Local projective group in an affine Cayley chart

For an odd prime `p` put

```text
G_p=(Z[i]/pZ[i])^x/(Z/pZ)^x,
|G_p|=p-chi_4(p).
```

Represent a finite projective class by

```text
[1+i*x],
x in F_p,
1+x^2 != 0 mod p.
```

The omitted class is `[i]`. When `p==3 mod 4`, every finite `x` is admissible and `|G_p|=p+1`. When `p==1 mod 4`, the two isotropic roots of `1+x^2` are excluded and `|G_p|=p-1`.

Let `chi_p` be a nonprincipal character of `G_p`. Extend its affine trace by zero at isotropic nonunits:

```text
F_{chi_p}(x)=chi_p([1+i*x]) if 1+x^2 != 0,
             0               otherwise.
```

Define

```text
G_p(chi_p;a)
 = sum_{x mod p} F_{chi_p}(x) exp(-2*pi*i*a*x/p).
```

Because the sum of a nonprincipal character over the full projective group is zero and the only omitted unit class is `[i]`,

```text
G_p(chi_p;0)=-chi_p([i]),
|G_p(chi_p;0)|=1.
```

For `a!=0`, the finite-field mixed character sum is a rank-one Kummer/Jacobi sum on the projective torus. The classical Weil bound gives

```text
|G_p(chi_p;a)| <= 2*sqrt(p).
```

This finite-field local estimate is not a global large-sieve theorem. After normalising by `p`,

```text
c_{chi_p}(a)=G_p(chi_p;a)/p,
```

we obtain

```text
|c_{chi_p}(0)|=1/p,
|c_{chi_p}(a)|<=2/sqrt(p)  (a!=0).
```

Parseval gives

```text
sum_{a mod p}|c_{chi_p}(a)|^2
 = (# admissible affine classes)/p
 <=1.
```

## 3. Squarefree conductor `d`: exact CRT Fourier expansion

Because `d` is squarefree and every `chi_p` for `p|d` is nonprincipal, define

```text
F_chi(x)=product_{p|d} F_{chi_p}(x mod p).
```

CRT gives the exact expansion

```text
F_chi(x)=sum_{a mod d} c_chi(a) exp(2*pi*i*a*x/d),
```

with primewise-factorised coefficients. Put

```text
q(a)=d/gcd(d,a).
```

Then

```text
|c_chi(a)|
 <= 2^omega(q(a))*sqrt(q(a))/d
 = B^o(1)*sqrt(q(a))/d.
```

For primitive additive frequency `(a,d)=1`,

```text
|c_chi(a)| <= d^(-1/2)*B^o(1).
```

If `z=gcd(d,a)` is the zero-frequency support, then

```text
|c_chi(a)| <= (d*z)^(-1/2)*B^o(1).
```

Parseval tensorises:

```text
sum_{a mod d}|c_chi(a)|^2 <=1.
```

The total Fourier `L2` mass on frequencies with prescribed zero-support divisor `z|d` is

```text
<= z^(-2)*B^o(1),
```

because every `p|z` contributes the exact local zero-frequency square `1/p^2`. Consequently

```text
sum_{gcd(a,d)>=Z}|c_chi(a)|^2
 <= Z^(-2)*B^o(1).
```

Thus any fixed-power additive-frequency deficit is automatically negligible in `L2`; the genuinely hard dual frequencies may be restricted to `(a,d)=1` up to endpoint-small support.

## 4. Conductor compression: `d^2` ideal norm becomes additive modulus `d`

The advisory tH22 conductor calculation identifies

```text
f_fin(chi)=(d),
N f_fin(chi)=d^2.
```

Stage14-t80 does not invoke a Hecke large sieve at conductor norm `d^2`. Instead, the exact projective Cayley Fourier transform rewrites the character using rational additive characters modulo `d`:

```text
PROJECTIVE_ADDITIVE_DUAL_MODULUS=d.
```

The primitive-frequency Fourier coefficient is

```text
d^(-1/2)*B^o(1).
```

This is a representation/conductor-compression theorem, not yet an estimate for the remaining incomplete physical bilinear sums.

## 5. Physical inverse-fraction phases

The 45-degree Gaussian coordinates from t71 are

```text
A+iBdir=(-1+i)*conj(pi*U),
r+it=(-1+i)*conj(V).
```

On `d`, all four rational coordinates `A,Bdir,r,t` are units. Hence the finite projective classes can be represented by

```text
x_pi=Bdir/A mod d,
x_V=t/r mod d.
```

Fixed `U`, fixed beta, and the conditioned reciprocal/inversion orientation only apply fixed projective multiplication, sign, conjugation, or inversion. These replace the affine coordinate by a fixed Mobius transform. Therefore the t77 separated kernel

```text
chi(pi)*conjugate((chi o sigma)(V))
```

becomes a finite sum of additive phases

```text
exp_d(a*Mobius_U(Bdir/A))
*
exp_d(-b*Mobius_beta,sigma(t/r)).
```

Representative hard phases include

```text
exp_d(a*Bdir*inv(A)),
exp_d(a*A*inv(Bdir)),
exp_d(b*t*inv(r)),
exp_d(b*r*inv(t)),
```

with fixed signs. For the hard part `(a*b,d)=1` may be assumed up to the Fourier-support deficit already paid.

Thus the nonprincipal near-full-support ray-character obstruction becomes an incomplete primitive inverse-fraction bilinear problem at rational modulus `d`.

## 6. Physical masks remain intact

Retain

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular g through the t78 four-cell coefficients,
balanced primitive cover,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell*odd(h)*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
delta=(r^2+t^2)/(2k),
fixed beta sign rule,
fixed reciprocal/inversion orientation,
d=M/B^o(1),
(a*b,d)=1 up to endpoint-small Fourier deficit.
```

The t78 Möbius divisor tensor remains valid. Dyadic/Mellin localization is still required in a global analytic adapter, but no angular-gcd obstruction is reintroduced.

## 7. Closed and live pieces

Closed in t80:

```text
principal ray character;
fixed-power inactive character support;
fixed-power zero additive-frequency support;
the d^2-vs-d projective conductor representation mismatch;
exact conversion to rational inverse-fraction additive phases.
```

Not closed:

```text
an incomplete bilinear large-sieve/dispersion estimate for primitive
inverse-fraction phases with canonical-prime and short-cover masks;
endpoint-small K_ext balanced physical cover energy;
a whole-family exponent improvement.
```

New receiver:

```text
SharedUBalancedNearFullSupportPrimitiveProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionEnergy
```

Analytic target:

```text
NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
```

## 8. tH decision

The situation is materially different from tH22. tH22 audited a Hecke/ray-character family with conductor norm up to `M^2`; t80 converts the hard family to primitive additive inverse-fraction phases at rational modulus `d=M/B^o(1)`.

```text
TH23_NEEDED=true
TH23_REQUESTED_OBJECT=NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
```

The one-shot tH23 request is recorded in

```text
stages/stage14/14-t80/th23-target.md
```

## 9. Current shared exponent

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
T80_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t81
```

## Locked boundary

```text
STAGE14_T80=COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL
MERGED_T79_IMPORTED=true
TH22_AUDIT_PR_MERGED=false
PROJECTIVE_LOCAL_AFFINE_FOURIER_EXPANSION_PROVED=true
PROJECTIVE_LOCAL_ZERO_FREQUENCY_COEFFICIENT_EXACT=1/p
PROJECTIVE_LOCAL_NONZERO_FREQUENCY_WEIL_BOUND=2/sqrt(p)
PROJECTIVE_CRT_FOURIER_FACTORIZATION_PROVED=true
PRIMITIVE_ADDITIVE_FREQUENCY_COEFFICIENT=d^-1/2*Bo1
ADDITIVE_FREQUENCY_FIXED_POWER_DEFICIT_AUTOMATICALLY_SAVED=true
ADDITIVE_FREQUENCY_DEFICIT_L2_BOUND=Z^-2*Bo1
PROJECTIVE_HECKE_CONDUCTOR_NORM=d^2
PROJECTIVE_ADDITIVE_DUAL_MODULUS=d
PROJECTIVE_CONDUCTOR_COMPRESSION_TO_RATIONAL_ADDITIVE_MODULUS_PROVED=true
PHYSICAL_PROJECTIVE_SLOPES_ARE_UNIT_AFFINE_MOD_D=true
PROJECTIVE_CHARACTER_KERNEL_BECOMES_INVERSE_FRACTION_ADDITIVE_KERNEL=true
FULL_PHYSICAL_MASKS_RETAINED=true
PRIMITIVE_INVERSE_FRACTION_PHYSICAL_ENERGY_PROVED=false
ENDPOINT_SMALL_EXTERNAL_KAPPA_PHYSICAL_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
T80_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH23_NEEDED=true
TH23_REQUESTED_OBJECT=NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
NEXT=Stage14-t81
```