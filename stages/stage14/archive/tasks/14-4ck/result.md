# Stage14-4ck — eliminate switch products and reduce the cell fiber to binary-quartic agreement incidence

## Status

`COMPLETE_SWITCH_PRODUCT_ELIMINATION_AND_BINARY_QUARTIC_AGREEMENT_REDUCTION`

Merged Stage14-4cj and Stage14-s7-24 collapse the physical `xi` short-vector geometry to one primitive saturated line. Merged Stage14-4ci supplies the common-core residual packet, full `k`-side saturation, and the normalized four-host equations.

Stage14-4ck removes the remaining switched-cell products from the mainline counting variables.

For fixed residual data

```text
q_k=C*u_res,
q_xi=C*v_res,
```

and a fixed primitive physical root direction

```text
X_root=(x_1,y_1,x_2,y_2),
```

the endpoint-small variables `r_i,s_i` and the finite `g_i in {1,2}` contribute only `B^o(1)` possibilities. After fixing them, every physical eight-cell packet is controlled by the four agreement cells

```text
(alpha,delta,R,J)
```

satisfying one exact binary-quartic value equation. The switched products

```text
beta*gamma,
S*T
```

are then determined exactly, and splitting those products into the two switched cells costs only divisor functions.

Thus the live mainline receiver is no longer an eight-cell incidence. It is a four-agreement-cell quartic incidence.

No whole-family fixed-power saving is promoted in this stage. The unconditional exponent remains

```text
V(B) << B^(7/8+o(1)).
```

---

## 1. Imported exact balanced packet

Use the balanced cells

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta,
```

with

```text
Xi_agree = R*J,
Xi_switch = S*T,
K_agree = alpha*delta,
K_switch = beta*gamma.
```

The physical roots satisfy

```text
x_i,y_i ~ B^(1/16),
r_i,s_i=B^o(1),
g_i in {1,2}.
```

Put

```text
r = r_1*r_2,
s = s_1*s_2,
X = x_1*x_2,
Y = y_1*y_2.
```

Merged 4cg/4ch give

```text
H_k^+  = delta^2*s^2 + alpha^2*r^2,
H_k^-  = delta^2*s^2 - alpha^2*r^2 > 0,

H_xi^+ = J^2*Y^2 + R^2*X^2,
H_xi^- = J^2*Y^2 - R^2*X^2 > 0,
```

and the exact residual products

```text
xi*q_k = H_k^+ H_k^-,
k*q_xi = H_xi^+ H_xi^-.
```

The exact plus-factor cross coupling is

```text
g_1*g_2*K_switch*H_k^+
 = 2*Xi_switch*H_xi^+.
```

All finite 2-primary conventions are regarded as fixed in what follows.

---

## 2. A complementary minus-factor cross identity

The plus identity is not the only useful cross coupling. Write

```text
G=g_1*g_2.
```

From

```text
xi = Xi_agree*Xi_switch,
k  = K_agree*K_switch,
```

and the two residual-product identities,

```text
Xi_switch
 = H_k^+ H_k^-/(q_k*Xi_agree),

K_switch
 = H_xi^+ H_xi^-/(q_xi*K_agree).
```

Substitute these expressions into

```text
G*K_switch*H_k^+ = 2*Xi_switch*H_xi^+
```

and cancel the positive factors `H_k^+ H_xi^+`. This gives the exact complementary identity

```text
boxed:
G*q_k*Xi_agree*H_xi^-
 = 2*q_xi*K_agree*H_k^-.                            (2.1)
```

Equivalently,

```text
boxed:
G*q_k*R*J*(J^2*Y^2-R^2*X^2)
 = 2*q_xi*alpha*delta*(delta^2*s^2-alpha^2*r^2).    (2.2)
```

This identity contains only the four agreement cells once the residual datum, root direction, and endpoint-small roots are fixed.

```text
COMPLEMENTARY_MINUS_FACTOR_CROSS_IDENTITY_PROVED=true
```

---

## 3. The two switched products are determined by the agreement cells

For any candidate agreement quadruple `(alpha,delta,R,J)`, define

```text
Xi_switch_candidate
 := H_k^+ H_k^-/(q_k*R*J),                           (3.1)

K_switch_candidate
 := H_xi^+ H_xi^-/(q_xi*alpha*delta).                (3.2)
```

Every physical packet must have these quantities integral and satisfy

```text
boxed:
S*T = Xi_switch_candidate,                           (3.3)

boxed:
beta*gamma = K_switch_candidate.                    (3.4)
```

Thus the switched products are not independent moving variables after the agreement cells have been chosen.

Because the cells inside each family are pairwise coprime and squarefree, the number of ordered factorizations

```text
S*T -> (S,T),
beta*gamma -> (beta,gamma)
```

is bounded by

```text
tau(S*T)*tau(beta*gamma)=B^o(1).                    (3.5)
```

The balanced dyadic ranges, switch/agreement designation, primewise residue locks, and 2-primary conventions only discard or `B^o(1)`-refine these choices.

Hence

```text
fixed agreement quadruple
=> switched-cell completion multiplicity B^o(1).    (3.6)
```

This is a genuine quantifier reduction:

```text
8 moving cells -> 4 agreement cells + B^o(1) completion.
```

---

## 4. Binary-quartic normal form

Define the split binary quartic

```text
F(a,b)
 := a*b*(b^2-a^2)
  = a*b*(b-a)*(b+a).                                (4.1)
```

Now put

```text
A = alpha*r,
D = delta*s,
U = R*X,
V = J*Y.                                             (4.2)
```

Then

```text
H_k^-  = D^2-A^2,
H_xi^- = V^2-U^2,
```

while

```text
alpha*delta = A*D/(r*s),
R*J         = U*V/(X*Y).
```

Multiplying (2.2) by `r*s*X*Y` and cancelling the fixed products gives

```text
boxed:
G*q_k*r*s * F(U,V)
 = 2*q_xi*X*Y * F(A,D).                             (4.3)
```

In original variables,

```text
boxed:
(g_1*g_2)*q_k*(r_1*r_2)*(s_1*s_2)
  * F(R*x_1*x_2, J*y_1*y_2)
=
2*q_xi*(x_1*x_2)*(y_1*y_2)
  * F(alpha*r_1*r_2, delta*s_1*s_2).                (4.4)
```

The physical positivity conditions are exactly

```text
D>A>0,
V>U>0.                                               (4.5)
```

Thus the remaining cell problem is an equal-value problem for the same completely split quartic form on two differently scaled primitive/squarefree coefficient families.

```text
BINARY_QUARTIC_AGREEMENT_EQUATION_PROVED=true
BINARY_QUARTIC_FORM=F(a,b)=a*b*(b-a)*(b+a)
```

---

## 5. Endpoint-small variables cost only B^o(1)

The root direction `X_root` fixes `x_i,y_i`. The endpoint theorem gives

```text
r_i,s_i=B^o(1),
g_i in {1,2}.
```

For every fixed dyadic epsilon used in the Stage14 endpoint decomposition, the number of integer tuples

```text
(r_1,r_2,s_1,s_2,g_1,g_2)
```

is `B^o(1)`.

Therefore these variables can be conditioned before counting (4.4), at subpolynomial cost.

The same is true of the primewise orientation decoration after merged 4ci/s7-24 full-line saturation: once a cell and the primitive physical line are fixed, the legal orientation is forced up to the existing `B^o(1)` refinement.

No orientation density is multiplied into the quartic count.

---

## 6. Exact cell-fiber reduction

For fixed

```text
(C,u_res,v_res),
X_root=(x_1,y_1,x_2,y_2),
```

define

```text
A_4(C,u_res,v_res;X_root)
```

to be the set of quadruples

```text
(alpha,delta,R,J)
```

in the balanced agreement-cell ranges for which there exists one endpoint-small tuple `(r_i,s_i,g_i)` satisfying (4.4), and for which (3.1)-(3.2) are positive integers admitting legal squarefree coprime splits into `(S,T)` and `(beta,gamma)`.

Then merged 4ch/X1 and Sections 3--5 give

```text
boxed:
# physical decorated packets over fixed
(C,u_res,v_res,X_root)
<= B^o(1) * #A_4(C,u_res,v_res;X_root).              (6.1)
```

Every physical pair is charged once after the canonical cell and root conventions are fixed.

The new minimal receiver is therefore

```text
CommonCoreBinaryQuarticAgreementIncidence.           (6.2)
```

A sufficient pointwise theorem would be

```text
#A_4(C,u_res,v_res;X_root) <= B^o(1),                (6.3)
```

but 4ck does **not** assert (6.3).

More generally an average fixed-power saving for (6.2), concentrated near the extreme corner if necessary, is sufficient for a whole-family exponent improvement.

---

## 7. Relation to the dyadic exponent ledger

Merged 4ci gives residual-triple support in a fixed `(theta,phi)` block

```text
B^(2*(theta+phi)-1/2+o(1)).                          (7.1)
```

Merged s7-24 gives the raw primitive root-direction support exponent `1/4`. If the quartic agreement fiber (6.3) were `B^o(1)`, the resulting conditional exponent would be

```text
2*(theta+phi)-1/4.                                   (7.2)
```

The only block where this reaches `7/8` is

```text
(theta,phi)=(5/16,1/4).                              (7.3)
```

Therefore any future quartic argument may focus its sharpest work on that extreme corner. Away from that corner, the target has a fixed dyadic margin once the quartic fiber is controlled.

This observation is conditional on controlling (6.2); it is not promoted to a new unconditional exponent in 4ck.

---

## 8. Why a divisor bound has not yet closed the quartic incidence

The quartic form factors completely:

```text
F(a,b)=a*b*(b-a)*(b+a).
```

For a **fixed value** `N`, the number of primitive representations `F(a,b)=N` is divisor-controlled after allocating the four near-coprime factors.

However (4.4) is not a fixed-value equation. Both quartic values move together:

```text
c_1 F(U,V)=c_2 F(A,D),                               (8.1)
```

with fixed coefficients `c_1,c_2` only after the residual/root/small data are conditioned.

Applying the divisor bound separately after fixing one side merely charges every candidate on that side and gives no automatic fixed-power saving. Thus the invalid shortcut

```text
split quartic + divisor bound => B^o(1) total fiber
```

is explicitly rejected.

The remaining issue is a genuine equal-value / multiplicative-energy problem with strong squarefree, coprimality, dyadic, and switch-product-integrality constraints.

---

## 9. H-line decision

Stage14-4ck itself uses only exact algebra, the already merged divisor-bound completions, and endpoint bookkeeping.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
```

No external quartic-incidence theorem is imported here.

The next stage should first exploit the complete factorization

```text
F(a,b)=a*b*(b-a)*(b+a)
```

together with the pairwise-coprime squarefree agreement cells and the exact integrality conditions (3.1)-(3.2). A mainline H audit becomes justified only if that exact factor-allocation attack leaves a genuine average quartic-energy estimate requiring an external theorem.

The fixed-U `tH17` request from the parallel t-route is on a different coefficient space and is not imported into this mainline receiver.

---

## 10. What is closed and what remains open

Closed in 4ck:

```text
- complementary minus-factor cross identity;
- exact recovery of S*T from agreement cells;
- exact recovery of beta*gamma from agreement cells;
- divisor-many split completion of the switched products;
- reduction of the fixed residual/root cell fiber to four agreement cells;
- exact common binary-quartic value equation.
```

Still open:

```text
COMMON_CORE_BINARY_QUARTIC_AGREEMENT_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
```

The unconditional whole-family endpoint remains

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

---

## Stage boundary

```text
STAGE14_4CK=COMPLETE_SWITCH_PRODUCT_ELIMINATION_AND_BINARY_QUARTIC_AGREEMENT_REDUCTION
MERGED_4CJ_IMPORTED=true
MERGED_S7_24_IMPORTED=true
MERGED_4CI_IMPORTED=true
MERGED_X1_CHARGE_ADAPTER_IMPORTED=true
COMPLEMENTARY_MINUS_FACTOR_CROSS_IDENTITY_PROVED=true
SWITCH_XI_PRODUCT_ST_RECOVERED_FROM_AGREEMENT_CELLS=true
SWITCH_K_PRODUCT_BETA_GAMMA_RECOVERED_FROM_AGREEMENT_CELLS=true
SWITCH_PRODUCT_SPLIT_COMPLETION_MULTIPLICITY=Bo1
EIGHT_CELL_FIBER_REDUCED_TO_FOUR_AGREEMENT_CELLS=true
BINARY_QUARTIC_AGREEMENT_EQUATION_PROVED=true
BINARY_QUARTIC_FORM=F(a,b)=a*b*(b-a)*(b+a)
COMMON_CORE_BINARY_QUARTIC_AGREEMENT_INCIDENCE_PROVED=false
FIXED_RESIDUAL_ROOT_AGREEMENT_QUARTIC_FIBER_BO1_PROVED=false
UNIQUE_CONDITIONAL_7_8_SATURATION_CORNER=(theta,phi)=(5/16,1/4)
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cl attack the split quartic agreement equation by prime-factor allocation, gcd structure, and the switch-product integrality constraints; start a mainline H audit only if a genuine external quartic-energy theorem remains after that exact attack
```
