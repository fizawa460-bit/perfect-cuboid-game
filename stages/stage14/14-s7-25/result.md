# Stage14-s7-25 — fixed xi-switch-product shell reconstruction and top-theta localization

## Status

`COMPLETE_FIXED_RESIDUAL_XI_SWITCH_PRODUCT_RECONSTRUCTION_AND_TOP_THETA_LOCALIZATION`

Merged Stage14-s7-24 closes the xi short-rank geometry completely:

```text
physical xi short span rank = 1,
primitive root-line quotient defect = 1.
```

The remaining s-side problem was stated there as the multiplicity of moving balanced eight-cell packets above a fixed common-core residual triple and primitive root direction.

Stage14-s7-25 proves a stronger reconstruction statement which does **not** need to fix the primitive root direction.  Put

```text
U := Xi_switch = S*T.
```

Then, uniformly on every balanced endpoint block,

```text
fixed (C,u_res,v_res,U)
=> B^o(1) legal decorated physical packets.
```

The proof uses the exact 4cg common-core factorization twice.  The first pair of factors becomes an elementary Pythagorean shell and recovers the xi-agreement product and k-agreement product with divisor-many multiplicity.  The second pair becomes a difference-of-squares shell and recovers the k-switch product and the total physical root product with divisor-many multiplicity.  Splitting the four recovered products into individual cells and roots costs only divisor functions.

Consequently, in a dyadic `(theta,phi)` block the physical packet count is bounded by

```text
B^(2*theta+1/4+o(1)).
```

The `phi` dependence cancels.  Therefore every block with `theta<5/16` by a fixed amount is already power-saved.  The only remaining `7/8` barrier is the top-theta edge

```text
theta=5/16,
3/16 <= phi <= 1/4.
```

No whole-family fixed-power saving is promoted yet, because the complete top-theta edge may still saturate `7/8`.

---

## 1. Imported exact packet

Keep one balanced same-`(xi,k)` physical collision pair with the merged s7-20 cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta.
```

Define the four product coordinates

```text
U := S*T,                 # xi switch
V := R*J,                 # xi agreement
M := beta*gamma,          # k switch
N := alpha*delta.         # k agreement             (1.1)
```

Thus

```text
xi = U*V,
k  = M*N.                                           (1.2)
```

Merged 4cg gives one odd common core `C` and positive reduced residuals `u,v` such that

```text
q_k  = C*u,
q_xi = C*v.                                         (1.3)
```

It also gives the exact positive factors

```text
H_k^+
 = delta^2*s_1^2*s_2^2
   +alpha^2*r_1^2*r_2^2,

H_k^-
 = delta^2*s_1^2*s_2^2
   -alpha^2*r_1^2*r_2^2,

xi*C*u = H_k^+*H_k^-,                               (1.4)
```

and

```text
H_xi^+
 = J^2*y_1^2*y_2^2
   +R^2*x_1^2*x_2^2,

H_xi^-
 = J^2*y_1^2*y_2^2
   -R^2*x_1^2*x_2^2,

k*C*v = H_xi^+*H_xi^-.                              (1.5)
```

The common-core definition is

```text
C = oddpart(H_k^+/oddpart(U))
  = oddpart(H_xi^+/oddpart(M)).                     (1.6)
```

All statements below are on this same physical packet.  No independent savings are multiplied.

---

## 2. Harmless endpoint decorations

The endpoint has

```text
r_i,s_i = B^o(1),
g_i in {1,2}.                                        (2.1)
```

Hence the total number of choices of

```text
(r_1,s_1,r_2,s_2,g_1,g_2)
```

is `B^o(1)`.

Likewise every relevant 2-adic valuation is at most `O(log B)`, so choosing any finite list of such valuations costs `B^o(1)`.  Primewise orientation branches, Gaussian units, and the finite masks already present in s7-21/X1 also cost only `B^o(1)`.

We may therefore fix these harmless decorations during the reconstruction and restore them at the end.

Define

```text
rho := r_1*r_2*s_1*s_2.                              (2.2)
```

---

## 3. Fixed `(C,U)` fixes `H_k^+` up to a dyadic `B^o(1)` choice

From (1.6),

```text
oddpart(H_k^+)=C*oddpart(U).                         (3.1)
```

Thus for some nonnegative integer `a=O(log B)`,

```text
boxed:
H_k^+ = 2^a*C*oddpart(U).                            (3.2)
```

For fixed `C` and `U`, there are only `O(log B)=B^o(1)` candidates for `H_k^+`.

This is the point where fixing the **product** `U=S*T`, rather than the two cells separately, already absorbs the common-core plus factor.

---

## 4. First shell: a Pythagorean equation recovers `H_k^-` and `N=alpha*delta`

Put

```text
A = delta^2*s_1^2*s_2^2,
B = alpha^2*r_1^2*r_2^2.
```

Then

```text
H_k^+=A+B,
H_k^-=A-B.
```

Hence exactly

```text
(H_k^+)^2-(H_k^-)^2
 =4*A*B
 =4*(alpha*delta)^2*(r_1*r_2*s_1*s_2)^2.
```

Using (1.1) and (2.2),

```text
boxed:
(H_k^+)^2
 =(H_k^-)^2+(2*rho*N)^2.                            (4.1)
```

For fixed `H_k^+` and `rho`, every candidate pair `(H_k^-,N)` is a representation of the fixed square `(H_k^+)^2` as a sum of two squares.  The elementary bound

```text
r_2(n) <= 4*tau(n)                                  (4.2)
```

gives

```text
boxed:
# {(H_k^-,N)} <= B^o(1).                            (4.3)
```

No distribution theorem is used.

---

## 5. The first shell also recovers `V=R*J`

Once `H_k^-` is fixed, the factorization (1.4) becomes

```text
U*V*C*u = H_k^+*H_k^-.
```

Therefore

```text
boxed:
V
 = H_k^+*H_k^-/(U*C*u).                             (5.1)
```

So integrality and positivity either reject the candidate or determine `V` uniquely.

Combining Sections 3--5,

```text
boxed:
fixed (C,u,v,U)
=> (V,N) have B^o(1) possibilities.                 (5.2)
```

The variable `v` is not yet used; it enters the second shell.

---

## 6. Fixed `(v,N)` leaves only dyadic-many possibilities for `H_xi^-`

Write

```text
M=2^e*M_o,
M_o=oddpart(M).
```

Since the cells are squarefree and pairwise coprime, `e` is bounded absolutely; allowing the weaker `O(log B)` bound is harmless.

From (1.6), for some `b=O(log B)`,

```text
H_xi^+ = 2^b*C*M_o.                                 (6.1)
```

Use (1.5):

```text
M*N*C*v = H_xi^+*H_xi^-.
```

Cancel `C*M_o` to obtain

```text
H_xi^- = 2^(e-b)*N*v.                               (6.2)
```

The right side must be a positive integer.  Thus, after fixing `(v,N)`, the possible values of `H_xi^-` form only a dyadic list of length `O(log B)=B^o(1)`.

We do **not** need to know `M` before this step; its odd part has cancelled.

---

## 7. Second shell: difference of squares recovers `H_xi^+` and the total root product

Define the total positive physical root product

```text
W := x_1*y_1*x_2*y_2.                               (7.1)
```

From (1.5),

```text
(H_xi^+)^2-(H_xi^-)^2
 =4*R^2*J^2*x_1^2*x_2^2*y_1^2*y_2^2.
```

Hence

```text
boxed:
(H_xi^+)^2-(2*V*W)^2=(H_xi^-)^2.                   (7.2)
```

Equivalently,

```text
(H_xi^+-2*V*W)(H_xi^++2*V*W)
 =(H_xi^-)^2.                                       (7.3)
```

For fixed `H_xi^-` and `V`, every candidate `(H_xi^+,W)` comes from a factor pair of the fixed integer `(H_xi^-)^2`.  Therefore

```text
boxed:
# {(H_xi^+,W)}
 <= tau((H_xi^-)^2)
 = B^o(1),                                          (7.4)
```

up to a harmless constant for ordering/parity.  Integrality of `W` is only a rejection test.

---

## 8. The second shell recovers `M=beta*gamma`

Once `H_xi^+` and `H_xi^-` are fixed, (1.5) gives

```text
boxed:
M
 = H_xi^+*H_xi^-/(N*C*v).                           (8.1)
```

Again positivity, integrality, the common-core odd-part identity, and the dyadic window are only rejection tests.

Thus

```text
boxed:
fixed (C,u,v,U)
=> (V,N,M,W) have B^o(1) possibilities.             (8.2)
```

---

## 9. Split the recovered products

The four cell products satisfy

```text
S*T=U,
R*J=V,
beta*gamma=M,
alpha*delta=N.                                      (9.1)
```

The number of ordered positive splits is at most

```text
tau(U)*tau(V)*tau(M)*tau(N)=B^o(1).                 (9.2)
```

Squarefreeness, pairwise coprimality, balanced dyadic sizes, the placement of the prime `2`, and all physical masks only reduce this list.

Likewise, from

```text
x_1*y_1*x_2*y_2=W,
```

the number of ordered positive root quadruples is the four-fold divisor function

```text
d_4(W)=B^o(1).                                      (9.3)
```

For every surviving split, the cells and roots reconstruct

```text
a_1=R*S,
b_1=T*J,
a_2=R*T,
b_2=S*J,

P_1=a_1*x_1^2,
Q_1=b_1*y_1^2,
P_2=a_2*x_2^2,
Q_2=b_2*y_2^2.                                      (9.4)
```

The fixed small variables `(r_i,s_i,g_i)` and all exact `k` identities then act only as consistency tests.

---

## 10. Fixed residual triple plus xi-switch product has `B^o(1)` packet fiber

Multiplying the divisor-many choices in Sections 2--9 yields the uniform theorem

```text
boxed:
# {
  legal decorated physical endpoint packets
  with fixed (C,u,v,U=S*T)
 }
 <= B^o(1).                                         (10.1)
```

Equivalently,

```text
FIXED_RESIDUAL_XI_SWITCH_PRODUCT_PACKET_FIBER_BO1=true. (10.2)
```

This is stronger than the first s7-24 target in one important sense: it does not fix the primitive root direction `X`.  The root product and then the full root quadruple are reconstructed inside the fiber.

Merged X1 guarantees that retaining the common-core and CRT labels is a charged-once refinement of the same physical pair.  No hypothetical common-core saving and CRT saving have been multiplied independently.

---

## 11. Dyadic support of `U=S*T`

Use the merged balanced parameterization

```text
R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)).                             (11.1)
```

Therefore

```text
boxed:
U=S*T = B^(3/4-2*phi+o(1)).                         (11.2)
```

The number of possible integer values of `U` in one dyadic block is at most

```text
boxed:
B^(3/4-2*phi+o(1)).                                 (11.3)
```

This is a raw support count, not an independence factor: by (10.1), each fixed `(C,u,v,U)` is charged only `B^o(1)` physical packets.

---

## 12. Unconditional dyadic packet bound

Merged 4ci gives, in the same `(theta,phi)` block, the residual-triple support

```text
# {(C,u,v)}
 <= B^(2*theta+2*phi-1/2+o(1)).                     (12.1)
```

Combine (10.1), (11.3), and (12.1):

```text
physical packet mass in the block
 <= B^o(1)
    * B^(2*theta+2*phi-1/2)
    * B^(3/4-2*phi).
```

Hence

```text
boxed:
E_{theta,phi}
 <= B^(2*theta+1/4+o(1)).                           (12.2)
```

The `phi` dependence cancels exactly.

This is now an **unconditional** bound, not the conditional fixed-`X` ledger of s7-24.

---

## 13. All blocks below the top-theta edge are power-saved

The balanced window has

```text
3/16 <= theta <= 5/16.                              (13.1)
```

Subtract (12.2) from the current `7/8` exponent:

```text
7/8-(2*theta+1/4)
 =2*(5/16-theta).                                   (13.2)
```

Therefore for every fixed `epsilon>0`,

```text
theta <= 5/16-epsilon
```

implies

```text
boxed:
E_{theta,phi}
 <= B^(7/8-2*epsilon+o(1)).                         (13.3)
```

So every block separated by a fixed amount from the top theta boundary already has a fixed-power saving.

---

## 14. The actual surviving `7/8` barrier is a top-theta edge

At

```text
theta=5/16,
```

(12.2) becomes exactly

```text
2*(5/16)+1/4=7/8.                                   (14.1)
```

The common-core strip is

```text
0<=theta-phi<=1/8,
theta+phi>=3/8.                                     (14.2)
```

Thus on the top theta boundary the allowed phi interval is

```text
boxed:
3/16 <= phi <= 1/4.                                 (14.3)
```

So s7-24's **conditional unique corner** is superseded by the proved reconstruction ledger:

```text
old conditional saturation set:
  one corner (5/16,1/4) after assuming fixed-X fiber B^o(1);

new unconditional saturation set:
  the top-theta edge theta=5/16, 3/16<=phi<=1/4.     (14.4)
```

This is not a regression.  The old corner statement depended on paying the full raw root-direction support `B^(1/4)`.  The new theorem reconstructs the roots and instead pays the xi-switch-product support.  It proves saving off the top-theta edge without assuming the missing fixed-X fiber theorem.

---

## 15. New minimal receiver on the top edge

For a fixed top-edge residual triple `(C,u,v)`, define the admissible xi-switch set

```text
A(C,u,v)
 := {
      U=S*T:
      there exists a legal balanced physical completion
      satisfying the two shell equations (4.1) and (7.2)
    }.                                               (15.1)
```

Because the fiber over fixed `(C,u,v,U)` is `B^o(1)`, the remaining top-edge physical mass is charged by

```text
B^o(1) * sum_{top-edge (C,u,v)} #A(C,u,v).          (15.2)
```

The new receiver is

```text
TopThetaCommonCoreXiSwitchCoupledShellIncidence.     (15.3)
```

A sufficient theorem is

```text
sum_{top-edge (C,u,v)} #A(C,u,v)
 << B^(7/8-delta+o(1))                              (15.4)
```

for some fixed `delta>0`.

Equivalently, one needs fixed-power scarcity of admissible `U` values relative to their raw interval on the top-theta edge.  The first shell is a Pythagorean hypotenuse condition

```text
(2^a*C*oddpart(U))^2
 =(H_k^-)^2+(2*rho*N)^2,                            (15.5)
```

and every surviving first-shell choice must also pass the second coupled difference-of-squares shell (7.2).

No such average incidence theorem is claimed in s7-25.

---

## 16. Relation to merged 4cj and toolbox guard

Merged 4cj independently proves the same xi rank-one physical rigidity as s7-24 and records multiplicity one inside a fixed oriented xi-CRT packet.  It is fully compatible with (10.1).

The toolbox-av guard forbids multiplying hypothetical common-core and dual-CRT savings.  Stage14-s7-25 does not do so: X1 supplies the legal charged-once common refinement, and (10.1) is a direct reconstruction theorem on that common physical coefficient space.

```text
MERGED_4CJ_COMPATIBILITY_CHECKED=true
TOOLBOX_AV_INDEPENDENT_SAVINGS_GUARD_RESPECTED=true
```

---

## 17. tH / auxiliary-line decision

No new tH/H stage is required for s7-25.

The proof uses only

```text
- merged exact 4cg common-core factorizations,
- merged 4ci dyadic support and normalized coefficient space,
- merged X1 charged-once adapter,
- the elementary sum-of-two-squares representation bound,
- elementary factor-pair/divisor bounds,
- endpoint B^o(1) small-variable and orientation costs.        (17.1)
```

No same-modulus character cancellation, large sieve, reciprocity, or external incidence theorem is invoked.

The existing tH16/tH17 work belongs to the separate fixed-U signed coefficient space and is not cross-promoted here.

```text
TH16_NEEDED_BY_S7_25=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false.                (17.2)
```

If Stage14-s7-26 turns (15.5) into a genuine analytic average over moving `U`, an H/tH audit should be reconsidered only after that coefficient space is fixed exactly.

---

## 18. Quantitative ledger

For one dyadic block:

```text
residual support exponent
 =2*theta+2*phi-1/2,

xi-switch-product support exponent
 =3/4-2*phi,

fixed residual + U packet fiber
 =o(1),

physical packet exponent
 =2*theta+1/4.                                      (18.1)
```

Gap below `7/8`:

```text
7/8-(2*theta+1/4)
 =2*(5/16-theta).                                   (18.2)
```

Top edge:

```text
theta=5/16,
3/16<=phi<=1/4,
physical exponent=7/8.                              (18.3)
```

The whole-family theorem therefore remains

```text
V(B) << B^(7/8+o(1)).                               (18.4)
```

but all fixed-distance off-top-theta blocks are now power-saved.

---

## Stage boundary

```text
STAGE14_S7_25=COMPLETE_FIXED_RESIDUAL_XI_SWITCH_PRODUCT_RECONSTRUCTION_AND_TOP_THETA_LOCALIZATION
MERGED_S7_24_IMPORTED=true
MERGED_4CG_COMMON_CORE_IMPORTED=true
MERGED_4CI_DYADIC_SUPPORT_IMPORTED=true
MERGED_X1_CHARGED_ONCE_ADAPTER_IMPORTED=true
MERGED_4CJ_COMPATIBILITY_CHECKED=true
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
TOOLBOX_AV_INDEPENDENT_SAVINGS_GUARD_RESPECTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
TH16_NEEDED_BY_S7_25=false
S_AUXILIARY_SUPERVISOR_LINE_CREATED=false
S_ROUTE_BLOCKED_WAITING_FOR_TH=false
NEXT=Stage14-s7-26
```