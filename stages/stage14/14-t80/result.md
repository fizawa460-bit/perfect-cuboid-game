# Stage14-t80 — primitive projective Gauss dualization and additive conductor compression

## Status

`COMPLETE_NEAR_FULL_SUPPORT_PROJECTIVE_GAUSS_DUALIZATION_TO_PRIMITIVE_INVERSE_FRACTION_KERNEL`

Stage14-t80 consumes merged t77, t78, t79, and merged tH22. The current strongest merged whole-family theorem remains

```text
V(B) << B^(23/44+o(1)).
```

No additional whole-family power saving is claimed here.

## 1. Entering packet

Fix

```text
(U,epsilon,k,h,kappa,beta)
```

and

```text
K=oddpart(kappa),
K_ext=K/gcd(K,k),
M=K/gcd(K,g*k)=K_ext/gcd(K_ext,g),
M>1.
```

Merged t79/tH22 reduce the hard ray family to characters with active support

```text
d=d(chi)=M/B^o(1),
```

so every `p|d` is locally nonprincipal and merged tH22 gives the exact finite conductor

```text
f_fin(chi)=(d),
N f_fin(chi)=d^2.
```

Merged t76 gives

```text
gcd(d,A*Bdir*r*t)=1,
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p.
```

Also `A+iBdir` and `r+it` are Gaussian units on `d`, so their affine projective slopes are admissible.

## 2. Local projective affine Fourier transform

For odd prime `p` put

```text
G_p=(Z[i]/pZ[i])^x/(Z/pZ)^x,
|G_p|=p-chi_4(p).
```

Represent finite projective classes by

```text
[1+i*x],
1+x^2 != 0 mod p,
```

with `[i]` as the omitted infinity class. For a nonprincipal local character `chi_p`, extend by zero at split isotropic nonunits and define

```text
G_p(chi_p;a)=sum_{x mod p} chi_p([1+i*x]) e_p(-a*x).
```

Since the full projective character sum is zero,

```text
G_p(chi_p;0)=-chi_p([i]),
|G_p(chi_p;0)|=1.
```

For `a!=0`, the classical finite-field Weil bound for this Kummer/Jacobi trace gives

```text
|G_p(chi_p;a)| <= 2*sqrt(p).
```

After normalisation

```text
c_{chi_p}(a)=G_p(chi_p;a)/p,
```

we obtain

```text
|c_{chi_p}(0)|=1/p,
|c_{chi_p}(a)|<=2/sqrt(p)  (a!=0),
sum_a |c_{chi_p}(a)|^2<=1.
```

## 3. CRT and primitive additive frequencies

Because `d` is squarefree,

```text
F_chi(x)=product_{p|d}F_{chi_p}(x mod p)
```

has exact additive Fourier expansion

```text
F_chi(x)=sum_{a mod d} c_chi(a)e_d(a*x).
```

Put

```text
q(a)=d/gcd(d,a).
```

Then primewise factorisation gives

```text
|c_chi(a)|
 <= 2^omega(q(a))*sqrt(q(a))/d
 = B^o(1)*sqrt(q(a))/d.
```

Hence for primitive frequency `(a,d)=1`,

```text
|c_chi(a)|<=d^(-1/2)*B^o(1).
```

If `z=gcd(d,a)` is the zero-frequency support, each `p|z` contributes exact squared mass `p^-2`, so

```text
sum_{gcd(a,d)>=Z}|c_chi(a)|^2
 <= Z^(-2)*B^o(1).
```

Therefore fixed-power additive-frequency deficit is automatically negligible in `L2`; the hard dual frequencies may be restricted to primitive frequencies up to endpoint-small support.

## 4. Projective conductor compression

Merged tH22 identifies the Hecke conductor norm as `d^2`, but t80 now rewrites the projective trace exactly using rational additive characters modulo

```text
PROJECTIVE_ADDITIVE_DUAL_MODULUS=d.
```

Thus the relevant additive dual modulus is linear in `d`, not the ambient ideal norm `d^2`, and the primitive Fourier coefficient has square-root size

```text
d^(-1/2)*B^o(1).
```

This is an exact representation/conductor-compression result. It is not yet a global inverse-fraction large-sieve estimate.

## 5. Physical inverse-fraction phases

Merged t71 gives

```text
A+iBdir=(-1+i)*conj(pi*U),
r+it=(-1+i)*conj(V).
```

Since `A,Bdir,r,t` are units on `d`, take affine slopes

```text
x_pi=Bdir/A mod d,
x_V=t/r mod d.
```

Fixed `U`, beta, sign, conjugation, and reciprocal/inversion orientation act by fixed projective Mobius maps. Consequently the t77 separated character kernel becomes a finite sum of additive rational inverse-fraction phases. Representative terms are

```text
e_d(a*Bdir*inv(A)),
e_d(a*A*inv(Bdir)),
e_d(b*t*inv(r)),
e_d(b*r*inv(t)),
```

with fixed signs and primitive `(a*b,d)=1` after the deficit peel.

Hence the hard ray-character problem is converted to an incomplete primitive inverse-fraction bilinear problem at rational modulus `d`.

## 6. Physical masks retained

The transform preserves

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular g through t78 four-cell coefficients,
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
primitive additive frequencies up to endpoint-small deficit.
```

The t78 Möbius divisor tensor remains valid.

## 7. Remaining receiver

Closed by t80:

```text
principal character,
fixed-power inactive character support,
fixed-power zero additive-frequency support,
d^2-vs-d representation mismatch,
conversion to rational inverse-fraction phases.
```

Still open:

```text
primitive inverse-fraction bilinear energy with the complete physical masks,
endpoint-small K_ext balanced physical cover energy,
whole-family improvement below 23/44.
```

Receiver:

```text
SharedUBalancedNearFullSupportPrimitiveProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionEnergy
```

## 8. tH decision

This is genuinely different from merged tH22, which audited the opaque Hecke/ray-character family. t80 has converted it to primitive additive inverse-fraction phases at rational modulus `d`.

```text
TH23_NEEDED=true
TH23_REQUESTED_OBJECT=NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH23=false
```

One-shot request:

```text
stages/stage14/14-t80/th23-target.md
```

## 9. Current ledger

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
MERGED_TH22_IMPORTED=true
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