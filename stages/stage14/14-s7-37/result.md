# Stage14-s7-37 — proportional same-side residual transfer and the 19/34 bound

## Status

`COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_PROMOTION`

Stage14-s7-37 consumes merged `s7-36` on current main.  The entering theorem is

```text
V(B) << B^(9/16+o(1)),
```

with the nonproportional branch already bounded by

```text
E_nonprop<=19/34
```

and the remaining global barrier equal to the proportional branch

```text
L_-=0,
z1*r2*s2=z2*r1*s1.
```

The new exact theorem is that the same-side part of the proportional common `z` scale cannot enter the xi residual norm at all.  It is forced into the reduced k-residual `u_res`.

This closes the proportional branch below the square-root scale:

```text
E_prop<=7/16.
```

Therefore the whole family is now controlled by the already-localized nonproportional branch:

```text
boxed:
V(B) << B^(19/34+o(1)).
```

No external incidence theorem is used.

---

## 1. Imported proportional structure

Merged s7-36 gives

```text
L_-=z1*r2*s2-z2*r1*s1=0.
```

Since `r_i,s_i=B^o(1)`, write the reduced endpoint ratio as

```text
r1*s1=d*a,
r2*s2=d*b,
gcd(a,b)=1.
```

Then

```text
z1*b=z2*a,
```

so exactly

```text
z1=a*t,
z2=b*t
```

for an integer common scale `t`.  In the balanced physical root box

```text
z1,z2=B^(1/8+o(1)),
```

hence

```text
t=B^(1/8+o(1)).                                    (1.1)
```

Merged 4ci gives for every physical packet, not only the proportional branch,

```text
oddpart(gcd(z1,z2))^2 | q_k=C*u_res.                (1.2)
```

Merged s7-34 gives the cross-root fourth-power theorem

```text
H^4 | q_xi=C*v_res.                                 (1.3)
```

The purpose of s7-37 is to distinguish the same-side and cross-side portions of the common `z` scale before using (1.2).

---

## 2. Exact four root-gcd cells

Statewise reducedness is

```text
gcd(x1,y1)=gcd(x2,y2)=1.
```

Define

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)).                            (2.1)
```

Every odd prime dividing

```text
gcd(x1*y1,x2*y2)
```

must occur in exactly one of these four cells.  Statewise reducedness also makes the four cells pairwise coprime.  Since

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},
```

the finite two-primary convention disappears after odd-part projection and we get exactly

```text
boxed:
oddpart(gcd(z1,z2))=K_x*K_y*H_S*H_T.                (2.2)
```

Put

```text
K=K_x*K_y,
H=H_S*H_T.
```

Then

```text
gcd(K,H)=1,
oddpart(gcd(z1,z2))=K*H.                            (2.3)
```

Thus on the proportional branch, if

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)),
```

then by (1.1)

```text
boxed:
kappa+eta=1/8.                                     (2.4)
```

```text
PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true.
```

---

## 3. Same-side primes are excluded from the xi residual norm

The key new point is stronger than the generic square divisibility `K^2|XY`.

### 3.1 A prime in `K_x`

Let odd `p|K_x`.  Then

```text
p|x1,
p|x2.
```

For state 1,

```text
P1=(R*S)*x1^2,
Q1=(T*J)*y1^2,
gcd(P1,Q1)=1,
```

so `p|P1` forces

```text
p∤T*J*y1.
```

For state 2,

```text
P2=(R*T)*x2^2,
Q2=(S*J)*y2^2,
```

and `p|P2` forces

```text
p∤S*J*y2.
```

In particular

```text
p∤S,
p∤J,
p∤y1.
```

Moreover

```text
Q2^2-P2^2=k*omega2^2
```

is a p-unit because `p|P2` and `p∤Q2`; hence

```text
p∤omega2.
```

The raw switched S-host is

```text
Z_S=R*x2^2*omega1 + i*J*y1^2*omega2.
```

Its imaginary coordinate is therefore a p-unit.  Also `p∤S=N(lambda_S)`, so the Gaussian square descent

```text
Z_S=lambda_S^2 W_S
```

is invertible modulo p.  Hence

```text
p∤N(W_S)=q_xi*O_2(1).
```

Thus odd `p∤q_xi`.

### 3.2 A prime in `K_y`

The argument is symmetric.  If `p|y1,y2`, reducedness gives

```text
p∤R,
p∤S,
p∤x2,
p∤omega1.
```

The real coordinate

```text
R*x2^2*omega1
```

of `Z_S` is a p-unit and `p∤S`, so again

```text
p∤q_xi.
```

Combining both same-side cells gives the exact theorem

```text
boxed:
gcd(K,q_xi)=1.                                     (3.1)
```

Therefore, since

```text
C|q_xi,
```

we also have

```text
boxed:
gcd(K,C)=1.                                        (3.2)
```

```text
SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true.
```

This statement is specific to the same-side cells.  The cross cells behave oppositely: merged s7-34 gives `H^4|q_xi`.

---

## 4. The same-side square lies entirely in `u_res`

From merged 4ci,

```text
(KH)^2 | q_k=C*u_res.
```

In particular

```text
K^2 | C*u_res.
```

By (3.2), `(K,C)=1`, so Euclid gives

```text
boxed:
K^2 | u_res.                                       (4.1)
```

This is the new residual-transfer theorem of s7-37:

```text
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true.
```

It is strictly sharper for the present proportional receiver than only using

```text
K^2|XY,
```

because `u_res` has the much shorter dyadic cap

```text
u_res <= B^(2theta-2phi+o(1)).                     (4.2)
```

No X-route result is required for (4.1).

---

## 5. Forced cross-root size on the proportional branch

Write

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)).
```

By (2.4),

```text
kappa+eta=1/8.                                     (5.1)
```

From (4.1) and (4.2),

```text
2*kappa <= 2theta-2phi+o(1),
```

hence

```text
kappa <= theta-phi+o(1).                           (5.2)
```

Subtracting from (5.1),

```text
boxed:
eta >= 1/8-theta+phi-o(1).                         (5.3)
```

Thus

```text
PROPORTIONAL_CROSS_ROOT_LOWER_EXPONENT=1/8-theta+phi.
```

This shows why the old `9/16` profile cannot be carried purely by same-side roots: `u_res` is too short to absorb the required full common-z square.

---

## 6. Reactivate the xi fourth-power complete count

Merged s7-34 gives the complete xi count

```text
E_H<=3phi-1/8-3eta.                                (6.1)
```

Insert (5.3):

```text
E_H
 <=3phi-1/8-3*(1/8-theta+phi)
 =3theta-1/2.                                      (6.2)
```

Therefore every proportional block satisfies

```text
boxed:
E_prop<=3theta-1/2.                                (6.3)
```

Since

```text
theta<=5/16,
```

we obtain

```text
boxed:
E_prop<=7/16.                                      (6.4)
```

This is already strictly below the square-root scale.

The old proportional k-host count

```text
E_k,prop<=3theta-3/8
```

remains valid but is no longer active.

Exact equality bookkeeping for the proved proportional envelope is

```text
theta=5/16,
3/16<=phi<=1/4,
kappa=theta-phi=5/16-phi,
eta=phi-3/16,
2*kappa=2theta-2phi.
```

At every such point

```text
E_H=7/16.
```

Hence

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16.
```

---

## 7. Whole-family promotion

Merged s7-36 already proves on the nonproportional branch

```text
E_nonprop<=19/34.                                  (7.1)
```

Section 6 gives

```text
E_prop<=7/16.                                      (7.2)
```

Since

```text
7/16 < 1/2 < 19/34,
```

the global maximum is now the nonproportional branch:

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34.       (7.3)
```

The improvement over merged s7-36 is

```text
9/16-19/34=1/272.                                  (7.4)
```

The remaining gap to square root is

```text
19/34-1/2=1/17.                                    (7.5)
```

Therefore

```text
IMPROVEMENT_OVER_PREVIOUS_9_16=1/272
CURRENT_GAP_TO_SQRT=1/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

---

## 8. New global equality profile

Because the proportional branch is now strictly sub-square-root, any possible `19/34` saturation must lie in the nonproportional equality profile already isolated in s7-36:

```text
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68.                                           (8.1)
```

The two residual row/column short supports both have exponent

```text
1/4-j=1/34.                                        (8.2)
```

Thus the new minimal receiver is

```text
NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence.
```

The word `SingleCrossRoot` records the equality requirement `eta_other=0`: only one cross-root cell carries fixed-power mass.

---

## 9. Relation to parallel X11 / t74

During s7-37, parallel X11 Draft work also decomposed the proportional common-z scale into the same four root-gcd cells and obtained a `19/34` whole-family theorem through a different same-side count based on `K^2|XY` and the dual-Cayley quantifier order.

s7-37 does **not** use that open Draft as theorem input.  The stronger s-route statement proved here is

```text
K^2|u_res,
```

which follows directly from

```text
gcd(K,q_xi)=1,
C|q_xi,
(KH)^2|q_k=C*u_res.
```

Consequently the s-route proportional branch reaches `7/16`, while the global theorem is still `19/34` because the nonproportional branch dominates.

Merged t74 is fixed-U coefficient-space work and is not cross-promoted.

```text
X11_OPEN_DRAFT_USED_AS_THEOREM_INPUT=false
T74_CROSS_PROMOTED_TO_S7_37=false.
```

---

## 10. H / tH decision

No auxiliary H/tH theorem is needed at s7-37.

The proportional obstruction has been eliminated by exact gcd/residual arithmetic.  At the new global equality profile there remains unused exact structure: the two short `B^(1/34)` quantities from the same row/column reconstruction are not yet compared directly.

Before introducing an averaged incidence theorem, the next stage should identify their exact quotient relation through the common values `M,N,J` and the single live cross-root cell.

Therefore

```text
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

---

## 11. Next stage

`Stage14-s7-38` should work only at the nonproportional equality profile (8.1).

Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
N=N_0+J*m,
```

where the total column-cofactor support and CRT-lift support both have exponent `1/34`.

The target is to compare

```text
h_-*h_+
and
m
```

through the exact identities defining `M`, `N`, the four row/column cells of `J`, and the single fixed-power cross-root cell `H_star`.  Determine whether one short quantity reconstructs the other divisor-many, or whether a genuinely averaged short-short incidence remains.

---

## Stage boundary

```text
STAGE14_S7_37=COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_PROMOTION
MERGED_S7_36_IMPORTED=true
MERGED_S7_34_FOURTH_POWER_IMPORTED=true
MERGED_4CI_COMMON_Z_SQUARE_IMPORTED=true
PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true
PROPORTIONAL_COMMON_Z_ODDPART_PRODUCT=K_x*K_y*H_S*H_T
PROPORTIONAL_ROOT_GCD_CELLS_PAIRWISE_COPRIME=true
SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true
SAMESIDE_ROOT_GCD_COPRIME_TO_COMMON_CORE=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true
PROPORTIONAL_KAPPA_PLUS_ETA=1/8
PROPORTIONAL_CROSS_ROOT_LOWER_EXPONENT=1/8-theta+phi
PROPORTIONAL_XI_FOURTH_POWER_COUNT_REACTIVATED=true
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34
IMPROVEMENT_OVER_PREVIOUS_9_16=1/272
CURRENT_GAP_TO_SQRT=1/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
NINETEEN_THIRTYFOURTHS_SATURATION_THETA=19/68
NINETEEN_THIRTYFOURTHS_SATURATION_PHI=1/4
NINETEEN_THIRTYFOURTHS_SATURATION_COMMON_CORE_EXPONENT=21/68
NINETEEN_THIRTYFOURTHS_SATURATION_LIVE_CROSS_ROOT_EXPONENT=3/136
NINETEEN_THIRTYFOURTHS_SATURATION_OTHER_CROSS_ROOT_EXPONENT=0
NINETEEN_THIRTYFOURTHS_SATURATION_JOINT_CORE_EXPONENT=15/68
NINETEEN_THIRTYFOURTHS_TWIN_SHORT_SUPPORT_EXPONENT=1/34
REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence
X11_OPEN_DRAFT_USED_AS_THEOREM_INPUT=false
T74_CROSS_PROMOTED_TO_S7_37=false
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-38
```
