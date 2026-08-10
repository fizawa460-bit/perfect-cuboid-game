# Stage14-t71 — physical Gaussian angular chart and squareclass four-cell transfer

## Purpose

Merged Stage14-t70 closes the large full-common-support branch by compressing the four noncanonical Cayley overlap components into one primitive root line. The live fixed-`U` obstruction is the small-`J` branch

```text
SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy.
```

The t70 synthetic `J=1` clique shows that generic Cayley algebra alone cannot force a large common-support modulus. Stage14-t71 restores the exact physical Gaussian multiplication and the primitive cover. This reveals a second, disjoint source of cross-state arithmetic data: the common squareclass `kappa` itself.

The main conclusions are:

1. the direction and cover angular deficits are 45-degree Gaussian coordinates;
2. the four factors of the Kummer quartic are the four real/imaginary Gaussian product components;
3. every state has a canonical numerator/denominator squarefree split `kappa=alpha*beta` coming from its reduced Cayley value;
4. two states in the same squareclass produce an exact four-cell decomposition of all of `kappa`;
5. these four cells are coprime to the t70 Cayley common modulus `J` and transfer, with only `B^o(1)` prime-orientation decoration, to cross-state Gaussian components.

Thus small `J` does not erase all cross-state modulus structure unless the odd squareclass itself is small (especially `kappa=1`). No new whole-family saving is claimed at t71.

Merged Stage14-s7-31 supplies the current whole-family ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8.
```

---

## 1. Fixed-`U` Gaussian angular chart

Fix one dominant invisible packet. Write

```text
z=a+i b = pi*U,
N(pi)=ell,
N(U)=m,
V=p+i q,
N(V)=k*delta,
h*k=epsilon*m.
```

The reciprocal physical chamber gives

```text
0<a<b,
0<p<q.
```

Define the 45-degree angular coordinates

```text
A=b-a,
B=b+a,
X=q-p,
Y=q+p.
```

Then

```text
A^2+B^2 = 2*ell*m,
X^2+Y^2 = 2*k*delta,
gcd(A,B)|2,
gcd(X,Y)|2.
```

Moreover

```text
A+iB = (-1+i)*conj(z)
     = (-1+i)*conj(pi)*conj(U),

X+iY = (-1+i)*conj(V).
```

If `pi=c+i d` and `U=R+i S`, then exactly

```text
A=(S-R)c+(R+S)d,
B=(R+S)c+(R-S)d.
```

The determinant of this linear map `(c,d)->(A,B)` is

```text
-2*(R^2+S^2) = -2m.
```

Hence away from the fixed support `2m`, the angular direction pair is an invertible linear image of the canonical Gaussian prime coordinates. This is the precise fixed-`U` structure absent from the t70 synthetic small-`J` guard.

```text
FIXED_U_DIRECTION_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED=true
DIRECTION_ANGULAR_MAP_DETERMINANT=-2m
COVER_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED=true
```

---

## 2. Angular deficits and exact Cayley identity

The t65 angular deficits become simply

```text
D_pi=b^2-a^2=A*B,
D_V=q^2-p^2=X*Y.
```

Therefore the exact t65 Cayley identity can be written without radial labels as

```text
C(s)=(1+s)/(1-s)
    = A*B*(X^2+Y^2) / (X*Y*(A^2+B^2)).
```

Equivalently, with

```text
r=A/B=(1-t)/(1+t),
w=X/Y=(1-x)/(1+x),
```

we have

```text
C(s)= r*(1+w^2)/(w*(1+r^2)).
```

This is the exact angular form of the split-torus law from t64/t65.

```text
ANGULAR_CAYLEY_RATIO_IDENTITY_PROVED=true
```

---

## 3. The four Kummer factors are Gaussian product components

Define

```text
L1=A*Y-B*X = 2*(b*p-a*q),
L2=B*Y-A*X = 2*(a*q+b*p),
L3=A*Y+B*X = 2*(b*q-a*p),
L4=B*Y+A*X = 2*(b*q+a*p).
```

Then

```text
s = (L1*L2)/(L3*L4),
F = (L1*L2*L3*L4)/16.
```

The four components have the exact Gaussian product identities

```text
2*z*V       = -L3 + i*L2,
2*conj(z)*V =  L4 - i*L1.
```

Since `z=pi U`, this is

```text
2*pi*U*V             = -L3+iL2,
2*conj(pi)*conj(U)*V =  L4-iL1.
```

Consequently

```text
L2^2+L3^2 = L1^2+L4^2
          = 4*ell*m*k*delta.
```

The squareclass is therefore exactly

```text
kappa = sf(L1*L2*L3*L4),
```

because `16` is a square.

```text
PHYSICAL_KUMMER_FACTORS_ARE_GAUSSIAN_PRODUCT_COMPONENTS=true
GAUSSIAN_COMPONENT_NORM_IDENTITY_PROVED=true
KAPPA_EQUALS_FOUR_GAUSSIAN_COMPONENT_SQUAREFREE_KERNEL=true
```

---

## 4. The t65 cross-cancellation has a 2x2 angular matrix

Write `odd(T)` for the odd part. Since

```text
gcd(odd(A),odd(B))=1,
gcd(odd(X),odd(Y))=1,
```

the t65 cancellation

```text
g=gcd(odd(A*B),odd(X*Y))
```

has the unique four-cell factorization

```text
g_AX=gcd(odd(A),odd(X)),
g_AY=gcd(odd(A),odd(Y)),
g_BX=gcd(odd(B),odd(X)),
g_BY=gcd(odd(B),odd(Y)),

g=g_AX*g_AY*g_BX*g_BY,
```

and the four cells are pairwise coprime.

They also identify exactly which numerator/denominator Gaussian components carry the angular cancellation:

```text
odd(gcd(L1,L3)) = g_AX*g_BY,
odd(gcd(L2,L4)) = g_AY*g_BX.
```

Thus the moving cross-gcd in t65 is not an opaque polynomial gcd. It is the 2x2 matching matrix between the two primitive angular pairs `(A,B)` and `(X,Y)`.

```text
T65_CROSS_GCD_ANGULAR_2X2_DECOMPOSITION_PROVED=true
ANGULAR_CANCELLATION_COMPONENT_DICTIONARY_PROVED=true
```

---

## 5. Every state has a canonical signed squareclass split

Let

```text
N=Pplus,
D=Pminus,
gcd(N,D)=1,
N>D>0.
```

Merged t65/t69 give

```text
C(s)=N/D,
(N-D)/(N+D)=s.
```

Put

```text
d0=gcd(N-D,N+D) in {1,2},
A0=(N-D)/d0,
B0=(N+D)/d0.
```

Then `gcd(A0,B0)=1` and

```text
A0/B0 = kappa*(r/t)^2
```

for a reduced rational square. Therefore, uniquely,

```text
A0=alpha*r^2,
B0=beta*t^2,
alpha,beta squarefree,
gcd(alpha,beta)=1,
alpha*beta=kappa.
```

If

```text
eta=2/d0 in {1,2},
```

then exactly

```text
eta*N = alpha*r^2 + beta*t^2,
eta*D = beta*t^2 - alpha*r^2.
```

Since the canonical prime satisfies `ell|D` and `gcd(ell,kappa)=1`, it follows that

```text
beta*t^2 == alpha*r^2  (mod ell),
gcd(ell,r*t)=1.
```

This is a state-local private root condition; t68/tH18 already show that it must not be incorrectly transferred to another state.

The new content is the exact split

```text
kappa=alpha*beta,
```

which can be fixed at only `tau(kappa)=B^o(1)` cost.

```text
CAYLEY_SIGNED_SQUARECLASS_SPLIT_PROVED=true
CAYLEY_SIGNED_SPLIT_MULTIPLICITY=Bo1
PRIVATE_ELL_SIGNED_SPLIT_ROOT_CONGRUENCE_PROVED=true
```

---

## 6. Same squareclass gives a four-cell transfer of all `kappa`

Take two physical states `i,j` in the same fixed-`U` packet and the same squareclass `kappa`. Let

```text
kappa=alpha_i*beta_i=alpha_j*beta_j
```

be the canonical signed splits from Section 5.

Define

```text
K_--=gcd(alpha_i,alpha_j),
K_-+=gcd(alpha_i,beta_j),
K_+-=gcd(beta_i,alpha_j),
K_++=gcd(beta_i,beta_j).
```

Because both `(alpha,beta)` pairs are coprime squarefree splittings of the same `kappa`, the four cells are pairwise coprime and

```text
boxed:
K_--*K_-+*K_+-*K_++ = kappa.
```

Set

```text
K_agree = K_--*K_++,
K_switch = K_-+*K_+-.
```

Then

```text
K_agree*K_switch=kappa,
max(K_agree,K_switch)>=sqrt(kappa),
max(K_--,K_-+,K_+-,K_++)>=kappa^(1/4).
```

This is the exact numerator/denominator analogue of the agreement/switch cell decomposition used successfully elsewhere in Stage14, but here it is derived directly from the physical Cayley squareclass.

```text
SAME_KAPPA_CAYLEY_SIGNED_FOUR_CELL_DECOMPOSITION_PROVED=true
KAPPA_AGREE_SWITCH_PRODUCT_IDENTITY_PROVED=true
```

---

## 7. The four cells transfer to physical Gaussian components

For each state,

```text
s=(L1*L2)/(L3*L4).
```

After reducing this rational number, `alpha` is exactly the squarefree kernel on the numerator side and `beta` the squarefree kernel on the denominator side. Hence every odd prime in

```text
alpha
```

has odd residual valuation in the numerator pair `{L1,L2}`, while every odd prime in

```text
beta
```

has odd residual valuation in the denominator pair `{L3,L4}`.

For each prime of a four-cell `K_sigma_tau`, choose which one of the two physical components on side `sigma` of state `i` and which one of the two components on side `tau` of state `j` carries the required odd valuation. The number of such primewise orientation patterns is

```text
<=4^omega(kappa)=B^o(1).
```

After fixing this divisor-many orientation decoration, each `K_sigma_tau` is refined into at most four pairwise-coprime component moduli, each dividing a concrete cross-state pair

```text
L_a(i), L_b(j).
```

Thus **all odd squareclass support transfers to actual Gaussian product components**, even on the t70 small-`J` branch.

```text
KAPPA_FOUR_CELL_REFINES_TO_GAUSSIAN_COMPONENT_TRANSFER=true
GAUSSIAN_COMPONENT_TRANSFER_ORIENTATION_MULTIPLICITY=Bo1
```

---

## 8. The `kappa` transfer is disjoint from the t70 Cayley modulus

Merged t69 proves statewise

```text
gcd(Pplus*Pminus,kappa)=1.
```

The t70 common modulus `J_ij` divides the noncanonical odd support of both states' `Pplus*Pminus`. Therefore

```text
boxed:
gcd(J_ij,kappa)=1.
```

Hence the small-`J` condition does not consume or duplicate the squareclass four-cell modulus. The two structures are prime-support orthogonal:

```text
Cayley common support: J_ij,
Kummer squareclass support: kappa=K_agree*K_switch.
```

This is why the t70 `kappa=1` synthetic clique is a valid no-go for generic Cayley reconstruction but does not rule out a physical large-`kappa` component-transfer argument.

```text
CAYLEY_COMMON_SUPPORT_AND_KAPPA_TRANSFER_COPRIME=true
SMALL_J_DOES_NOT_ERASE_KAPPA_COMPONENT_TRANSFER=true
```

---

## 9. Synthetic split-switch guard

At the reduced Cayley level take common squareclass

```text
kappa=15.
```

State 1:

```text
Pplus=4,
Pminus=1,
s=3/5,
(alpha,beta)=(3,5).
```

State 2:

```text
Pplus=17,
Pminus=7,
s=5/12,
(alpha,beta)=(5,3).
```

Both rational values have squareclass `15`, while

```text
gcd(Pplus_1*Pminus_1,
    Pplus_2*Pminus_2)=1.
```

Thus the Cayley common support is `J=1`, but

```text
K_agree=1,
K_switch=15.
```

This is an algebraic guard only, not a physical cuboid reconstruction. It demonstrates that small Cayley overlap and large squareclass-switch support are logically compatible.

---

## 10. Revised receiver

The t70 receiver is sharpened to

```text
SharedUSmallCayleySupportGaussianSquareclassFourCellEnergy.
```

It counts same-`kappa` physical pairs after the t67--t70 removals, retaining

```text
fixed U,
private canonical ell_i,ell_j,
small full Cayley common support J_ij,
45-degree Gaussian angular coordinates,
primitive V_i,V_j,
canonical signed splits alpha_i*beta_i=alpha_j*beta_j=kappa,
K_--,K_-+,K_+-,K_++ component-transfer cells.
```

The next stage should exploit the large/small squareclass dichotomy:

- large `kappa`: use the four-cell / Gaussian-component transfer moduli before any further uncharging;
- small `kappa` (including `kappa=1`): retain the full physical Gaussian product equations and test direct reconstruction/fiber bounds.

No theorem on this remaining energy is claimed here.

```text
SHARED_U_SMALL_CAYLEY_SUPPORT_GAUSSIAN_SQUARECLASS_FOUR_CELL_ENERGY_PROVED=false
```

---

## 11. tH decision

A new tH line is **not yet needed**. The current obstruction has just acquired an exact four-cell decomposition and Gaussian component transfer that has not been used analytically. Stage14-t72 should first perform the internal large/small-`kappa` split and determine the root-line / bilinear spacing available from the component cells.

Only if t72 leaves a genuine averaged theorem for cross-state Gaussian component divisibility should tH19 be opened.

```text
TH19_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
```

---

## Shared exponent ledger

Merged Stage14-s7-31 proves

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
```

for the global Stage14 problem. Stage14-t71 imports this ledger and proves no additional whole-family saving.

```text
MERGED_S7_31_GLOBAL_5_8_LEDGER_IMPORTED=true
T71_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
```

---

## Locked boundary

```text
STAGE14_T71=COMPLETE_PHYSICAL_GAUSSIAN_ANGULAR_AND_SQUARECLASS_FOUR_CELL_TRANSFER_REDUCTION
MERGED_T70_IMPORTED=true
MERGED_S7_31_GLOBAL_5_8_LEDGER_IMPORTED=true
FIXED_U_DIRECTION_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED=true
DIRECTION_ANGULAR_MAP_DETERMINANT=-2m
COVER_45_DEGREE_GAUSSIAN_LINEARIZATION_PROVED=true
ANGULAR_CAYLEY_RATIO_IDENTITY_PROVED=true
PHYSICAL_KUMMER_FACTORS_ARE_GAUSSIAN_PRODUCT_COMPONENTS=true
GAUSSIAN_COMPONENT_NORM_IDENTITY_PROVED=true
KAPPA_EQUALS_FOUR_GAUSSIAN_COMPONENT_SQUAREFREE_KERNEL=true
T65_CROSS_GCD_ANGULAR_2X2_DECOMPOSITION_PROVED=true
ANGULAR_CANCELLATION_COMPONENT_DICTIONARY_PROVED=true
CAYLEY_SIGNED_SQUARECLASS_SPLIT_PROVED=true
CAYLEY_SIGNED_SPLIT_MULTIPLICITY=Bo1
PRIVATE_ELL_SIGNED_SPLIT_ROOT_CONGRUENCE_PROVED=true
SAME_KAPPA_CAYLEY_SIGNED_FOUR_CELL_DECOMPOSITION_PROVED=true
KAPPA_AGREE_SWITCH_PRODUCT_IDENTITY_PROVED=true
KAPPA_FOUR_CELL_REFINES_TO_GAUSSIAN_COMPONENT_TRANSFER=true
GAUSSIAN_COMPONENT_TRANSFER_ORIENTATION_MULTIPLICITY=Bo1
CAYLEY_COMMON_SUPPORT_AND_KAPPA_TRANSFER_COPRIME=true
SMALL_J_DOES_NOT_ERASE_KAPPA_COMPONENT_TRANSFER=true
SHARED_U_SMALL_CAYLEY_SUPPORT_GAUSSIAN_SQUARECLASS_FOUR_CELL_ENERGY_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
T71_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
TH19_NEEDED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
NEXT=Stage14-t72
```
