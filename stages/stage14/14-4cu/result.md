# Stage14-4cu — residual/Cayley orientation transfer and the 19/32 bound

## Status

`COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION`

This stage consumes merged `4ct`, `s7-32`, `4cs`, `4cr`, and checks compatibility with merged `X10`.  The current mainline input is

```text
E(theta,phi)
 <= min(max(2theta,1-2theta), 3theta-1/4, 3phi-1/8)
 <= 5/8,
```

with unique 5/8 corner `(theta,phi)=(5/16,1/4)`.

The new point is that the Gaussian orientation of an xi residual host can be compared to the xi plus-host orientation on a large common-core divisor.  The relative sign is carried by the endpoint linear forms

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1,
```

whose product has exponent at most `1/4`.  This forces a positive residual coordinate gcd before the old 5/8 corner can be reached and yields

```text
boxed:
V(B) << B^(19/32+o(1)).
```

No external incidence theorem is used.

---

## 1. Imported scales

Use the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

The common core satisfies

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4.                               (1.1)
```

The physical roots satisfy

```text
P1=RS*x1^2, Q1=TJ*y1^2,
P2=RT*x2^2, Q2=SJ*y2^2,
gcd(x1,y1)=gcd(x2,y2)=1,

z_i=2*x_i*y_i/g_i=B^(1/8+o(1)),
omega_i=g_i*r_i*s_i,
r_i,s_i=B^o(1).                                    (1.2)
```

Merged `s7-32` supplies the alternative whole-packet counts

```text
E_s=max(2theta,1-2theta),
E_k=3theta-1/4,
E_xi=3phi-1/8.                                     (1.3)
```

---

## 2. Split the common root gcd into two cross cells

Merged `4cs` gives

```text
H=oddpart(gcd(x1*x2,y1*y2)),
H^2 | C*u_res,
H^2 | (x1*x2)*(y1*y2).                             (2.1)
```

Same-state reducedness forces every odd common prime to occur crosswise.  Define

```text
H_S=oddpart(gcd(x2,y1)),
H_T=oddpart(gcd(x1,y2)).                            (2.2)
```

Then exactly

```text
boxed:
H=H_S*H_T,
gcd(H_S,H_T)=1.                                   (2.3)
```

Use the xi switched hosts

```text
Z_S=R*x2^2*omega1+i*J*y1^2*omega2=lambda_S^2 W_S,
Z_T=J*y2^2*omega1+i*R*x1^2*omega2=lambda_T^2 W_T.  (2.4)
```

Let

```text
g_S=oddpart(gcd(Re(W_S),Im(W_S))),
g_T=oddpart(gcd(Re(W_T),Im(W_T))).                 (2.5)
```

A prime in `H_S` cannot divide `S` by state-2 reducedness, so division by `lambda_S^2` is a unit operation at that prime.  Since `x2^2,y1^2` occur in the two coordinates,

```text
boxed:H_S^2 | g_S.                                 (2.6)
```

Similarly

```text
boxed:H_T^2 | g_T.                                 (2.7)
```

Choose `star in {S,T}` so that the dyadic size of `H_star` is at least that of `H_other`, and write

```text
g_star=B^(rho+o(1)).                               (2.8)
```

If `H_star=B^(eta_star+o(1))`, `H_other=B^(eta_other+o(1))`, then

```text
eta_other<=eta_star,
rho>=2eta_star,
2eta_other<=rho.                                   (2.9)
```

---

## 3. Gcd-stratified xi one-host count

The norm-gcd peel of merged `4ct` is symmetric in `S,T`.  Fixing a coordinate gcd of size `B^rho` costs `B^rho`, while its square divides the residual norm and removes `B^(2rho)` from residual-norm support.  Therefore

```text
boxed:
E_xi,star <= 3phi-1/8-rho.                        (3.1)
```

This is an alternative complete count of the same physical block; it is not multiplied into (1.3).

---

## 4. Joint Cayley/residual good core

Merged `4cr/4cs` give a Cayley-good core `C_Cayley|C` with

```text
C/C_Cayley | B^o(1)*H^2.                           (4.1)
```

The selected residual host is primitive on

```text
C_res=C/gcd(C,g_star^2).                            (4.2)
```

Put

```text
J_star=gcd(C_Cayley,C_res).                         (4.3)
```

Because `H_star^2|g_star`, the lcm of the two bad supports is, up to `B^o(1)`, bounded by

```text
g_star^2*H_other^2.
```

Using (2.9),

```text
boxed:
J_star >= B^(chi-3rho-o(1)).                       (4.4)
```

This is consistent with merged `X10`: its large-`H` saving is contained in the same matched-root-gcd mechanism, while its small-`H` Cayley core remains available inside `J_star`.

---

## 5. Orientation survives the switched Gaussian square descent

Let `p^e||J_star`.  The residual host `W_star` is primitive modulo `p` and `p^e|N(W_star)`.

If `p` is not in the switched cell, `lambda_star` is a Gaussian unit and the orientation in `W_star` equals that in `Z_star`.

If `p` is also in the switched cell, merged `4cf` gives a unique orientation `pi^2|Z_star`.  If the remaining `p` in `W_star` used the conjugate orientation, then both `pi` and `bar(pi)` would divide `Z_star`, forcing `p` to divide both integer coordinates of the switched host.  The switched-cell coprimality forbids this.

Hence on all of `J_star`

```text
boxed:
orientation(W_star)=orientation(Z_star).           (5.1)
```

No switched-cell prime is discarded.

---

## 6. The relative orientation is an endpoint linear sign

Write

```text
P=R*x1*x2,
Q=J*y1*y2.                                         (6.1)
```

On `J_star`, the xi plus host is primitive and

```text
P^2+Q^2 == 0 mod J_star.                            (6.2)
```

For the `T` host, comparison of its coordinate root with `P/Q` gives

```text
w_T/(P/Q)
 = x1*y1*omega2/(x2*y2*omega1)
 = z1*r2*s2/(z2*r1*s1).                            (6.3)
```

For the `S` host the same comparison with the conjugate xi root has the same final ratio.  Both sides are square roots of `-1`, so each prime power of `J_star` chooses one of the two signs.  Equivalently, exact cross multiplication gives the two factors

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1.                           (6.4)
```

Therefore

```text
boxed:
J_star | L_-*L_+.                                  (6.5)
```

Merged `4cr` already supplies the independent relative sign between the primitive agreement/k-plus root and the xi plus root (`C_+` same orientation, `C_-` opposite orientation).  Thus the three Gaussian roots have only two relative sign bits.  On `J_star` they form four pairwise-coprime cells indexed by

```text
(y/x, w_star/y) in {+1,-1}^2.                     (6.6)
```

The second bit is exactly the `L_-/L_+` allocation.  No third orientation entropy survives.

---

## 7. Nonproportional branch

Assume

```text
L_-*L_+ != 0.                                      (7.1)
```

Since `z_i=B^(1/8+o(1))` and `r_i,s_i=B^o(1)`,

```text
|L_-*L_+| <= B^(1/4+o(1)).                         (7.2)
```

Together with (4.4) and (6.5),

```text
chi-3rho <= 1/4+o(1),
```

so

```text
boxed:
rho >= max(0,(chi-1/4)/3)-o(1).                  (7.3)
```

When `theta+phi>1/2`, this is

```text
rho >= (2theta+2phi-1)/3-o(1).                    (7.4)
```

Insert (7.4) into (3.1).  Since `theta>1/4` in this region,

```text
E <= min(
       2theta,
       3phi-1/8-(2theta+2phi-1)/3
     ).                                            (7.5)
```

Using `phi<=1/4`,

```text
E <= min(2theta, 19/24-2theta/3).                 (7.6)
```

The branches meet at

```text
theta=19/64,
E=19/32.                                           (7.7)
```

If `theta+phi<=1/2`, the original `s7-32` envelope is already at most `11/20`, hence strictly below `19/32`.

Therefore

```text
boxed:
E_nonprop<=19/32.                                  (7.8)
```

Equality in the proved envelope requires

```text
boxed:
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
log_B J_star=1/4.                                  (7.9)
```

---

## 8. Proportional branch

Positivity makes `L_+>0`, so the zero-product case is only

```text
L_-=0,
```

i.e.

```text
z1*r2*s2=z2*r1*s1.                                (8.1)
```

Reduce the endpoint-small ratio `r1*s1:r2*s2=a:b` with `a,b=B^o(1)` and `gcd(a,b)=1`.  Then

```text
z1=a*t,
z2=b*t,
t=B^(1/8+o(1)).                                   (8.2)
```

For the k switched host

```text
Z_beta=alpha*r2^2*z1+i*delta*s1^2*z2
      =lambda_beta^2 W_beta,                       (8.3)
```

the full integer `t` divides both coordinates.  Since `beta|k` and merged coprimality gives `gcd(k,xi*z1*z2)=1`, the Gaussian divisor `lambda_beta` has norm coprime to `t`; the common coordinate divisor survives in `W_beta`.

Thus the gcd-stratified k one-host count saves `1/8` from `E_k`:

```text
E_prop <= 3theta-3/8 <= 9/16.                     (8.4)
```

Hence

```text
boxed:E_prop<=9/16<19/32.                          (8.5)
```

---

## 9. Whole-family theorem

Every packet is nonproportional or proportional, so

```text
E <= max(19/32,9/16)=19/32.
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32
IMPROVEMENT_OVER_PREVIOUS_5_8=1/32
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.         (9.1)
```

There is no double charge: the common core is used only to force the residual gcd lower bound, and the `C_+/C_-` plus `L_-/L_+` factors partition the same core instead of being multiplied back as new spacing moduli.

The new minimal receiver is

```text
NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence
```

at

```text
theta=19/64,
phi=1/4,
C~B^(11/32),
g_star~B^(1/32),
J_star~B^(1/4),
J_star|L_-L_+,
|L_-L_+|~B^(1/4).
```

---

## 10. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T72_CROSS_PROMOTED_TO_MAINLINE=false
```

The proof is internal arithmetic plus minimax.  `t72` remains a fixed-U coefficient-space theorem and is not cross-promoted.  A new H should be considered only if the exact `19/32` divisor-allocation receiver survives `4cv` and leaves a genuinely averaged incidence problem.

---

## Stage boundary

```text
STAGE14_4CU=COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION
MERGED_4CT_IMPORTED=true
MERGED_S7_32_IMPORTED=true
MERGED_4CS_IMPORTED=true
MERGED_4CR_IMPORTED=true
MERGED_X10_COMPATIBILITY_CHECKED=true
CROSS_ROOT_GCD_TWO_CELL_DECOMPOSITION_PROVED=true
CROSS_ROOT_CELL_SQUARES_DIVIDE_MATCHED_XI_RESIDUAL_COORDINATE_GCD=true
SELECTED_XI_RESIDUAL_GCD_STRATIFIED_BLOCK_EXPONENT=3phi-1/8-rho
JOINT_CAYLEY_RESIDUAL_CORE_LOWER_EXPONENT=chi-3rho
RESIDUAL_GAUSSIAN_ORIENTATION_PRESERVED_THROUGH_SWITCH_SQUARE_DESCENT=true
JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true
ENDPOINT_LINEAR_PRODUCT_MAX_EXPONENT=1/4
THREE_GAUSSIAN_ROOT_ORIENTATION_ENTROPY_RANK=2
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/32
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32
IMPROVEMENT_OVER_PREVIOUS_5_8=1/32
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
NINETEEN_THIRTYSECONDS_SATURATION_THETA=19/64
NINETEEN_THIRTYSECONDS_SATURATION_PHI=1/4
NINETEEN_THIRTYSECONDS_SATURATION_COMMON_CORE_EXPONENT=11/32
NINETEEN_THIRTYSECONDS_SATURATION_SELECTED_XI_GCD_EXPONENT=1/32
NINETEEN_THIRTYSECONDS_SATURATION_JOINT_CORE_EXPONENT=1/4
REMAINING_RECEIVER=NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T72_CROSS_PROMOTED_TO_MAINLINE=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cv
```