# Stage14-s7-37 — proportional same-side residual transfer and the 19/34 bound

## Status

`COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_PROMOTION`

Stage14-s7-37 consumes merged `s7-36` on current main. The entering theorem is

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

The new exact theorem is that the same-side part of the proportional common `z` scale cannot enter the xi residual norm at all. It is forced into the reduced k-residual `u_res`.

This closes the proportional branch below the square-root scale:

```text
E_prop<=7/16.
```

Therefore the whole family is now controlled by the already-localized nonproportional branch:

```text
V(B) << B^(19/34+o(1)).
```

No external incidence theorem is used.

## 1. Imported proportional structure

Merged s7-36 gives

```text
L_-=z1*r2*s2-z2*r1*s1=0.
```

Since `r_i,s_i=B^o(1)`, reduce the ratio by writing

```text
r1*s1=d*a,
r2*s2=d*b,
gcd(a,b)=1.
```

Then `z1*b=z2*a`, so exactly

```text
z1=a*t,
z2=b*t
```

for an integer common scale `t`. In the balanced root box

```text
z1,z2=B^(1/8+o(1)),
```

hence

```text
t=B^(1/8+o(1)).
```

Merged 4ci gives

```text
oddpart(gcd(z1,z2))^2 | q_k=C*u_res.
```

Merged s7-34 gives

```text
H^4 | q_xi=C*v_res.
```

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
H_T=oddpart(gcd(x1,y2)).
```

Every odd prime dividing `gcd(x1*y1,x2*y2)` occurs in exactly one of these four cells, and the four cells are pairwise coprime. Since

```text
z_i=2*x_i*y_i/g_i,
g_i in {1,2},
```

we get exactly

```text
oddpart(gcd(z1,z2))=K_x*K_y*H_S*H_T.
```

Put

```text
K=K_x*K_y,
H=H_S*H_T.
```

Then

```text
gcd(K,H)=1,
oddpart(gcd(z1,z2))=K*H.
```

On the proportional branch, if

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)),
```

then

```text
kappa+eta=1/8.
```

```text
PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true.
```

## 3. Same-side primes are excluded from `q_xi`

Let odd `p|K_x`. Then `p|x1,x2`. For state 1,

```text
P1=(R*S)*x1^2,
Q1=(T*J)*y1^2,
gcd(P1,Q1)=1,
```

so `p∤T*J*y1`. For state 2,

```text
P2=(R*T)*x2^2,
Q2=(S*J)*y2^2,
```

so `p∤S*J*y2`.

Also

```text
Q2^2-P2^2=k*omega2^2
```

is a p-unit, because `p|P2` and `p∤Q2`. Hence `p∤omega2`.

For the raw switched S-host

```text
Z_S=R*x2^2*omega1 + i*J*y1^2*omega2,
```

the imaginary coordinate is a p-unit and `p∤S=N(lambda_S)`. Thus Gaussian descent by `lambda_S^2` is invertible modulo p, so

```text
p∤q_xi.
```

The argument for `p|K_y` is symmetric: reducedness makes `R*x2^2*omega1` a p-unit and again `p∤S`, hence `p∤q_xi`.

Therefore

```text
gcd(K,q_xi)=1.
```

Since `C|q_xi`, also

```text
gcd(K,C)=1.
```

```text
SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true.
```

The cross cells behave oppositely: merged s7-34 gives `H^4|q_xi`.

## 4. Same-side square lies entirely in `u_res`

Merged 4ci gives

```text
(KH)^2 | q_k=C*u_res.
```

Therefore `K^2|C*u_res`. Since `(K,C)=1`,

```text
K^2 | u_res.
```

```text
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true.
```

This is stronger for the current proportional receiver than only using `K^2|XY`, because

```text
u_res <= B^(2theta-2phi+o(1)).
```

No X-route theorem is required.

## 5. Forced cross-root size

From

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)),
kappa+eta=1/8,
```

and `K^2|u_res`,

```text
2*kappa <= 2theta-2phi+o(1),
```

so

```text
kappa <= theta-phi+o(1).
```

Hence

```text
eta >= 1/8-theta+phi-o(1).
```

Thus

```text
PROPORTIONAL_CROSS_ROOT_LOWER_EXPONENT=1/8-theta+phi.
```

## 6. Reactivate the xi fourth-power count

Merged s7-34 gives

```text
E_H<=3phi-1/8-3eta.
```

Using the previous lower bound,

```text
E_H
 <=3phi-1/8-3*(1/8-theta+phi)
 =3theta-1/2.
```

Therefore every proportional block satisfies

```text
E_prop<=3theta-1/2<=7/16,
```

because `theta<=5/16`.

The old proportional k-host count `E_k,prop<=3theta-3/8` remains valid but is no longer active.

The equality bookkeeping for this proved proportional envelope is

```text
theta=5/16,
3/16<=phi<=1/4,
kappa=5/16-phi,
eta=phi-3/16,
2*kappa=2theta-2phi.
```

Hence

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16.
```

## 7. Whole-family promotion

Merged s7-36 already proves

```text
E_nonprop<=19/34.
```

Together with

```text
E_prop<=7/16
```

and

```text
7/16 < 1/2 < 19/34,
```

we obtain

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34.
```

The improvement is

```text
9/16-19/34=1/272,
```

and the remaining gap to square root is

```text
19/34-1/2=1/17.
```

Thus

```text
IMPROVEMENT_OVER_PREVIOUS_9_16=1/272
CURRENT_GAP_TO_SQRT=1/17
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

## 8. New global equality profile

Any possible `19/34` saturation now lies in the nonproportional equality profile already isolated in s7-36:

```text
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68.
```

The row/column short supports both have exponent

```text
1/4-j=1/34.
```

The new minimal receiver is

```text
NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence.
```

`SingleCrossRoot` records the equality requirement `eta_other=0`.

## 9. Parallel X11 and tH20/t74 guard

Parallel X11 Draft #550 independently decomposes the same proportional common-z scale and reaches the same global `19/34` using `K^2|XY` plus the dual-Cayley quantifier order. It is not used as theorem input here.

The s-route proves the stronger local statement

```text
K^2|u_res,
```

which closes the proportional branch at `7/16`.

Merged t74/tH20 are fixed-U coefficient-space work and are not cross-promoted.

```text
X11_OPEN_DRAFT_USED_AS_THEOREM_INPUT=false
T74_CROSS_PROMOTED_TO_S7_37=false
TH20_CROSS_PROMOTED_TO_S7_37=false.
```

## 10. H / tH decision

No auxiliary H/tH theorem is needed at s7-37.

The proportional obstruction is eliminated by exact gcd/residual arithmetic. At the new global equality profile, the two `B^(1/34)` short quantities from the same row/column reconstruction have not yet been compared directly. That exact quotient structure should be exhausted before introducing an averaged incidence theorem.

```text
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

## 11. Next stage

`Stage14-s7-38` should work only at the nonproportional equality profile. Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
N=N_0+J*m,
```

where the total column-cofactor support and CRT-lift support both have exponent `1/34`.

Compare `h_-*h_+` and `m` through the exact identities defining `M`, `N`, the four row/column cells of `J`, and the single live cross-root cell `H_star`. Determine whether one short quantity reconstructs the other divisor-many, or whether a genuinely averaged short-short incidence remains.

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
TH20_CROSS_PROMOTED_TO_S7_37=false
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-38
```
