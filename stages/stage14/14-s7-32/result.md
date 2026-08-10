# Stage14-s7-32 — one-host Gaussian reconstruction and collapse of the two 5/8 boundaries

## Status

`COMPLETE_ONE_HOST_GAUSSIAN_RECONSTRUCTION_AND_UNIQUE_TOP_CORNER_5_8_LOCALIZATION`

Stage14-s7-32 consumes merged `s7-31` and the exact Gaussian square-divisor descents of merged `4cf/4cg`, together with the rank-one xi CRT rigidity of merged `4cj`.

Merged s7-31 proves

```text
V(B) << B^(5/8+o(1))
```

with two apparent saturation loci:

```text
upper edge:  theta=5/16, 3/16<=phi<=1/4,
lower corner: theta=phi=3/16.
```

The purpose of s7-32 is to test those two loci with a different legal quantifier order.  Instead of fixing the common-core packet first, choose one switched Gaussian square divisor and its residual Gaussian quotient.  One such host already reconstructs the entire physical collision up to `B^o(1)` multiplicity.

There are two versions.

- One `k`-switched host gives

```text
E_k(theta) <= 3*theta-1/4.
```

- One `xi`-switched host, together with the already-proved agreement-cell CRT short-root uniqueness, gives

```text
E_xi(phi) <= 3*phi-1/8.
```

Combining these alternative counts with merged s7-31,

```text
E_s(theta)=max(2*theta,1-2*theta),
```

gives

```text
E(theta,phi)
 <= min(
      max(2*theta,1-2*theta),
      3*theta-1/4,
      3*phi-1/8
    )
 <= 5/8.
```

The exponent does **not** improve below `5/8` in this stage.  What improves sharply is the saturation geometry: equality can occur only at

```text
boxed:
(theta,phi)=(5/16,1/4).
```

Thus the lower corner disappears completely, and every point of the old top-theta edge with `phi<1/4` is power-saved.

No external determinant method, large sieve, genus-one theorem, or H/tH theorem is used.

---

## 1. Imported balanced packet

Use the merged common-core strip

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

The two physical states are

```text
P_1=(R*S)*x_1^2,
Q_1=(T*J)*y_1^2,
P_2=(R*T)*x_2^2,
Q_2=(S*J)*y_2^2,
```

with

```text
x_i,y_i=B^(1/16+o(1)).
```

The k-split cells are

```text
k_{-,1}=alpha*beta,
k_{+,1}=gamma*delta,
k_{-,2}=alpha*gamma,
k_{+,2}=beta*delta,
```

and

```text
u_i=(Q_i-P_i)/g_i=k_{-,i} r_i^2,
v_i=(Q_i+P_i)/g_i=k_{+,i} s_i^2,
g_i in {1,2},
r_i,s_i=B^o(1).
```

Write

```text
z_i=2*x_i*y_i/g_i=B^(1/8+o(1)),
omega_i=g_i*r_i*s_i=B^o(1).
```

Merged 4cg supplies the equal residual norms

```text
q_beta=q_gamma=:q_k,
q_S=q_T=:q_xi.
```

Merged 4cf/4ci give the exact positive host equations

```text
beta^2*q_k
 = alpha^2*r_2^4*z_1^2
   +delta^2*s_1^4*z_2^2,                         (1.1)

gamma^2*q_k
 = delta^2*s_2^4*z_1^2
   +alpha^2*r_1^4*z_2^2,                         (1.2)

S^2*q_xi
 = R^2*x_2^4*omega_1^2
   +J^2*y_1^4*omega_2^2,                         (1.3)

T^2*q_xi
 = J^2*y_2^4*omega_1^2
   +R^2*x_1^4*omega_2^2.                         (1.4)
```

The corresponding Gaussian hosts are

```text
Z_beta
 = alpha*r_2^2*z_1
   + i*delta*s_1^2*z_2,                           (1.5)

Z_S
 = R*x_2^2*omega_1
   + i*J*y_1^2*omega_2.                           (1.6)
```

After the finite 2-primary convention, merged 4cf gives

```text
Z_beta=lambda_beta^2 W_beta,
N(lambda_beta)=oddpart(beta),
N(W_beta)=q_k * O_2(1),                            (1.7)

Z_S=lambda_S^2 W_S,
N(lambda_S)=oddpart(S),
N(W_S)=q_xi * O_2(1),                              (1.8)
```

where `O_2(1)` denotes one of finitely many powers coming from the squarefree cell's possible factor `2`.

---

## 2. Residual norm ranges in one variable

From merged 4cf,

```text
q_k <= B^(4*theta-3/4+o(1)),                       (2.1)
q_xi<= B^(4*phi-1/2+o(1)).                         (2.2)
```

These are exactly the residual norms seen by one switched host before imposing the common-core decomposition.

The switched-cell norm scales are

```text
N(lambda_beta)=B^(1/2-theta+o(1)),                 (2.3)
N(lambda_S)   =B^(3/8-phi+o(1)).                   (2.4)
```

The number of Gaussian integers with norm in a dyadic interval of size `L` is `O(L)`.  Consequently the raw choices for one square divisor satisfy

```text
#lambda_beta <= B^(1/2-theta+o(1)),                (2.5)
#lambda_S    <= B^(3/8-phi+o(1)).                  (2.6)
```

For fixed residual norm `q`, the Gaussian quotient `W` has at most divisor-many representations, hence `B^o(1)` choices.  Summing over all residual norms up to (2.1) or (2.2) therefore costs exactly the residual-support exponent and no additional fixed power.

The only remaining issue is whether fixing one host leaves a positive-dimensional physical fiber.  Sections 3 and 4 show that it does not.

---

## 3. One k-switched Gaussian host reconstructs the physical pair

Fix the following data:

```text
q_k,
lambda_beta,
W_beta,
finite 2-primary beta decoration,
(r_1,s_1,r_2,s_2,g_1,g_2).
```

The endpoint-small tuple contributes only `B^o(1)` possibilities.

Equation (1.7) reconstructs the integer coordinates of `Z_beta` exactly up to one Gaussian unit, so define

```text
A_beta=Re(Z_beta),
B_beta=Im(Z_beta).                                  (3.1)
```

Every physical lift must satisfy

```text
A_beta=alpha*r_2^2*z_1,
B_beta=delta*s_1^2*z_2.                             (3.2)
```

For fixed small `r_2,s_1`, the number of decompositions of a fixed integer coordinate into

```text
squarefree cell * positive integer root
```

in the required dyadic ranges is divisor-bounded.  Hence

```text
(A_beta,B_beta)
 => (alpha,delta,z_1,z_2)
```

with `B^o(1)` multiplicity.  This statement is purely arithmetic: choose the squarefree divisor `alpha|A_beta/r_2^2` and `delta|B_beta/s_1^2`; the complementary roots are then forced.  Invalid choices are discarded by the physical masks.

The norm of the second k-host is now determined:

```text
N(Z_gamma)
 = delta^2*s_2^4*z_1^2
   +alpha^2*r_1^4*z_2^2.                           (3.3)
```

Since (1.2) must hold with the already fixed `q_k`,

```text
gamma^2=N(Z_gamma)/q_k.                            (3.4)
```

Thus `gamma` is uniquely determined if the quotient is a positive square, and otherwise the candidate is nonphysical.  The chosen `lambda_beta` already determines `oddpart(beta)` and its finite 2-primary decoration determines `beta`.

Therefore all four k cells are fixed:

```text
(alpha,beta,gamma,delta).                           (3.5)
```

Now reconstruct the two states directly from the k split:

```text
u_1=alpha*beta*r_1^2,
v_1=gamma*delta*s_1^2,

u_2=alpha*gamma*r_2^2,
v_2=beta*delta*s_2^2,                                (3.6)
```

and

```text
P_i=g_i*(v_i-u_i)/2,
Q_i=g_i*(v_i+u_i)/2.                                (3.7)
```

Every legal physical packet has integral positive values here.  Once `(P_i,Q_i)` are fixed, their canonical squarefree decompositions

```text
P_i=a_i*x_i^2,
Q_i=b_i*y_i^2,
```

are unique, so the xi cells `(R,S,T,J)` and all physical roots are recovered uniquely.

Hence

```text
boxed:
fixed one k-switched Gaussian host data
=> physical collision fiber B^o(1).                 (3.8)
```

No common-core root-line count is charged in this alternative quantifier order.

---

## 4. One xi-switched Gaussian host also reconstructs the physical pair

The xi side needs one extra ingredient because a canonical `P/Q` allocation does not by itself determine the `Q-P,Q+P` split.  The needed ingredient is already merged: the agreement-cell CRT congruences have moduli much larger than the root box.

Fix

```text
q_xi,
lambda_S,
W_S,
finite 2-primary S decoration,
(omega_1,omega_2),
one legal primewise orientation on R and J.
```

The omega variables are endpoint-small, and the number of orientation decorations is `B^o(1)`.

Equation (1.8) reconstructs

```text
A_S=Re(Z_S),
B_S=Im(Z_S),                                       (4.1)
```

with

```text
A_S=R*x_2^2*omega_1,
B_S=J*y_1^2*omega_2.                               (4.2)
```

For fixed `omega_1,omega_2`, divisor decomposition of the fixed coordinates gives

```text
(R,x_2,J,y_1)
```

with only `B^o(1)` possibilities.  The chosen `lambda_S` fixes `S` up to its finite 2-primary decoration.

Now use the two xi agreement root congruences from merged s7-21/4cj:

```text
y_1 == lambda_R*y_2 (mod R^2),
x_1 == lambda_J*x_2 (mod J^2).                     (4.3)
```

Every physical root lies in a box of size `B^(1/16+o(1))`, whereas

```text
R^2,J^2 >= B^(1/4-o(1)).                           (4.4)
```

throughout the balanced strip.  Therefore for a fixed orientation each congruence has at most one physical positive root in the short box.  Consequently

```text
(R,J,x_2,y_1, orientations)
=> (x_1,y_2)
```

with `B^o(1)` multiplicity.                         (4.5)

It remains to recover the last xi cell `T`.  Equality of the two k labels gives

```text
(Q_1^2-P_1^2)/omega_1^2
 = (Q_2^2-P_2^2)/omega_2^2.                        (4.6)
```

Substituting

```text
P_1=R*S*x_1^2,
Q_1=T*J*y_1^2,
P_2=R*T*x_2^2,
Q_2=S*J*y_2^2
```

yields the exact linear equation in `T^2`

```text
T^2 * (
  omega_2^2*J^2*y_1^4
 +omega_1^2*R^2*x_2^4
)
=
S^2 * (
  omega_1^2*J^2*y_2^4
 +omega_2^2*R^2*x_1^4
).                                                  (4.7)
```

The coefficient on the left is positive.  Thus `T^2`, and hence positive `T`, is uniquely determined if the quotient is an integral square.

At this point all xi cells and roots are fixed, so `(P_i,Q_i)` are fixed.  Their `Q-P,Q+P` canonical squarefree decompositions then recover the k cells and endpoint-small k roots with divisor-many multiplicity.

Therefore

```text
boxed:
fixed one xi-switched Gaussian host data
+ agreement CRT orientation
=> physical collision fiber B^o(1).                 (4.8)
```

This is the xi-side one-host reconstruction theorem needed to remove the old top-edge continuum.

---

## 5. Alternative one-host block bounds

### 5.1 k-host count

Choose `q_k`, one Gaussian square divisor `lambda_beta`, its residual quotient `W_beta`, and endpoint-small decorations.  By Sections 2-3,

```text
E_k(theta)
 <= (4*theta-3/4) + (1/2-theta)
 = 3*theta-1/4.                                    (5.1)
```

Thus

```text
boxed:
E_k(theta)<=3*theta-1/4.                           (5.2)
```

At the old lower corner `theta=3/16`,

```text
E_k=5/16,                                          (5.3)
```

so that corner is far below the `5/8` barrier.

For all `theta<=1/4`,

```text
E_k(theta)<=1/2.                                   (5.4)
```

Hence every lower-theta block is already at or below square-root scale under this alternative count.

### 5.2 xi-host count

Likewise Sections 2 and 4 give

```text
E_xi(phi)
 <= (4*phi-1/2)+(3/8-phi)
 = 3*phi-1/8.                                      (5.5)
```

Thus

```text
boxed:
E_xi(phi)<=3*phi-1/8.                              (5.6)
```

In particular

```text
phi<1/4
=> E_xi(phi)<5/8.                                  (5.7)
```

At `phi=1/4`, the bound is exactly `5/8`.

---

## 6. Minimax with merged s7-31

Merged s7-31 gives the same physical block the independent upper bound

```text
E_s(theta)=max(2*theta,1-2*theta).                 (6.1)
```

The one-host counts are alternative quantifier orders for the same family, so taking the minimum is legal:

```text
boxed:
E(theta,phi)
 <= min(
      max(2*theta,1-2*theta),
      3*theta-1/4,
      3*phi-1/8
    ).                                             (6.2)
```

No supports from different ledgers are multiplied.

### 6.1 theta <= 1/4

By (5.4),

```text
E(theta,phi)<=1/2.                                 (6.3)
```

So the old lower corner `(3/16,3/16)` is not a current saturation point.

### 6.2 theta >= 1/4

Merged s7-31 gives

```text
E_s(theta)=2*theta<=5/8.                           (6.4)
```

Equality requires

```text
theta=5/16.                                        (6.5)
```

But if additionally `phi<1/4`, then (5.7) gives a strict saving.  Hence equality in the combined envelope also requires

```text
phi=1/4.                                           (6.6)
```

Therefore

```text
boxed:
UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4). (6.7)
```

The current whole-family theorem remains

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8.         (6.8)
```

No claim below `5/8` is made because both the merged s7-31 count and the xi one-host count attain `5/8` at the top corner.

---

## 7. Exact scales at the unique top corner

At

```text
theta=5/16,
phi=1/4,
```

we have

```text
alpha,delta = B^(5/16+o(1)),
beta,gamma  = B^(3/16+o(1)),
R,J         = B^(1/4+o(1)),
S,T         = B^(1/8+o(1)).                        (7.1)
```

Merged s7-30/31 pin

```text
C=B^(3/8+o(1)),
u_res<=B^(1/8+o(1)),
v_res<=B^(1/8+o(1)).                               (7.2)
```

The residual norms have maximal scale

```text
q_k=C*u_res <= B^(1/2+o(1)),
q_xi=C*v_res<= B^(1/2+o(1)).                       (7.3)
```

The xi one-host barrier is exactly

```text
q_xi support:       B^(1/2),
lambda_S support:   B^(1/8),
physical fiber:     B^o(1),
--------------------------------
total:              B^(5/8+o(1)).                 (7.4)
```

The remaining saving must therefore couple the residual Gaussian quotient `W_S` or its norm `q_xi=C*v_res` to the common-core/primitive-agreement structure.  Treating `q_xi` and `lambda_S` as independent ambient parameters cannot improve the exponent.

Define the new minimal receiver

```text
TopCornerCommonCoreXiGaussianSquareHostPrimitiveAgreementIncidence.  (7.5)
```

It retains simultaneously

```text
(theta,phi)=(5/16,1/4),
C~B^(3/8),
v_res<=B^(1/8),
q_xi=C*v_res,
Z_S=lambda_S^2 W_S,
N(lambda_S)=S~B^(1/8),
N(W_S)=q_xi*O_2(1),
primitive xi agreement pair (U,V),
common-core Gaussian root orientation,
full reciprocal reconstruction,
all physical masks.
```

This is narrower than the generic four-root or genus-one receivers.

---

## 8. Relation to merged 4cr/X8/t70

Merged 4cr and X8 prove a `2/3` minimax bound from the older s7-30 ledger plus the dual-Cayley ledger.  Their exact Cayley/Gaussian orientation factorization remains compatible, but their exponent is superseded on the s route by merged s7-31's `5/8` theorem.

Stage14-s7-32 does not regress to `2/3` and does not multiply the old dual-Cayley support into the one-host count.

Merged t70 concerns a different fixed-`U` Cayley coefficient space.  Its primitive common-support root-line lemma is not needed for Sections 3-6 and is not cross-promoted.

---

## 9. H / tH decision

No new s-side H theorem is needed.

The stage uses only:

- merged exact Gaussian square descent;
- divisor-bounded factorization of fixed integer coordinates;
- equality of the two residual norms;
- already-merged xi agreement CRT root orientations;
- modulus-versus-root-box uniqueness;
- exact reconstruction identities.

Therefore

```text
S7_32_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_32=false
T70_CROSS_PROMOTED_TO_S7_32=false
GENERIC_GENUS_ONE_H_USED_BY_S7_32=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.               (9.1)
```

An s-specific H should be reconsidered only if the exact top-corner receiver (7.5) survives further common-core/Gaussian quotient factorization.

---

## Stage boundary

```text
STAGE14_S7_32=COMPLETE_ONE_HOST_GAUSSIAN_RECONSTRUCTION_AND_UNIQUE_TOP_CORNER_5_8_LOCALIZATION
MERGED_S7_31_IMPORTED=true
MERGED_4CF_GAUSSIAN_SQUARE_DESCENT_IMPORTED=true
MERGED_4CG_EQUAL_RESIDUAL_NORMS_IMPORTED=true
MERGED_4CJ_XI_RANK_ONE_ROOT_RIGIDITY_IMPORTED=true
K_ONE_SWITCHED_GAUSSIAN_HOST_PHYSICAL_FIBER=Bo1
XI_ONE_SWITCHED_GAUSSIAN_HOST_PLUS_AGREEMENT_ORIENTATION_PHYSICAL_FIBER=Bo1
K_ONE_HOST_BLOCK_EXPONENT=3theta-1/4
XI_ONE_HOST_BLOCK_EXPONENT=3phi-1/8
COMBINED_BLOCK_EXPONENT=min(max(2theta,1-2theta),3theta-1/4,3phi-1/8)
LOWER_THETA_HALF_UPPER_BOUND_EXPONENT=1/2
OLD_FIVE_EIGHTHS_LOWER_CORNER_SURVIVES=false
OLD_FIVE_EIGHTHS_TOP_EDGE_PHI_LT_1_4_SURVIVES=false
UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4)
TOP_CORNER_COMMON_CORE_EXPONENT=3/8
TOP_CORNER_QK_EXPONENT=1/2
TOP_CORNER_QXI_EXPONENT=1/2
TOP_CORNER_XI_SWITCHED_CELL_EXPONENT=1/8
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8
NEW_WHOLE_FAMILY_POWER_SAVING_BELOW_5_8_PROVED=false
CURRENT_GAP_TO_SQRT=1/8
REMAINING_RECEIVER=TopCornerCommonCoreXiGaussianSquareHostPrimitiveAgreementIncidence
S7_32_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_32=false
T70_CROSS_PROMOTED_TO_S7_32=false
GENERIC_GENUS_ONE_H_USED_BY_S7_32=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-33
```