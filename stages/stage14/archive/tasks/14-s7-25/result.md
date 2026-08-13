# Stage14-s7-25 — fixed xi-switch-product shell reconstruction and top-theta localization

## Status

`COMPLETE_FIXED_RESIDUAL_XI_SWITCH_PRODUCT_RECONSTRUCTION_AND_TOP_THETA_LOCALIZATION`

Stage14-s7-25 starts from latest merged main containing s7-24, 4cj, 4ck and X3.  The xi short-vector geometry is already exhausted:

```text
physical xi short span rank = 1,
primitive xi root line is saturated,
fixed oriented xi-CRT packet has at most one physical root vector.
```

X3/4ck show that, if one fixes the primitive root line first, the remaining moving-cell problem can be expressed as a binary-quartic agreement incidence and that the relaxed equal-value quartic problem has a diagonal obstruction.  This stage uses a different quantifier order.

Define the xi-switch product

```text
U := S*T.
```

The new theorem is

```text
fixed (C,u_res,v_res,U)
=> B^o(1) legal decorated physical endpoint packets.          (0.1)
```

No primitive root direction is fixed in (0.1).  It is reconstructed inside the fiber.  The proof uses the exact 4cg common-core factors twice: first as a Pythagorean shell, then as a difference-of-squares shell.

Combining (0.1) with the exact 4ci dyadic residual support gives the unconditional block estimate

```text
E(theta,phi) << B^(2*theta+1/4+o(1)).                         (0.2)
```

Thus every block with `theta<=5/16-epsilon` is already saved by `2*epsilon`.  The only surviving `7/8` barrier is

```text
theta=5/16,
3/16<=phi<=1/4.                                                (0.3)
```

The whole-family exponent remains `7/8` because this top-theta edge is not yet power-saved.

---

## 1. Imported exact packet

Keep the balanced cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Use the product coordinates

```text
U := S*T,                 # xi switch
V := R*J,                 # xi agreement
M := beta*gamma,          # k switch
N := alpha*delta.         # k agreement                       (1.1)
```

Then

```text
xi=U*V,
k=M*N.                                                         (1.2)
```

Merged 4cg gives one odd common core `C` and positive residuals `u,v`:

```text
q_k=C*u,
q_xi=C*v.                                                       (1.3)
```

It also gives

```text
H_k^+
 = delta^2*s_1^2*s_2^2 + alpha^2*r_1^2*r_2^2,
H_k^-
 = delta^2*s_1^2*s_2^2 - alpha^2*r_1^2*r_2^2 > 0,

U*V*C*u=H_k^+*H_k^-,                                           (1.4)
```

and

```text
H_xi^+
 = J^2*y_1^2*y_2^2 + R^2*x_1^2*x_2^2,
H_xi^-
 = J^2*y_1^2*y_2^2 - R^2*x_1^2*x_2^2 > 0,

M*N*C*v=H_xi^+*H_xi^-.                                         (1.5)
```

The common-core definition is

```text
C=oddpart(H_k^+/oddpart(U))
 =oddpart(H_xi^+/oddpart(M)).                                  (1.6)
```

All later reductions remain on this same physical packet.  X1 supplies the charged-once bridge, so no hypothetical savings from different descriptions are multiplied.

---

## 2. Endpoint-small data cost only `B^o(1)`

At the endpoint

```text
r_i,s_i=B^o(1),
g_i in {1,2}.                                                   (2.1)
```

The total number of tuples `(r_1,s_1,r_2,s_2,g_1,g_2)` is therefore `B^o(1)`.  A finite list of 2-adic valuations has only `O(log B)^{O(1)}=B^o(1)` choices.  Primewise orientation branches and Gaussian-unit decorations are also `B^o(1)` by the merged s7/X1 interface.

Fix these harmless decorations.  Put

```text
rho:=r_1*r_2*s_1*s_2.                                          (2.2)
```

---

## 3. Fixed `(C,U)` fixes `H_k^+` up to dyadic multiplicity

Equation (1.6) gives

```text
oddpart(H_k^+)=C*oddpart(U).
```

Hence

```text
boxed:
H_k^+=2^a*C*oddpart(U),
a=O(log B).                                                     (3.1)
```

For fixed `C,U`, there are only `B^o(1)` possible values of `H_k^+`.

---

## 4. First shell: recover `H_k^-` and `N=alpha*delta`

Let

```text
A=delta^2*s_1^2*s_2^2,
B=alpha^2*r_1^2*r_2^2.
```

Then `H_k^+=A+B` and `H_k^-=A-B`, so

```text
(H_k^+)^2-(H_k^-)^2
 =4*A*B
 =(2*rho*N)^2.
```

Thus

```text
boxed:
(H_k^+)^2=(H_k^-)^2+(2*rho*N)^2.                    (4.1)
```

For fixed `H_k^+` and `rho`, every candidate `(H_k^-,N)` is an integral representation of the fixed square `(H_k^+)^2` as a sum of two squares.  The elementary representation bound

```text
r_2(n)<=4*tau(n)                                                (4.2)
```

gives

```text
boxed:
# {(H_k^-,N)}=B^o(1).                                          (4.3)
```

No average theorem is used.

---

## 5. Recover `V=R*J`

From (1.4), once `H_k^-` is fixed,

```text
boxed:
V=H_k^+*H_k^-/(U*C*u).                                         (5.1)
```

Integrality and positivity only reject candidates.  Therefore

```text
boxed:
fixed (C,u,v,U)
=> (V,N) have B^o(1) possibilities.                            (5.2)
```

---

## 6. Fixed `(v,N)` leaves only dyadic-many `H_xi^-`

Write

```text
M=2^e*M_o,
M_o=oddpart(M).
```

By (1.6), for some `b=O(log B)`,

```text
H_xi^+=2^b*C*M_o.                                               (6.1)
```

Insert this into (1.5):

```text
2^e*M_o*N*C*v
 =2^b*C*M_o*H_xi^-.
```

Therefore

```text
boxed:
H_xi^-=2^(e-b)*N*v.                                            (6.2)
```

The right side must be integral and positive.  Thus fixed `(v,N)` gives only `B^o(1)` possible values of `H_xi^-`.  The odd part of the still-unknown `M` has cancelled.

---

## 7. Second shell: recover `H_xi^+` and the total root product

Put

```text
W:=x_1*y_1*x_2*y_2.                                            (7.1)
```

From the definitions in (1.5),

```text
(H_xi^+)^2-(H_xi^-)^2
 =4*R^2*J^2*x_1^2*x_2^2*y_1^2*y_2^2
 =(2*V*W)^2.
```

Hence

```text
boxed:
(H_xi^+)^2-(2*V*W)^2=(H_xi^-)^2.                    (7.2)
```

Equivalently,

```text
(H_xi^+-2*V*W)(H_xi^++2*V*W)=(H_xi^-)^2.            (7.3)
```

For fixed `H_xi^-` and `V`, the two factors in (7.3) form a factor pair of the fixed integer `(H_xi^-)^2`.  Hence

```text
boxed:
# {(H_xi^+,W)}=B^o(1).                                          (7.4)
```

Parity and divisibility conditions for recovering `W` only remove candidates.

---

## 8. Recover `M=beta*gamma`

Now (1.5) gives

```text
boxed:
M=H_xi^+*H_xi^-/(N*C*v).                                      (8.1)
```

Thus

```text
boxed:
fixed (C,u,v,U)
=> (V,N,M,W) have B^o(1) possibilities.                        (8.2)
```

---

## 9. Split the recovered products

The cells satisfy

```text
S*T=U,
R*J=V,
beta*gamma=M,
alpha*delta=N.                                                 (9.1)
```

The number of ordered positive splits is at most

```text
tau(U)*tau(V)*tau(M)*tau(N)=B^o(1).                            (9.2)
```

Squarefreeness, pairwise coprimality, the balanced dyadic boxes and all canonical prime-routing masks only reduce this list.

Similarly

```text
x_1*y_1*x_2*y_2=W
```

has at most `d_4(W)=B^o(1)` ordered positive root quadruples.  Once cells and roots are fixed,

```text
a_1=R*S,  b_1=T*J,
a_2=R*T,  b_2=S*J,
P_i=a_i*x_i^2,
Q_i=b_i*y_i^2                                                     (9.3)
```

reconstruct the two states, and the remaining k-side identities are rejection tests.

---

## 10. Fixed `(C,u,v,U)` packet fiber theorem

Multiplying Sections 2--9 gives

```text
boxed:
# {
  legal decorated physical endpoint packets
  with fixed (C,u,v,U=S*T)
 }
 <= B^o(1).                                                     (10.1)
```

Therefore

```text
FIXED_RESIDUAL_XI_SWITCH_PRODUCT_PACKET_FIBER_BO1=true.         (10.2)
```

This theorem uses a different quantifier order from X3.  X3 fixes the primitive root line and studies moving agreement cells; s7-25 fixes the switch product `S*T` and reconstructs the root data.  Hence X3's relaxed quartic diagonal obstruction does not contradict (10.1), and (10.1) does not claim the X3 fixed-root-line receiver is pointwise `B^o(1)`.

---

## 11. Dyadic support of the xi-switch product

The balanced xi cells are

```text
R,J=B^(phi+o(1)),
S,T=B^(3/8-phi+o(1)).                                  (11.1)
```

Hence

```text
boxed:
U=S*T=B^(3/4-2*phi+o(1)).                              (11.2)
```

The raw number of possible integer `U` values in one block is therefore

```text
boxed:
B^(3/4-2*phi+o(1)).                                   (11.3)
```

Because (10.1) is a charged-once fiber theorem, (11.3) can be multiplied with the residual-support count without violating the toolbox independence guard.

---

## 12. Unconditional block bound

Merged 4ci gives

```text
# {(C,u,v) in one (theta,phi) block}
 <=B^(2*theta+2*phi-1/2+o(1)).                        (12.1)
```

Combining (10.1), (11.3) and (12.1),

```text
E(theta,phi)
 <=B^(2*theta+2*phi-1/2)
   *B^(3/4-2*phi)
   *B^o(1).
```

Thus

```text
boxed:
E(theta,phi)<<B^(2*theta+1/4+o(1)).                   (12.2)
```

The `phi` dependence cancels exactly.

---

## 13. Fixed-power saving away from the top theta boundary

Since

```text
3/16<=theta<=5/16,
```

we have

```text
7/8-(2*theta+1/4)
 =2*(5/16-theta).                                    (13.1)
```

Therefore, for every fixed `epsilon>0`,

```text
theta<=5/16-epsilon
```

implies

```text
boxed:
E(theta,phi)<<B^(7/8-2*epsilon+o(1)).                 (13.2)
```

So every fixed-distance off-top-theta block is already power-saved unconditionally.

---

## 14. Remaining saturation edge

At

```text
theta=5/16,
```

(12.2) is exactly `B^(7/8+o(1))`.

The merged common-core strip is

```text
0<=theta-phi<=1/8,
theta+phi>=3/8.
```

Thus the surviving top edge is

```text
boxed:
theta=5/16,
3/16<=phi<=1/4.                                      (14.1)
```

The s7-24 statement that `(5/16,1/4)` was the unique **conditional** saturation corner used the unproved fixed-`X` fiber and paid the raw `X` support.  Stage14-s7-25 replaces that conditional ledger by the proved fixed-`U` reconstruction.  The proved saturation set is therefore the top-theta edge (14.1).

---

## 15. Relation to merged 4ck and X3

Merged 4ck/X3 reduce the fixed-root-line quantifier order to the split quartic

```text
F(a,b)=a*b*(b-a)*(b+a)
```

with switch-product integrality conditions.  X3 correctly shows that a relaxed equal-value quartic estimate cannot be `B^o(1)` because of a diagonal fixed-power family.

Stage14-s7-25 does not use a relaxed equal-value estimate.  It fixes `U=S*T` first, after which the exact common-core odd-part relation fixes `H_k^+` up to a dyadic choice and forces the Pythagorean shell (4.1).  The second shell then reconstructs the root product.  Thus the new result is complementary to the quartic reduction:

```text
4ck/X3 quantifier:
  fixed residual + root line -> quartic agreement cells move;

s7-25 quantifier:
  fixed residual + xi-switch product -> both agreement products and roots are divisor-many.  (15.1)
```

No X3 claim is strengthened beyond this exact compatible transfer.

```text
MERGED_4CK_COMPATIBILITY_CHECKED=true
MERGED_X3_COMPATIBILITY_CHECKED=true
X3_RELAXED_DIAGONAL_OBSTRUCTION_BYPASSED_BY_FIXED_SWITCH_QUANTIFIER=true
X3_PHYSICAL_RECEIVER_COUNTEREXAMPLE_CONTRADICTED=false
```

---

## 16. New minimal receiver

For a top-edge residual triple `(C,u,v)`, define

```text
A(C,u,v)
 := { U=S*T : a legal physical completion exists }.             (16.1)
```

By (10.1), the remaining physical mass is

```text
B^o(1) * sum_{top-edge (C,u,v)} #A(C,u,v).                      (16.2)
```

The new receiver is

```text
TopThetaCommonCoreXiSwitchCoupledShellIncidence.                 (16.3)
```

A sufficient next theorem is

```text
sum #A(C,u,v)
 <<B^(7/8-delta+o(1))                                           (16.4)
```

for some fixed `delta>0`.

The first necessary shell is

```text
(2^a*C*oddpart(U))^2
 =(H_k^-)^2+(2*rho*N)^2,                                       (16.5)
```

and every surviving first-shell choice must also satisfy the coupled xi difference-of-squares shell (7.2).

No average scarcity of admissible `U` is proved in this stage.

---

## 17. tH / auxiliary-line decision

No new tH/H line is needed for s7-25.  The argument is exact common-core arithmetic plus elementary divisor bounds.  It uses no same-modulus character cancellation, reciprocity, large sieve or external incidence theorem.

The merged tH17 work belongs to the separate signed fixed-U coefficient space and is not cross-promoted.

```text
TH16_NEEDED_BY_S7_25=false
TH17_CROSS_PROMOTED_TO_S7_25=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false.                            (17.1)
```

If s7-26 turns (16.5) into a genuine analytic average over moving `U`, an H/tH audit should be reconsidered after that coefficient space is fixed.

---

## Stage boundary

```text
STAGE14_S7_25=COMPLETE_FIXED_RESIDUAL_XI_SWITCH_PRODUCT_RECONSTRUCTION_AND_TOP_THETA_LOCALIZATION
MERGED_S7_24_IMPORTED=true
MERGED_4CG_COMMON_CORE_IMPORTED=true
MERGED_4CI_DYADIC_SUPPORT_IMPORTED=true
MERGED_X1_CHARGED_ONCE_ADAPTER_IMPORTED=true
MERGED_4CJ_COMPATIBILITY_CHECKED=true
MERGED_4CK_COMPATIBILITY_CHECKED=true
MERGED_X3_COMPATIBILITY_CHECKED=true
XI_SWITCH_PRODUCT_DEFINED=U=S*T
XI_AGREE_PRODUCT_DEFINED=V=R*J
K_SWITCH_PRODUCT_DEFINED=M=beta*gamma
K_AGREE_PRODUCT_DEFINED=N=alpha*delta
SMALL_ROOT_DECORATION_TOTAL=B^o(1)
HK_PLUS_FIXED_BY_C_AND_U_UP_TO_DYADIC_BO1=true
HK_PYTHAGOREAN_SHELL_EXACT=true
HK_PYTHAGOREAN_SHELL=(Hk+)^2=(Hk-)^2+(2*rho*N)^2
FIXED_CUVU_V_N_MULTIPLICITY=B^o(1)
HXI_MINUS_FIXED_BY_v_AND_N_UP_TO_DYADIC_BO1=true
HXI_DIFFERENCE_OF_SQUARES_SHELL_EXACT=true
HXI_DIFFERENCE_OF_SQUARES_SHELL=(Hxi+)^2-(2*V*W)^2=(Hxi-)^2
FIXED_CUVU_M_ROOT_PRODUCT_MULTIPLICITY=B^o(1)
FIXED_ROOT_PRODUCT_QUADRUPLE_MULTIPLICITY=B^o(1)
FIXED_PRODUCT_CELL_SPLIT_MULTIPLICITY=B^o(1)
FIXED_RESIDUAL_XI_SWITCH_PRODUCT_PACKET_FIBER_BO1=true
DYADIC_XI_SWITCH_PRODUCT_SUPPORT_EXPONENT=3/4-2*phi
DYADIC_PHYSICAL_PACKET_BOUND_EXPONENT=2*theta+1/4
DYADIC_BLOCK_POWER_SAVING_FOR_THETA_BELOW_TOP=true
TOP_THETA_BARRIER=theta=5/16
TOP_THETA_ALLOWED_PHI_INTERVAL=[3/16,1/4]
TOP_THETA_COMMON_CORE_XI_SWITCH_COUPLED_SHELL_INCIDENCE_REQUIRED=true
TOP_THETA_COMMON_CORE_XI_SWITCH_COUPLED_SHELL_INCIDENCE_PROVED=false
X3_RELAXED_DIAGONAL_OBSTRUCTION_BYPASSED_BY_FIXED_SWITCH_QUANTIFIER=true
X3_PHYSICAL_RECEIVER_COUNTEREXAMPLE_CONTRADICTED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH16_NEEDED_BY_S7_25=false
TH17_CROSS_PROMOTED_TO_S7_25=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-s7-26
```