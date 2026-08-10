# Stage14-4cu — residual/Cayley orientation transfer, small linear product, and the 19/32 bound

## Status

`COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION`

Stage14-4cu consumes merged `4ct`, `s7-32`, `4cs`, and `4cr` on the same charged-once balanced physical collision packet.

Merged `s7-32` gives

```text
E(theta,phi)
 <= min(
      max(2*theta,1-2*theta),
      3*theta-1/4,
      3*phi-1/8
    )
 <= 5/8,
```

with unique `5/8` saturation

```text
(theta,phi)=(5/16,1/4).
```

Merged `4ct` then shows that any fixed-power odd coordinate gcd of the xi residual host saves the same exponent from the xi one-host count.  Stage14-4cu compares that residual-host Gaussian orientation to the `xi` plus-host orientation used by merged `4cr`.  The relative orientation is controlled by two endpoint-small linear forms

```text
L_- = z_1*r_2*s_2-z_2*r_1*s_1,
L_+ = z_1*r_2*s_2+z_2*r_1*s_1.
```

Their product has exponent at most `1/4`.  After the exact root-gcd and residual-gcd peels, the surviving joint common core divides `L_-L_+`.  This creates a new minimax bound

```text
boxed:
V(B) << B^(19/32+o(1)).
```

No external determinant method, large sieve, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported balanced strip and current envelopes

Use

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
3/16 <= theta <= 5/16,

R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)),
1/8 <= phi <= 1/4,

0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

The common core has exact dyadic exponent

```text
C=B^(chi+o(1)),
chi=2*theta+2*phi-3/4.                              (1.1)
```

The physical roots satisfy

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2,

gcd(x_1,y_1)=gcd(x_2,y_2)=1,

z_i=2*x_i*y_i/g_i=B^(1/8+o(1)),
g_i in {1,2},

omega_i=g_i*r_i*s_i,
r_i,s_i=B^o(1).                                     (1.2)
```

Merged `s7-32` supplies three legal alternative counts:

```text
E_s(theta)=max(2*theta,1-2*theta),
E_k(theta)=3*theta-1/4,
E_xi(phi)=3*phi-1/8.                                (1.3)
```

They count the same packet with different quantifier orders, so taking their minimum is legal.

---

## 2. The two cross-root gcd cells

Merged `4cs` identifies

```text
H=oddpart(gcd(X,Y)),
X=x_1*x_2,
Y=y_1*y_2,
H^2 | C*u_res,
H^2 | X*Y.                                         (2.1)
```

Because the same-state pairs are primitive, every odd prime of `H` occurs crosswise.  Define

```text
H_S := oddpart(gcd(x_2,y_1)),
H_T := oddpart(gcd(x_1,y_2)).                       (2.2)
```

Then primewise reducedness gives exactly

```text
boxed:
H=H_S*H_T,
gcd(H_S,H_T)=1.                                   (2.3)
```

There is no third common-root cell: a prime cannot lie in both cross cells without violating `gcd(x_i,y_i)=1`.

---

## 3. Cross-root cells force residual-host coordinate gcds

Use the two xi switched Gaussian hosts

```text
Z_S=R*x_2^2*omega_1+i*J*y_1^2*omega_2,
Z_T=J*y_2^2*omega_1+i*R*x_1^2*omega_2,              (3.1)
```

with merged `4cf/s7-32` descents

```text
Z_S=lambda_S^2*W_S,
Z_T=lambda_T^2*W_T,
N(lambda_S)=oddpart(S),
N(lambda_T)=oddpart(T),
N(W_S)=N(W_T)=q_xi=C*v_res*O_2(1).                  (3.2)
```

Define full coordinate gcds

```text
G_S=gcd(Re(W_S),Im(W_S)),
G_T=gcd(Re(W_T),Im(W_T)),                           (3.3)
```

and odd parts `g_S,g_T`.

Let an odd prime power `ell^e|H_S`.  Then `ell^e|x_2,y_1`, so `ell^(2e)` divides both coordinates of `Z_S`.  Reducedness of state 2 excludes `ell|S`; hence `lambda_S` is an `ell`-adic Gaussian unit and division by `lambda_S^2` preserves the common coordinate valuation.  Therefore

```text
boxed:
H_S^2 | g_S.                                       (3.4)
```

Similarly

```text
boxed:
H_T^2 | g_T.                                       (3.5)
```

Choose `star in {S,T}` so that in the current dyadic block

```text
H_star >= H_other.                                 (3.6)
```

Write

```text
g_star=B^(rho+o(1)).                               (3.7)
```

If `H_star=B^(eta_star+o(1))` and `H_other=B^(eta_other+o(1))`, then

```text
eta_other<=eta_star,
rho>=2*eta_star,
2*eta_other<=rho.                                  (3.8)
```

---

## 4. Gcd-stratified one-host count on either xi switched host

The `4ct` norm-gcd peel is symmetric in `S,T`.  For a fixed dyadic coordinate gcd

```text
g_star=B^(rho+o(1)),
```

choose `g_star` first.  Since `g_star^2|N(W_star)`, the residual norm support loses `2*rho`, while choosing the gcd costs only `rho`.  The switched square divisor and physical reconstruction costs are unchanged.  Hence

```text
boxed:
E_xi,star(theta,phi;rho)
 <= 3*phi-1/8-rho.                                 (4.1)
```

This is the general-strip form of the top-corner `5/8-rho` estimate proved in `4ct`.

The same statement is valid for the full coordinate gcd when only the counting saving is used; oddness is needed only for the Gaussian orientation comparison below.

---

## 5. Joint Cayley/residual good core

Merged `4cr/4cs` peel the xi plus-host coordinate gcd and give a Cayley-good core

```text
C_Cayley | C,
C/C_Cayley | B^o(1)*H^2,                            (5.1)
```

where the `B^o(1)` factor is the endpoint-small `g_A^2|r^2s^2` decoration.

Merged `4ct` gives the residual-host good core

```text
C_res := C/gcd(C,g_star^2).                         (5.2)
```

Put

```text
J_star := gcd(C_Cayley,C_res).                      (5.3)
```

The bad support removed from `C` is bounded by the lcm of `H^2` and `g_star^2`.  Because `H_star^2|g_star`, the `H_star` part is already absorbed in `g_star^2`; only the opposite cross cell can remain extra.  Thus

```text
C/J_star
 | B^o(1)*g_star^2*H_other^2.                      (5.4)
```

Using (3.8),

```text
boxed:
J_star >= B^(chi-3*rho-o(1)).                      (5.5)
```

This `J_star` is simultaneously primitive for the selected residual Gaussian host and for the xi Cayley plus host.

---

## 6. Residual orientation equals the original switched-host orientation

Let `p^e||J_star`.  The selected residual host `W_star` is primitive modulo `p`, and `p^e|N(W_star)`.

If `p` does not divide the switched cell (`S` or `T`), `lambda_star` is a unit and

```text
pi|W_star <=> pi|Z_star
```

for either Gaussian orientation `pi|p`.

If `p` also divides the switched cell, the square-divisor descent uses the unique orientation `pi^2|Z_star`.  Were the residual factor `W_star` divisible by the conjugate `bar(pi)`, then `Z_star` would be divisible by both `pi` and `bar(pi)`, hence both integer coordinates of `Z_star` would be divisible by `p`.  The switched-cell coprimality in merged `4cf` forbids this.  Therefore the remaining `p`-factor in `W_star` has the same orientation as `lambda_star` and `Z_star`.

Hence on all of `J_star`:

```text
boxed:
GAUSSIAN_ORIENTATION(W_star)=GAUSSIAN_ORIENTATION(Z_star). (6.1)
```

No switched-cell primes need to be discarded.

---

## 7. Compare the residual root to the xi plus-host root

Write

```text
P=R*x_1*x_2,
Q=J*y_1*y_2.                                       (7.1)
```

On `J_star`, the xi plus host is primitive and

```text
P^2+Q^2 == 0 (mod J_star).                         (7.2)
```

For the `T` host define the coordinate root

```text
w_T := (R*x_1^2*omega_2)/(J*y_2^2*omega_1),
y := P/Q.                                          (7.3)
```

Both satisfy square `-1` modulo every prime power of `J_T`, and direct cancellation gives

```text
w_T/y
 = x_1*y_1*omega_2/(x_2*y_2*omega_1)
 = z_1*r_2*s_2/(z_2*r_1*s_1).                     (7.4)
```

For the `S` host the same computation gives the negative reciprocal convention

```text
w_S/y
 = - z_1*r_2*s_2/(z_2*r_1*s_1).                   (7.5)
```

Since each quotient of two square roots of `-1` is `+1` or `-1`, every odd prime power of `J_star` divides one of

```text
L_- := z_1*r_2*s_2-z_2*r_1*s_1,
L_+ := z_1*r_2*s_2+z_2*r_1*s_1.                   (7.6)
```

The assignment is reversed between the `S` and `T` host, but the product is identical.  Because `J_star` is odd, the two sign factors are coprime on each prime-power allocation.  Therefore

```text
boxed:
J_star | L_-*L_+.                                  (7.7)
```

This is the missing exact bridge between the residual Gaussian divisor of `4ct` and the Cayley `xi` plus-host orientation of `4cr`.

---

## 8. Three-host orientation entropy collapses to four cells

Merged `4cr` already compares the primitive agreement/k-plus root `x` to the xi plus root `y`:

```text
C_+: y=x,
C_-: y=-x.                                         (8.1)
```

Section 7 compares the residual root `w_star` to `y` by the sign of `L_-` versus `L_+`.  Hence on `J_star` the three roots

```text
primitive agreement root x,
xi plus-host root y,
residual-host root w_star
```

carry only two binary relative signs.  Prime powers split into four pairwise-coprime cells

```text
J_{++}, J_{+-}, J_{-+}, J_{--},
J_{++}J_{+-}J_{-+}J_{--}=J_star,                   (8.2)
```

indexed by

```text
(y/x, w_star/y) in {+1,-1}^2.                     (8.3)
```

The first sign is the existing `C_+/C_-` Cayley allocation; the second is the new `L_-/L_+` linear allocation.  There is no third independent Gaussian orientation decoration.

This four-cell description is structural.  The saving below comes from the small size of the second sign hosts `L_-,L_+`, not from recharging the common core as another determinant modulus.

---

## 9. Nonproportional branch: joint core forces a residual gcd

Assume

```text
L_-*L_+ != 0.                                      (9.1)
```

All endpoint roots have scale `z_i=B^(1/8+o(1))` and `r_i,s_i=B^o(1)`, so

```text
|L_-*L_+| <= B^(1/4+o(1)).                         (9.2)
```

By (7.7),

```text
J_star <= B^(1/4+o(1)).                             (9.3)
```

Combine with (5.5):

```text
chi-3*rho <= 1/4+o(1).                             (9.4)
```

Hence

```text
boxed:
rho >= max(0,(chi-1/4)/3)-o(1).                   (9.5)
```

Using `chi=2theta+2phi-3/4`, the positive branch is

```text
rho >= (2theta+2phi-1)/3-o(1)                      (9.6)
```

whenever `theta+phi>1/2`.

Insert this into the selected xi one-host bound (4.1).

---

## 10. Exact nonproportional minimax: 19/32

### 10.1. Region `theta+phi<=1/2`

Here `chi<=1/4`, so the orientation-product argument need not force a positive `rho`.

If `theta<=1/4`, the k one-host bound gives

```text
E<=3theta-1/4<=1/2<19/32.                          (10.1)
```

If `theta>=1/4`, then `E_s=2theta` and

```text
phi<=1/2-theta
=> E_xi<=3phi-1/8<=11/8-3theta.                    (10.2)
```

Therefore

```text
E<=min(2theta,11/8-3theta)<=11/20<19/32.           (10.3)
```

### 10.2. Region `theta+phi>1/2`

Now `theta>1/4`, so

```text
E_s=2theta.                                         (10.4)
```

By (4.1) and (9.6),

```text
E_xi,star
 <= 3phi-1/8-(2theta+2phi-1)/3
 = 7phi/3-2theta/3+5/24.                           (10.5)
```

Since `phi<=1/4`,

```text
E_xi,star <= 19/24-2theta/3.                       (10.6)
```

Thus

```text
E<=min(2theta,19/24-2theta/3).                     (10.7)
```

The two branches cross at

```text
2theta=19/24-2theta/3
=> theta=19/64,                                    (10.8)
```

where

```text
E=19/32.                                           (10.9)
```

Hence uniformly on the nonproportional branch,

```text
boxed:
E_nonprop<=19/32.                                  (10.10)
```

Equality forces

```text
boxed:
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
log_B J_star=1/4.                                  (10.11)
```

---

## 11. Proportional branch: `L_-=0` forces a large k-host coordinate gcd

Because all variables are positive,

```text
L_+>0.                                             (11.1)
```

Thus the only zero-product branch is

```text
L_-=0,
```

i.e.

```text
z_1*r_2*s_2=z_2*r_1*s_1.                          (11.2)
```

Reduce the endpoint-small ratio

```text
r_1*s_1 : r_2*s_2 = a:b,
gcd(a,b)=1,
a,b=B^o(1).                                        (11.3)
```

Then (11.2) gives

```text
z_1=a*t,
z_2=b*t                                           (11.4)
```

for an integer

```text
t=B^(1/8+o(1)).                                    (11.5)
```

Use the k switched host

```text
Z_beta=alpha*r_2^2*z_1+i*delta*s_1^2*z_2
      =lambda_beta^2*W_beta.                       (11.6)
```

The full integer `t` divides both coordinates of `Z_beta`.  Since `beta|k` and merged coprimality gives

```text
gcd(k,xi*z_1*z_2)=1,                               (11.7)
```

`lambda_beta` has norm coprime to `t`; dividing by `lambda_beta^2` preserves the common coordinate divisor.  Hence

```text
boxed:
t | gcd(Re(W_beta),Im(W_beta)).                    (11.8)
```

The gcd-stratified k one-host count therefore saves at least `1/8` from

```text
E_k=3theta-1/4,
```

giving

```text
E_prop
 <= 3theta-3/8
 <= 9/16                                           (11.9)
```

because `theta<=5/16`.

Thus

```text
boxed:
E_prop<=9/16<19/32.                                (11.10)
```

The proportional branch cannot saturate the new bound.

---

## 12. Whole-family promotion to 19/32

Every physical packet lies in exactly one of the two branches:

```text
L_-*L_+ != 0,
or
L_-=0                                              (12.1)
```

(the branch `L_+=0` is impossible by positivity).

Sections 10-11 give

```text
E_nonprop<=19/32,
E_prop<=9/16.                                      (12.2)
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32.       (12.3)
```

Since

```text
5/8-19/32=1/32,                                    (12.4)
```

we obtain a new unconditional whole-family fixed-power saving:

```text
boxed:
IMPROVEMENT_OVER_PREVIOUS_5_8=1/32,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.         (12.5)
```

No support is charged twice:

- `E_s`, `E_k`, and `E_xi,star` are alternative complete counts of the same physical block;
- `J_star` is used only to force the already-counted residual gcd `g_star` through (9.5);
- `C_+/C_-` and `L_-/L_+` only partition the same joint common core and are not multiplied back as independent spacing moduli.

---

## 13. New 19/32 saturation packet

The only possible `19/32` saturation of the proved envelope is the nonproportional block

```text
boxed:
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
J_star=B^(1/4+o(1)).                               (13.1)
```

At this packet:

```text
C            ~ B^(11/32),
selected xi residual coordinate gcd ~ B^(1/32),
joint Cayley/residual good core J_star ~ B^(1/4),
|L_-L_+|    ~ B^(1/4),
R,J          ~ B^(1/4),
S,T          ~ B^(1/8).                            (13.2)
```

The prime-power support of `J_star` is partitioned simultaneously by

```text
C_+/C_-                    (agreement-vs-xi Cayley sign),
L_-/L_+                    (xi-plus-vs-residual sign).   (13.3)
```

The next minimal receiver is

```text
NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence. (13.4)
```

It retains the exact four orientation cells, the selected residual gcd at exponent `1/32`, and the near-saturation divisibility `J_star|L_-L_+` with both sides at exponent `1/4`.

---

## 14. H / tH decision

No auxiliary H theorem is needed in Stage14-4cu.

The `19/32` improvement uses only:

- merged exact common-core and root-gcd peels;
- merged Gaussian square descent and one-host reconstruction;
- primewise Gaussian orientation uniqueness;
- the exact endpoint identity (7.4)-(7.5);
- a two-factor integer divisibility and exact minimax bookkeeping.

Therefore

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T72_CROSS_PROMOTED_TO_MAINLINE=false.              (14.1)
```

A new H should be considered only if the exact `19/32` receiver survives the next divisor-allocation step and leaves a genuinely averaged incidence theorem.  The old generic genus-one H remains nonminimal.

---

## Stage boundary

```text
STAGE14_4CU=COMPLETE_RESIDUAL_CAYLEY_ORIENTATION_LINEAR_PRODUCT_TRANSFER_AND_19_32_PROMOTION
MERGED_4CT_IMPORTED=true
MERGED_S7_32_IMPORTED=true
MERGED_4CS_IMPORTED=true
MERGED_4CR_IMPORTED=true
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