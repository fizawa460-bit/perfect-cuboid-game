# Stage14-t78 — external squareclass support, radial-only reduction, and exact four-cell gcd tensorization

## Status

`COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION`

Stage14-t78 consumes merged t77 and the merged t75/t76 arithmetic behind it.  It does not use an unmerged tH22 result.  The current strongest merged whole-family theorem is Stage14-4cx:

```text
V(B) << B^(23/44+o(1)).
```

No additional whole-family power saving is claimed here.

The t77 notation is

```text
A=b-a,
Bdir=b+a,
r=q-p,
t=q+p,
K=oddpart(kappa),
g=gcd(oddpart(A*Bdir),oddpart(r*t)),
Q=K/gcd(K,g),
Q_rad=gcd(Q,k),
M=Q_ray=Q/Q_rad.
```

The main new observation is that the ray modulus has the closed form

```text
boxed:
M = K/gcd(K,g*k).
```

Thus the analytic ray modulus is exactly the squarefree odd squareclass support which is carried by neither the angular gcd nor the fixed radial norm.

---

## 1. Exact external-squareclass formula

Because `K` is squarefree, primewise there are only three possibilities for a prime `p|K`:

1. `p|g`: it is removed in `K_bad=gcd(K,g)`;
2. `p∤g` but `p|k`: it survives to `Q` and is then radial support in `Q_rad`;
3. `p∤gk`: it survives to the ray modulus `M`.

Consequently

```text
Q = K/gcd(K,g),
Q_rad = gcd(Q,k),
M = Q/Q_rad
  = K/gcd(K,g*k).
```

Define the external squareclass support relative to the fixed radial norm

```text
K_ext := K/gcd(K,k).
```

Then exactly

```text
boxed:
M = K_ext/gcd(K_ext,g).
```

and therefore

```text
boxed:
M=1  <=>  K_ext | g.
```

This sharpens the qualitative t77 radial/ray split: radial-only is not a free exceptional family.  It requires all squareclass support outside the fixed norm `k` to be absorbed by the already-exposed angular gcd.

```text
RAY_MODULUS_EQUALS_EXTERNAL_KAPPA_OUTSIDE_GK=true
RADIAL_ONLY_IFF_EXTERNAL_KAPPA_DIVIDES_ANGULAR_GCD=true
```

---

## 2. Consequence for the radial-only branch

Merged t75 proved for every threshold `G` a one-state large-angular-gcd parameter-mass bound

```text
N_{g>=G} << B^(1+o(1))/G.
```

Since `M=1` implies `g>=K_ext`, the radial-only contribution obeys the inherited bound

```text
boxed:
N_radial-only(K_ext) << B^(1+o(1))/K_ext.
```

This is only a one-state parameter-mass statement, exactly as in t75; it is not promoted here to a pair-energy theorem.

In particular every radial-only block with fixed-power `K_ext` is already subsumed by the t75 large-`g` mechanism.  A genuinely separate radial-only residue can remain only when

```text
K_ext=B^o(1).
```

Equivalently, up to endpoint-small support, all odd squareclass primes then lie in the fixed radial norm `k`.

```text
RADIAL_ONLY_FIXED_POWER_EXTERNAL_SUPPORT_SUBSUMED_BY_T75_LARGE_G=true
RADIAL_ONLY_LIVE_ONLY_IF_EXTERNAL_KAPPA_ENDPOINT_SMALL=true
```

The endpoint-small radial residue is not declared empty and is left for t79.

---

## 3. Exact four-cell decomposition of the angular gcd

Put

```text
A0=oddpart(A),
B0=oddpart(Bdir),
R=oddpart(r),
T=oddpart(t).
```

Primitive direction and cover coordinates give

```text
gcd(A0,B0)=1,
gcd(R,T)=1.
```

Define the four cross cells

```text
d_AR = gcd(A0,R),
d_AT = gcd(A0,T),
d_BR = gcd(B0,R),
d_BT = gcd(B0,T).
```

Every two distinct cells are coprime.  Moreover

```text
boxed:
g=d_AR*d_AT*d_BR*d_BT.
```

Define residual coordinates

```text
A1=A0/(d_AR*d_AT),
B1=B0/(d_BR*d_BT),
R1=R /(d_AR*d_BR),
T1=T /(d_AT*d_BT).
```

Then

```text
gcd(A1*B1,R1*T1)=1.
```

Thus the angular gcd is not one opaque coupling: it is a unique four-cell allocation between two primitive direction columns and two primitive cover columns.

```text
ANGULAR_GCD_FOUR_CELL_DECOMPOSITION_PROVED=true
ANGULAR_GCD_FOUR_CELLS_PAIRWISE_COPRIME=true
ANGULAR_GCD_RESIDUAL_CROSS_SUPPORT_COPRIME=true
```

---

## 4. The t74 cofactor is the residual cover product

Write

```text
H=oddpart(h),
c=oddpart(Pminus/ell).
```

Merged t74/t75 gives

```text
c/H = oddpart(r*t)/g.
```

The four-cell notation makes this exact relation

```text
boxed:
c/H = R1*T1.
```

Equivalently

```text
boxed:
g*c = H*R*T.
```

This eliminates `g` completely from the strongest t74 hyperbola:

```text
ell*g*c < 2B
```

becomes

```text
boxed:
ell*H*R*T < 2B.
```

Since `ell^2>4B`, it follows in particular that

```text
H*R*T < sqrt(B).
```

The weaker `ell*c<2B` is automatic from `g>=1` and the displayed identity.  The canonical short-cofactor condition `2c<ell` becomes

```text
2*H*R*T < ell*g.
```

Hence, after the exact four-cell tuple is conditioned, every remaining archimedean coupling is between the direction scale `ell` and a cover-only statistic (`R*T`, `r^2+t^2`, or `delta`).

```text
SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD=true
SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true
ODD_COVER_PRODUCT_IS_SQRT_B_SHORT=true
```

---

## 5. Only the K-supported part of the four cells changes the ray modulus

Define

```text
s_AR=gcd(K,d_AR),
s_AT=gcd(K,d_AT),
s_BR=gcd(K,d_BR),
s_BT=gcd(K,d_BT).
```

The four `s`-cells are pairwise coprime and

```text
s_AR*s_AT*s_BR*s_BT = gcd(K,g).
```

Because `K` is fixed in the t packet, assigning every prime of `gcd(K,g)` to one of four cells costs at most

```text
4^omega(K)=B^o(1)
```

local orientations.

Write

```text
e_AR=d_AR/s_AR,
e_AT=d_AT/s_AT,
e_BR=d_BR/s_BR,
e_BT=d_BT/s_BT.
```

Then every `e`-cell is coprime to `K`.  In particular varying the entire K-coprime part

```text
g_perp=e_AR*e_AT*e_BR*e_BT
```

does not alter `Q`, `Q_rad`, `M`, the projective ray group, or the t77 character family.

```text
RAY_MODULUS_DEPENDS_ONLY_ON_K_SUPPORTED_GCD_CELLS=true
K_COPRIME_ANGULAR_GCD_DOES_NOT_CHANGE_RAY_CHARACTER_FAMILY=true
K_SUPPORTED_FOUR_CELL_ORIENTATION_MULTIPLICITY=Bo1
```

This is the exact coefficient bookkeeping needed before applying a ray-character large sieve uniformly in the remaining small angular-gcd variables.

---

## 6. Exact Möbius tensorization of the angular gcd constraints

For positive integers `x,y,d`,

```text
1_{gcd(x,y)=d}
=
1_{d|x}1_{d|y}
 sum_{e | x/d, e | y/d} mu(e).
```

Each summand factors as

```text
mu(e) * 1_{d e|x} * 1_{d e|y}.
```

Apply this independently to

```text
(A0,R), (A0,T), (B0,R), (B0,T).
```

For a fixed four-cell tuple the exact angular-gcd indicator is therefore a finite Möbius sum of products

```text
(direction divisibility coefficient in A0,B0)
*
(cover divisibility coefficient in R,T).
```

Internal primitivity `gcd(A0,B0)=1` is direction-only and `gcd(R,T)=1` is cover-only.  Pointwise, the number of divisor terms is bounded by a fixed power of the divisor function and hence is `B^o(1)`.

Thus the arithmetic gcd part of the physical weight tensorizes exactly after divisor switching; this is stronger than merely saying divisor switching is formally available.

```text
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
ANGULAR_GCD_MOBIUS_POINTWISE_MULTIPLICITY=Bo1
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
```

We do **not** claim that the complete hard archimedean cutoff is one pure tensor without localization.  Dyadic/Mellin localization still has to be included in any analytic theorem adapter.

```text
FULL_HARD_CUTOFF_SINGLE_TENSOR_FACTORIZATION_PROVED=false
```

---

## 7. Effect on the t77 ray-character receiver

Merged t77 gives on the ray-active modulus `M`

```text
[pi]=[U]^-1 I_beta sigma([V])
```

inside

```text
G(M)=(Z[i]/MZ[i])^x/(Z/MZ)^x,
```

and therefore the exact character kernel

```text
C_chi(U,beta) * chi(pi) * conjugate((chi o sigma)(V)).
```

Stage14-t78 now shows that:

1. the modulus is exactly `M=K/gcd(K,gk)`;
2. its dependence on the moving angular gcd is only through the `K`-supported four-cell allocation;
3. all K-coprime gcd allocation admits exact Möbius tensorization;
4. the strongest `ell*g*c` cutoff becomes the tensor-compatible product cutoff `ell*H*R*T<2B`.

Therefore the ray-active analytic object is narrowed to

```text
SharedUSmallOddKappaFixedTagBalancedExternalKappaRayCharacterFourCellMobiusTypeIIEnergy.
```

No nonprincipal character saving is proved here.

---

## 8. tH22 / tH23 decision

The tH22 request remains necessary:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve.
```

Stage14-t78 removes one of its requested adapter questions — exact angular-gcd Möbius/divisor-switch tensorization — but does not prove the Hecke/ray-character large sieve itself.

No tH23 should be opened before tH22 returns and t79 consumes the endpoint-small radial residue / principal-character packet.

```text
TH22_NEEDED=true
TH22_TARGET_REFINED_BY_T78=true
TH23_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH22=false
```

---

## 9. Current shared exponent

Merged Stage14-4cx is currently strongest:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
```

Stage14-t78 proves no additional whole-family power saving.

---

## Locked boundary

```text
STAGE14_T78=COMPLETE_EXTERNAL_KAPPA_RADIAL_REDUCTION_AND_FOUR_CELL_MOBIUS_TENSORIZATION
MERGED_T77_IMPORTED=true
RAY_MODULUS_EQUALS_EXTERNAL_KAPPA_OUTSIDE_GK=true
RAY_MODULUS_FORMULA=M=K/gcd(K,g*k)
EXTERNAL_KAPPA=K/gcd(K,k)
RAY_MODULUS_EXTERNAL_FORMULA=M=K_ext/gcd(K_ext,g)
RADIAL_ONLY_IFF_EXTERNAL_KAPPA_DIVIDES_ANGULAR_GCD=true
RADIAL_ONLY_FIXED_POWER_EXTERNAL_SUPPORT_SUBSUMED_BY_T75_LARGE_G=true
RADIAL_ONLY_LIVE_ONLY_IF_EXTERNAL_KAPPA_ENDPOINT_SMALL=true
ANGULAR_GCD_FOUR_CELL_DECOMPOSITION_PROVED=true
ANGULAR_GCD_FOUR_CELLS_PAIRWISE_COPRIME=true
ANGULAR_GCD_RESIDUAL_CROSS_SUPPORT_COPRIME=true
COFACTOR_RESIDUAL_PRODUCT_IDENTITY=c/H=R1*T1
SHARP_ELL_G_C_HYPERBOLA_CANCELS_ANGULAR_GCD=true
SHARP_HYPERBOLA_REWRITTEN_AS_ELL_H_R_T=true
ODD_COVER_PRODUCT_IS_SQRT_B_SHORT=true
RAY_MODULUS_DEPENDS_ONLY_ON_K_SUPPORTED_GCD_CELLS=true
K_COPRIME_ANGULAR_GCD_DOES_NOT_CHANGE_RAY_CHARACTER_FAMILY=true
ANGULAR_GCD_MOBIUS_TENSOR_DECOMPOSITION_PROVED=true
CELL_CONDITIONED_ARITHMETIC_WEIGHT_TENSORIZATION_PROVED=true
FULL_HARD_CUTOFF_SINGLE_TENSOR_FACTORIZATION_PROVED=false
RAY_ACTIVE_TYPEII_ENERGY_PROVED=false
TH22_NEEDED=true
TH22_TARGET_REFINED_BY_T78=true
TH23_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH22=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=23/44
T78_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t79
```
