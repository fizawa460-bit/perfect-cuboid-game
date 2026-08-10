# Stage14-4cm — quadratic-branch elimination and residual linear factor-pair collapse

## Status

`COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_RESIDUAL_LINEAR_FACTOR_PAIR_COLLAPSE`

This stage consumes merged `14-4cl`, `s7-25`, and `X4`, and reuses the exact common-core identities of merged `14-4cg`.

The key new fact is stronger than the `-,+,i` three-way cyclotomic decomposition retained in 4cl.  On every physical packet,

```text
oddpart(H_k^-)=oddpart(R*J)*oddpart(u_res),
oddpart(H_xi^-)=oddpart(alpha*delta)*oddpart(v_res).
```

Since

```text
H_k^-=(D-A)(D+A),
H_xi^-=(V-U)(V+U),
```

every odd agreement prime already lies in a linear factor.  Hence the two formal quadratic `i` branches are empty.  The nine 4cl dominant types reduce to four sign pairs, and even those signs only record which of two simultaneous linear factors is larger.

Moreover, after dividing the linear factors by their agreement moduli, the two quotient products are exactly the fixed reduced residuals `u_res` and `v_res` in odd part.  Thus fixed residual data leave only `B^o(1)` quotient decorations.

The remaining mainline object is no longer a generic binary-quartic energy.  It is a pair of coupled reciprocal difference-of-squares equations in four linear branch moduli.

The unconditional whole-family exponent remains

```text
V(B) << B^(7/8+o(1)).
```

Merged `s7-25` additionally localizes the unsaved region to the top-theta edge

```text
theta=5/16,
3/16<=phi<=1/4.
```

No statement from an open PR is used.

---

## 1. Imported notation

Put

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y,
```

with

```text
r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,
D>A>0,
V>U>0.
```

Merged 4cg gives

```text
q_k=C*u_res,
q_xi=C*v_res,
```

where `C` is odd, and

```text
xi*q_k=H_k^+*H_k^-,
k*q_xi=H_xi^+*H_xi^-,
```

with

```text
H_k^+=D^2+A^2,
H_k^-=D^2-A^2,
H_xi^+=V^2+U^2,
H_xi^-=V^2-U^2.
```

The plus-factor common-core definition is

```text
oddpart(H_k^+)=C*oddpart(S*T),
oddpart(H_xi^+)=C*oddpart(beta*gamma).                (1.1)
```

All reductions below remain on the same charged-once physical packet.

---

## 2. Exact minus-factor identities

Taking odd parts in

```text
(RJ)(ST)(C*u_res)=H_k^+H_k^-
```

and using (1.1), cancel `C*oddpart(ST)` to obtain

```text
boxed:
oddpart(H_k^-)=oddpart(RJ)*oddpart(u_res).            (2.1)
```

Likewise

```text
boxed:
oddpart(H_xi^-)
 =oddpart(alpha*delta)*oddpart(v_res).                 (2.2)
```

Thus

```text
boxed:
oddpart(RJ) | D^2-A^2,                                (2.3)

boxed:
oddpart(alpha*delta) | V^2-U^2.                       (2.4)
```

These are exact factor identities, not density bounds.

---

## 3. The quadratic cyclotomic branches vanish

Use the 4cl definitions

```text
M_xi^- = gcd(oddpart(RJ),D-A),
M_xi^+ = gcd(oddpart(RJ),D+A),
M_xi^i = gcd(oddpart(RJ),D^2+A^2),
```

and similarly

```text
M_k^- = gcd(oddpart(alpha*delta),V-U),
M_k^+ = gcd(oddpart(alpha*delta),V+U),
M_k^i = gcd(oddpart(alpha*delta),V^2+U^2).
```

Merged 4cl gives the opposite-base coprimalities

```text
gcd(oddpart(RJ),A*D)=1,
gcd(oddpart(alpha*delta),U*V)=1.
```

An odd `p|RJ` already divides `D^2-A^2`.  If it also divided `D^2+A^2`, then it would divide both `2D^2` and `2A^2`, contradicting `p∤AD`.  Hence

```text
boxed:
M_xi^i=1,
M_xi^-*M_xi^+=oddpart(RJ).                            (3.1)
```

The same argument gives

```text
boxed:
M_k^i=1,
M_k^-*M_k^+=oddpart(alpha*delta).                     (3.2)
```

Therefore the physical cyclotomic allocation is exactly two-way linear on both sides.  No Gaussian/quadratic branch survives to be estimated.

---

## 4. Quotient pairs are fixed-residual factor pairs

Define

```text
e_xi^- = oddpart(D-A)/M_xi^-,
e_xi^+ = oddpart(D+A)/M_xi^+,

e_k^-  = oddpart(V-U)/M_k^-,
e_k^+  = oddpart(V+U)/M_k^+.
```

From (2.1) and (3.1),

```text
boxed:
e_xi^-*e_xi^+=oddpart(u_res).                        (4.1)
```

From (2.2) and (3.2),

```text
boxed:
e_k^-*e_k^+=oddpart(v_res).                          (4.2)
```

Hence, for fixed `(C,u_res,v_res)`, the odd quotient tuple has at most

```text
tau(oddpart(u_res))*tau(oddpart(v_res))=B^o(1)
```

choices.  The 2-primary valuations of the four linear factors contribute only `O(log B)^{O(1)}=B^o(1)` further choices.

After conditioning this harmless data, write full positive quotients

```text
D-A=a_-*m_-,
D+A=a_+*m_+,
V-U=b_-*n_-,
V+U=b_+*n_+,                                          (4.3)
```

where

```text
m_-=M_xi^-, m_+=M_xi^+,
n_-=M_k^-,  n_+=M_k^+.
```

The coefficient tuple `(a_-,a_+,b_-,b_+)` ranges over only `B^o(1)` possibilities for fixed residual data.

---

## 5. Linear-modulus strength on the merged top-theta barrier

Because the `i` branches vanish,

```text
max(m_-,m_+) >= oddpart(RJ)^(1/2)=B^(phi-o(1)),
max(n_-,n_+) >= oddpart(alpha*delta)^(1/2)=B^(theta-o(1)). (5.1)
```

Merged s7-25 leaves only

```text
theta=5/16,
3/16<=phi<=1/4.                                      (5.2)
```

On this edge,

```text
D,A=B^(5/16+o(1)),
V,U=B^(phi+1/8+o(1)).
```

Therefore the quotient attached to a dominant xi-linear modulus has exponent at most

```text
5/16-phi,
```

while the quotient attached to a dominant k-linear modulus has exponent at most

```text
phi+1/8-5/16 = phi-3/16.
```

Their sum is identically

```text
boxed:
(5/16-phi)+(phi-3/16)=1/8.                           (5.3)
```

At the old 4cl corner `phi=1/4`, both are at most `B^(1/16+o(1))` and the dominant moduli improve to

```text
xi: B^(1/4-o(1)),
k:  B^(5/16-o(1)).                                   (5.4)
```

These box bounds are diagnostic; Section 4 is stronger because fixed residual data already make the quotient decoration divisor-many.

---

## 6. Exact coupled difference-of-squares system

From (4.3),

```text
2D=a_-m_-+a_+m_+,
2A=a_+m_+-a_-m_-,                                   (6.1)

2V=b_-n_-+b_+n_+,
2U=b_+n_+-b_-n_-.                                   (6.2)
```

Let

```text
epsilon_k  =2^v2(alpha*delta) in {1,2},
epsilon_xi =2^v2(RJ)          in {1,2}.
```

Since the cells are squarefree and pairwise coprime inside each family,

```text
alpha*delta=epsilon_k*n_-*n_+,
R*J=epsilon_xi*m_-*m_+.                             (6.3)
```

Subtracting squares in (6.1) gives

```text
boxed:
(a_+m_+)^2-(a_-m_-)^2
 =4*epsilon_k*r*s*n_-*n_+.                          (6.4)
```

Likewise

```text
boxed:
(b_+n_+)^2-(b_-n_-)^2
 =4*epsilon_xi*X*Y*m_-*m_+.                         (6.5)
```

Conversely, a legal solution of (6.4)-(6.5), together with the conditioned quotient/2-primary data, reconstructs

```text
A,D,U,V
```

from (6.1)-(6.2), hence candidate

```text
alpha=A/r,
delta=D/s,
R=U/X,
J=V/Y.
```

All original physical masks only discard candidates.

Thus the post-4cl receiver reduces at `B^o(1)` cost to the solution count of (6.4)-(6.5).

---

## 7. New minimal receiver

Define

```text
CoupledResidualLinearFactorPairDifferenceSquareIncidence
```

to count legal positive squarefree/coprime quadruples

```text
(m_-,m_+,n_-,n_+)
```

satisfying (6.4)-(6.5) after fixing

```text
(C,u_res,v_res),
primitive physical root line,
endpoint-small roots,
2-primary pattern,
one divisor-pair decoration of u_res and v_res.
```

Then

```text
boxed:
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
 <= B^o(1)
    * CoupledResidualLinearFactorPairDifferenceSquareIncidence. (7.1)
```

The algebraic chain is now

```text
binary quartic agreement
 -> reciprocal fourth-difference allocation
 -> exact linear two-way allocation
 -> fixed-residual quotient pairs
 -> coupled reciprocal difference-of-squares.        (7.2)
```

A generic binary-quartic energy theorem is no longer the correct target.

---

## 8. Compatibility with merged s7-25 and X4

Merged s7-25 proves the independent quantifier-order theorem

```text
fixed (C,u_res,v_res,S*T)
=> decorated physical packet fiber <= B^o(1),
```

and the block bound

```text
E(theta,phi) << B^(2theta+1/4+o(1)).
```

This localizes the remaining barrier to (5.2).  Stage14-4cm does not reprove that theorem; it supplies a different structural reduction of the surviving top-theta packets.

Merged X4 independently aligns the X-route with 4cl's physical proportional-branch elimination.  4cm preserves that off-proportional guard and further removes the formal quadratic cyclotomic branches.  There is no conflict or double charging.

---

## 9. What remains open

Closed in 4cm:

```text
COMMON_CORE_MINUS_ODD_FACTOR_IDENTITY_PROVED=true
XI_CYCLOTOMIC_I_BRANCH=1
K_CYCLOTOMIC_I_BRANCH=1
XI_LINEAR_ALLOCATION_PRODUCT=oddpart(RJ)
K_LINEAR_ALLOCATION_PRODUCT=oddpart(alpha*delta)
XI_LINEAR_QUOTIENT_PRODUCT=oddpart(u_res)
K_LINEAR_QUOTIENT_PRODUCT=oddpart(v_res)
FIXED_RESIDUAL_LINEAR_QUOTIENT_DECORATION_COST=Bo1
RECIPROCAL_COUPLED_DIFFERENCE_SQUARE_SYSTEM_PROVED=true
```

Still open:

```text
COUPLED_RESIDUAL_LINEAR_FACTOR_PAIR_DIFFERENCE_SQUARE_INCIDENCE_PROVED=false
TOP_THETA_EDGE_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
```

Therefore

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8.
```

---

## 10. H-line decision

No external theorem is needed for Stage14-4cm.

The planned 4cl branchwise audit has shown that the Gaussian/quadratic branch is not live and that the generic quartic equal-value problem was too broad.  The surviving system (6.4)-(6.5) is an exact coupled arithmetic system with divisor-bounded residual coefficients.

Stage14-4cn should first attack it by primitive gcd decomposition, cross multiplication, and factor-pair reconstruction.  Only if a genuinely positive-dimensional average incidence survives that exact attack should a mainline H audit be opened.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
```

---

## Stage boundary

```text
STAGE14_4CM=COMPLETE_QUADRATIC_BRANCH_ELIMINATION_AND_RESIDUAL_LINEAR_FACTOR_PAIR_COLLAPSE
MERGED_4CL_IMPORTED=true
MERGED_S7_25_IMPORTED=true
MERGED_X4_IMPORTED=true
MERGED_4CG_COMMON_CORE_REUSED=true
COMMON_CORE_MINUS_ODD_FACTOR_IDENTITY_PROVED=true
ODD_HK_MINUS=oddpart(RJ)*oddpart(u_res)
ODD_HXI_MINUS=oddpart(alpha*delta)*oddpart(v_res)
XI_CYCLOTOMIC_I_BRANCH=1
K_CYCLOTOMIC_I_BRANCH=1
XI_LINEAR_ALLOCATION_PRODUCT=oddpart(RJ)
K_LINEAR_ALLOCATION_PRODUCT=oddpart(alpha*delta)
XI_LINEAR_QUOTIENT_PRODUCT=oddpart(u_res)
K_LINEAR_QUOTIENT_PRODUCT=oddpart(v_res)
FIXED_RESIDUAL_LINEAR_QUOTIENT_DECORATION_COST=Bo1
TOP_THETA_EDGE=theta=5/16,3/16<=phi<=1/4
TOP_THETA_DOMINANT_QUOTIENT_EXPONENT_SUM_MAX=1/8
EXTREME_CORNER_XI_DOMINANT_LINEAR_EXPONENT=1/4
EXTREME_CORNER_K_DOMINANT_LINEAR_EXPONENT=5/16
EXTREME_CORNER_XI_DOMINANT_QUOTIENT_EXPONENT_MAX=1/16
EXTREME_CORNER_K_DOMINANT_QUOTIENT_EXPONENT_MAX=1/16
EXTREME_CORNER_DOMINANT_BRANCH_TYPE_COUNT=4
RECIPROCAL_COUPLED_DIFFERENCE_SQUARE_SYSTEM_PROVED=true
COUPLED_RESIDUAL_LINEAR_FACTOR_PAIR_DIFFERENCE_SQUARE_INCIDENCE_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_BINARY_QUARTIC_ENERGY_H_REQUESTED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cn attack CoupledResidualLinearFactorPairDifferenceSquareIncidence by primitive gcd decomposition, cross multiplication, and factor-pair reconstruction before deciding whether an external H theorem is genuinely needed
```
