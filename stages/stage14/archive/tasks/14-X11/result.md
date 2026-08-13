# Stage14-X11 — proportional common-z root-gcd decomposition and 19/34 promotion

## Status

`COMPLETE_PROPORTIONAL_FOUR_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION`

Stage14-X11 is based on merged main

```text
6f8f6f64d29fb195f97e4b7a3e1bf9352b8c466d
```

and consumes merged `s7-36`, together with the `s7-34/s7-35`, `4cq`, and `4cu/4cv` arithmetic it already imports.

The entering whole-family theorem is

```text
V(B) << B^(9/16+o(1)).
```

Merged `s7-36` has already reduced the nonproportional branch to

```text
E_nonprop <= 19/34,
```

while the proportional branch

```text
L_-=0
```

remains at `9/16` because the common `z` scale `t=B^(1/8+o(1))` survives in the k-side residual Gaussian hosts.

X11 decomposes that common scale primewise into four root-gcd cells.  The cross cells are controlled by the merged fourth-power theorem `H^4|q_xi`; the same-side cells form a square divisor of the physical root product `XY` and therefore sharpen the merged dual-Cayley complete count.  Combining these two alternative counts lowers the proportional branch to

```text
E_prop <= 13/24.
```

Since

```text
13/24 < 19/34 < 9/16,
```

the whole-family exponent improves to

```text
boxed:
V(B) << B^(19/34+o(1)).
```

The gain over merged `9/16` is

```text
9/16-19/34=1/272,
```

and the remaining gap to square-root scale is

```text
19/34-1/2=1/17.
```

No external sieve, determinant theorem, genus-one theorem, or H/tH theorem is used.

---

## 1. The merged 9/16 split

Use the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Merged `s7-36` proves

```text
nonproportional: L_-L_+ != 0,  E <= 19/34,
proportional:    L_-=0,         E <= 9/16.
```

The proportional identity is

```text
z_1 r_2 s_2=z_2 r_1 s_1.
```

After reducing the endpoint-small ratio,

```text
z_1=a t,
z_2=b t,
a,b=B^o(1),
t=B^(1/8+o(1)).                                    (1.1)
```

At odd primes the finite `g_i in {1,2}` factors do not affect the gcd, so

```text
oddpart(t)=oddpart(gcd(x_1y_1,x_2y_2)).            (1.2)
```

Statewise reducedness gives

```text
gcd(x_1,y_1)=gcd(x_2,y_2)=1.                      (1.3)
```

---

## 2. Exact four-cell decomposition of the common z scale

Define

```text
K_x=oddpart(gcd(x_1,x_2)),
K_y=oddpart(gcd(y_1,y_2)),
H_T=oddpart(gcd(x_1,y_2)),
H_S=oddpart(gcd(y_1,x_2)).                         (2.1)
```

For any odd prime `p|t`, (1.3) forces `p` to occur in exactly one of the four pairings in (2.1).  The same statement holds valuation by valuation: if `p^e` is the common odd power in `x_1y_1` and `x_2y_2`, the valuation `e` is exactly the minimum valuation in that unique pairing.

Therefore

```text
boxed:
oddpart(t)=K_x K_y H_S H_T,                        (2.2)
```

and the four factors are pairwise coprime.

Put

```text
K=K_xK_y,
H=H_SH_T.                                          (2.3)
```

Dyadically write

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)).                                    (2.4)
```

Since `t=B^(1/8+o(1))`, (2.2) gives the exact exponent partition

```text
boxed:
kappa+eta=1/8.                                    (2.5)
```

This is the key proportional-branch conservation law.

---

## 3. Cross cells: fourth-power sparsity in q_xi

Merged `s7-34` proves

```text
boxed:
H^4 | q_xi.                                        (3.1)
```

The xi one-host reconstruction then gives, for `H=B^(eta+o(1))`,

```text
boxed:
E_H <= 3phi-1/8-3eta.                              (3.2)
```

Using `phi<=1/4`,

```text
boxed:
E_H <= 5/8-3eta.                                   (3.3)
```

This is a complete count of the proportional physical block; it is not multiplied by the same-side saving below.

---

## 4. Same-side cells: square divisor of the root product

Set

```text
X=x_1x_2,
Y=y_1y_2.
```

By definition of `K_x,K_y`, valuation by valuation,

```text
K_x^2 | X,
K_y^2 | Y.                                         (4.1)
```

Since `K_x,K_y` are coprime,

```text
boxed:
K^2 | X Y.                                         (4.2)
```

The balanced root product satisfies

```text
XY<=B^(1/4+o(1)).                                  (4.3)
```

For a dyadic `K=B^(kappa+o(1))`, write

```text
XY=K^2 R.
```

The pair `(K,R)` has support

```text
B^(kappa+o(1)) * B^(1/4-2kappa+o(1))
 =B^(1/4-kappa+o(1)).                              (4.4)
```

Thus the physical square-divisor condition saves exactly `kappa` from the raw `XY` support.

---

## 5. Insert the same-side saving into the merged dual-Cayley count

Merged `4cq` gives the legal alternative charged-once count

```text
E_dual <= 1/2+2phi-chi,                            (5.1)
```

where

```text
chi=2theta+2phi-3/4.
```

In (5.1), one `1/4` support is the reduced residual hyperbola and one `1/4` support is the root product `XY`.  Section 4 replaces the latter by `1/4-kappa` while leaving the rest of the reconstruction unchanged.  Therefore

```text
boxed:
E_K <= 1/2+2phi-chi-kappa
     =5/4-2theta-kappa.                            (5.2)
```

This is again a complete count of the same physical block.  No self-generated modulus is recharged: `K^2|XY` is used only to sparsify the already-charged root-product parameter.

Using the conservation law (2.5),

```text
boxed:
E_K <= 9/8-2theta+eta.                             (5.3)
```

---

## 6. Proportional minimax: 13/24

For the same proportional block, (3.3) and (5.3) are alternative complete bounds:

```text
E_H <= 5/8-3eta,
E_K <= 9/8-2theta+eta.                             (6.1)
```

Hence

```text
min(E_H,E_K)
 <=(E_H+3E_K)/4
 =1-(3/2)theta.                                    (6.2)
```

The merged proportional k-host count remains

```text
E_prop,k<=3theta-3/8.                              (6.3)
```

Therefore

```text
E_prop
 <=min(3theta-3/8, 1-(3/2)theta).                 (6.4)
```

The two functions meet at

```text
3theta-3/8=1-(3/2)theta,
```

i.e.

```text
boxed:
theta=11/36,
E_prop=13/24.                                      (6.5)
```

Thus uniformly

```text
boxed:
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24.    (6.6)
```

Equality in the derived proportional envelope requires

```text
theta=11/36,
phi=1/4,
eta=1/36,
kappa=7/72.                                       (6.7)
```

The common-core exponent there is

```text
chi=13/36.                                         (6.8)
```

This branch is strictly below `19/34`:

```text
19/34-13/24=7/408.                                 (6.9)
```

---

## 7. Whole-family promotion to 19/34

Merged `s7-36` gives

```text
E_nonprop<=19/34.
```

Section 6 gives

```text
E_prop<=13/24.
```

Every physical packet is in exactly one branch, so

```text
E<=max(19/34,13/24)=19/34.                        (7.1)
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34,
IMPROVEMENT_OVER_MERGED_9_16=1/272,
CURRENT_GAP_TO_SQRT=1/17,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.         (7.2)
```

The global obstruction returns to the nonproportional row/column equality profile.

---

## 8. New minimal receiver

Merged `s7-36` localizes the `19/34` nonproportional envelope at

```text
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68,
```

with twin row/column short supports

```text
1/4-j=1/34.                                        (8.1)
```

The new X receiver is

```text
NineteenThirtyFourthsFourthPowerJointCoreTwinShortRowColumnIncidence.
```

It retains simultaneously

```text
J=J_{--}J_{-+}J_{+-}J_{++},
|h_-h_+|<=B^(1/34+o(1)),
# row CRT lifts <=B^(1/34+o(1)),
H^4|q_xi,
rho=2eta_star,
all primitive/reduced/canonical physical masks.
```

The proportional common-z receiver is now strict subcritical and is no longer minimal.

The next X step should compare the two `1/34` short quantities as exact integer quotients of the same four-cell allocation before invoking any external theorem.

---

## 9. H / tH decision

The X11 saving is elementary: primewise gcd decomposition, square divisibility, merged one-host counts, and an existing dual-Cayley quantifier order.

Therefore

```text
X11_AUXILIARY_H_NEEDED=false,
X_ROUTE_BLOCKED_BY_H=false,
GENERIC_GENUS_ONE_H_REOPENED=false,
TH20_CROSS_PROMOTED_TO_X11=false.
```

The fixed-U tH20 norm-value problem remains a distinct coefficient space.

---

## Stage boundary

```text
STAGE14_X11=COMPLETE_PROPORTIONAL_FOUR_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION
MERGED_S7_36_IMPORTED=true
PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true
PROPORTIONAL_COMMON_Z_GCD_CELL_COUNT=4
PROPORTIONAL_COMMON_Z_ODDPART_PRODUCT=K_x*K_y*H_S*H_T
PROPORTIONAL_SAME_SIDE_PRODUCT=K_x*K_y
PROPORTIONAL_CROSS_PRODUCT=H_S*H_T
PROPORTIONAL_SAME_SIDE_SQUARE_DIVIDES_XY=true
PROPORTIONAL_CROSS_FOURTH_POWER_DIVIDES_QXI=true
PROPORTIONAL_KAPPA_PLUS_ETA=1/8
SAME_SIDE_SQUARE_DIVISOR_ROOT_PRODUCT_SAVING=kappa
PROPORTIONAL_DUAL_CAYLEY_BLOCK_EXPONENT=5/4-2theta-kappa
PROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=1:3
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24
PROPORTIONAL_SATURATION_THETA=11/36
PROPORTIONAL_SATURATION_PHI=1/4
PROPORTIONAL_SATURATION_CROSS_EXPONENT=1/36
PROPORTIONAL_SATURATION_SAME_SIDE_EXPONENT=7/72
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34
IMPROVEMENT_OVER_MERGED_9_16=1/272
CURRENT_GAP_TO_SQRT=1/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_RECEIVER=NineteenThirtyFourthsFourthPowerJointCoreTwinShortRowColumnIncidence
X11_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT_RECOMMENDED=Stage14-X12
```