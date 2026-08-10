# Stage14-tH22 target emitted by t77

Requested object:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

Audit only the post-t77 **ray-active** branch. Do not reopen Pell/class-number/regulator, canonical-largest-prime detection, t74 fixed `(ell,c)` fibers, t75 large-`g`, t75 high-imbalance Type-I, t76 large-`K_clean` spacing, or the tH21 negative DFI/Kuznetsov verdict before the ray-character reduction.

Condition on the fixed packet

```text
(U,epsilon,k,h,kappa,beta)
```

and the t77 split

```text
Q=K_clean,
Q_rad=gcd(Q,k)=gcd(Q,m),
M=Q_ray=Q/Q_rad.
```

The `Q_rad` support is already reduced to a split-mod-4 isotropic Gaussian-divisor selector of `B^o(1)` local orientation cost. It carries no moving canonical-`pi` phase and must not be charged with an artificial `1/Q_rad` density.

On `M`, retain the exact projective group

```text
G(M)=(Z[i]/M Z[i])^x/(Z/MZ)^x,
|G(M)|=prod_{p|M}(p-chi_4(p))=M*B^o(1).
```

After the t76/t77 fixed-beta + reciprocal orientation is conditioned, retain the exact class equality

```text
[pi]=[U]^-1 * I_beta * sigma([V])
```

and its character expansion

```text
1_{class equality}
=
1/|G(M)| sum_{chi in G(M)^}
 C_chi(U,beta) * chi(pi) * conjugate((chi o sigma)(V)).
```

The principal character gives the natural `M^-1 B^o(1)` projective density. The audit target is a uniform fixed-power bound for the **nonprincipal** contribution.

All physical masks must remain:

```text
ell=N(pi) canonical Gaussian direction prime,
ell^2>4B,
small angular g,
balanced primitive cover V=p+iq,
r=q-p,
t=q+p,
gcd(r,t) in {1,2},
r,t<sqrt(ell),
M deficient on the t76 scale,
c/odd(h)=R0*T0,
gcd(R0,T0)=1,
ell*c<2B,
ell*g*c<2B,
h*ell*(r^2+t^2)<=4B,
ell*delta<=Y_U,
delta=(r^2+t^2)/(2k),
fixed beta sign rule,
fixed reciprocal/inversion orientation.
```

In particular audit, with exact conductor/range matching:

1. large sieve for Hecke/ray-class characters over `Q(i)`;
2. Gaussian primes in ray classes / Bombieri–Vinogradov or Barban–Davenport–Halberstam over `Q(i)`;
3. whether projective characters trivial on rational scalars are a usable subfamily of standard ray-class/Hecke characters;
4. the actual conductor ideal of a projective character modulo rational squarefree `M` — do not confuse group size `~M` with ideal norm/conductor `~M^2`;
5. hybrid large sieve in the moving Gaussian prime variable `pi` and the primitive cover variable `V`;
6. duality/Cauchy using the exact separated kernel `chi(pi) * conjugate(chi_sigma(V))`;
7. whether the cover character sum with fixed norm structure `N(V)=k*delta`, balanced short coordinates and coprime residual columns has a theorem-ready bound;
8. whether dyadic/Mellin localization of `ell*c`, `ell*g*c`, short ellipse and `ell*delta` retains a fixed-power saving;
9. whether the exact angular-gcd allocation can be Möbius/divisor-switched into admissible coefficient sequences without paying back the saving;
10. the full deficient range of `M` relative to the Gaussian-prime scale and `R*T`.

A theorem name alone is insufficient. `APPLICABLE=true` requires an explicit adapter preserving the conductor, quantifier order, moving-prime scale, projective-character family, cover sequence, and all masks above.

Required verdict fields:

```text
STAGE14_TH22=COMPLETE_...
T77_PROJECTIVE_RAY_KERNEL_RETAINED=...
T77_RADIAL_SELECTOR_REOPENED=false
PROJECTIVE_CHARACTERS_EMBED_IN_STANDARD_HECKE_RAY_FAMILY=...
PROJECTIVE_CHARACTER_CONDUCTOR_IDENTIFIED=...
GAUSSIAN_PRIME_RAY_CLASS_LARGE_SIEVE_APPLICABLE=...
GAUSSIAN_BV_BDH_APPLICABLE=...
HYBRID_PI_V_CHARACTER_LARGE_SIEVE_APPLICABLE=...
COVER_CHARACTER_SEQUENCE_BOUND_APPLICABLE=...
FULL_PHYSICAL_MASKS_RETAINED=...
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=...
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
TH23_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<read latest main>
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=...
NEXT=Stage14-t78
```

Create the dedicated `stages/stage14/14-tH22/` area, literature applicability note where useful, deterministic audit/frozen boundary, dedicated CI, and PR. Do not claim a power saving unless the complete physical mask and actual Hecke conductor range survive the adapter.
