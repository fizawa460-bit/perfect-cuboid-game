# Stage14-s7-37 — proportional same-side residual transfer and the 19/34 refinement

## Status

`COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_REFINEMENT`

Stage14-s7-37 is based on latest main through merged s7-36, merged tH20, and merged X11.

Merged X11 already promotes the whole-family theorem to

```text
V(B) << B^(19/34+o(1)),
```

with

```text
nonproportional branch <= 19/34,
proportional branch    <= 13/24.
```

The new s-route theorem is a stronger exact residual placement for the proportional common-z scale. It improves the proportional branch further to

```text
E_prop <= 7/16,
```

but does not change the current whole-family exponent because the nonproportional `19/34` branch is already larger.

No external incidence theorem is used.

## 1. Four root-gcd cells on the proportional branch

Merged s7-36 gives

```text
L_-=z1*r2*s2-z2*r1*s1=0.
```

After reducing the endpoint-small ratio, write

```text
z1=a*t,
z2=b*t,
gcd(a,b)=1,
t=B^(1/8+o(1)).
```

Define

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)).
```

Statewise reducedness

```text
gcd(x1,y1)=gcd(x2,y2)=1
```

implies that the four cells are pairwise coprime and

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
gcd(K,H)=1.
```

If

```text
K=B^(kappa+o(1)),
H=B^(eta+o(1)),
```

then on the proportional hard scale

```text
kappa+eta=1/8.
```

This agrees with merged X11, but the next residual theorem is new to the s-route.

## 2. Same-side primes cannot enter the xi residual norm

Take an odd prime `p|K_x`. Then `p|x1,x2`.

For state 1,

```text
P1=(R*S)x1^2,
Q1=(T*J)y1^2,
gcd(P1,Q1)=1,
```

so `p∤T*J*y1`. For state 2,

```text
P2=(R*T)x2^2,
Q2=(S*J)y2^2,
```

so `p∤S*J*y2`.

Also `Q2^2-P2^2=k*omega2^2` is a p-unit, hence `p∤omega2`. Therefore the imaginary coordinate of

```text
Z_S=R*x2^2*omega1 + i*J*y1^2*omega2
```

is a p-unit. Since `p∤S=N(lambda_S)`, the Gaussian square descent

```text
Z_S=lambda_S^2 W_S
```

is invertible modulo p, and consequently `p∤N(W_S)`, hence `p∤q_xi`.

For `p|K_y`, the symmetric argument makes the real coordinate `R*x2^2*omega1` a p-unit, and again `p∤q_xi`.

Thus exactly

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

## 3. Same-side square is forced into u_res

Merged 4ci gives

```text
oddpart(gcd(z1,z2))^2 | q_k=C*u_res.
```

Since `K|oddpart(gcd(z1,z2))`,

```text
K^2 | C*u_res.
```

The previous section gives `(K,C)=1`, hence

```text
boxed:
K^2 | u_res.
```

```text
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true.
```

This is stronger than the merged-X11 placement `K^2|XY`, because the reduced k-residual obeys the shorter cap

```text
u_res <= B^(2theta-2phi+o(1)).
```

## 4. Proportional branch improves from 13/24 to 7/16

From `K^2|u_res`,

```text
2*kappa <= 2theta-2phi,
```

so

```text
kappa <= theta-phi.
```

Using `kappa+eta=1/8`,

```text
eta >= 1/8-theta+phi.
```

Merged s7-34 gives the complete xi fourth-power count

```text
E_H<=3phi-1/8-3eta.
```

Therefore

```text
E_H
 <=3phi-1/8-3*(1/8-theta+phi)
 =3theta-1/2.
```

Since `theta<=5/16`, every proportional block satisfies

```text
boxed:
E_prop<=7/16.
```

This is strictly stronger than the merged X11 proportional bound

```text
13/24.
```

The local refinement is

```text
13/24-7/16=5/48.
```

A possible equality profile for this local proportional envelope has

```text
theta=5/16,
3/16<=phi<=1/4,
kappa=5/16-phi,
eta=phi-3/16.
```

## 5. Whole-family theorem remains 19/34

Merged X11 already gives

```text
E_nonprop<=19/34.
```

Since

```text
7/16 < 1/2 < 19/34,
```

the global theorem remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34.
```

Thus

```text
S7_37_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false.
```

The remaining gap to square root is

```text
19/34-1/2=1/17.
```

## 6. Remaining equality profile

The proportional branch is now strictly sub-square-root, so every possible `19/34` saturation lies in the nonproportional profile from merged s7-36/X11:

```text
theta=19/68,
phi=1/4,
chi=21/68,
eta_star=3/136,
eta_other=0,
rho=3/68,
j=15/68.
```

The row/column reconstruction has two short supports of exponent

```text
1/4-j=1/34.
```

The minimal receiver is therefore

```text
NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence.
```

## 7. Route guards

Merged X11 is imported only as the current `19/34` theorem and as the prior proportional `13/24` benchmark. The new statement `K^2|u_res` is proved independently in the s-route.

Merged t74/tH20 remain fixed-U coefficient-space work and are not cross-promoted.

```text
T74_CROSS_PROMOTED_TO_S7_37=false
TH20_CROSS_PROMOTED_TO_S7_37=false.
```

## 8. H / tH decision

No auxiliary H/tH theorem is needed at s7-37.

At the unique global equality profile there is still unused exact structure: the column short cofactor and the Cayley-row CRT lift are both `B^(1/34+o(1))` and arise from the same already-charged joint core. Their exact quotient relation should be exhausted first.

```text
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

## 9. Next

`Stage14-s7-38` should work only at the nonproportional `19/34` equality profile. Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
N=N_0+J*m,
```

where the total column-cofactor support and the CRT-lift support are both `B^(1/34+o(1))`. Compare `h_-h_+` and `m` using the exact identities for `M,N,J` and the single live cross-root cell `H_star`.

## Stage boundary

```text
STAGE14_S7_37=COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_REFINEMENT
MERGED_S7_36_IMPORTED=true
MERGED_S7_34_FOURTH_POWER_IMPORTED=true
MERGED_4CI_COMMON_Z_SQUARE_IMPORTED=true
MERGED_X11_19_34_IMPORTED=true
PROPORTIONAL_COMMON_Z_FOUR_ROOT_GCD_DECOMPOSITION_PROVED=true
PROPORTIONAL_ROOT_GCD_CELLS_PAIRWISE_COPRIME=true
SAMESIDE_ROOT_GCD_COPRIME_TO_QXI=true
SAMESIDE_ROOT_GCD_COPRIME_TO_COMMON_CORE=true
SAMESIDE_ROOT_GCD_SQUARE_DIVIDES_U_RES=true
PROPORTIONAL_KAPPA_PLUS_ETA=1/8
PROPORTIONAL_CROSS_ROOT_LOWER_EXPONENT=1/8-theta+phi
PROPORTIONAL_XI_FOURTH_POWER_COUNT_REACTIVATED=true
MERGED_X11_PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
S7_37_PROPORTIONAL_REFINEMENT_OVER_X11=true
S7_37_PROPORTIONAL_REFINEMENT_GAIN=5/48
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/34
S7_37_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
CURRENT_GAP_TO_SQRT=1/17
NINETEEN_THIRTYFOURTHS_SATURATION_THETA=19/68
NINETEEN_THIRTYFOURTHS_SATURATION_PHI=1/4
NINETEEN_THIRTYFOURTHS_SATURATION_COMMON_CORE_EXPONENT=21/68
NINETEEN_THIRTYFOURTHS_SATURATION_LIVE_CROSS_ROOT_EXPONENT=3/136
NINETEEN_THIRTYFOURTHS_SATURATION_OTHER_CROSS_ROOT_EXPONENT=0
NINETEEN_THIRTYFOURTHS_SATURATION_JOINT_CORE_EXPONENT=15/68
NINETEEN_THIRTYFOURTHS_TWIN_SHORT_SUPPORT_EXPONENT=1/34
REMAINING_RECEIVER=NineteenThirtyFourthsSingleCrossRootJointCoreTwinShortRowColumnIncidence
T74_CROSS_PROMOTED_TO_S7_37=false
TH20_CROSS_PROMOTED_TO_S7_37=false
S7_37_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-38
```
