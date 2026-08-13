# Stage14-tH23 target emitted by t80

Requested object:

```text
NearFullSupportProjectiveGaussDualCanonicalPrimeShortCoverInverseFractionLargeSieve
```

Audit only the post-t80 primitive additive inverse-fraction kernel. Do not reopen Pell/class-number/regulator, canonical-largest-prime detection, t74 fixed `(ell,c)` fibers, t75 large-`g`, t75 high-imbalance Type-I, t76 large-`K_clean` spacing, t77 projective-ray conversion, t78 angular-gcd tensorization, t79 principal/inactive-support removal, or merged tH22's negative verdict for the pre-dual Hecke/ray family.

Fix `(U,epsilon,k,h,kappa,beta)` and retain

```text
K=oddpart(kappa),
K_ext=K/gcd(K,k),
M=K/gcd(K,g*k),
d=d(chi)=M/B^o(1).
```

Merged tH22 gives

```text
f_fin(chi)=(d),
N f_fin(chi)=d^2.
```

t80 gives the exact affine projective Fourier expansion

```text
|c_{chi_p}(0)|=1/p,
|c_{chi_p}(a)|<=2/sqrt(p) for a!=0,
F_chi(x)=sum_{a mod d}c_chi(a)e_d(a*x),
|c_chi(a)|<=B^o(1)*sqrt(d/gcd(d,a))/d.
```

Fixed-power zero-frequency support is already removed in `L2`, so hard dual frequencies may be taken primitive:

```text
(a,d)=1,
|c_chi(a)|<=d^(-1/2)B^o(1).
```

Do not charge the ambient ideal norm `d^2` again after this exact transform: the additive dual modulus is `d`.

Physical coordinates are

```text
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p,
A+iBdir=(-1+i)conj(pi*U),
r+it=(-1+i)conj(V),
gcd(d,A*Bdir*r*t)=1.
```

After fixed packet/orientation, representative hard phases are

```text
e_d(a*Bdir*inv(A)),
e_d(a*A*inv(Bdir)),
e_d(b*t*inv(r)),
e_d(b*r*inv(t)),
```

with primitive frequencies and fixed signs.

Retain all masks:

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular g via t78 four-cell Möbius coefficients,
balanced primitive cover,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
ell*odd(h)*odd(r)*odd(t)<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
delta=(r^2+t^2)/(2k),
fixed beta sign rule,
fixed reciprocal/inversion orientation,
d=M/B^o(1).
```

Audit exact applicability of:

1. fixed-squarefree-modulus incomplete Kloosterman/inverse-fraction large sieve;
2. Deshouillers-Iwaniec / Bettin-Chandee / spectral or additive duality for `e_d(a*x/y)`;
3. canonical Gaussian-prime direction versus balanced primitive-cover bilinear forms;
4. whether the `d^-1/2` Gauss coefficient compensates frequency count after Cauchy/duality;
5. extra orthogonality from summing near-full-support projective characters before/after dualization;
6. theorem-ready `L2` norms for t78 four-cell coefficients after localization;
7. complementary-modulus or Type-I/II switching from `ell*odd(h)*odd(r)*odd(t)<2B` and the short ellipse;
8. whether fixed `d<M<R*T*B^o(1)` lies in a proved inverse-fraction range;
9. split/inert distinctions after rational additive dualization;
10. elementary closure of endpoint-small `K_ext` balanced physical energy.

A theorem name alone is insufficient. `APPLICABLE=true` requires a complete adapter preserving the fixed modulus/frequency range and every physical mask.

Required verdict fields:

```text
STAGE14_TH23=COMPLETE_...
T80_PROJECTIVE_GAUSS_DUALIZATION_RETAINED=...
T80_ADDITIVE_DUAL_MODULUS_RETAINED=d
T79_PRINCIPAL_CHARACTER_REOPENED=false
T79_FIXED_POWER_INACTIVE_SUPPORT_REOPENED=false
T78_GCD_TENSORIZATION_REOPENED=false
TH22_PRE_DUAL_NEGATIVE_VERDICT_REOPENED=false
PRIMITIVE_INVERSE_FRACTION_KERNEL_RETAINED=...
GAUSS_COEFFICIENT_SQRT_GAIN_RETAINED=...
FIXED_MODULUS_KLOOSTERMAN_LARGE_SIEVE_APPLICABLE=...
INVERSE_FRACTION_BILINEAR_ESTIMATE_APPLICABLE=...
SPECTRAL_DUALITY_APPLICABLE=...
CANONICAL_GAUSSIAN_PRIME_SIDE_BOUND_APPLICABLE=...
BALANCED_COVER_SIDE_BOUND_APPLICABLE=...
FOUR_CELL_COEFFICIENT_L2_THEOREM_READY=...
FULL_PHYSICAL_MASKS_RETAINED=...
OFF_THE_SHELF_PRIMITIVE_INVERSE_FRACTION_POWER_SAVING_PROVED=...
CERTIFIED_PRIMITIVE_INVERSE_FRACTION_B_POWER_SAVING_EXPONENT=...
ENDPOINT_SMALL_EXTERNAL_KAPPA_ENERGY_CLOSED=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
TH24_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<read latest main>
STRICT_SUBSQRT_POWER_SAVING_PROVED=<read latest main>
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=...
NEXT=Stage14-t81
```

Create dedicated `stages/stage14/14-tH23/`, a literature note where useful, deterministic audit/frozen boundary, dedicated CI, and PR. Do not claim a saving unless the complete physical masks and actual fixed-modulus/frequency ranges survive the adapter.
