# Stage14-4cw — proportional common-z root-gcd decomposition and the 19/34 bound

## Status

`COMPLETE_PROPORTIONAL_COMMON_Z_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION`

Stage14-4cw consumes merged `s7-36`, merged `s7-34`, merged `4ci`, and the physical root/cell parametrization retained by `4cu`.

The current mainline theorem entering this stage is

```text
V(B) << B^(9/16+o(1)),
```

and merged `s7-36` proves that the nonproportional branch is already bounded by

```text
E_nonprop <= 19/34.
```

Thus only the proportional branch

```text
L_-=0,
z1*r2*s2=z2*r1*s1,
z1=a*t,
z2=b*t,
t=B^(1/8+o(1))
```

can still attain `9/16`.

The new exact point is that the common z-scale `t` cannot hide entirely inside the k residual norm.  Its odd part splits into four pairwise-coprime cross-state root-gcd cells.  The two same-side cells, together with the entire 2-primary part of `t`, have square forced into `u_res`; the two cross cells are the already-known `H_S,H_T`, whose fourth power divides `q_xi`.

The `u_res` size cap therefore forces a positive cross-root mass, and the merged fourth-power-root complete count collapses the proportional branch to

```text
E_prop <= 7/16.
```

Since `7/16<1/2<19/34`, the whole family is now controlled by the nonproportional row/column branch:

```text
boxed:
V(B) << B^(19/34+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported physical root parametrization

For the two reduced physical states write

```text
P_1=R*S*x_1^2,
Q_1=T*J*y_1^2,
P_2=R*T*x_2^2,
Q_2=S*J*y_2^2,
```

with

```text
gcd(x_1,y_1)=gcd(x_2,y_2)=1.
```

The squarefree xi cells `R,S,T,J` are pairwise coprime.

From merged `s7-21`,

```text
z_i = 2*x_i*y_i/g_i,
g_i=gcd(Q_i-P_i,Q_i+P_i) in {1,2}.                 (1.1)
```

Hence `g_i` has no odd prime support and

```text
oddpart(z_i)=oddpart(x_i*y_i).                      (1.2)
```

Merged `s7-36` proves on the only potentially maximal branch

```text
L_-=0,
z_1*r_2*s_2=z_2*r_1*s_1.
```

After reducing the endpoint-small ratio,

```text
z_1=a*t,
z_2=b*t,
gcd(a,b)=1,
a,b=B^o(1),
t=B^(1/8+o(1)).                                    (1.3)
```

The common scale is exactly

```text
t=gcd(z_1,z_2)
```

up to the already-fixed endpoint-small unit normalization.

---

## 2. Exact odd root-gcd four-cell decomposition of `t`

Define

```text
K_x := oddpart(gcd(x_1,x_2)),
K_y := oddpart(gcd(y_1,y_2)),
H_T := oddpart(gcd(x_1,y_2)),
H_S := oddpart(gcd(y_1,x_2)).                       (2.1)
```

Because each state is reduced, no odd prime can occur in two of these four cells.  For example, a prime in both `K_x` and `H_T` would divide both `x_2` and `y_2`; all other pairs are identical by symmetry.  Therefore the four cells are pairwise coprime.

Prime by prime, a common odd divisor of `x_1*y_1` and `x_2*y_2` must choose exactly one coordinate from state 1 and exactly one coordinate from state 2.  Hence

```text
boxed:
oddpart(gcd(x_1*y_1,x_2*y_2))
 =K_x*K_y*H_S*H_T.                                  (2.2)
```

Using (1.2),

```text
boxed:
oddpart(t)=K_x*K_y*H_S*H_T.                         (2.3)
```

This is an exact prime-power identity, not merely a radical decomposition.

The cross product

```text
H:=H_S*H_T
```

is precisely the cross-root gcd already used in merged `4cu/s7-34/s7-35`.

---

## 3. Put the 2-primary and same-side cells into one noncross bucket

Let

```text
t_2:=2^v2(t),
T_0:=t_2*K_x*K_y.                                   (3.1)
```

Then, at exponent scale,

```text
t=T_0*H*B^o(1).                                     (3.2)
```

In fact the odd equality is exact by (2.3), and the displayed `B^o(1)` only records the harmless endpoint normalization already present in (1.3).

Merged `4ci` proves the full integer divisibility

```text
boxed:
t^2 | q_k=C*u_res.                                  (3.3)
```

The common core `C` is odd by construction.  Therefore

```text
t_2^2 | u_res.                                      (3.4)
```

It remains to place the two odd same-side cells `K_x,K_y`.

---

## 4. Same-side odd primes do not divide `q_xi` or `C`

Consider an odd prime power `p^e|K_x`.

Then

```text
p|x_1,
p|x_2,
p∤y_1*y_2.
```

From reducedness of state 1 and state 2,

```text
p∤S*T*J,
```

although `p` may divide `R`.

Also

```text
Q_i^2-P_i^2=k*omega_i^2
```

is a p-unit in each state because `p|P_i` and `p∤Q_i`; hence

```text
p∤k*omega_1*omega_2.                                (4.1)
```

Use the xi switched S-host

```text
Z_S=R*x_2^2*omega_1+i*J*y_1^2*omega_2
    =lambda_S^2 W_S,
N(lambda_S)=oddpart(S).
```

Its imaginary coordinate is a p-unit, so

```text
p∤N(Z_S).
```

Since `p∤S`, division by `lambda_S^2` is p-adically invertible and therefore

```text
p∤q_xi=N(W_S).                                      (4.2)
```

The common core satisfies `C|q_xi`, hence

```text
p∤C.                                                (4.3)
```

Now (3.3) gives

```text
p^(2e)|u_res.
```

Thus

```text
K_x^2 | u_res
```

outside no bad odd support at all.

The `K_y` proof is symmetric: `p|Q_1,Q_2`, the real coordinate of `Z_S` is a p-unit, and again `p∤q_xi`, so

```text
K_y^2 | u_res.                                      (4.4)
```

Since `K_x,K_y,t_2` are pairwise coprime,

```text
boxed:
T_0^2 | u_res.                                      (4.5)
```

This is the crucial proportional-branch transfer.

---

## 5. The noncross bucket is too small to carry all of `t`

Dyadically write

```text
T_0=B^(sigma+o(1)),
H=B^(eta+o(1)).
```

From (1.3) and (3.2),

```text
boxed:
sigma+eta=1/8.                                     (5.1)
```

The physical residual bound retained from `s7-30/s7-31` is

```text
u_res=B^(mu+o(1)),
mu<=2theta-2phi.                                    (5.2)
```

By (4.5),

```text
2sigma<=mu,
```

so

```text
boxed:
sigma<=theta-phi.                                  (5.3)
```

Combining (5.1)-(5.3),

```text
boxed:
eta>=phi-theta+1/8.                                (5.4)
```

The balanced strip has `0<=theta-phi<=1/8`, so the right side is nonnegative.

Thus every proportional packet contains enough **odd cross-root** mass to compensate for whatever part of `t` is not already forced into `u_res`.  A large 2-primary part cannot escape this argument: it belongs to `T_0` and consumes the same `u_res` square budget.

---

## 6. Feed the forced cross mass into the fourth-power-root complete count

Merged `s7-34` proves

```text
H^4 | q_xi
```

and the corresponding complete physical-block count

```text
boxed:
E_H<=3phi-1/8-3eta.                                (6.1)
```

Apply (5.4):

```text
E_prop
 <=3phi-1/8
   -3(phi-theta+1/8)
 =3theta-1/2.                                      (6.2)
```

Hence on the full balanced strip

```text
boxed:
E_prop<=3theta-1/2<=7/16.                          (6.3)
```

The old proportional bound `9/16` is therefore superseded by a full `1/8` exponent at the top theta edge.

In particular

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
```

and the entire proportional branch is already strictly below the square-root scale.

No row/column division by `L_-` is used on this branch.

---

## 7. Nonproportional branch remains `19/34`

Merged `s7-36` has already proved, using the s7-35 gcd collapse and the 4cv row/column reconstruction on `L_-L_+!=0`, that

```text
boxed:
E_nonprop<=19/34.                                  (7.1)
```

Its unique equality profile is

```text
boxed:
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68.                                          (7.2)
```

Both surviving row/column short supports have exponent

```text
boxed:
1/4-j=1/34.                                        (7.3)
```

Stage14-4cw does not recharge any of these already-counted moduli.

---

## 8. Whole-family promotion to `19/34`

Every physical packet is proportional or nonproportional.  By (6.3) and (7.1),

```text
E
 <=max(7/16,19/34)
 =19/34.
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34
IMPROVEMENT_OVER_MERGED_S7_36_9_16=1/272
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (8.1)
```

The current gap to the square-root scale is

```text
boxed:
CURRENT_GAP_TO_SQRT=1/17.                          (8.2)
```

For reference,

```text
4/7-19/34=3/238.
```

---

## 9. New unique saturation profile and receiver

Because the proportional branch is `<1/2`, any `19/34` saturation packet must be nonproportional and therefore lies at the unique s7-36 equality profile (7.2).

At that point

```text
J=B^(15/68+o(1)),
|h_-h_+|<=B^(1/34+o(1)),
# {CRT lifts of N mod J} <= B^(1/34+o(1)).          (9.1)
```

Define the new minimal receiver

```text
NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence.
```

Its characteristic data are

```text
theta=19/68,
phi=1/4,
chi=21/68,
H_star=B^(3/136+o(1)),
H_other=B^o(1),
g_star=B^(3/68+o(1)),
J=B^(15/68+o(1)),
linear cofactor product <=B^(1/34+o(1)),
CRT N-lift support <=B^(1/34+o(1)).                 (9.2)
```

The next exact task is to compare the two surviving `1/34` quantities instead of treating them as independent short supports.  In particular, `M` is reconstructed from the linear cofactor column while `N=N_0(M)+J*h_N`; the reciprocal signed-quotient equations may force a common divisor or a direct relation between `h_-h_+` and `h_N`.

---

## 10. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T74_CROSS_PROMOTED_TO_MAINLINE=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
```

The current receiver still contains two explicit short integer cofactors attached to one exact CRT system.  Their mutual arithmetic has not been exhausted, so an external averaged theorem would be premature.

The fixed-`U` t74/tH20 receiver remains a different coefficient space and is not cross-promoted.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_PROPORTIONAL_COMMON_Z_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION
MERGED_S7_36_IMPORTED=true
MERGED_S7_34_IMPORTED=true
MERGED_4CI_IMPORTED=true
PROPORTIONAL_COMMON_Z_SCALE_EXPONENT=1/8
PROPORTIONAL_ODD_T_FOUR_ROOT_GCD_CELL_DECOMPOSITION_PROVED=true
PROPORTIONAL_ROOT_GCD_CELLS_PAIRWISE_COPRIME=true
PROPORTIONAL_ODDPART_T_EQUALS_KX_KY_HS_HT=true
PROPORTIONAL_NONCROSS_BUCKET_INCLUDES_FULL_TWO_PRIMARY_T=true
PROPORTIONAL_NONCROSS_BUCKET_SQUARE_DIVIDES_URES=true
PROPORTIONAL_SAME_SIDE_KX_SQUARE_DIVIDES_URES=true
PROPORTIONAL_SAME_SIDE_KY_SQUARE_DIVIDES_URES=true
PROPORTIONAL_FORCED_CROSS_ROOT_EXPONENT_LOWER_BOUND=phi-theta+1/8
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
MERGED_S7_36_NONPROPORTIONAL_BOUND_IMPORTED=true
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34
IMPROVEMENT_OVER_MERGED_S7_36_9_16=1/272
CURRENT_GAP_TO_SQRT=1/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
NINETEEN_THIRTYFOURTHS_SATURATION_THETA=19/68
NINETEEN_THIRTYFOURTHS_SATURATION_PHI=1/4
NINETEEN_THIRTYFOURTHS_SELECTED_CROSS_ROOT_EXPONENT=3/136
NINETEEN_THIRTYFOURTHS_OTHER_CROSS_ROOT_EXPONENT=0
NINETEEN_THIRTYFOURTHS_SELECTED_XI_GCD_EXPONENT=3/68
NINETEEN_THIRTYFOURTHS_JOINT_CORE_EXPONENT=15/68
NINETEEN_THIRTYFOURTHS_TWIN_SHORT_SUPPORT_EXPONENT=1/34
REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T74_CROSS_PROMOTED_TO_MAINLINE=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```
