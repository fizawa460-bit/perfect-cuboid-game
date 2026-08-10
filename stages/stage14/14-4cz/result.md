# Stage14-4cz — same-side root-gcd square transfer and globally odd-primitive 23/44 receiver

## Status

`COMPLETE_SAMESIDE_ROOT_GCD_SQUARE_ROW_COLUMN_TRANSFER_AND_GLOBALLY_ODD_PRIMITIVE_23_44_RECEIVER`

Stage14-4cz consumes merged `Stage14-4cy`, merged `Stage14-s7-40`, and the exact root-gcd placement of merged `Stage14-s7-37`, on latest main through merged `Stage14-t79`.

The entering canonical whole-family theorem is

```text
V(B) << B^(23/44+o(1)).
```

Merged 4cy/s7-40 have already collapsed every possible `23/44` saturation packet to the unique endpoint

```text
theta=23/88,
phi=19/88,
chi=j=9/44,
H=B^o(1),
C=J=C_Cayley*B^o(1),
```

with remaining column and row supports both of exponent `1/22`.

Stage14-4cz proves that the same-side odd root gcd enters **both** of those short coordinates with square strength. A dyadic same-side gcd `K=B^(kappa+o(1))` therefore gives the charged-once endpoint count

```text
E_4cz(kappa)
 <= 19/44
    + kappa
    + 2*max(0,1/22-2kappa).
```

The maximum remains `23/44`, but it is attained only at `kappa=0`. Thus every fixed-power same-side root-gcd stratum is strictly subcritical; if `kappa>=1/132`, that stratum is already at or below square-root scale.

No external sieve, determinant theorem, genus-one theorem, or auxiliary H/tH theorem is used.

---

## 1. Imported unique endpoint

Use the physical root coordinates

```text
P1=(R*S)*x1^2,
Q1=(T*J0)*y1^2,
P2=(R*T)*x2^2,
Q2=(S*J0)*y2^2,
```

with statewise reducedness

```text
gcd(x1,y1)=gcd(x2,y2)=1.
```

To avoid conflict with the joint common core, denote the xi agreement cell by `J0`; the joint core remains `J`.

Merged 4cy/s7-40 give, for every possible 23/44 saturation sequence,

```text
theta=23/88,
phi=19/88,
chi=j=9/44,
C=B^(9/44+o(1)),
J=C*B^o(1),
C_Cayley=C*B^o(1),
H=B^o(1),
C/J=B^o(1).
```

Here

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)),
H=H_S*H_T.
```

The endpoint-linear forms are

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1,
```

and the full column split is

```text
J_L-*J_L+=J,
gcd(J_L-,J_L+)=1,
J_L- | L_-,
J_L+ | L_+,

L_-=J_L-*h_-,
L_+=J_L+*h_+.
```

Merged 4cy/s7-40 count

```text
# column residual <= B^(1/22+o(1)),
# row lift       <= B^(1/22+o(1)).
```

The first residual satisfies

```text
u_res<=B^(1/11+o(1)),
oddpart(a*b)=oddpart(u_res).
```

The numerical identity

```text
1/11=1/22+1/22
```

is the endpoint obstruction addressed below.

---

## 2. Same-side root-gcd cells

Define

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
K=K_x*K_y.
```

Statewise reducedness implies that the four cross-state odd gcd cells

```text
K_x,
K_y,
H_S,
H_T
```

are pairwise coprime and

```text
boxed:
oddpart(gcd(z1,z2))=K_x*K_y*H_S*H_T=K*H.          (2.1)
```

Indeed the odd part of

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},
```

is the odd part of `x_i*y_i`; because `x_i` and `y_i` are coprime within each state, any common odd prime across `z1,z2` occurs in exactly one of the four cross-state cells.

Merged 4cy/s7-40 already force

```text
H=B^o(1).
```

The only potentially fixed-power common root scale still unexamined at the unique endpoint is therefore `K`.

Write

```text
K=B^(kappa+o(1)).                                  (2.2)
```

---

## 3. Same-side primes are units on the xi residual/common core

The s7-37 primewise argument does not require proportionality for this support statement, so we record it independently at the 4cz endpoint.

Let odd `p|K_x`. Then `p|x1,x2`. Statewise reducedness makes `p` a unit on `y1,y2` and on the complementary xi cells needed in the switched host. In the xi switched host

```text
Z_S=R*x2^2*omega1+i*J0*y1^2*omega2,
```

the imaginary coordinate is a `p`-unit, and the Gaussian square descent by the switched-cell factor is also a `p`-unit operation. Hence

```text
p not| q_xi.
```

The same argument for `p|K_y` uses the real coordinate and gives the same conclusion. Therefore

```text
boxed:
gcd(K,q_xi)=1.                                    (3.1)
```

Since

```text
C|q_xi,
J|C,
C_Cayley|C,
```

we have

```text
boxed:
gcd(K,C)=gcd(K,J)=gcd(K,C_Cayley)=1.              (3.2)
```

Thus every same-side root-gcd prime is invertible on the entire fixed-power Cayley/common-core modulus at the live endpoint.

---

## 4. `K^2` divides the first residual

Merged 4ci gives exactly

```text
oddpart(gcd(z1,z2))^2 | q_k=C*u_res.
```

By (2.1), `K` divides the odd common z scale. Thus

```text
K^2|C*u_res.
```

Using (3.2),

```text
boxed:
K^2|u_res.                                         (4.1)
```

Since

```text
u_res<=B^(1/11+o(1)),
```

we obtain the endpoint range

```text
boxed:
0<=kappa<=1/22.                                    (4.2)
```

Moreover `K` is odd and merged signed-quotient reconstruction gives

```text
oddpart(a*b)=oddpart(u_res),
```

so

```text
boxed:
K^2|a*b|N,                                         (4.3)
```

where

```text
N=a*b*c*d.
```

---

## 5. `K^2` divides the Cayley numerator `M`

Put

```text
X=x1*x2,
Y=y1*y2.
```

For every prime power of `K_x`, the minimum valuation in `x1,x2` occurs twice in the product `X`, hence

```text
K_x^2|X.
```

Similarly

```text
K_y^2|Y.
```

The two same-side cells are coprime, so

```text
boxed:
K^2|X*Y.                                           (5.1)
```

The Cayley numerator is

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k.
```

Therefore, for the odd integer `K`,

```text
boxed:
K^2|M.                                             (5.2)
```

Combining (4.3) and (5.2), the same square factor occurs in both sides of the Cayley row arithmetic:

```text
boxed:
K^2|gcd(M,N).                                      (5.3)
```

---

## 6. `K^2` divides the endpoint-column cofactor product

Because `K|z1,z2`, the endpoint-linear forms satisfy

```text
K|L_-,
K|L_+.
```

The column moduli `J_L-`, `J_L+` divide `J`, and (3.2) gives

```text
gcd(K,J_L-*J_L+)=1.
```

Consequently division by the column moduli cannot remove any `K`-valuation:

```text
boxed:
K|h_-,
K|h_+.                                             (6.1)
```

Hence

```text
boxed:
K^2|h_-h_+.                                        (6.2)
```

This is the column analogue of the 4cy/s7-40 `H^2` row reduction, but for the still-live same-side root gcd.

---

## 7. Divide the Cayley row by `K^2`

The Cayley signs satisfy

```text
C_-|M-N,
C_+|M+N,
C_-*C_+=C_Cayley,
gcd(C_-,C_+)=1.
```

By (3.2), `K` is a unit modulo `C_Cayley`, while (5.3) gives `K^2|M,N`. Define

```text
M_K=M/K^2,
N_K=N/K^2.
```

Then exact cancellation gives

```text
boxed:
C_-|M_K-N_K,
C_+|M_K+N_K.                                       (7.1)
```

Equivalently, after `M` is reconstructed, the row conditions

```text
N == N0(M) (mod C_Cayley),
N == 0     (mod K^2)
```

combine by CRT because `(K,C_Cayley)=1`.

Thus the row spacing modulus is effectively

```text
C_Cayley*K^2
```

for fixed `K`; this is not a new freely summed modulus because `K` is the dyadic gcd stratum currently being counted.

At the endpoint

```text
N<=B^(1/4+o(1)),
C_Cayley=B^(9/44+o(1)),
```

so for fixed `K=B^(kappa+o(1))` the row-lift support is

```text
boxed:
E_row,K<=max(0,1/22-2kappa).                       (7.2)
```

---

## 8. Primitive column count after removing `K`

Write

```text
z1=K*z1',
z2=K*z2'.
```

By (2.1), the odd common gcd of `(z1',z2')` is exactly the cross-root part `H`, up to the harmless finite 2-primary decoration. Since merged 4cy/s7-40 force

```text
H=B^o(1),
```

the reduced pair is primitive for determinant-spacing purposes up to `B^o(1)`.

Because `(K,J)=1`, the column congruences become the same primitive root line modulo `J=C*B^o(1)` after dividing by `K`.

The original z-box has product

```text
z1*z2<=B^(1/4+o(1)),
```

so the reduced box has product

```text
z1'*z2'<=B^(1/4-2kappa+o(1)).
```

Apply the merged primitive determinant/root-line lemma modulo

```text
J=B^(9/44+o(1)).
```

For fixed `K` and fixed divisor-many column orientation,

```text
# {(z1',z2')}
 <=B^o(1)*(1+B^(1/4-2kappa)/J).
```

Therefore

```text
boxed:
E_col,K<=max(0,1/22-2kappa).                       (8.1)
```

This is a charged-once count of the actual column pair, not a second use of the common core.

---

## 9. Cost of the dyadic `K` stratum

A dyadic interval

```text
K=B^(kappa+o(1))
```

contains at most

```text
B^(kappa+o(1))
```

possible integers. Charging this choice once, and then using (7.2) and (8.1), gives the fixed-power short-coordinate cost

```text
boxed:
F(kappa)
 = kappa
   +2*max(0,1/22-2kappa).                          (9.1)
```

The common-core plus first primitive-pair cost at the endpoint is

```text
2phi=19/44.                                        (9.2)
```

Hence

```text
boxed:
E_4cz(kappa)
 <=19/44
   +kappa
   +2*max(0,1/22-2kappa).                          (9.3)
```

This count reconstructs the same physical packet as the merged row/column count: after the column fixes `(z1,z2)` and `M`, the strengthened row fixes `N` up to the stated lift, and fixed `N` has only divisor-many signed quotient factorizations before the merged reciprocal reconstruction.

---

## 10. Exact `kappa` stratification

Let

```text
a0=1/22.
```

For

```text
0<=kappa<=a0/2=1/44,
```

(9.1) is

```text
F(kappa)
 =kappa+2*(a0-2kappa)
 =1/11-3kappa.                                     (10.1)
```

For

```text
1/44<=kappa<=1/22,
```

both positive parts vanish and

```text
F(kappa)=kappa.                                    (10.2)
```

Thus

```text
boxed:
max_{0<=kappa<=1/22} F(kappa)=1/11,                (10.3)
```

and equality in (10.3) occurs only at

```text
boxed:
kappa=0.                                           (10.4)
```

Substituting into (9.3),

```text
boxed:
E_4cz(kappa)<=23/44,
```

with equality possible only for

```text
K=B^o(1).                                          (10.5)
```

Therefore every fixed-power same-side root-gcd stratum is strictly below the current mainline barrier.

---

## 11. Square-root threshold inside the same-side strata

In the first regime,

```text
E_4cz(kappa)
 <=23/44-3kappa.
```

The current gap to square root is

```text
23/44-1/2=1/44.
```

Hence

```text
23/44-3kappa<=1/2
```

as soon as

```text
boxed:
kappa>=1/132.                                      (11.1)
```

For the second regime `kappa>=1/44`,

```text
E_4cz(kappa)
 <=19/44+kappa
 <=21/44
 <1/2.                                             (11.2)
```

Consequently

```text
boxed:
K>=B^(1/132+o(1))
=> E<=1/2+o(1).                                    (11.3)
```

This is a local square-root closure of all sufficiently large same-side gcd strata. It does not yet promote a whole-family square-root theorem because the primitive stratum `K=B^o(1)` remains.

---

## 12. Saturation requires global odd primitivity of the four roots

Merged 4cy/s7-40 already force

```text
H_S=H_T=B^o(1).
```

Section 10 now forces

```text
K_x=K_y=B^o(1)
```

on every possible `23/44` saturation sequence.

Together with the exact statewise primitive conditions

```text
gcd(x1,y1)=gcd(x2,y2)=1,
```

we obtain the full cross-state pairwise statement

```text
boxed:
oddpart(gcd(x1,x2))=B^o(1),
oddpart(gcd(y1,y2))=B^o(1),
oddpart(gcd(x1,y2))=B^o(1),
oddpart(gcd(x2,y1))=B^o(1).                        (12.1)
```

Thus the four-root tuple

```text
(x1,y1,x2,y2)
```

is globally odd-primitive up to subpolynomial pairwise gcds.

Equivalently,

```text
boxed:
oddpart(gcd(z1,z2))=B^o(1).                        (12.2)
```

This is a strict receiver contraction not present in 4cy/s7-40.

---

## 13. Whole-family theorem and new receiver

The primitive `kappa=0` stratum still attains the current charged-once ledger, so Stage14-4cz does **not** claim a new global exponent below `23/44`.

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

The old receiver

```text
TwentyThreeFortyFourthsCrossRootFreeEqualCoreTwinOneTwentySecondLiftIncidence
```

and the s7-40 receiver

```text
TwentyThreeFortyFourthsZeroCrossRootFullCayleyCoreTwinShortFirstResidualQuotientIncidence
```

are both superseded by the narrower object

```text
boxed:
TwentyThreeFortyFourthsGloballyOddPrimitiveFourRootFullCayleyTwinShortFirstResidualIncidence.
```

Any saturation packet for this receiver must satisfy simultaneously

```text
theta=23/88,
phi=19/88,
chi=j=9/44,
C=J=C_Cayley*B^o(1),
H=B^o(1),
K=B^o(1),
oddpart(gcd(z1,z2))=B^o(1),
column residual<=B^(1/22+o(1)),
row lift<=B^(1/22+o(1)),
u_res<=B^(1/11+o(1)),
oddpart(a*b)=oddpart(u_res),
```

with all four root-gcd cells subpolynomial.

The next exact task is to use this global odd primitivity in the two surviving short coordinates. In particular, once no fixed-power root gcd remains, `Stage14-4da` should test whether the column cofactor pair and the reduced Cayley row lift can still vary independently under the two reciprocal signed equations, or whether a primitive resultant/determinant forces a further `1/44` saving.

---

## 14. H / tH decision

No mainline H/tH theorem is needed at Stage14-4cz.

The live packet has become more elementary, not more analytic: all fixed-power root gcds are gone and the obstruction is a primitive exact signed-reciprocal reconstruction with two short coordinates.

The merged fixed-U `t78/t79` and parallel `tH22` projective ray-character work are a different coefficient space and are not cross-promoted.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
T78_CROSS_PROMOTED_TO_MAINLINE=false
T79_CROSS_PROMOTED_TO_MAINLINE=false.
```

If `Stage14-4da` leaves a genuine averaged incidence after the primitive resultant structure is exhausted, formulate H specifically for that final primitive twin-short receiver; do not reopen the generic genus-one audit.

---

## Stage boundary

```text
STAGE14_4CZ=COMPLETE_SAMESIDE_ROOT_GCD_SQUARE_ROW_COLUMN_TRANSFER_AND_GLOBALLY_ODD_PRIMITIVE_23_44_RECEIVER
MERGED_4CY_IMPORTED=true
MERGED_S7_40_IMPORTED=true
MERGED_S7_37_SAMESIDE_SUPPORT_REPROVED_ON_ENDPOINT=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44
CURRENT_GAP_TO_SQRT=1/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
TWENTYTHREE_44_SATURATION_THETA=23/88
TWENTYTHREE_44_SATURATION_PHI=19/88
TWENTYTHREE_44_COMMON_CORE_EXPONENT=9/44
TWENTYTHREE_44_JOINT_CORE_EXPONENT=9/44
TWENTYTHREE_44_CROSS_ROOT_EXPONENT=0
SAMESIDE_ROOT_GCD_CELLS_PAIRWISE_WITH_CROSS_CELLS=true
SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true
SAMESIDE_ROOT_GCD_COPRIME_TO_COMMON_CORE=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_CAYLEY_M=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_CAYLEY_N=true
SAMESIDE_ROOT_GCD_DIVIDES_BOTH_COLUMN_COFACTORS=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_COLUMN_COFACTOR_PRODUCT=true
CAYLEY_ROW_DIVIDABLE_BY_SAMESIDE_ROOT_GCD_SQUARE=true
KAPPA_RANGE=[0,1/22]
KAPPA_STRATIFIED_SHORT_COST=kappa+2*max(0,1/22-2kappa)
KAPPA_STRATIFIED_BLOCK_EXPONENT=19/44+kappa+2*max(0,1/22-2kappa)
FIXED_POWER_SAMESIDE_ROOT_GCD_STRICTLY_SUBCRITICAL=true
SAMESIDE_ROOT_GCD_SQRT_CLOSURE_THRESHOLD=1/132
SAMESIDE_ROOT_GCD_AT_23_44_SATURATION=Bo1
ALL_FOUR_CROSS_STATE_ROOT_GCD_CELLS_AT_SATURATION=Bo1
ODD_COMMON_Z_GCD_AT_SATURATION=Bo1
GLOBAL_ODD_FOUR_ROOT_PRIMITIVITY_AT_SATURATION=true
TWENTYTHREE_44_COLUMN_SHORT_EXPONENT=1/22
TWENTYTHREE_44_ROW_SHORT_EXPONENT=1/22
TWENTYTHREE_44_U_RESIDUAL_CAP_EXPONENT=1/11
REMAINING_RECEIVER=TwentyThreeFortyFourthsGloballyOddPrimitiveFourRootFullCayleyTwinShortFirstResidualIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH22_CROSS_PROMOTED_TO_MAINLINE=false
T78_CROSS_PROMOTED_TO_MAINLINE=false
T79_CROSS_PROMOTED_TO_MAINLINE=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4da
```
